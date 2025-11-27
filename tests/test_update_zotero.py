"""Unit tests for update-zotero-collection script."""
import json
import sys
from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import Mock, MagicMock, patch

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
script_path = PROJECT_ROOT / "code" / "update-zotero-collection"
if not script_path.exists():
    raise ImportError(f"Script not found: {script_path}")
update_zotero = SourceFileLoader("update_zotero", str(script_path)).load_module()


class TestParseBibtexFile:
    """Tests for parse_bibtex_file function."""

    @pytest.mark.ai_generated
    def test_parse_valid_bibtex_file(self, sample_bibtex_file: Path) -> None:
        """Test parsing a valid BibTeX file."""
        entries = update_zotero.parse_bibtex_file(str(sample_bibtex_file))

        assert len(entries) == 1
        assert entries[0]["ID"] == "000001/0.210801.2033"
        assert "Doe, Jane" in entries[0]["author"]
        assert entries[0]["title"] == "Test Dandiset"

    @pytest.mark.ai_generated
    def test_parse_empty_bibtex_file(self, temp_dir: Path) -> None:
        """Test parsing an empty BibTeX file."""
        empty_file = temp_dir / "empty.bib"
        empty_file.write_text("")

        entries = update_zotero.parse_bibtex_file(str(empty_file))

        assert len(entries) == 0

    @pytest.mark.ai_generated
    def test_parse_multiple_entries(self, temp_dir: Path) -> None:
        """Test parsing a BibTeX file with multiple entries."""
        multi_bib = temp_dir / "multi.bib"
        multi_bib.write_text("""
@misc{entry1,
  author = {Doe, Jane},
  title = {First Entry},
  year = {2021}
}

@misc{entry2,
  author = {Smith, John},
  title = {Second Entry},
  year = {2022}
}
""")

        entries = update_zotero.parse_bibtex_file(str(multi_bib))

        assert len(entries) == 2
        assert entries[0]["ID"] == "entry1"
        assert entries[1]["ID"] == "entry2"


class TestBibtexToZoteroItem:
    """Tests for bibtex_to_zotero_item function."""

    @pytest.mark.ai_generated
    def test_convert_misc_to_dataset(self) -> None:
        """Test converting @misc entry to Zotero dataset."""
        bibtex_entry = {
            "ID": "000001/0.210801.2033",
            "ENTRYTYPE": "misc",
            "author": "Doe, Jane and Smith, John",
            "title": "Test Dandiset",
            "year": "2021",
            "publisher": "DANDI Archive",
            "doi": "10.48324/dandi.000001/0.210801.2033",
            "url": "https://doi.org/10.48324/dandi.000001/0.210801.2033",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert zotero_item["itemType"] == "dataset"
        assert zotero_item["title"] == "Test Dandiset"
        assert zotero_item["date"] == "2021"
        assert zotero_item["DOI"] == "10.48324/dandi.000001/0.210801.2033"
        assert zotero_item["repository"] == "DANDI Archive"
        assert zotero_item["versionNumber"] == "0.210801.2033"
        assert len(zotero_item["creators"]) == 2

    @pytest.mark.ai_generated
    def test_parse_author_last_first_format(self) -> None:
        """Test parsing authors in 'Last, First' format."""
        bibtex_entry = {
            "ENTRYTYPE": "misc",
            "author": "Doe, Jane and Smith, John Q.",
            "title": "Test",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert len(zotero_item["creators"]) == 2
        assert zotero_item["creators"][0]["firstName"] == "Jane"
        assert zotero_item["creators"][0]["lastName"] == "Doe"
        assert zotero_item["creators"][1]["firstName"] == "John Q."
        assert zotero_item["creators"][1]["lastName"] == "Smith"

    @pytest.mark.ai_generated
    def test_parse_author_first_last_format(self) -> None:
        """Test parsing authors in 'First Last' format."""
        bibtex_entry = {
            "ENTRYTYPE": "misc",
            "author": "Jane Doe and John Smith",
            "title": "Test",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert len(zotero_item["creators"]) == 2
        assert zotero_item["creators"][0]["firstName"] == "Jane"
        assert zotero_item["creators"][0]["lastName"] == "Doe"

    @pytest.mark.ai_generated
    def test_convert_article_type(self) -> None:
        """Test converting @article entry."""
        bibtex_entry = {
            "ENTRYTYPE": "article",
            "author": "Doe, Jane",
            "title": "Research Paper",
            "year": "2021",
            "doi": "10.1234/example",
            "publisher": "Academic Press",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert zotero_item["itemType"] == "journalArticle"
        assert zotero_item["DOI"] == "10.1234/example"
        assert zotero_item["publisher"] == "Academic Press"

    @pytest.mark.ai_generated
    def test_extract_version_from_doi(self) -> None:
        """Test extraction of version number from DOI."""
        bibtex_entry = {
            "ENTRYTYPE": "misc",
            "title": "Test",
            "doi": "10.48324/dandi.000027/0.210831.2033",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert zotero_item["versionNumber"] == "0.210831.2033"

    @pytest.mark.ai_generated
    def test_no_version_for_short_suffix(self) -> None:
        """Test that short DOI suffixes don't get treated as versions."""
        bibtex_entry = {
            "ENTRYTYPE": "misc",
            "title": "Test",
            "doi": "10.48324/dandi.000027",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert "versionNumber" not in zotero_item

    @pytest.mark.ai_generated
    def test_handle_missing_fields(self) -> None:
        """Test handling of entries with missing optional fields."""
        bibtex_entry = {
            "ENTRYTYPE": "misc",
            "title": "Minimal Entry",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        assert zotero_item["itemType"] == "dataset"
        assert zotero_item["title"] == "Minimal Entry"
        assert "creators" not in zotero_item
        assert "DOI" not in zotero_item

    @pytest.mark.ai_generated
    def test_citation_key_in_extra_field(self) -> None:
        """Test that citation key is added to extra field."""
        bibtex_entry = {
            "ID": "dandi.000001/0.210801.2033",
            "ENTRYTYPE": "misc",
            "title": "Test",
        }

        zotero_item = update_zotero.bibtex_to_zotero_item(bibtex_entry)

        # The citation key should be in the extra field
        assert "Citation Key: dandi.000001/0.210801.2033" in zotero_item["extra"]


class TestItemsAreDifferent:
    """Tests for items_are_different function."""

    @pytest.mark.ai_generated
    def test_identical_items_are_not_different(self) -> None:
        """Test that identical items are detected as same."""
        item1 = {
            "title": "Test",
            "DOI": "10.1234/test",
            "creators": [{"firstName": "Jane", "lastName": "Doe"}],
        }
        item2 = item1.copy()

        assert not update_zotero.items_are_different(item1, item2)

    @pytest.mark.ai_generated
    def test_different_titles_detected(self) -> None:
        """Test that different titles are detected."""
        item1 = {"title": "Test 1"}
        item2 = {"title": "Test 2"}

        assert update_zotero.items_are_different(item1, item2)

    @pytest.mark.ai_generated
    def test_ignores_zotero_metadata_fields(self) -> None:
        """Test that Zotero-specific fields are ignored in comparison."""
        item1 = {
            "title": "Test",
            "DOI": "10.1234/test",
        }
        item2 = {
            "title": "Test",
            "DOI": "10.1234/test",
            "key": "ABCD1234",
            "version": 5,
            "links": {},
        }

        # Should be considered the same despite Zotero metadata
        assert not update_zotero.items_are_different(item1, item2)

    @pytest.mark.ai_generated
    def test_different_creators_detected(self) -> None:
        """Test that differences in creators are detected."""
        item1 = {
            "title": "Test",
            "creators": [{"firstName": "Jane", "lastName": "Doe"}],
        }
        item2 = {
            "title": "Test",
            "creators": [{"firstName": "John", "lastName": "Smith"}],
        }

        assert update_zotero.items_are_different(item1, item2)


class TestGetExistingItems:
    """Tests for get_existing_items function."""

    @pytest.mark.ai_generated
    def test_get_items_single_page(self) -> None:
        """Test getting items when results fit in single page."""
        mock_zot = MagicMock()
        mock_zot.collection_items.return_value = [
            {"key": "ITEM1", "data": {"title": "Test 1"}},
            {"key": "ITEM2", "data": {"title": "Test 2"}},
        ]
        mock_zot.num_collectionitems.return_value = 2

        items = update_zotero.get_existing_items(mock_zot, "COLLKEY")

        assert len(items) == 2
        assert items[0]["key"] == "ITEM1"
        mock_zot.collection_items.assert_called_once()

    @pytest.mark.ai_generated
    def test_get_items_pagination(self) -> None:
        """Test getting items with pagination."""
        mock_zot = MagicMock()

        # Simulate 150 total items requiring 2 pages
        mock_zot.num_collectionitems.return_value = 150
        mock_zot.collection_items.side_effect = [
            [{"key": f"ITEM{i}", "data": {"title": f"Test {i}"}} for i in range(100)],
            [{"key": f"ITEM{i}", "data": {"title": f"Test {i}"}} for i in range(100, 150)],
        ]

        items = update_zotero.get_existing_items(mock_zot, "COLLKEY")

        assert len(items) == 150
        assert mock_zot.collection_items.call_count == 2

    @pytest.mark.ai_generated
    def test_get_items_empty_collection(self) -> None:
        """Test getting items from empty collection."""
        mock_zot = MagicMock()
        mock_zot.num_collectionitems.return_value = 0
        mock_zot.collection_items.return_value = []

        items = update_zotero.get_existing_items(mock_zot, "COLLKEY")

        assert len(items) == 0


class TestUpdateZoteroCollection:
    """Tests for update_zotero_collection function."""

    @pytest.mark.ai_generated
    def test_dry_run_mode(self, temp_dir: Path) -> None:
        """Test that dry run mode doesn't make actual changes."""
        bib_file = temp_dir / "test.bib"
        bib_file.write_text("""@misc{test,
  author = {Doe, Jane},
  title = {Test},
  doi = {10.1234/test}
}""")

        mock_zot = MagicMock()
        mock_zot.num_collectionitems.return_value = 0
        mock_zot.collection_items.return_value = []

        update_zotero.update_zotero_collection(
            str(bib_file),
            mock_zot,
            "COLLKEY",
            dry_run=True,
            cache_file=None
        )

        # Should not have called any update methods
        mock_zot.create_items.assert_not_called()
        mock_zot.update_item.assert_not_called()

    @pytest.mark.ai_generated
    def test_skips_invalid_entries(self, temp_dir: Path) -> None:
        """Test that invalid BibTeX entries are skipped."""
        bib_file = temp_dir / "test.bib"
        # Entry starting with # is invalid
        bib_file.write_text("""# No valid BibTeX for 000001/0.210801.2033""")

        mock_zot = MagicMock()
        mock_zot.num_collectionitems.return_value = 0
        mock_zot.collection_items.return_value = []

        update_zotero.update_zotero_collection(
            str(bib_file),
            mock_zot,
            "COLLKEY",
            dry_run=False,
            cache_file=None
        )

        # Should not attempt to create any items
        mock_zot.create_items.assert_not_called()
