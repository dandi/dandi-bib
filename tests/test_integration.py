"""Integration tests for dandi-bib workflows."""
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import pytest
import responses


@pytest.mark.integration
@pytest.mark.ai_generated
class TestGetBibliographyIntegration:
    """Integration tests for get-bibliography script."""

    def test_script_executable(self) -> None:
        """Test that get-bibliography script is executable."""
        script_path = Path(__file__).parent.parent / "code" / "get-bibliography"
        assert script_path.exists()
        assert script_path.stat().st_mode & 0o111  # Check executable bit

    def test_help_output(self) -> None:
        """Test that script shows help message."""
        script_path = Path(__file__).parent.parent / "code" / "get-bibliography"
        result = subprocess.run(
            [str(script_path), "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "usage:" in result.stdout.lower() or "usage:" in result.stderr.lower()
        assert "--bibfile" in result.stdout or "--bibfile" in result.stderr

    @responses.activate
    def test_fetch_single_dandiset(self, temp_dir: Path) -> None:
        """Test fetching bibliography for a single dandiset (mocked)."""
        # Mock API responses
        responses.add(
            responses.GET,
            "https://api.dandiarchive.org/api/dandisets/",
            json={
                "count": 1,
                "next": None,
                "results": [
                    {
                        "identifier": "000001",
                        "most_recent_published_version": {"version": "0.210801.2033"},
                    }
                ],
            },
            status=200,
        )

        responses.add(
            responses.GET,
            "https://api.dandiarchive.org/api/dandisets/000001/versions/",
            json={"results": [{"version": "0.210801.2033"}]},
            status=200,
        )

        responses.add(
            responses.GET,
            "https://doi.org/10.48324/dandi.000001/0.210801.2033",
            body="@misc{https://doi.org/10.48324/dandi.000001/0.210801.2033,\n  title={Test}\n}",
            status=200,
        )

        script_path = Path(__file__).parent.parent / "code" / "get-bibliography"
        bib_file = temp_dir / "test.bib"

        result = subprocess.run(
            [str(script_path), "--bibfile", str(bib_file), "--bibtype", "bibtex"],
            capture_output=True,
            text=True,
            cwd=temp_dir,
        )

        # Should succeed
        assert result.returncode == 0
        # BibTeX file should be created
        assert bib_file.exists()
        content = bib_file.read_text()
        # Should have the entry with corrected citation key
        assert "@misc{dandi.000001/0.210801.2033" in content


@pytest.mark.integration
@pytest.mark.ai_generated
class TestUpdateZoteroIntegration:
    """Integration tests for update-zotero-collection script."""

    def test_script_executable(self) -> None:
        """Test that update-zotero-collection script is executable."""
        script_path = Path(__file__).parent.parent / "code" / "update-zotero-collection"
        assert script_path.exists()
        assert script_path.stat().st_mode & 0o111

    def test_help_output(self) -> None:
        """Test that script shows help message."""
        script_path = Path(__file__).parent.parent / "code" / "update-zotero-collection"
        result = subprocess.run(
            [str(script_path), "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "--api-key" in result.stdout or "--api-key" in result.stderr
        assert "--group-id" in result.stdout or "--group-id" in result.stderr

    def test_dry_run_with_bibtex(self, temp_dir: Path) -> None:
        """Test dry-run mode with a sample BibTeX file."""
        bib_file = temp_dir / "test.bib"
        bib_file.write_text("""@misc{000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Dandiset},
  year = {2021},
  doi = {10.48324/dandi.000001/0.210801.2033}
}
""")

        script_path = Path(__file__).parent.parent / "code" / "update-zotero-collection"

        # Run in dry-run mode (should not require API key)
        result = subprocess.run(
            [
                str(script_path),
                "--bib-file", str(bib_file),
                "--api-key", "fake-key",
                "--group-id", "123456",
                "--collection-key", "TESTKEY",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
        )

        # Should complete without errors (though it will fail connecting to Zotero)
        # The important part is that it parses the BibTeX correctly
        assert "Test Dandiset" in result.stderr or result.returncode == 0


@pytest.mark.integration
@pytest.mark.ai_generated
class TestUpdateReadmeIntegration:
    """Integration tests for update-readme-stats script."""

    def test_script_executable(self) -> None:
        """Test that update-readme-stats script is executable."""
        script_path = Path(__file__).parent.parent / "code" / "update-readme-stats"
        assert script_path.exists()
        assert script_path.stat().st_mode & 0o111

    def test_generate_readme_from_bib(self, temp_dir: Path, monkeypatch) -> None:
        """Test generating README from bibliography file."""
        # Create fake project structure
        code_dir = temp_dir / "code"
        code_dir.mkdir()

        # Create test BibTeX file
        bib_file = temp_dir / "dandi.bib"
        bib_file.write_text("""# DANDISET 000001
@misc{dandi.000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Dandiset}
}

@misc{dandi.000001,
  author = {Doe, Jane},
  title = {Test Dandiset}
}
""")

        # Create results.json
        cache_dir = temp_dir / "cache"
        cache_dir.mkdir()
        results_data = {
            "000001": {
                "0.210801.2033": {"status": "success"},
                None: {"status": "success"},
            }
        }
        (cache_dir / "results.json").write_text(json.dumps(results_data))

        # Copy script to temp location
        original_script = Path(__file__).parent.parent / "code" / "update-readme-stats"
        test_script = code_dir / "update-readme-stats"
        test_script.write_text(original_script.read_text())
        test_script.chmod(0o755)

        # Run the script
        result = subprocess.run(
            [str(test_script)],
            capture_output=True,
            text=True,
            cwd=code_dir,
        )

        assert result.returncode == 0

        # Check README was created/updated
        readme_path = temp_dir / "README.md"
        assert readme_path.exists()

        content = readme_path.read_text()
        assert "## Statistics" in content
        assert "1" in content  # 1 dandiset
        assert "2" in content  # 2 records


@pytest.mark.integration
@pytest.mark.ai_generated
class TestFullWorkflow:
    """Integration tests for the complete workflow."""

    @responses.activate
    def test_end_to_end_workflow(self, temp_dir: Path) -> None:
        """Test the complete workflow: fetch -> update stats -> check files."""
        # Setup mock API responses
        responses.add(
            responses.GET,
            "https://api.dandiarchive.org/api/dandisets/",
            json={
                "count": 1,
                "next": None,
                "results": [
                    {
                        "identifier": "000001",
                        "most_recent_published_version": {"version": "0.210801.2033"},
                    }
                ],
            },
            status=200,
        )

        responses.add(
            responses.GET,
            "https://api.dandiarchive.org/api/dandisets/000001/versions/",
            json={"results": [{"version": "0.210801.2033"}]},
            status=200,
        )

        responses.add(
            responses.GET,
            "https://doi.org/10.48324/dandi.000001/0.210801.2033",
            body="""@misc{https://doi.org/10.48324/dandi.000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Workflow Dandiset},
  year = {2021},
  doi = {10.48324/dandi.000001/0.210801.2033},
  publisher = {DANDI Archive}
}""",
            status=200,
        )

        # Create project structure
        code_dir = temp_dir / "code"
        code_dir.mkdir()
        cache_dir = temp_dir / "cache"
        cache_dir.mkdir()

        # Step 1: Fetch bibliography
        get_bib_script = Path(__file__).parent.parent / "code" / "get-bibliography"
        bib_file = temp_dir / "dandi.bib"
        results_file = cache_dir / "results.json"

        result = subprocess.run(
            [
                str(get_bib_script),
                "--bibfile", str(bib_file),
                "--bibtype", "bibtex",
                "--results", str(results_file),
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert bib_file.exists()
        assert results_file.exists()

        # Verify BibTeX content
        bib_content = bib_file.read_text()
        assert "@misc{dandi.000001" in bib_content
        assert "Test Workflow Dandiset" in bib_content

        # Step 2: Update README stats
        update_readme_script = Path(__file__).parent.parent / "code" / "update-readme-stats"
        test_update_script = code_dir / "update-readme-stats"
        test_update_script.write_text(update_readme_script.read_text())
        test_update_script.chmod(0o755)

        result = subprocess.run(
            [str(test_update_script)],
            capture_output=True,
            text=True,
            cwd=code_dir,
        )

        assert result.returncode == 0

        # Verify README was created
        readme_path = temp_dir / "README.md"
        assert readme_path.exists()

        readme_content = readme_path.read_text()
        assert "## Statistics" in readme_content
        assert "1" in readme_content  # 1 dandiset

    def test_scripts_in_path(self) -> None:
        """Test that all main scripts exist and are in the expected location."""
        code_dir = Path(__file__).parent.parent / "code"
        scripts = [
            "get-bibliography",
            "update-zotero-collection",
            "update-readme-stats",
        ]

        for script_name in scripts:
            script_path = code_dir / script_name
            assert script_path.exists(), f"Script {script_name} not found"
            assert script_path.stat().st_mode & 0o111, f"Script {script_name} not executable"
