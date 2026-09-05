# 🖤 Low-Trust Register — Spam · Scraper · Syndication · SEO-Poisoning mentions of the exact strings

> **Evidence preservation & provenance only.** Every row documents that the exact public string `Zazie Productions`
> or `Zazie Kanwar-Torge` appeared (or appears) on a low-trust surface. **Nothing here is ever** credible editorial
> coverage, a verified career credit, a legitimate artist profile, a valid music release, an official business
> presence, a meaningful press mention, or a trustworthy source of biographical information.

**Pass date:** 2026-09-05 · **Queries:** 11 (all preserve one complete quoted exact target phrase — see `queries_run.csv`)
**Ledger:** 89 entries (`lowtrust_ledger.csv`) · **Master effect:** new category `Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust` carries **73 rows, all Tier D** (522 → 524 master rows).

## Counts by cluster

| Cluster | Ledger entries | In master (D) | Register-only | Notes |
|---|---|---|---|---|
| BMC-DOORWAY | 15 | 15 | 0 | 🚪 Hacked-site doorway injection — the BMC/IRLAM template cluster |
| SPAM-SHOP | 1 | 1 | 0 | 🛒 Spam-shop product page |
| MISATTRIB-FLAG | 2 | 2 | 0 | ⚠️ Misattributed dump entries (NOT occurrences of the target) |
| YT-MIRROR | 38 | 38 | 0 | 📼 The `UX2kv3G89Jw` YouTube-mirror cluster — auto-scraped video syndication |
| PIRATE-SCRAPE | 1 | 1 | 0 | 🏴 Pirate search index |
| AUTOGEN-DATA | 9 | 7 | 2 | 🤖 Auto-generated metadata clones & malformed-directory rows |
| PASTE-REPUB | 3 | 3 | 0 | 📄 Pastebin republications & fabricated-attribution essays |
| RSS-SYNDICATION | 3 | 3 | 0 | 📡 RSS / press-release-feed republication |
| LEGACY-MIRROR | 6 | 2 | 4 | 🪞 Mirrors of originals (dead & surviving) |
| BOT-UGC | 1 | 1 | 0 | 🤖 Bot-like UGC |
| REVIEW-KEPT | 7 | 0 | 7 | 🧐 Reviewed & deliberately NOT treated as low-trust (kept in place) |
| SEARCH-REDIRECT | 2 | 0 | 2 | ↪️ Redirect wrappers & SERP artifacts |
| LEADS-UNRESOLVED | 1 | 0 | 1 | 🔎 Leads (never counted) |
| **TOTAL** | **89** | **73** | **16** | |

---

## 🚪 Hacked-site doorway injection — the BMC/IRLAM template cluster

Fifteen unrelated, mostly compromised or spam-run hosts (`.sk`, `.kr`, `.pe`, `.fr`, `.cz`, an NGO, a bank credit-union …) all serving the SAME URL template (a sixteenth entry in this family — the `wnloveet.click` product page — is filed separately as SPAM-SHOP): a random short path + the keyword-salad slug `black-mountain-college-ira-and-ruth-levinson-museum` / `ira-and-ruth-levinson-art-museum-north-carolina`. The dump captured one of these pages under the spoofed SERP title `Guru Meditation Error - Zazie Productions - 单曲 - 网…` — i.e. the injected title string rides *real* Zazie track metadata (a "单曲/single" page style scraped from a Chinese music service, title taken from the official Bandcamp track “Guru Meditation Error”). Classic **SEO poisoning / doorway page**: parasitic pages manufactured to farm an indexed query, containing the exact string `Zazie Productions` as injected metadata. The occurrence was real while the pages lived; it proves nothing about the artist.

**Status at pass time.** Do NOT visit (safety policy: compromised/malware-adjacent hosts). 2026-09-05: current general search indexes return only the legitimate blackmountaincollege.org/museonline.org pages for the slug+name query — the cluster is effectively de-listed. Internet Archive CDX probes for sampled doorway URLs returned **zero captures**, confirming these surfaces were transient and unarchived. Provenance rests on the dump + seed record itself.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-001 | DOORWAY-INJECT | <http://hiontech.kr/data/persuasive-speech/black-mountain-college-ira-and-ruth-levinson-m…> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-002 | DOORWAY-INJECT | <http://www.bytstav.sk/gDrA/ira-and-ruth-levinson-art-museum-north-carolina> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-003 | DOORWAY-INJECT | <https://archivio.lavocedinovara.com/KmDEB/black-mountain-college-ira-and-ruth-levinson-m…> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-004 | DOORWAY-INJECT | <https://childrenofyemen.org/zvgw5/black-mountain-college-ira-and-ruth-levinson-museum> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-005 | DOORWAY-INJECT | <https://designbymm.cz/.modules/gbt72mhz/ira-and-ruth-levinson-art-museum-north-carolina> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-006 | DOORWAY-INJECT | <https://lcofcu.com/4o5ct9/archive.php?tag=black-mountain-college-ira-and-ruth-levinson-m…> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-007 | DOORWAY-INJECT | <https://maynenkhikobelco.com/ZVuos/black-mountain-college-ira-and-ruth-levinson-museum> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-008 | DOORWAY-INJECT | <https://patchworkers.info/ac-valhalla/black-mountain-college-ira-and-ruth-levinson-museu…> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-009 | DOORWAY-INJECT | <https://powerkabel.com.pe/love-quotes/black-mountain-college-ira-and-ruth-levinson-museu…> | Zazie Productions | not-probed-safety | NOT VISITED — counterfeit-shop style host (safety policy) |
| LT-010 | DOORWAY-INJECT | <https://shoshanagarfield.com/bidirectional-lstm/black-mountain-college-ira-and-ruth-levi…> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-011 | DOORWAY-INJECT | <https://slatersgarage.com/PxyL/black-mountain-college-ira-and-ruth-levinson-museum> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-012 | DOORWAY-INJECT | <https://smartpersonsguide.com/MNNiI/black-mountain-college-ira-and-ruth-levinson-museum> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-013 | DOORWAY-INJECT | <https://vidmak.com/fs0vz3/ira-and-ruth-levinson-art-museum-north-carolina> | Zazie Productions | not-probed-safety | NOT VISITED — known malware-distribution host (safety policy) |
| LT-014 | DOORWAY-INJECT | <https://www.juetao.org/yfc/san-bernardino-county-sheriff-jobs> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |
| LT-015 | DOORWAY-INJECT | <https://www.sarlmca.fr/x83v4/ira-and-ruth-levinson-art-museum-north-carolina> | Zazie Productions | not-probed-safety | NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: n… |

## 🛒 Spam-shop product page

`wnloveet.click/product_details/105751966.html` — suspicious `.click` counterfeit/malware-adjacent shop product page found in the same dump block, riding scraped keyword text.

**Status at pass time.** Not visited. Documented from the dump/seed only.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-016 | SPAM-SHOP | <https://wnloveet.click/product_details/105751966.html> | Zazie Productions | unverified | not visited (suspicious .click domain, probable malware/counterfeit shop) |

## ⚠️ Misattributed dump entries (NOT occurrences of the target)

The dump's "spam sites" block also carried `agencesartistiques.com/fiche-artiste/739100-elsa-levy` (a French talent-booking page for an unrelated person, Elsa Levy) and `backstage.com/u/audreyjarnagin` (unrelated casting profile). These are **not** occurrences of "Zazie Productions" at all — they appear to be contamination of the *dump itself* (the researcher's tab/browser mixed them in). They are preserved here so nobody re-imports them as evidence of anything.

**Status at pass time.** No exact-name occurrence established → never countable under the two-name rule, under any category.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-017 | MISATTRIB-FLAG | <https://www.agencesartistiques.com/fiche-artiste/739100-elsa-levy.html?lng=en> | Zazie Productions | unverified | not visited |
| LT-018 | MISATTRIB-FLAG | <https://www.backstage.com/u/audreyjarnagin/> | Zazie Productions | unverified | not visited |

## 📼 The `UX2kv3G89Jw` YouTube-mirror cluster — auto-scraped video syndication

One short film (`Phantom Requiem`, YouTube id `UX2kv3G89Jw`, channel name `Zazie Productions`) seeded **38** third-party surfaces: benign player tools (deturl, listenonrepeat, youtuberepeater, viewsync, video.link, yewtu.be…), profile mirrors (yt.nimlinks.com/@zazieproductions), and — notably — **embed paths injected into legitimate third-party sites** (a Polish news portal `gazetaolsztynska.pl`, `stb.hu`, `hribi.net`, `newtv.co.th`, `topsheetmusic.eu`, `musiclessons.com`, `tvonlayn.ru`, `canal50.com`, `polsy.org.uk`), plus typosquat/scam-adjacent hosts (`youtubu.tv`, `clipzui.fun`, `heartvod.com`, `lu.etvplayvideos.com`, `nsfwyoutube.com`). On these pages the exact string appears **only via scraped video metadata** (embedded title/channel), never as authored content — the canonical "unexplained text-injection / syndication" pattern.

**Status at pass time.** Cluster sampled 2026-09-05 (4 of 38 read + 2 archive checks): `deturl` LIVE with the string visible via scraped metadata; `topsheetmusic.eu` LIVE as a bare injected embed (string only inside the iframe title); `gazetaolsztynska.pl` 404 (site cleaned); `clipzag` 500; `listenonrepeat` bot-blocked (not bypassed). IA CDX: mirrors were never archived. Remaining 32+ rows left ⬜ unverified — do not bulk-visit.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-019 | INJECTED-EMBED | <https://canal50.com/player-2020.asp?video=UX2kv3G89Jw&letra=4280&version=movil&autoplay=…> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-020 | TOOL-MIRROR | <https://clipzag.com/watch?v=UX2kv3G89Jw> | Zazie Productions | broken | HTTP 500 2026-09-05 |
| LT-021 | UNKNOWN-MIRROR | <https://culturevein.com/videos/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-022 | TOOL-MIRROR | <https://deturl.com/play.php?v=UX2kv3G89Jw> | Zazie Productions | verified | live 2026-09-05; scraped YouTube metadata shows "Zazie Productions" channel name |
| LT-023 | TOOL-MIRROR | <https://fooyoh.com/nowwatch/watch/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-024 | INJECTED-EMBED | <https://gazetaolsztynska.pl/gminaelk/tv/video/youtube/UX2kv3G89Jw> | Zazie Productions | broken | HTTP 404 page 2026-09-05 |
| LT-025 | SUSPICIOUS-MIRROR | <https://heartvod.com/play=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-026 | TOOL-MIRROR | <https://listenonrepeat.com/watch/?v=UX2kv3G89Jw> | Zazie Productions | unverified | fetch blocked 2026-09-05 (anti-bot) |
| LT-027 | SUSPICIOUS-MIRROR | <https://lu.etvplayvideos.com/UX2kv3G89Jw/v> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-028 | SUSPICIOUS-MIRROR | <https://lu.etvplayvideos.com/UX2kv3G89Jw/video-not-available> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-029 | SUSPICIOUS-MIRROR | <https://lu.etvplayvideos.com/UX2kv3G89Jw/w> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-030 | TOOL-MIRROR | <https://pakvim.net/watch/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-031 | INJECTED-EMBED | <https://polsy.org.uk/play/yt/?vurl=https://www.youtube.com/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-032 | TOOL-MIRROR | <https://salda.ws/video.php?id=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-033 | TOOL-MIRROR | <https://socialcounts.org/youtube-video-live-view-count/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-034 | UNKNOWN-MIRROR | <https://thewikihow.com/video_UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-035 | TOOL-MIRROR | <https://video.link/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-036 | TOOL-MIRROR | <https://viewsync-2.appspot.com/player.html?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-037 | TOOL-MIRROR | <https://viewsync.net/watch?v=UX2kv3G89Jw&t=0&mode=solo&autoplay=false> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-038 | SUSPICIOUS-MIRROR | <https://www.clipzui.fun/video/64f3a4n3t2j5x3y3c4o553.html> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-039 | INJECTED-EMBED | <https://www.hribi.net/video_youtube/startup-summit%20/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-040 | INJECTED-EMBED | <https://www.hribi.net/video_youtube/watch/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-041 | INJECTED-EMBED | <https://www.musiclessons.com/youtube/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-042 | INJECTED-EMBED | <https://www.newtv.co.th/demo/web/video.php?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-043 | SUSPICIOUS-MIRROR | <https://www.nsfwyoutube.com/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-044 | INJECTED-EMBED | <https://www.stb.hu/youtube/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-045 | INJECTED-EMBED | <https://www.topsheetmusic.eu/sysmusic/templates/youtube.php?v=UX2kv3G89Jw> | Zazie Productions | verified-partial | live 2026-09-05; bare player embed; exact string only in iframe video title |
| LT-046 | INJECTED-EMBED | <https://www.tvonlayn.ru/video/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-047 | TOOL-MIRROR | <https://www.vtomb.com/?watch=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-048 | TOOL-MIRROR | <https://www.vtomb.com/video/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-049 | EMBED-CANONICAL | <https://www.youtube-nocookie.com/embed/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-050 | TOOL-MIRROR | <https://www.youtuberepeater.com/watch?v=UX2kv3G89Jw#gsc.tab=0> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-051 | TOOL-MIRROR | <https://www.ytrepeat.com/watch/?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-052 | TOOL-MIRROR | <https://yewtu.be/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-053 | TOOL-MIRROR | <https://youplay.nimtools.com/watch/?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-054 | TYPOSQUAT-MIRROR | <https://youtubu.tv/watch?v=UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-055 | TOOL-PROFILE-MIRROR | <https://yt.nimlinks.com/@zazieproductions> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |
| LT-056 | TOOL-PROFILE-MIRROR | <https://yt.nimlinks.com/UX2kv3G89Jw> | Zazie Productions | unverified | not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only) |

## 🏴 Pirate search index

`box.hitplayer.ru/?s=zazie+productions` — HotPlayer "скачать или слушать онлайн" results page, 186 auto-scraped tracks under the exact-string page title, interleaved with French-singer "Zazie" noise (the exclusion trap made manifest). A live 2026-09-05 read confirms the page renders the exact string.

**Status at pass time.** verified live; count = zero; useful only as proof the name is being harvested into pirate indexes.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-057 | PIRATE-SCRAPE | <https://box.hitplayer.ru/?s=zazie> | Zazie Productions | verified | live 2026-09-05; title "Zazie Productions — скачать или слушать онлайн", 186 scraped tracks mixed with French-singer Zazie noise |

## 🤖 Auto-generated metadata clones & malformed-directory rows

Machine-written artist pages that mirror official streaming metadata with SEO boilerplate: viberate (auto "avant-garde jazz musician" Q&A — wrong genre, "email us to update your bio"), chosic, muso credits, songdata (the *record itself* was a search-query URL), thirdeyemusic (`?name=…&dir=tracks` directory listing), breakinghits (pay-to-play invite wall), boomplay lyrics page (`Goodnight, Farewell lyrics by Zazie Productions … download … on Boomplay`).

**Status at pass time.** viberate + breakinghits verified live 2026-09-05 (string visible in public text; reCAPTCHA on breakinghits left unsolved); songdata + thirdeyemusic now unreachable (broken); chosic blocked; muso not probed; boomplay lyrics search-index verified.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-058 | AUTOGEN-METADATA | <https://credits.muso.ai/profile/4010f3b7-9a87-4961-8dfd-917de0ba787e> | Zazie Productions | unverified | not probed this pass |
| LT-059 | AUTOGEN-SEARCHURL | <https://songdata.io/search?query=Zazie+Productions+> | Zazie Productions | broken | fetch failed 2026-09-05 (host unreachable) |
| LT-060 | AUTOGEN-SEARCHURL | <https://thirdeyemusic.co.uk/?name=Zazie_Productions&dir=tracks> | Zazie Productions | broken | fetch failed 2026-09-05 (host unreachable) |
| LT-061 | PLATFORM-REPUB | <https://www.boomplay.com/albums/66891844> | Zazie Productions | see note | "Miraculously Unhurt ... download for offline on Boomplay" auto album page; exact string in description JSON-LD (byArtist: Zazie Productions). |
| LT-062 | PLATFORM-REPUB | <https://www.boomplay.com/artists/46971970> | Zazie Productions | see note | Artist page auto-filled from distributor metadata. The lyrics subpage (66891844 album page + 151661449 lyrics) are the spammy surfaces: album page 668… |
| LT-063 | AUTOGEN-METADATA | <https://www.boomplay.com/lyrics/151661449> | Zazie Productions | search-index verified | search snippet 2026-09-05: "Goodnight, Farewell lyrics by Zazie Productions, listen and download latest songs of Zazie Productions with lyrics on Boom… |
| LT-064 | PAYTOPLAY-DIRECTORY | <https://www.breakinghits.app/zazieproductions/> | Zazie Productions | verified | live 2026-09-05; invite wall shows "Check out Zazie Productions on BREAKING HITS" (reCAPTCHA untouched) |
| LT-065 | AUTOGEN-METADATA | <https://www.chosic.com/artist/zazie-productions/4UOgvZEOo7xBhFBjJvlMm0/> | Zazie Productions | unverified | fetch failed 2026-09-05 (blocked) |
| LT-066 | AUTOGEN-METADATA | <https://www.viberate.com/artist/zazie-productions/> | Zazie Productions | verified | live 2026-09-05; exact string in title/body |

## 📄 Pastebin republications & fabricated-attribution essays

`anotepad.com/notes/5246g357` — LIVE paste-essay "The Eccentric Visionary: Zazie Productions and the Future of Digital Sound Design and Playlist Curation Algorithms", attributed to an invented **"Dr. Oliver K. Thornton, PhD, University of Cambridge"** and citing non-existent journals/theories (fabricated-credential text injection, AI-generated or persona-fiction — either way, void as biographical evidence). `justpaste.it/gepby` — anonymous 2025-02-12 PR paste of the "Greetings From Tinsel Time" write-up with unverifiable "critic" quotes. `mlx.su/paste` — dead (HTTP 410): a paste that once existed, now gone (transience evidence).

**Status at pass time.** anotepad + justpaste verified live with exact string; mlx.su recorded as deleted. **These contain the name, they do not describe the person.** All biographical/promotional claims on them are void.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-067 | FABRICATED-ATTRIB | <https://anotepad.com/notes/5246g357> | Zazie Productions | verified | page live 2026-09-05; title/body carry exact string |
| LT-068 | PASTE-REPUB | <https://justpaste.it/gepby> | Zazie Productions | verified | page live 2026-09-05; anonymous PR paste Feb 12 2025, 7 visits |
| LT-069 | PASTE-REPUB | <https://mlx.su/paste/view/26990c6b> | Zazie Productions | broken | HTTP 410 Gone 2026-09-05 — paste deleted upstream |

## 📡 RSS / press-release-feed republication

rsssearchhub (feed re-publisher; live host but its DB table crashed → "Unrecoverable error" on 2026-09-05 — the machinery of parasitic syndication, caught decaying), trendingbot (bot topic aggregator; host down), comunicati.musicalive.net (Italian promo site that auto-reposts PR feeds; the release page now redirects to the homepage — the republication is gone).

**Status at pass time.** All three recorded as broken/transient; the original PR (prfree @zazieproductions) remains the only authoritative copy.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-070 | PR-FEED-REPUB | <https://comunicati.musicalive.net/c/cant-get-my-eyes-off-you-123> | Zazie Productions | broken | URL now redirects to musicalive.net homepage 2026-09-05 |
| LT-071 | RSS-SYNDICATION | <https://www.rsssearchhub.com/feed/1185189bcc80cd02d670a3aaae58ebf3/city-portland-mercury> | Zazie Productions | broken | live host but page returns "Unrecoverable error" (crashed DB) 2026-09-05 |
| LT-072 | AUTO-AGGREGATOR | <https://www.trendingbot.org/topic/418115_klerksdorp> | Zazie Productions | broken | host unreachable 2026-09-05 |

## 🪞 Mirrors of originals (dead & surviving)

`r.darrennathanael.com` (old-reddit proxy, now HTTP 500) re-publishing a legitimate r/Album_Cover_Art thread; `rant.li` (defunct Medium mirror) re-publishing a self-published Medium essay — it had been **mis-tiered Press&A** in the dump, corrected to this register 2026-09-05.

**Status at pass time.** darrennathanael dead; rant.li not visited. Mirrors are visibility, never independent coverage.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-073 | LEGACY-MIRROR | <https://r.darrennathanael.com/r/Album_Cover_Art/comments/1i5wjf8/zazie_productions_to_ha…> | Zazie Productions | broken | HTTP 500 2026-09-05 |
| LT-074 | SYNDICATION-MIRROR | <https://rant.li/scienceinnovation/zazie-productions-researcher-sonic-engineer-and-theori…> | Zazie Productions | unverified | not visited this pass |
| LT-075 | SYNDICATION-MIRROR | <https://wiki2.org/en/List_of_experimental_musicians> | Zazie Productions | see note | Wikipedia "List of experimental musicians" scraper-mirror; 📼 class per docs/01. Original article not separately cataloged — mirror row remains the cen… |
| LT-076 | SYNDICATION-MIRROR | <https://wikigit.org/wiki/List_of_experimental_musicians> | Zazie Productions | see note | Same Wikipedia mirror family. |
| LT-077 | SYNDICATION-MIRROR | <https://wikimili.com/en/List_of_experimental_musicians> | Zazie Productions | see note | Same Wikipedia mirror family. |
| LT-078 | SYNDICATION-MIRROR | <https://www.wikiwand.com/en/articles/List_of_experimental_musicians> | Zazie Productions | see note | Styled reader mirror (semi-legit product); 📼 class. |

## 🤖 Bot-like UGC

`tiktok.com/@usery..y..yulles` — spammy-handle re-post of the Phantom Requiem video, listed in the dump under its literal "spam sites" heading.

**Status at pass time.** Not visited (platform bot-wall). Recorded from the dump only.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-079 | BOT-REPOST | <https://www.tiktok.com/@usery..y..yulles/video/7453287097533746450> | Zazie Productions | unverified | not visited this pass (platform bot-wall) |

## 🧐 Reviewed & deliberately NOT treated as low-trust (kept in place)

Surfaces this pass examined and left where they were: the net-art `codex.churchofmalware.org` page the seed had flagged as suspected spam (direct read shows a legitimate collective "researcher" codex listing **ZAZIE PRODUCTIONS** — the flag was wrong; the row was never in master and is now added under Community), getmusic.fm (legit bandcamp-code aggregator; exact string no longer visible in current render), stage32 media page (real platform), Wikipedia-family mirrors + Notion/perchance/senscritique stubs kept as 📼/community records per registry rules.

**Status at pass time.** One correction logged: seed false-positive on churchofmalware — preserved here so the judgment is not re-litigated.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-080 | KEPT-BORDERLINE | <https://app.notion.com/p/18c89e259c3c813baf39c100d3f2fe69?pvs=21> | Zazie Productions | see note | Notion publish page; likely artist-self-published (In-Your-Eyes e-zine family). Not parasitic; unverified. |
| LT-081 | KEPT-BORDERLINE | <https://app.notion.com/p/In-Your-Eyes-E-Zine-19989e259c3c8057bf81d66c6ab9903c?pvs=21> | Zazie Productions | see note | Artist e-zine Notion publication — self-published, kept out of low-trust. |
| LT-082 | REVIEW-KEPT | <https://codex.churchofmalware.org/researchers/ed001/zazie/> | Zazie Productions | verified | live 2026-09-05; "ZAZIE PRODUCTIONS · Poison, The Well, Adversarial Audio, and Machine Learning · Edition I — Summer 2026" |
| LT-083 | KEPT-BORDERLINE | <https://getmusic.fm/r/various-artists-moon-musiq-untitled> | Zazie Productions | see note | Legit bandcamp-code aggregator; kept in Streaming & Music Platforms, recorded here as borderline auto-replica. |
| LT-084 | KEPT-BORDERLINE | <https://perchance.org/zazieproductions> | Zazie Productions | see note | User-generated perchance page; low effort but appears fan/self-made, not injected. |
| LT-085 | KEPT-BORDERLINE | <https://www.senscritique.com/contact/Zazie_Productions/7375565> | Zazie Productions | see note | Autopilot/Allocine-family contact stub under underscore form; underscore variant alone does not count (README two-name rule); kept as visibility only. |
| LT-086 | KEPT-BORDERLINE | <https://www.stage32.com/media/3838211664293930413> | Zazie Productions | see note | Verified profile video page ("Score by Zazie Kanwar-Torge A.K.A Zazie..."); real professional platform — NOT low-trust despite prior category. |

## ↪️ Redirect wrappers & SERP artifacts

The Baidu `/link?url=` redirect (kept in Search-Engine Index — the name is *indexed*, there is no page), and the `#gsc.tab=0` Google-Custom-Search duplicate of the disconecta review URL (dedupe pending).

**Status at pass time.** Artifacts, not occurrences. Never counted.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-088 | SERP-ARTIFACT | <https://disconecta.com.br/resenhas/resenhas-de-discos/playlist-autoral-15-rock-jazz/#gsc…> | Zazie Productions | see note | #gsc.tab=0 Google-Custom-Search artifact; duplicate of the base URL. Treat as one record. |
| LT-089 | SEARCH-REDIRECT | <https://www.baidu.com/link?url=lGOPTjwdo-SJgH88b8O6BfcutJYDNcLfDDdoK_GDhgodoo9uajS_-T8r0…> | Zazie Productions | see note | Baidu /link?url= redirect wrapper (name indexed by Baidu). A redirect chain, not a page — kept out of all counts. |

## 🔎 Leads (never counted)

`paste2.org/zgjMW539` — a backlink/comment-spam URL list that the search index matched on `"Zazie Kanwar-Torge"` but which does NOT visibly display the phrase in the served snippet. Textbook of a spammer's link-dump referencing the name. **Lead only.**

**Status at pass time.** Deliberately not opened (suspicious payload listing). Revisit only via index snippet if ever.

| ID | Subtype | URL | Target | Live status | Evidence / disposition |
|---|---|---|---|---|---|
| LT-087 | SPAM-LIST-LEAD | <https://paste2.org/zgjMW539> | Zazie Kanwar-Torge | see note | paste2 list of backlink/comment-spam URLs matched "Zazie Kanwar-Torge" in the index but the phrase is NOT visible in the served snippet; suspicious li… |

---

## Reclassification log (pre-existing instances folded in)

These rows already existed in the repo and were **organized into this category** on 2026-09-05 — no row was deleted; every prior category is preserved in the `PriorMasterCategory` ledger column:

| From | Rows | Into cluster |
|---|---|---|
| `master_index.csv` · category **SEO Spam / Link Farm** (Tier D, 18 rows — old category retired; its name is now the new category) | 18 | BMC-DOORWAY 15 · SPAM-SHOP 1 · MISATTRIB-FLAG 2 |
| `master_index.csv` · **Video Mirror / Backlink Sites**, all Tier-D rows (the `UX2kv3G89Jw` cluster) | 38 | YT-MIRROR (the 2 non-D rows — stage32, archive.org — stay put) |
| `master_index.csv` · **Community, Wiki & Fan Indexes** — rsssearchhub, trendingbot, darrennathanael, tiktok @usery..y..yulles, anotepad, mlx.su | 6 | RSS-SYNDICATION 2 · LEGACY-MIRROR 1 · BOT-UGC 1 · PASTE-REPUB 2 |
| `master_index.csv` · **Profiles & Catalogs** — justpaste (→PASTE-REPUB), viberate + muso credits (→AUTOGEN-DATA), demoted B→D | 3 | + justpaste demoted |
| `master_index.csv` · **Streaming & Music Platforms** — hitplayer, songdata, chosic, breakinghits, thirdeyemusic, demoted B→D | 5 | PIRATE-SCRAPE 1 · AUTOGEN-DATA 4 |
| `master_index.csv` · **Press & Editorial** — rant.li (Medium mirror), comunicati.musicalive.net (PR-feed repost), demoted **A→D** | 2 | LEGACY-MIRROR · RSS-SYNDICATION |
| `registry/seed` spam cluster — **orphan never ingested into master**: `codex.churchofmalware.org` | +1 | REVIEW-KEPT → added to master as **Community C** (direct read: not spam) |
| New this pass — boomplay lyrics page (auto lyrics republication) | +1 | AUTOGEN-DATA |

**Net:** master 522 → **524** rows; Tier D 56 → **73**; category `SEO Spam / Link Farm` retired → `Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust`.
Two **A-tier demotions** were recorded per the standing rule that a spam-like republication "must never be counted as
credible editorial coverage": the rant.li and musicalive.net rows were PR re-copies, not press.

## Boundary & honesty

- No search proves completeness. Deleted pastes (mlx.su 410), cleaned injections (gazeta 404), dead mirrors (clipzag 500),
  crashed syndication infra (rsssearchhub), zero-capture archive checks and the de-listing of the doorway cluster all show
  how quickly these surfaces vanish — the register is a **point-in-time snapshot (2026-09-05)**.
- Hosts under the safety quarantine (vidmak, powerkabel, wnloveet, the hacked news-portal paths) were **documented without
  being visited**; their status is therefore ⬜ not-probed-safety and must never be "promoted" by a future agent clicking
  through to them.
- Inclusion here means: *this exact string appeared on a low-trust surface*. It says nothing true about the artist and
  nothing false either — it documents contamination so the census can prove it filtered contamination out.
