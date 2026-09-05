<div align="center">

# 🔍 ZAZIE PRESENCE CENSUS — Backlink & Mention Tracker

### A week-long, agent-driven sweep to find **every** place **`Zazie Kanwar-Torge`** and **`Zazie Productions`** are indexed, named, credited, embedded, or linked — across mainstream **and** obscure search engines.

</div>

---

## 🎯 What this project is

This is the **mission homepage** for a *comprehensive, reproducible, week-long directory* of every public-web location where the artist and producer **`Zazie Kanwar-Torge`** / **`Zazie Productions`** appears — including places that only surface on **obscure engines** (SearXNG, Yandex, Bing, Brave, Mojeek, Marginalia, SearX, meta-search layers, regional engines, niche music/film databases, wiki mirrors, YouTube aggregators, archive caches, and so on).

The repo already contains a **dump of earlier research**. This directory turns that dump into an **organized, color-coded operating system** for a repeatable census:

- 📖 **Explains the task** to any future agent (scope, inclusion rules, evidence standard).
- 🗺️ **A color-coded document map** so agents know exactly where to look and what to produce.
- 🧠 **Deep-searching methods & copy-paste queries** ready to prompt agents engine-by-engine.
- 🗂️ **A seed registry** auto-extracted from the existing dump (the places found so far).
- ✅ **A verification runbook** for the “double-check that they work later” pass.
- 📊 **A live master index** of every confirmed exact-name URL discovered by the census sweeps.

> 🚩 **Important framing:** `Zazie Kanwar-Torge` and `Zazie Productions` refer to **one person / one artist project** (composer, film-scorer, experimental/noise musician, filmmaker, writer, and multimedia artist). The census deliberately tracks the *name-as-person/company*, not the unrelated French singer **“Zazie”**, the company **“Zazie Films”**, or other similarly-named entities.

---

## 🎨 COLOR-CODING SYSTEM (use this everywhere)

Colors carry **meaning** in every table below. If a viewer does not render colors, the matching **emoji + bold label** still carries the same meaning, so the files never break.

### Media-type (what kind of place it is)

| Emoji | Label | Color | Meaning |
|---|---|---|---|
| 🔴 | **Press / Editorial** | `#d93025` | Reviews, features, interviews, articles, press releases |
| 🌸 | **Film / Festivals / Exhibitions** | `#d81b60` | Film credits, screenings, festival pages, gallery shows |
| 🟣 | **Publications / Recognition / Academic** | `#7b1fa2` | Awards, anthologies, papers, honor rolls, security/credits pages |
| 🔵 | **Profiles & Catalogs** | `#1a73e8` | Streaming/artist/directory profile pages, platform catalogs |
| 🟠 | **Music & Discography** | `#e8710a` | Releases, compilations, net-labels, track credits |
| 🩵 | **Data-studies / Analytics / Tooling** | `#0f9d8f` | Stats sites, analytics dashboards, AI/research pages about the work |
| 🟢 | **Social & Community** | `#188038` | Native social posts, community pages, UGC, fan-made content |
| 📼 | **Mirrors / Aggregators** | `#607d8b` | YouTube mirrors, video aggr., RSS scrape/index mirrors (secondary) |
| 🖤 | **Spam / scraper / syndication / SEO-poisoning / low-trust** | `#616161` | Hacked-site doorways, scraped/auto-gen clones, RSS & PR republications, mirror embeds, pastes — *evidence-preservation bucket, never counted* (`registry/spam_scraper_syndication_lowtrust_2026-09-05/`) |

### Status (used during the verification pass)

| Status | Color | Meaning |
|---|---|---|
| ✅ **LIVE / VERIFIED** | `#188038` | Link works **and** the exact name is visible on the page |
| 🟡 **PARTIAL / RE-CHECK** | `#b06000` | Page loads but evidence is weak, region-gated, or JS-hidden |
| ❌ **BROKEN / NO EVIDENCE** | `#c5221f` | Dead link, 404/403, or no exact-name evidence found |
| ⬜ **UNCHECKED** | `#80868b` | Recorded but not yet double-checked (this is every seed row today) |

### Priority (used when ranking evidence strength)

- 🥇 **Priority A** — independent editorial, institutional, or database-of-record (press-kit lead)
- 🥈 **Priority B** — supporting coverage / secondary context
- 🥉 **Priority C** — self-issued profiles, own storefronts, catalog/discography rows
- 🔎 **Lead** — unverified or unresolved (do **not** count in totals)

> **Two-name rule (from the “Strict Exact-Name” master):** eligible evidence is the exact
> string **`Zazie Productions`** (the contiguous *Productions* sequence in any spacing/case:
> `Zazie Productions`, `ZazieProductions`, `Zazie_Productions`, `zazieproductions`,
> `ZAZIEPRODUCTIONS`, and platform-URL forms like `github.com/zazieproductions`) **or** the
> exact person string **`Zazie Kanwar-Torge`**. A Productions-sequence hit already counts on
> its own (it does not need the person's name alongside); the no-space person variant
> (`ZazieKanwar-Torge`) and en-dash (`Zazie Kanwar–Torge`) do **not** count on their own.

---

## 📚 DOCUMENT MAP

### Mission & method (the “why” and the “how-to-think”)

| File | What it is |
|---|---|
| [`docs/01_MISSION_SCOPE_AND_RULES.md`](docs/01_MISSION_SCOPE_AND_RULES.md) | **The master brief.** Full explanation of the task, targets, eligibility & exclusion rules, evidence standard, and output conventions. Hand this to any agent that asks “what am I doing?” |
| [`docs/02_DEEP_SEARCH_PLAYBOOK.md`](docs/02_DEEP_SEARCH_PLAYBOOK.md) | **Deep-searching methods.** Boolean/operator syntax per engine, meta-search strategy, obscure-engine technique, freshness & backlink-chasing, evidence capture. |

### Look-up references (search-time tools)

| File | What it is |
|---|---|
| [`docs/03_ENGINE_DIRECTORY.md`](docs/03_ENGINE_DIRECTORY.md) | **Color-coded engine directory.** Every engine class to run each name against (major, meta, independent, obscure/alt, regional, music, film, academic, social-native, archive) with the exact URL pattern to use. |
| [`docs/04_QUERY_LIBRARY.md`](docs/04_QUERY_LIBRARY.md) | **Copy-paste query library.** Canonical exact-name queries, near-name/handle variants, platform `site:` dorks, noise-filtering exclusions, file-type sweeps — ready to paste. |

### Execution (how a week gets run)

| File | What it is |
|---|---|
| [`docs/05_WEEK_PLAN_AND_CADENCE.md`](docs/05_WEEK_PLAN_AND_CADENCE.md) | **The 7-day plan.** Day-by-day batching, session cadence, dedupe & logging rhythm, day-7 consolidation. |
| [`docs/06_AGENT_PROMPT_TEMPLATES.md`](docs/06_AGENT_PROMPT_TEMPLATES.md) | **Prompt templates.** Ready-to-send agent briefs per phase with required output format & evidence rules. |
| [`docs/07_LINK_CHECK_AND_VERIFICATION.md`](docs/07_LINK_CHECK_AND_VERIFICATION.md) | **The “double-check they work later” runbook.** HTTP-status probing, redirect handling, exact-name grep, LIVE/PARTIAL/BROKEN tagging, rate-limit etiquette, tooling. |

### Seed registry (extracted from the dump)

| Path | What it is |
|---|---|
| [`registry/README.md`](registry/README.md) | How the live registry is structured and how to add rows. |
| [`registry/seed/SEED_INDEX_FROM_DUMP.md`](registry/seed/SEED_INDEX_FROM_DUMP.md) | **260 unique URLs** auto-extracted from the dump, clustered by media type. *(Source for the “found so far” starting set.)* |
| [`registry/spam_scraper_syndication_lowtrust_2026-09-05/`](registry/spam_scraper_syndication_lowtrust_2026-09-05/LOWTRUST_REGISTER.md) | **🖤 Low-Trust Register (Pass 10).** Charter + 89-row ledger for every spam / scraper / syndication / SEO-poisoning / text-injection occurrence of the exact strings; safety protocol; reclassification log for all pre-existing instances. |
| [`registry/seed/seed_unique_urls.csv`](registry/seed/seed_unique_urls.csv) | Machine-readable full list (domain, url, first-seen source file). |
| [`registry/seed/seed_domain_summary.csv`](registry/seed/seed_domain_summary.csv) | Domain → URL-count summary for eyeballing coverage. |

### Live master index (the deliverable)

| File | What it is |
|---|---|
| `data/master/master_index.csv` | **Canonical index.** One row per URL: url · host · target · category · trust_tier · source · date · title · status · notes. Edit/add here. |
| `data/master/SUMMARY.md` | Auto-generated counts by category, trust tier, source. |
| `data/master/categorized/` | Auto-generated per-category Markdown references (14 categories). |
| `data/master/REGISTER_LINK_MAP.md` | Maps the 2026 Accomplishment Register's 203 unlinked features to public links; marks HUNT / AUTH / lead per row. |
| `data/research/search_engine_audit.md` | Which engines index the name; which block bots; what each surfaced (Pass 1–8). |
| `docs/METHODOLOGY.md` | Inclusion rules, definition of “counts,” trust tiers, reproducibility. |
| `docs/PLAN.md` | The week-long roadmap + live checklist. |
| `scripts/generate_docs.py` | Regenerates the categorized docs + summary from the CSV. |

### Original source dump (untouched originals at repo root)

| File | Notes |
|---|---|
| `Random Zazie Productions links .pdf` | Raw link dump (the URL-rich source the seed registry was built from). |
| `Zazie_Media_Master (1).pdf` | Reading edition of the **133-record exact-name master** (Press 25 · Film 11 · Publications 6 · Profiles 31 · Compilations 60), researched through **Aug 9, 2026**. Its URLs are stored as clickable `OPEN` tokens and live in the **companion `.xlsx`/`.csv` which are *not* present in this repo**. |
| `Zazie_2026_Accomplishment_Register_Maximal_Edition.docx` | 2026 external-memory register of releases, press, selections, and professional reach (useful as a **known-ground-truth list** to cross-check the census against). |
| `resource1` | Note file (`maxintel.org` — an OSINT tool referenced as useful). |

---

## 📊 Census results (latest pass)

The search sweeps (Pass 1–10) fold confirmed exact-name URLs into the live master index.
As of the latest pass the master index holds **524 records**:

```
TOTAL                    524
  Music Compilations      117
  Spam/Scraper/Syndic./
    SEO-Poison/Low-Trust   73
  Profiles & Catalogs      63
  Streaming Platforms      52
  Press & Editorial        53
  Community/Wiki/Fan       50
  Official Properties      45
  Film, Festivals & Exhib. 41
  Publications & Recogn.   18
  Podcasts & Broadcasts     6
  Video Mirror / Backlink   2
  Music Discography         2
  Lyrics & Music Databases  1
  Search-Engine Index       1
```
Trust tiers: **A** 105 · **B** 159 · **C** 187 · **D** 73 (D = flagged spam/scraper/syndication/mirrors — see below).
Sources: media_master 132 · link_dump 252 · research 116 · regional_alt_pass 24.

> **Pass 10 — Low-Trust & Parasite Watch (2026-09-05).** A dedicated category now consolidates
> every spam / scraper / syndication / SEO-poisoning / low-trust occurrence of the two exact strings:
> `registry/spam_scraper_syndication_lowtrust_2026-09-05/` (charter, 89-entry ledger, query log,
> access log). The former `SEO Spam / Link Farm` category and all 38 Tier-D rows of
> `Video Mirror / Backlink Sites` were folded into it, together with 16 misfiled rows pulled out of
> Community/Profiles/Streaming/Press (incl. two A-tier PR-republication demotions), plus new finds
> (boomplay auto-lyrics page; live hacked-site-embed sampling; Wayback CDX transience checks;
> safety-quarantined doorway hosts left documented-but-unvisited). Nothing in Tier D ever counts
> as credible coverage, credit, profile, release, official presence, press mention, or biography.


> **Note on rule evolution:** Pass 7 broadened the inclusion standard to the contiguous
> “Productions” sequence (any spacing/case, plus platform-URL forms), per the user directive.
> Pass 8 resolved register **#64** (Infinite Self Pavilion / The Wrong Biennale) and catalogued
> the DistroKid-family platform artist pages. **Pass 9** (2026-09-05) swept **62 regional,
> independent, archival and scholarly engines/interfaces** (Baidu→Leit.is, Yep, Marginalia
> retry, YaCy, Wiby, meta-veterans, national web archives, scholarly APIs) — full access
> matrix in `registry/regional_alt_engine_pass_2026-09-05/`. Outcomes: Mail.ru confirmed as
> a captcha-free **Yandex-index access path**; **+15 Internet Archive records** (incl. the IA
> Public Domain Day Remix Contest 2026 film, a zines-collection item, and the Mystery File
> Dumps); OK.ru artist page resolved the "1 Year Anniversary" listen-link; Ghostery Search
> confirmed discontinued (closed beta 2026-06); clean negatives logged for OpenAlex, Europe
> PMC, Zenodo, LoC and Arquivo.pt. Blocked / snippet-only hits were classified as leads.

### Engine findings (one-line)
- **Indexed everywhere**, including the independent crawler **Marginalia**, which surfaced
  netlabel/bandcamp track pages the mainstream engines deprioritize.
- **Yahoo** returned the richest exact-match set; **Brave** and **Marginalia** are directly
  scrapable. **DuckDuckGo, Startpage, Yandex, Mojeek, searx.be** block bots (captcha /
  anti-bot) and need a browser or a self-hosted SearXNG instance.
- Pass 9 (2026-09-05): regional sweep — Mail.ru = captcha-free Yandex path; 360/Seznam/Yahoo!JP/Walla!/Yep/OceanHero worked; Sogou/Mojeek/Trove/Rambler blocked; BIGLOBE·Excite JP·GiveWater·Stract·BoardReader·Ask·AOL·HotBot·UK-WA dead or down;
- **+15 Internet Archive full-text records** (zines collection, PD-Day Remix Contest 2026 film, Mystery File Dumps);
- Full detail: `data/research/search_engine_audit.md` + `registry/regional_alt_engine_pass_2026-09-05/`.

---

## 📌 Current status & next actions

- [x] **Dump cataloged** — media master read; 260 real URLs extracted into `registry/seed/`.
- [x] **Operating docs written** — mission, playbook, engine dir, query library, week plan, prompts, verification runbook.
- [x] **Census run (Pass 1–10)** — 524 confirmed/flagged exact-name URLs consolidated into `data/master/master_index.csv`; register link map resolved for most features.
- [x] **Pass 10 — LOW-TRUST QUARANTINE (2026-09-05)**: every spam / scraper / syndication / SEO-poisoning / doorway / text-injection occurrence of the exact strings folded into `registry/spam_scraper_syndication_lowtrust_2026-09-05/` + master category of the same kind (73 Tier-D rows); safety protocol enforced (unsafe hosts documented, never visited).
- [ ] **Pass 2 — VERIFY** (run per `docs/07`): double-check every found link (HTTP status + exact-name evidence) and tag ✅ / 🟡 / ❌.
- [ ] **Pass 3 — CONSOLIDATE**: reconcile remaining HUNT rows (Pandora, Audiomack, Facebook/TikTok, Claro Música, Saavn/JioSaavn, Snapchat, NetEase, Tencent/QQ/Kugou/Kuwo/WeSing, Pretzel, TouchTunes, JOOX, Kuack, MediaNet, Dubset, Roblox, Soundtrack by Twitch) against the known-ground-truth register.

> **Easy first step for any agent:** open [`docs/01_MISSION_SCOPE_AND_RULES.md`](docs/01_MISSION_SCOPE_AND_RULES.md), then [`docs/05_WEEK_PLAN_AND_CADENCE.md`](docs/05_WEEK_PLAN_AND_CADENCE.md) for Day 1.

## How to use the master index
```bash
# Regenerate the categorized docs + summary from the master CSV
python3 scripts/generate_docs.py
```
To add/verify a record: edit `data/master/master_index.csv`, then re-run the script.

## Notes
- “Inclusion proves an exact-name public record exists; it does *not* independently validate
  every promotional, biographical, award, review, or profile claim made by the source.”
- Tier **D** records are preserved for completeness but are never presented as authoritative.

---

*Built for Zazie Productions · Last updated 2026-09-05 · Research baseline in dumps dated through 2026-08-09.*
