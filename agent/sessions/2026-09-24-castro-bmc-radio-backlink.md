# 📋 Session handoff — 2026-09-24 · castro-bmc-radio-backlink

**Branch:** `arena/01a0d1a8-comprehensive-backlink-tracker` · **PR:** [#20](https://github.com/zazieproductions/Comprehensive-Backlink-Tracker---Zazie-Productions-/pull/20) · **Merged to main:** pending — merging #20 completes the ritual

## 🙋 What was asked

> "https://castro.fm/episode/6w8RTd another backlink I found"

## 🛠️ What was done

- **Verified the link.** It is Castro's episode page for *BMC Radio Art: Zazie Productions - Cheaper
  Impressions* on **Black Mountain College Radio**, the Black Mountain College Museum + Arts Center podcast
  (15 Dec 2021, 4 min). Both exact names render on the page: "Zazie Productions" in the title and
  "Zazie Kanwar-Torge (they/them)…" in the show notes. The sandbox shell can't reach castro.fm (TLS reset;
  bing.com fails the same way while github.com and pypi.org answer), so the page was read through
  `fetch_page`. Both attempts are logged.
- **Recorded it as one new record** (755 total): Podcasts & Broadcasts · Tier B · verified · 2021-12-15,
  with a curated row in `master_index.csv` and a new pass dir `registry/user_submitted_link_2026-09-24/`
  (ledger `USB24-01`, same-episode map `DUP-017`, leads `USL24-01…03`, access log).
- **Project:** it joins `bmc-radio` via that rule's existing title phrases (`bmc radio art`,
  `cheaper impressions`). No `projects.csv` edit was needed. `castro.fm` was added to `HOST_ROLE` →
  `distribution`, beside the other podcast directories. BMC RADIO ART now has 23 links (distribution 9).
  castro.fm is a new host, not a new credit: the commission was already counted, and the episode was
  already catalogued on Apple Podcasts, SoundCloud, iVoox, podcast365.ro and Listen Notes.
- **Found and fixed a pipeline feedback loop** before adding anything. A baseline rebuild of the
  *untouched* repo changed 66 statuses, 161 dates, 276 scores and 695 ranks. Cause: `ingest_all_links.py`
  globs `data/**/*.csv`, which includes `data/master/project_clusters.csv`, the output of step 2. That file
  is now excluded (`DERIVED_OUTPUTS`). The HEAD rebuild is byte-identical, and steps 1→4 are idempotent.
- **Annex §17** added (banner `#3949ab`): ledger, same-episode surface map, leads, fetch log and the
  pipeline-fix note. Cover stat, intro, TOC and subtitle all say 17 now.
- **Fixed the Annex contents chips.** They were painted one row low; the grid has no header row, but
  `enumerate(TOC, start=1)` assumed one. Every chip now matches the README colour table.
- Counts bumped in the root README (badges, prose, tables, repo map), the project-register README and
  📍 memory. Several figures were *already* stale and were corrected from the data (see 📍 note).

## 📁 Files touched

| File | Change |
|---|---|
| `registry/user_submitted_link_2026-09-24/submission_ledger.csv` | new — `USB24-01`, the verdict + evidence |
| `registry/user_submitted_link_2026-09-24/duplicate_map.csv` | new — `DUP-017`: the same episode on 5 catalogued surfaces, kept separate, credit not double-counted |
| `registry/user_submitted_link_2026-09-24/adjacent_leads.csv` | new — `USL24-01…03` show-level player pages (not opened; `LeadURL` is never harvested) |
| `registry/user_submitted_link_2026-09-24/source_access_log.csv` | new — fetch_page 200 (worked) + curl 000 (sandbox egress) |
| `data/master/master_index.csv` | +1 curated row (castro.fm) |
| `data/master/consolidated_directory.json` | regenerated — 755 records; `generated_from_repo_date` 2026-09-24 |
| `data/master/project_clusters.json` / `.csv` | regenerated — `bmc-radio` +1 link; 424 rows / 407 unique URLs |
| `scripts/ingest_all_links.py` | `DERIVED_OUTPUTS` exclusion + docstring; census date 2026-09-24 |
| `scripts/build_project_sections.py` | `HOST_ROLE['castro.fm'] = 'distribution'` |
| `scripts/build_research_annex_pdf.py` | §17 + TOC/cover/intro wiring; contents-chip index fix |
| `Zazie_Master_Directory_COLOUR_CODED.pdf` | regenerated (221 pp · 755 links) |
| `Zazie_Research_Annex_COLOUR_CODED.pdf` | regenerated (68 pp · 17 sections + appendix) |
| `README.md` | counts, badges, §17 row, repo map, regenerate tip |
| `registry/project_sections/README.md` | current-state figures (402 / 348 / 755), Annex §15 reference |
| `agent/AGENT_MEMORY.md` | 📍 · 🧠 · 🌀 · 📜 · how-to · pitfalls 7–9 |

## ✅ Verification

- [x] Live-count checks run before trusting memory: 754 / 73 / 634 / 124 (102 + 22) / 423 (406 unique) / 61, all matching memory
- [x] Regenerate steps 1→4 run from an empty page-map cache; the re-run of steps 1+2 is byte-identical (idempotent)
- [x] Root README badges/prose counts updated
- [x] `AGENT_MEMORY.md` updated (📍 state · 🧠 decision log · 🌀 open loops · 📜 session index)

```
# baseline, untouched checkout, ingest WITH the fix:   consolidated_directory.json byte-identical to HEAD
# delta vs HEAD after the new row:                      +1 record (castro.fm/episode/6w8rtd); only `rank`
#                                                       changed on existing records (606 shifted by one)
consolidated_directory: 755 records, 73 engine endpoints (generated_from_repo_date 2026-09-24)
master_index.csv:       635 rows
project_clusters.json:  124 projects (102 multi-link, 22 single-link); unassigned 348; shared 13
project_clusters.csv:   424 rows = 402 (multi-link) + 22 (single-link); 407 unique URLs
listen_links.csv:       61 rows
new record:             https://castro.fm/episode/6w8RTd · Podcasts & Broadcasts · tier B · verified · score 83 · rank 149 · flags []
project membership:     only bmc-radio changed — +castro.fm as distribution (B, verified)
PDFs:                   Master p.19 (PART I · BMC RADIO ART), p.122 (§4 Podcasts), p.83 (Path 3), p.201 (App. A);
                        Annex §17 pp.65-66; contents page numbers == PDF outline for all 18 entries
```

## 🧠 Decisions (→ mirrored in the AGENT_MEMORY.md decision log)

| Decision | Why |
|---|---|
| Full pass treatment for a single link (dated dir + master row + Annex §17) | Standing job #1; provenance stays uniform whatever the batch size |
| Tier **B**, category Podcasts & Broadcasts | "Supporting platform record" (tier legend); same tier as the Listen Notes copy of this episode |
| `castro.fm` → `distribution` in the global `HOST_ROLE` table | It is a podcast directory everywhere, not only in `bmc-radio`; unmapped hosts become `reference` |
| Exclude `project_clusters.csv` from the ingest | Downstream output looping back in as evidence; the exclusion restores byte-identical rebuilds |
| Fix the Annex contents-chip index; only flag the Master one (L-004) | The Annex bug mis-coloured the row this session added; the Master bug is pre-existing and unrelated |
| Both names on the page → master target `Zazie Kanwar-Torge` | Follows the 2026-09-15 rows (Clan Analogue track page, exibart event page) |

## 🌀 Open loops left

| ID | Loop | Next step |
|---|---|---|
| L-001 | 24/7 personal-agent stack (unchanged, user-parked) | User picks when ready |
| L-003 | Unopened adjacent leads `USL24-01…03` (+ `USL15-01…04` from 2026-09-15) | Open; record only on an exact-name render |
| L-004 | Master Directory contents chips one row low | Needs the user's OK — shift the `toc_extra` row indices by −1 |
| L-005 | Latent "unverified" ⊃ "verified" status substring in `harvest_csv` (0 records affected) | Optional word-boundary fix; keep the rebuild byte-identical |
| L-006 | Page-map caches only re-measured when absent | Documented; optional auto-refresh in both builders |

## 🤝 Handoff notes — next agent, read this

- **Resume point:** data pipeline clean and idempotent at 755 records. L-003 is the natural next research
  step. L-004 is a one-helper code fix waiting on the user's OK.
- **Watch out:** (1) **baseline-rebuild first.** On an untouched checkout, steps 1+2 must leave `data/`
  unchanged in `git status`; that check is how this session found the loop. (2) Delete both page-map
  caches before the final build (L-006). (3) The ingest's topic classifier matches bare substrings:
  every "Cheaper Im**press**ions" row lands in *Major press features*, which is why the whole BMC episode
  family shows up in Reading Path 3. Pre-existing and left as-is. (4) The README media-type share bars
  are hand-drawn and not strictly proportional (61 → 3 blocks, 59 → 4). Pre-existing, cosmetic, left as-is.
  (5) The sandbox shell can't reach many hosts; use `fetch_page` for verification and log the failed
  route honestly.
