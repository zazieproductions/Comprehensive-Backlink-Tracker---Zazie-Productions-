# 🗂️ REGISTRY — where found places live

This folder is the **working directory of every place** `Zazie Productions` / `Zazie Kanwar-Torge` has been found. Seed (found-in-dump) data is auto-extracted under `seed/`. New census finds are appended by agents following the conventions below.

---

## Structure

```
registry/
├── README.md                        <- you are here (how to add rows)
└── seed/                            <- auto-extracted from the existing dump
    ├── SEED_INDEX_FROM_DUMP.md      <- 260 URLs, clustered by media type (human-readable)
    ├── seed_unique_urls.csv         <- machine list: domain,url,first_seen_source
    └── seed_domain_summary.csv      <- domain -> URL-count coverage summary
```

### Phase files

| File | Phase | What it holds |
|---|---|---|
| [`PHASE3_EDITORIAL_LITERARY.md`](PHASE3_EDITORIAL_LITERARY.md) | Phase Three — editorial / literary / criticism / blog ecosystems | New exact-string places in published-writing venues (magazines, anthologies, journals, podcast notes), partial/handle-only rows, open leads and the full query log. Rows follow the universal row template below. |

> ⚠️ `seed/` files are **generated** from the source PDFs. If the source PDFs change, regenerate rather than hand-editing these three files (keeps them in sync). New live research goes into the **live master** below.

---

## The LIVE MASTER (create during the census)

Add one master file for verified/active work — a Markdown table is recommended so it renders on GitHub. Suggested filename: `LIVE_MASTER.md` (or keep rows in a spreadsheet/CSV of your choice and mirror a view here).

### Recommended columns (one row = one unique place)

| Column | Values / example |
|---|---|
| `URL` | as-found; you may add a clean canonical URL too |
| `MEDIA` | 🔴 press · 🌸 film · 🟣 recognition · 🔵 profile · 🟠 music · 🩵 data · 🟢 social · 📼 mirror · 🖤 spam |
| `PRIORITY` | 🥇A · 🥈B · 🥉C · 🔎Lead |
| `STATUS` | ✅ live · 🟡 partial · ❌ broken · ⬜ unchecked |
| `NAME` | `Prod` · `Kanwar` · `Both` |
| `EVIDENCE` | 1–2 line exact-name snippet |
| `FOUND ON` | engine/index/platform + date |
| `CONTEXT` | track / film / compilation / project it refers to |

Example:

```
| https://www.last.fm/music/Zazie+Productions | 🔵 | 🥉C | ✅ | Prod | "Zazie Productions — albums, tracks…" | last.fm internal search · 2026-09-04 | artist profile |
```

---

## Rules for adding rows

1. **Append; never edit or delete** existing rows unless you're correcting a verified error (and then note the change).
2. **One unique page = one row.** A mirror/aggregator of an original is *not* a new row — record the mirror separately in the 📼 bucket if you log it at all.
3. **Evidence is mandatory.** No snippet / no found-on / no date = it's a 🔎 Lead, not a result. Don't pad totals with leads.
4. **Don't count 🖤 spam or 📼 mirrors** toward “real places”; keep them visible but clearly separate.
5. Run the [`docs/07`](../docs/07_LINK_CHECK_AND_VERIFICATION.md) runbook before promoting any `⬜` to `✅`.
6. Follow the color legend in the root [`README.md`](../README.md) so statuses and types stay consistent across the whole repo.

---

## Ground-truth files to reconcile against (elsewhere in repo)

- `Zazie_2026_Accomplishment_Register_Maximal_Edition.docx` — 2026 releases/press/selects.
- `Zazie_Media_Master (1).pdf` — the 133-record exact-name master (Priority A/B/C + 15 leads).
- `Random Zazie Productions links .pdf` — the raw link dump that produced `seed/`.

When the census is done, the live master + seed should **cover** every ground-truth item (or explain the gap). That coverage check is the measure of a successful week.
