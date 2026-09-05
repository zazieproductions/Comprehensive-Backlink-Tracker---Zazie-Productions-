#!/usr/bin/env python3
"""Build the 2026-09-05 Spam / Scraper / Syndication / SEO-Poisoning / Low-Trust pass.

- Reclassifies every pre-existing low-trust instance in data/master/master_index.csv
  into the new category "Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust".
- Adds records produced by this pass (new finds + one seed-orphan restored).
- Writes the pass registry: lowtrust_ledger.csv + source_access_log.csv + queries_run.csv.

Usage:  python3 scripts/build_lowtrust_pass.py
Idempotent: re-running re-derives everything from a pristine master ONLY if you first
restore master_index.csv from git (it stamps its own notes, so don't run twice blindly).
"""
import csv, os, re
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, 'data', 'master', 'master_index.csv')
OUT = os.path.join(BASE, 'registry', 'spam_scraper_syndication_lowtrust_2026-09-05')
os.makedirs(OUT, exist_ok=True)

NEW_CAT = 'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust'
OLD_CAT = 'SEO Spam / Link Farm'
MIRROR_CAT = 'Video Mirror / Backlink Sites'
DATE = '2026-09-05'

# ---------------------------------------------------------------- helpers
def U(sub):  # find master URL by substring, assert unique
    hits = [r for r in rows if sub in r['url']]
    assert len(hits) == 1, f"{sub!r} -> {len(hits)} hits"
    return hits[0]

rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
fields = rows[0].keys()
if any(r['category'] == NEW_CAT for r in rows):
    import sys
    sys.exit('Pass already applied (category present). Restore master_index.csv from git before re-running.')

# ---------------------------------------------------------------- subtype metadata
# host-class maps for the YouTube-mirror cluster (all mirror rows share video id UX2kv3G89Jw)
TOOL_HOSTS = {'deturl.com': 'TOOL-MIRROR', 'listenonrepeat.com': 'TOOL-MIRROR',
              'youtuberepeater.com': 'TOOL-MIRROR', 'ytrepeat.com': 'TOOL-MIRROR',
              'video.link': 'TOOL-MIRROR', 'viewsync.net': 'TOOL-MIRROR',
              'viewsync-2.appspot.com': 'TOOL-MIRROR', 'clipzag.com': 'TOOL-MIRROR',
              'yewtu.be': 'TOOL-MIRROR', 'fooyoh.com': 'TOOL-MIRROR',
              'salda.ws': 'TOOL-MIRROR', 'socialcounts.org': 'TOOL-MIRROR',
              'pakvim.net': 'TOOL-MIRROR', 'vtomb.com': 'TOOL-MIRROR',
              'youtube-nocookie.com': 'EMBED-CANONICAL',
              'nimtools.com': 'TOOL-MIRROR', 'nimlinks.com': 'TOOL-PROFILE-MIRROR'}
INJ_HOSTS = {'canal50.com': 'INJECTED-EMBED', 'gazetaolsztynska.pl': 'INJECTED-EMBED',
             'hribi.net': 'INJECTED-EMBED', 'stb.hu': 'INJECTED-EMBED',
             'newtv.co.th': 'INJECTED-EMBED', 'topsheetmusic.eu': 'INJECTED-EMBED',
             'tvonlayn.ru': 'INJECTED-EMBED', 'musiclessons.com': 'INJECTED-EMBED',
             'polsy.org.uk': 'INJECTED-EMBED'}
SUSP_HOSTS = {'youtubu.tv': 'TYPOSQUAT-MIRROR', 'clipzui.fun': 'SUSPICIOUS-MIRROR',
              'heartvod.com': 'SUSPICIOUS-MIRROR', 'etvplayvideos.com': 'SUSPICIOUS-MIRROR',
              'nsfwyoutube.com': 'SUSPICIOUS-MIRROR'}

def host_class(url):
    h = re.sub(r'^https?://', '', url).split('/')[0]
    for k, v in TOOL_HOSTS.items():
        if h.endswith(k): return v, h
    for k, v in INJ_HOSTS.items():
        if h.endswith(k): return v, h
    for k, v in SUSP_HOSTS.items():
        if h.endswith(k): return v, h
    return 'UNKNOWN-MIRROR', h

# per-URL overrides: substring -> (subtype, status, evidence, note)
OV = {
 'anotepad.com/notes/5246g357': ('FABRICATED-ATTRIB', 'verified',
    'page live 2026-09-05; title/body carry exact string',
    'Paste-essay attributing invented "Dr. Oliver K. Thornton, PhD, Univ. of Cambridge" + non-existent journals (The Journal of Experimental Sound and Emotion 2023, QPA/SFM theories). Auto-generated or persona fiction; treat biographical claims as void.'),
 'justpaste.it/gepby': ('PASTE-REPUB', 'verified',
    'page live 2026-09-05; anonymous PR paste Feb 12 2025, 7 visits',
    'Anonymous PR repost ("Greetings From Tinsel Time": A Subversive Holiday Classic...) with unverifiable quotes from "The New York Institute of Sound Theory" etc. Not editorial coverage.'),
 'box.hitplayer.ru': ('PIRATE-SCRAPE', 'verified',
    'live 2026-09-05; title "Zazie Productions — скачать или слушать онлайн", 186 scraped tracks mixed with French-singer Zazie noise',
    'HotPlayer pirate search/listen index page; malformed directory mixing unrelated artists.'),
 'songdata.io': ('AUTOGEN-SEARCHURL', 'broken',
    'fetch failed 2026-09-05 (host unreachable)',
    'Was a search-query URL (not a stable record); removed from Streaming & Music Platforms.'),
 'chosic.com': ('AUTOGEN-METADATA', 'unverified',
    'fetch failed 2026-09-05 (blocked)',
    'Auto-generated artist page cloned from Spotify metadata.'),
 'breakinghits.app': ('PAYTOPLAY-DIRECTORY', 'verified',
    'live 2026-09-05; invite wall shows "Check out Zazie Productions on BREAKING HITS" (reCAPTCHA untouched)',
    'Pay-to-play chart/promo platform; profile behind invite wall.'),
 'thirdeyemusic.co.uk': ('AUTOGEN-SEARCHURL', 'broken',
    'fetch failed 2026-09-05 (host unreachable)',
    'Auto directory-listing URL (?name=...&dir=tracks), not a curated record.'),
 'viberate.com': ('AUTOGEN-METADATA', 'verified',
    'live 2026-09-05; exact string in title/body',
    'Machine-written stats SEO copy (mislabels genre "avant-garde jazz"; boilerplate Q&A; "email us to update your bio").'),
 'credits.muso.ai': ('AUTOGEN-METADATA', 'unverified',
    'not probed this pass',
    'Auto-cloned Spotify credits profile.'),
 'rsssearchhub.com': ('RSS-SYNDICATION', 'broken',
    'live host but page returns "Unrecoverable error" (crashed DB) 2026-09-05',
    'RSS feed republisher; feed page currently erroring. Flagged as suspected spam already in seed.'),
 'trendingbot.org': ('AUTO-AGGREGATOR', 'broken',
    'host unreachable 2026-09-05',
    'Bot-generated topic aggregation page. Flagged in seed spam cluster.'),
 'r.darrennathanael.com': ('LEGACY-MIRROR', 'broken',
    'HTTP 500 2026-09-05',
    'Dead old-reddit proxy mirror of a legit r/Album_Cover_Art thread; mirror itself carries no independent value.'),
 'tiktok.com/@usery..y..yulles': ('BOT-REPOST', 'unverified',
    'not visited this pass (platform bot-wall)',
    'Spammy user handle re-posting the Phantom Requiem video; flagged under "spam sites" in the dump.'),
 'codex.churchofmalware.org': ('REVIEW-KEPT', 'verified',
    'live 2026-09-05; "ZAZIE PRODUCTIONS · Poison, The Well, Adversarial Audio, and Machine Learning · Edition I — Summer 2026"',
    'Seed flagged it as suspected spam; direct read shows a net-art collective "researcher" codex page linking the official Linktree. Not parasitic. Added to Community bucket for coverage; NOT spam.'),
 'comunicati.musicalive.net': ('PR-FEED-REPUB', 'broken',
    'URL now redirects to musicalive.net homepage 2026-09-05',
    'Italian promo agency auto-reposting press-release feeds; PR republication, not editorial. Was mis-tiered Press&A in the dump.'),
 'rant.li': ('SYNDICATION-MIRROR', 'unverified',
    'not visited this pass',
    'Defunct Medium mirror of a self-published Medium essay ("researcher, sonic engineer, and theorist..."). Not independent press.'),
 'gazetaolsztynska.pl': ('INJECTED-EMBED', 'broken',
    'HTTP 404 page 2026-09-05',
    'Injected YouTube-embed path on a Polish news portal; since removed/cleaned. Provenance note: hacked-site-syndication trace.'),
 'clipzag.com': ('TOOL-MIRROR', 'broken',
    'HTTP 500 2026-09-05',
    'Video mirror; currently failing.'),
 'deturl.com': ('TOOL-MIRROR', 'verified',
    'live 2026-09-05; scraped YouTube metadata shows "Zazie Productions" channel name',
    'Benign player tool; string present only via scraped video metadata.'),
 'topsheetmusic.eu': ('INJECTED-EMBED', 'verified-partial',
    'live 2026-09-05; bare player embed; exact string only in iframe video title',
    'Misused template path on a music-site; page renders video only.'),
 'listenonrepeat.com': ('TOOL-MIRROR', 'unverified',
    'fetch blocked 2026-09-05 (anti-bot)',
    'Not bypassed per policy; left unverified.'),
 'mlx.su/paste/view/26990c6b': ('PASTE-REPUB', 'broken',
    'HTTP 410 Gone 2026-09-05 — paste deleted upstream',
    'Pastebin republication (dump listed it among profile/paste material); now 410. Recorded for provenance; the underlying paste content was never captured in the dump.'),
 'getmusic.fm': ('REVIEW-KEPT', 'verified-partial',
    'live 2026-09-05; exact string NOT visible in current render (release page for moon musiq comp; name was in tracklist context)',
    'Legit bandcamp-code aggregator; kept in Streaming & Music Platforms, recorded here as borderline auto-replica.'),
 'www.boomplay.com/lyrics': ('AUTOGEN-METADATA', 'search-index verified',
    'search snippet 2026-09-05: "Goodnight, Farewell lyrics by Zazie Productions, listen and download latest songs of Zazie Productions with lyrics on Boomplay"',
    'Auto lyrics + "download for FREE" boilerplate republication (also album page 66891844 with "Download ... MP3 songs online free" pattern; recorded register-only to respect dedupe).'),
 'agencesartistiques.com': ('MISATTRIB-FLAG', 'unverified',
    'not visited',
    'Dump flagged as spam-site; page is an unrelated talent booking profile (Elsa Levy). No exact-name occurrence established — NEVER countable.'),
 'backstage.com': ('MISATTRIB-FLAG', 'unverified',
    'not visited',
    'Dump flagged as spam-site; unrelated casting profile (audreyjarnagin). No exact-name occurrence established — NEVER countable.'),
 'wnloveet.click': ('SPAM-SHOP', 'unverified',
    'not visited (suspicious .click domain, probable malware/counterfeit shop)',
    'SEO-poisoning product page riding scraped keywords.'),
 'vidmak.com': ('DOORWAY-INJECT', 'not-probed-safety',
    'NOT VISITED — known malware-distribution host (safety policy)',
    'Compromised-host doorway under BMC/IRLAM template slug.'),
 'powerkabel.com.pe': ('DOORWAY-INJECT', 'not-probed-safety',
    'NOT VISITED — counterfeit-shop style host (safety policy)',
    'Compromised-host doorway under BMC/IRLAM template slug.'),
}

DOORWAY_HOSTS = ['bytstav.sk', 'archivio.lavocedinovara.com', 'childrenofyemen.org',
                 'designbymm.cz', 'hiontech.kr', 'juetao.org', 'lcofcu.com',
                 'maynenkhikobelco.com', 'patchworkers.info', 'sarlmca.fr',
                 'shoshanagarfield.com', 'slatersgarage.com', 'smartpersonsguide.com',
                 'vidmak.com', 'powerkabel.com.pe']

def overrides(url):
    for k, v in OV.items():
        if k in url:
            return v
    return None

# ---------------------------------------------------------------- master rework
ledger = []
def add_ledger(r, cluster, subtype, evidence, status, note, origin, prior):
    ledger.append({
        'EntryID': '', 'Cluster': cluster, 'Subtype': subtype, 'URL': r['url'],
        'Host': r['host'], 'Target': r['target'], 'Origin': origin,
        'PriorMasterCategory': prior, 'MasterCategory': r['category'],
        'TrustTier': r['trust_tier'], 'LiveStatus_2026-09-05': status,
        'EvidenceLevel': evidence, 'Notes': note})

def reclassify(r, cluster, note_extra=''):
    prior = r['category']
    o = overrides(r['url'])
    if o:
        sub, st, ev, note = o
    else:
        if cluster == 'BMC-DOORWAY':
            sub, st, ev = 'DOORWAY-INJECT', 'not-probed-safety', \
                'NOT VISITED (compromised-host policy); dump-era SERP title trace "Guru Meditation Error - Zazie Productions - 单曲 - 网..." ; IA CDX sample 2026-09-05: no captures exist for sampled doorway URLs'
            note = 'Injected doorway on hacked/unrelated site; streamed-metadata title spoofed. Preserve as contamination trace only.'
        else:
            sub, st = host_class(r['url'])[0], 'unverified'
            ev = 'not individually probed this pass (cluster sample: deturl live w/ name, gazeta 404, clipzag 500, topsheet embed-only)'
            note = 'Auto-embed YouTube mirror of video UX2kv3G89Jw ("Phantom Requiem"); name appears via scraped video metadata only.'
    r['category'] = NEW_CAT
    r['trust_tier'] = 'D'
    r['status'] = st
    r['date'] = r['date'] or ''
    r['notes'] = (f"[LOWTRUST {cluster}/{sub}] {note}" + (f' {note_extra}' if note_extra else '')).strip()
    add_ledger(r, cluster, sub, ev, st, note, 'pre-existing (master + seed + dump)', prior)

# 1) old SEO-spam rows (18) -> split into doorway vs misattrib
for r in [x for x in rows if x['category'] == OLD_CAT]:
    o = overrides(r['url'])
    if any(h in r['url'] for h in DOORWAY_HOSTS):
        reclassify(r, 'BMC-DOORWAY')
    else:
        # wnloveet handled inside OV (SPAM-SHOP) and agencies/backstage MISATTRIB
        cluster = 'SPAM-SHOP' if 'wnloveet' in r['url'] else 'MISATTRIB-FLAG'
        if o:
            sub, st, ev, note = o
            r['category'] = NEW_CAT; r['trust_tier'] = 'D'; r['status'] = st
            r['notes'] = f"[LOWTRUST {cluster}/{sub}] {note}"
            add_ledger(r, cluster, sub, ev, st, note, 'pre-existing (master + seed + dump)', r['category'] if False else OLD_CAT)
        else:
            reclassify(r, cluster)

# 2) Video mirror rows -> all D-tier move; non-D stay
for r in [x for x in rows if x['category'] == MIRROR_CAT and x['trust_tier'] == 'D']:
    reclassify(r, 'YT-MIRROR')

# 3) targeted moves from other categories
MOVES = {
 'Community, Wiki & Fan Indexes': ['rsssearchhub.com', 'trendingbot.org',
     'r.darrennathanael.com', 'tiktok.com/@usery..y..yulles', 'anotepad.com', 'mlx.su'],
 'Profiles & Catalogs': ['justpaste.it/gepby', 'viberate.com', 'credits.muso.ai'],
 'Streaming & Music Platforms': ['box.hitplayer.ru', 'songdata.io', 'chosic.com',
     'breakinghits.app', 'thirdeyemusic.co.uk'],
 'Press & Editorial': ['rant.li', 'comunicati.musicalive.net'],
}
for cat, pats in MOVES.items():
    for pat in pats:
        r = next(x for x in rows if pat in x['url'] and x['category'] == cat)
        prior = r['category']
        sub, st, ev, note = overrides(r['url'])
        cluster = {'FABRICATED-ATTRIB': 'PASTE-REPUB', 'PASTE-REPUB': 'PASTE-REPUB',
                   'PIRATE-SCRAPE': 'PIRATE-SCRAPE', 'AUTOGEN-SEARCHURL': 'AUTOGEN-DATA',
                   'AUTOGEN-METADATA': 'AUTOGEN-DATA', 'PAYTOPLAY-DIRECTORY': 'AUTOGEN-DATA',
                   'RSS-SYNDICATION': 'RSS-SYNDICATION', 'AUTO-AGGREGATOR': 'RSS-SYNDICATION',
                   'LEGACY-MIRROR': 'LEGACY-MIRROR', 'BOT-REPOST': 'BOT-UGC',
                   'PR-FEED-REPUB': 'RSS-SYNDICATION', 'SYNDICATION-MIRROR': 'LEGACY-MIRROR'}.get(sub, 'OTHER')
        r['category'] = NEW_CAT; r['trust_tier'] = 'D'; r['status'] = st
        r['notes'] = f"[LOWTRUST {cluster}/{sub}] {note}"
        add_ledger(r, cluster, sub, ev, st, note, 'pre-existing (master) — moved this pass', prior)

# 4) new records
def newrow(url, host, target, cat, tier, source, status, title, notes):
    return {'url': url, 'host': host, 'target': target, 'category': cat,
            'trust_tier': tier, 'source': source, 'date': DATE, 'title': title,
            'status': status, 'notes': notes}

rows.append(newrow('https://www.boomplay.com/lyrics/151661449', 'boomplay.com',
    'Zazie Productions', NEW_CAT, 'D', 'research', 'search-index verified',
    'Zazie Productions Goodnight, Farewell Lyrics',
    '[LOWTRUST AUTOGEN-DATA/AUTOGEN-METADATA] ' + (overrides('www.boomplay.com/lyrics')[2] + ' || ' + overrides('www.boomplay.com/lyrics')[3])))
add_ledger(rows[-1], 'AUTOGEN-DATA', 'AUTOGEN-METADATA',
           overrides('www.boomplay.com/lyrics')[2], 'search-index verified',
           overrides('www.boomplay.com/lyrics')[3], 'NEW this pass (web_search exact-phrase sweep)', '(new)')

rows.append(newrow('https://codex.churchofmalware.org/researchers/ed001/zazie/',
    'codex.churchofmalware.org', 'Zazie Productions', 'Community, Wiki & Fan Indexes', 'C',
    'research', 'verified', 'ZAZIE PRODUCTIONS · Poison, The Well, Adversarial Audio, and Machine Learning · Edition I — Summer 2026',
    '[LOWTRUST REVIEW] Seed "suspected spam" orphan; reviewed 2026-09-05 = net-art collective codex page (exact string in title); NOT parasitic — restored to Community, never counted as editorial.'))
add_ledger(rows[-1], 'REVIEW-KEPT', 'REVIEW-KEPT',
           overrides('codex.churchofmalware.org')[2], 'verified',
           overrides('codex.churchofmalware.org')[3], 'pre-existing (seed-only, never in master) — added', '(new)')

# 5) kept-borderline / register-only (no master change)
BORDERLINE = [
 ('LEGACY-MIRROR', 'SYNDICATION-MIRROR', 'https://wiki2.org/en/List_of_experimental_musicians', 'wiki2.org',
  'retained in Community, Wiki & Fan Indexes', 'Wikipedia "List of experimental musicians" scraper-mirror; 📼 class per docs/01. Original article not separately cataloged — mirror row remains the census evidence of the list inclusion.'),
 ('LEGACY-MIRROR', 'SYNDICATION-MIRROR', 'https://wikimili.com/en/List_of_experimental_musicians', 'wikimili.com',
  'retained in Community, Wiki & Fan Indexes', 'Same Wikipedia mirror family.'),
 ('LEGACY-MIRROR', 'SYNDICATION-MIRROR', 'https://wikigit.org/wiki/List_of_experimental_musicians', 'wikigit.org',
  'retained in Community, Wiki & Fan Indexes', 'Same Wikipedia mirror family.'),
 ('LEGACY-MIRROR', 'SYNDICATION-MIRROR', 'https://www.wikiwand.com/en/articles/List_of_experimental_musicians', 'wikiwand.com',
  'retained in Community, Wiki & Fan Indexes', 'Styled reader mirror (semi-legit product); 📼 class.'),
 ('SEARCH-REDIRECT', 'SEARCH-REDIRECT', 'https://www.baidu.com/link?url=lGOPTjwdo-SJgH88b8O6BfcutJYDNcLfDDdoK_GDhgodoo9uajS_-T8r0CJBuFvTJ6JJ63asEqzCWIS0zFOkNK&wd=&eqid=94b87bd700fb95d100000006676ae907', 'baidu.com',
  'retained in Search-Engine Index', 'Baidu /link?url= redirect wrapper (name indexed by Baidu). A redirect chain, not a page — kept out of all counts.'),
 ('SEARCH-REDIRECT', 'SERP-ARTIFACT', 'https://disconecta.com.br/resenhas/resenhas-de-discos/playlist-autoral-15-rock-jazz/#gsc.tab=0', 'disconecta.com.br',
  'retained in Press & Editorial (dedupe pending)', '#gsc.tab=0 Google-Custom-Search artifact; duplicate of the base URL. Treat as one record.'),
 ('AUTOGEN-DATA', 'PLATFORM-REPUB', 'https://www.boomplay.com/artists/46971970', 'boomplay.com',
  'retained in Streaming & Music Platforms', 'Artist page auto-filled from distributor metadata. The lyrics subpage (66891844 album page + 151661449 lyrics) are the spammy surfaces: album page 66891844 recorded register-only ("Download ... for FREE" boilerplate), lyrics page promoted to a master row.'),
 ('AUTOGEN-DATA', 'PLATFORM-REPUB', 'https://www.boomplay.com/albums/66891844', 'boomplay.com',
  'register-only (deduped against lyrics row)', '"Miraculously Unhurt ... download for offline on Boomplay" auto album page; exact string in description JSON-LD (byArtist: Zazie Productions).'),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://getmusic.fm/r/various-artists-moon-musiq-untitled', 'getmusic.fm',
  'retained in Streaming & Music Platforms', overrides('getmusic.fm')[3]),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://app.notion.com/p/18c89e259c3c813baf39c100d3f2fe69?pvs=21', 'app.notion.com',
  'retained in Community, Wiki & Fan Indexes', 'Notion publish page; likely artist-self-published (In-Your-Eyes e-zine family). Not parasitic; unverified.'),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://app.notion.com/p/In-Your-Eyes-E-Zine-19989e259c3c8057bf81d66c6ab9903c?pvs=21', 'app.notion.com',
  'retained in Community, Wiki & Fan Indexes', 'Artist e-zine Notion publication — self-published, kept out of low-trust.'),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://perchance.org/zazieproductions', 'perchance.org',
  'retained in Profiles & Catalogs', 'User-generated perchance page; low effort but appears fan/self-made, not injected.'),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://www.senscritique.com/contact/Zazie_Productions/7375565', 'senscritique.com',
  'retained in Community, Wiki & Fan Indexes', 'Autopilot/Allocine-family contact stub under underscore form; underscore variant alone does not count (README two-name rule); kept as visibility only.'),
 ('REVIEW-KEPT', 'KEPT-BORDERLINE', 'https://www.stage32.com/media/3838211664293930413', 'stage32.com',
  'retained in Video Mirror / Backlink Sites', 'Verified profile video page ("Score by Zazie Kanwar-Torge A.K.A Zazie..."); real professional platform — NOT low-trust despite prior category.'),
 ('LEADS-UNRESOLVED', 'SPAM-LIST-LEAD', 'https://paste2.org/zgjMW539', 'paste2.org',
  'LEAD ONLY — never counted', 'paste2 list of backlink/comment-spam URLs matched "Zazie Kanwar-Torge" in the index but the phrase is NOT visible in the served snippet; suspicious link-dump payload. NOT opened (safety policy); revisit only via index snippet.'),
]
for cluster, sub, url, host, disp, note in BORDERLINE:
    tgt = 'Zazie Kanwar-Torge' if 'paste2' in url else 'Zazie Productions'
    add_ledger({'url': url, 'host': host, 'target': tgt, 'category': disp,
                'trust_tier': '—'}, cluster, sub, note, 'see note', note,
               'register-only (no master row change)', disp)

# order + IDs + provenance fields
CL_ORDER = ['BMC-DOORWAY', 'SPAM-SHOP', 'MISATTRIB-FLAG', 'YT-MIRROR', 'PIRATE-SCRAPE',
            'AUTOGEN-DATA', 'PASTE-REPUB', 'RSS-SYNDICATION', 'LEGACY-MIRROR', 'BOT-UGC',
            'REVIEW-KEPT', 'LEADS-UNRESOLVED']
ledger.sort(key=lambda x: (CL_ORDER.index(x['Cluster']) if x['Cluster'] in CL_ORDER else 99, x['URL']))
for i, e in enumerate(ledger, 1):
    e['EntryID'] = f'LT-{i:03d}'
    e['FirstRecordedIn'] = ('registry/seed SEED_INDEX_FROM_DUMP.md; Random Zazie Productions links .pdf ("spam sites" block)'
                            if 'pre-existing' in e['Origin'] else f'low-trust pass {DATE}')

cols = ['EntryID', 'Cluster', 'Subtype', 'URL', 'Host', 'Target', 'Origin',
        'PriorMasterCategory', 'MasterCategory', 'TrustTier',
        'LiveStatus_2026-09-05', 'EvidenceLevel', 'FirstRecordedIn', 'Notes']
with open(os.path.join(OUT, 'lowtrust_ledger.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
    w.writeheader(); w.writerows(ledger)

# ---------------------------------------------------------------- write master back
with open(CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(fields))
    w.writeheader(); w.writerows(rows)

# ---------------------------------------------------------------- access log
acc = [
 ('2026-09-05', 'https://www.trendingbot.org/topic/418115_klerksdorp', 'fetch_page', 'read attempt', 'DOWN — host unreachable', 'no (page unavailable)', '❌ broken', 'flagged in seed'),
 ('2026-09-05', 'https://www.rsssearchhub.com/feed/1185189bcc80cd02d670a3aaae58ebf3/city-portland-mercury', 'fetch_page', 'read attempt', 'site up; "Unrecoverable error" (crashed DB); no content rendered', 'no (currently)', '❌ broken', 'flagged in seed'),
 ('2026-09-05', 'https://codex.churchofmalware.org/researchers/ed001/zazie/', 'fetch_page', 'read attempt', 'live net-art codex page', 'YES — title "ZAZIE PRODUCTIONS · Poison, The Well, Adversarial Audio, and Machine Learning"', '✅ live+verified', 'seed orphan; re-judged NOT spam'),
 ('2026-09-05', 'https://r.darrennathanael.com/r/Album_Cover_Art/comments/1i5wjf8/zazie_productions_to_halt_space_adrift_2023/', 'fetch_page', 'read attempt', 'HTTP 500', 'no (unreachable)', '❌ broken', 'legacy reddit proxy'),
 ('2026-09-05', 'https://justpaste.it/gepby', 'fetch_page', 'read attempt', 'live anonymous paste 2025-02-12', 'YES — body', '✅ live+verified', 'PR repost w/ fabricated quotes'),
 ('2026-09-05', 'https://anotepad.com/notes/5246g357', 'fetch_page', 'read attempt', 'live paste essay', 'YES — title + body', '✅ live+verified', 'FABRICATED academic attributions'),
 ('2026-09-05', 'https://songdata.io/search?query=Zazie+Productions+', 'fetch_page', 'read attempt', 'host unreachable', 'n/a', '❌ broken', 'search-URL record'),
 ('2026-09-05', 'https://box.hitplayer.ru/?s=zazie+productions', 'fetch_page', 'read attempt', 'live pirate index, 186 results', 'YES — page title', '✅ live+verified', 'mixed with French singer noise'),
 ('2026-09-05', 'https://thirdeyemusic.co.uk/?name=Zazie_Productions&dir=tracks', 'fetch_page', 'read attempt', 'host unreachable', 'n/a', '❌ broken', 'auto listing URL'),
 ('2026-09-05', 'https://www.chosic.com/artist/zazie-productions/4UOgvZEOo7xBhFBjJvlMm0/', 'fetch_page', 'read attempt', 'fetch failed (blocked)', 'index-presence per prior passes', '⬜ blocked', 'not bypassed per policy'),
 ('2026-09-05', 'https://getmusic.fm/r/various-artists-moon-musiq-untitled', 'fetch_page', 'read attempt', 'live; exact string not visible in current render', 'no (visible text)', '🟡 partial', 'kept borderline'),
 ('2026-09-05', 'https://comunicati.musicalive.net/c/cant-get-my-eyes-off-you-123', 'fetch_page', 'read attempt', 'redirects to musicalive.net homepage', 'no (target gone)', '❌ broken', 'dead PR-feed republication'),
 ('2026-09-05', 'https://www.viberate.com/artist/zazie-productions/', 'fetch_page', 'read attempt', 'live auto-stats page', 'YES — title + body', '✅ live+verified', 'AUTOGEN SEO copy, genre mislabeled'),
 ('2026-09-05', 'https://www.breakinghits.app/zazieproductions/', 'fetch_page', 'read attempt', 'live invite wall; reCAPTCHA NOT solved', 'YES — pre-wall text', '✅ live+verified (public part only)', 'pay-to-play directory'),
 ('2026-09-05', 'https://mlx.su/paste/view/26990c6b', 'fetch_page', 'read attempt', 'HTTP 410 Gone', 'n/a — deleted', '❌ dead', 'paste deleted upstream'),
 ('2026-09-05', 'https://www.topsheetmusic.eu/sysmusic/templates/youtube.php?v=UX2kv3G89Jw', 'fetch_page', 'read attempt', 'live bare embed on misused template path', 'iframe video title only', '🟡 partial', 'hacked-site-embed pattern'),
 ('2026-09-05', 'https://deturl.com/play.php?v=UX2kv3G89Jw', 'fetch_page', 'read attempt', 'live player; scraped YouTube metadata', 'YES — "Zazie Productions" channel name', '✅ live+verified', 'benign tool mirror'),
 ('2026-09-05', 'https://listenonrepeat.com/watch/?v=UX2kv3G89Jw', 'fetch_page', 'read attempt', 'fetch blocked (anti-bot)', 'prior passes: indexed', '⬜ blocked', 'not bypassed per policy'),
 ('2026-09-05', 'https://gazetaolsztynska.pl/gminaelk/tv/video/youtube/UX2kv3G89Jw', 'fetch_page', 'read attempt', 'HTTP 404', 'n/a — cleaned up', '❌ dead', 'injected path removed'),
 ('2026-09-05', 'https://clipzag.com/watch?v=UX2kv3G89Jw', 'fetch_page', 'read attempt', 'HTTP 500', 'n/a', '❌ broken', 'mirror failing'),
 ('2026-09-05', 'https://web.archive.org/cdx/search/cdx?url=bytstav.sk/gDrA/ira-and-ruth-levinson-art-museum-north-carolina&output=json&limit=6', 'fetch_page', 'CDX availability', 'zero captures', 'n/a', 'no archive trace', 'proves transience of doorway pages'),
 ('2026-09-05', 'https://web.archive.org/cdx/search/cdx?url=childrenofyemen.org/zvgw5/black-mountain-college-ira-and-ruth-levinson-museum&output=json&limit=6', 'fetch_page', 'CDX availability', 'zero captures', 'n/a', 'no archive trace', 'proves transience of doorway pages'),
 ('2026-09-05', 'https://web.archive.org/cdx/search/cdx?url=stb.hu/youtube/UX2kv3G89Jw&output=json&limit=6', 'fetch_page', 'CDX availability', 'zero captures', 'n/a', 'no archive trace', 'mirror never archived'),
 ('2026-09-05', 'https://web.archive.org/cdx/search/cdx?url=hribi.net/video_youtube/watch/UX2kv3G89Jw&output=json&limit=6', 'fetch_page', 'CDX availability', 'zero captures', 'n/a', 'no archive trace', 'mirror never archived'),
 ('2026-09-05', 'https://bytstav.sk/gDrA/... | powerkabel.com.pe/love-quotes/... | vidmak.com/fs0vz3/... | wnloveet.click/product_details/105751966.html | juetao.org/yfc/... | agenciesartistiques.com/fiche-artiste/739100-elsa-levy.html | backstage.com/u/audreyjarnagin/ | mlx.su (done) — refused hosts', 'POLICY', 'REFUSED reads (safety policy: known-compromised / malware-adjacent hosts; no visits, no downloads, no scripts)', 'documented from repo seed + dump only', 'n/a', '⬜ not-probed-safety', '7 refused'),
]
with open(os.path.join(OUT, 'source_access_log.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Date', 'URL', 'Method', 'Action', 'Outcome', 'ExactPhraseFound', 'StatusTag', 'Notes'])
    w.writerows(acc)

# ---------------------------------------------------------------- query log
queries = [
 ('LT-Q01', '"Zazie Productions" spam doorway scrape', 'Zazie Productions', 'web_search (general index), depth 2', DATE, '1 result — slaps.com profile (legit); no new doorway hits', 'No new spam; current index has de-listed the old doorway cluster'),
 ('LT-Q02', '"Zazie Kanwar-Torge"', 'Zazie Kanwar-Torge', 'web_search depth 2', DATE, 'ReelCrafter share link, IMDb, LinkedIn, ListenNotes, Hackaday — all legit/self', 'No new low-trust hits'),
 ('LT-Q03', '"Zazie Productions" "Guru Meditation Error"', 'Zazie Productions', 'web_search depth 2', DATE, 'Bandcamp track pages (official)', 'Established the string is a real track title spoofed by the 单曲 doorway titles'),
 ('LT-Q04', '"Zazie Productions" black-mountain-college-ira-and-ruth-levinson-museum', 'Zazie Productions', 'web_search depth 2', DATE, 'Only legit blackmountaincollege.org/museonline.org results', 'Doorway cluster no longer indexed on current engine'),
 ('LT-Q05', '"Zazie Productions" 单曲', 'Zazie Productions', 'web_search depth 2', DATE, 'Deezer/Apple/Spotify/linktr/bandcamp only', 'Chinese-doorway remnants not indexed'),
 ('LT-Q06', '"Zazie Productions" lyrics -bandcamp -discogs -spotify', 'Zazie Productions', 'web_search depth 2', DATE, 'boomplay.com/lyrics/151661449 + deezer + slaps + viberate', 'NEW: boomplay lyrics republication'),
 ('LT-Q07', '"Zazie Productions" "press release" -prfree.org -linktr.ee -bandcamp.com', 'Zazie Productions', 'web_search depth 2', DATE, 'bandmix profile text; no fresh PR-farm', 'Negative'),
 ('LT-Q08', '"Zazie Productions" rsssearchhub OR trendingbot OR "deturl" OR "UX2kv3G89Jw"', 'Zazie Productions', 'web_search depth 1', DATE, 'bandmix (carries video id UX2kv3G89Jw — feed source of mirror cluster)', 'No NEW mirror hosts'),
 ('LT-Q09', '"Zazie Productions" muso.ai OR boomplay OR "soundunwound" OR sndup', 'Zazie Productions', 'web_search depth 1', DATE, 'boomplay album page 66891844 ("Download ... for FREE")', 'NEW (register-only) + lyrics page promoted'),
 ('LT-Q10', '"Zazie Productions" "free download" mp3 -bandcamp -soundclick', 'Zazie Productions', 'web_search depth 1', DATE, 'official bandcamp only', 'No new pirate index beyond hitplayer/boomplay'),
 ('LT-Q11', '"Zazie Kanwar-Torge" paste OR pastebin OR anotepad OR telegra', 'Zazie Kanwar-Torge', 'web_search depth 1', DATE, 'paste2.org/zgjMW539 backlink list (LEAD); telegra.ph generic malware-adjacent articles', 'Lead LT-lead-01 logged, never counted'),
]
with open(os.path.join(OUT, 'queries_run.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['QueryID', 'ExactQuery', 'TargetPreserved', 'Engine', 'Date', 'HitsOfInterest', 'Disposition'])
    w.writerows(queries)

# ---------------------------------------------------------------- console stats
cnt = Counter(r['category'] for r in rows)
tier = Counter(r['trust_tier'] for r in rows)
print('TOTAL MASTER ROWS:', len(rows))
print('NEW CAT ROWS:', cnt[NEW_CAT])
print('LEDGER ROWS:', len(ledger))
print('CLUSTERS:', dict(Counter(e['Cluster'] for e in ledger)))
print('TIERS:', dict(tier))
print('CATS:', dict(cnt))
print('statuses moved:', dict(Counter(r['status'] for r in rows if r['category'] == NEW_CAT)))
