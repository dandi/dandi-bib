Folder to potentially contain config and dump of citations of our DANDI dandisets, as performed using https://github.com/con/citation-collector.

- [nwb-data-reuse.tsv](./nwb-data-reuse.tsv) came from https://rly1.notion.site/nwb-data-reuse?v=99f8e0f855a5486b8fc521066b34d4b3 as converted by claude code.

- [comparison-report.md](./comparison-report.md) provides comparison between that notion table and our auto-discovered listing in [dandi-full-citations.tsv](./dandi-full-citations.tsv)

For viewing full listing in .tsv, I recommend using [visidata](https://visidata.org), and can run it directly from URL:

```shell
visidata https://raw.githubusercontent.com/dandi/dandi-bib/refs/heads/master/citations/dandi-full-citations.tsv
```
