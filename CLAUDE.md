# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**rvlinks** provides web pages that display individual verses of the Ṛgveda, enabling direct links from CDSL dictionaries to the cited Ṛgveda passages. It is deployed at `https://sanskrit-lexicon.github.io/rvlinks/`.

Each verse page (e.g., `rvhymns/rv02.003.html#rv02.003.05`) shows the verse in Devanagari with accents, IAST transliteration, Russian translation (Elizarenkova), German translation, and English translation.

## Architecture

| File/Directory | Purpose |
|---|---|
| `rvhymns/` | Generated HTML files, one per hymn (`rv01.001.html` through `rv10.191.html`) |
| `make_hymns_01.py` | Generates `rvhymns/*.html` from the processed RV source |
| `redo.sh` | Full pipeline: processes source → generates hymn pages |
| `RV_sa-hn-ru-de-en_1.html` | Primary source: Ṛgveda with Sanskrit, Hindi, Russian, German, English columns |
| `fonts/` | Sanskrit display fonts (Siddhanta) |
| `badchars.txt` | Log of character encoding issues found during processing |
| `clean.sh` | Removes large intermediate files after build |
| `readme.org` | Detailed pipeline notes |

### Build pipeline

```bash
sh redo.sh
# Runs rvtest.py steps 5-7 to transform RV_sa-hn-ru-de-en_1.html
# Then: python make_hymns_01.py <processed_source> rvhymns
# Then: sh clean.sh (removes intermediate files)
```

After building, `rvhymns/` is pushed and served via GitHub Pages.

## Dependencies

- **Python 3**
- `RV_sa-hn-ru-de-en_1.html` — source Ṛgveda file (in repo)
