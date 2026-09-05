# Web-Presence Blind-Spot Expansion — Pass 11 (2026-09-05)

**Targets:** "Zazie Productions" (contiguous, any case/spacing) · "Zazie Kanwar-Torge" (exact).
**Baseline deduped against:** `data/master/master_index.csv` (522 rows) + all registry CSV/MD URLs
(1,041 normalised known URLs). Nothing listed below as *new* appeared in that baseline.
**Tooling constraints this pass:** sandbox egress blocked (no curl); all web work via page-fetch
and web-search tools; Internet Archive intermittently "Temporarily Offline" (CDX) — the
availability API and direct snapshot URLs worked. Bluesky search 403; RYM bot-wall; Reddit via
redditmedia mirror only.

**Data files:** `registry/web_presence_expansion/` — `discoveries.csv` (28) · `backlinks.csv` (16) ·
`entity_map.csv` (17) · `historical_records.csv` (22) · `web_archaeology.csv` (5) ·
`research_log.csv` (36). **20 canonical records** reconciled into the master index
(source = `web_presence_expansion`), derived docs regenerated (544 records).

Evidence levels used: **destination page** > **DB/API metadata** > **archive** > **index** >
**snippet (lead only)**. CV value 1–5; "Best use" per the user's list.

---

## Executive answers

| Question | Answer |
|---|---|
| **What is genuinely new?** | (1) VisualcontainerTV Winter-2024 award **press-release PDF** naming both name forms with "JURY SPECIAL MENTION" and a Feb 1–15 2025 broadcast window. (2) The **deleted PVTV Fringe Flicks April-2025 programme page**, recovered from Wayback: *Deaf Orphans of Streamcast*, "Director: Zazie Kanwar-Torge", screened 4 Apr 2025 at DoES Liverpool alongside Kenneth Anger's *Lucifer Rising* (+ PVTV Patreon and Eventbrite corroboration). (3) **8 IMDb title records** (4 with full credits verified) under nm17333332. (4) **5 Discogs release IDs** absent from master (2 with role=Main). (5) A **5-post clongclongmoo.org backlink cluster** (2025–26) with live links to bandcamp + linktree. (6) The **only genuine third-party discussion** found: an AI-authenticity challenge in the Lake Ivan review comments and the author's process reply. (7) Machine-readable facts: GitHub account created **2021-06-09** (earliest dated self-owned asset); Substack profile; TMDB movie record. |
| **Which dimension produced most?** | **Area 4 (entity/machine-readable)** by count (IMDb titles, Discogs API, GitHub API, TMDB, Substack) and **Area 5 (historical)** by quality (the recovered PVTV page, the earliest Bandcamp bio, BMC page provenance). Area 3 (social) produced almost nothing independent — consistent with the prior passes. |
| **Professionally important finds** | *Film CV:* VisualcontainerTV PDF (value 4); PVTV Liverpool screening (value 3, cite via Wayback URL); IMDb title crosswalk (value 3). *Composer CV:* BMC page provenance (unchanged since 2021-12-05; value 4 as an authority anchor, not new). *Press kit:* Pebbles film-card image + VisualcontainerTV collage poster. *Grants/bio honesty:* the Lake Ivan comment thread documents the artist's own account of tool use (RIFE/StyleGAN-2 assists) — useful if AI-assistance questions arise. |
| **Independent & authoritative vs derivative/spam** | Independent: VisualcontainerTV PDF, PVTV (archive + Patreon), Lake Ivan (known), BMC (known), clongclongmoo (independent but *derivative* — reposts label credit text). Self-authored: TMDB movie, Substack, GitHub, groover, itch forum reply, r/lastfm comment (associated account). Spam: BMC/Levinson doorway cluster (14 hosts, one copy source), YouTube mirror cluster (~40). |
| **What disappeared?** | `peopleversus.tv/fringe-flicks-archive/april-2025/` (404; site search returns nothing for "Kanwar-Torge"; 6 Wayback captures to 2026-02-15). Older ReelCrafter reel `z6vU_hn4T76AE0kv4rtd9w` dead (a newer reel ID is on Linktree). `zazieproductions.com` has **never** been captured by Wayback or Common Crawl despite being referenced in bios. 2021 Bandcamp bio ("teenage friend you wished you had in high school", Typescript-magazine claim) since replaced. |
| **Spam clusters tracing to one source** | **BMC_LEVINSON_SPAM_CLUSTER** → single copy source `blackmountaincollege.org/broadcast-bmc-radio-artist-zazie-productions/` (text unchanged 2021-12-05 → today). Common Crawl shows member `childrenofyemen.org` serving thousands of unrelated keyword slugs with an identical 600-byte digest → keyword-doorway network on hijacked domains. **YT_UX2kv3G89Jw_MIRROR_CLUSTER** → YouTube metadata for one video. |
| **Unresolved leads (manual pass)** | Bluesky (login-gated); RateYourMusic artist page (bot wall); Reddit user ManicMolotov profile (gated); r/lastfm ujng7o target comment (snippet only, thread deep); "Typescript magazine" playlist feature (claimed 2021, never located); `mycommunitycinema.org.uk` PVTV pages (known URL, not re-fetched); linktr.ee Wayback history (CDX empty shell); Wayback CDX for itch.io/filmfreeway/github (IA offline); VIAF/ISNI (tool-limited, inconclusive); 4 IMDb titles' credit pages not opened. |

---

## 1 · Real backlinks (not mentions)

Rule applied: a *backlink* is an `<a href>` from a third-party page to a target-owned property.
Boilerplate nav links and platform auto-links are excluded. Full table: `backlinks.csv`.

| # | Source | → Destination | Anchor | Type | Independence | Status |
|---|---|---|---|---|---|---|
| BL-001/002 | pebblesunderground.art/video/phantom-requiem/ | linktr.ee/zazieproductions; zazieproductions.bandcamp.com | URL text | editorial credit | independent festival | live |
| BL-003 | visualcontainer.tv …Press-Release.pdf | linktr.ee; bandcamp | URL text (in PDF) | editorial credit | independent institution | live |
| BL-004 | lakeivan.substack.com review | youtube.com/watch?v=UX2kv3G89Jw | "Phantom Requiem" | inline editorial | independent critic | live |
| BL-005–009 | clongclongmoo.org (5 posts: Beyond The Body 05/2025, Ju-On 07/2025, Experiments on the Witch House 10/2025, I Want To Believe 07/2026, DOOM 08/2026) | zazieproductions.bandcamp.com (+ linktr.ee in Ju-On) | URL text | credit list (reposted label notes) | independent aggregator, **derivative text** | live |
| BL-010 | archive.org/details/ju-on-the-music-compilation | bandcamp; linktree | URL text | label-authored | not independent press | live |
| BL-011 | groover.co curator profile | linktr.ee | URL | profile field | self | live |
| BL-012 | itch.io/t/4739756 (forum reply) | linktr.ee | URL | self-posted comment | self | snippet-verified |

**Mentions that are *not* backlinks (important for authority accounting):**
- `blackmountaincollege.org` BMC Radio Artist page — high-authority **mention**, zero outbound links to target properties.
- PVTV April-2025 programme (archived) — "Director: Zazie Kanwar-Torge" unlinked (other directors received IG/site links).
- PVTV Patreon update — title-only listing.
- r/lastfm comment — mention by the associated ManicMolotov account.

**Net:** 3 independent editorial backlink sources (Pebbles, VisualcontainerTV, Lake Ivan→YouTube) + 1 legitimate-but-derivative aggregator cluster. No new high-authority inbound links were found; the strongest institutional page (BMC) does not link out.

---

## 2 · Visual web presence

| Asset | Where | Names visible? | Use | CV | Notes |
|---|---|---|---|---|---|
| **Winter-2024 Award Winners press-release PDF** (6 pages read) | visualcontainer.tv/wp-content/uploads/2025/01/… | **Yes — both forms** | Film CV / Press Kit | **4** | Full PHANTOM REQUIEM entry: "by Zazie Kanwar-Torge (Zazie Productions) \| USA (2024) – JURY SPECIAL MENTION", synopsis, bio, links. Same `achievement_id` as the Pebbles page (ACH_PEBBLES_JURY_SPECIAL_MENTION_2024) — one achievement, two institutions, one broadcast leg (Feb 1–15 2025). |
| "winter 2024 award winning works on air february 1-15" collage poster | visualcontainer.tv …/Winter2024AW_Poster.landscape-1024x576.png | target card not legible | Press Kit (supporting) | 2 | Viewed. Programme-level artwork only. |
| Pebbles film card `PHANTOM-REQUIEM-by-Zazie-Kanwar-Torge_Zazie-Productions-1024x576.jpg` | pebblesunderground.art/wp-content/uploads/2024/12/ | filename + page title | Press Kit / Film CV | 3 | Festival-produced card; image itself not fetchable from sandbox (URL recorded). |
| "Jury and Audience Award Winners — Winter Screenings 2024" graphic | pebblesunderground.art …/AWARD-WINNERS_GENERIC.jpg | no | Press Kit | 1 | Generic. |
| Stage32 stills (Phantom Requiem / Deaf Orphans / Beyond The Silken Threads) | stage32.com/profile/1164424 | self-uploaded | Research Only | 1 | Only images an image-search returns for the target; self-hosted. |
| horror.zazieproductions.com posters (8) + 6 YouTube IDs | self site | self | Research Only | 1 | Read earlier this pass; self-hosted, not independent. |

Negative: generic image searches ("Zazie Productions poster/flyer") return unrelated stock/Etsy
results; no independent flyers, venue posters or print credits surfaced. No PVTV April-2025
poster with the target's name was found (the archived page's images are unrelated stills).

---

## 3 · Social / community / discussion

| Item | Class | Verdict |
|---|---|---|
| lakeivan.substack.com comments (2025-03-24): zach dorn questions if the film is AI-generated; target (@zazieproductions) posts a long process statement (Blender Decimate, hand-keyed on 3s/4s + RIFE interpolation, StyleGAN-2 texture variation, After Effects vector blur, "$300 budget", "19 years old"); reviewer replies | **independent discussion + author reply** | Only genuine third-party discussion found. Research Only / press-kit context. Not an accolade. |
| r/lastfm ujng7o (May 2022) — "Constrained Capacity by Zazie Productions… relatively unknown noise album that I adore" by ManicMolotov | associated account | Same account as the known r/musicsuggestions self-post → `CL_REDDIT_MANICMOLOTOV_2022`; **not fan coverage**. |
| mastodon.bida.im/@iyezine status | automated (dlvr.it) | known; re-tagged *automated*. |
| Bluesky | access-gated | API 403 on repeat; web search login-gated. Manual lead. |
| Mastodon.social search, Tumblr, X, TikTok, FB, IG (web-search) | none new | negatives logged. |
| Last.fm / RYM | none new | only known RYM song page; RYM artist page bot-walled. |
| itch.io community reply (t/4739756) | self-posted | lead (snippet). |
| Substack profile @zazieproductions | self | no newsletter; 2 subscriptions (incl. "UNdersUNg by VIK KANWAR" — noted, not analysed). |

Assessment: no independent fan discussion, forum thread or repost surfaced beyond the Lake Ivan
comment exchange. Social footprint remains self-originated.

---

## 4 · Entity / machine-readable crosswalk

Full table: `entity_map.csv`.

| System | Entity name | ID | Connects to | Authored by | Note |
|---|---|---|---|---|---|
| IMDb | **Zazie Kanwar-Torge** | nm17333332 | 8 titles: tt19369318 (Phantom Requiem), tt43438100, tt37707793, tt43746773 (credits verified); tt43407807, tt36984141, tt36954700, tt38637541 (filmography-listed) | IMDb | **new title IDs** |
| TMDB | **Zazie Productions** | person 5112050 · movie 1328893 | IMDb nm/tt | target's own account (ZazieProductionsEnterprises) | **Identity split**: same person is "Kanwar-Torge" on IMDb, "Zazie Productions" on TMDB/MusicBrainz. |
| MusicBrainz | Zazie Productions (type Person, US) | b610b4cb-87da-44d7-a262-2bd65fb8098c | Discogs, RYM, Spotify, Bandcamp, Apple | community | no Wikidata/ISNI/VIAF rels |
| Discogs | Zazie Productions | artist 11354435 → 64 releases | MusicBrainz | community; profile empty, "Needs Major Changes" | **5 releases missing from master** → added: 35541229 (Constrained Capacity, Main), 36415555 (Amnesia X Zazie Productions, Main), 38112006, 38147292 (+ 32807628 is the main release of known master 4006543 — not added). |
| GitHub | Zazie Productions · company "Zazie Productions LLC" | user 85637520 | linktr.ee | self | created **2021-06-09**; 38 repos; 31 followers |
| Substack | Zazie | 35672413 / @zazieproductions | Lake Ivan comment | self | |
| Wikidata | — | none | | | searched both names — none — 2026-09-05 |
| LoC id.loc.gov | — | 0 hits | | | |
| VIAF / ISNI | — | inconclusive | | | endpoints returned empty shells — tool-limited, not a negative |
| Common Crawl 2026-34 | zazieproductions.com | **no captures** | | | |

Conflicts/duplicates: (a) IMDb ↔ TMDB name split (above); (b) songstats has two fragmented IDs
(known); (c) MusicBrainz "Person" typed under the project alias. Recommendation for a manual
pass: add IMDb/TMDB/GitHub URL relationships to the MusicBrainz artist and align the TMDB
person name with IMDb, or document the alias explicitly.

---

## 5 · Historical / deleted presence — timeline

Full table: `historical_records.csv`.

- **2021** — 06-09 GitHub account created (API). 09-14 first Bandcamp capture (Archive Team): 4 albums (*Sellotape*, *demos, outtakes…*, *Stutter to stammer*, *G7e Torpedo*); bio: "Asheville-based experimental producer… & the teenage friend you wished you had in high school… playlist curator… featured on The Typescript magazine". 12-05 BMC Radio Artist page first captured (14 captures → 2026-05-09, text unchanged, still "Postponed – Date TBD").
- **2022** — 05-06 *Constrained Capacity* first archived; 05-06/05-10 ManicMolotov Reddit posts.
- **2023** — 03-21 *Distant Bells* archived; 07-27 Discogs artist image uploaded.
- **2024** — 06-11 *Anything Can Happen* / *Interference Archive* archived; 12 Pebbles Underground Jury Special Mention; 12-23 WFCN profile created (JSON-LD, snippet).
- **2025** — 02-01→15 VisualcontainerTV broadcast; 03-03 *To Halt Space Adrift* archived; 03-24 Lake Ivan review + comment debate; 04-01 PVTV Patreon line-up; **04-04 PVTV Fringe Flicks screening, Liverpool**; 04 castingcall.club joined; 04-26 first FilmFreeway capture; 08-15 first itch.io capture.
- **2026** — 01-28 *Greetings From Tinsel Time (Super Deluxe)* archived; PVTV site redesign deletes the archive page (last capture 02-15); older ReelCrafter reel dead by 09-05.
- **Never archived:** zazieproductions.com (Wayback 0, Common Crawl 0). linktr.ee history unresolved.

---

## 6 · Web archaeology / spam clusters

Full table: `web_archaeology.csv`.

**BMC_LEVINSON_SPAM_CLUSTER** (14 Tier-D hosts, unchanged count)
- *Copy source:* the BMC Radio Artist page (and its listing page) — confirmed unchanged since 2021-12-05 via Wayback.
- *Injection pattern:* random-slug subdirectories (`/zvgw5/`, `/KmDEB/`, `/gDrA/`, `/x83v4/`) on hijacked or expired WordPress domains; keyword slug "black-mountain-college-ira-and-ruth-levinson-museum". Common Crawl (CC-MAIN-2026-34) lists `childrenofyemen.org` serving thousands of unrelated keyword slugs, each with the same 600-byte body digest → cloaked doorway pages.
- *Domain purposes:* Italian newspaper archive, Slovak builder, Yemen charity, Czech designer, Korean tech firm, US credit union, Peruvian cable company, French SARL — none editorial.
- *Live status:* 2 sampled members failed (HTTP 500 / fetch error). Cluster is decaying.
- *Verdict:* zero independence; keep in census as Tier D; never cite.

**YT_UX2kv3G89Jw_MIRROR_CLUSTER** (~40 hosts) — YouTube-ID proxy sites; not re-swept; no new members.

**CL_CLONGCLONGMOO_NETLABEL_FEED** (5 posts) — *not spam*: a long-running (since 2010) German netlabel news hub republishing label submissions verbatim. Independent host, derivative text, real links. Count as one aggregator cluster, not five features.

**CL_REDDIT_MANICMOLOTOV_2022** — associated account; self-recommendation pattern across ≥2 subreddits.

**CL_DEAD_PVTV_APRIL_2025** — legitimate independent page lost to a CMS redesign; cite the Wayback URL.

---

## Reconciliation performed

- `data/master/master_index.csv`: +20 rows (source `web_presence_expansion`, status `verified`), no duplicates against normalised baseline. 524 → 544 records after merging with main's Pass 10 low-trust quarantine; tiers A 107 · B 172 · C 192 · D 73.
- `scripts/generate_docs.py` re-run → `data/master/SUMMARY.md` + 15 category docs.
- `README.md` census block and pass history updated (Pass 11).
- Achievement IDs used (events, not URLs): `ACH_PEBBLES_JURY_SPECIAL_MENTION_2024` (Pebbles page + VisualcontainerTV PDF + poster + film card = **one** achievement), `ACH_PVTV_FRINGE_FLICKS_2025-04-04` (Wayback page + Patreon + Eventbrite = **one** screening), `ACH_LAKE_IVAN_REVIEW_2025`, `ACH_BMC_RADIO_ARTIST_2021`, `ACH_FILM_IMDB_CREDITS`, `ACH_COMP_*` per compilation.

## Not done / carry-forward

- Wayback CDX sweeps for itch.io, filmfreeway, github, stage32, wfcn, linktr.ee (IA offline at attempt time).
- Fetch `mycommunitycinema.org.uk` PVTV pages to add a second live independent record for the Liverpool screening.
- Open the 4 remaining IMDb title credit pages.
- Manual/browser: Bluesky search, RYM artist page, Reddit ManicMolotov profile and full ujng7o thread, Typescript magazine archive.
