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

- [`rvtest.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/rvtest.py) — successive transformations of the source HTML (bad-character fixes, accent/visarga spelling normalization, Devanāgarī digit + udātta/anudātta encoding, Unix line endings); [`prep_source.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/prep_source.py) is the Python-3 port of the 5/6/7 chain used by `redo.sh`.
- [`make_hymns_01.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/make_hymns_01.py) — splits the normalized document into per-hymn files under `rvhymns/` and emits Open Graph meta (title, description = first IAST line of verse 1, canonical URL).
- [`keep_griffith_fix.py`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/keep_griffith_fix.py) — re-grafts the hand-fixed 2020 Griffith bodies of `rv08.049`–`rv08.103` (issue [#2](https://github.com/sanskrit-lexicon/rvlinks/issues/2)) after every rebuild, until the source document itself is corrected.
- [`redo.sh`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/redo.sh) / [`clean.sh`](https://github.com/sanskrit-lexicon/rvlinks/blob/gh-pages/clean.sh) — regenerate `rvhymns/` from the source and remove intermediate files.

Every hymn page carries Open Graph meta (`og:title` "RV X.Y", `og:description` = first IAST pāda of verse 1, canonical `og:url`). When a 1200x630 PNG exists at `cards/rv<book>.<hymn>.png`, the page also references it as `og:image` **and** emits `twitter:card=summary_large_image` + `twitter:image` — without that hint Telegram renders the compact preview instead of the large card. Card faces carry the hymn number + first line in Devanāgarī + IAST only (the Russian layer keeps its Elizarenkova-aligned attribution on the pages). Generate cards with headless Chrome (`CHROME_BIN` overrides the Chrome path): `python3 make_cards.py temp_RV_sa-hn-ru-de-en_5.html rv01.001 rv02.001 ...`, then re-run `make_hymns_01.py` + `keep_griffith_fix.py`. The 10-sūkta pilot set (H6477): first sūkta of each of the 10 maṇḍalas; the full 1028 set follows the Telegram canary.

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
