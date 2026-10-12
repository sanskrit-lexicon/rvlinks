# Vedic layer — estate inventory and Ṛgveda profile (H6062, ruling MG A7)

_Created: 07-10-2026 · Last updated: 07-10-2026 · Executor: GLM 5.3 (opencode/zai-coding-plan/glm-5.3)_
_Handoff: [H6062](https://github.com/gasyoun/Uprava/blob/main/handoffs/H6062-GLM_rvlinks_vedic-rv-layer_04.10.26.md) · Epic: [E024](https://github.com/gasyoun/Uprava/blob/main/handoffs/epics/E024-Uprava_sanskrit-research-fund-2027_04.10.26.md) (fundamental measurements 2026-27, ruling A7 «в волну»)_

Scope: what Vedic material the estate already holds, a measured frequency profile of the Ṛgveda against classical corpus strata, the live connection points to corpus statistics and the sense-seq line, and the map of what a Vedic expansion of the kosha dictionary union still needs. All numbers below are reproducible from the committed script + JSON in [`vedic-layer/`](vedic-layer/).

---

## 1. Inventory of Vedic material in the estate

### 1.1 Texts and readers

| Asset | Home | What it is | Measured scale / state |
|---|---|---|---|
| rvlinks (this repo) | `sanskrit-lexicon/rvlinks`, branch `gh-pages` | Linked multi-layer RV reader; source file `RV_sa-hn-ru-de-en_1.html` (M. Gasuns, June 2018, one bad character fixed vs `_0`), split by `redo.sh`/`make_hymns_01.py` into per-hymn pages | **1,028 hymn files, 10,552 verse anchors** (`rvMM.SSS.VV`), 5 layers per verse: `sa` accented Devanāgarī · `hn` IAST · `ru` (Elizarenkova-school) · `de` · `en` (Griffith, per H1843); `work/missing_translations.txt` = 956 lines |
| ScharfSandhi | `gasyoun/ScharfSandhi` (fork of funderburkjim) | Scharf's sandhi engine (saṃhitā ↔ pada), SLP1; Pascal → Perl → Java → Python (v1–v4) + testfiles/testlog | Runnable, test-suite carried; the estate's only accent-aware sandhi tool — the RV-specific junction layer |
| DCS-conllu | local dump of DCS (2022-08-09 UD release) | 270 texts / 5.46 M words, CoNLL-U; Vedic core present: **Ṛgveda**, Ṛgvedakhilāni, Ṛgvedavedāṅgajyotiṣa, AV (Śaunaka), AV (Paippalāda), Aitareya-Āraṇyaka/Brāhmaṇa/Upaniṣad, Vedic treebank syntax on RV; `Unsandhied` (padapāṭha) MISC layer; `IsMantra` flag from **Bloomfield's Vedic Concordance** | RV folder: 1,028 `.conllu` + 1,028 `_parsed`; see §2 for measured profile |
| Elizarenkova RV (RU) | `SamudraManthanam` `01/02_rigveda.no_tags` blocks (H2863) | Russian RV translation corpus inside the NKRYa parallel-corpus programme | Consumed by kosha `bloomfield-rv-x-elizarenkova-ru` (see §1.3) |
| RV multi-translation spine | H1843 (archived, `RussianTranslation` wave W1a) | Griffith EN extraction, lemma-keyed 4-translation JSONL/TSV, Renou locus index; rvlinks `_1.html` recorded as the only Griffith-layer source | Archived handoff; artifacts keyed by verse locus, re-derivable from rvlinks |

### 1.2 Dictionaries with Vedic / RV content

| Asset | Home | What it is | Vedic relevance |
|---|---|---|---|
| **GRA** — Grassmann, *Wörterbuch zum Rig-Veda* (1873) | `sanskrit-lexicon/GRA` (+ canonical `gra.txt` in fenced `csl-orig`) | The RV dictionary: every entry keyed to RV occurrences; subworkflows `verbs01`, `vn` Nachträge, `graab`, `issues/`, `prefaces` (foreword OCR'd EN+RU) | The natural 7th column for the union — but **no numbered sense inventory** (see §4.2) |
| PWG / MW `<ls>` RV citations | `csl-orig` (fenced, read-only consume) via kosha concordance layers | Classical dictionaries citing RV by locus | kosha `sense-dating`: **1,342 PWG dated senses first-attested in the Vedic era** (era census vedic 1342 / epic-sutra 2184 / classical 1107 / early-medieval 1039 / late-medieval 652 / null 1025, H4019); `sense-corpus-concordance` 'locus 5' tier = DCS verse-EQUAL attestation for canonically-numbered Vedic texts |
| LRV | `sanskrit-lexicon/LRV` | **False friend** — L. R. Vaidya's 1889 Sanskrit-English dictionary, nothing to do with the Rigveda | Listed here only to prevent future confusion |
| rsvpnanorus | local clone | **False friend** — "RV" = Rapid Serial Visual Presentation reading device | Excluded from the Vedic layer |

### 1.3 Registered kosha datasets (the data spine)

From `kosha/data/manifest/datasets.json` — every Vedic/RV-keyed row:

| kosha dataset id | Content | Key numbers |
|---|---|---|
| `bloomfield-rv-citations` | Direct RV citations from Franceschini's digital Bloomfield 1906 concordance (pratīka index) | 88,835 concordance entries scanned; **10,374 distinct RV (maṇḍala, sūkta, verse) keys**; 85% of the RV parallel-passage subset pratīka-validated; rights: direct Franceschini permission |
| `bloomfield-rv-x-elizarenkova-ru` | Bloomfield RV citations × Elizarenkova RU — citation-to-translation pointer join | Emits **`rvlinks_anchor` (rvMM.SSS.VV URLs back into this repo)** — the live citation→verse bridge |
| `parallel-passage-concordance` (B3) | Bloomfield-style parallel-passage concordance across DCS | RV subset 13,581 rows with `bloomfield_pratika` column |
| `sense-dating` (H4019) | Per-sense first-attestation era buckets (vedic < epic-sutra < classical < …) | vedic bucket = 1,342 senses; the Vedic edge of the chronology |
| `sense-portraits` (H4735) | Diachronic sense portraits: frequency × first-era join | 7,349 dated senses over 500 lemmas; the join point where Vedic-era senses meet corpus frequency |
| `dcs-lsc-pilot` | Lexical semantic change (PPMI-cosine) over DCS 5-slot chronology | The chronology **starts at Vedic**: `freq-shift baseline (Vedic→Epic)` is already a keyed column |
| `sense-corpus-concordance` | Per-sense corpus attestation | 'locus 5' confidence tier = canonically-numbered Vedic texts |
| `pd-dcs-coverage` (H1336) | Poona Dictionary × DCS coverage | DCS holds the Vedic/epic core (77.9% DCS-token-weighted) but misses purāṇic/lexicographic breadth — the mirror-image gap |
| `zaliznyak-lectures-transcripts` | Zaliznyak public-lecture census | 66/272 groups tagged `sanskrit_vedic` (RV close reading + grammar courses) — teaching-side Vedic demand signal |

### 1.4 Not yet probed for RV content

- `Parallel-Sanskrit-Corpora` — RV presence unverified (candidate follow-up, not measured here).
- H097 (archived) GRA ↔ VedaWeb 2.0 crosswalk design — Grassmann entries → attested RV occurrences; VedaWeb-side lemmatization is the external dependency.

---

## 2. Ṛgveda frequency profile vs classical strata (own computation)

**Source:** local DCS-conllu dump (2022-08-09 release; 270 texts, 5,464,818 words). **Method:** stream every `*.conllu` (excluding `_parsed` twins), tokens = non-range numbered lines, lemma/form = raw string identity, no `form_key()` normalization. Script + JSON committed in [`vedic-layer/`](vedic-layer/) — rerun to reproduce.

| Text | Files | Tokens | Distinct forms | Lemmas | TTR @25,040 tokens |
|---|---:|---:|---:|---:|---:|
| **Ṛgveda** | 1,028 | **169,972** | 34,642 | **8,765** | **0.3927** |
| Rāmāyaṇa (epic) | 606 | 261,568 | 43,371 | 10,922 | 0.3448 |
| Mahābhārata (epic) | 1,995 | 1,147,887 | 105,154 | 22,427 | 0.3779 |
| Hitopadeśa (classical prose) | 5 | 25,040 | 8,858 | 3,781 | 0.3538 |

**Findings:**

1. **RV is the lexically densest stratum** — highest normalized TTR (0.393 at 25k tokens) despite being the smallest corpus: hymnic-poetic register plus accent-marked orthography inflate the form inventory. Epic bulk does not catch up (MBh 0.378 even at its scale advantage).
2. **RV vs epic lemma overlap (raw string):** shared 3,097; RV-only 5,668 (64.7% of RV lemmas); epic-only 21,399. **Caveat — 1,714 of the 5,668 RV-only lemmas carry accent/diacritic characters beyond plain IAST** (accented Vedic lemma keys), so part of the "gap" is normalization, not vocabulary. Even after allowing for that, the mid-frequency residue is genuinely Vedic: *puroḍāś, vidatha, jaritṛ, vajrivat, somin, ojiṣṭha, dyumna, cakṣas, avṛka, śrath*…
3. **Top-lemma profiles diverge by register:** RV leaders are pronouns + *su* (2,101) + the ritual-theological triad **indra (2,586) · deva (1,916) · agni (1,843) · soma (1,139)**; Rāmāyaṇa leaders are narrative particles (*tad, ca, mad, tvad, mahat, rāma*). The RV frequency core is the sacrificial pantheon, not narrative syntax.
4. **Vedic Treebank:** 34,748 RV tokens (20.4%) carry syntactic HEAD/DEPREL — RV is the only estate text family with gold syntax; Rām/MBh have essentially none (526/4,461 tokens).
5. `IsMantra` = 0 hits inside RV itself — the Bloomfield mantra flag marks mantra quotations *inside ritual prose*, not the source hymns (expected, now measured).

---

## 3. Connection points (стыковки)

| Neighbour line | Where it touches the Vedic layer |
|---|---|
| **Corpus statistics (H6059, DCS-conllu)** | Same source dump — this profile's per-text numbers are the RV rows of that census; H6059 should consume/extend rather than recompute. |
| **sense-seq ρ-matrix (H6051, kosha union of 6 dictionaries)** | Three live legs: (a) `sense-dating` vedic era bucket supplies the chronology edge; (b) GRA is the RV-specific sense inventory candidate; (c) `dcs-lsc-pilot`'s 5-slot chronology already starts its freq-shift at Vedic. |
| **rvlinks anchors** | kosha `bloomfield-rv-x-elizarenkova-ru` already emits `rvlinks_anchor` URLs into this repo — the citation→verse bridge is live today; the extension path is GRA-entry→anchor (same key space, `rvMM.SSS.VV`). |
| **Sandhi** | Three orthographic layers over one junction problem: rvlinks `sa`/`hn` (accented), DCS `Unsandhied` padapāṭha (partial), ScharfSandhi (generative, SLP1). |
| **Translations** | H1843 4-translation spine + SamudraManthanam Elizarenkova RU + rvlinks' own 5-layer pages — all keyed by verse locus. |
| **Mānadaṇḍa (H6052)** | RV hymnic metre/structure census is the Vedic-side input to the corpus-wide metre line. |

---

## 4. Needs map for the Vedic expansion of the union

Ordered by blocking power:

1. **Lemma normalization layer (blocking).** Accented Vedic lemma keys vs plain IAST/SLP1 — 1,714/5,668 of the RV-only mass (§2.2). Before RV frequency can join the 6-dict union, apply the house `form_key()` + an explicit accent-stripping table; keys must stay accent-*preserving* as a second column (accent is lexical information in Vedic, §4.3).
2. **GRA sense inventory (the 7th-column prerequisite).** GRA has entries + occurrence keys but no numbered senses. Needs a PWG-style sense-segmentation pass over `gra.txt` (fenced csl-orig — read-only consume, corrections via the GRA issue lane, never direct commits).
3. **Accent policy in the union schema.** rvlinks `sa` and DCS accented lemmas are the only accent carriers; union frequency columns must decide accent-stripped vs accent-aware keys — recommended: two-key scheme (join on stripped, preserve accented).
4. **Padapāṭha coverage measurement.** DCS `Unsandhied` is explicitly partial; ScharfSandhi can generate the missing side, but coverage per maṇḍala has never been measured — measure first, generate second.
5. **One hymn-key crosswalk table.** rvlinks `rvMM.SSS.VV` vs DCS chapter ids vs Bloomfield `(m,s,v,pada)` vs Renou locus: kosha already joins 3 of the 4; publish the crosswalk as a kosha dataset to close the loop.
6. **Treebank widening is upstream.** Syntax covers 20.4% of RV tokens; widening is Hellwig-side — consume releases, don't rebuild.
7. **AV parity gap (out of scope, noted).** Both AV śākhās are in DCS-conllu, but the estate holds no Atharvaveda lexical layer (Whitney-Lanman un-digitized here) — flagged so the "Vedic layer" is never silently equated with "RV only".

---

## 5. Reproduction

- `vedic-layer/profile.py` — streams the DCS-conllu folders, emits all §2 aggregate numbers (tokens/forms/lemmas/overlap/top-lemmas) to `profile.json`.
- `vedic-layer/ttr.py` — the normalized TTR@25,040 pass quoted in the §2 table.
- `vedic-layer/profile.json` — the raw aggregate output this page quotes.
- Source dump: DCS-conllu 2022-08-09 release, local at `~/Documents/GitHub/DCS-conllu` (5,464,818 words; not vendored here).

_Гасунс_
