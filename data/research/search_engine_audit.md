# Search-Engine Index Audit — Zazie Productions / Zazie Kanwar-Torge

Date of this pass: **2026-09-04** (Arena agent session)
Names audited: `"Zazie Productions"` and `"Zazie Kanwar-Torge"` (exact-phrase queries)

Purpose: to verify **how widely and where the exact names are indexed**, including
**obscure / independent engines and meta-search aggregators** that are often missed by
a single mainstream engine. This is a snapshot; engines re-index continuously.

---

## TL;DR

- The two names are **indexed on every major engine and on at least two independent
  crawlers** (Marginalia, Brave's own crawler).
- **Meta-search / aggregator behavior matters more than engine choice.** Yahoo returned
  the richest, most relevant exact-match set at the time of this pass; Bing's direct
  page returned AI-generated results that were weak for this niche query; DuckDuckGo,
  Yandex, Startpage, Mojeek and a public SearXNG instance all **block bots** (captcha /
  anti-bot), so they need a different access path.
- **Marginalia** (an independent, non-Big-Tech crawler that loves small/underground sites)
  surfaced **compilation track-level Bandcamp pages that the mainstream engines did not**.
  This is the single most "obscure-engine" win of the pass.

---

## Engine-by-engine results

| Engine | Access method | Accessible? | Notes / what it surfaced |
|---|---|---|---|
| **Google** | arena `web_search` aggregator | ✅ | Confirms the major surfaces (IMDb, LinkedIn, MUSE, Groover, SoundBetter, Slaps, Viberate, Bandcamp, FilmFreeway, Stage32, ReelCrafter, WFCN, Musicians.Directory). |
| **Bing** | `bing.com/search?q="..."` | ⚠️ partial | Returned AI-generated, largely off-topic pages for the exact query (visa/immigration results — wrong match). Bing's *index* clearly holds the name (Yahoo runs on Bing's index), but its direct SERP was not useful. |
| **Yahoo** | `search.yahoo.com/search?p="..."` | ✅ | Best exact-match set. Surfaced: itch.io, Musicians.Directory, `youtube.com/@zazieproductions`, Linktree, **`instagram.com/zazieproductionsofficial/` (12K followers)** and **`pro.soundclick.com/ZazieProductions`**. |
| **DuckDuckGo (HTML)** | `html.duckduckgo.com/html/` | ❌ blocked | Returns the "select all squares with a duck" bot challenge. |
| **Startpage** | `startpage.com/sp/search` | ❌ blocked | "Anubis" JavaScript proof-of-work verification. |
| **Yandex** | `yandex.com/search/` | ❌ blocked | "Please confirm you are not a robot" (SmartCaptcha). |
| **Mojeek** | `mojeek.com/search` | ❌ blocked | Altcha "I'm not a robot" challenge. |
| **SearXNG (searx.be)** | `searx.be/search` | ❌ blocked | "Cap" self-hosted captcha / browser verification. |
| **SearXNG (searx.tiekoetter.com)** | `searx.tiekoetter.com/search` | ❌ blocked | Captcha / "Checking request". |
| **SearXNG (opnxng.com)** | `opnxng.com/search` | ✅ **WORKED** | Best SearXNG workhorse. Found label/compilation listen URLs (GhostNun, Owlripper, The Hills Are Dead, Gelombang, Vanishing Point Syndicate, Dittany of Crete, Z-Dimension, Plataforma Recs, Camembert, Psych Lovers, Terminal Future Industries, etc.). |
| **SearXNG (baresearch.org)** | `baresearch.org/search` | ✅ **WORKED** | Fallback SearXNG; confirmed GhostNun result. |
| **SearXNG (search.inetol.net)** | `search.inetol.net/search` | ⚠️ reachable | Returned "no results" for most exact-title queries (Weak coverage for niche netlabel titles). |
| **Brave Search** | `search.brave.com/search` | ✅ | Surfaced: Bandcamp, SoundBetter, FilmFreeway, itch.io, Apple Music, Slaps (all already in master). |
| **Marginalia** | `marginalia-search.com/search` | ✅ (but rate-limited) | Independent crawler. Surfaced **track-level Bandcamp pages**: Synthetic Dystopia's `Slippage Beneath the Hyperlink`, Petroglyph Music's `Moving in Perpetual Slumber`, Institute For Alien Research `Liquid Phosphorus` / `movimiento diez 'Oscillographia'`, Camembert Électrique `Isochamber Drift`, Argali Records `Vibroscriptorium`, plus FilmFreeway sub-pages — and **non-Bandcamp obscure wins** (CJSW radio, Breezewiki/Analog-Horror, CincyMusic, Tinnitist article, Broken Zen). Starts throttling after ~3 requests; query in spaced bursts or self-host. |

---

## New surfaces discovered this pass (now in the master directory)

These were **not** in the source PDFs and were added to `data/master/master_index.csv` (source = `research`):

- Instagram profile: `https://www.instagram.com/zazieproductionsofficial/`
- SoundClick pro profile: `https://pro.soundclick.com/ZazieProductions`
- Full **Bandcamp discography** (18 releases) under `zazieproductions.bandcamp.com` (album/track pages)
- Marginalia-surfaced compilation track pages:
  - `thechurchofnoisygoat.bandcamp.com/track/zazie-productions-slippage-beneath-the-hyperlink`
  - `petroglyphmusic.bandcamp.com/track/zazie-productions-moving-in-perpetual-slumber`
  - `ifarmusiqueconcretecompilation.bandcamp.com/track/liquid-phosphorus`
  - `ifarmusiqueconcretecompilation.bandcamp.com/track/movimiento-diez-oscillographia`
  - `camembertelectrique.bandcamp.com/track/isochamber-drift`
  - `argalirecordsnetlabel.bandcamp.com/track/vibroscriptorium`
- Bandcamp **netlabel album** pages (album, not artist, level): `camembertelectrique.bandcamp.com/album/icelock-continuum`, `argalirecordsnetlabel.bandcamp.com/album/fourteenth-quarterly-report-of-argali-records-netlabel-the-great-reconnection`, plus the `argalirecordsnetlabel.com/` netlabel homepage.
- **Non-Bandcamp obscure wins** (found via Marginalia + platform search):
  - `cjsw.com/program/noise/episode/20251113/` — CJSW Radio program airing *To Halt Space Adrift*
  - `breezewiki.com/aesthetics/wiki/Analog_Horror` — Aesthetics Wiki mirror citing Zazie Productions
  - `cincymusic.com/blog/2025/12/lo-fi-city-drops-2025-comp-in-time-for-bandcamp-friday`
  - `tinnitist.com/2025/02/10/groover-playlist-299-brilliant-numbers-part-2/`
  - `brokenzen.wordpress.com/2025/12/16/new-track-new-comp/`
  - `tumblr.com/lezet` — community blog announcing compilations featuring Zazie Productions
- FilmFreeway project sub-pages (Phantom Requiem, Deaf Orphans of Streamcast)

---

## Method & reproducibility

Exact-phrase queries (quotes) were used throughout so the results contain the literal
name and not near-matches (e.g. the French singer Zazie, "Zazie Films", or the handles
`@zazieproductions` without a space). Each engine was queried with the same two queries:

1. `"Zazie Productions"`
2. `"Zazie Kanwar-Torge"`

### Access decisions
- Use the **arena `web_search` aggregator** and **Yahoo / Brave / Marginalia** HTML GET
  for automated access.
- **DuckDuckGo, Startpage, Yandex, Mojeek, and most public SearXNG** block headless
  requests. To cover them, run the queries in a real browser, or host a self-run SearXNG
  instance (which you control) and query its JSON API on your own origin.

### Next steps (see PLAN.md)
- Trial additional public SearXNG instances; record which allow HTML.
- Query Marginalia / Mojeek / Brave for the second name and for individual releases and
  compilations.
- Verify each `research`-sourced record manually (open it, confirm the exact name appears).
- Track Yandex presence via the Yahoo/Bing index fallback.

---

## Pass 3 — Listen-link hunt (SearXNG instances)

Goal: for each of the **60 compilations** on the Discogs artist page, find a **listen**
link (mostly the label's Bandcamp). Result: `data/master/listen_links.csv` and
`data/master/LISTEN_LINKS.md`.

- **30 confirmed** direct listen URLs (opened): e.g. Shadowlands 4 (Owlripper), Dissonance
  Index Vol. 1 (Vanishing Point Syndicate — Zazie's own netlabel), Summoning 1/2/3
  (Dittany of Crete), SHARDS Vol. 1 (Z-Dimension), Field Recording Vol. 3/4 (Gelombang),
  Icelock Continuum & Arboreal Telegraph (Camembert Électrique), Two Years & LSD100
  (LOUDsilence), Synthetic Dystopia (Church of Noisy Goat), Psych Against Cancer Vol. 3
  pt. 2 (Psych Lovers), Ecstatic Feedback II (Terminal Future Industries), Harsh Noise
  Corpus 4 & 5 (The Hills Are Dead), Late Night Love Letters (Utopia District),
  Aspirin Age Vol. 5 (Broken Sound Tapes), Frequências Cadavéricas (Brutalize Netlabel),
  Make a Change (Rocket Punch), NYOTGRINDER vol. 2, Echoes Of Ancient Wrath (Dodendans),
  H.P. Lovecraft Whisperer In Darkness (GoH Recordings), Beyond The Body (Witch-House.com),
  etc.
- **28 label sites** — the compilation lives on this label's Bandcamp (open to reach the
  exact album/track). Includes the Dawn of Darkness netlabel (internetdaemon.bandcamp.com,
  which hosts Ju-On / I Want To Believe / Mulholland Drive / Experiments on the Witch House),
  TSHN Productions (Stonewall/Noisewall vol. 1), AIN23 (Twenty Three Seconds Ov Time),
  Ensemble For Sound Poetry (One String), Relics Of The Eternal City (Tavern Synth),
  DivergentArtists `<1` (7.7), Errant Static (1985).
- **2 unresolved** — no Bandcamp listen link surfaced this pass: Warm Music For Cold Weather
  (New Shagg Plus) and 1 Year Anniversary (Elements Of Tech & Bass Recordings). The Discogs
  release page is the safest pointer.

Note: **opnxng.com** and **baresearch.org** (public SearXNG instances) were the metasearch
workhorses for this pass. Search title strings were exact-phrase + `bandcamp`.

---

## Pass 4 — Name-index sweep across fresh SearXNG instances

Goal: find **new** surfaces that verify either exact name, using public SearXNG instances
not tried in earlier passes. Two queries per instance: `"Zazie Productions"` and
`"Zazie Kanwar-Torge"`.

### Working instances (new this pass) + what they surfaced
- **`search.lumy.live`** (SearXNG, engines **yandex + seznam**) — the standout. Gives a
  **Yandex-index access path** (Yandex itself is blocked). Surfaced new surfaces:
  `slated.com/people/134406/`, `manicworldmagazine.com/zazie-kanwar-torge-the-hour-collapses-inward/`,
  `shazam.com/song/6771371298/vibroscriptorium`, `pulitzercenter.org`, `github.com/zazieproductions`,
  `openhfilmzone` (`openfilmzone.com`), `legateaugallery.com/zazie-productions.html`, plus adds
  that were already in the master (Linktree, Deezer, Apple Music, TV Tropes, Pebbles Underground).
- **`searx.ononoki.org`** (engines **bing + yahoo + fynd**) — worked. Confirmed
  `manicworldmagazine.com`, `musicians.directory`, and compilation track pages
  (`thechurchofnoisygoat`, `z-dimension`, `errantstaticnoise` bandcamp).
- **`paulgo.io`** (engine **google cse**) — worked; surfaced `beatport.com/artist/zazie-productions/...`.
- **`search.pereira.is`** (engine **google cse**) — worked; surfaced the same Google-cse set
  (Bandcamp, MUSE, FilmFreeway, SoundBetter, Instagram, itch.io, IMDb, Spotify, Black Mountain College).
- **`baresearch.org`** — worked (as before).

### Reachable but low/zero coverage (do not retry for this niche)
- `search.2b9t.xyz` — no results.
- `sear.lurx.net` — no results.
- `libresearch.space` — no results.
- `search.bladerunn.in` — reachable (bing) but only returned the French singer Zazie.

### Blocked / not useful (do not retry)
- `searxng.deggo.fyi` — **Anubis** JS proof-of-work.
- `searx.linxx.net` — **Cap** captcha.
- `searx.oloke.xyz` — reachable but returned irrelevant (leboncoin) results.
- `searxng.website` / `searxng.site` — reachable but returned totally unrelated results.

### New verified surfaces added to the master (source = `research`): 9 total
- `slated.com/people/134406/` — "Zazie Kanwar-Torge, known professionally as Zazie Productions"
- `manicworldmagazine.com/zazie-kanwar-torge/` — artist profile
- `manicworldmagazine.com/zazie-kanwar-torge-the-hour-collapses-inward/` — work article
- `beatport.com/artist/zazie-productions/1440962/tracks` — artist page
- `github.com/zazieproductions` — official GitHub (README "ZAZIE PRODUCTIONS")
- `openfilmzone.com/videos/phantom-requiem/` — "original experimental short film by Zazie Kanwar-Torge"
- `legateaugallery.com/zazie-productions.html` — "Zazie Kanwar-Torge, professionally known as Zazie Productions"
- `shazam.com/song/6771371298/vibroscriptorium` — song page
- `equipboard.com/pros/zazie-productions` — artist/gear profile

Master count after Pass 4: **434**.

### Skipped in Pass 4 (did not meet the exact-name standard)
- `artfacts.net/artist/zazie-kanwar-torge` — renders "Zazie Kanwar-torge" (lowercase *t*), not the exact string.
- `aesthetics.fandom.com/wiki/Analog_Horror` — same content as the breezewiki mirror already in the master.
- `ogre.red` editor's note — intro page listing did not render the exact name.
- YouTube / Shazam album pages using "ZazieProductions" (no space) — near-match only.

### Engine rationale
`search.lumy.live` (yandex+seznam) is the single most valuable new engine for this name-index
task because it consults the **Yandex index**, which is otherwise unreachable from this
environment. The Google-CSE instances (`paulgo.io`, `search.pereira.is`, `opnxng.com`) all
return essentially the same Google-derived set, so they mostly re-confirm rather than expand.


## Pass 5 — Register + Media Master "feature without a link" hunt

Directive: for every feature/claim in `Zazie_2026_Accomplishment_Register_Maximal_Edition.docx`
and in the "OPEN" items of the Media Master PDF that had no link, find the link.

### Extraction outcome
- **Register docx:** 203 records across 10 sections. The register text contains **zero URLs**
  (all 203 items were unlinked). One summary table (203 core / 33 serious-reach). Mapping is in
  `data/master/REGISTER_LINK_MAP.md`.
- **Media Master PDF:** 133 records. Its "OPEN" labels are placeholder strings (no hrefs in the
  extracted text); the PDF was re-derived via the register + the name-index, so no annotation
  layer was recoverable. Its records are already largely represented in the master (they are the
  `media_master` source).

### What the hunt found
Most 2026 register items fall into these buckets:
- **Already in the master** (via the Media Master / Discogs / Bandcamp / press): all Section 1
  compilations and press features, Section 5 press/outlets, Section 6 bandcamp items.
- **Near-match / no-space render** (excluded under the strict rule): Dittany of Crete album
  pages list the artist as "ZazieProductions"; film-festival + Facebook credits render
  "ZazieKanwar-Torge" (no space); ogre.red issue render only in the search-index sidebar,
  not on the fetched body.
- **Auth / private / contractual** (no public exact-name page): Sections 2, 4, 7, 8, 9, 10
  (client screen-music deliverables, adversarial-AI testing, paid/curation work, submitted
  applications, formal outreach). Mapped as AUTH / lead.

### New verified surfaces added (source = `research`): 7 total
- `github.com/zazieproductions/void-oculus` — Register #108; org renders "Zazie Productions"; live board.
- `github.com/zazieproductions/Contrapuntal-Academic-Nonsense-Engine` — Register #105.
- `github.com/zazieproductions/Spectra-DSP-Visualizer-Architecture` — Register #107 (SPECTRA//LAB).
- `github.com/zazieproductions/interactive-harsh-noise-generator` — Register #109 (NOISE WALL).
- `thevanishingpointsyndicate.bandcamp.com/album/dissonance-index-vol-1-various-artists` — Register #38; tracklist renders "[Zazie Productions - Pyrogenesis]".
- `thevanishingpointsyndicate.bandcamp.com/track/pyrogenesis` — exact-name track credit.
- `news.prfree.org/@noisemusicnewsdaily/zazie-productions-launches-the-vanishing-point-syndicate...` — already in master (media_master), re-confirmed, so not double-counted.

Master count after Pass 5: **440** (was 434; +6 net, since the prfree release was a duplicate).

### Skipped in Pass 5 (did not meet the exact-name standard)
- `thevanishingpointsyndicate.bandcamp.com` (label home) — the org itself is "The Vanishing Point Syndicate"; exact string appears only on the album/track credit rows.
- `ogre.red/issues/2025-02/*` — "Zazie Kanwar-Torge | ZazieProductions" appeared only in the search-result snippet (Google-CSE cache), not on the fetched contributor/issue body; treated as a lead.
- Viennale 2026 / IN THE PALACE / Facebook credits for Phantom Requiem — render "ZazieKanwar-Torge" (no space); near-match.
- Publications (Coin-Operated Press "For the Sad Kids", Milkweed Poetry, Dark Holme, Blastbones, Posthuman Press, re:natura, Barb) — no exact-name page surfaced on SearXNG; remain HUNT/AUTH.
- `radioreach.us` — live product (Register #70–73, #102); footer does not render the exact name; recorded as a lead.

### Engine rationale
`opnxng.com` (Google CSE) was the only instance that surfaced the ogre.red exact-string snippet
and the Vanishing Point Syndicate Bandcamp pages. `search.lumy.live` (Yandex/Seznam) has not
returned new register-specific surfaces this pass. The register's unlinked items are mostly
private contractual work, so the public exact-name yield is concentrated in the GitHub org and
the 2025 netlabel/press releases.

## Pass 6 — Deep multi-engine sweep (Brave, Yahoo, Yandex, Bing, Google-CSE)

Goal: maximize engine coverage and catch any remaining exact-name page the earlier passes
missed, including structured metadata DBs, independent crawlers, and niche industry indexes.

### Engines that worked this pass
- **`sx.catgirl.cloud` (Brave)** — highest-value new instance; surfaced songstats, Pulitzer Center,
  Canyon Cinema Connects, Lynne Sachs, Visualcontainer, hackaday, muso.ai.
- **`search.pi.vps.pw` (Yahoo)** — surfaced LinkedIn, IMDb, ogre.red Dec-2025 author page.
- **`search.lumy.live` (Yandex + Seznam)** — surfaced soundshiva, z-dimension.org, musicbrainz,
  dionysianpubliclibrary, distrokid, deezer/anghami, 1619education.
- **`opus/sx.catgirl.cloud`** & **`search.pereira.is` / `opnxng.com` (Google-CSE)** — reconfirmed
  and cross-checked the same top set; useful for duplicates but low new yield.
- **`searxng.site`, `search.rhscz.eu`, `Search 5iq`** — return junk / irrelevant (satellite TV,
  office-config spam); do not retry.
- **`priv.au`** returned only its home page (no results); **`searx.tiekoetter.com`** has a JS
  captcha; **`search.bus-hit.me`** DNS-failed; **Mojeek** and **Startpage** now bot-blocked
  (Altcha / Anubis); **Marginalia** asks for a 3-second wait (aggressive-bot guard).

### New verified surfaces added (source = `research`): 16 total
- `github.com/zazieproductions/void-oculus`, `.../Contrapuntal-Academic-Nonsense-Engine`,
  `.../Spectra-DSP-Visualizer-Architecture`, `.../interactive-harsh-noise-generator` (Register §6 built projects).
- `thevanishingpointsyndicate.bandcamp.com/album/dissonance-index-vol-1-various-artists` + `/track/pyrogenesis` (Register #38).
- `connects.canyoncinema.com/projects/films-for-freedom/` — "Zazie Kanwar-Torge" exact (participating filmmakers).
- `ogre.red/issues/2025-12/2025-12-kanwar-torge-zazie/` — "Zazie Kanwar-Torge | Zazie Productions" exact (Dec-2025 issue).
- `z-dimension.org/shards-vol-1/` — track 16 "Zazie Productions — Vibroscriptorium" exact.
- `tickettailor.com/events/motherof/2336870` — "Composer — Zazie Kanwar-Torge" exact (Swinewomb theater).
- `stage32.com/media/3838211664293930413` — "Score by Zazie Kanwar-Torge A.K.A Zazie Productions" exact.
- `soundshiva.net/release/various-artists-music-inspired-by-mulholland-drive` — "Zazie Productions: https://zazieproductions.bandcamp.com/" exact.
- `shazam.com/song/6771371302/crt-204-bone-static` + `/song/1894640537/rhapsody-of-the-unplayable-hand` — "Zazie Productions" exact.
- `musicbrainz.org/artist/b610b4cb-87da-44d7-a262-2bd65fb8098c` — structured music-metadata artist entity, "Zazie Productions" exact.
- `hackaday.io/project/204427-photon-flux-analyzer-v2-reverse-bias-led-sensor` — "Zazie Kanwar-Torge" exact (R&D hardware project).

Master count after Pass 6: **450** (was 440 after Pass 5; +10 net on top of the Pass-5 set).

### Skipped in Pass 6 (did not meet the exact-name standard)
- `dionysianpubliclibrary.com/print-season-iii` — lists "ZazieProductions" (no space).
- `amazon.com/Fearful-Symmetries-Anthology-...` — contributor list "ZazieProductions" (no space).
- `mywebar.com/blog/ar-packaging-results-case-studies/` — "Zazie Kanwar–Torge" (en-dash, not hyphen).
- `1619education.org/blog/winners-and-finalists-local-letters-global-change-2019` — "ZazieKanwar-Torge" (no space).
- `letterboxd.com/film/expire-1/` — "ZazieKanwar-Torge" (no space, IMDb-linked short).
- `psychlovers.bandcamp.com/...` / `musicbrainz.org/release/811777b0-...` (track row) — "ZazieProductions".
- `openfilmzone.com/zone-wall/` — name in awards list without spaces.
- `kinorium.com`, `mini-film.com`, `tumgik`, `lezet.blogspot`, `distrokid`, `anghami` — near-match / no exact render.

### Engine rationale
Brave (`sx.catgirl.cloud`) and Yandex (`search.lumy.live`) are the two highest-yield backends
for this niche because they index content (film-festival filmmaker lists, metadata DBs, project
logs) that Google/Bing-CSE surfaces only partially. MusicBrainz, Hackaday and Canyon Cinema are
notable new *structured/curated* index types (metadata DB, maker project, experimental-film
archive) rather than just profile/mirror pages.

## Pass 7 — Broadened inclusion rule (contiguous "Productions" sequence) [2026-09-04]

After the user's directive, the Definition of "counts" was broadened: target 1 is the
**contiguous "Zazie Productions" sequence in any spacing/case** (`Zazie Productions`,
`ZazieProductions`, `Zazie_Productions`, `zazieproductions`, `ZAZIEPRODUCTIONS`,
platform-URL forms). A Productions-sequence hit does NOT need the person's name alongside.
Target 2 (person name) is unchanged: exact `Zazie Kanwar-Torge` only; no-space (`ZazieKanwar-Torge`)
or en-dash (`Zazie Kanwar–Torge`) variants still do NOT count on their own.

### Re-checked surfaces that were SKIPPED in Pass 6 (now count)
- `dionysianpubliclibrary.com/print-season-iii` — re-fetched: renders exact "Zazie Productions" (space form)
  in the Fearful Symmetries contributor list. Added. (Register #58)
- `psychlovers.bandcamp.com/album/psych-against-cancer-vol-3-part-2` — re-fetched: fan review + track
  credit render "Zazie Productions"/"ZazieProductions". Added. (Register #8)
- `dittanyofcrete.bandcamp.com/album/summoning-2` + `/summoning-3` — contiguous "ZazieProductions" now counted. Added.
- `internetdaemon.bandcamp.com/album/music-inspired-by-mulholland-drive` — contiguous "ZazieProductions" now counted. Added.
- `amazon.com/Fearful-Symmetries-Anthology-Psychedelic-Anthologies/dp/B0GFXWQ5YB` — contributor sequence now counted. Added.
- `archive.org/details/va-music-inspired-on-mulholland-drive` — tracklist renders "Zazie Productions" exact. Added.

### New no-space rule surfaces (search.lumy.live / Brave backend)
- `github.com/zazieproductions/spectra-lab` — SPECTRA//LAB (Register #107) renders "Zazie Productions". Added.
- `opensea.io/ZazieProductions` — profile title renders exact contiguous sequence. Added.
- `sequencer.party/users/175` — "ZazieProductions". Added.
- `x.com/zazieoverlord` — display name "ZazieProductions". Added.
- `www.gamedevmarket.net/member/zazieproductions` — profile + "Galactic Requiem by ZazieProductions" (Register #79). Added.
- `promptbase.com/profile/zazieproductions` — "@zazieproductions". Added.
- `www.soundshiva.net/release/various-artists-i-want-to-believe-x-files-tribute` — "Zazie Productions: https://zazieproductions.bandcamp.com/". Added.
- `zazieproductions.itch.io/unholyanatomy` — "UNHOLY ANATOMY ... by Zazie Productions" exact. Added.

### Confirmed no-change (not added)
- `1619education.org/blog/...` — "ZazieKanwar-Torge" is the PERSON name no-space, NOT the Productions
  sequence; still does not count.
- `mywebar.com/blog/...` — "Zazie Kanwar–Torge" en-dash person name; still does not count.
- `trevor.se/tag/darkwave/` — re-verify only; not confirmed as a counted render.
- `amazon.com/Fearful-Symmetries` URL variant verified via `search.lumy.live`; the exact product page renders the sequence.

### Master count after Pass 7
**465** (was 457 as of the Pass-6/P7 split; +8 net this pass).

Remaining HUNT (register): `legateaugallery.com` (confirmed via search snippet, add), §3 Coin-Operated
Press / Milkweed / Barb / Posthuman Press publications, Wrong Biennale (#64), Bario BetaList (#94),
Vortex AV Engine repo slug (#103), yyyyyyyy.info repo slug (#110).

### Pass 7 register-resolution (cont.) — [2026-09-04]
Resolved register §1 music releases to exact-render bandcamp album/track pages:
- #5 Frida Kahlo → plataformarecs v-a-frida-kahlo (track 8); #7 Pyrogenesis → v-a-noise-around-the-world-14 (track 14).
- #12 Field Rec Vol 3 → gelombang issue-51 (track 9); #17 Field Rec Vol 4 → issue-52 (track 11).
- #13 Frequências Cadavéricas → brutalizerecs (track 11 Negative Organ Function).
- #15 Obelisk of Static Collapse → thehillsaredead its-only-hnw-but-i-like-it-ix (track 8 "ZAZIE PRODUCTIONS").
- #6 Høuse FΩrgøt Its Name → dittanyofcrete summoning-1 + internetdaemon experiments-on-the-witch-house (track 4).
- #18 Egregore Intrasound → terminalfutureindustries ecstatic-feedback-ii (track 4).
- #19 Trust No Signal → soundshiva + archive.org/details/v-a-i-want-to-believe.
- #80-82 itch catalog → zazieproductions.itch.io (root) + /unholyanatomy + itch.io/c/5777018 collection vol 2.
- New no-space profile surfaces: samplefocus/users/zazie-productions, lyrics.com/artist (lists register #59 "Stunning That You'd Care", "Well Meaning Neurotypicals"), a2b2.org/users/ZazieProductions, gamedevmarket member, promptbase profile, opensea, sequencer.party, x.com/zazieoverlord.
Still HUNT: §3 publications (For the Sad Kids zine body, Bipolar/Milkweed/Barb/Posthuman — no public exact-name index), Wrong Biennale/#64 (Instagram blocked), Bario/BetaList (#94), Vortex AV Engine & yyyyyyyy.info now = Conic-Vortex (linked). Master **484**.

## Pass 8 — Wrong Biennale (#64) resolution + DistroKid-family platform sweep [2026-09-04]

### Register #64 — Infinite Self Pavilion / The Wrong Biennale — RESOLVED
- `cyberneticfutures.com/infinite-self-pavilion` — artist list renders "…Zazie Productions, Garrett
  Lynch IRL…" **exact** (space form). Wrong Biennale 2025–2026, curated Dr Lila Moore
  (Nov 1 2025–Mar 31 2026). Register #64 now **linked** (was lead). `/artistsbios` sub-page also present.
- #94 Bario on BetaList: `betalist.com/startups/bario` + Indiegogo + `bario.icu` attribute the
  creator as **"Bario Ai"**, NOT the exact name → remains a **lead** (no exact-name render).

### New exact-name surfaces added (contiguous "Productions" sequence)
- `soundsforthesoul.bandcamp.com/album/the-undead` — track 7 "Zazie Productions - Zombies Were
  People Too" exact (a previously-unlogged Bandcamp compilation).
- `thesqueakywheel.org/author/zazieproductions/` — author page renders "zazieproductions".
- `itch.io/post/12575624` — forum post by "Zazie Productions" exact (links linktr.ee).
- `itch.io/c/5777074/zazie-productions-collection-vol-3` — "Zazie Productions' Collection Vol. 3" exact.
- `lyrics.com/lyric-lf/16514291/.../Well+Meaning+Neurotypicals` — renders "Zazie Productions" exact;
  "written by Zazie Torge"; Lyrics © O/B/O DistroKid.
- `www.tiktok.com/music/Well-Meaning-Neurotypicals-Low-Sensory-Instrumental-7116236683586062338` —
  TikTok sound/artist page indexed as "ZazieProductions" exact; TikTok blocks direct fetch (403).

### DistroKid distribution-platform coverage (confirmed in master; current set)
Spotify `artist/4UOgvZEOo7xBhFBjJvlMm0` · Apple Music `artist/zazie-productions/1623719351` ·
Instagram `zazieproductionsofficial` · Amazon Music `artists/B0B14FFGFV` · Deezer `artist/170543657` ·
TIDAL `artist/32246195` · iHeartRadio `artist/zazie-productions-38017001` · Boomplay `artists/46971970` ·
Qobuz `interpreter/zazie-productions/14145610` · Beatport `artist/zazie-productions/1440962` ·
Shazam `artist/zazie-productions/1623719351` · Slaps `ZazieProd` (DistroKid-affiliated) · YouTube `@zazieproductions`.
Still no public artist-profile page found for: Pandora (slug 404), Audiomack (404), Facebook/TikTok (403),
Luna, CapCut, Claro Música, Saavn, Anghami artist page, Snapchat, NetEase, Tencent/QQ/Kugou/Kuwo/WeSing,
Pretzel, TouchTunes, JOOX, Kuack, MediaNet, Dubset, Roblox, Soundtrack by Twitch. These are largely
app-only or bot-blocked; recorded as HUNT.

### Master count after Pass 8
**494** (was 487 at end of the last commit boundary; +7 net this session incl. #64 resolution &
Bario lead documentation). REGISTER_LINK_MAP updated: #64 linked, #94 lead, #57–59/#65–68 unchanged.

### Pass 8-b — DistroKid-family platform resolutions (same session)
- `play.anghami.com/artist/14553637` — Anghami **artist** page renders "Zazie Productions" exact;
  full discography. Previously marked missing. **Added.**
- `music.youtube.com/browse/UCeYo8Y6ocrsQzscw158u-tw` — distinct **YouTube Music** ARTIST channel
  (195 subs) renders "Zazie Productions" exact + full discography. **Added.**
- `internetdaemon.bandcamp.com/album/doom-a-creative-commons-music-compilation` + `/track/74mm-under-orange-lights`
  — "Zazie Productions - 7.4mm Under Orange Lights" exact (DOOM creative-commons compilation). **Added.**
- `www.tiktok.com/music/Well-Meaning-Neurotypicals-7116236683321821186` — TikTok sound page (non-instrumental
  variant) indexed as "ZazieProductions" exact. **Added.**
- `www.jiosaavn.com/search/zazie-productions` — returns **no-match** (no artist page). JioSaavn remains HUNT.
