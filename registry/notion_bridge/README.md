# 🔗 Notion Bridge — the census ↔ Notion continuity layer

> **This directory is a register, not evidence.** It carries no research truth: it records
> *which Notion object is wired to which repo artifact, and in which direction*. Every link
> that enters the census still enters through a dated pass with evidence — see the ground rules
> in the root README and standing job #1 in `agent/AGENT_MEMORY.md`.

## 🧭 What this bridges

The census lives in this repo (research, tiers, statuses, both PDFs). The Notion workspace —
**Media Coverage**, the **Coverage** database, the **Deep Web Engine** page — holds the
outreach and working lists around the same appearances. Until 2026-10-07 neither side knew the
other existed. This bridge is the seam.

| Side | Role | Authority |
|---|---|---|
| `data/`, `registry/`, `scripts/`, the two PDFs | the census | **source of truth** |
| Notion — hub, intake DB, Coverage, pages | working surface + intake | derived; never a census source |

**Rule:** when Notion and the repo disagree, the repo wins and Notion gets refreshed. A Notion
link is a *candidate*; it becomes a census record only after the exact name is seen rendering on
the page and a pass ledger records it.

## 📄 The map

[`notion_object_map.csv`](notion_object_map.csv) — one row per Notion object, with its ID, its
repo counterpart, the direction of the relationship and an evidence note. Read it before
touching any Notion object that a build depends on, and update it in the same session as any
change to the objects it lists.

**Column convention (matters):** the map deliberately uses **none** of the URL column names that
`scripts/ingest_all_links.py` harvests into census records (`URL`, `url`, `Link`, `link`,
`listen_url`, `url_or_asset`, `ArchiveLink`, `discogs`, `DuplicateURLs`, `backlink`, `ResultURL`,
`CanonicalURL`), nor any of its tier/status/notes/date column names. The ingest globs
`registry/**/*.csv`, so a careless column name here would silently create fake records. Keep it
that way: `NotionID`, `NotionURL`, `RepoArtifact`, `Relationship`, `Direction`, `VerifiedOn`,
`EvidenceNote` are all inert on purpose.

## 🔁 The two flows

**Notion → repo (intake).** A candidate link is dropped in the **Backlink Submissions** database
(hub page → child database) or surfaces as a published Coverage row. The agent opens the target,
checks whether an exact name (*Zazie Productions* / *Zazie Kanwar-Torge*) renders, and if it does,
records it as a dated pass — `registry/user_submitted_<YYYY-MM-DD>/` with a submission ledger, a
duplicate map and a source access log (smallest complete example:
`registry/user_submitted_link_2026-09-24/`), plus one curated `master_index.csv` row. Then rebuild
steps 1→4 and bump the counts. The submission row is marked `Ingested` with the pass folder, or
`Duplicate` / `Not exact name` with the reason.

**Repo → Notion (mirror).** After any change to the numbers, the hub page's *Where things stand*
table and *Open loops* list are refreshed from `agent/AGENT_MEMORY.md` — same session, with the
as-of date. The hub is a mirror with a date on it; the memory file is the resume point.

## 🔒 No secrets here

The bridge is operated by the agent through its connected Notion app (session-scoped). No API
key, token or `.env` content is ever committed to this directory or referenced by it — the same
rule as `agent/` (see *What never goes in `agent/`*). If a future session automates the bridge
with a script, the credential lives outside the repo and the script references it by name only.

## 🛠️ Changing the bridge

1. Update the Notion object (page, database, property).
2. Update its row in `notion_object_map.csv` — including `VerifiedOn`.
3. If the change affects counts or loops, mirror it into `agent/AGENT_MEMORY.md` (📍 / 🌀) and the
   hub page in the same session.
4. If the change touches anything under `data/` or the PDFs: rebuild steps 1→4 in `.venv`
   (`python3 -m venv .venv && ./.venv/bin/pip install pymupdf reportlab`) and confirm
   `git status --porcelain data/` is **clean** — a dirty rebuild means evidence drifted, not that
   the check is flaky. The ingest now hard-fails if `pymupdf` is missing rather than rewriting PDF
   provenance silently (L-007, fixed 2026-10-07).

## 🔗 Live objects

- Hub: **🧭 Backlink Census — Continuity Hub** (child of *Media Coverage*)
- Intake: **📥 Backlink Submissions** (child of the hub)
