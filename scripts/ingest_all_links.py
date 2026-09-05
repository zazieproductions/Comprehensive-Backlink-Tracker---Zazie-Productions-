#!/usr/bin/env python3
"""Consolidate EVERY public-web link held anywhere in this repository into one normalized record set.

Output: `data/master/consolidated_directory.json` (consumed by `scripts/build_master_directory_pdf.py`).

Sources ingested
  data/master/master_index.csv                              curated master (544 rows, authoritative)
  Zazie_Media_Master (1).pdf                                133 verified URL-level records (+leads), structured rows
  Random Zazie Productions links .pdf                       raw link dump (annotations + text lines)
  Zazie_2026_Accomplishment_Register_Maximal_Edition.docx   docx relationship hyperlinks
  data/master/listen_links.csv / LISTEN_LINKS.md            one listen link per compilation appearance
  data/master/REGISTER_LINK_MAP.md                          register entry -> public link map
  registry/**.csv                                           feature directory, low-trust ledger, regional pass, expansion
  registry/**.md                                            seed index, phase-3, magazine/zine, blind spots, register map
  "aximum-Depth Research Pass"                              maximum-depth research report

Usage:  python3 scripts/ingest_all_links.py
"""
import csv
import glob
import json
import os
import re
import sys
import zipfile
from collections import Counter

try:
    import pymupdf
except Exception:
    pymupdf = None

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'data', 'master', 'consolidated_directory.json')

SPAM = 'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust'

CANON_CATS = ['Press & Editorial', 'Film, Festivals & Exhibitions', 'Publications & Recognition',
              'Profiles & Catalogs', 'Streaming & Music Platforms', 'Music Compilations',
              'Official Properties & Channels', 'Podcasts & Broadcasts',
              'Community, Wiki & Fan Indexes', 'Music Discography', 'Lyrics & Music Databases',
              'Video Mirror / Backlink Sites', 'Search-Engine Index', SPAM]

CAT_SYNONYMS = {
    'Expert commentary': 'Press & Editorial', 'Expert commentary / industry report': 'Press & Editorial',
    'Feature article / review': 'Press & Editorial', 'Review': 'Press & Editorial',
    'Profile / feature': 'Press & Editorial', 'Press / Editorial': 'Press & Editorial',
    'Directories & Databases': 'Profiles & Catalogs', 'Profiles, Catalogs & Directories': 'Profiles & Catalogs',
    'Film / Festival / Exhibition': 'Film, Festivals & Exhibitions', 'Award / Recognition': 'Publications & Recognition',
}

RULES = [
    (re.compile(r'bandcamp\.com|soundcloud\.com', re.I), 'Music Compilations'),
    (re.compile(r'spotify|music\.apple|apple\.com/music|deezer|tidal|qobuz|anghami|boomplay|shazam|iheart|kkbox|'
                r'last\.fm|viberate|beatport|musicbrainz|soundclick|musicgateway|163\.com|kkbox', re.I),
     'Streaming & Music Platforms'),
    (re.compile(r'filmfreeway|imdb\.com|themoviedb|expcinema|cyberneticfutures|canyoncinema|film-makerscoop|'
                r'visualcontainer|pebblesunderground|artspace|gallery|kunstmatrix|arthive|artrabbit|festival|biennale', re.I),
     'Film, Festivals & Exhibitions'),
    (re.compile(r'github\.com|github\.io|hackaday|replit|websim|\.itch\.io|itch\.io|patreon|gumroad', re.I),
     'Official Properties & Channels'),
    (re.compile(r'fandom\.com|wiki|tvtropes|icebergcharts|quotev|tiermaker|reddit|spacehey|bsky|mastodon|tumblr|'
                r'tiktok|x\.com|twitter|imgur|pastebin|justpaste|anotepad|perchance|scrapbox|hackmd|saidit|commie', re.I),
     'Community, Wiki & Fan Indexes'),
    (re.compile(r'podcast|listennotes|ivoox|podbean|tunein|player\.fm|anchor\.fm|podfollow', re.I), 'Podcasts & Broadcasts'),
    (re.compile(r'youtube|youtu\.be|dai\.ly|deturl|clipzag|yewtu|viewsync|vtomb|youplay|nimlinks|canal50|stb\.hu|'
                r'hribi\.net|etvplayvideos|clipzui|heartvod|fooyoh|salda\.ws|nsfwyoutube|youtuberepeater', re.I),
     'Video Mirror / Backlink Sites'),
]

# Quarantine host list — every host here is taken from the repo's own low-trust register
# (`registry/spam_scraper_syndication_lowtrust_2026-09-05/lowtrust_ledger.csv`), which is the
# project's authoritative definition of the bucket, plus the mirror/pirate/doorway hosts the
# master CSV already carries with trust_tier D. Nothing is guessed here.
# --------------------------------------------------------------------------- helpers
STRIP_MARK = set('`<>/[](){}"\'.*|~')


def clean_url(u):
    if not u:
        return ''
    u = str(u).strip()
    u = re.sub(r'</?code>.*$', '', u)
    u = re.sub(r'</?a>.*$', '', u)
    u = u.replace('\\', '')
    while u and u[-1] in STRIP_MARK:
        u = u[:-1]
    u = re.sub(r'\.{3}$', '', u)
    u = u.replace('…', '').replace('&amp;', '&')
    return u.strip()


def norm(u):
    x = clean_url(u)
    x = re.sub(r'^https?://', '', x, flags=re.I)
    x = re.sub(r'^m\.', '', x)
    x = re.sub(r'^www\.', '', x, flags=re.I)
    return x.rstrip('/').lower()


def host_of(u):
    x = re.sub(r'^https?://', '', clean_url(u), flags=re.I)
    return x.split('/')[0].split('?')[0].lower().replace('www.', '', 1)


ENGINE_HOSTS = re.compile(
    r'^(?:(?:google|bing|duckduckgo|mojeek|marginalia|yandex|baidu|sogou|seznam|ecosia|startpage|qwant|brave|'
    r'presearch|metager|infoseek|rediff|goo|naver|daum|wykop|mwmbl|retrieva|openkatalog|find|excite|lycos|ask|so)'
    r'\.[a-z.]{2,7}|search\.[a-z0-9.-]+|searx\.[a-z.]+|opnxng\.com|baresearch\.org|search\.inetol\.net|'
    r'yep\.com|wiby\.me|boardreader\.com|index\.commoncrawl\.org|timetravel\.mementoweb\.org|archive\.ph|'
    r'trove\.nla\.gov\.au|marginalia\.nu|spikeart\.eu|searchresults\.org|pm\.me|yacy\.searchlab\.eu|'
    r'www3\.neva\.ru|coccoc\.com|archive\.org/advancedsearch)$', re.I)


def is_engine_or_tooling(u):
    """Search endpoints, API probes and archive-lookup URLs are method artefacts, not media records."""
    h = host_of(u)
    path = re.sub(r'^https?://', '', u)
    if ENGINE_HOSTS.match(h):
        return True
    if re.search(r'(advancedsearch\.php|/cdx/search/cdx|/api/|^api\.|/search\?|\?s=|\?q=|\?query=|\?wd=|\?text=|\?name=|/link/url=)',
                 path, re.I):
        return True
    if 'web.archive.org/web/' in u and '*/' in u:
        return True
    return False


LEDGER = os.path.join(BASE, 'registry', 'spam_scraper_syndication_lowtrust_2026-09-05', 'lowtrust_ledger.csv')
SPAM_URL_SET = set()        # exact URLs the project's own quarantine register marked D
SPAM_HOST_WIDE = set()      # whole-domain quarantine (hacked doorways, mirror farms)
WIDE_SUBTYPES = ('DOORWAY-INJECT', 'TOOL-MIRROR', 'INJECTED-EMBED', 'TYPOSQUAT-MIRROR',
                 'SUSPICIOUS-MIRROR', 'SPAM-SHOP', 'PIRATE-SCRAPE', 'UNKNOWN-MIRROR', 'LEGACY-MIRROR')
HOST_SUBTYPES = {}
if os.path.exists(LEDGER):
    with open(LEDGER, encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            h = (r.get('Host') or '').strip().lower().replace('www.', '')
            u = norm(r.get('URL') or '')
            if (r.get('TrustTier') or '').strip().upper() == 'D' and u:
                SPAM_URL_SET.add(u)
            HOST_SUBTYPES.setdefault(h, set()).add((r.get('Subtype') or '').strip())
    for h, subs in HOST_SUBTYPES.items():
        if subs and subs <= set(WIDE_SUBTYPES):
            SPAM_HOST_WIDE.add(h)


def quarantined(r):
    """True when the repository's own low-trust register (or the curated master) marks this exact
    URL, or when the whole domain is a known doorway/mirror farm."""
    if r['url'] and norm(r['url']) in SPAM_URL_SET:
        return True
    h = r['host']
    if h in SPAM_HOST_WIDE or any(h == w or h.endswith('.' + w) for w in SPAM_HOST_WIDE):
        return True
    return False


# --------------------------------------------------------------------------- credibility overlay
# Integrity flags taken from the repository's own research passes, so the PDF never invents
# judgements: each flag states what the evidence actually is (a PR wire repost, a wiki mirror,
# an embed farm, a hacked-site doorway ...) and how far it moves the credibility score.
FLAG_RULES = [
    ('PAY-TO-PLAY PR WIRE', re.compile(r'(prfree\.org|pronthego\.com|musicalive\.net|prnewswire|openpr|einpresswire|24-7pressrelease)', re.I),
     'self-issued press-release distribution, not independent editorial', -24),
    ('SELF-PUBLISHED PROPERTY', re.compile(r'(^|\.)(zazieproductions\.|zazieproduction\.)|linktr\.ee|churchofmalware|witch-house\.com|bario\.icu|yyyyyyy\.info|horror\.zazieproductions', re.I),
     'artist- or collective-owned surface: proves existence, not third-party recognition', -10),
    ('UNOFFICIAL FILM MIRROR', re.compile(r'(frenchstream\.tv|justwatch-hd|hdfilmcehennemi|openfilmzone|filmacorn|moview\.|pelis-api|thomas-spinec\.students|newtv\.co\.th|tvonlayn|stb\.hu|video\.link)', re.I),
     'scraper/streamer replica of the same TMDB or festival record - not a separate placement', -30),
    ('WIKI MIRROR', re.compile(r'(wiki2\.org|wikimili|wikiwand|wikigit|breezewiki|outsider\.fandom)', re.I),
     'machine mirror of a Wikipedia list page - the underlying record is the Wikipedia article', -18),
    ('EMBED / BACKLINK FARM', re.compile(r'(nimlinks|etvplayvideos|youplay|nimtools|vtomb|hribi\.net|clipzag|clipzui|deturl|yewtu|viewsync|youtuberepeater|youtubu|ytrepeat|youtube-nocookie|canal50|heartvod|fooyoh|salda\.ws|nsfwyoutube|listenonrepeat|socialcounts|gazetaolsztynska|pakvim|polsy\.org\.uk|culturevein|topsheetmusic|musiclessons)', re.I),
     'proxy player built to farm a backlink to one video', -36),
    ('PASTE / SELF-SERVE HOSTING', re.compile(r'(anotepad|justpaste|txt\.fyi|hackmd|scrapbox|writexo|perchance|websim|replit|telegra\.ph|medium\.com|write\.as|vocal\.media|imgur|commie\.io|saidit\.net|xoyondo|paste2| notion)', re.I),
     'anonymous paste or self-serve page: provenance not established', -16),
    ('AUTO-GENERATED METADATA', re.compile(r'(hitplayer|chosic|gnoosic|songdata|sonichits|soundgasm|playlost|paroles-musique|zvu4no|gequbao|fangpi|musicstax|getmusic|muzvibe|x-minusovka|ligaudio|breakinghits|viberate|boomplay|163\.com|kkbox|anghami|douyin|ok\.ru|thirdeyemusic|lyricsplayground|muso\.ai)', re.I),
     'algorithmically built artist/metadata page, not curated coverage', -16),
    ('SEO DOORWAY ON HIJACKED SITE', re.compile(r'(black-mountain-college-ira|ira-and-ruth-levinson|/gDrA/|/zvgw5/|/KmDEB/|/PxyL/|/MNNiI/|/ac-valhalla/|/fs0vz3/|persuasive-speech/|love-quotes/|/4o5ct9/|bidirectional-lstm|\.modules/)', re.I),
     'injected doorway on a compromised, unrelated site using the artist name as bait', -42),
    ('USER-GENERATED LIST / QUIZ / CHART', re.compile(r'(quotev|tiermaker|icebergcharts|coolmindmaps|isitagoodplaylist|urbanpoll|purwana|sequencer\.party|spacehey|tvtropes|senscritique)', re.I),
     'community-made list, quiz or chart: mentions rather than journalism', -10),
    ('SOCIAL / FORUM MENTION', re.compile(r'(reddit\.com|stevehoffman|mastodon|bsky|tumblr|facebook\.com|instagram\.com|x\.com|twitter\.com|tiktok\.com)', re.I),
     'social or forum mention - reach without editorial review', -6),
    ('ARCHIVE SNAPSHOT', re.compile(r'(web\.archive\.org|archive\.ph|mementoweb|commoncrawl|timetravel)', re.I),
     'archival snapshot of a primary record, not an independent placement', -8),
    ('PAY-TO-PLAY CREDS MERCHANT', re.compile(r'(media-match\.com|reverbnation|breakinghits|viberate|slaps\.com|theresanaiforthat|promptbase|opensea|mailmodo)', re.I),
     'paid listing / cred-marketing platform - listing is purchased, not editorially awarded', -14),
    ('SCRAPE / MIRRORED MUSIC DATABASE', re.compile(r'(metal-tracker|theresanaiforthat|promptbase|opensea|grayswan|mailmodo|wiby)', re.I),
     'auto-mirrored database entry or AI-listing clone', -12),
]


def apply_flags(r):
    flags, reasons, adj = [], [], 0
    hay = r['url'] + ' ' + r['title'] + ' ' + r['notes']
    for name, rx, why, delta in FLAG_RULES:
        if rx.search(hay) and name not in flags:
            flags.append(name)
            reasons.append(f'{name} - {why}')
            adj += delta
    r['flags'] = flags
    r['flag_reasons'] = reasons
    r['flag_adj'] = adj


LOWTRUST_MARK = re.compile(r'(LOWTRUST|SEO-POISON|DOORWAY|SCRAPE-CLONE|PARASITE|PIRATE|AUTO-GENER|'
                           r'FABRICATED|SPAM|HIJACK|SYNDICAT)', re.I)

# --------------------------------------------------------------------------- store
SRC_PRIORITY = {          # whose characterisation of a URL wins
    'master_index': 5,
    'media_master_pdf': 4,
    'registry/spam_scraper_syndication_lowtrust_2026-09-05/lowtrust_ledger.csv': 4,
    'registry/magazine_zine_features/feature_directory.csv': 4,
    'link_dump_pdf': 3,
    'accomplishment_register_docx': 3,
}


def prio(source):
    return SRC_PRIORITY.get(source, 2)


class Store:
    """Dedupe by normalized URL; keep the highest-priority value for each field."""

    def __init__(self):
        self.rec = {}
        self.engine = {}

    def add(self, url, source, **fields):
        url = clean_url(url)
        if not re.match(r'^https?://[^\s]+\.[a-z]{2,}', url, re.I):
            return None
        key = norm(url)
        if len(key) < 6:
            return None
        if is_engine_or_tooling(url) and source != 'master_index':
            e = self.engine.setdefault(key, {'url': url, 'host': host_of(url), 'sources': {}})
            e['sources'][source] = max(prio(source), e['sources'].get(source, 0))
            return None
        r = self.rec.get(key)
        if r is None:
            r = {'url': url, 'norm': key, 'host': host_of(url), 'sources': {}, '_p': {},
                 'target': '', 'category': '', 'tier': '', 'status': '', 'date': '',
                 'title': '', 'notes': '', 'primary': False}
            self.rec[key] = r
        p = prio(source)
        r['sources'][source] = max(p, r['sources'].get(source, 0))
        if source == 'master_index':
            r['primary'] = True
        TIER_ORDER = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
        STATUS_RANK = {'verified': 6, 'live': 6, 'search-index verified': 5, 'verified-partial': 4,
                       'partial': 3, 'lead': 2, 'unverified': 1, 'not-probed-safety': 0, 'broken': 0}
        for k, v in fields.items():
            v = ('' if v is None else str(v)).strip()
            if not v:
                continue
            cur_p = r['_p'].get(k, 0)
            if k == 'notes':
                if v not in r['notes'] and len(v) > 12:
                    r['notes'] = (r['notes'] + '  ·  ' + v).strip(' ·')[:1500]
                continue
            if p < cur_p:
                continue                                  # a better source already spoke
            if k == 'tier':
                t = v[:1].upper()
                if t in TIER_ORDER and (not r['tier'] or p > cur_p or TIER_ORDER[t] > TIER_ORDER.get(r['tier'], 0)):
                    r['tier'] = t
                    r['_p'][k] = p
            elif k == 'status':
                if not r['status'] or STATUS_RANK.get(v, -1) > STATUS_RANK.get(r['status'], -1) or p > cur_p:
                    r['status'] = v
                    r['_p'][k] = p
            elif k == 'category':
                v2 = CAT_SYNONYMS.get(v, v)
                if v2 in CANON_CATS and not r['category']:
                    r['category'] = v2
                    r['_p'][k] = p
            elif not r.get(k):
                r[k] = v[:700]
                r['_p'][k] = p
            elif p > cur_p and k in ('title', 'date', 'target'):
                r[k] = v[:700]
                r['_p'][k] = p
        return r

    def rows(self):
        return list(self.rec.values())


store = Store()
URL_RE = re.compile(r'https?://[^\s<>"\')\]]+', re.I)


# --------------------------------------------------------------------------- 1. curated master
with open(os.path.join(BASE, 'data', 'master', 'master_index.csv'), encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        store.add(r['url'], 'master_index', target=r.get('target'), category=r.get('category'),
                  tier=r.get('trust_tier'), status=r.get('status'), date=r.get('date'),
                  title=r.get('title'), notes=r.get('notes'))


# --------------------------------------------------------------------------- 2. generic harvesters
def harvest_md(path, label):
    if not os.path.exists(path):
        return
    for line in open(path, encoding='utf-8', errors='replace').read().split('\n'):
        urls = URL_RE.findall(line)
        if not urls:
            continue
        low = line.lower()
        tier = ''
        for pat, val in (('🥇', 'A'), ('tier a', 'A'), ('priority a', 'A'), ('🥈', 'B'), ('tier b', 'B'),
                         ('priority b', 'B'), ('🥉', 'C'), ('tier c', 'C'), ('priority c', 'C'),
                         ('🖤', 'D'), ('tier d', 'D')):
            if pat in low:
                tier = val
                break
        status = ''
        for pat, val in (('✅', 'verified'), ('live verified', 'verified'), ('verified-live', 'verified'),
                         ('search-index verified', 'search-index verified'), ('🟡', 'partial'),
                         ('❌', 'broken'), ('⬜', 'unverified'), ('🔎', 'lead')):
            if pat in low:
                status = val
                break
        cat = ''
        for pat, val in (('🔴', 'Press & Editorial'), ('🌸', 'Film, Festivals & Exhibitions'),
                         ('🟣', 'Publications & Recognition'), ('🔵', 'Profiles & Catalogs'),
                         ('🟠', 'Music Compilations'), ('🩵', 'Search-Engine Index'),
                         ('🟢', 'Community, Wiki & Fan Indexes'), ('📼', 'Video Mirror / Backlink Sites'),
                         ('🖤', SPAM)):
            if pat in low:
                cat = val
                break
        cells = [c.strip() for c in line.strip().strip('|').split('|')] if line.strip().startswith('|') else []
        plain = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', line)
        plain = re.sub(r'https?://\S+', '', plain)
        plain = re.sub(r'[`*|]', '', plain).strip()
        for u in urls:
            store.add(u, label, tier=tier, status=status, category=cat,
                      notes=(plain[:340] if len(plain) > 8 else ''),
                      title=(cells[1][:240] if len(cells) > 3 and not cells[1].lower().startswith('http')
                             and re.search(r'[A-Za-z]{4}', cells[1]) else ''))


def harvest_csv(path, label):
    if not os.path.exists(path):
        return
    with open(path, encoding='utf-8', errors='replace') as fh:
        for r in csv.DictReader(fh):
            def g(*keys):
                for k in keys:
                    v = r.get(k)
                    if isinstance(v, list):
                        v = ' '.join(str(x) for x in v if x)
                    if v and str(v).strip():
                        return str(v).strip()
                return ''
            t = g('TrustTier', 'Tier', 'trust_tier')
            tier = (re.search(r'\b([ABCD])\b', t).group(1) if re.search(r'\b([ABCD])\b', t) else '')
            title = g('FeatureTitle', 'DisplayedTitle', 'Publication', 'title', 'Compilation', 'summary', 'Item')
            notes = ' · '.join(filter(None, [
                g('Notes'), g('EvidenceExcerpt')[:200], g('WhyQualifies')[:200], g('VerificationStatus'),
                g('LiveStatus', 'LiveStatus_2026-09-05', 'status'), g('best_use'), g('Subtype'), g('Cluster')]))[:500]
            live = (g('LiveStatus', 'LiveStatus_2026-09-05', 'VerificationStatus', 'status')).lower()
            status = ('verified' if ('verified' in live or 'live' in live.split(' ')[0:1]) else
                      'partial' if 'partial' in live else
                      'broken' if 'broken' in live else
                      'not-probed-safety' if 'not-probed' in live else '')
            for col in ('URL', 'url', 'ResultURL', 'CanonicalURL', 'Link', 'link', 'listen_url',
                        'url_or_asset', 'ArchiveLink', 'discogs', 'DuplicateURLs', 'backlink'):
                v = g(col)
                if not v:
                    continue
                for u in re.findall(r'https?://[^\s,;"\']+', v):
                    store.add(u, label, tier=tier, title=title[:240],
                              category=g('MasterCategory', 'ProposedCategory', 'Category'),
                              target=g('Target', 'TargetPhrase', 'target'), status=status,
                              date=g('Date', 'DateSearched', 'year', 'date')[:24], notes=notes)


for f in sorted(glob.glob(os.path.join(BASE, 'registry', '**', '*.csv'), recursive=True)):
    harvest_csv(f, os.path.relpath(f, BASE))
for f in sorted(glob.glob(os.path.join(BASE, 'data', '**', '*.csv'), recursive=True)):
    harvest_csv(f, os.path.relpath(f, BASE))
for f in (sorted(glob.glob(os.path.join(BASE, 'registry', '**', '*.md'), recursive=True))
          + sorted(glob.glob(os.path.join(BASE, 'data', '**', '*.md'), recursive=True))
          + [os.path.join(BASE, 'aximum-Depth Research Pass')]):
    harvest_md(f, os.path.relpath(f, BASE))


# --------------------------------------------------------------------------- 3. docx hyperlinks
DOCX = os.path.join(BASE, 'Zazie_2026_Accomplishment_Register_Maximal_Edition.docx')
if os.path.exists(DOCX):
    try:
        z = zipfile.ZipFile(DOCX)
        rels = z.read('word/_rels/document.xml.rels').decode('utf8', 'replace')
        for u in re.findall(r'Target="(https?://[^"]+)"', rels):
            store.add(u, 'accomplishment_register_docx',
                      notes='hyperlink inside the 2026 Accomplishment Register (docx relationship table)')
    except Exception as e:
        print('docx warn', e, file=sys.stderr)


# --------------------------------------------------------------------------- 4. source PDFs
def harvest_pdf(path, label):
    if not (pymupdf and os.path.exists(path)):
        return
    d = pymupdf.open(path)
    for page in d:
        links = [l for l in (page.get_links() or []) if l.get('uri')]
        words = page.get_text('words')
        for l in links:
            u = clean_url(l['uri'])
            if not u:
                continue
            r = pymupdf.Rect(l['from'])
            near = [w[4] for w in words if abs((w[1] + w[3]) / 2 - (r.y0 + r.y1) / 2) < 40]
            ctx = re.sub(r'\s+', ' ', ' '.join(near)).replace('OPEN', ' ').strip()
            store.add(u, label, notes=ctx[:300])
        raw = [ln.strip() for ln in page.get_text().split('\n')]
        lines = []
        for ln in raw:                                  # rejoin PDF line-wrapped URLs
            if lines and lines[-1].endswith('-') and re.match(r'https?://', lines[-1]) and ln and ' ' not in ln:
                lines[-1] = lines[-1][:-1] + ln
            else:
                lines.append(ln)
        for i, ln in enumerate(lines):
            for u in re.findall(r'https?://\S+', ln):
                nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
                tail = nxt if (nxt and not re.match(r'https?://', nxt) and 6 < len(nxt) < 220) else ''
                store.add(u, label, title=tail[:200])


harvest_pdf(os.path.join(BASE, 'Random Zazie Productions links .pdf'), 'link_dump_pdf')
harvest_pdf(os.path.join(BASE, 'Zazie_Media_Master (1).pdf'), 'media_master_pdf')

# Media Master structured rows: Priority / Date / Publication / Title / Exact-name field
if pymupdf and os.path.exists(os.path.join(BASE, 'Zazie_Media_Master (1).pdf')):
    d = pymupdf.open(os.path.join(BASE, 'Zazie_Media_Master (1).pdf'))
    for page in d:
        try:
            tables = page.find_tables().tables
        except Exception:
            continue
        links = [l for l in (page.get_links() or []) if l.get('uri')]
        for t in tables:
            for ri, row in enumerate(t.extract()):
                y0, y1 = t.rows[ri].bbox[1], t.rows[ri].bbox[3]
                urls = [clean_url(l['uri']) for l in links
                        if y0 - 2 <= (pymupdf.Rect(l['from']).y0 + pymupdf.Rect(l['from']).y1) / 2 <= y1 + 2]
                urls = [u for u in urls if u]
                if not urls:
                    continue
                cells = [re.sub(r'\s*\|\s*', ' — ', (c or '').replace('\n', ' ').strip()) for c in row]
                cells = [c for c in cells if c and c.upper() != 'OPEN']
                tier = cells[0].strip()[-1:].upper() if cells and re.fullmatch(r'(Priority )?[ABCD]', cells[0].strip()) else ''
                date = ''
                for c in cells:
                    if re.fullmatch(r'\d{4}(-\d{2}(-\d{2})?)?|Unknown|n\.d\.', c.strip()):
                        date = c.strip()
                        break
                rest = [c for c in cells if c != date]
                pub = title = exact = ''
                if len(rest) >= 4:
                    pub, title, exact = rest[1], rest[2], rest[3]
                elif len(rest) == 3:
                    pub, title, exact = rest
                elif len(rest) == 2:
                    pub, title = rest
                for u in urls:
                    store.add(u, 'media_master_pdf', tier=tier, date=date, title=title[:280] or pub[:200],
                              notes=(f'Media Master record — publication: {pub[:120]}'
                                      + (f' — exact name: {exact[:110]}' if exact else '')))


# --------------------------------------------------------------------------- 5. collapse truncation artefacts
keys_by_len = sorted(store.rec, key=len, reverse=True)
longer_keys = [k for k in keys_by_len if len(k) > 24]
drop = {}
for k in keys_by_len:
    if len(k) <= 24 or k in drop:
        continue
    if store.rec[k]['primary']:
        continue                       # curated master rows are never swallowed
    for L in longer_keys:
        if len(L) <= len(k) or not L.startswith(k):
            continue
        if L[len(k)] == '/':
            break                      # k is a real parent/root page, keep both
        drop[k] = L
        break
for k, L in drop.items():
    if k not in store.rec:
        continue
    src = store.rec.pop(k)
    tgt = store.rec[L]
    for kk, pp in src['sources'].items():
        tgt['sources'][kk] = max(pp, tgt['sources'].get(kk, 0))
    tgt['primary'] = tgt['primary'] or src['primary']
    if len(src['notes']) > len(tgt['notes']):
        tgt['notes'] = src['notes'][:1400]
    for f in ('title', 'category', 'date', 'target', 'tier', 'status'):
        if not tgt.get(f) and src.get(f):
            tgt[f] = src[f]


# --------------------------------------------------------------------------- 6. classify
HOST_CATEGORY = {}
for r in store.rows():
    if r['category'] and r['host'] not in HOST_CATEGORY:
        HOST_CATEGORY[r['host']] = r['category']


def classify(r):
    cat = CAT_SYNONYMS.get(r['category'], r['category'])
    if cat not in CANON_CATS:
        cat = CAT_SYNONYMS.get(HOST_CATEGORY.get(r['host'], ''), HOST_CATEGORY.get(r['host'], ''))
    if cat not in CANON_CATS:
        for rx, name in RULES:
            if rx.search(r['host']):
                cat = name
                break
    if cat not in CANON_CATS:
        path = re.sub(r'^https?://', '', r['url'])
        for rx, name in RULES:
            if rx.search(path):
                cat = name
                break
    if cat not in CANON_CATS:
        cat = 'Profiles & Catalogs'
    # quarantine: the register's own row, the curated master's D tier, or a verbatim LOWTRUST tag
    if quarantined(r) or r['tier'] == 'D' or LOWTRUST_MARK.search(r['notes'][:200]):
        cat = SPAM
    if cat == SPAM:
        r['tier'] = 'D'
    elif not r['tier']:
        r['tier'] = 'C'
    r['category'] = cat
    if not r['status']:
        r['status'] = 'unverified'
    if not r['target']:
        s = r['url'].lower().replace('-', ' ').replace('_', ' ') + ' ' + r['title'].lower()
        r['target'] = ('Zazie Kanwar-Torge' if 'kanwar' in s else
                       'Zazie Productions' if 'zazie productions' in s or 'zazieproductions' in s else
                       'Zazie Productions (contextual)')
    return r


for r in store.rows():
    classify(r)

# --------------------------------------------------------------------------- 7. topics
TOPICS = [
    ('Award-winning film & festival recognition', re.compile(r'phantom requiem|festival|award|jury|screening|film|pebbles|biennale|exhibition|selection', re.I)),
    ('Major press features & interviews', re.compile(r'magazine|interview|profile|billboard|grammy|heavy|press|feature|review|coverage|journal|webzine', re.I)),
    ('Institutional, academic & museum records', re.compile(r'college|museum|pulitzer|universit|academia|archive\.org|institute|library|jstor', re.I)),
    ('Cybersecurity, AI & technical credits', re.compile(r'security|vulnerab|apple|hackaday|malware|codex|researcher|emulator|software|github', re.I)),
    ('Literary, poetry & anthology publications', re.compile(r'poem|poetry|antholog|zine|literary|subtext|review|quotev|allpoetry|lulu|press', re.I)),
    ('Bandcamp & netlabel compilation credits', re.compile(r'bandcamp|netlabel|compilation|split|vinyl|tape', re.I)),
    ('Streaming-platform & catalogue records', re.compile(r'spotify|apple|deezer|tidal|amazon|shazam|qobuz|last\.fm|discogs|musicbrainz|rateyourmusic|lyrics|soundclick|beatport', re.I)),
    ('Official artist channels & storefronts', re.compile(r'zazieproductions|linktr|patreon|gumroad|itch\.io|youtube\.com/@', re.I)),
    ('Radio, podcast & broadcast appearances', re.compile(r'podcast|radio|broadcast|listennotes|tunein|ivoox|cjsw|episode', re.I)),
    ('Community, wiki & fan-curated pages', re.compile(r'wiki|fandom|tvtropes|reddit|quotev|tiermaker|iceberg|chart|forum|blog|spacehey|bsky|mastodon|tumblr|tiktok', re.I)),
    ('Profile, directory & industry listings', re.compile(r'profile|directory|artist|catalog|backstage|casting|behance|imdb|linkedin| Equipboard| Reverbnation|sketchfab', re.I)),
    ('Mirrors, embeds & syndicated copies', re.compile(r'embed|mirror|watch|player|repeat|proxy', re.I)),
]


def topic_of(r):
    hay = ' '.join([r['host'], r['url'].split('/', 2)[-1].replace('-', ' ').replace('_', ' ').replace('%20', ' '),
                    r['title'], r['notes'][:300]])
    if r['category'] == SPAM:
        return 'Quarantined: scraped, syndicated & poisoned copies'
    for name, rx in TOPICS:
        if rx.search(hay):
            return name
    return 'Other verbatim web presence'


for r in store.rows():
    r['topic'] = topic_of(r)

# --------------------------------------------------------------------------- 8. credibility score
AUTH = {
    'pulitzercenter.org': 34, 'billboardwire.com': 26, 'blackmountaincollege.org': 30, 'support.apple.com': 30,
    'pro.imdb.com': 22, 'imdb.com': 21, 'themoviedb.org': 10, 'musicbrainz.org': 20, 'discogs.com': 19,
    'rateyourmusic.com': 14, 'open.spotify.com': 16, 'creators.spotify.com': 14, 'music.apple.com': 18,
    'podcasts.apple.com': 16, 'music.youtube.com': 14, 'deezer.com': 12, 'tidal.com': 12, 'qobuz.com': 12,
    'last.fm': 10, 'shazam.com': 10, 'youtube.com': 12, 'youtu.be': 4, 'vimeo.com': 10, 'soundcloud.com': 10,
    'wikipedia.org': 26, 'academia.edu': 16, 'jstor.org': 24, 'trove.nla.gov.au': 20,
    'cyberneticfutures.com': 20, 'expcinema.org': 18, 'film-makerscoop.com': 20, 'canyoncinema.com': 19,
    'connects.canyoncinema.com': 20, 'visualcontainer.tv': 17, 'pebblesunderground.art': 17,
    'newmediartspace.info': 15, 'thesqueakywheel.org': 16, 'a2b2.org': 16, 'concertarchives.org': 15,
    'grammyweekly.com': 15, 'heavymag.com.au': 17, 'limitless-magazine.com': 15, 'tinnitist.com': 14,
    'whitelight-whiteheat.com': 17, 'portlandmercury.com': 18, 'vitalentum.net': 10, 'igloomag.com': 13,
    'shockwebradio.com': 13, 'rockculture.es': 13, 'soundsgoodwebzine.com': 12, 'rangermagazine.net': 15,
    'superpresent.org': 17, 'viralnation.com': 13, 'clongclongmoo.org': 15, 'metapsychosis.com': 15,
    'thewrong.org': 17, 'indieam.com.mx': 13, 'popfantasma.com.br': 11, 'lakeivanfilmjournal.org': 16,
    'lakeivan.substack.com': 15, 'mandeliterary.com': 10, 'manicworldmagazine.com': 11, 'cjsw.com': 10,
    'thelatest.co.uk': 12, 'peopleversus.tv': 13, 'mycommunitycinema.org.uk': 14, 'casey-douglass.com': 9,
    'brokenzen.wordpress.com': 7, 'dionysianpubliclibrary.com': 12, 'linktr.ee': 6, 'patreon.com': 10,
    'gumroad.com': 8, 'amazon.com': 8, 'behance.net': 8, 'linkedin.com': 12, 'substack.com': 4,
    'lulu.com': 8, 'poetryformentalhealth.org': 10, 'bipolarpoetry.com': 12, '100subtextsmagazine.blogspot.com': 12,
    'pw.org': 20, 'duotrope.com': 14, 'goodreads.com': 8, 'eventbrite.co.uk': 4, 'upwork.com': 4,
    'gamedevmarket.net': 6, 'samplefocus.com': 8, 'opensea.io': 0, 'promptbase.com': 0, 'pixabay.com': 4,
    'enigmalabs.io': 6, 'greenville.k12.sc.us': 10, 'experiment.com': 8, 'smashwords.com': 2,
    'artfacts.net': 14, 'arthive.com': -2, 'artvee.com': 2, 'art.kunstmatrix.com': 8, 'artrabbit.com': 0,
    'castingcall.club': 6, 'backstage.com': 8, 'thetalentmanager.com': 6, 'soundbetter.com': 6,
    'stage32.com': 8, 'getheard.fm': 2, 'viberate.com': 0, 'reverbnation.com': 8, 'bandzoogle': 4,
    'kickstarter.com': 8, 'indiegogo.com': 4, 'prnewswire.com': 10, 'prfree.org': -6, 'pronthego.com': -6,
    'quotev.com': -6, 'tiermaker.com': -4, 'icebergcharts.com': -6, 'tvtropes.org': 2, 'reddit.com': 2,
    'x.com': 2, 'twitter.com': 2, 'tiktok.com': 2, 'm.douyin.com': -4, 'anotepad.com': -14,
    'justpaste.it': -12, 'telegra.ph': -10, 'perchance.org': -12, 'websim.ai': -12, 'replit.com': -8,
    'hackmd.io': -8, 'scrapbox.io': -6, 'imgur.com': -2, 'medium.com': 0, 'write.as': -2, 'vocal.media': -6,
    'hackaday.io': 12, 'github.com': 12, 'gitlab': 6, 'web.archive.org': 12, 'archive.org': 14,
    'setlist.fm': 6, 'songstats.com': 2, 'equipboard.com': 6, 'museonline.org': 8, 'creativemornings.com': 2,
    'the-dots.com': 4, 'sketchfab.com': 6, 'play.reelcrafter.com': 6, 'musicians.directory': 0,
    'bandmix.com': -8, 'groover.co': 2, 'slaps.com': -12, 'thepromptindex.com': -2, 'theresanaiforthat.com': -4,
    'metal-tracker.com': -4, 'senscritique.com': -6, 'allpoetry.com': 2, 'txt.fyi': -10, 'writexo.com': -8,
    'xn--sraphits-sraphta-bqbj3h5m.weebly.com': -18, 'wnloveet.click': -22, 'hiontech.kr': -22,
    'lu.etvplayvideos.com': -22, 'youplay.nimtools.com': -20, 'box.hitplayer.ru': -20, 'zvu4no.org': -18,
    'gequbao.com': -18, 'musicstax.com': -16, 'deturl.com': -14, 'clipzag.com': -16, 'vtomb.com': -16,
    'hribi.net': -16, 'yewtu.be': -8, 'viewsync.net': -10, 'youtuberepeater.com': -14, 'youtubu.tv': -18,
    'ytrepeat.com': -14, 'canal50.com': -16, 'stb.hu': -16, 'nsfwyoutube.com': -20, 'art-squat.com': -8,
    'commie.io': -12, 'saidit.net': -12, 'samples.eduwriter.ai': -18, 'urbanpoll.com': -14, 'xoyondo.com': -10,
    'spacehey.com': -4, 'tumblr.com': -2, 'archive.transformativeworks.org': -8, 'archive.independentmail.com': 8,
    'musicgateway.com': -12, 'muzvibe.org': -10, 'getmusic.fm': -12, 'chosic.com': -10, 'gnoosic.com': -8,
    'playlost.fm': -10, 'paroles-musique.com': -8, 'so.com': -18, '163.com': -6, 'ok.ru': -6, 'lyrics.com': 2,
    'yyyyyyy.info': -22, 'bario.icu': -18, 'mailmodo.com': -6, 'muso.ai': -6, 'grayswan.ai': -8,
    'frenchstream.tv': -22, 'justwatch-hd.com': -20, 'hdfilmcehennemi.beauty': -24, 'openfilmzone.com': -18,
    'filmacorn.vercel.app': -16, 'moview.janakoudelkova.cz': -18, 'pelis-api.vercel.app': -18,
    'media-match.com': 6, 'thomas-spinec.students-laplateforme.io': -12, 'tickettailor.com': 8,
    'allevents.in': 0, 'amazingradio.com': 6, 'cincymusic.com': 8, 'killthedj.com': 12, 'codex.churchofmalware.org': 8,
    'churchofmalware.org': 8, 'ogre.red': 10, 'filmfreeway.com': 14, 'instagram.com': 6, 'facebook.com': 4,
    'bizapedia.com': -10, 'voterrecords.com': 4, 'search.goo.ne.jp': -12, 'search.infoseek.co.jp': -12,
    'search.rediff.com': -12, 'metager.org': -12, 'archive.ph': 2, 'timetravel.mementoweb.org': 0,
    'coinoperatedpress.wordpress.com': 6, 'coinoperatedpress.bigcartel.com': 4, 'tumblr.com': -2,
}


def auth_of(r):
    h = r['host']
    for k in sorted(AUTH, key=len, reverse=True):
        if h == k or h.endswith('.' + k):
            return AUTH[k]
    if h.endswith('bandcamp.com'):
        return 9
    if h.endswith('.github.io'):
        return 2
    if h.endswith(('.blogspot.com', '.wordpress.com', '.substack.com')):
        return 3
    if re.search(r'\.(ru|cn|su|kz|top|click|xyz|fun|icu|buzz|shop|live|link|beauty|quest|site|online|space)$', h):
        return -14
    if re.search(r'\.(org|edu|gov|ac)(\.[a-z]{2})?$', h):
        return 7
    return 0


STATUS_ADJ = {'verified': 12, 'live': 12, 'search-index verified': 8, 'verified-partial': 6, 'partial': 2,
              'unverified': 0, 'lead': -4, 'not-probed-safety': -8, 'broken': -16}
TIER_ADJ = {'A': 42, 'B': 26, 'C': 10, 'D': -34}
CAT_ADJ = {'Press & Editorial': 16, 'Publications & Recognition': 14, 'Film, Festivals & Exhibitions': 10,
            'Podcasts & Broadcasts': 4, 'Profiles & Catalogs': 3, 'Music Discography': 0,
            'Lyrics & Music Databases': -3, 'Search-Engine Index': -4, 'Streaming & Music Platforms': -5,
            'Official Properties & Channels': -7, 'Music Compilations': -10,
            'Community, Wiki & Fan Indexes': -16, 'Video Mirror / Backlink Sites': -24, SPAM: -70}
NAME_ADJ = {'Zazie Kanwar-Torge': 4, 'Zazie Productions': 2}


def score(r):
    s = 46 + TIER_ADJ.get(r['tier'], 0) + CAT_ADJ.get(r['category'], 0) + auth_of(r)
    s += STATUS_ADJ.get(r['status'], 0) + NAME_ADJ.get(r['target'], 0) + r.get('flag_adj', 0)
    if len(r['notes']) > 90:
        s += 3
    if r['date']:
        s += 2
    if r['title']:
        s += 1
    return s


rows = store.rows()
for r in rows:
    apply_flags(r)
    r['raw'] = score(r)
    r['sources'] = sorted(r['sources'])
    r.pop('_p', None)
lo = min(r['raw'] for r in rows)
hi = max(r['raw'] for r in rows)
for r in rows:
    r['score'] = round(100 * (r['raw'] - lo) / (hi - lo)) if hi > lo else 50
rows.sort(key=lambda r: (-r['raw'], r['category'], r['host'], r['url']))
for i, r in enumerate(rows, 1):
    r['rank'] = i

engine_rows = sorted(store.engine.values(), key=lambda e: e['host'])
for e in engine_rows:
    e['sources'] = sorted(e['sources'])

with open(OUT, 'w', encoding='utf-8') as fh:
    json.dump({'generated_from_repo_date': '2026-09-05',
               'counts': {'records': len(rows), 'engine_endpoints': len(engine_rows)},
               'records': rows, 'engine_endpoints': engine_rows}, fh, indent=1, ensure_ascii=False)

print(f'wrote {OUT}')
print(f'{len(rows)} link records · {len(engine_rows)} engine/tooling endpoints')
print('-- categories --')
for k, v in Counter(r['category'] for r in rows).most_common():
    print(f'   {v:>4}  {k}')
print('-- tiers --', dict(Counter(r['tier'] for r in rows).most_common()))
print('-- status --', dict(Counter(r['status'] for r in rows).most_common()))
print('-- topics --')
for k, v in Counter(r['topic'] for r in rows).most_common():
    print(f'   {v:>4}  {k}')
