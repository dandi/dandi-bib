"""Shared pytest fixtures and configuration for dandi-bib tests."""
import json
import tempfile
from pathlib import Path
from typing import Any, Dict

import pytest


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Provide a temporary directory for test files."""
    return tmp_path


@pytest.fixture
def sample_dandiset_data() -> Dict[str, Any]:
    """Provide sample dandiset data from DANDI API."""
    return {
        "identifier": "000001",
        "name": "Test Dandiset",
        "url": "https://dandiarchive.org/dandiset/000001",
        "description": "A test dandiset for unit tests",
        "contributors": [
            {
                "name": "Doe, Jane",
                "roleName": ["dcite:Author", "dcite:ContactPerson"],
                "affiliation": [{"name": "Test University"}],
            }
        ],
        "license": ["spdx:CC-BY-4.0"],
        "assetsSummary": {"numberOfBytes": 1234567890, "numberOfFiles": 10},
    }


@pytest.fixture
def sample_version_data() -> Dict[str, Any]:
    """Provide sample version data from DANDI API."""
    return {
        "version": "0.210801.2033",
        "status": "Published",
        "created": "2021-08-01T20:33:00.000000Z",
        "modified": "2021-08-01T20:33:00.000000Z",
        "dandiset": {
            "identifier": "000001",
        },
        "name": "Test Dandiset",
        "description": "A test version",
        "doi": "10.48324/dandi.000001/0.210801.2033",
    }


@pytest.fixture
def sample_bibtex_entry() -> str:
    """Provide a sample BibTeX entry."""
    return """@misc{000001/0.210801.2033,
  author = {Doe, Jane},
  title = {Test Dandiset},
  year = {2021},
  publisher = {DANDI Archive},
  doi = {10.48324/dandi.000001/0.210801.2033},
  url = {https://doi.org/10.48324/dandi.000001/0.210801.2033}
}"""


@pytest.fixture
def sample_bibtex_file(temp_dir: Path, sample_bibtex_entry: str) -> Path:
    """Create a sample BibTeX file for testing."""
    bib_file = temp_dir / "test.bib"
    bib_file.write_text(sample_bibtex_entry)
    return bib_file


@pytest.fixture
def sample_zotero_item() -> Dict[str, Any]:
    """Provide a sample Zotero item."""
    return {
        "key": "TESTKEY1",
        "version": 1,
        "itemType": "document",
        "title": "Test Dandiset",
        "creators": [{"creatorType": "author", "firstName": "Jane", "lastName": "Doe"}],
        "date": "2021",
        "url": "https://doi.org/10.48324/dandi.000001/0.210801.2033",
        "DOI": "10.48324/dandi.000001/0.210801.2033",
        "publisher": "DANDI Archive",
        "extra": "Citation Key: 000001/0.210801.2033",
    }


@pytest.fixture
def sample_results_json(temp_dir: Path) -> Path:
    """Create a sample results.json file for testing."""
    results_file = temp_dir / "results.json"
    results_data = {
        "000001/0.210801.2033": {"status": "success", "doi": "10.48324/dandi.000001/0.210801.2033"},
        "000002/draft": {"status": "success", "doi": None},
    }
    results_file.write_text(json.dumps(results_data, indent=2))
    return results_file


@pytest.fixture
def mock_api_response() -> Dict[str, Any]:
    """Provide a mock API response for paginated requests."""
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "identifier": "000001",
                "name": "Test Dandiset 1",
                "most_recent_published_version": {
                    "version": "0.210801.2033",
                    "doi": "10.48324/dandi.000001/0.210801.2033",
                },
            },
            {
                "identifier": "000002",
                "name": "Test Dandiset 2",
                "most_recent_published_version": None,
            },
        ],
    }
