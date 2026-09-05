# 📰 PHASE THREE — Editorial, Literary & Text-Led Publishing Census

**Scope:** literary/cultural magazines, online journals, anthologies, zines, editorial & criticism sites, bylines/contributor pages, podcast show-notes, blogs, newsletters — i.e. *published-writing ecosystems only*. This is **not** a repeat of Phase One (broad audit) or Phase Two (general long-tail).
**Exact-string rule:** only `"Zazie Productions"` and `"Zazie Kanwar-Torge"` count. Handles/slugs without the space (`zazieproductions`) are Leads, never rows.
**Dedup baseline:** every URL below was checked against the 576 normalised URLs already held in the earlier-phase catalogue (PR #2 `data/master/master_index.csv` + `registry/seed/`). Rows marked **NEW** are not in that baseline. Rows marked *(baseline)* are already catalogued and are shown only for context / because a *new sibling page* on the same host was found.
**Census window:** 2026-09-05 (UTC). Engines that worked from the sandbox: `web_search`, Yahoo (Bing index) SERP, Brave SERP, direct site fetches. Google/Bing direct SERPs were bot-walled — see §E.

Legend (from root `README.md`): 🔴 press/editorial · 🌸 film · 🟣 recognition · 🔵 profile · 🟠 music · 🩵 data · 🟢 social · 📼 mirror · 🖤 spam — Status ✅ live / 🟡 partial / ❌ broken / ⬜ unchecked — Priority 🥇A / 🥈B / 🥉C / 🔎Lead.

---

## A. NEW literary / editorial places (exact string verified on page)

| URL | MEDIA | PRIORITY | STATUS | NAME | EVIDENCE | FOUND ON | CONTEXT |
|---|---|---|---|---|---|---|---|
| https://bipolarpoetry.com/the-bell-of-the-hollow-luxuries/ | 🔴 | 🥇A | ✅ | Prod | Poem page, byline **"Zazie Productions"**, dated 8 February 2026. Opens "I am loved in a thousand / bright, well-meaning gestures." | bipolarpoetry.com internal search (`?s=Hollow+Luxuries`) · 2026-09-05. *Not* indexed by Bing/Yahoo; site's author-name search returns nothing (body-text only). | Poem "The Bell of the Hollow Luxuries" — Bipolar Poetry (Sydney, ed. Joseph Dunn; listed on pw.org) |
| https://100subtextsmagazine.blogspot.com/2025/03/issue-31feature.html | 🔴 | 🥇A | ✅ | Prod | Editor's feature post (John Hopper), 1 Mar 2025: "In this brand new issue of the literary magazine 100subtexts, we feature the writer, composer, filmmaker **Zazie Productions**, who brings us a stunning poem: Anchor and Ascend." Image file `5 zazie productions.jpg`. | Blogger RSS feed `feeds/posts/default?q=Zazie` · 2026-09-05 (HTML shell renders empty for non-JS fetch; feed body is the evidence) | 100subtexts Magazine Issue 31 (UK) — poem "Anchor and Ascend" |
| https://www.lulu.com/shop/som/thresholds-a-micro-fiction-anthology/paperback/product-nvmmywe.html | 🔴 🟣 | 🥇A | ✅ | Kanwar | Publisher product page, "Contributors: … Zach Keali'i Murphy, **Zazie Kanwar-Torge**". Publication date Sep 3 2025, 75 pp, edited by SOM (Fresh Words: An International Literary Magazine). | Yahoo `lulu.com SOM "THRESHOLDS" micro fiction anthology` · 2026-09-05 | THRESHOLDS: A Micro Fiction Anthology (35 writers, 100–200-word micro-fictions) |
| https://www.poetryformentalhealth.org/anxiety-and-depression | 🔴 🟣 | 🥇A | ✅ | Kanwar | Book page, CONTENTS list: "Poetry by Laura / **Poetry by Zazie Kanwar-Torge** / Poetry by Tina Carey…". 7th title in the Poetry for Mental Health series, compiled by Robin Barratt; ISBN 9798284477878, 280 pp, 114 contributors; Amazon ASIN B0FCXQ5K2S (paperback) / B0FCSBRDSM (Kindle). | Brave `"Zazie Kanwar-Torge"` (result #3 of chunk 3) · 2026-09-05. *Not* in Yahoo index. | Anthology *Anxiety & Depression* (Poetry for Mental Health, UK) |
| https://ogre.red/issues/2025-12/2025-12-introduction/ | 🔴 | 🥈B | ✅ | Both | Editor's note for Red Ogre Review's 33rd issue: "Music by: **Zazie Kanwar-Torge** \| **Zazie Productions**" ("Sul Ponticello Dreaming"). | Direct fetch after web_search `"Zazie Kanwar-Torge" "Red Ogre Review"` · 2026-09-05 | Red Ogre Review Dec 2025 issue (ed. Matthew Bullen) — companion to the *(baseline)* contributor page `ogre.red/issues/2025-12/2025-12-kanwar-torge-zazie/` |
| https://ogre.red/issues/2024-10/2024-10-introduction/ | 🔴 | 🥉C | ✅ | Both | Site-wide contributor sidebar/index lists the Dec 2025 Kanwar-Torge entry. Body text of the Oct 2024 issue itself does not mention Zazie. | web_search · 2026-09-05 | Red Ogre Review navigation index (low value — same link repeats on every issue page; Feb 2025 issue confirmed no mention) |
| https://metapsychosis.com/creative-agents/zazie-productions/ | 🔴 | 🥈B | ✅ | Prod | "Creative Agents" contributor profile on *Metapsychosis* (Cosmos Co-op literary/arts journal): "**Zazie Productions**, Asheville's clandestine autistic polymath… Commissioned by Black Mountain College at just 14…". WP-API `post_type=creative-agents` id 14391, published 2025-02-23. | Yahoo `"Zazie Productions" interview` p1 · 2026-09-05 | Journal contributor page (no linked article found yet — `wp-json/wp/v2/posts?search=Zazie Productions` returns []) |
| https://codex.churchofmalware.org/editions/ed001/ | 🔴 | 🥈B | ✅ | Prod | Edition gallery: "⛧ featured researchers ⛧ … **ZAZIE PRODUCTIONS** — Poison, The Well, Adversarial Audio, and Machine Learning". Print editions via Mixam (Community Codex 001; DEFCON 34 Special Edition). | Direct fetch from *(baseline)* researcher page · 2026-09-05 | Church of Malware *Community Codex* Edition I — Summer 2026 (11-page PDF paper `researcher_zazie.pdf`) |
| https://thewrong.org/2025-26 | 🟣 🔴 | 🥈B | ✅ | Prod | Official 7th-edition catalogue page, "2o25/26 artists: … Plamen Yordanov, Zhongyao Wang, **Zazie Productions**, Garrett Lynch IRL…" (2,361 artists, 176 curators, Nov 1 2025 – Mar 31 2026). | web_search `"Zazie Productions" "Wrong Biennale"` · 2026-09-05 | The Wrong Biennale 2025/26 — matches the 2026 Register's "Wrong Biennale catalogue" entry; pavilion page still unidentified (Lead) |
| https://www.listennotes.com/podcasts/black-mountain/bmc-radio-art-zazie-atrX8jsp-6h/ | 🔴 🎙 | 🥈B | ✅ | Kanwar | Show-notes mirror of BMC Radio Art episode (2021-12-15): "**Zazie Kanwar-Torge** (they/them) is a composer and multi-instrumentalist living in Asheville…". | Yahoo `"Zazie Kanwar-Torge"` p2 · 2026-09-05 | Black Mountain College Museum + Arts Center podcast — "Cheaper Impressions" commission (podcast notes = text-led) |
| https://www.listennotes.com/podcasts/black-mountain/episode-7-ruth-asawas-jCOn1up_zYy/ | 🔴 🎙 | 🥉C | ✅ | Kanwar | Episode 7 notes (2024-06-07) carry the same Zazie bio paragraph ("…Zazie pays tribute to 'Cheap Imitation'… **Zazie Kanwar-Torge** (they/them)…"). | Brave `"Zazie Kanwar-Torge"` chunk 3 · 2026-09-05 | BMC podcast feed — bio re-used in a later episode's notes |

### A2. Self-published poetry platform pages (text-led, but *not* editorially selected — count separately)

| URL | MEDIA | PRIORITY | STATUS | NAME | EVIDENCE | FOUND ON | CONTEXT |
|---|---|---|---|---|---|---|---|
| https://allpoetry.com/Zazie_Productions | 🔵 | 🥉C | ✅ | Prod | *(baseline)* poet profile "Zazie Productions, Poet at AllPoetry", user_id 6116816, **8 poems**. Listed here because the poem permalinks below are new. | Yahoo `"Zazie Productions" poetry` p1 · 2026-09-05 | profile |
| https://allpoetry.com/poem/18318896-Entry-00-%CE%B4-the-Spalled-Vestibule-or-Where-the-Bylaws-Go-to-Rot-by-Zazie-Productions | 🔴 | 🥉C | ✅ | Prod | Prose-poem "Entry 00-δ. // the Spalled Vestibule, or: Where the Bylaws Go to Rot by Zazie Productions", © Mar '25. | allpoetry profile crawl · 2026-09-05 | NEW poem permalink |
| https://allpoetry.com/poem/18284408-3-Untitled-Micro-Haikus-by-Zazie-Productions | 🔴 | 🥉C | ✅ | Prod | "3 Untitled Micro-Haikus by Zazie Productions", © Mar '25 · **picked Oct '25** (site editorial pick). | allpoetry profile crawl · 2026-09-05 | NEW poem permalink |
| https://allpoetry.com/poem/17245942-By-Daybreak-s-Dawn-by-Zazie-Productions | 🔴 | 🥉C | ✅ | Prod | "By Daybreak's Dawn by Zazie Productions", © Jun '23. | allpoetry profile crawl · 2026-09-05 | NEW poem permalink |
| https://allpoetry.com/poem/17245444-The-Microbe--by-Zazie-Productions | 🔴 | 🥉C | ✅ | Prod | "The Microbe by Zazie Productions", © Jun '23. | Yahoo `"Zazie Productions" poetry` p1 · 2026-09-05 | NEW poem permalink |
| https://allpoetry.com/poem/17227437-Special-Edition--by-Zazie-Productions | 🔴 | 🥉C | ⬜ | Prod | Yahoo title "Special Edition by Zazie Productions". Yahoo also served the *same* id 17227437 for "The Geography of Absence" — one of the two titles is a stale index entry; open and confirm before promoting. | Yahoo `"Zazie Productions" poetry` p1–2 · 2026-09-05 | poem permalink (id collision — verify) |

---

## B. Partial / handle-only editorial pages (🟡 — do **not** count toward exact-string totals)

| URL | MEDIA | PRIORITY | STATUS | NAME | EVIDENCE | FOUND ON | CONTEXT |
|---|---|---|---|---|---|---|---|
| https://www.instagram.com/p/DGp310vszdo/ | 🟢 🔴 | 🥈B | 🟡 | Prod | Yahoo snippet of @100subtextsmagazine post (1 Mar 2025): "we feature the writer, composer, filmmaker **Zazie Productions**, who brings us a stunning poem: Anchor and Ascend. Issue 31". Direct fetch → HTTP 403 (login wall). | Yahoo `"Zazie Productions" poetry` p1 · 2026-09-05 | Social announcement of the Issue 31 feature (blog post in §A is the citable original) |
| https://thesqueakywheel.org/dissociation-support-group-to-hold-meeting-attendees-plan-to-show-up-in-spirit/ | 🔴 | 🔎Lead | 🟡 | — | Satire article, 29 Oct 2024. Byline is the handle **"zazieproductions"** (no space) — exact string absent. Author archive `/author/zazieproductions/` is *(baseline)*. | Direct fetch · 2026-09-05 | The Squeaky Wheel (satire site) — matches LinkedIn "Publications" entry |
| https://thesqueakywheel.org/doctor-asks-man-who-has-been-in-coma-for-45-years-if-he-ever-considered-it-might-just-be-anxiety/ | 🔴 | 🔎Lead | 🟡 | — | Second satire piece, 14 Mar 2024, same handle byline. | Author archive crawl · 2026-09-05 | The Squeaky Wheel |
| http://www.lynnesachs.com/category/sections/page/6/ | 🌸 🔴 | 🥉C | 🟡 | Kanwar | Brave snippet: participant list "…Andrew Reichel **Zazie Kanwar-Torge** ALina Taalman…" under the *Films for Freedom* post. URL is a paginated archive (content shifts); permalink of the post not yet captured (site search is reCAPTCHA-gated). | Brave `"Zazie Kanwar-Torge"` chunk 3 · 2026-09-05 | Lynne Sachs' blog re-post of the Film-Makers' Coop × Canyon Cinema "Films for Freedom" line-up *(baseline: film-makerscoop.com + connects.canyoncinema.com + vimeo)* |
| https://mastodon.bida.im/@iyezine/113995823411563269 | 🔴 📼 | 🥉C | ✅ | Prod | *(baseline)* "#radariye Zazie Productions - CAN'T GET MY EYES OFF YOU (123)… multi-instrumentalist, savant, and whimsical outsider musician" (13 Feb 2025, auto-posted via dlvr.it). | re-verified · 2026-09-05 | In Your Eyes Ezine (IT) — the **iyezine.com article itself was not found**: site search for "zazie"/"eyes off you" returns no hit, `/tag/zazie-productions/` 404, Yahoo `iyezine "Zazie Productions"` = 0. Keep as Lead. |

---

## C. Leads — publications named in the 2026 Register / bios / LinkedIn, **no exact-name page found yet**

| Target | What was checked (2026-09-05) | Next action |
|---|---|---|
| **Mailmodo — "The State of Onboarding 2025"** (LinkedIn: 21 Oct 2025) | https://www.mailmodo.com/ebook/state-of-onboarding/2025-o/ renders (80+ SaaS companies, expert corners Ramli John / Jon Farrah) — no Zazie string in HTML; Yahoo `mailmodo "Kanwar-Torge"` = 0. | Download the report PDF (gated) and grep contributor list. |
| **100subtexts Issue 31 PDF** | https://payhip.com/b/XVlRA product page: "69 pieces of work by 27 contemporary writers and poets", £0.99 — contributor names not listed. | Purchase/obtain PDF; cite page number of "Anchor and Ascend". |
| **THRESHOLDS — Goodreads / Amazon** | https://www.goodreads.com/book/show/241165826-thresholds shows Scott C. Holstad as author, no contributor list. hankrules2011.com post (5 Sep 2025) cites ISBN 9798265953896. | Amazon page for ISBN 9798265953896 may include "Look inside" TOC. |
| **Anxiety & Depression — Amazon B0FCXQ5K2S** | Not fetched (Amazon blocks). Publisher page in §A is the primary citation. | Optional: Amazon "Look inside" for page number. |
| **Red Ogre Review anthology *Bite More Smash More*** (Amazon B0G4LHKM2M, 30 Nov 2025) | https://ogre.red/press/anthologies/2025-anthology/ — covers issues **Oct 2024 → Sep 2025**. Zazie's contribution is the **Dec 2025** issue, so it is most likely **not** in this volume. | Watch for the 2026 anthology (Oct 2025 → Sep 2026 issues). |
| **Fresh Words / SOM magazine issues** | https://sites.google.com/view/freshwordsmagazine/issues lists issue PDFs (Drive/FlipHTML5/Lulu) — no contributor names in HTML. | Grep Sept–Nov 2025 issue PDFs for a Zazie piece or the anthology announcement. |
| **In Your Eyes Ezine (iyezine.com)** | See §B row — only the Mastodon auto-post exists in the index. | Ask editors for the #radariye permalink; try `iyezine.com/?s=miscreant`. |
| **Metapsychosis article** | Contributor profile exists (§A) but no post links to it. | Check Cosmos Co-op newsletters / *Metapsychosis* issues Feb–Mar 2025. |
| **The Wrong Biennale pavilion page** | Artist list confirmed (§A); pavilion/curator not identified. | Grep each 2025/26 pavilion page on thewrong.org for "Zazie Productions". |
| **Lynne Sachs blog permalink** | See §B. | Find `lynnesachs.com/2025/11/…films-for-freedom…` permalink. |
| **Typescript Magazine · Album of The Year · Ghost Nun Records · Glacier FM · Asheville FM 103.3** (claimed on SoundBetter bio) | Yahoo `"Zazie Productions" typescript` → only GitHub/itch.io; web_search `"The Typescript" "Zazie Productions"` = 0. | Contact-based verification; no indexable page. |
| **"Subterranean Sound Index" / "Oblique Frequencies Review"** (pull-quotes on musicians.directory) | web_search for either publication name + Zazie returns only the musicians.directory bio itself. ⚠️ No evidence these outlets exist as publications. | Treat as unverifiable blurbs; do **not** log as press. |
| **Coin-Operated Press — *For the Sad Kids Zine*** | coinoperatedpress.com generic pages only; no Zazie string. | Ask press for issue PDF / contributor list. |
| **Dark Holme Publishing — *Dark Descent: Whispers From Beyond* ("Husk")** | darkholmepublishing.uk product page (ISBN 1068616407) has no contributor list; heyzine Vol 4 PDF (Sept 2024) not text-searchable. | Obtain TOC. |
| **Blastbones Zine Vol. II** (ed. Mateo Perez Lara, Bakersfield) | Eventbrite launch (Oct 23, Beyond Baroque, "20 contributors"); theindexbooks.com hosts Vol. 1 only. | Request Vol. II contributor list. |
| **Milkweed Poetry Journal** | Only instagram.com/milkweedpoetry (Hudson Valley workshop journal); Milkweed Editions is a different entity. | Check their IG for a Zazie post. |
| **Thorn In Your Side — *Barb* #3** | web_search `"Zazie" "Thorn In Your Side" Barb issue 3` = 0. | Ask zine. |
| **Posthuman Press · re:natura #06 · MEDIUM SONORUM (Bruckner Univ. Linz) · Beatformers doc · BetaList "Bario"** | web_search `"Zazie Productions" "Posthuman Press" OR "re:natura" OR "Medium Sonorum"` → only The Wrong Biennale hit. | Individual site searches next phase. |

---

## D. Incidental non-editorial finds (out of Phase-3 scope; logged so nobody re-discovers them)

All 🥉C / ✅ unless noted; none are in the baseline. Do **not** count toward editorial totals.

| URL | MEDIA | NAME | EVIDENCE (1 line) | FOUND ON |
|---|---|---|---|---|
| https://www.imdb.com/name/nm17333332/bio/ | 🔵 | Both | Bio: "Zazie Kanwar-Torge was raised in North Carolina… Performing and releasing work under Zazie Productions". (`/name/nm17333332/` is baseline.) | Yahoo `"Zazie Kanwar-Torge"` p1 |
| https://artfacts.net/artist/zazie-kanwar-torge | 🔵 🟣 | Kanwar | ArtFacts artist entry; exhibition Muslab 2025, Quito, 24–28 Nov 2025. | Yahoo p3 |
| https://www.creativemornings.com/individuals/zaziekanwartorge | 🔵 | Kanwar | Member profile. | Yahoo p2 |
| https://www.upwork.com/freelancers/~010411a0e4129d9d14 | 🔵 | Kanwar | Freelancer profile. | Yahoo p2 |
| https://www.twine.net/ZazieProductions | 🔵 | Prod | Freelancer profile. | web_search |
| https://www.behance.net/zaziediya | 🔵 | Prod | *(baseline)* "Zazie Productions – Evil Overlord in NC" — projects *Ouroborean Sunmouth*, *Paranoid Heraldry of the Pink Sun*, *Glossolalia Engine / 23-Vector Gospel*. | web_search |
| https://www.bizapedia.com/nc/zazie-productions-llc.html | 🩵 | Both | NC LLC record, file 3188652, registered agent "Zazie Diya Kanwar-Torge". | Yahoo p4 |
| https://voterrecords.com/voter/127892431/zazie-kanwar-torge | 🩵 | Kanwar | Public voter record (PII — record existence only; do not re-publish details). | Yahoo p4 |
| https://www.youtube.com/watch?v=XF0nks0Nnak · https://www.youtube.com/watch?v=c9ZoZhSci2Q ("Organized Chaos") · https://www.youtube.com/watch?v=ld4BzJkKMi8 ("Spectral Ode to Synesthesia") | 📼 🟠 | Kanwar | DistroKid auto-uploads crediting Zazie Kanwar-Torge. | Yahoo p4 |
| https://www.instagram.com/p/DQWpMP8kYmJ/ | 🟢 | Kanwar | IG post surfaced for the exact name (403 on fetch — 🟡). | Yahoo p1 |
| https://open.spotify.com/playlist/5hy3SZN9SNkgbHgWx4UwSO | 🟠 | Prod | "Sound Art / Experimental Poetry / Musique Concrète" playlist by Zazie Productions (135 items). | Yahoo `"Zazie Productions" poetry` p1 |
| https://credits.muso.ai/profile/4010f3b7-9a87-4961-8dfd-917de0ba787e · https://www.songstats.com/artist/mljz9dxu/zazie-kanwar-torge | 🩵 🟠 | Both | *(baseline)* credit databases. | Brave chunk 0 |

---

## E. Method log — queries run, engines, dead ends (so Phase 4 doesn't repeat them)

**Engines usable from the sandbox:** `web_search`; Yahoo SERP `https://search.yahoo.com/search?p=<q>&n=40&b=<1|8|15|22|29>` (7 results/page); Brave SERP `https://search.brave.com/search?q=<q>&source=web` (4 chunks); direct site search/RSS/WP-JSON. **Unusable:** Google (bot wall after 1st chunk), Bing direct (returns unrelated Roblox junk), raw `curl` (no egress), Instagram pages (403), iyezine.com search (reCAPTCHA).

**Exact-string queries exhausted (all pages read):**
- Yahoo `"Zazie Kanwar-Torge"` p1–p4 (b=1,8,15,22) — p4 tail = bizapedia/voterrecords only.
- Yahoo `"Zazie Productions" poetry` p1–p3 — p3 degraded to non-matching noise (result set ends ≈14).
- Yahoo `"Zazie Productions" interview` p1–p2 — p2 = Zazie Beetz noise; p1 yielded metapsychosis (new), soundbetter/limitless/reverbnation/filmfreeway (baseline).
- Yahoo `"Zazie Productions" review album OR EP OR single` — noise only.
- Yahoo `"Zazie Kanwar-Torge" poetry OR anthology OR interview` — noise only (Bing drops the phrase when OR-ed).
- Brave `"Zazie Kanwar-Torge"` chunks 0–3 — complete; new: poetryformentalhealth.org, lynnesachs.com; rest baseline.
- web_search: `"Zazie Kanwar-Torge" poetry OR poem OR zine OR journal OR anthology`; `"Zazie Productions" review OR interview OR essay magazine`; `"Zazie Productions" substack` (none); `"Zazie Productions" blog review OR feature OR essay`; `"Zazie Kanwar-Torge" "Red Ogre Review"`; `"Zazie Productions" Mountain Xpress` (none); `iyezine.com "Zazie Productions"` (none); `"Zazie Productions" "Posthuman Press" OR "re:natura" OR "Wrong Biennale" OR "Medium Sonorum"`.

**Targeted checks with negative result:** Church of Malware article title "Poison in the Well" → resolves to the Codex paper (§A); Substack (none); Mountain Xpress (none); Typescript (none); 100subtexts blog search `?q=Zazie` (Blogger search UI empty — use feed); bipolarpoetry `?s=Zazie` / `?s=Productions` (none — body-text search only); metapsychosis posts search (none beyond profile); ogre.red Feb 2025 issue (no mention); Fresh Words issues page (no names).

**Totals for this phase (exact-string, non-mirror, non-profile):** §A = **11 new editorial/literary pages** (9 🔴 editorial + 2 podcast-notes) + **4 new poem permalinks** (§A2, self-published; count separately) · §B = 5 partial/handle rows · §C = 18 open leads · §D = 12 incidental out-of-scope rows.
