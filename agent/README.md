# 🤖 Agent Memory & Session Handoffs

> Working state for AI coding agents (Arena, Claude Code, …) that work on this repo in separate,
> amnesiac sessions. **This is an ops layer, not a research report** — the Ground rules stand:
> research truth lives in `data/`, `registry/`, `sources/`, `scripts/` and the two PDFs.
> Nothing in `agent/` overrides them.

## 🗂️ Layout

| File | What it is | Who writes it |
|---|---|---|
| [`AGENT_MEMORY.md`](AGENT_MEMORY.md) | 🧠 living state: mission, current counts, decision log, open loops | updated at the **end** of every session |
| [`sessions/_TEMPLATE.md`](sessions/_TEMPLATE.md) | handoff note template | copied once per session |
| `sessions/YYYY-MM-DD-<slug>.md` | one handoff note per session: what was asked, done, left | written at the **end** of every session |

## ▶️ Session start ritual

1. Read `agent/AGENT_MEMORY.md` — top to bottom. It **is** the resume point.
2. Read the newest `agent/sessions/*.md` entry (and any older ones its handoff notes point to).
3. Before touching data or registries, skim the root README ground rules.
4. If the session will change `data/` or `registry/`, verify live counts first (commands in 🧰 of `AGENT_MEMORY.md`) — don't trust remembered numbers.
5. Tell the user in one sentence where work left off and what you're about to do — before doing it.

## ⏹️ Session end ritual

1. Finish (or deliberately park) the work.
2. Copy `sessions/_TEMPLATE.md` → `sessions/YYYY-MM-DD-<slug>.md` and fill every section.
3. Update `AGENT_MEMORY.md`: refresh 📍 Current state; append 🧠 Decision log rows; update 🌀 Open loops
   (close finished ones with ✅ + date — **don't delete history**); add a 📜 Session index row.
4. If data changed: run the regenerate steps 1→4 (root README §♻️) and update **every** count —
   root README badges/prose and `AGENT_MEMORY.md` — in the same session. Never edit the PDFs by hand.
5. Commit the memory updates **in the same commit/PR as the work they describe** — memory that lands
   separately describes a repo state that never existed.
6. **Get it merged to `main`.** Agent sessions branch from `main`; memory stranded on an unmerged
   branch is invisible to the next session. (This repo's history — Arena branches merged via PRs — is the pattern.)

## 🚀 Kickstart prompt for a new session

Paste this (or something like it) when opening a fresh agent session:

> Resume from agent memory: read `agent/AGENT_MEMORY.md`, then the newest entry in `agent/sessions/`.
> Continue the top open loop in AGENT_MEMORY.md unless I redirect you. Follow the rituals in
> `agent/README.md` — end this session by updating `AGENT_MEMORY.md` and writing a session handoff.

## 🤝 Merge-conflict rule (multiple agents, one memory)

- 📜 Session index & 🧠 Decision log are **append-only**: on conflict, keep *all* rows from both sides,
  in chronological order.
- 🌀 Open loops: keep both sides' loops; if IDs collide, renumber one with an `-a` / `-b` suffix.
- 📍 Current state & counts: take the block from the **latest** session note, then re-verify against
  `data/` — the data files settle any argument.

## ⛔ What never goes in `agent/`

- **Secrets** — no API keys, tokens, passwords or `.env` contents. References only ("key lives in X").
- **Research narrative** — findings, ledgers and readable reports belong in `data/`, `registry/` and
  the PDFs (Ground rules). This folder exists by explicit, narrow exception: it is working
  instructions + state, of the same class as `registry/project_sections/README.md`.
- **Duplicates of the truth** — when a count lives in `data/master/`, memory quotes it with an
  as-of date. Memory never becomes the source.
