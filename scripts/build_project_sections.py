#!/usr/bin/env python3
"""Group the census into PROJECTS: the underlying real-world things a link belongs to.

Input
  data/master/consolidated_directory.json     every catalogued link (built by scripts/ingest_all_links.py)
  data/master/listen_links.csv                one row per compilation appearance (compilation, label, listen URL)
  data/master/register_link_map.csv           2026 Accomplishment Register entries mapped to public links
  registry/project_sections/projects.csv      the curated project register (one row per project + its match rules)

Output
  data/master/project_clusters.json           projects with their member links, roles and per-role counts
  data/master/project_clusters.csv            the same thing flattened: one row per link, with its project + role

Why this exists
  The main directory is sorted by MEDIA TYPE, so one project's links end up scattered across sections
  (the Black Mountain College radio commission alone sits in Press, Podcasts, Community and Spam). This
  pass re-cuts the same corpus by PROJECT - the thing the links are actually about - so that a broadcast
  commission, a compilation appearance, an anthology or a film can each be read as one section: the
  project's own page first, then its catalogue records, distribution mirrors, press, archive snapshots
  and (clearly separated, last) the scraped/poisoned copies of the same thing.

Matching
  Each register row carries `match_phrases` (folded substring match against URL + title), optional
  `notes_match`/`notes_hosts` (for hosts whose page title never names the project) and `exclude`
  patterns. Matching is deliberately conservative and fully deterministic: a link joins a project only
  when a phrase is present, never by fuzzy similarity. `--report` prints what was matched, what was not,
  and which multi-link hosts are still unclaimed so the register can be extended by hand.

Usage
  python3 scripts/build_project_sections.py            # build data/master/project_clusters.{json,csv}
  python3 scripts/build_project_sections.py --report   # build, then print the curation QA report
"""
import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from urllib.parse import unquote

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data', 'master')
DIRECTORY = os.path.join(DATA, 'consolidated_directory.json')
LISTEN = os.path.join(DATA, 'listen_links.csv')
REGISTER_MAP = os.path.join(DATA, 'register_link_map.csv')
PROJECTS = os.path.join(BASE, 'registry', 'project_sections', 'projects.csv')
OUT_JSON = os.path.join(DATA, 'project_clusters.json')
OUT_CSV = os.path.join(DATA, 'project_clusters.csv')

# --------------------------------------------------------------------------- role vocabulary
# The order below is the reading order used inside every project section of the PDF: what the
# project IS first, then how the world indexed, mirrored and finally poisoned it.
ROLES = [
    ('canonical', 'PROJECT PAGE', '#0b6e4f',
     'the project’s own home: label page, publisher page, broadcaster page, festival page, register entry'),
    ('credit', 'ARTIST CREDIT', '#2e7d32',
     'the artist’s own page for the work — a release, track, book, score or tool carrying the credit'),
    ('catalogue', 'CATALOGUE RECORD', '#1a73e8',
     'database records of the same project: Discogs, IMDb, RateYourMusic, Beatport, lyrics and metadata DBs'),
    ('distribution', 'DISTRIBUTION / LISTEN', '#039be5',
     'platform mirrors that carry the same project: streaming services, podcast directories, retail listings'),
    ('media', 'MEDIA / EMBED', '#7b1fa2',
     'the project itself as audio/video: official uploads, trailers, screeners, embeds'),
    ('press', 'PRESS & REVIEWS', '#d93025',
     'independent coverage OF this project: features, reviews, interviews, news items'),
    ('event', 'EVENT / SCREENING', '#e8710a',
     'listings, tickets, screening and performance pages for the project'),
    ('reference', 'REFERENCE / DIRECTORY', '#188038',
     'wikis, community pages, profiles and directories that describe the project'),
    ('mirror', 'MIRROR / SYNDICATION', '#607d8b',
     'legitimate-but-derived copies: netlabel news reposts, archive.org copies, aggregator mirrors'),
    ('archive', 'ARCHIVE SNAPSHOT', '#8a6d3b',
     'Wayback / archive captures of a page that also exists live'),
    ('quarantine', 'QUARANTINE — DO NOT CITE', '#616161',
     'scraped clones, SEO doorways and syndication spam carrying the project — evidence of contamination only'),
]
ROLE_ORDER = [r[0] for r in ROLES]
ROLE_BY_KEY = {r[0]: r for r in ROLES}

# host suffix -> role (first match wins; longest suffix first)
HOST_ROLE = {
    'discogs.com': 'catalogue', 'rateyourmusic.com': 'catalogue', 'imdb.com': 'catalogue',
    'pro.imdb.com': 'catalogue', 'shazam.com': 'catalogue', 'beatport.com': 'catalogue',
    'musicbrainz.org': 'catalogue', 'lyrics.com': 'catalogue', 'songmeanings.com': 'catalogue',
    'paroles-musique.com': 'catalogue', 'sonichits.com': 'catalogue', 'soundbetter.com': 'catalogue',
    'web.archive.org': 'archive', 'archive.org': 'mirror', 'archive.ph': 'archive',
    'open.spotify.com': 'distribution', 'podcasts.apple.com': 'distribution',
    'music.apple.com': 'distribution', 'apple.com': 'distribution', 'qobuz.com': 'distribution',
    'deezer.com': 'distribution', 'tidal.com': 'distribution', 'amazon.com': 'distribution',
    'mightyape.co.nz': 'distribution', 'frauhofer.at': 'distribution', 'smashwords.com': 'distribution',
    'tunein.com': 'distribution', 'ivoox.com': 'distribution', 'podbean.com': 'distribution',
    'listennotes.com': 'distribution', 'podcasts-online.org': 'distribution',
    'podcast365.ro': 'distribution', 'soundcloud.com': 'distribution', 'bandcamp.com': 'distribution',
    'youtube.com': 'media', 'youtu.be': 'media', 'vimeo.com': 'media', 'tiktok.com': 'media',
    'eventbrite.co.uk': 'event', 'tickettailor.com': 'event', 'stayhappening.com': 'event',
    'mycommunitycinema.org.uk': 'event', 'dionysianpubliclibrary.com': 'canonical',
    'lulu.com': 'distribution', 'store.pothi.com': 'distribution', 'ogre.red': 'canonical',
    'clongclongmoo.org': 'mirror', 'soundshiva.net': 'mirror', 'telegra.ph': 'mirror',
    'prfree.org': 'press', 'news.prfree.org': 'press', 'github.com': 'credit', 'itch.io': 'credit',
    'gumroad.com': 'credit', 'artfacts.net': 'catalogue', 'filmfreeway.com': 'event',
    'film-makerscoop.com': 'event', 'connects.canyoncinema.com': 'event', 'expcinema.org': 'event',
    'peopleversus.tv': 'event', 'patreon.com': 'reference', 'icebergcharts.com': 'reference',
    'reddit.com': 'reference', 'wikipedia.org': 'reference', 'fandom.com': 'reference',
}
# host -> role for the largest families, expressed as suffix match
BANDCAMP_OWN = 'zazieproductions.bandcamp.com'

FOLD_KEEP = re.compile(r'[^a-z0-9]+')


def fold(text):
    """Lower-case, strip accents, collapse punctuation: the canonical comparison form."""
    text = unicodedata.normalize('NFKD', text or '').encode('ascii', 'ignore').decode()
    return FOLD_KEEP.sub(' ', text.lower()).strip()


def url_relates(rec_url, pin):
    """True when a record URL and a register pin are the same address.

    The repository holds a number of truncated URLs (a long URL cut for display in the source PDF),
    so equality is too strict in both directions: a pin may be longer than the stored URL or the
    stored URL may be longer than the pin. Comparison ignores scheme, www and trailing punctuation.
    """
    a = re.sub(r'^https?://(www\.)?', '', (rec_url or '').lower()).rstrip('/ .,')
    b = re.sub(r'^https?://(www\.)?', '', (pin or '').lower()).rstrip('/ .,')
    if not a or not b:
        return False
    if a == b:
        return True
    short, long = (a, b) if len(a) <= len(b) else (b, a)
    # prefix-tolerant (the census stores some truncated URLs) but never a bare host:
    # the shorter form must carry a real path, so a label homepage cannot claim every release on it
    return len(short) >= 25 and '/' in short and short in long


def haystack(rec):
    """What a phrase is matched against: the URL (unquoted) plus the record title."""
    return fold(unquote(rec['url'])) + ' ' + fold(rec.get('title') or '')


def role_for(rec, project):
    """Classify one link inside one project, most specific rule first."""
    host = (rec.get('host') or '').lower()
    # 1. quarantine beats everything: the record itself says it is untrustworthy
    if rec.get('tier') == 'D' or rec.get('category', '').startswith('Spam, Scraper'):
        return 'quarantine'
    # 2. explicit per-project role overrides (host or url fragment -> role)
    for rule, role in project.get('role_overrides', []):
        rule = rule.strip().lower()
        if rule in rec['url'].lower() or rule == host or host.endswith('.' + rule) or host.endswith(rule):
            return role
    # 3. the project's own bandcamp / label page
    if host == BANDCAMP_OWN and 'bandcamp.com' in host:
        return 'credit'
    # 4. curator-declared canonical hosts for this project (label page, publisher site, broadcaster)
    for h in project.get('canonical_hosts', []):
        if host == h or host.endswith('.' + h):
            return 'canonical'
    # 5. press hosts
    if project.get('press_hosts') and any(host == h or host.endswith('.' + h) for h in project['press_hosts']):
        return 'press'
    # 6. global host table
    for suffix, role in sorted(HOST_ROLE.items(), key=lambda kv: -len(kv[0])):
        if host == suffix or host.endswith('.' + suffix):
            return role
    # 7. everything else is a directory / community page describing the project
    return 'reference'


# --------------------------------------------------------------------------- register
MATCH_MODES = ('phrase', 'loose')


def load_register():
    """Read the curated project register. Every column is documented in the file header."""
    if not os.path.exists(PROJECTS):
        return []
    out = []
    with open(PROJECTS, encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            name = (row.get('name') or '').strip()
            if (row.get('project_id') or '').strip().startswith('#'):
                continue                                   # comment line in the register
            if not name or name.startswith('#'):
                continue
            project = {
                'id': (row.get('project_id') or '').strip() or re.sub(r'-+', '-', fold(name).replace(' ', '-')),
                'name': name,
                'kind': (row.get('kind') or 'Project').strip(),
                'year': (row.get('year') or '').strip(),
                'artist_role': (row.get('artist_role') or '').strip(),
                'summary': (row.get('summary') or '').strip(),
                'anchor': (row.get('anchor') or '').strip(),
                'phrases': [p.strip() for p in (row.get('match_phrases') or '').split('|') if p.strip()],
                'loose_phrases': [p.strip() for p in (row.get('loose_phrases') or '').split('|') if p.strip()],
                'exclude': [p.strip() for p in (row.get('exclude') or '').split('|') if p.strip()],
                'notes_match': [p.strip() for p in (row.get('notes_match') or '').split('|') if p.strip()],
                'notes_hosts': [p.strip().lower() for p in (row.get('notes_hosts') or '').split('|') if p.strip()],
                'pins': [p.strip().lower() for p in (row.get('pin') or '').split('|') if p.strip()],
                'canonical_hosts': [p.strip().lower() for p in (row.get('canonical_hosts') or '').split('|') if p.strip()],
                'press_hosts': [p.strip().lower() for p in (row.get('press_hosts') or '').split('|') if p.strip()],
                'role_overrides': [tuple(p.split('=', 1)) for p in (row.get('role_overrides') or '').split('|')
                                   if '=' in p],
                'register_refs': [p.strip() for p in (row.get('register_refs') or '').split('|') if p.strip()],
                'source': (row.get('source') or 'curated').strip(),
            }
            if not (project['phrases'] or project['loose_phrases'] or project['notes_match'] or project['pins']):
                project['phrases'] = [name]
            out.append(project)
    return out


def compilation_tracks():
    """track credit per compilation, harvested from the 2026 Accomplishment Register link map.

    The register writes an appearance as 'Track Name (Compilation Name)'; that is the one place in
    the repository where the artist's own credit for a compilation is recorded, so it is used to
    label the compilation sections with what was actually contributed. Entries of the form
    'Work (Series/Compilation)' are mapped by exact folded compilation name, so nothing is guessed.
    """
    tracks = {}
    if not os.path.exists(REGISTER_MAP):
        return tracks
    for row in csv.DictReader(open(REGISTER_MAP, encoding='utf-8')):
        m = re.match(r'^(.*?)\s*\((.+)\)\s*$', (row.get('RegisterEntry') or '').strip())
        if m:
            tracks[fold(m.group(2))] = m.group(1).strip()
    return tracks


def register_projects_from_sources():
    """Auto rows: one project per compilation in listen_links.csv that the register does not cover.

    The register stays the source of truth; this guarantees that a compilation which appears in the
    listen-link table is never silently dropped from the project view. Each auto row is pinned to
    the Discogs release and the listen URL recorded in that table, so even a compilation whose
    pages never print its name in the title (an ID-only Bandcamp URL, a bare Discogs release) still
    collects its own links. Register rows win: they may add aliases, credits and exclusions the auto
    row cannot know about.
    """
    if not os.path.exists(LISTEN):
        return []
    tracks = compilation_tracks()
    out = []
    for row in csv.DictReader(open(LISTEN, encoding='utf-8')):
        name = (row.get('compilation') or '').strip()
        if not name:
            continue
        pid = 'comp-' + re.sub(r'-+', '-', fold(name).replace(' ', '-'))[:60]
        pins = [u.strip().lower() for u in (row.get('discogs'), row.get('listen_url')) if u and u.strip()]
        label = (row.get('label') or '').strip()
        listen_url = (row.get('listen_url') or '').strip()
        canonical = []
        if 'bandcamp.com' in listen_url:
            canonical = [listen_url.split('/')[2]]
        track = ''
        for key, val in tracks.items():
            if key == fold(name) or (len(key) > 8 and key in fold(name)) or (len(fold(name)) > 8 and fold(name) in key):
                track = val
                break
        out.append({
            'id': pid,
            'name': name,
            'kind': 'Compilation appearance',
            'year': '',
            'artist_role': (f'track “{track}”' if track else (row.get('track') or '').strip()),
            'summary': 'V/A compilation' + (f' on {label}' if label else '') +
                       '. Auto-derived from the listen-link table; add a curated register row to describe it.',
            'anchor': listen_url or (row.get('discogs') or '').strip(),
            'phrases': [name],
            'loose_phrases': [],
            'exclude': [],
            'notes_match': [],
            'notes_hosts': [],
            'pins': pins,
            'canonical_hosts': canonical,
            'press_hosts': [],
            'role_overrides': [],
            'register_refs': [],
            'source': 'auto:listen_links',
        })
    return out


def merge_projects(curated, auto):
    """Curated rows win by id; auto rows are added when no curated row claims them by name."""
    by_id = {p['id']: p for p in curated}
    curated_names = {fold(p['name']) for p in curated}
    curated_phrases = {fold(ph) for p in curated for ph in p['phrases']}
    merged = list(curated)
    for p in auto:
        fname = fold(p['name'])
        if p['id'] in by_id or fname in curated_names or fname in curated_phrases:
            continue
        # a curated row may cover it with an alias phrase
        if any(fname in ph or ph in fname for ph in curated_phrases if len(ph) > 6):
            continue
        # a curated row may also claim the auto row's own anchor URL
        if p['anchor'] and any(p['anchor'].lower() in pin for row in curated for pin in row['pins']):
            continue
        merged.append(p)
    return merged


def matches(project, rec, hay):
    """True when this record belongs to this project. Deterministic, phrase-first."""
    for pat in project['exclude']:
        if fold(pat) and fold(pat) in hay:
            return False
    for pin in project['pins']:
        if url_relates(rec['url'], pin):
            return True
    for phr in project['phrases']:
        f = fold(phr)
        if f and re.search(r'(?<![a-z0-9])' + re.escape(f) + r'(?![a-z0-9])', hay):
            return True
    for phr in project['loose_phrases']:
        toks = [t for t in fold(phr).split() if len(t) >= 4]
        if toks and all(re.search(r'(?<![a-z0-9])' + re.escape(t), hay) for t in toks):
            return True
    if project['notes_match']:
        host = (rec.get('host') or '').lower()
        allowed = (not project['notes_hosts']) or any(host == h or host.endswith('.' + h)
                                                      for h in project['notes_hosts'])
        if allowed:
            notes = fold(rec.get('notes') or '')
            for phr in project['notes_match']:
                f = fold(phr)
                if f and re.search(r'(?<![a-z0-9])' + re.escape(f) + r'(?![a-z0-9])', notes):
                    return True
    if project['register_refs']:
        notes = rec.get('notes') or ''
        for ref in project['register_refs']:
            if re.search(r'(?<![0-9])' + re.escape(ref) + r'(?![0-9])', notes):
                return True
    return False


def build_projects(verbose=False):
    """Assign every catalogued link to zero, one or several projects and return the payload."""
    payload = json.load(open(DIRECTORY, encoding='utf-8'))
    recs = payload['records']
    register = load_register()
    projects = merge_projects(register, register_projects_from_sources())

    hays = {r['rank']: haystack(r) for r in recs}
    members = defaultdict(list)                       # project id -> ranks
    for p in projects:
        for r in recs:
            if matches(p, r, hays[r['rank']]):
                members[p['id']].append(r['rank'])

    by_rank = {r['rank']: r for r in recs}
    out_projects = []
    assigned = Counter()
    for p in projects:
        ranks = sorted(set(members[p['id']]))
        if not ranks:
            continue
        rows = []
        for rank in ranks:
            r = by_rank[rank]
            role = role_for(r, p)
            assigned[rank] += 1
            rows.append({
                'rank': r['rank'], 'url': r['url'], 'host': r['host'], 'title': r.get('title') or '',
                'category': r['category'], 'tier': r['tier'], 'status': r['status'],
                'score': r['score'], 'date': r.get('date') or '', 'role': role,
                'flags': r.get('flags') or [], 'notes': (r.get('notes') or '')[:400],
            })
        order = {k: i for i, k in enumerate(ROLE_ORDER)}
        rows.sort(key=lambda x: (order.get(x['role'], 99), -x['score'], x['host']))
        role_ct = Counter(x['role'] for x in rows)
        tier_ct = Counter(x['tier'] for x in rows)
        best = max(x['score'] for x in rows)
        out_projects.append({
            'id': p['id'], 'name': p['name'], 'kind': p['kind'], 'year': p['year'],
            'artist_role': p['artist_role'], 'summary': p['summary'], 'anchor': p['anchor'],
            'source': p['source'], 'links': rows, 'link_count': len(rows),
            'role_counts': {k: role_ct.get(k, 0) for k in ROLE_ORDER if role_ct.get(k, 0)},
            'tier_counts': {t: tier_ct.get(t, 0) for t in ('A', 'B', 'C', 'D') if tier_ct.get(t, 0)},
            'live': sum(1 for x in rows if x['status'] in ('verified', 'live', 'search-index verified')),
            'quarantined': role_ct.get('quarantine', 0),
            'best_score': best,
        })

    # reading order for the PDF: big, strong projects first; then the small ones
    out_projects.sort(key=lambda pr: (-len(pr['role_counts']), -pr['link_count'] - (pr['best_score'] / 40.0),
                                      pr['name'].lower()))
    multi = [pr for pr in out_projects if pr['link_count'] > 1]
    single = [pr for pr in out_projects if pr['link_count'] == 1]
    unassigned = [r['rank'] for r in recs if not assigned[r['rank']]]
    shared = sorted([r for r, n in assigned.items() if n > 1])

    return {
        'generated': payload.get('generated_from_repo_date'),
        'counts': {
            'records': len(recs),
            'projects_defined': len(projects),
            'projects_matched': len(out_projects),
            'multi_link_projects': len(multi),
            'single_link_projects': len(single),
            'links_in_multi_link_projects': sum(pr['link_count'] for pr in multi),
            'links_in_single_link_projects': len(single),
            'unassigned_links': len(unassigned),
            'links_in_several_projects': len(shared),
            'quarantined_in_projects': sum(pr['quarantined'] for pr in out_projects),
        },
        'roles': [{'key': k, 'label': l, 'colour': c, 'blurb': b} for k, l, c, b in ROLES],
        'projects': out_projects,
        'multi_link_projects': multi,
        'single_link_projects': single,
        'unassigned_ranks': unassigned,
        'shared_ranks': shared,
    }


# --------------------------------------------------------------------------- output
def write_outputs(data):
    os.makedirs(DATA, exist_ok=True)
    with open(OUT_JSON, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['project_id', 'project', 'kind', 'year', 'artist_role', 'links', 'role',
                    'rank', 'host', 'tier', 'cred', 'status', 'category', 'title', 'url'])
        for pr in data['projects']:
            for lk in pr['links']:
                w.writerow([pr['id'], pr['name'], pr['kind'], pr['year'], pr['artist_role'],
                            pr['link_count'], lk['role'], lk['rank'], lk['host'], lk['tier'],
                            lk['score'], lk['status'], lk['category'], lk['title'], lk['url']])
    return data


def report(data):
    """Curation QA: what matched, what is still loose, which multi-link hosts remain unclaimed."""
    c = data['counts']
    print(f"projects defined      : {c['projects_defined']}")
    print(f"projects with links   : {c['projects_matched']}  "
          f"({c['multi_link_projects']} multi-link · {c['single_link_projects']} single-link)")
    print(f"links in projects     : {c['links_in_multi_link_projects']} in multi-link projects · "
          f"{c['links_in_single_link_projects']} in single-link projects")
    print(f"links with no project : {c['unassigned_links']}")
    print(f"links in >1 project   : {c['links_in_several_projects']}")
    print(f"quarantined in project: {c['quarantined_in_projects']}")
    print()
    print('--- multi-link projects (PDF sections) ---')
    for pr in data['multi_link_projects']:
        roles = ' '.join(f'{k[:4]}:{v}' for k, v in pr['role_counts'].items())
        print(f"{pr['link_count']:>4}  {pr['name'][:58]:<58} [{pr['kind'][:22]:<22}] {roles}")
    print()
    print('--- single-link projects ---')
    for pr in data['single_link_projects']:
        print(f"   1  {pr['name'][:70]:<70} {pr['links'][0]['host']}")
    # unclaimed multi-link hosts: the curation backlog
    by_host = defaultdict(list)
    payload = json.load(open(DIRECTORY, encoding='utf-8'))
    for r in payload['records']:
        by_host[r['host']].append(r)
    loose = [(h, rs) for h, rs in by_host.items() if len(rs) > 1
             and not any(lk['host'] == h for pr in data['projects'] for lk in pr['links'])]
    loose.sort(key=lambda kv: -len(kv[1]))
    print()
    print(f'--- hosts with 2+ links still outside every project ({len(loose)}) ---')
    for h, rs in loose[:40]:
        print(f"{len(rs):>4}  {h[:44]:<44} e.g. {rs[0]['title'][:60] or rs[0]['url'][:60]}")


def main():
    ap = argparse.ArgumentParser(description='Cluster the census into project sections.')
    ap.add_argument('--report', action='store_true', help='print the curation QA report after building')
    args = ap.parse_args()
    data = build_projects()
    write_outputs(data)
    print(f"wrote {os.path.relpath(OUT_JSON, BASE)} and {os.path.relpath(OUT_CSV, BASE)} · "
          f"{data['counts']['multi_link_projects']} multi-link projects · "
          f"{data['counts']['links_in_multi_link_projects']} links organised · "
          f"{data['counts']['unassigned_links']} links unassigned")
    if args.report:
        print()
        report(data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
