# DANDI Bibliography

Complete bibliography for all published DANDI datasets in BibTeX and RIS formats.

## Statistics

- **Dandisets**: 326
- **Published Versions**: 799
- **Total Records**: 1121 (including "latest" entries)

### Known Issues

3 records failed to fetch valid BibTeX:

- `# No valid BibTeX for 000029/0.230317.1553. Starts with <!DOCTYPE html>`
- `# No valid BibTeX for 000029/0.231017.1955. Starts with <!DOCTYPE html>`
- `# No valid BibTeX for 000029/0.231017.1959. Starts with <!DOCTYPE html>`


## Files

- **dandi.bib**: BibTeX format bibliography
- **dandi.ris**: RIS format bibliography

## Zotero Collection

This bibliography is synchronized to a public Zotero collection:
https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3

## Citation Keys

Each dataset has two citation keys:
- Versioned: `dandi.000027/0.210831.2033` (specific version)
- Latest: `dandi.000027` (most recent published version)

## Usage

### LaTeX/BibTeX

```latex
\bibliographystyle{plain}
\bibliography{dandi}

Cite as: \cite{dandi.000027/0.210831.2033}
```

### Zotero

Import `dandi.bib` directly into Zotero, or access the public collection above.

## Workflow

```mermaid
flowchart TD
    %% Current Implementation (solid lines)
    trigger[["⏰ GitHub Actions Trigger<br/>(Daily @ 3:22 AM UTC)"]]
    trigger -.->|<a href='.github/workflows/update-bibliography.yml'>update-bibliography.yml</a>| fetch

    subgraph current["🟢 Current Implementation"]
        direction TB
        fetch["📥 Fetch Dandiset Metadata<br/><a href='code/get-bibliography'>get-bibliography</a>"]
        api[("🌐 DANDI Archive API<br/>dandiarchive.org")]

        fetch -->|"Query published<br/>dandisets"| api
        api -->|"DOI, title,<br/>authors, etc"| fetch

        fetch --> bib["📄 dandi.bib<br/>(BibTeX)"]
        fetch --> ris["📄 dandi.ris<br/>(RIS)"]
        fetch --> cache["💾 cache/results.json"]

        zotero_sync["🔄 Sync to Zotero<br/><a href='code/update-zotero-collection'>update-zotero-collection</a>"]
        bib --> zotero_sync
        zotero_sync -->|"pyzotero API"| zotero_main[("📚 Zotero Group Collection<br/><a href='https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3'>T8I34DL3</a>")]

        commit["✅ Git Commit & Push"]
        bib --> commit
        ris --> commit
        cache --> commit
        readme --> commit

        stats["📊 Update Statistics<br/><a href='code/update-readme-stats'>update-readme-stats</a>"]
        bib --> stats
        stats --> readme["📝 README.md"]


    end

    %% Planned Future Additions (dashed lines)
    subgraph planned["🔵 WiP: Citation Discovery Pipeline <a href='citations/'>(citations/)</a>"]
        direction TB
        cc_config["⚙️ Configuration<br/><a href='citations/dandi-full.yaml'>dandi-full.yaml</a>"]

        discover["🔍 Discover Citations<br/><a href='https://github.com/con/citations-collector'>citations-collector</a>"]
        bib -.->|"Input:<br/>dandiset DOIs"| cc_config
        cc_config -.-> discover

        sources[("🔬 Citation Sources<br/>OpenAlex | DataCite<br/>CrossRef | OpenCitations")]
        discover -->|Query on Dandiset DOI| sources
        sources -->|Citation DOIs| discover

        merge["🔀 Merge Preprints<br/>(detect published versions)"]
        discover -.-> merge

        tsv["📊 dandi-full-citations.tsv"]
        merge -.-> tsv

        pdfs["📑 Fetch PDFs<br/>(unpaywall, OA sources)"]
        tsv -.-> pdfs
        pdf_dir["📁 citations/pdfs/"]
        pdfs -.-> pdf_dir

        zotero_citations["🔄 Sync Citations to Zotero<br/>(subcollection)"]
        tsv -.-> zotero_citations
        zotero_citations -.->|"via citations-collector"| zotero_sub[("📚 Zotero Subcollection<br/><a href='https://www.zotero.org/groups/5774211/dandi/collections/UHK47FKX'>UHK47FKX</a>")]

        makefile["🛠️ Automation<br/><a href='citations/Makefile'>Makefile</a>"]
        makefile -.->|"make all"| discover
    end

    %% Connections between workflows
    commit -.->|"Manually (TODO: add to CI)"| cc_config

    %% Styling
    classDef implemented fill:#90EE90,stroke:#2d5016,stroke-width:2px,color:#000
    classDef planned fill:#87CEEB,stroke:#1e3a5f,stroke-width:2px,stroke-dasharray: 5 5,color:#000
    classDef external fill:#FFE4B5,stroke:#8B4513,stroke-width:2px,color:#000

    class fetch,bib,ris,cache,stats,readme,zotero_sync,commit,zotero_main implemented
    class cc_config,discover,merge,tsv,pdfs,pdf_dir,zotero_citations,zotero_sub,makefile planned
    class api,sources external
```

### Workflow Details

#### Current Implementation

1. **Daily Automation**: [GitHub Actions workflow](.github/workflows/update-bibliography.yml) runs daily at 3:22 AM UTC
2. **Metadata Fetch**: [`get-bibliography`](code/get-bibliography) queries [DANDI Archive API](https://dandiarchive.org) for all published dandisets
3. **Format Generation**: Creates both [`dandi.bib`](dandi.bib) (BibTeX) and [`dandi.ris`](dandi.ris) (RIS) files
4. **Statistics Update**: [`update-readme-stats`](code/update-readme-stats) updates this README with current counts
5. **Zotero Sync**: [`update-zotero-collection`](code/update-zotero-collection) syncs to [public Zotero group collection](https://www.zotero.org/groups/5774211/dandi/collections/T8I34DL3)
6. **Git Commit**: Changes are automatically committed and pushed to the repository

#### Planned: Citation Discovery Pipeline

The [`citations/`](citations/) directory contains configuration and tooling for discovering citations to DANDI dandisets:

1. **Configuration**: [`dandi-full.yaml`](citations/dandi-full.yaml) points to `dandi.bib` as the source of dandiset DOIs
2. **Citation Discovery**: [citations-collector](https://github.com/con/citations-collector) queries multiple sources:
   - [OpenAlex](https://openalex.org)
   - [DataCite](https://datacite.org)
   - [CrossRef](https://crossref.org)
   - [OpenCitations](https://opencitations.net)
3. **Preprint Merging**: Detects and merges preprint citations with their published versions
4. **Output**: Results saved to [`dandi-full-citations.tsv`](citations/dandi-full-citations.tsv)
5. **PDF Fetching**: Downloads open-access PDFs to [`citations/pdfs/`](citations/pdfs/)
6. **Zotero Subcollection**: Syncs citations to [dedicated subcollection](https://www.zotero.org/groups/5774211/dandi/collections/UHK47FKX)
7. **Automation**: [`Makefile`](citations/Makefile) provides targets for running the pipeline locally or via DataLad

See [`citations/README.md`](citations/README.md) for detailed usage instructions.

## Scripts

Located in `code/`:
- `get-bibliography`: Fetch bibliography from DANDI API
- `update-zotero-collection`: Sync to Zotero collection
- `update-readme-stats`: Update this README with statistics

## License

The bibliography data is derived from DANDI Archive metadata and follows the same licenses as the individual datasets.
