# rvlinks

_Created: 14-06-2026 · Last updated: 11-07-2026_

CDSL **linking-tool** repository in the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) project.
A GitHub Pages site that hosts individually addressable HTML pages for the verses of the Ṛg Veda, with parallel Sanskrit, Hindi, Russian, German, and English text.

> Note: the default (and only) branch of this repository is `gh-pages`, so the site is served directly from the branch root. Push and pull against that branch: `git push origin gh-pages` / `git pull origin gh-pages`.

## What is here

- [`RV_sa-hn-ru-de-en_1.html`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/RV_sa-hn-ru-de-en_1.html) — the source multi-language Ṛg Veda document (Sanskrit / Hindi / Russian / German / English), originally supplied by Mārcis Gasūns (June 2018) and corrected to a double-daṇḍa at the final verse.
- [`rvhymns/`](https://github.com/sanskrit-lexicon/rvlinks/tree/gh-pages/rvhymns) — the split output: one HTML file per hymn (`rv01.001.html` … ), **1028 hymns / 10552 verses** in total, plus a bundled `fonts/` directory.
- [`fonts/`](https://github.com/sanskrit-lexicon/rvlinks/tree/gh-pages/fonts) — Devanāgarī fonts (Siddhanta / Sanskrit2003) needed for correct accent + visarga display.
- [`work/`](https://github.com/sanskrit-lexicon/rvlinks/tree/gh-pages/work) — auxiliary material, including a `missing_translations` scan.

## Pipeline

The build is driven by small Python scripts and shell wrappers, documented step-by-step in [`readme.org`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/readme.org):

- [`rvtest.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/rvtest.py) — successive transformations of the source HTML (bad-character fixes, accent/visarga spelling normalization, Devanāgarī digit + udātta/anudātta encoding, Unix line endings).
- [`make_hymns_01.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/make_hymns_01.py) — splits the normalized document into per-hymn files under `rvhymns/`.
- [`redo.sh`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/redo.sh) / [`clean.sh`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/clean.sh) — regenerate `rvhymns/` from the source and remove intermediate files.

The reference spelling target is the [Sanskrit Documents Ṛg Veda](https://sanskritdocuments.org/doc_veda/r01.html?lang=sa).

## Issues

Snapshot 11-07-2026: **1** open, **1** closed.

| Milestone | Open | Closed | Total |
|---|---:|---:|---:|
| API Stability | 0 | 0 | 0 |
| User Experience | 0 | 0 | 0 |
| Data Quality | 1 | 0 | 1 |
| Developer Experience | 0 | 0 | 0 |
| Community | 0 | 0 | 0 |

The single open issue is [#3 "Missing translations"](https://github.com/sanskrit-lexicon/rvlinks/issues/3) (`bug` · `minor` · Data Quality). The one closed issue, [#2](https://github.com/sanskrit-lexicon/rvlinks/issues/2), carries no milestone.

## GitHub issue conventions

Follows the [Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md): exactly one **type** label, one **severity** (`trivial` · `minor` · `major` · `critical`), and one **milestone** (API Stability · User Experience · Data Quality · Developer Experience · Community) per issue. Tool work across repositories is tracked in the org-level [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9). See [`CLAUDE.md`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/CLAUDE.md) for the full label set.

_Dr. Mārcis Gasūns_
