"""Integration tests for dandi-bib workflows."""
import json
import subprocess
from pathlib import Path

import pytest


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

    # NOTE: Can't mock HTTP responses for subprocess calls - @responses.activate
    # only works within the same process. Real HTTP mocking for subprocess would
    # require a mock server or environment variable based URL override.


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
        """Test dry-run mode with a sample BibTeX file.

        Note: Even in dry-run mode, the script needs to connect to Zotero
        to check existing items. So this test just verifies that the script
        starts and parses the BibTeX file correctly before the Zotero call.
        """
        bib_file = temp_dir / "test.bib"
        bib_file.write_text("""@misc{000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Dandiset},
  year = {2021},
  doi = {10.48324/dandi.000001/0.210801.2033}
}
""")

        script_path = Path(__file__).parent.parent / "code" / "update-zotero-collection"

        # Run in dry-run mode with short timeout - it will fail connecting to Zotero
        # but we can verify it parsed the BibTeX file
        result = subprocess.run(
            [
                str(script_path),
                "--bibfile", str(bib_file),  # NOTE: not --bib-file
                "--api-key", "fake-key",
                "--group-id", "123456",
                "--collection-key", "TESTKEY",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            timeout=10,  # Short timeout since it will fail on Zotero connection
        )

        # Check that it at least parsed the BibTeX file and logged the entry count
        assert "Found 1 entries" in result.stderr or "Test Dandiset" in result.stderr


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
    """Integration tests for the complete workflow.

    NOTE: Full end-to-end tests that require HTTP mocking for subprocess calls
    cannot be implemented with @responses.activate as it only works within the
    same process. See test_fetch_dandisets_* tests in test_get_bibliography.py
    for in-process tests with HTTP mocking.
    """

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
