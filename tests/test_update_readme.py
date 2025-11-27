"""Unit tests for update-readme-stats script."""
import json
import sys
from pathlib import Path
from typing import Dict, Any

import pytest

# Find project root (where pyproject.toml is)
def find_project_root():
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise RuntimeError("Could not find project root (pyproject.toml)")

PROJECT_ROOT = find_project_root()

# Add code directory to path
sys.path.insert(0, str(PROJECT_ROOT / "code"))

# Import the module
from importlib.machinery import SourceFileLoader
script_path = PROJECT_ROOT / "code" / "update-readme-stats"
if not script_path.exists():
    raise ImportError(f"Script not found: {script_path}")
update_readme = SourceFileLoader("update_readme", str(script_path)).load_module()


class TestAnalyzeBibliography:
    """Tests for analyze_bibliography function."""

    @pytest.mark.ai_generated
    def test_analyze_empty_repository(self, temp_dir: Path) -> None:
        """Test analyzing an empty repository."""
        stats = update_readme.analyze_bibliography(temp_dir)

        assert stats["dandisets"] == 0
        assert stats["versions"] == 0
        assert stats["records"] == 0
        assert len(stats["errors"]) == 0

    @pytest.mark.ai_generated
    def test_analyze_bibtex_file(self, temp_dir: Path) -> None:
        """Test analyzing a BibTeX file."""
        bib_content = """# DANDISET 000001
@misc{dandi.000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Dandiset}
}

@misc{dandi.000001,
  author = {Doe, Jane},
  title = {Test Dandiset}
}

# DANDISET 000002
@misc{dandi.000002/0.210901.1234,
  author = {Smith, John},
  title = {Another Dandiset}
}
"""
        (temp_dir / "dandi.bib").write_text(bib_content)

        stats = update_readme.analyze_bibliography(temp_dir)

        assert stats["dandisets"] == 2
        assert stats["records"] == 3  # Three @misc entries

    @pytest.mark.ai_generated
    def test_analyze_with_errors(self, temp_dir: Path) -> None:
        """Test analyzing BibTeX file with error comments."""
        bib_content = """# DANDISET 000001
@misc{dandi.000001/0.210801.2033,
  title = {Valid Entry}
}

# No valid BibTeX for 000002/0.210901.1234. Starts with Invalid content
# No valid BibTeX for 000003/0.211001.5678. Starts with Another invalid
"""
        (temp_dir / "dandi.bib").write_text(bib_content)

        stats = update_readme.analyze_bibliography(temp_dir)

        assert stats["records"] == 1
        assert len(stats["errors"]) == 2
        assert "000002/0.210901.1234" in stats["errors"][0]
        assert "000003/0.211001.5678" in stats["errors"][1]

    @pytest.mark.ai_generated
    def test_analyze_results_json(self, temp_dir: Path) -> None:
        """Test analyzing cache/results.json file."""
        cache_dir = temp_dir / "cache"
        cache_dir.mkdir()

        results_data = {
            "000001": {
                "0.210801.2033": {"status": "success"},
                "0.210802.1234": {"status": "success"},
                None: {"status": "success"},  # "latest" entry
            },
            "000002": {
                "0.210901.1234": {"status": "success"},
                None: {"status": "success"},
            },
        }
        (cache_dir / "results.json").write_text(json.dumps(results_data))

        stats = update_readme.analyze_bibliography(temp_dir)

        assert stats["dandisets"] == 2
        assert stats["versions"] == 3  # Excludes None entries

    @pytest.mark.ai_generated
    def test_analyze_both_files(self, temp_dir: Path) -> None:
        """Test analyzing both BibTeX and results.json."""
        # Create BibTeX file
        (temp_dir / "dandi.bib").write_text("""# DANDISET 000001
@misc{dandi.000001/0.210801.2033,
  title = {Test}
}

@misc{dandi.000001,
  title = {Test}
}
""")

        # Create results.json
        cache_dir = temp_dir / "cache"
        cache_dir.mkdir()
        results_data = {
            "000001": {
                "0.210801.2033": {"status": "success"},
                None: {"status": "success"},
            },
        }
        (cache_dir / "results.json").write_text(json.dumps(results_data))

        stats = update_readme.analyze_bibliography(temp_dir)

        # Results.json should take precedence for counts
        assert stats["dandisets"] == 1
        assert stats["versions"] == 1
        # BibTeX count still used for records
        assert stats["records"] == 2


class TestGenerateStatsSection:
    """Tests for generate_stats_section function."""

    @pytest.mark.ai_generated
    def test_generate_basic_stats(self) -> None:
        """Test generating basic statistics section."""
        stats = {
            "dandisets": 10,
            "versions": 25,
            "records": 35,
            "errors": [],
        }

        section = update_readme.generate_stats_section(stats)

        assert "## Statistics" in section
        assert "10" in section
        assert "25" in section
        assert "35" in section
        assert "Known Issues" not in section

    @pytest.mark.ai_generated
    def test_generate_with_errors(self) -> None:
        """Test generating statistics with error entries."""
        stats = {
            "dandisets": 10,
            "versions": 25,
            "records": 33,
            "errors": [
                "# No valid BibTeX for 000001/0.210801.2033",
                "# No valid BibTeX for 000002/0.210901.1234",
            ],
        }

        section = update_readme.generate_stats_section(stats)

        assert "## Statistics" in section
        assert "Known Issues" in section
        assert "2 records failed" in section
        assert "000001/0.210801.2033" in section
        assert "000002/0.210901.1234" in section

    @pytest.mark.ai_generated
    def test_generate_with_many_errors(self) -> None:
        """Test generating statistics with more than 10 errors."""
        errors = [f"# No valid BibTeX for 00000{i}/0.210801.2033" for i in range(15)]
        stats = {
            "dandisets": 100,
            "versions": 200,
            "records": 185,
            "errors": errors,
        }

        section = update_readme.generate_stats_section(stats)

        assert "15 records failed" in section
        assert "...and 5 more" in section
        # Should only show first 10
        assert "000000" in section
        assert "000009" in section
        assert "000014" not in section  # 15th error shouldn't be shown in full


class TestUpdateReadme:
    """Tests for update_readme function."""

    @pytest.mark.ai_generated
    def test_create_new_readme(self, temp_dir: Path) -> None:
        """Test creating a new README.md file."""
        stats_section = """## Statistics

- **Dandisets**: 10
- **Published Versions**: 25
- **Total Records**: 35
"""

        update_readme.update_readme(temp_dir, stats_section)

        readme_path = temp_dir / "README.md"
        assert readme_path.exists()

        content = readme_path.read_text()
        assert "# DANDI Bibliography" in content
        assert "## Statistics" in content
        assert "10" in content
        assert "25" in content
        assert "35" in content

    @pytest.mark.ai_generated
    def test_update_existing_readme_with_stats(self, temp_dir: Path) -> None:
        """Test updating README that already has a statistics section."""
        existing_readme = """# DANDI Bibliography

Some intro text.

## Statistics

- **Dandisets**: 5
- **Published Versions**: 10
- **Total Records**: 15

## Files

- dandi.bib
- dandi.ris
"""
        readme_path = temp_dir / "README.md"
        readme_path.write_text(existing_readme)

        new_stats_section = """## Statistics

- **Dandisets**: 100
- **Published Versions**: 250
- **Total Records**: 350
"""

        update_readme.update_readme(temp_dir, new_stats_section)

        content = readme_path.read_text()
        assert "100" in content
        assert "250" in content
        assert "350" in content
        # Old values should be gone
        assert "- **Dandisets**: 5" not in content
        # Other sections should remain
        assert "## Files" in content
        assert "Some intro text" in content

    @pytest.mark.ai_generated
    def test_update_readme_without_stats_section(self, temp_dir: Path) -> None:
        """Test updating README that doesn't have a statistics section."""
        existing_readme = """# DANDI Bibliography

Introduction text.

## Files

- dandi.bib
"""
        readme_path = temp_dir / "README.md"
        readme_path.write_text(existing_readme)

        stats_section = """## Statistics

- **Dandisets**: 50
- **Published Versions**: 100
- **Total Records**: 150
"""

        update_readme.update_readme(temp_dir, stats_section)

        content = readme_path.read_text()
        # Statistics should be inserted
        assert "## Statistics" in content
        assert "50" in content
        # Existing content should remain
        assert "## Files" in content

    @pytest.mark.ai_generated
    def test_preserves_other_sections(self, temp_dir: Path) -> None:
        """Test that updating stats preserves other README sections."""
        existing_readme = """# DANDI Bibliography

Introduction.

## Statistics

- Old stats

## Usage

How to use.

## License

MIT License
"""
        readme_path = temp_dir / "README.md"
        readme_path.write_text(existing_readme)

        stats_section = """## Statistics

- New stats
"""

        update_readme.update_readme(temp_dir, stats_section)

        content = readme_path.read_text()
        assert "New stats" in content
        assert "Old stats" not in content
        assert "## Usage" in content
        assert "How to use" in content
        assert "## License" in content


class TestMain:
    """Tests for main function."""

    @pytest.mark.ai_generated
    def test_main_integration(self, temp_dir: Path, monkeypatch) -> None:
        """Test main function end-to-end."""
        # Create a fake script in temp_dir/code
        code_dir = temp_dir / "code"
        code_dir.mkdir()
        fake_script = code_dir / "update-readme-stats"
        fake_script.write_text("# fake script")

        # Create test data
        bib_content = """# DANDISET 000001
@misc{dandi.000001/0.210801.2033,
  title = {Test}
}
"""
        (temp_dir / "dandi.bib").write_text(bib_content)

        # Mock __file__ to point to our temp location
        monkeypatch.setattr(
            update_readme,
            "__file__",
            str(fake_script)
        )

        # Run main
        update_readme.main()

        # Verify README was created
        readme_path = temp_dir / "README.md"
        assert readme_path.exists()
        content = readme_path.read_text()
        assert "## Statistics" in content
