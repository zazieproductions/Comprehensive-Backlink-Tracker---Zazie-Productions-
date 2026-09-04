# ✅ 07 — LINK-CHECK & VERIFICATION RUNBOOK

> The **“double-check that they work later”** pass. Turns a pile of recorded URLs into a clean, statused directory. Goal: decide for every URL whether it is **✅ live+verified**, **🟡 partial**, **❌ broken/no-evidence**, or still **⬜ unchecked** — using **both** an HTTP probe *and* exact-name text evidence.

---

## 1. What "verified" means (two gates, both must pass)

A URL is **✅ LIVE/VERIFIED** only when:

1. **Reachable** — HTTP 200 (or a legitimate redirect that lands on the real page), and
2. **Evidence** — the rendered page contains at least one of the exact strings
   **`Zazie Productions`** or **`Zazie Kanwar-Torge`**.

Passing gate 1 but failing gate 2 → **🟡 PARTIAL**. Failing gate 1 (after archive retry) → **❌**.

| Status | HTTP | Exact name on page | Meaning |
|---|---|---|---|
| ✅ LIVE / VERIFIED | 200 (or good redirect) | Yes | Count it. |
| 🟡 PARTIAL / RE-CHECK | 200 but hidden/weak | Not visible (JS, region, login) | Count only if index-snippet proves name; else lead. |
| ❌ BROKEN / NO EVIDENCE | error / 404 / 403 / dead | No | Do not count; note code. |
| ⬜ UNCHECKED | not probed yet | unknown | Default state of every recorded row until touched. |

---

## 2. Steps for each URL

1. **Probe** the URL with a polite client (respect robots.txt, low rate, realistic User-Agent). Follow **1–2 redirects**; record the **final URL** and **final status code**. Note common blocks: `403` (bot-blocked — retry manually in a browser), `429` (slow down), `999`/`301` loops.
2. **If 200:** fetch the readable text and search for both exact strings. Case is free; the **spacing matters** (the two names must appear as spaced strings).
3. **If the name isn't visible** but the URL *looks* right, try:
   - Wayback snapshot `https://web.archive.org/web/2026/https://URL`
   - Text proxy `https://r.jina.ai/https://URL` (bypasses JS-only render)
   - A search-engine `site:`/title lookup to see if the **index snippet** preserves the name.
   If the snippet proves the name → **🟡 index-verified** (countable per `01` §5). Otherwise → 🔎 lead.
4. **If the probe errors**, retry once via Wayback, then once via a text proxy, then mark **❌** with the reason/code. A page deleted from the live web but preserved in archive still *exists* historically — decide whether the census counts archived-only (recommend: log separately as 📼/🩵 archived, don't count as live).

---

## 3. Bulk-tooling suggestions (Day 7)

Manual checking of hundreds of links is slow. A script (run locally, politely) can pre-classify:

- HEAD/GET probe each URL with a small pool of threads + **delay/backoff**, capturing final status.
- Save `status` column back to the registry CSV (turn `⬜` → a provisional ✅/❌ by HTTP only).
- **Then a human/agent still must confirm exact-name evidence** for every provisional ✅ (HTTP 200 alone is NOT verification).
- Respect per-site rate limits; spread requests; stop if 429/403 sweeps begin.

> Example polite pseudo-logic:
> ```
> for url in registry:
>     s = request(url, follow_redirects=True, delay=rnd(1,3))
>     record(final_status=s.status, final_url=s.url)
>     if s.ok and any(name in s.text for name in NAMES): tag="LIVE"
>     elif s.ok: tag="PARTIAL"
>     else: tag="DEAD"; retry via wayback/proxy; fallback tag
> ```

---

## 4. Special-cases & gotchas

- **Bot walls (Cloudflare/403/999):** probe again in a real browser; if blocked for everyone, it's effectively dead for census purposes → 🟡/❌ with note.
- **Region-locked:** try a different region/language SERP or a Wayback capture before declaring broken.
- **JS-only SPA:** HTTP 200 but body empty of the name → use the index snippet or text proxy before calling it partial.
- **Tracking-param variants:** `?si=…`, `?fbclid=…` point at the same page. Keep one canonical row, note the variant.
- **Aggregator/mirror duplicates:** dozens of repeater URLs for one YouTube ID are *one* underlying item. Keep primary + count mirrors separately in the 📼 bucket.
- **Spam/parasite:** HTTP 200 + the name auto-injected from an RSS/press scrape ≠ editorial presence. Keep in 🖤 and never count as real.

---

## 5. Reporting the double-check

End-of-pass output = every row tagged, plus a summary:

| Bucket | ✅ Live | 🟡 Partial | ❌ Broken | ⬜ Unchecked | Total |
|---|---|---|---|---|---|
| 🔴 Press | | | | | |
| 🌸 Film | | | | | |
| 🟣 Recognition | | | | | |
| 🔵 Profiles | | | | | |
| 🟠 Music | | | | | |
| 🩵 Data | | | | | |
| 🟢 Social | | | | | |
| 📼 Mirrors | | | | | |
| 🖤 Spam | | | | | |

Also produce the **Gap list**: ground-truth items (accomplishment register + 133-record master) that the census could not re-locate live — these are either genuinely gone or still-to-find. Never imply completeness if gaps remain.

---

*Ready to consolidate. See [`registry/README.md`](../registry/README.md) to write final rows.*
