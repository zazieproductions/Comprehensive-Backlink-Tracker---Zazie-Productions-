# 📋 Session handoff — 2026-09-21 · agent-memory-convention

**Branch:** `arena/01a0c52f-comprehensive-backlink-tracker` · **PR:** this change's PR · **Merged to main:** pending at session end

## 🙋 What was asked

> How to turn Arena.ai agent mode into a 24/7 personal agent like OpenClaw — or a worker visible in
> the multi-agent fleet dashboards — or otherwise push it beyond its sandbox. From the options
> offered, the user picked: **"Agent memory + runbook"** — `AGENT_MEMORY.md` convention and session
> handoff docs so every Arena session resumes where the last one stopped.

## 🛠️ What was done

- Answered the 24/7 question with a three-tier map (see Handoff notes — the map is summarized in L-001).
- Built this `agent/` convention: `AGENT_MEMORY.md` (living state), `README.md` (rituals),
  `sessions/_TEMPLATE.md` (handoff template), this note (first real entry).
- Reconciled the project-count numbers (102 vs 124) so future agents don't "fix" a non-bug.
- Root README: repository-map entry for `agent/` + ground-rule note documenting the narrow exception.

## 📁 Files touched

| File | Change |
|---|---|
| `agent/README.md` | new — rituals, kickstart prompt, merge-conflict rule |
| `agent/AGENT_MEMORY.md` | new — living state, seeded with verified counts |
| `agent/sessions/_TEMPLATE.md` | new — handoff template |
| `agent/sessions/2026-09-21-agent-memory-convention.md` | new — this note |
| `README.md` | map + one ground-rule note (agent/ layer documented) |

## ✅ Verification

- [x] Live-count checks run before trusting memory (output below)
- [x] Regenerate steps 1→4 run — **not needed** (no data change; `data/`, `registry/`, PDFs untouched)
- [x] Root README badges/prose counts — **unchanged** (no count changed)
- [x] `AGENT_MEMORY.md` updated (all four sections)

```
consolidated_directory: 754 records, 73 engine endpoints
master_index.csv:       634 rows
project_clusters.json:  124 projects (102 multi-link, 22 single-link)
project_clusters.csv:   423 rows = 401 (multi-link) + 22 (single-link); 406 unique URLs
listen_links.csv:       61 rows
```

## 🧠 Decisions (→ mirrored in the AGENT_MEMORY.md decision log)

| Decision | Why |
|---|---|
| Adopted `agent/` memory + handoff convention | Git-backed memory is the only persistence amnesiac agent sessions get |
| `agent/` documented as a narrow ground-rule exception | Same doc class as `registry/project_sections/README.md` — instructions + state, not research narrative |
| Memory updates commit in the same commit/PR as the work | Memory describing an unlanded state is fiction |
| Memory must reach `main` | Next session branches from `main`; unmerged = invisible |

## 🌀 Open loops left

| ID | Loop | Next step |
|---|---|---|
| L-001 | 24/7 personal-agent stack | User picks when ready — remaining build options: **OpenClaw deploy kit** (scripts + systemd + loopback/Tailscale hardening), **GitHub Actions cron workers** (scheduled jobs → commits + issue queue), **monitoring/heartbeats** (Uptime Kuma / healthchecks.io + Telegram alerts) |

## 🤝 Handoff notes — next agent, read this

- **Resume point:** convention is live. Default next work is L-001 when the user asks for it.
  Otherwise apply the ▶️/⏹️ rituals from `agent/README.md` to whatever the user brings.
- **Watch out:**
  - **Merge this to `main`** or the next session never sees the memory — the convention dies on the branch.
  - The 24/7 map from the original discussion (kept so nobody re-researches it):
    Arena sessions are sandboxed and session-bound — no true 24/7, no self-wake/webhooks. Three tiers:
    (1) *maximize Arena* — session-lifetime background processes, git as memory (this folder),
    GitHub Actions as the real cron with issues as the queue;
    (2) *real 24/7 assistant* — OpenClaw (the ex-Clawdbot/Moltbot project) self-hosted on a VPS,
    `npm install -g openclaw@latest` + `openclaw onboard --install-daemon`, proactive messaging over
    Telegram/Discord/WhatsApp — **keep its gateway on loopback + token auth, reach it via Tailscale;
    install only from official sources** (exposed dashboards + typosquat installers were real incidents);
    (3) *fleet dashboards* — Claude Code Agent View (`claude agents`), GitHub Copilot desktop "My Work",
    amux, AgentsRoom manage local CLI agents (Arena sessions don't appear there natively);
    Uptime Kuma / healthchecks.io glue for alerts.
  - Counts live in three places — data files, root README, `AGENT_MEMORY.md`. Change all three together.
