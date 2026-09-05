# Week-Long Project Plan — Zazie Index Directory

Goal: an **extensive, reproducible directory of every place `Zazie Productions` /
`Zazie Kanwar-Torge` is indexed or named**, including obscure engines and meta-search
aggregators. This is a research scaffold + live status. Tick items as you go.

---

## ✅ Done (session 1)
- [x] Extracted all URLs from the two source PDFs using their embedded clickable links
      (avoiding PDF line-wrap). Media Master = 133 URL-level records; link dump = 278 unique.
- [x] Built the canonical master index: `data/master/master_index.csv` (**412 records**).
- [x] Classified into 12 categories with trust tiers (A/B/C/D) and a `source` field.
- [x] Generated per-category Markdown + `SUMMARY.md` via `scripts/generate_docs.py`.
- [x] Ran the first multi-engine pass (Google, Bing, Yahoo, DuckDuckGo, Startpage, Yandex,
      SeekXNG/searx.be, Mojeek, Brave, Marginalia) and logged results.
- [x] Added 27 new surfaces found by opening the search engines (Instagram profile,
      SoundClick pro, the full Bandcamp discography, Marginalia-track pages, FilmFreeway sub-pages).
- [x] **Second search pass** added 13 more obscure-engine wins (CJSW radio, Breezewiki/Analog-Horror,
      CincyMusic, Tinnitist, Broken Zen, Tumblr, Argali/Camembert netlabel pages).
      Master is now **425 records**.
- [x] **Listen-link hunt (SearXNG pass 3):** found a listen link for each of the 60
      Discogs compilations (30 confirmed Bandcamp URLs, 28 label sites, 2 unresolved).
      Wrote `data/master/listen_links.csv` + `data/master/LISTEN_LINKS.md`. Used
      opnxng.com & baresearch.org SearXNG instances.
- [x] Wrote `docs/METHODOLOGY.md` and this `docs/PLAN.md`.
- [x] **Register/Media-Master link hunt (Pass 5):** extracted the 2026 Accomplishment
      Register (203 records, **zero URLs**) and mapped every feature to a public link via
      `data/master/REGISTER_LINK_MAP.md` (linked / HUNT / AUTH / lead). Resolved the GitHub
      org projects (void-oculus, Contrapuntal, Spectra, harsh-noise-generator) and the
      Vanishing Point Syndicate netlabel. Master is now **440 records**.
- [x] **Deep multi-engine sweep (Pass 6):** probed many additional SearXNG instances and
      backends (Brave via sx.catgirl.cloud, Yahoo via search.pi.vps.pw, Yandex/Seznam via
      search.lumy.live, Google-CSE via opnxng/pereirag). Added 16 verified exact-name
      surfaces (Canyon Cinema, Red Ogre Dec-2025, Z-Dimension SHARDS, TicketTailor/Swinewomb,
      Stage32 video, SoundShiva, 2 more Shazam song pages, MusicBrainz artist entity,
      Hackaday R&D project). Master is now **450 records**.

## 🔲 Verification (suggested days 1–3)
- [ ] Open each record (or spot-check a sample) and confirm the exact name appears.
- [ ] Mark `status` as `verified` / `404` / `dead` in `master_index.csv`.
- [x] Tier-D sample opened & dispositions recorded (Pass 10, 2026-09-05: 9 surfaces read live (2 string-partial), 9 dead/errored, 2 bot-blocked, 4 Wayback CDX availability probes; doorway hosts left unvisited per safety policy; full results in `registry/spam_scraper_syndication_lowtrust_2026-09-05/source_access_log.csv`).
- [ ] Re-check the 133 Media Master URLs still resolve and match the Media Master PDF.

## 🔲 Engine & metadata searches (days 2–4)
- [ ] Trial **more public SearXNG instances**; note which allow HTML and which block.
      Self-host a SearXNG instance and query its JSON API for a clean path.
- [ ] Re-run `"Zazie Kanwar-Torge"` through Yahoo, Brave, Marginalia (the accepted engines).
- [ ] Query Marginalia per *release* and per *compilation* to surface more netlabel /
      bandcamp track pages that Big-Tech engines miss.
- [ ] Query YouTube video mirrors and the `Phantom Requiem` video for additional backlink
      surfaces (the existing 57-item backlink table in the link dump is a starting point).
- [ ] Document **Yandex** presence via the Yahoo/Bing index fallback (Yandex blocks bots).

## 🔲 Expansion (days 4–6)
- [ ] Enumerate the remaining Bandcamp/Label track pages associated with the 85 compilations.
- [ ] Add per-release and per-track pages across platforms (Spotify album/playlist, Qobuz,
      Deezer, Amazon Music, Apple Music, KKBox, TIDAL, Boomplay, iHeart, SoundClick, etc.).
- [ ] Add the festival/award pages implied by FilmFreeway (Re:Fract, Taha Island, Tromsø
      Arctic, Helsinki Quiet Frames, Ljubljana Indie, Riviera Art, Skyline Fringe, Kvikmynda,
      Cascadia Digital, etc.).
- [ ] Add PR/press syndications and secondary coverage pages.
- [ ] Add social handles and meme-persona surfaces (@WellMeaningNeurotypicals, etc.) —
      note they are separate from the two exact names.

## 🔲 Finalize (day 7)
- [ ] Rebuild docs: `python3 scripts/generate_docs.py`.
- [ ] Update `data/research/search_engine_audit.md` with the second pass.
- [ ] Write the top-level `README.md` summary + a press-kit-priority ordering.
- [ ] Commit and (if wanted) open a PR from `arena/01a06e73-comprehensive-backlink-tracker`.

---

## How to run the regeneration
```bash
python3 scripts/generate_docs.py
```
Regenerates `data/master/categorized/*.md` and `data/master/SUMMARY.md` from
`data/master/master_index.csv`.

## Where things live
```
README.md                     project overview
docs/METHODOLOGY.md           inclusion rules, trust tiers, reproducibility
docs/PLAN.md                  this week-long roadmap
data/master/master_index.csv  the canonical index (edit/add here)
data/master/SUMMARY.md        auto-generated summary
data/master/categorized/*.md  auto-generated per-category references
data/research/search_engine_audit.md  engine-by-engine findings
scripts/generate_docs.py      regenerates the markdown from the CSV
```
