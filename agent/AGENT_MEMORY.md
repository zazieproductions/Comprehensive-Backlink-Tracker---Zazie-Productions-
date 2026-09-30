# 🧠 AGENT_MEMORY — Comprehensive Backlink Tracker

> **Agents: read this first, every session.** Living working state for whoever picks up next.
> Ops layer only — research truth lives in `data/`, `registry/`, `sources/`, `scripts/` and the two
> PDFs; this file never overrides them (when in doubt, `data/` wins and this file gets fixed).
> Rituals and rules: [`agent/README.md`](README.md).

**Last updated:** 2026-09-24 ·
**Last session:** [`2026-09-24-castro-bmc-radio-backlink`](sessions/2026-09-24-castro-bmc-radio-backlink.md) ·
**Branch:** `arena/01a0d1a8-comprehensive-backlink-tracker`

## 🎯 Mission

Exact-name census of every public appearance of the artist names **Zazie Productions** and
**Zazie Kanwar-Torge** — backlinks, media features, stream credits, engine indexes, mirror
syndication and archival records. Every link is tier-ranked (A–D), status-checked and
colour-coded. Research baseline **2026-09-05**, extended by four user-submitted passes (three on
2026-09-15, one on 2026-09-24) through **2026-09-24**. Two permanent deliverables: 📕 Master Directory PDF and 📓 Research Annex PDF.

## 📍 Current state (as of 2026-09-24)

| Figure | Value | Where it lives |
|---|---|---|
| records | 755 | `data/master/consolidated_directory.json` |
| engine endpoints | 73 | same |
| canonical URL rows | 635 | `data/master/master_index.csv` (one row per URL) |
| media types | 14 | root README badge / PDF PART III |
| curated projects | **124** = 102 multi-link + 22 single-link | `data/master/project_clusters.json` (`multi_link_projects` / `single_link_projects`) |
| project-cluster rows | 424 = 402 rows in the 102 multi-link projects + 22 single-link rows (407 unique URLs; some links shared across projects) | `data/master/project_clusters.csv` |
| links in no project | 348 = 755 records − 407 unique project URLs (`counts.unassigned_links`) | `data/master/project_clusters.json` |
| compilation appearances | 61 | `data/master/listen_links.csv` |
| Research Annex sections | 17 + appendix A | `scripts/build_research_annex_pdf.py` (one hard-coded section per user pass) |

- Pipeline healthy: `sources/` → `registry/` → `scripts/` → `data/master/` → PDFs. Both PDFs current
  with the data; root README badge counts match. **Steps 1→4 are now idempotent** — the ingest no
  longer reads the project pass's own output (see decision log 2026-09-24); a re-run is byte-identical.
- **Number reconciliation (so nobody "fixes" a non-bug):** the README headline *"102 projects,
  402 links"* (Master Directory PART I) counts **multi-link** projects only. The project register
  curates **124** projects in total (the extra 22 are single-link projects). Both numbers are
  correct; they measure different things. 402 + 22 = the 424 rows of `project_clusters.csv`.
- **Figures corrected from the data on 2026-09-24** (they were stale before that session, not moved
  by it): README "links with no project" 338 → **348**; README role band *Reference* 43 → **44**;
  project-register README "400 links" → 402 and "743 records" → 755.

## 🔁 Standing jobs (the recurring playbook)

1. **New user-submitted links arrive** → create a dated `registry/user_submitted_*/` pass
   (submission ledger + duplicate map + access log — copy the pattern of the 2026-09-15 passes; the
   smallest complete example is `registry/user_submitted_link_2026-09-24/`) + one curated
   `master_index.csv` row per new URL → `ingest_all_links.py` → project pass → both PDFs → bump every
   count (root README + this file). Each pass also gets its own **Annex section** in
   `build_research_annex_pdf.py`: data reads, TOC row + unique banner colour, cover stat, the two intro
   sentences, the "N colour-coded registers" subtitle, and the root README §-table row. A new platform
   host (podcast directory, store…) may need a `HOST_ROLE` entry in `build_project_sections.py`, or it
   falls through to role `reference`.
2. **New project to curate** → exactly one row in `registry/project_sections/projects.csv` per its
   README (alias / URL pin / evidence-note phrase — **never** fuzzy matching) → rebuild step 2.
3. **Link decay / re-verification** → add a reverify ledger in the pass dir (pattern:
   `registry/maxdepth_pass_2026-09-05`); never edit old ledgers in place.
4. **Anything that changes counts** → regenerate steps 1→4 (root README §♻️) and update, in one
   session: root README badges & prose, and 📍 in this file.

## 🧠 Decision log (append-only)

| Date | Decision | Why | Session |
|---|---|---|---|
| 2026-09-21 | Adopted `agent/` memory + handoff convention | Agent sessions are amnesiac; git-backed memory lets each session resume exactly where the last stopped (from the 24/7-personal-agent discussion — the "memory & runbook" build the user picked) | [2026-09-21](sessions/2026-09-21-agent-memory-convention.md) |
| 2026-09-21 | Ops layer lives in `agent/`, a documented narrow exception to the "no narrative Markdown" ground rule | Same class of doc as `registry/project_sections/README.md`: working instructions + state, not research narrative | same |
| 2026-09-24 | A single submitted link still gets the full pass treatment: dated dir `registry/user_submitted_link_2026-09-24/` + curated master row + Annex §17 (banner `#3949ab`, the Podcasts & Broadcasts colour) | Standing job #1; uniform provenance whatever the batch size | [2026-09-24](sessions/2026-09-24-castro-bmc-radio-backlink.md) |
| 2026-09-24 | `castro.fm` → `distribution` in the global `HOST_ROLE` table (not a per-project `role_overrides`) | It is a podcast directory like tunein/ivoox/podbean/listennotes on every project; unmapped hosts fall through to `reference` | same |
| 2026-09-24 | Ingest excludes the derived `data/master/project_clusters.csv` (`DERIVED_OUTPUTS` in `ingest_all_links.py`) | It globs `data/**/*.csv`, so every rebuild after the first looped the project pass back in: 66 unverified→verified promotions, 161 injected dates, 276 score / 695 rank changes, no evidence. With the exclusion, HEAD rebuilds byte-identically and the pipeline is idempotent | same |
| 2026-09-24 | Annex contents-grid chip index fixed (`enumerate(TOC)` from 0) | The grid has no header row, so every chip sat one row low (row 1 blank, appendix in §16's colour); the new §17 row would have shown §16's colour | same |
| 2026-09-24 | Page renders **both** names → `master_index` target = `Zazie Kanwar-Torge`; the pass ledger's Target lists both | Follows the 2026-09-15 rows (Clan Analogue track page, exibart event page) | same |

## 🌀 Open loops

| ID | Loop | Next step | Since |
|---|---|---|---|
| L-001 | 24/7 personal-agent stack (user exploring: OpenClaw deploy kit · GitHub Actions cron workers · monitoring/heartbeats) | User picks the next build when ready; full map + options in the session note | 2026-09-21 |
| L-002 | ~~_(nothing pending in the data pipeline — clean)_~~ ✅ 2026-09-24 — superseded: that session found and fixed an ingest feedback loop and opened L-003…L-006 | — | — |
| L-003 | Adjacent leads, unopened: `USL24-01…03` (Castro / Pocket Casts / Overcast **show** pages of Black Mountain College Radio, in `registry/user_submitted_link_2026-09-24/adjacent_leads.csv`) — plus `USL15-01…04` (Kinorium titles) from the 2026-09-15 third batch, never tracked here before | Open each; record (new dated pass) only if the exact name renders on the page | 2026-09-24 |
| L-004 | Master Directory contents grid paints every chip **one row low** — same header-less-grid bug fixed in the Annex this session, but encoded in ~12 hand-written row offsets (`toc_extra` in `build_master_directory_pdf.py`, ~L756-771: band tints, chips, separator rules) | Flagged to the user, not fixed (pre-existing, outside that session's task). With an OK: shift every `toc_extra` row index by −1 (keep `-1` end rows), rebuild, check page 7 visually | 2026-09-24 |
| L-005 | Latent: `harvest_csv` computes status with `'verified' in live`, so a cell reading "unverified" harvests as verified. **0 records affected today** (a higher-priority `master_index` status always wins); it only amplified the L-002 loop | Optional fix: word-boundary test; must still rebuild byte-identical to the current census | 2026-09-24 |
| L-006 | Page-map caches (`data/master/.pdf_pagemap.json`, `.annex_pagemap.json`) are only re-measured when **absent** — with a stale cache the contents pages keep old page numbers | Documented (root README ♻️ tip + pitfall 1). Optional code fix: re-run pass 2 whenever the measured map differs from the cached one | 2026-09-24 |

## 🧰 Quick how-to (details in root README)

- Rebuild everything, in order: `python scripts/ingest_all_links.py` →
  `python scripts/build_project_sections.py --report` → `python scripts/build_master_directory_pdf.py` →
  `python scripts/build_research_annex_pdf.py` (Python 3 + `reportlab` + `pymupdf`; `.venv/` is git-ignored).
- Verify counts before trusting this file:
  `python -c "import json; d=json.load(open('data/master/consolidated_directory.json')); print(len(d['records']), len(d['engine_endpoints']))"`
- Project arithmetic check: `project_clusters.csv` rows should equal
  `multi_link_projects' links + single_link_projects` (402 + 22 = 424 today).
- Before the final build: `rm -f data/master/.pdf_pagemap.json data/master/.annex_pagemap.json`
  (see L-006), then run steps 1→4. A baseline rebuild on an untouched checkout must leave
  `git status` clean for `data/` — if it doesn't, stop and find out why before adding anything.

## ⛔ Pitfalls distilled (for agents)

1. **Never edit the PDFs by hand** — regenerate. Page-number caches are git-ignored and only
   re-measured when absent: delete both before the final build (L-006).
2. **Never invent links.** Every URL enters through a pass ledger with evidence + access log.
   Tier D is quarantined (Annex §8 safety charter) — printed last, always marked, never promoted
   without new evidence.
3. **Projects are curated, never guessed** — membership must trace to one rule in `projects.csv`.
4. **One palette, everywhere** — colours are defined in the two build scripts; the README legend
   mirrors them.
5. **Counts live in three places** (data files · root README badges/prose · this file) — change one,
   change all, same session.
6. **Memory is never the source of truth** — when this file and `data/` disagree, `data/` wins.
7. **Registry column names decide what becomes a record.** `harvest_csv` turns every URL in the
   `URL` / `url` / `ResultURL` / `CanonicalURL` / `Link` / `link` / `listen_url` / `url_or_asset` /
   `ArchiveLink` / `discogs` / `DuplicateURLs` / `backlink` columns into a census record. Put leads
   in `LeadURL`, duplicate maps in `Canonical` / `Variants`, and no-count probes in `ProbeURL`.
8. **Words that auto-quarantine.** A record whose merged notes contain LOWTRUST / SEO-POISON /
   DOORWAY / SCRAPE-CLONE / PARASITE / PIRATE / AUTO-GENER / FABRICATED / SPAM / HIJACK / SYNDICAT
   in their **first 200 characters** is filed Tier D. Master rows come first in that merge, so keep
   those words out of the opening of a new `master_index.csv` note (write "distributes", not
   "syndicates").
9. **Derived outputs under `data/` must be listed in `DERIVED_OUTPUTS`** (`ingest_all_links.py`) —
   the ingest globs `data/**/*.csv`, and anything it reads back becomes evidence.

## 📜 Session index

| Date | Session note | Branch | Summary |
|---|---|---|---|
| 2026-09-21 | [agent-memory-convention](sessions/2026-09-21-agent-memory-convention.md) | `arena/01a0c52f-comprehensive-backlink-tracker` | Created this convention (from the 24/7-agent discussion); no data changes |
| 2026-09-24 | [castro-bmc-radio-backlink](sessions/2026-09-24-castro-bmc-radio-backlink.md) | `arena/01a0d1a8-comprehensive-backlink-tracker` (PR [#20](https://github.com/zazieproductions/Comprehensive-Backlink-Tracker---Zazie-Productions-/pull/20)) | +1 record (castro.fm BMC Radio Art episode → project `bmc-radio`, Tier B, live) → 755; fixed the ingest feedback loop + Annex contents chip offset; Annex §17 |
