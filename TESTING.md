# Testing Documentation

This document describes the testing setup for dandi-bib.

## Overview

The project now includes comprehensive unit and integration tests to ensure the bibliography management scripts work correctly without requiring full execution against the live DANDI API.

## Test Structure

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Shared pytest fixtures
├── test_get_bibliography.py # Tests for get-bibliography script
├── test_update_zotero.py    # Tests for update-zotero-collection script
├── test_update_readme.py    # Tests for update-readme-stats script
└── test_integration.py      # Integration tests for full workflows
```

## Running Tests

### Prerequisites

**Note**: This is a script collection, not an installable Python package. Tests use tox with `skip_install=true`.

Install test dependencies:

```bash
# Using pip (installs from pyproject.toml extras)
pip install -e ".[devel]"

# Or using uv (faster)
uv pip install -e ".[devel]"

# Or just use tox (it installs dependencies automatically)
pip install tox tox-uv
tox -e py3
```

All dependencies are defined in `pyproject.toml` as the single source of truth.

### Running with pytest

```bash
# Run all tests
pytest

# Run only unit tests (exclude integration tests)
pytest -m "not integration"

# Run only integration tests
pytest -m integration

# Run with coverage report
pytest --cov=code --cov-report=html --cov-report=term-missing

# Run specific test file
pytest tests/test_get_bibliography.py

# Run with verbose output
pytest -v
```

### Running with tox

Tox provides isolated test environments for different Python versions:

```bash
# Run tests with current Python version
tox -e py3

# Run with coverage
tox -e cov

# Run unit tests only
tox -e unit

# Run integration tests only
tox -e integration

# Run linter
tox -e lint

# Run type checker
tox -e type

# Run all environments
tox
```

### Using tox with uv (faster)

For faster execution, tox can use uv as the installer:

```bash
# Install tox-uv
pip install tox-uv

# Run tox (will automatically use uv)
tox -e py3
```

## Test Categories

### Unit Tests

Unit tests verify individual functions work correctly in isolation:

- **test_get_bibliography.py**: Tests session creation, API pagination, BibTeX/RIS format handling, error cases
- **test_update_zotero.py**: Tests BibTeX parsing, format conversion, item comparison, pagination
- **test_update_readme.py**: Tests statistics extraction, markdown generation, README updates

Unit tests use mocking (via `responses` library) to avoid external API calls.

### Integration Tests

Integration tests verify complete workflows:

- Script executability and help output
- End-to-end workflows with mocked APIs
- File I/O operations
- Multi-step processes (fetch → stats → README)

Mark integration tests with `@pytest.mark.integration`.

## Test Fixtures

Common fixtures are defined in `tests/conftest.py`:

- `temp_dir`: Temporary directory for test files
- `sample_dandiset_data`: Mock DANDI API dandiset response
- `sample_version_data`: Mock DANDI API version response
- `sample_bibtex_entry`: Example BibTeX entry
- `sample_bibtex_file`: Temporary BibTeX file
- `sample_zotero_item`: Example Zotero item
- `sample_results_json`: Mock results.json file
- `mock_api_response`: Paginated API response

## Writing New Tests

### Unit Test Example

```python
import pytest

@pytest.mark.ai_generated
def test_my_function(temp_dir: Path) -> None:
    """Test description."""
    # Arrange
    test_file = temp_dir / "test.txt"
    test_file.write_text("content")

    # Act
    result = my_function(str(test_file))

    # Assert
    assert result == expected_value
```

### Integration Test Example

```python
import subprocess
from pathlib import Path
import pytest

@pytest.mark.integration
@pytest.mark.ai_generated
def test_script_help(temp_dir: Path) -> None:
    """Test script help output."""
    script_path = Path(__file__).parent.parent / "code" / "my-script"

    result = subprocess.run(
        [str(script_path), "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "--option" in result.stdout
```

**Note**: `@responses.activate` only mocks HTTP within the same process.
It does NOT work for subprocess calls. For subprocess-based integration tests,
either test CLI argument parsing or use actual HTTP endpoints.

## Continuous Integration

The CI is fully tox-centric: all testing is defined in `tox.ini` and GitHub Actions simply invokes tox.

### CI Workflow

- **Matrix testing**: Python 3.10, 3.11, 3.12, 3.13, 3.14
- **Python 3.12 additionally runs**:
  - `lint` - Code quality checks with ruff
  - `type` - Type checking with mypy
  - `cov` - Coverage reporting with XML output for Codecov
- **Triggers**: Every push to master, all pull requests, manual dispatch

### Benefits of tox-centric CI

1. **Consistency**: Same commands work locally and in CI
2. **Simplicity**: CI just runs `tox`, all logic in `tox.ini`
3. **Maintainability**: Change test config in one place
4. **Developer experience**: Test locally exactly as CI does

See `.github/workflows/test.yml` for CI configuration.

## Coverage

Test coverage goals:

- **Overall**: >80%
- **Core functions**: >90%
- **Critical paths**: 100%

Generate coverage report:

```bash
# Terminal report
pytest --cov=code --cov-report=term-missing

# HTML report (open htmlcov/index.html)
pytest --cov=code --cov-report=html

# XML report (for CI/codecov)
pytest --cov=code --cov-report=xml
```

## Test Markers

Custom pytest markers defined in `pyproject.toml`:

- `@pytest.mark.integration`: Integration tests (slower, test workflows)
- `@pytest.mark.ai_generated`: Tests generated by AI assistants
- `@pytest.mark.slow`: Tests that take significant time
- `@pytest.mark.requires_api`: Tests requiring external API access

Filter by marker:

```bash
# Run only integration tests
pytest -m integration

# Skip integration tests
pytest -m "not integration"

# Run only AI-generated tests
pytest -m ai_generated
```

## Troubleshooting

### Import Errors

If tests fail with import errors, ensure you're running from the repository root:

```bash
cd /path/to/dandi-bib
pytest tests/
```

### Mock API Not Working

Ensure `responses` library is installed and the `@responses.activate` decorator is applied:

```python
import responses

@responses.activate
def test_api_call():
    responses.add(responses.GET, "https://...", json={})
    # ... test code
```

### Test Discovery Issues

Ensure test files follow pytest naming conventions:

- Files: `test_*.py` or `*_test.py`
- Classes: `Test*`
- Functions: `test_*`

## Test Timeout

All tests have a **30 second timeout** configured in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
timeout = 30
```

This prevents tests from hanging indefinitely on network issues or other blocking operations.

## Best Practices

1. **Isolate tests**: Each test should be independent
2. **Use fixtures**: Share common setup via pytest fixtures
3. **Mock external calls**: Use `responses` for HTTP, `mock` for other dependencies
4. **Clear assertions**: Use specific assertions with helpful messages
5. **Test edge cases**: Include error conditions, empty inputs, boundary values
6. **Keep tests fast**: Unit tests should run in milliseconds
7. **Document intent**: Use clear docstrings explaining what is tested
8. **Respect timeout**: Tests must complete within 30 seconds

## Dependency Management

All dependencies are defined in **pyproject.toml** as the single source of truth:

- `[project].dependencies`: Runtime dependencies
- `[project.optional-dependencies].test`: Test dependencies (pytest, responses, etc.)
- `[project.optional-dependencies].devel`: All development tools (test + ruff, mypy, tox)

Requirements files simply reference pyproject.toml:
- `requirements.txt`: `-e .` (runtime deps)
- `requirements-test.txt`: `-e .[devel]` (all dev deps)

### Why skip_install in tox?

This project contains standalone scripts in `code/` without `.py` extensions.
Tox uses `skip_install=true` but still installs dependencies via `deps = .[test]`
or `deps = .[devel]`. Tests run against the scripts in place.

### Installing dependencies

```bash
# Runtime dependencies only
pip install -e .

# All test and development dependencies
pip install -e ".[devel]"

# Or let tox handle it automatically
pip install tox tox-uv
tox -e py3
```

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [tox documentation](https://tox.wiki/)
- [responses library](https://github.com/getsentry/responses)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [PEP 621 - pyproject.toml](https://peps.python.org/pep-0621/)
