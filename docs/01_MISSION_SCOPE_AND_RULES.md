# 📘 01 — MISSION, SCOPE & RULES

> **This is the master brief.** If an agent asks *“what am I doing and how do I decide what counts?”,* point it here. Read this before any searching.

---

## 1. The one-line mission

> Build an **extensive, organized, color-coded directory of every public place** where the exact names **`Zazie Kanwar-Torge`** and/or **`Zazie Productions`** are **indexed or named** — searched across mainstream, meta, obscure, independent, regional, and niche engines — then **verify that each found link actually works** and carries exact-name evidence.

This is deliberately a **“find-it-anywhere” census**, not just a backlink report. “Backlink” in the repo name is shorthand for *any discoverable mention/embed/credit*, whether it links out or not.

---

## 2. The two targets (only these two count)

| Rank | Exact target string | Notes |
|---|---|---|
| 1 | **`Zazie Productions`** | The artist project / label name. (Beware unrelated firms using this string.) |
| 2 | **`Zazie Kanwar-Torge`** | The person's name (composer, scorer, filmmaker, multimedia artist). |

**Countable evidence must contain at least one of these two exact strings**, spaced, on the page or in the search-result snippet (per the repo's own “Strict Exact-Name” convention).

### Non-countable but still useful (record as 🔎 leads)
Handles, slugs, and URL-only variants — useful for discovery but **not counted** toward totals:

- `zazieproductions`, `zazie_productions`, `zazie-productions`, `@zazieproductions`, `@ZazieProd`
- `Zazie Kanwar-Torge` joined forms: `zazie-kanwar-torge`, `zaziekanwartorge`
- The real home URLs: `zazieproductions.com`, `horror.zazieproductions.com`, `linktr.ee/zazieproductions`
- Related author/creator handles and the curated press-hub on Linktree

---

## 3. What counts as a “place”

Include when a unique URL (or unique account/platform entity) publicly displays **or** is search-indexed with the exact name:

- 🔴 **Press / editorial** — features, reviews, interviews, roundups, quotes, press releases, magazines, blogs, podcasts written about it.
- 🌸 **Film / festivals / exhibitions** — IMDb/TheMovieDB credit pages, festival & award pages, gallery & museum exhibition pages, screening listings.
- 🟣 **Publications / recognition / academic** — awards, honor rolls, anthologies, contributed chapters, contest-finalist letters, security-credit pages, academic or research write-ups.
- 🔵 **Profiles & catalogs** — artist/creator/directory profiles on streaming platforms, portfolio hubs, industry directories, service marketplaces, analytics dashboards.
- 🟠 **Music & discography** — albums, singles, net-label & compilation credit rows, lyric pages, track/credit registries.
- 🩵 **Data-studies / analytics / tooling** — AI/Q&A pages about the artist, stats sites, research-style write-ups, community-built studies.
- 🟢 **Social & community / UGC** — native posts, community threads, fan quizzes/tier-lists, curated playlist credits, meme/blog mentions.
- 📼 **Mirrors & aggregators** — YouTube-repeater/mirror sites, wiki mirrors (Wikimili/Wikiwand/wiki2/wikigit), RSS scrape pages, video embedding layers. *Secondary, but still logged.*
- 🖤 **Spam / SEO parasite** — auto-scraped or spun keyword pages. *Log as a separate bucket and cross-check before counting; do not let them inflate “real places.”*

---

## 4. Exclusions (do NOT record)

- The **French singer “Zazie”** (huge noise source — must be filtered constantly).
- The **company “Zazie Films”** or any other business whose full string is not exactly one of the two targets.
- Other real people/companies coincidentally named “Zazie Productions”.
- Pages containing only a **near/spelling variant** of the name with no exact match.
- Mentions of the word “Zazie” alone (e.g., unrelated “Zazie” artists, pets, characters).
- Generic scraped/spam pages that merely auto-fill the name from a press release and add no real presence — keep them in the 🖤 bucket, flagged, never counted as editorial.
- Private/paywalled/print-only items **unless** an archived or index-snippet captures the exact name.

---

## 5. Evidence standard (three levels)

When you record a row, state the **verification language** honestly:

1. **✅ Direct page verified** — you opened the live URL and read the exact name in the page body.
2. **🟡 Search-index verified** — the result index *visibly preserves* the exact name (title/snippet), even if you could not fully render the page (JS-gated, region-locked, login-walled).
3. **⬜ Lead / unverified** — a plausible hit you could not confirm. Put it in the leads list; **never** count it toward verified totals.

**Rule:** a “hit” is only **counted** when it is level 1 or 2. Level 3 goes to the leads register.

---

## 6. Output conventions (always, everywhere)

- One row per **unique URL-level item** (or unique platform entity). Separate editions/syndications may be separate rows.
- Tag every row with: **media-type emoji**, **status emoji (✅/🟡/❌/⬜)**, and **priority (A/B/C/Lead)**.
- Always capture the **exact snippet** or **context sentence** showing the exact name (this is your evidence).
- Capture the **URL as-found** (do not silently strip tracking params, but you *may* also store a clean canonical URL in a second column).
- Record the **date searched** and the **engine/index** it was found on.
- **Deduplicate aggressively.** The same underlying page reached via a mirror/meta engine is one item. Keep the *best/cleanest* URL as primary and note others.
- Do **not** edit source originals; add new rows to the registry (see `registry/README.md`).

---

## 7. Honesty & boundary

- **No web search can prove absolute completeness.** Deleted/private/paywalled/print-only/social-only/unindexed/region-restricted content will be missed. Say so in the final report.
- This census shows **that** a public exact-name record exists. It does **not** validate the *truth* of any biographical/promotional claim inside a given page.
- Where the dump's own labels conflict (e.g., Discogs “58 appearances” vs. “60 rows”), preserve both and explain, as the master does.

---

## 8. Ground-truth to reconcile against

These define what the census *should* be able to rediscover (a known-answers sanity check):

- **`Zazie_2026_Accomplishment_Register_Maximal_Edition.docx`** — lists every 2026 release, press feature, film selection, and professional reach. Cross-reference: did the census find each corresponding public page?
- **`Zazie_Media_Master (1).pdf`** — the **133-record** exact-name master (Priority A=23, B=26, C=84, +15 leads). Cross-reference: are all 133 still live? Any now broken?
- **`registry/seed/`** — the **260 raw URLs** from the links dump (see README map).

A successful week = the census **catches everything in ground truth**, plus genuinely *new* finds that ground truth never listed.

---

## 9. The color/status quick reminder

🔴 Press · 🌸 Film · 🟣 Recognition · 🔵 Profiles · 🟠 Music · 🩵 Data · 🟢 Social · 📼 Mirrors · 🖤 Spam
✅ Live · 🟡 Partial · ❌ Broken · ⬜ Unchecked · 🥇A · 🥈B · 🥉C · 🔎 Lead

*Proceed to [`docs/02_DEEP_SEARCH_PLAYBOOK.md`](02_DEEP_SEARCH_PLAYBOOK.md).*
