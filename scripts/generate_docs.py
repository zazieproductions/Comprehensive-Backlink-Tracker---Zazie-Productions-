#!/usr/bin/env python3
"""Regenerate the categorized Markdown references and summary from data/master/master_index.csv.

Usage:  python3 scripts/generate_docs.py
"""
import csv, os, re
from collections import defaultdict, Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, 'data', 'master', 'master_index.csv')
OUT = os.path.join(BASE, 'data', 'master', 'categorized')
os.makedirs(OUT, exist_ok=True)

CAT_META = {
 'Press & Editorial':                ('Press & Editorial', 'Independent coverage, features, reviews, press releases and news mentions.'),
 'Film, Festivals & Exhibitions':    ('Film, Festivals & Exhibitions', 'Film credits, festival selections, awards and exhibition listings.'),
 'Publications & Recognition':       ('Publications & Recognition', 'Anthologies, contest recognition, security credits and other published recognition.'),
 'Profiles & Catalogs':              ('Profiles & Catalogs', 'Artist, composer and professional profiles across industry and creative platforms.'),
 'Streaming & Music Platforms':      ('Streaming & Music Platforms', 'Artist pages on streaming services and music databases.'),
 'Music Compilations':               ('Music Compilations', 'Compilation appearances (Discogs / Bandcamp releases).'),
 'Official Properties & Channels':   ('Official Properties & Channels', 'Self-owned channels: storefronts, Bandcamp, itch.io, YouTube, Linktree.'),
 'Podcasts & Broadcasts':            ('Podcasts & Broadcasts', 'Podcast episodes, radio broadcasts and audio features.'),
 'Community, Wiki & Fan Indexes':    ('Community, Wiki & Fan Indexes', 'Fan quizzes, wikis, forums, charts and community pages.'),
 'Search-Engine Index':              ('Search-Engine Index', 'Search-engine result pages (SERPs) that index the target name.'),
 'Video Mirror / Backlink Sites':    ('Video Mirror / Backlink Sites', 'Video/backlink surfaces still treated as ordinary census records (parasitic mirrors were moved to the low-trust category).'),
 'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust': ('Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust', 'Evidence-preservation register: hacked-site doorways, auto-scraped / auto-generated replicas, RSS & PR republications, mirror/embed parasitism, pastes, search-redirect artifacts. NEVER counted as credible coverage, credits, profiles or biographical fact. Full ledger: registry/spam_scraper_syndication_lowtrust_2026-09-05/.'),
 'Music Discography':                ('Music Discography', 'Discography / catalogue database records (Discogs, RateYourMusic, etc.).'),
 'Lyrics & Music Databases':         ('Lyrics & Music Databases', 'Lyrics and music-metadata database records (Lyrics.com, archived databases).'),
}
ORDER = ['Press & Editorial','Film, Festivals & Exhibitions','Publications & Recognition','Profiles & Catalogs',
 'Streaming & Music Platforms','Music Compilations','Official Properties & Channels','Podcasts & Broadcasts',
 'Community, Wiki & Fan Indexes','Search-Engine Index','Video Mirror / Backlink Sites',
 'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust','Music Discography','Lyrics & Music Databases']

def safe(t):
    return re.sub(r'[^A-Za-z0-9-]+', '-', t).strip('-')

rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
by = defaultdict(list)
for r in rows:
    by[r['category']].append(r)

for cat in ORDER:
    if cat not in by:
        continue
    recs = by[cat]
    title, desc = CAT_META[cat]
    lines = [f'# {title}', '', f'**{len(recs)} records.** {desc}', '']
    hostc = defaultdict(list)
    for r in recs:
        hostc[r['host']].append(r)
    for h in sorted(hostc):
        lines.append(f'## {h} — {len(hostc[h])}')
        lines.append('')
        lines.append('| URL | Target | Tier | Date | Title | Source | Status | Notes |')
        lines.append('|---|---|---|---|---|---|---|---|')
        for r in sorted(hostc[h], key=lambda x: x['url']):
            url = r['url']
            url_disp = url if len(url) <= 90 else url[:90] + '...'
            lines.append(f'| [{url_disp}]({url}) | {r["target"]} | {r["trust_tier"]} | {r["date"]} | {(r["title"] or "")[:60].replace("|","/")} | {r["source"]} | {r["status"]} | {r["notes"]} |')
        lines.append('')
    with open(os.path.join(OUT, safe(title) + '.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# Summary
total = len(rows)
tier = Counter(r['trust_tier'] for r in rows)
src = Counter(r['source'] for r in rows)
summary = ['# Master Directory — Summary', '',
           f'**{total} records** across {len(by)} categories.',
           '',
           '## By category', '',
           '| Category | Count |', '|---|---|']
for cat in ORDER:
    if cat in by:
        summary.append(f'| {cat} | {len(by[cat])} |')
summary += ['', '## By trust tier', '', '| Tier | Count |', '|---|---|']
for t in sorted(tier):
    summary.append(f'| {t} | {tier[t]} |')
summary += ['', '## By source', '', '| Source | Count |', '|---|---|']
for s in sorted(src):
    summary.append(f'| {s} | {src[s]} |')
summary += ['', '**Trust tiers:**  A = strong independent/institutional press & recognition · B = supporting profiles/catalogs · C = compilations/community/lower-priority · D = spam / scraper / syndication / low-trust (flagged, non-authoritative — see the low-trust register).']
with open(os.path.join(BASE, 'data', 'master', 'SUMMARY.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(summary))

print(f'Regenerated {len(by)} category docs + SUMMARY.md for {total} records.')
