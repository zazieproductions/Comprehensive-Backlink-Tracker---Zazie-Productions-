# 🗺️ 03 — ENGINE DIRECTORY (color-coded)

> Run each exact name against **at least one engine per family**. Replace `QUERY` with the URL-encoded query (use `+` for spaces). Engines marked **own-index** matter most for *independent* coverage; engines marked **meta** are good for recall/confirmation; **cache/archive** are for *dead or JS-hidden* pages.

**Legend:** 🔵 Major/global · 🟢 Meta / privacy-aggregator · 🟣 Independent / obscure · 🔴 Regional · 🟠 Niche vertical · 🟤 Social-native · 🩵 Archive / cache / proxy · 🖤 Special (do-not-automate lightly).

---

## 🔵 1. Major global engines (own-index)

*Crawl everything first. Note many power each other.*

| Engine | Search URL pattern | Class | Notes |
|---|---|---|---|
| Google | `https://www.google.com/search?q=QUERY` | OWN | Largest index; also `tbm=` verticals (news `tbm=nws`, videos `tbm=vid`, images `tbm=isch`) |
| Bing | `https://www.bing.com/search?q=QUERY&setmkt=xx-XX&setlang=xx` | OWN | Second-biggest; supports `setmkt` region flips; Copilot layer |
| Yahoo | `https://search.yahoo.com/search?p=QUERY` | OWN (Bing-fed) | Different UI/surfacing, sometimes extra modules |
| Baidu | `https://www.baidu.com/s?wd=QUERY` | OWN (CN) | Chinese index — run once for CJK coverage |
| Naver | `https://search.naver.com/search.naver?query=QUERY` | OWN (KR) | Korean index — run once |
| Sogou | `https://www.sogou.com/web?query=QUERY` | OWN (CN) | — |
| Yandex | `https://yandex.com/search/?text=QUERY` (or `yandex.ru`) | OWN (RU/CIS) | **Obscure-gold**; use `title:` + `""`. Region-flip to RU/CIS for best recall |

---

## 🟢 2. Meta / privacy layers

*High recall, de-personalized; a hit here is a lead until verified on the source page.*

| Engine | Search URL pattern | Class | Notes |
|---|---|---|---|
| DuckDuckGo | `https://duckduckgo.com/?q=QUERY` | META (Bing/etc.) | Familiar; region setting available |
| Startpage | `https://www.startpage.com/sp/search?query=QUERY` | META (Google) | Unbiased Google results — good *second* check |
| Ecosia | `https://www.ecosia.org/search?q=QUERY` | META (Bing) | EU context |
| Qwant | `https://www.qwant.com/?q=QUERY` | META/OWN (EU, FR) | EU/FR slant |
| MetaGer | `https://metager.org/meta/meta.ger3?eingabe=QUERY` | META (DE) | Non-profit metasearch |
| SearXNG | instance-dependent → see **searx.space** for a live public list; pattern `https://INSTANCE/search?q=QUERY` | META | **User's requested engine.** Fan out across 2–3 live instances (each enables different backends). |
| Kagi | `https://kagi.com/search?q=QUERY` | OWN+ (paid) | Power-user lenses, high signal-to-noise |

**AI-answer engines** *(ask them directly; treat every cited URL as a lead to verify):*
`https://www.perplexity.ai/search?q=QUERY` · `https://chatgpt.com/` · `https://you.com/search?q=QUERY`

---

## 🟣 3. Independent / obscure (own crawlers — where the long tail lives)

*These reach the small indie net-label / blog / fan-web pages the mega-indexes bury.*

| Engine | Search URL pattern | Class | Notes |
|---|---|---|---|
| Mojeek | `https://www.mojeek.com/search?q=QUERY` | OWN | UK independent index; supports `inurl:`, `intext:`, `intitle:` |
| Stract | `https://stract.com/search?q=QUERY` | OWN | Open-source independent index |
| Marginalia | `https://search.marginalia.nu/search?query=QUERY` | OWN | Favors old/indie/non-commercial web |
| Wiby | `https://wiby.me/?q=QUERY` | OWN | Old-school lightweight pages |
| Yep | `https://yep.com/web?q=QUERY` | OWN | Ahrefs-backed independent search |

---

## 🔴 4. Regional & language-flipped

*Change the UI region/language to your query, not just the words — many Euro/LatAm/Asian music & press sites only rank under a regional SERP.*

- Bing with `setmkt` per country (es-ES, es-MX, pt-BR, de-DE, fr-FR, pl-PL, nl-NL, ko-KR, ja-JP…).
- Yandex `.ru`, `.com.tr`, `.co.il`, etc. — flip region to CIS/EU/TR.
- DuckDuckGo & Google: set region + language in settings.
- **LatAm press found in the dump** (`indieam.com.mx`, `disconecta.com.br`, `radioclickdigital.com.ar`, `rockculture.es`) suggests **Spanish/Portuguese SERPs** are high-value. Search the Spanish quotes: `"Zazie Productions"` + `reseña`, `crítica`, `música`, `lanzamiento`.
- Also try localized *lyric/stream* verticals' internal search (see §9).

---

## 🟠 5. Niche vertical — MUSIC (search each one's *internal* box)

*Detecting presence here is the point; treat these as targets, and also `site:`-query them from the open engines.*

| Platform | Internal search URL | What you're hunting |
|---|---|---|
| Spotify | `https://open.spotify.com/search/QUERY` | artist/album/track/credit rows |
| Apple Music | `https://music.apple.com/us/search?term=QUERY` | artist page / composer credits |
| Deezer | `https://www.deezer.com/search/QUERY` | artist profile |
| Bandcamp | `https://bandcamp.com/search?q=QUERY&item_type=b` | storefronts, labels, compilation rows |
| Discogs | `https://www.discogs.com/search/?q=QUERY` | the 60-compilation credit index |
| Last.fm | `https://www.last.fm/search?q=QUERY` | artist page & scrobble index |
| MusicBrainz | `https://musicbrainz.org/search?query=QUERY&type=artist` | canonical artist record |
| RateYourMusic | `https://rateyourmusic.com/search?searchterm=QUERY&searchtype=l` | credits/appearances |
| SoundCloud | `https://soundcloud.com/search?q=QUERY` | hosted radio art / label sets |
| YouTube | `https://www.youtube.com/results?search_query=QUERY` | channel + every track upload |
| Lyrics aggregators | `lyrics.com`, `genius.com`, `songdata.io`, `sonichits`, `paroles-musique.com` | lyric-page rows |
| Streaming analytics | `songstats.com`, `breakinghits.app`, `viberate`, `chosic` | analytics-profile rows |

**Regional/stream mirrors in the dump to also `site:`-search:** `music.163.com` (NetEase), `douyin.com`, `kkbox.com`, `play.anghami.com`, `gequbao.com`, `fangpi.net`, `qobuz.com` (de-de), `ligaudio.ru`, `zvu4no.org`, `boomplay.com`, `iheart.com`, `x-minusovka.com`, `clipzui.fun`.

---

## 🟠 6. Niche vertical — FILM, TV, festivals, art

| Platform | Internal search URL | What you're hunting |
|---|---|---|
| IMDb | `https://www.imdb.com/find/?q=QUERY` | name nm17333332 & film credits |
| TheMovieDB | `https://www.themoviedb.org/search?query=QUERY` | person/credit mirror rows |
| FilmFreeway | `https://filmfreeway.com/QUERY` | filmography + award/news feed |
| Letterboxd | `https://letterboxd.com/search/QUERY/` | film presence |
| AllMovie / JustWatch | search each | presence |
| Art platforms | `art.kunstmatrix.com`, `artrabbit.com`, `behance.net`, `arthive.com` | artist/exhibition rows |
| Festival pages | `pebblesunderground.art`, `thelatest.co.uk`, `newmediartspace.info`, BMC etc. | award/screening/exhibition listings |

---

## 🟠 7. Niche vertical — ACADEMIC / LITERATURE / CODE

| Target | Where to search | Notes |
|---|---|---|
| Google Scholar | `https://scholar.google.com/scholar?q=QUERY` | any research/paper/abstract mention |
| Semantic Scholar / Crossref / OpenAlex | their search APIs/pages | scholarly metadata |
| Archive of Our Own (AO3) | `https://archive.transformativeworks.org/works/search?utf8=✓&work_search[query]=QUERY` | a fan-work already referenced (`works/56506408`) |
| AllPoetry / Vocal / Wattpad / FanFiction | internal search | creative-writing presence |
| GitHub | `https://github.com/search?q=QUERY&type=code` | code/username references |
| Hackaday.io | search | hardware/audio project profile already found |
| Replit / Grep.app / Common Crawl | internal / `grep.app` | code & web-snapshot presence |

---

## 🟤 8. Social-native search (post-level presence)

| Platform | Search URL | Notes |
|---|---|---|
| X/Twitter | `https://x.com/search?q=QUERY` | posts + replies mentioning the name |
| Bluesky | search in-app / `bsky.app` | the dump has a bluesky post |
| Reddit | `https://www.reddit.com/search/?q=QUERY` | r/AlbumArtPorn etc. |
| Mastodon | per-instance search (e.g. `mastodon.bida.im`) | fediverse posts |
| Instagram / TikTok | in-app search | limited web access; note handles found |

---

## 🩵 9. Archive / cache / text-proxy (recover dead or JS-hidden pages)

| Tool | How to use |
|---|---|
| Wayback Machine | `https://web.archive.org/web/*/QUERY` (view) · `https://web.archive.org/cdx/search/cdx?url=DOMAIN&output=json&fl=timestamp,original,statuscode&collapse=urlkey&limit=5000` (bulk list every captured URL under a domain — **excellent for domain sweeps**) |
| CachedView | `https://cachedview.nl/` — try multiple cache providers |
| r.jina.ai text proxy | `https://r.jina.ai/http://…` or `https://r.jina.ai/https://…` — fetch a page's readable text when JS-gated |
| Common Crawl index | `http://index.commoncrawl.org/CC-MAIN-2026-*?url=DOMAIN&output=json` — which pages of a domain were crawled |

**Power move:** for any domain known to host the name, run the Wayback **CDX** query above to enumerate every historical URL under that domain, then grep for name-bearing paths (e.g. all `bandcamp.com` album pages that ever credited the name).

---

## 🖤 10. Care & compliance (automation etiquette)

- Respect each site's **robots.txt** and ToS; add **rate limiting + delays**; rotate instances for SearXNG.
- When using tools/scripts on engines, keep volume modest and identify clearly. When in doubt, do it by hand in a browser.
- Baidu, Naver, social logins, and some regional engines block datacenter traffic — plan a manual or browser-assisted pass for those.

*Next: the copy-paste [`04_QUERY_LIBRARY.md`](04_QUERY_LIBRARY.md).*
