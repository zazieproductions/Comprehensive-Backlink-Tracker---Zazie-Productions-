# 🤖 06 — AGENT PROMPT TEMPLATES

> Copy-paste-ready briefs to hand any (future) research agent. Each prompt references this repo's files so the agent self-loads the rules. Fill the `<<BRACKETS>>` before sending.

---

## Template 0 — Universal preamble (prepend to every agent)

```
You are a meticulous web-presence researcher. The subject is ONE artist project:
"Zazie Productions", whose principal is the person "Zazie Kanwar-Torge"
(composer, film scorer, experimental/noise musician, filmmaker, multimedia artist).

TASK RULES — read and obey:
1. First read docs/01_MISSION_SCOPE_AND_RULES.md (what counts) and
   docs/02_DEEP_SEARCH_PLAYBOOK.md (how to search). They override anything vague here.
2. Only the EXACT strings "Zazie Productions" and "Zazie Kanwar-Torge" count as evidence.
   Do NOT count the French singer "Zazie", the company "Zazie Films", or mere handle/URL
   variants (record those only as LEADS).
3. For every hit, copy the exact snippet that proves the name, the URL, which engine/index
   you found it on, the date, the media-type, and mark evidence level
   (direct-verified / index-verified / lead).
4. Do not claim "verified" unless you opened the live page and read the exact name in it.
5. Deduplicate: a mirror of an original is one primary row.
6. Output new findings in the exact row template shown below. Append, never delete.
```

---

## Template 1 — Engine-family sweep (reuse for any family)

```
<<MISSION>>: sweep the <<FAMILY: major / meta+privacy / independent-obscure / regional / music-vertical / film-recognition / social-native / mirrors>> engines in docs/03_ENGINE_DIRECTORY.md (section <<X>>).

Run BOTH canonical names and then the near-handle and noise-filtered variants from
docs/04_QUERY_LIBRARY.md (sections A, B, C, and D as applicable).

ENGINES TO USE (exact): <<list, e.g. Mojeek, Stract, Marginalia, Wiby>>

INSTRUCTIONS:
- For each engine run at least: "Zazie Productions" then "Zazie Kanwar-Torge".
- Log EVERY unique public place found (not just the top 10).
- Keep going past page 1 on engines that show more than ~10 results when hits exist.
- Capture snippets + URLs + which engine found each.
Return a tidy list grouped by media type (🔴 press, 🌸 film, 🟣 recognition, 🔵 profiles,
🟠 music, 🩵 data, 🟢 social, 📼 mirror, 🖤 spam), each row following the row template.
```

---

## Template 2 — Search an unknown engine correctly (obscure-engine decoder)

```
You are testing whether the subject appears on a specific engine.
ENGINE: <<engine name / URL>>

1. Open the engine. If it has settings/regions, set the most permissive language/region.
2. Paste exactly, one at a time (record results after each):
   "Zazie Productions"
   "Zazie Kanwar-Torge"
   intitle:"Zazie Productions"
   site:<<relevant known host>> "Zazie Productions"
3. If zero results, try without quotes and with handle "zazieproductions" — and note whether
   the engine appears to have a small/regional index (that is a finding in itself).
4. Report: (a) whether the exact name surfaces, (b) the top URLs with snippets,
   (c) whether results are contaminated by the unrelated singer "Zazie",
   (d) the engine's index type (own / meta / niche) if you can tell.
```

---

## Template 3 — Platform internal-presence audit (music/film vertical)

```
Audit the presence of "Zazie Productions" / "Zazie Kanwar-Torge" on these platforms using
EACH platform's OWN internal search box: <<Spotify, Apple Music, Deezer, Bandcamp, Discogs,
Last.fm, MusicBrainz, RateYourMusic, SoundCloud, YouTube, IMDb, FilmFreeway, TheMovieDB, >>...

For each platform report a row:
PLATFORM | TYPE(artist/song/credit/profile/playlist) | EXACT NAME present?(Y/N/both) |
CANONICAL URL | EVIDENCE snippet | STATUS (live/needs-check)
Skip platforms that require login or block automation; say so and move on.
```

---

## Template 4 — Regional & non-English sweep

```
Run the census against region/language-specific surfaces for <<languages/regions: es-MX,
pt-BR, de-DE, es-ES, ru/CIS, fr-FR, pl-PL, nl-NL, ko-KR>>.

Use docs/03_ENGINE_DIRECTORY.md §4 (regional) and docs/04_QUERY_LIBRARY.md §H + §F.
Include Yandex (flip to RU/CIS) and regional-flipped Bing/DuckDuckGo.
Report any non-English press, lyric, or label page, quoting the local-language sentence
that contains the name. Flag likely spam/parasite pages separately (🖤).
```

---

## Template 5 — Link double-check / verification agent

```
Verify the live-ness and evidence of every URL in <<list or registry file>> for the subject.

For each URL:
1. Request it (respect robots; modest rate; follow one or two redirects). Record final HTTP
   status and any redirect chain.
2. If 200, load readable text and search for the exact strings "Zazie Productions" and
   "Zazie Kanwar-Torge". If found, tag ✅ LIVE/VERIFIED. If the page loads but the name is
   not visible (JS-gated, region wall, login), tag 🟡 PARTIAL and say why.
3. If error/not-found/blocked, retry once from an archive (web.archive.org) and once via a
   text proxy (r.jina.ai). If still nothing, tag ❌ BROKEN/NO-EVIDENCE and give the code.
4. Output rows: URL | STATUS(✅/🟡/❌) | HTTP code | exact-name-found?(Y/N) | note.
5. Never soften a ❌ into ✅. Accuracy over optimism.
See docs/07_LINK_CHECK_AND_VERIFICATION.md for the full runbook.
```

---

## Universal ROW TEMPLATE (use in every agent output)

```
| URL | MEDIA(emoji) | PRIORITY(A/B/C/Lead) | STATUS(✅/🟡/❌/⬜) | NAME(Both/Prod/Kanwar) | EVIDENCE(1-2 line snippet) | FOUND ON(engine/platform + date) | CONTEXT(track/film/compilation) |
```

Example row:

```
| https://www.last.fm/music/Zazie+Productions | 🔵 | 🥉C | ✅ | Prod | "Zazie Productions — albums, tracks..." | last.fm internal search · 2026-09-04 | artist profile |
```

---

## Prompt discipline

- **One agent = one family/phase.** Don't ask one agent to “do everything” — it breeds shallow, duplicate work.
- **Demand evidence columns.** A finding with no snippet and no found-on value is a lead, not a result.
- **Freeze then merge.** Agents return new rows; a human (or a merge agent) dedupes against `registry/` before committing.
- **Re-run for freshness** with a new date whenever a long time passes — the directory is a living snapshot, not a permanent truth.
