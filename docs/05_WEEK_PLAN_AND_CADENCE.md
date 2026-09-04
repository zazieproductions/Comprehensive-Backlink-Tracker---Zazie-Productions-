# 🗓️ 05 — WEEK PLAN & CADENCE (the 7-day run)

> A one-week, batched schedule that guarantees full coverage without burning out. Each day = one **engine family** against both target names. At the end of every session, **log results** and do a **10-minute spot-verify** of that day's finds. Day 7 consolidates.

**Session rhythm (every day):**
1. Re-read the mission brief once (`01`), then the day's sheet.
2. Run the day's engine family against **both** names using `04` queries.
3. Record every hit into the registry (`registry/README.md`) with evidence snippet + status `⬜` (unchecked).
4. 10-minute spot-verify of the day's strongest hits (tag ✅/🟡).
5. Note anything unresolved as a 🔎 lead.

---

## Day 1 — Baseline & major engines 🔵
**Goal:** reproduce what the ground-truth dumps already claim (the “known answers”), plus any fresh mega-index surface.

- Engines: **Google, Bing, Yahoo**, (Baidu/Naver/Sogou optional quick pass).
- Queries: section A (canonical) + C (noise-filter) + E (filetype).
- Also: pull the known canonical IDs (IMDb `nm17333332`, Discogs artist, streaming artist pages) and confirm they're alive → tag ✅/🟡.
- **Success marker:** every item in the 133-record media master and the accomplishment register is *accounted for* (found or explicitly marked dead).

## Day 2 — Meta & privacy layers 🟢
**Goal:** de-personalized, high-recall confirmation + catching anything the majors ranked away.

- Engines: **DuckDuckGo, Startpage, Ecosia, Qwant, MetaGer**, plus 2–3 live **SearXNG** instances from **searx.space**.
- Queries: section A, B (handle variants), C.
- **Note:** a result unique to one SearXNG instance = still a 🔎 lead; open it.

## Day 3 — Independent, obscure & regional 🟣🔴
**Goal:** the long tail — indie net-labels, fan wikis, foreign press.

- Engines: **Mojeek, Stract, Marginalia, Wiby, Yep**, then **Yandex** (RU/CIS flip) and **regional-flipped Bing/DDG** (es, pt-BR, de, fr, pl, nl).
- Queries: A + C + F (context qualifiers) + H (Spanish/Portuguese).
- **Likely reward:** unknown compilation/label/lyric pages not in any prior dump.

## Day 4 — Music vertical 🟠
**Goal:** exhaust discography/credit/lyric presence platform-by-platform.

- Hit the **internal search box** of each platform in `03` §5: Spotify, Apple, Deezer, Bandcamp, Discogs, Last.fm, MusicBrainz, RYM, SoundCloud, YouTube, lyrics aggregators, analytics, and the regional mirrors.
- Queries: section D `site:` dorks (music block) + G (credit chasing) for each known release/compilation.
- **Success marker:** every compilation row in the Discogs index and every track credit is accounted for with its canonical URL.

## Day 5 — Film, recognition, academic, code, literature 🎬🟣🟠
**Goal:** cover the non-music side thoroughly.

- Film/search: IMDb, TheMovieDB, FilmFreeway, art platforms, festival pages (`03` §6).
- Recognition/academic: Google Scholar, AO3, AllPoetry, Vocal, GitHub, Hackaday (`03` §7).
- Queries: section D (film/art + social block), E (filetype), F.

## Day 6 — Social-native + mirrors + spam triage 🟤📼🖤
**Goal:** post-level mentions, then separate signal from noise.

- Social-native search (`03` §8): X, Reddit, Bluesky, Mastodon, YouTube comments/channel, Instagram/TikTok (as accessible).
- Mirror chase: run `"UX2kv3G89Jw"` and the "Phantom Requiem"/album title sweeps (`04` §G) → tag every aggregator/repeater as 📼.
- Spam triage: re-review every seed URL tagged 🖤 in `registry/seed/` and decide *keep-as-spam* vs *reclassify* vs *drop*.
- **Success marker:** a clean, separated signal list vs. a documented 📼/🖤 noise list.

## Day 7 — Verification pass + consolidation ✅🗂️
**Goal:** the “double-check they work later” + a single clean directory.

- Run the full **link-check & verification runbook** (`07`) over the entire combined set: seed (260) + newly found + the 133 master records. Tag every row ✅ / 🟡 / ❌.
- Reconcile against ground truth (accomplishment register + 133 master) — produce a **gap list** (items in ground truth the census couldn't re-locate).
- Consolidate into the final registry + write the **week report** (counts by media type, by status, notable new finds, open leads, and honest completeness caveats).

---

## Cadence rules that keep it clean

- **One engine family per day** prevents index-bias and double-counting the same page.
- **Log same-day** — evidence snippets lose fidelity if deferred.
- **Dedupe at the moment of logging** (mirror vs original = one primary row).
- **Never claim verified until it's opened and read** (`01` §5).
- If a day overruns, **finish breadth first** (all engines touched) before depth (all pages opened); leave depth to the verification day.

*Next: ready-made agent briefs in [`06_AGENT_PROMPT_TEMPLATES.md`](06_AGENT_PROMPT_TEMPLATES.md).*
