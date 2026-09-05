# Methodology — How this master directory is built

## Objective
Produce an extensive, reproducible directory of **every place the exact names
`Zazie Productions` and `Zazie Kanwar-Torge` are indexed, named, credited, or listed** on
the public web — across press, film, publications, profiles, music platforms, compilations
(the part already curated in the Media Master) **and** across search engines / meta-search
aggregators (the part the raw link dump and this project expand).

## Definition of "counts" (target name sequence)
A record counts when a page renders, or is publicly indexed with, **at least one occurrence of
the "Zazie Productions" name sequence** (target 1) or the exact person name **`Zazie Kanwar-Torge`**
(target 2).

### Target 1 — "Zazie Productions" sequence (contiguous, any spacing/case)
The words *Zazie* + *Productions* in that order, contiguous. Any separator or casing is accepted
because it is the same sequence:
- `Zazie Productions` (space)
- `ZazieProductions` (no space)
- `Zazie_Productions` (underscore)
- `zazieproductions` / `ZAZIEPRODUCTIONS` / `zazie production`-style case variants, and the
  platform-URL form `zazieproductions` (e.g. `hackaday.io/ZazieProductions`,
  `soundbetter.com/profiles/…-zazie-productions`, `github.com/zazieproductions`).

A target-1 hit does **not** require the person's name to appear.

### Target 2 — "Zazie Kanwar-Torge" (exact person name)
The exact string `Zazie Kanwar-Torge` (space between given name and the hyphenated surname).
Contiguous case/space variants of *this* sequence (`ZazieKanwar-Torge`, `Zazie Kanwar-Torge`
no-space, `zazie-kanwar-torge`) **do not** count on their own — the user restricted the
contiguous-sequence broadening to the **Productions** name only.

### Excluded by definition (other name sequences)
- A completely different person/entity: the French singer **Zazie**, **Zazie Films**,
  same-surnamed producers, **Zazie Beetz**, etc.
- Pages that merely repeat the name but are unrelated (see the SEO-spam category — kept but
  **flagged**, never presented as authoritative).
- `Zazie Prod`, `DAS Zazie`, hyphen-en-dash variants (`Zazie Kanwar–Torge`), and any other
  reordering/spacing of words that is not the contiguous *Zazie Productions* sequence.

## Trust tiers
| Tier | Meaning |
|---|---|
| **A** | Strong independent / institutional press, film, awards, recognition. |
| **B** | Supporting profiles, catalogs, official properties, streaming pages. |
| **C** | Compilations, community/wiki/fan indexes, lower-priority pages. |
| **D** | Auto-generated mirrors / SEO link-farm spam. Kept for completeness, **flagged**. |

## Categories
- Press & Editorial · Film, Festivals & Exhibitions · Publications & Recognition ·
  Profiles & Catalogs · Streaming & Music Platforms · Music Compilations ·
  Official Properties & Channels · Podcasts & Broadcasts · Community, Wiki & Fan Indexes ·
  Search-Engine Index · Video Mirror / Backlink Sites · SEO Spam / Link Farm

## Sources
| `source` value | Origin |
|---|---|
| `media_master` | The 133 verified URL-level records in `Zazie_Media_Master (1).pdf`. |
| `link_dump` | The raw links in `Random Zazie Productions links .pdf`. |
| `research` | Links discovered during this project's search-engine pass. |

## Search-engine method
- Always **exact-phrase** (`"name"`) queries so results contain the literal name.
- Query the **same two names** against each engine/aggregator: `"Zazie Productions"`,
  `"Zazie Kanwar-Torge"`.
- Record, per engine: **accessible?**, **what it surfaced**, and **blocking behavior**.
  See `data/research/search_engine_audit.md`.
- Independent crawlers (Marginalia, Brave) are especially valuable for underground /
  netlabel content that Big-Tech engines deprioritize.

## Reproducibility
- `data/master/master_index.csv` is the canonical, filtered, deduplicated index.
- `scripts/generate_docs.py` regenerates the per-category Markdown and the summary from
  that CSV (run `python3 scripts/generate_docs.py`).
- Category assignment and trust tier are deterministic from URL host + curated overrides,
  so the directory can be rebuilt and expanded.

## Verification
`status` defaults to `unverified`. Each row should be opened and checked during the
verification week: does the page render, and does it contain the exact name? Verified rows
should be updated to `verified` (or `dead` / `404` when they no longer resolve).

## Boundary (stated honestly)
No public-web search can prove absolute completeness across deleted, private, paywalled,
print-only, social-only, unindexed, or region-restricted media. This is an extensive,
reproducible census **as of the research date**, not a mathematical guarantee of totality.
