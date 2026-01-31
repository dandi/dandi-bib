# DANDI Citations Collection

This folder contains citation collection configuration and outputs for DANDI dandisets using [citations-collector](https://github.com/dandi/citations-collector).

## Files

- **[dandi-full.yaml](./dandi-full.yaml)**: Collection configuration using BibTeX source (`../dandi.bib`)
- **[dandi-full-citations.tsv](./dandi-full-citations.tsv)**: Discovered citations (auto-generated)
- **[Makefile](./Makefile)**: Pipeline automation for discovery → merge → PDF fetching
- **[nwb-data-reuse.tsv](./nwb-data-reuse.tsv)**: Manual curation from [NWB Data Reuse Notion table](https://rly1.notion.site/nwb-data-reuse?v=99f8e0f855a5486b8fc521066b34d4b3)
- **[comparison-report.md](./comparison-report.md)**: Comparison between manual and auto-discovered citations

## Usage

### Quick Start

Run the full citation collection pipeline:

```bash
make all
```

This will:
1. Discover citations from all configured sources (CrossRef, OpenCitations, DataCite, OpenAlex)
2. Detect and merge preprints with their published versions
3. Fetch open-access PDFs into `pdfs/` directory

### Individual Steps

```bash
make discover      # Step 1: Discover citations only
make merge         # Step 2: Detect/merge preprints only
make pdfs          # Step 3: Fetch PDFs only
make status        # Show current statistics
make clean         # Remove generated files
```

### Using with DataLad

For reproducible execution tracking:

```bash
datalad run -m "Update DANDI citations" --output dandi-full-citations.tsv --output pdfs/ make all
```

## BibTeX Source Integration

The collection now uses a **BibTeX source** pointing to `../dandi.bib`, which is maintained by the [dandi-citations](https://github.com/dandi/dandi-citations) tool. This allows:

- External maintenance of dandiset metadata in BibTeX format
- Automatic extraction of item IDs and version numbers from DOIs
- Integration with existing bibliography management workflows

The BibTeX file contains all DANDI dandisets with versioned DOIs. The citation collector:
1. Parses `dandi.bib` using regex pattern to extract `item_id` and `flavor_id` from DOIs
2. Discovers citations for each dandiset version from multiple sources
3. Deduplicates and merges preprints with published versions
4. Fetches open-access PDFs where available

## Viewing Results

For interactive exploration of the TSV file, we recommend [visidata](https://visidata.org):

```bash
visidata dandi-full-citations.tsv

# Or directly from GitHub:
visidata https://raw.githubusercontent.com/dandi/dandi-bib/refs/heads/master/citations/dandi-full-citations.tsv
```

## Configuration

Edit `dandi-full.yaml` to customize:
- Citation sources to query
- PDF output directory
- Email for API polite pools
- Regex pattern for BibTeX parsing

See [citations-collector documentation](https://github.com/dandi/citations-collector) for full configuration options.
