# 🧩 Project register — how the census is grouped by *thing*, not by media type

The Master Directory prints the census by media type, which is the right shape for a directory and the
wrong shape for a reader: one commission, compilation or anthology ends up spread across a museum page,
three podcast directories, a Discogs release, an archive copy, a netlabel news repost and a lyric
database. This register re-cuts the same 727 records by **project** — the thing the links are actually
about — and drives **PART I** of `Zazie_Master_Directory_COLOUR_CODED.pdf`.

```
registry/project_sections/projects.csv     ← the curated register (this is the editable surface)
        │
        │  scripts/build_project_sections.py   (run automatically by the master PDF build)
        ▼
data/master/project_clusters.json          ← projects + their links, roles, counts
data/master/project_clusters.csv           ← the same, flattened: one row per link
        │
        ▼
Master Directory PDF · PART I              Research Annex PDF · §14
```

## The file

One CSV row per project. Columns:

| Column | Meaning |
|---|---|
| `project_id` | stable slug; used for the PDF bookmarks and the page map. A row whose `project_id` starts with `#` is a comment. |
| `name` | the section title printed in the PDF |
| `kind` | project type — `Film`, `Radio commission`, `Anthology`, `Compilation appearance`, `Exhibition / biennale`, `Press feature`, `Release (own)`, `Software`, … (also picks the banner colour) |
| `year` | year (or year range) the thing belongs to |
| `artist_role` | what the artist actually did — printed as the section's *Artist credit* line |
| `summary` | one-line description printed under the section banner |
| `anchor` | the single link a reader should open first |
| `match_phrases` | `\|`-separated phrases; a link joins when a phrase is found in its **URL or title** (accents/case folded, word-bounded) |
| `loose_phrases` | `\|`-separated token sets; every token must appear — for pages that reword the title. Use sparingly. |
| `exclude` | `\|`-separated phrases that veto a match (this is how a project stops swallowing pages that merely mention it) |
| `pin` | `\|`-separated URL fragments that force a link into the project. Also the tool for links the census stores with a **truncated URL**. |
| `notes_match` | phrases matched inside the record's evidence notes (for hosts whose page title never names the project) |
| `notes_hosts` | `;`-separated host list that `notes_match` is allowed to fire on — always restrict it |
| `canonical_hosts` | `;`-separated hosts that count as *the project's own page* (role `canonical`) |
| `press_hosts` | `;`-separated hosts that count as *press coverage of this project* (role `press`) |
| `role_overrides` | `host-or-url-fragment=role` pairs, e.g. `youtube-nocookie=quarantine` — used for TMDB-id clones and embed farms |
| `register_refs` | 2026 Accomplishment Register entry numbers this project answers to |
| `source` | `curated` for hand-written rows; `auto:listen_links` for rows derived from `data/master/listen_links.csv` |

## The rules the script enforces

* **A phrase must appear in the URL or the title** — matching is deterministic and word-bounded, never fuzzy.
  A project section can therefore be audited from the register alone.
* **Pins need a path.** A pin such as `label.bandcamp.com/album/x` may match the census's truncated form of
  the same URL, but a bare host (`label.bandcamp.com`) never claims every release on that host.
* **Quarantine wins.** A tier-D record is always filed under the `quarantine` role, whatever else it is.
* **Everything else gets a role** from the host table in `scripts/build_project_sections.py`
  (`canonical → credit → catalogue → distribution → media → press → event → reference → mirror → archive → quarantine`),
  and the roles are printed in that order inside each project.
* **Compilations are never silently dropped.** Every compilation in `data/master/listen_links.csv` gets a
  project row automatically, pinned to its Discogs release and listen URL — so a compilation whose pages never
  print its own name in a title still collects its own links. A curated row with the same name wins.

## Adding or fixing a project

1. Add (or edit) one row in `projects.csv`. Quote every field that contains a comma; separate multiple
   values with `|`.
2. Run `python3 scripts/build_project_sections.py --report`. The report lists every project it matched,
   every project that matched nothing, and — most usefully — **which hosts with two or more links are still
   outside every project**: that list is the curation backlog.
3. Rebuild the volumes: `python3 scripts/build_master_directory_pdf.py` (it runs the pass itself) and
   `python3 scripts/build_research_annex_pdf.py`.

Links that faithfully describe the **artist** rather than one project (platform profiles, streaming pages,
the artist's own catalogue, artist-level press, community and quiz pages, metadata scrapers) are
deliberately left out of PART I and stay in full in the media-type sections and Appendix A. A project
section means *the link is about that thing* — nothing wider.
