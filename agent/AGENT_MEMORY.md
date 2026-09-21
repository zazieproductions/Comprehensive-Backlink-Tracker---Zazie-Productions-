# 🧠 AGENT_MEMORY — Comprehensive Backlink Tracker

> **Agents: read this first, every session.** Living working state for whoever picks up next.
> Ops layer only — research truth lives in `data/`, `registry/`, `sources/`, `scripts/` and the two
> PDFs; this file never overrides them (when in doubt, `data/` wins and this file gets fixed).
> Rituals and rules: [`agent/README.md`](README.md).

**Last updated:** 2026-09-21 ·
**Last session:** [`2026-09-21-agent-memory-convention`](sessions/2026-09-21-agent-memory-convention.md) ·
**Branch:** `arena/01a0c52f-comprehensive-backlink-tracker`

## 🎯 Mission

Exact-name census of every public appearance of the artist names **Zazie Productions** and
**Zazie Kanwar-Torge** — backlinks, media features, stream credits, engine indexes, mirror
syndication and archival records. Every link is tier-ranked (A–D), status-checked and
colour-coded. Research baseline **2026-09-05**, extended by three user-submitted intake passes
through **2026-09-15**. Two permanent deliverables: 📕 Master Directory PDF and 📓 Research Annex PDF.

## 📍 Current state (as of 2026-09-21)

| Figure | Value | Where it lives |
|---|---|---|
| records | 754 | `data/master/consolidated_directory.json` |
| engine endpoints | 73 | same |
| canonical URL rows | 634 | `data/master/master_index.csv` (one row per URL) |
| media types | 14 | root README badge / PDF PART III |
| curated projects | **124** = 102 multi-link + 22 single-link | `data/master/project_clusters.json` (`multi_link_projects` / `single_link_projects`) |
| project-cluster rows | 423 = 401 rows in the 102 multi-link projects + 22 single-link rows (406 unique URLs; some links shared across projects) | `data/master/project_clusters.csv` |
| compilation appearances | 61 | `data/master/listen_links.csv` |

- Pipeline healthy: `sources/` → `registry/` → `scripts/` → `data/master/` → PDFs. Both PDFs current
  with the data; root README badge counts match.
- **Number reconciliation (so nobody "fixes" a non-bug):** the README headline *"102 projects,
  401 links"* (Master Directory PART I) counts **multi-link** projects only. The project register
  curates **124** projects in total (the extra 22 are single-link projects). Both numbers are
  correct; they measure different things. 401 + 22 = the 423 rows of `project_clusters.csv`.

## 🔁 Standing jobs (the recurring playbook)

1. **New user-submitted links arrive** → create a dated `registry/user_submitted_*/` pass
   (submission ledger + duplicate map + access log — copy the pattern of the 2026-09-15 passes)
   → `ingest_all_links.py` → project pass → both PDFs → bump every count (root README + this file).
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

## 🌀 Open loops

| ID | Loop | Next step | Since |
|---|---|---|---|
| L-001 | 24/7 personal-agent stack (user exploring: OpenClaw deploy kit · GitHub Actions cron workers · monitoring/heartbeats) | User picks the next build when ready; full map + options in the session note | 2026-09-21 |
| L-002 | _(nothing pending in the data pipeline — clean)_ | — | — |

## 🧰 Quick how-to (details in root README)

- Rebuild everything, in order: `python scripts/ingest_all_links.py` →
  `python scripts/build_project_sections.py --report` → `python scripts/build_master_directory_pdf.py` →
  `python scripts/build_research_annex_pdf.py` (Python 3 + `reportlab` + `pymupdf`; `.venv/` is git-ignored).
- Verify counts before trusting this file:
  `python -c "import json; d=json.load(open('data/master/consolidated_directory.json')); print(len(d['records']), len(d['engine_endpoints']))"`
- Project arithmetic check: `project_clusters.csv` rows should equal
  `multi_link_projects' links + single_link_projects` (401 + 22 = 423 today).

## ⛔ Pitfalls distilled (for agents)

1. **Never edit the PDFs by hand** — regenerate. Page-number caches are git-ignored.
2. **Never invent links.** Every URL enters through a pass ledger with evidence + access log.
   Tier D is quarantined (Annex §8 safety charter) — printed last, always marked, never promoted
   without new evidence.
3. **Projects are curated, never guessed** — membership must trace to one rule in `projects.csv`.
4. **One palette, everywhere** — colours are defined in the two build scripts; the README legend
   mirrors them.
5. **Counts live in three places** (data files · root README badges/prose · this file) — change one,
   change all, same session.
6. **Memory is never the source of truth** — when this file and `data/` disagree, `data/` wins.

## 📜 Session index

| Date | Session note | Branch | Summary |
|---|---|---|---|
| 2026-09-21 | [agent-memory-convention](sessions/2026-09-21-agent-memory-convention.md) | `arena/01a0c52f-comprehensive-backlink-tracker` | Created this convention (from the 24/7-agent discussion); no data changes |
