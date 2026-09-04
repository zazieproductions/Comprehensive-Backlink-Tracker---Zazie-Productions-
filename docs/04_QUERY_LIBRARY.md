# 🔤 04 — QUERY LIBRARY (copy-paste)

> Every query below is ready to paste. Replace nothing unless told. These are grouped: **canonical**, **near/handle**, **noise-filtered**, **platform `site:` dorks**, **file-type**, and **context qualifiers**. Run them across the families in `03_ENGINE_DIRECTORY.md`.

> URL-encode `+` for spaces when building search URLs: e.g. `"Zazie Productions"` → `%22Zazie+Productions%22`. The literal strings below work in any search box.

---

## A. Canonical exact-name queries (run first, everywhere)

```
"Zazie Productions"
"Zazie Kanwar-Torge"
("Zazie Productions" OR "Zazie Kanwar-Torge")
```

## B. Near-name / handle variants (leads, not counted)

```
Zazie Productions Zazie Kanwar-Torge
"Zazie Kanwar Torge"            <- hyphen/spacing variant (lead)
"Zazie Productions" composer film soundtrack
zazieproductions
zazie-productions
zazie_productions
"@zazieproductions"
"@ZazieProd"
"Zazie Kanwar-Torge" IMDb
```

## C. Noise-filtered (use when the French singer "Zazie" floods results)

Google/Bing/Brave/Mojeek/Startpage:

```
"Zazie Productions" -"Zazie" -musique -chanson -Paris -"Tout là-haut"
```

DuckDuckGo (no reliable `OR`; run negatives):

```
"Zazie Productions" -musique -chanson
```

Short-name sweep **only** if needed (still noisy — prefer full two-word strings):

```
"Zazie" "Productions" -"Zazie" -musique -chanson
```

Title/URL targeted forms (skip the generic short name entirely):

```
intitle:"Zazie Productions"
inurl:"zazie-productions"
inurl:"zazieproductions"
intitle:"Zazie Kanwar-Torge"
```

## D. Platform `site:` dorks (paste into any engine that honors `site:`)

Run each with BOTH target names. The two-line pattern per platform:

```
site:open.spotify.com "Zazie Productions"
site:open.spotify.com "Zazie Kanwar-Torge"
```

Music streaming / lyrics / analytics:

```
site:music.apple.com "Zazie Productions"
site:music.apple.com "Zazie Kanwar-Torge"
site:deezer.com "Zazie Productions"
site:bandcamp.com "Zazie Productions"
site:last.fm "Zazie Productions"
site:soundcloud.com "Zazie Productions"
site:discogs.com "Zazie Productions"
site:musicbrainz.org "Zazie Productions"
site:shazam.com "Zazie Productions"
site:qobuz.com "Zazie Productions"
site:tidal.com "Zazie Productions"
site:music.163.com "Zazie Productions"
site:songstats.com "Zazie Productions"
site:lyrics.com "Zazie Productions" OR "Zazie Kanwar-Torge"
site:genius.com "Zazie Productions"
```

Film / TV / festivals / art:

```
site:imdb.com "Zazie Kanwar-Torge"
site:themoviedb.org "Zazie Productions"
site:filmfreeway.com "Zazie Productions"
site:stage32.com "Zazie Kanwar-Torge"
site:artrabbit.com "Zazie"
site:behance.net "Zazie Productions"
site:arthive.com "Zazie"
site:pebblesunderground.art "Zazie"
site:thelatest.co.uk "Zazie"
site:newmediartspace.info "Zazie"
site:kunstmatrix.com "Zazie"
```

Press / editorial / blogs:

```
site:prfree.org "Zazie Productions"
site:medium.com "Zazie Productions"
site:telegra.ph "Zazie Productions"
site:tinnitist.com "Zazie Productions"
site:billboardwire.com "Zazie Productions"
site:grammyweekly.com "Zazie Productions"
site:rockculture.es "Zazie Productions"
site:indieam.com.mx "Zazie Productions"
site:disconecta.com.br "Zazie Productions"
site:radioclickdigital.com.ar "Zazie Productions"
site:blackmountaincollege.org "Zazie"
site:pulitzercenter.org "Zazie Kanwar-Torge"
```

Social & community:

```
site:x.com "Zazie Productions"
site:reddit.com "Zazie Productions"
site:bsky.app "Zazie Productions"
site:quotev.com "Zazie Productions"
site:tiermaker.com "Zazie Productions"
site:perchance.org "zazieproductions"
site:youtube.com "Zazie Productions"
site:youtube.com "@zazieproductions"
site:medium.com "Zazie Productions"
site:the-dots.com "Zazie Productions"
site:itch.io "zazieproductions"
site:gumroad.com "Zazie Productions"
site:linktr.ee/zazieproductions
```

Wiki mirrors / reference (run on *each* mirror — they mirror independently):

```
site:wikimili.com "Zazie Productions"
site:wiki2.org "Zazie Productions"
site:wikiwand.com "Zazie Productions"
site:wikigit.org "Zazie Productions"
site:fandom.com "Zazie Productions"
site:tvtropes.org "Zazie Productions"
```

## E. File-type sweeps (records/PDFs, honor rolls, anthologies, releases)

```
"Zazie Productions" filetype:pdf
"Zazie Kanwar-Torge" filetype:pdf
"Zazie Productions" filetype:doc
"Zazie Kanwar-Torge" filetype:docx
("Zazie Productions" OR "Zazie Kanwar-Torge") filetype:csv
```
(Bing alternative: `"Zazie Productions" ext:pdf`.)

## F. Context qualifiers (broaden recall when an exact search returns too little)

These help surface *indirect* but legitimate pages (compilations, credits, roundups) that mention the name deep in text:

```
"Zazie Productions" netlabel compilation
"Zazie Productions" "harsh noise" compilation track
"Zazie Productions" "The Vanishing Point Syndicate"
"Zazie Productions" "Dissonance Index"
"Zazie Productions" "Phantom Requiem"
"Zazie Kanwar-Torge" "Phantom Requiem"
"Zazie Kanwar-Torge" film composer score
"Zazie Productions" "Can't Get My Eyes Off You"
"Zazie Productions" "Seroquel Coma"
"Zazie Productions" experimental noise
"Zazie Kanwar-Torge" psychologist? psychological horror composer
```

## G. Backlink / credit chasing

Given a canonical asset or release, chase its mirrors and credits:

```
"UX2kv3G89Jw"                       <- Phantom Requiem YouTube ID (mirror sweep)
"Phantom Requiem" "Zazie Productions"
"Phantom Requiem" "Zazie Kanwar-Torge"
"Zazie Productions" "Shadowlands 4"
"Zazie Productions" "Late Night Love Letters"
"Zazie Productions" "Synthetic Dystopia"
intext:"Zazie Productions" "compilation"
intext:"Zazie Productions" "Various Artists"
```

## H. Spanish / Portuguese (the LatAm press cluster)

```
"Zazie Productions" reseña
"Zazie Productions" crítica música
"Zazie Productions" lanzamiento
"Zazie Productions" resenha
"Zazie Productions" "Can't Get My Eyes Off You" español
```

---

## House rules for queries

1. **Exact two-word phrases first.** Never rely on the bare word `Zazie`.
2. **Run both names** (`Zazie Productions` **and** `Zazie Kanwar-Torge`) for every pattern that matters.
3. **One clause per search box** unless combining with a documented operator.
4. When an engine ignores an operator (DDG `OR`, some `site:` limits), **fall back to splitting** into simpler queries — a split search beats a silently-ignored one.
5. **Screenshot/copy the snippet** proving the exact name — that's your evidence (see `01` §5).

*Next: [`05_WEEK_PLAN_AND_CADENCE.md`](05_WEEK_PLAN_AND_CADENCE.md) for the day-by-day schedule.*
