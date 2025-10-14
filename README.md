# DANDI Bibliography

Complete bibliography for all published DANDI datasets in BibTeX and RIS formats.

## Statistics

- **Dandisets**: 299
- **Published Versions**: 0
- **Total Records**: 741 (including "latest" entries)
- **Last Updated**: 2025-10-13 19:47:31 UTC

### Known Issues

3 records failed to fetch valid BibTeX:

- # No valid BibTeX for 000029/0.230317.1553. Starts with <!DOCTYPE html>
- # No valid BibTeX for 000029/0.231017.1955. Starts with <!DOCTYPE html>
- # No valid BibTeX for 000029/0.231017.1959. Starts with <!DOCTYPE html>



## Files

- **dandi.bib**: BibTeX format bibliography
- **dandi.ris**: RIS format bibliography

## Zotero Collection

This bibliography is synchronized to a public Zotero collection:
https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3

## Citation Keys

Each dataset has two citation keys:
- Versioned: `dandi.000027@0.210831.2033` (specific version)
- Latest: `dandi.000027` (most recent published version)

## Usage

### LaTeX/BibTeX

```latex
\bibliographystyle{plain}
\bibliography{dandi}

Cite as: \cite{dandi.000027@0.210831.2033}
```

### Zotero

Import `dandi.bib` directly into Zotero, or access the public collection above.

## Automation

This bibliography is automatically updated by GitHub Actions.
See `.github/workflows/update-bibliography.yml` for details.

## Scripts

Located in `code/`:
- `get-bibliography`: Fetch bibliography from DANDI API
- `update-zotero-collection`: Sync to Zotero collection
- `update-readme-stats`: Update this README with statistics

## License

The bibliography data is derived from DANDI Archive metadata and follows the same licenses as the individual datasets.
