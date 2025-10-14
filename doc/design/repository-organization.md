# DANDI Bibliography Repository - Design Document

## Overview

This repository maintains bibliography records (BibTeX and RIS formats) for all published versions of DANDI datasets, with automated synchronization to a Zotero collection for collaborative curation.

## Repository Structure

```
dandi-bib/
├── README.md                    # Main documentation with statistics
├── dandi.bib                    # BibTeX bibliography (all dandisets, all versions)
├── dandi.ris                    # RIS bibliography (all dandisets, all versions)
├── code/                        # Scripts and tools
│   ├── get-bibliography         # Fetch bibliography from DANDI API
│   ├── update-zotero-collection # Sync bibliography to Zotero
│   ├── update-readme-stats      # Generate README.md statistics
│   └── test-citation-key        # Test citation key handling in Zotero
├── cache/                       # Cached data and intermediate files
│   └── results.json             # JSON cache of bibliography records
├── doc/                         # Documentation
│   └── design/                  # Design documents
│       └── repository-organization.md  # This file
└── .github/
    └── workflows/               # GitHub Actions automation
        └── update-bibliography.yml  # Automated bibliography updates
```

## File Purposes

### Top-Level Files

- **dandi.bib**: Complete BibTeX bibliography containing:
  - All published dandisets (no draft versions)
  - All published versions of each dandiset (e.g., 0.210831.2033, 0.220113.0400)
  - One "latest" entry per dandiset (e.g., dandi.000027) pointing to most recent version
  - Citation keys in format: `dandi.{identifier}` or `dandi.{identifier}/{version}`

- **dandi.ris**: Same content as dandi.bib but in RIS format
  - Includes abstracts (which BibTeX sometimes lacks)
  - Compatible with reference managers that prefer RIS

- **README.md**: Repository documentation including:
  - Current statistics (number of dandisets, versions, records)
  - Link to Zotero collection: https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3
  - Information about errors/issues fetching records
  - Usage instructions
  - Last update timestamp

### Code Directory

- **get-bibliography**: Python script that:
  - Queries DANDI API for all published dandisets
  - Fetches DOI metadata for each version from DataCite
  - Converts to BibTeX/RIS format
  - Handles missing or invalid DOI records
  - Supports caching via results.json
  - Outputs to dandi.bib and dandi.ris

- **update-zotero-collection**: Python script that:
  - Parses dandi.bib
  - Syncs to Zotero collection via API
  - Uses citation keys (not DOIs) as unique identifiers
  - Supports incremental updates (add new, update changed, skip unchanged)
  - Can clear entire collection with --clear-collection
  - Validates that >95% of existing records match local file

- **update-readme-stats**: Python script that:
  - Analyzes dandi.bib and results.json
  - Counts dandisets, versions, records
  - Identifies records with errors or missing data
  - Generates statistics section for README.md
  - Updates timestamp

- **test-citation-key**: Test utility for Zotero citation key handling

### Cache Directory

- **results.json**: JSON cache of bibliography records
  - Used by get-bibliography to avoid re-fetching unchanged records
  - Nested structure: `{dandiset_id: {version: bibtex_entry}}`
  - Enables incremental updates

### Automation

- **update-bibliography.yml**: GitHub Actions workflow that:
  - Runs on schedule (e.g., daily or weekly)
  - Executes get-bibliography to fetch latest records
  - Executes update-readme-stats to regenerate statistics
  - Commits changes if bibliography or README changed
  - Optionally syncs to Zotero (requires API key secret)

## Data Flow

```
DANDI API
    ↓
get-bibliography → results.json (cache)
    ↓              ↓
dandi.bib ←-------+
dandi.ris
    ↓
update-readme-stats → README.md
    ↓
update-zotero-collection → Zotero Collection
```

## Citation Key Format

Citation keys use format compatible with BibTeX:
- Versioned: `dandi.000027@0.210831.2033` (uses @ instead of /)
- Latest: `dandi.000027` (points to most recent published version)

**Why @ instead of /?**
- BibTeX citation keys cannot contain `/` character
- `@` provides clear separator while being BibTeX-compatible
- Zotero stores citation key in "extra" field as: `Citation Key: dandi.000027@0.210831.2033`

## Known Issues

### DataCite/DOI Records

Some dandisets have issues with their DOI records:
- Missing BibTeX metadata (empty response)
- Invalid schema (e.g., ROR identifiers in older schema versions)
- Missing DOIs (early dandiset versions)

These are tracked as comments in dandi.bib:
```bibtex
# No valid BibTeX for 000029/0.210503.0649. Starts with ...
```

### Zotero Field Compatibility

Zotero item types have different supported fields:
- "webpage" (used for datasets) doesn't support DOI or publisher as direct fields
- These are stored in "extra" field instead
- Code handles this automatically based on item type

## Update Schedule

GitHub Actions runs:
- **Daily**: Check for new dandiset versions
- **On manual trigger**: Force complete refresh
- **On push to main**: Re-run statistics generation

## Zotero Collection

Public collection for collaborative curation:
- Group: DANDI (5774211)
- Collection: Bibliography (T8I34DL3)
- URL: https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3

## Maintenance Tasks

### Regular
- Monitor GitHub Actions runs for errors
- Review failed DOI fetches
- Update citation keys when format changes (requires --clear-collection)

### Periodic
- Validate Zotero sync (check match rate)
- Review and clean up error records
- Update documentation

## Future Enhancements

1. **Error Reporting**: Generate detailed report of failed/invalid DOI records
2. **Validation**: Add tests to verify bibliography integrity
3. **Notifications**: Alert when new dandisets published
4. **Exports**: Generate additional formats (e.g., EndNote, CSL JSON)
5. **Metadata Enhancement**: Add keywords, abstracts from DANDI metadata
6. **Versioning**: Track changes to bibliography over time
