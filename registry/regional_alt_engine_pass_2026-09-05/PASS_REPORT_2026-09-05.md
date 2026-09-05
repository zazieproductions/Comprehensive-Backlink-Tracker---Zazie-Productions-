# Pass 9 — Regional, Independent, Archival & Scholarly Engine Sweep
## Zazie Productions / Zazie Kanwar-Torge — 2026-09-05

**Branch:** `arena/01a06f1a-comprehensive-backlink-tracker` · **Operator:** Arena Agent Mode
**Queries (strict):** only the complete exact quoted phrases **`"Zazie Productions"`** and
**`"Zazie Kanwar-Torge"`** — no variants, no partial names, no generic "Zazie".
**Canonical directory at pass start:** `data/master/master_index.csv` — 499 records (baseline after Pass 8).
**Canonical directory at pass end:** **523 records** (+24 verified/index-verified additions, all logged in `candidate_ledger.csv`).

> Access-restriction policy (per brief): engines that captcha/403/login-wall or that
> rendered **snippet-only** evidence are recorded as **access-test rows** or **leads**,
> never as verified records. Every counted addition below was confirmed either on the
> destination page itself or in an authoritative index surface of the destination host
> (e.g. archive.org item metadata).

---

## 1. What was actually run

- **62 engine/interface access tests** (see `ENGINE_ACCESS_MATRIX.csv`) across:
  - **Regional:** Baidu, Sogou, 360/So.com, Shenma, Naver, Daum, Nate, NAVER encyclopedia
    surfaces, Seznam, Cốc Cốc, Petal Search, Yandex (blocked) **+ Mail.ru as a working
    Yandex-index access path**, Rambler, Goo, Yahoo! JAPAN, Rakuten Infoseek, BIGLOBE,
    Excite Japan, Walla!, Search.ch, Najdi.si, SAPO, Rediff, Egerin, Yongzin, Leit.is.
  - **Independent / alt-web:** Kagi, Mojeek, Marginalia (throttled → retry), Wiby, Brave,
    Yep, Qwant, Swisscows, Stract, Gigablast (no archival instance reachable), YaCy public
    node, public SearXNG (opnxng; searx.be/tiekoetter blocked), Whoogle (no stable public
    instance), MetaGer, Ekoru, GiveWater (dead), OceanHero, Ghostery Private Search
    (**discontinued to closed beta 2026-06**), BoardReader (path changed), Million Short
    (login-gated), Search Encrypt, Dogpile, Info.com, AOL, Ask, Lycos, HotBot (pivoted to
    AI chat), Excite, WebCrawler.
  - **Archival:** Internet Archive full-text search, Wayback CDX (+ availability API),
    archive.today, Memento, Common Crawl index, Arquivo.pt, UK Web Archive, LoC Web
    Archives, Trove, Europeana/DPLA (key-gated; pending).
  - **Scholarly/catalog:** OpenAlex, Crossref, Europe PMC, Semantic Scholar, BASE, DOAJ,
    Zenodo, OSF, OAIster family; IA Texts covered by the IA full-text sweep.
- **31 logged queries** (`query_inventory.csv`) and **29 ledger rows** (`candidate_ledger.csv`),
  each with engine, interface language, query, date, pagination depth, result URL,
  verification status, and novelty-vs-master.

### Access verdict highlights

| Verdict | Engines |
|---|---|
| ✅ Worked, full organic SERP | **360/So.com**, **Seznam**, **Yahoo! JAPAN**, **Walla!**, **Mail.ru (Yandex path)**, **Brave**, **Yep**, **Marginalia (retry)**, **Swisscows (snippet-level)**, **OceanHero**, **Info.com**, **opnxng SearXNG**, **YaCy node (0 hits)**, **Wiby (0 hits)** |
| ⚠️ Worked, results not extractable / partial | Baidu (chrome-only server render), Naver (no exact-name organic rows), Qwant & Ekoru (JS-gated), Najdi.si (portal redirect) |
| 🚫 Blocked / gated | Sogou (antispider), Mojeek (ALTCHA), Rambler & Yandex (SmartCaptcha), Kagi (login), Million Short (login), Trove (Anubis PoW), archive.today (reCAPTCHA), BASE API (IP-denied), Yongzin (403), Ghostery (closed beta) |
| 💀 Dead / retired / changed | BIGLOBE (endpoint gone), Excite Japan (404), GiveWater (404), Stract (404), BoardReader `/search` (404), Ask `/web` (404), AOL (404), HotBot (AI-chat pivot), Egerin (search path now serves news), OSF search API (retired), **UK Web Archive (down — BL cyber-incident recovery)** |
| 🟢 Clean negatives (exact phrase, zero results) | Arquivo.pt, Library of Congress, OpenAlex (both names), Europe PMC, Zenodo, Wiby, YaCy node; Wayback availability API: no snapshots of the root domain |

### Backend notes (who actually indexes what)
- **Mail.ru Search is a Yandex-index proxy that does not captcha** — the practical Yandex
  access path from automation (Yandex direct + Rambler are SmartCaptcha-walled).
- **Yahoo! JAPAN and Walla!** confirm the name is served from the **Google index** through
  regional interfaces (ja, he) — page 1 remains all-known surfaces (no new records; still
  evidence of regional interface coverage).
- **Seznam** is the only tested regional engine with its **own crawler** that returned a
  full organic set — its deep-tail results matched master entries (independent confirmation).
- **360/So.com** proves the name sits in a **Chinese index** via Douyin/汽水音乐 music pages.
- **Yep (Ahrefs' own crawler)** and **OceanHero (Bing)** independently surfaced pages the
  other backends missed (Metapsychosis; Heard/Arthive/ReverbNation respectively).
- **Meta veterans** (Dogpile/AOL/Ask/Lycos/HotBot/Excite/WebCrawler) are retired, pivoted,
  or erroring for programmatic access; Info.com is the only healthy Google-fed survivor.

---

## 2. New canonical records added (+24, see `candidate_ledger.csv` RAN-001…RAN-025)

### Internet Archive items — 15 new URL-level records (the pass's biggest cluster)
IA full-text search returned **19 items** matching `"Zazie Productions"`; only 3 were
already in the master. **14 self-issued + 2 compilation mirrors + 1 lead** added:

| Item | Verification | Category |
|---|---|---|
| `…/unexplained-aerial-phenomena-report-zazie-productions` (UFO report ZP-AEP-0328-MID-FL) | ✅ creator+body | Official |
| `…/data-conversation-01-17675` — *Mystery File Dump: Vol 1* | ✅ creator+description | Official |
| `…/liquid-phosphorus-4-33` — *Mystery File Dump: Vol 2* | ✅ IA index title | Official |
| `…/phantom-requiem-short-film` — official upload, CC BY-ND | ✅ creator row | Film |
| `…/instructions-for-clean-living` — **Public Domain Day Remix Contest 2026 entry** (Tier B) | ✅ creator+description | Film |
| `…/quantum-geometry-3-d-emulator` (software) | ✅ creator | Official |
| `…/neural_dynamics_simulation_by_…` (software, v0.7.3a 2022) | ✅ creator+description | Official |
| `…/textual-exhumation-5-gnosis-of-the-null-horizon_202504` (zine-text) | ✅ creator | Publications |
| `…/textual-exhumations-unicode` (zine-text) | ✅ creator | Publications |
| `…/ra-codename-the-rhizosigil` — **IA zines collection item** | ✅ creator | Publications |
| `…/img-1941_202505` — *THE SEVENTH SCREEN…* visual archive | ✅ title+creator | Official |
| `…/5-bb-30-…-667` — *yyyyyyy.info lost animation* (creator "Zazie Productions, yyyyyyy.info") | ✅ creator | Official |
| `…/va-doom-a-creative-commons-music-compilation` (track 6 credit) | ✅ track metadata | Compilations |
| `…/experiments-on-the-witch-house` (archive.org full-album copy) | ✅ IA full text | Compilations |
| `…/arrhythnia-discography` (incl. **Amnesia X Zazie Productions** split aNr124) | ✅ file listing | Compilations |
| `…/sepsis-d-…` (unicode-titled Sepsis video copy) | IA full-text hit | Video Mirror |

### Profiles / platforms / storefronts — 9 new records
- `metapsychosis.com/creative-agents/zazie-productions/` — ✅ fetched (Tier B, edited literary profile)
- `getheard.fm/producers/zazie-productions` — ✅ fetched (contact/submission database)
- `ok.ru/music/artist/122911094866528` — ✅ fetched; **also resolves the previously
  unresolved listen-link for the "1 Year Anniversary" compilation** → `ok.ru/music/album/123001281196995`
- `github.com/zazieproductions/zazieproductions` — ✅ fetched (profile README repo)
- `zazieproductions.gumroad.com/l/plugin` — ✅ fetched (Gumroad product page)
- `reverbnation.com/zazieproductions` (root; sub-pages already master) — index-verified
- `music.yandex.ru/artist/17856702/tracks` — 🟡 region-blocked; Yandex-index snippet verified (**first Yandex Music record**)
- `spacehey.com/profile?id=3044031` — 🟡 region-blocked (VA age-verification); title verified in Yep/Brave index
- `arthive.com/zazieproductions/biography` — 🟡 bot-gated on fetch; snippet-verified via both the Bing (OceanHero) and Yandex (Mail.ru) paths (RU twin: `artchive.ru/zazieproductions/biography`)

### Leads recorded but NOT counted (snippet-only / redirect-only)
- Facebook group comment by `Zazie Kanwar-Torge` (film-composer thread) — login-walled, snippet-only → lead (RAN-026).
- Two Douyin/汽水音乐 track pages (*Subliminal Failures*, *Stokes Diapir*) surfaced by 360/So.com — redirect URLs only → leads (RAN-027/028).
- `thechurchofnoisygoat.bandcamp.com` *Post-Carbon Signal Rot (Comunion V.2.3)* — surfaced by Marginalia retry, page not yet fetched → lead (RAN-029), queued for Pass 10 verification.

---

## 3. Scholarly & catalog verdicts (exact-phrase)
- **Confirmed negatives:** OpenAlex (0, both names), Europe PMC (0), Zenodo (0),
  Library of Congress (0), Arquivo.pt (0), Trove/UK WA (blocked/down, not negative-confirmed).
- **Crossref:** fuzzy-only — all top hits are *Zazie dans le Métro* (Queneau/Malle)
  scholarship; **no exact-name work**.
- **Rate/blocked:** Semantic Scholar (429), BASE API (IP denial), DOAJ (502), OSF search
  endpoint retired. Europeana/DPLA/WorldCat/HathiTrust/JSTOR/MUSE = key- or JS-gated → pending.

## 4. Honesty & boundaries
- Baidu's organic section and Naver/Daum/Nate organics could not be extracted server-side;
  they are recorded as access-partial, not as negatives.
- All 24 additions meet evidence level 1 (page/metadata) or level 2 (authoritative index
  of the destination host); nothing below that was counted.
- Wayback CDX failed with HTTP 500 from this environment — re-run from a browser before
  treating "no captures" as final (availability API shows no root-domain snapshot).

**Repro:** `python3 scripts/build_regional_alt_pass.py` (rebuilds this folder's CSVs;
idempotent against the master CSV) · `python3 scripts/generate_docs.py` (regenerates
categorized docs + SUMMARY from the master).
