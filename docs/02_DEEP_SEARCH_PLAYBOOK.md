# 🧠 02 — DEEP-SEARCH PLAYBOOK

> The **methods** behind the sweep. Covers operator syntax per engine, meta-search strategy, obscure-engine technique, evidence capture, and backlink-chasing. Pair with [`03_ENGINE_DIRECTORY.md`](03_ENGINE_DIRECTORY.md) and [`04_QUERY_LIBRARY.md`](04_QUERY_LIBRARY.md).

---

## 1. The golden rule: never trust one index

Google does **not** equal “the internet.” Different engines run different crawlers and indexes:

- **Own-index engines** (Bing, Brave, Mojeek, Yandex, Baidu, Naver, Yep, Marginalia, Qwant-FR, Startpage-via-Google) each surface pages the others miss.
- **Meta engines** (SearXNG, MetaGer, Startpage, Ecosia, DuckDuckGo-bing) re-query several backends — great for recall, but results come from their backends.
- **Obscure / niche engines** reach pockets (small indie blogs, net-labels, fan wikis, foreign music sites) that mega-engines bury.

Run **every target name** through at least one engine in each class — otherwise the “directory” is incomplete by construction.

---

## 2. Always start from canonical queries

For each target, always run the **strict exact-name** form first, then the near/handle variants:

```
"Zazie Productions"
"Zazie Kanwar-Torge"
```

Then broaden per platform / region as shown in [`04_QUERY_LIBRARY.md`](04_QUERY_LIBRARY.md).

---

## 3. Operator cheat-sheet (which works where)

These travel well across Google, Bing, Brave, Mojeek, Startpage, DuckDuckGo:

| Operator | Use | Example |
|---|---|---|
| `" "` | Exact phrase (most important for name census) | `"Zazie Productions"` |
| `OR` or `\|` | Alternatives (uppercase; group with parens) | `("Zazie Productions" OR "Zazie Kanwar-Torge")` |
| `-` | Exclude a term | `Zazie -singer` / `"Zazie" -musique -chanson` |
| `site:` | Restrict to one domain | `site:last.fm "Zazie Productions"` |
| `-site:` | Exclude a domain | `"Zazie Productions" -site:youtube.com` |
| `intitle:` | Word in page title | `intitle:"Zazie Productions"` |
| `inurl:` | Word in URL | `inurl:zazie-productions` |
| `intext:` | Word in body | `intext:"Zazie Kanwar-Torge"` |
| `filetype:` / `ext:` | Limit to a file type | `"Zazie Productions" filetype:pdf` |
| `after:` / `before:` | Date window (Google/Bing) | `"Zazie Productions" after:2024-01-01` |

**Engine-specific notes (keep these straight):**

- **Bing** documents `OR`, `NOT`/`-`, `+`, parentheses, quotes; also `contains:`, `inanchor:`, `inbody:`, `feed:`/`hasfeed:`. Use uppercase `OR`/`NOT`.
- **DuckDuckGo** supports `""`, `-`, `site:`, `filetype:`, `intitle:`, `inurl:`, `-site:`. It does **not** honor `OR` reliably — run alternatives as separate queries.
- **Mojeek** supports `inanchor:`, `intext:`, `intitle:`, `inurl:` (and `allin*` variants). Great independent index to double-check against.
- **Startpage** = Google results through a privacy layer; Google operators mostly apply, results are de-personalized (useful for an “unbiased” SERP check).
- **Brave Search** supports quotes, `site:`, `intitle:`, `inurl:`, `-`. Supports its own **Goggles** re-ranking.
- **Yandex** uses `""` for exact (no extra words between), `-` to exclude, `!` to fix word form, `+` to force stop-words, `|` for OR, `site:`, `host:`, `url:`, `domain:`, `title:`, `lang:`. **Quotes in Yandex are stricter** (verbatim word count), so prefer `title:` + quotes for name lookups. Note: Yandex may require a RU-context or region flag for best results on the exact name.
- **Baidu / Naver** mostly for CJK-adjacent coverage; the exact Latin names are unlikely to surface but run once for completeness. Baidu supports `site:`, quotes loosely.
- **Perplexity / ChatGPT Search / You.com / Google AI Overviews** — *ask them directly*: they often pull obscure niche pages and cite sources with URLs, effectively “searching” indexes you wouldn't hit manually. Treat their citations as leads to then verify directly.

---

## 4. The noise problem: filter out “Zazie the singer” early

The French artist **Zazie** dominates results for the short string. Mitigations:

1. Always use **exact two-word phrases** first (`"Zazie Productions"` / `"Zazie Kanwar-Torge"`) — this alone kills 95% of the noise because those are two-word distinctive strings.
2. When you must search `"Zazie"` + qualifier, append negatives:
   `"Zazie" -"Zazie" -musique -chanson -"Tout sera" -Paris -Enchantée`
3. Use `intitle:`/`inurl:` with the full distinctive phrase so the short name never matches alone.
4. Add qualifiers that belong to this project when recall is too narrow: `composer`, `soundtrack`, `horror`, `experimental`, `netlabel`, `phantom requiem`, `the vanishing point syndicate`, `stop-motion`.

See the exclusion templates in [`04_QUERY_LIBRARY.md`](04_QUERY_LIBRARY.md).

---

## 5. Meta-search strategy (max recall in fewer clicks)

A meta layer queries many backends behind one query string.

- **SearXNG** — open-source meta. Pick **several different public instances** (a current list lives at **searx.space**; instances churn, so verify each is alive). Enable many categories (general + the installed engines) so a single query fans out. Repeat the same query on 2–3 distinct instances because each instance's enabled engine set differs.
- **Startpage / Ecosia / DuckDuckGo / MetaGer / Qwant** — each is effectively a meta pass over Google/Bing/own; use them to get *de-personalized* or *second-source* confirmation that a page truly ranks.
- **Rule:** a result surfaced only by *one* meta instance is still just a **lead** until the underlying page is opened and verified.

---

## 6. Obscure-engine & “long tail” technique

These catch the genuinely buried places:

- **Independent indexes** (Mojeek, Stract, Marginalia, Wiby) favor the small/non-commercial web where net-labels and indie blogs live. Run the canonical phrases there — this is where unknown compilation pages often hide.
- **Marginalia / Wiby** — heavily favor old-school/indie pages; worth a dedicated pass for obscure net-label and blog mentions.
- **Region-flip engines** — query Yandex (RU/CIS), Bing with `cc=xx`, DuckDuckGo with region settings, Ecosia/Qwant (EU). Many European & LatAm music sites only surface under a regional SERP. Change the search UI **language + region**, not just the query.
- **Vertical/niche databases** (see `03_ENGINE_DIRECTORY.md` §9) — these aren't “web search” but are where discography/film/lyric/credit rows live. Search each one's **internal** search box directly.
- **Localized lyric/stream mirrors** surfaced in the dump (Douyin, NetEase `music.163.com`, fangpi, gequbao, ligaudio, zvu4no, Angahmi, Qobuz DE, KKBOX) — search *their* internal search, not the open web.

---

## 7. Backlink- & mirror-chasing (how one find becomes ten)

A single YouTube ID (`UX2kv3G89Jw` for *Phantom Requiem*) was found mirrored on 50+ aggregator/repeater sites in the dump. Method to replicate:

1. Take a known **canonical asset URL** (a YouTube video, a bandcamp track, a press page).
2. Extract the **stable ID** (video ID, bandcamp slug, Discogs release id, IMDb name id).
3. Search each engine for `"<id>"`, and search the canonical page title in quotes.
4. Log every mirror/embedder/aggregator as a **📼 mirror** row (secondary), not primary coverage.

Also chase **true backlinks**: for editorial/streaming pages, ask the engine for `intext:"Zazie Productions"` and for who links to the canonical URL. Cached views (Google cache, `web.archive.org`, `r.jina.ai/http://…`) can expose text on JS-gated or dead pages.

---

## 8. Evidence capture (do this on every hit)

For each confirmed place, record (see `registry/README.md` for the template):

- **URL** (as found) + optional clean canonical URL
- **Media-type** emoji and **priority** (A/B/C)
- **Evidence level** (✅ direct / 🟡 index / ⬜ lead)
- **Snippet** — copy 1–2 lines showing the exact name
- **Engine/index found on** and **date**
- **Name form** present (`Zazie Productions`, `Zazie Kanwar-Torge`, or both)
- Optional **context** (track/title/project it refers to)

---

## 9. Freshness

- Web pages and indexes change **every day**. Record a **“searched on” date** for every row.
- For the verification pass, re-probe links (runbook: [`07_LINK_CHECK_AND_VERIFICATION.md`](07_LINK_CHECK_AND_VERIFICATION.md)).
- Note in the final report the **census window** (dates searched) so the directory is honest about its freshness.

---

## 10. Chain of custody for future agents

Always start a session by reading, in order:

1. `01_MISSION_SCOPE_AND_RULES.md` — what counts
2. `02_DEEP_SEARCH_PLAYBOOK.md` — how to search (this file)
3. `03_ENGINE_DIRECTORY.md` — what to search
4. `04_QUERY_LIBRARY.md` — exact queries to paste
5. `05_WEEK_PLAN_AND_CADENCE.md` — what to do today

Then record findings, then verify. Don't skip the mission brief — it prevents counting the wrong “Zazie.”
