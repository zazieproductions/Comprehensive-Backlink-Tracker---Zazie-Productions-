#!/usr/bin/env python3
"""Build the single colour-coded master directory PDF of every media feature in this repository.

Input : data/master/consolidated_directory.json    (produce it with scripts/ingest_all_links.py)
Output: Zazie_Master_Directory_COLOUR_CODED.pdf     (repository root)

Layout
  A4 landscape. One table row per link. Links are grouped into media-type / topic sections ordered
  from the most reputable kind of placement to the most spammy, and within every section rows are
  ranked by the computed credibility score (tier A > B > C > D, host authority, verification status,
  evidence-quality flags). Colour carries meaning: tier chip, credibility heat cell, status chip,
  red integrity flags and section header bands. A full alphabetical link register follows as an
  appendix so that literally every link is printed in complete form.

Usage:  python3 scripts/build_master_directory_pdf.py
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data', 'master', 'consolidated_directory.json')
OUT = os.path.join(BASE, 'Zazie_Master_Directory_COLOUR_CODED.pdf')

PAGE = landscape(A4)
LM = RM = 11 * mm
TM = 17 * mm
BM = 13 * mm
CW = PAGE[0] - LM - RM

# --------------------------------------------------------------------------- palette
INK = colors.HexColor('#12161c')
SOFT = colors.HexColor('#5b6674')
RULE = colors.HexColor('#c9d2dc')
BAND = colors.HexColor('#eef3f8')
HEADBG = colors.HexColor('#37424e')

TIER = {'A': (colors.HexColor('#0b6e4f'), colors.HexColor('#eaf6ef')),
        'B': (colors.HexColor('#1a73e8'), colors.HexColor('#eaf1fc')),
        'C': (colors.HexColor('#b06000'), colors.HexColor('#fdf4e5')),
        'D': (colors.HexColor('#8c1d18'), colors.HexColor('#fbeceb'))}
TIER_LABEL = {'A': 'A · verified institutional or independent-press record',
              'B': 'B · supporting platform, catalogue or trade record',
              'C': 'C · community, compilation or self-published context',
              'D': 'D · quarantined: spam, scraper, syndication or poisoned'}
STATUS = {'verified': (colors.HexColor('#188038'), 'LIVE'), 'live': (colors.HexColor('#188038'), 'LIVE'),
          'search-index verified': (colors.HexColor('#0f9d58'), 'IDX-OK'),
          'verified-partial': (colors.HexColor('#5f8b3a'), 'PARTIAL'),
          'partial': (colors.HexColor('#b06000'), 'PARTIAL'),
          'unverified': (colors.HexColor('#7b8794'), 'UNCHECKED'),
          'not-probed-safety': (colors.HexColor('#8a6d3b'), 'DO-NOT-OPEN'),
          'broken': (colors.HexColor('#b3261e'), 'BROKEN'),
          'lead': (colors.HexColor('#607d8b'), 'LEAD')}
CAT_COLOR = {'Press & Editorial': '#d93025', 'Publications & Recognition': '#7b1fa2',
             'Film, Festivals & Exhibitions': '#d81b60', 'Podcasts & Broadcasts': '#3949ab',
             'Profiles & Catalogs': '#1a73e8', 'Music Discography': '#c2185b',
             'Streaming & Music Platforms': '#039be5', 'Lyrics & Music Databases': '#00897b',
             'Music Compilations': '#e8710a', 'Official Properties & Channels': '#2e7d32',
             'Community, Wiki & Fan Indexes': '#188038', 'Search-Engine Index': '#0f9d8f',
             'Video Mirror / Backlink Sites': '#607d8b',
             'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust': '#616161'}
SECTION_ORDER = list(CAT_COLOR.keys())
SECTION_BLURB = {
    'Press & Editorial': 'Independent magazines, webzines, journals and news coverage: dedicated features, reviews and interviews where the artist is the subject.',
    'Publications & Recognition': 'Awards, honours, contest placements, institutional credit roll-pages and published writing carrying the exact name.',
    'Film, Festivals & Exhibitions': 'Festival selections and award citations, exhibition pages, screening listings and film-credit records.',
    'Podcasts & Broadcasts': 'Radio broadcasts, podcast episodes and show notes where the name is spoken or printed.',
    'Profiles & Catalogs': 'Artist, composer and professional profiles on industry, creative and database platforms.',
    'Music Discography': 'Catalogue and discography database records (label, master and release pages).',
    'Streaming & Music Platforms': 'Artist pages on streaming services, music-identification apps and audio catalogues.',
    'Lyrics & Music Databases': 'Lyrics and music-metadata database entries.',
    'Music Compilations': 'Compilation, netlabel and split-release appearances: one row per public listing of the credit.',
    'Official Properties & Channels': 'Artist-owned storefronts, channels, repositories and self-published pages. Presence proves the account exists, not third-party recognition.',
    'Community, Wiki & Fan Indexes': 'Wikis, fan lists, forums, quizzes, charts and community-maintained pages.',
    'Search-Engine Index': 'Search-engine and index surfaces holding the exact name, including redirect artefacts.',
    'Video Mirror / Backlink Sites': 'Video-proxy and embed surfaces that still read as ordinary listings.',
    'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust': 'QUARANTINE. Hacked-site doorways, scraped clones, auto-generated metadata, paste reposts and mirror farms. Recorded to document contamination and to support takedown or correction requests. Never treat any row below as coverage, credit or biographical fact.',
}

# --------------------------------------------------------------------------- styles
def S(name, **kw):
    kw.setdefault('fontName', 'Helvetica')
    kw.setdefault('fontSize', 7)
    kw.setdefault('leading', 8.4)
    kw.setdefault('textColor', INK)
    return ParagraphStyle(name, **kw)


ST = {
    'h1': S('h1', fontName='Helvetica-Bold', fontSize=20, leading=23),
    'h2': S('h2', fontName='Helvetica-Bold', fontSize=13.5, leading=16),
    'h3': S('h3', fontName='Helvetica-Bold', fontSize=9.5, leading=12),
    'body': S('body', fontSize=8.4, leading=11),
    'small': S('small', fontSize=7.2, leading=9, textColor=SOFT),
    'cell': S('cell', fontSize=6.5, leading=7.7),
    'url': S('url', fontName='Courier', fontSize=5.7, leading=6.8, wordWrap='CJK',
             textColor=colors.HexColor('#1a3d8f')),
    'apx': S('apx', fontName='Courier', fontSize=5.5, leading=6.6, wordWrap='CJK',
             textColor=colors.HexColor('#1a3d8f')),
    'th': S('th', fontName='Helvetica-Bold', fontSize=6.3, leading=7.6, textColor=colors.white),
    'legend': S('legend', fontSize=7.4, leading=9.6),
}


BOX = {}
SPECIAL = {'‘': '‘', '’': '’', '“': '“', '”': '”', '–': '–',
           '—': '—', '…': '…', '·': '·', ' ': ' ', '•': '·',
           '°': '°', 'é': 'é', 'è': 'è', 'à': 'à', 'ü': 'ü',
           'ö': 'ö', 'ä': 'ä', 'ñ': 'ñ', 'å': 'å', 'ß': 'ß',
           '±': '±', '£': '£', '€': '€', '→': '·', '»': '»',
           '«': '«', '‚': '’', '„': '“'}


def esc(t):
    t = t or ''
    out = []
    for ch in t:
        if ch in SPECIAL:
            out.append(SPECIAL[ch])
        elif ord(ch) < 128:
            out.append(ch)
        elif 32 <= ord(ch) <= 255:
            out.append(ch)
        else:
            out.append('')          # drop emoji / CJK / box glyphs Helvetica cannot draw
    t = ''.join(out)
    t = re.sub(r' {2,}', ' ', t)
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def heat(v):
    if v >= 80:
        return colors.HexColor('#bfe8cf'), colors.HexColor('#0b5d2b')
    if v >= 62:
        return colors.HexColor('#e4f3d6'), colors.HexColor('#33691e')
    if v >= 45:
        return colors.HexColor('#fff2cc'), colors.HexColor('#8a6d3b')
    if v >= 28:
        return colors.HexColor('#ffe0b2'), colors.HexColor('#a04000')
    return colors.HexColor('#fbd6d3'), colors.HexColor('#8c1d18')


def para(text, style='cell', align=None, colour=None, size=None, bold=False):
    base = ST.get(style) if isinstance(style, str) else None
    st = dict(fontName=('Helvetica-Bold' if bold else (base.fontName if base else 'Helvetica')),
              fontSize=size or (base.fontSize if base else 6.5),
              leading=(size + 1.3) if size else (base.leading if base else 7.8),
              textColor=colour or (base.textColor if base else INK))
    if base and getattr(base, 'wordWrap', None):
        st['wordWrap'] = base.wordWrap
    if align:
        st['alignment'] = align
    return Paragraph(text, S('tmp', **st))


# --------------------------------------------------------------------------- document
# two-pass build: pass 1 records which page every section lands on, pass 2 prints those numbers
# in the contents table. `python3 scripts/build_master_directory_pdf.py` runs both passes itself.
PAGEMAP_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'master',
                             '.pdf_pagemap.json')
PAGEMAP_CACHE = os.path.normpath(PAGEMAP_CACHE)
PAGEMAP = {}
OUTLINE = []
HAVE_MAP = False
if os.path.exists(PAGEMAP_CACHE):
    try:
        PAGEMAP = json.load(open(PAGEMAP_CACHE, encoding='utf-8'))
        HAVE_MAP = bool(PAGEMAP)
    except Exception:
        PAGEMAP = {}
OUTLINE = []
OUTLINE = []


class Marker(Paragraph):
    """Zero-height flowable that records the page it lands on (and bookmarks it)."""

    def __init__(self, key, title):
        super().__init__('', S('mk', fontSize=0.1, leading=0.1))
        self.key, self.title = key, title
        if (key, title) not in OUTLINE:
            OUTLINE.append((key, title))
        self.spaceBefore = 0
        self.spaceAfter = 0

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        PAGEMAP[self.key] = self.canv.getPageNumber()


class DirDoc(BaseDocTemplate):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        frame = Frame(LM, BM, CW, PAGE[1] - TM - BM, id='main',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id='cover', frames=[frame], onPage=self.cover_deco),
                               PageTemplate(id='body', frames=[frame], onPage=self.body_deco)])
        self.section_title = ''

    def cover_deco(self, cv, doc):
        cv.saveState()
        cv.setFillColor(INK)
        cv.rect(0, PAGE[1] - 44 * mm, PAGE[0], 44 * mm, stroke=0, fill=1)
        xs = ['#d93025', '#7b1fa2', '#d81b60', '#3949ab', '#1a73e8', '#c2185b', '#039be5',
              '#e8710a', '#2e7d32', '#188038', '#607d8b', '#616161']
        w = PAGE[0] / len(xs)
        for i, c in enumerate(xs):
            cv.setFillColor(colors.HexColor(c))
            cv.rect(i * w, PAGE[1] - 47 * mm, w - 1.5, 3 * mm, stroke=0, fill=1)
        cv.setFillColor(colors.white)
        cv.setFont('Helvetica-Bold', 20)
        cv.drawString(LM, PAGE[1] - 20 * mm, 'ZAZIE PRODUCTIONS  ·  ZAZIE KANWAR-TORGE')
        cv.setFont('Helvetica', 11.6)
        cv.drawString(LM, PAGE[1] - 28.5 * mm,
                      'Colour-Coded Master Directory of Media Features, Press, Film, Publications, Credits, Profiles, Mentions & Quarantined Links')
        cv.setFont('Helvetica', 9)
        cv.drawString(LM, PAGE[1] - 35 * mm,
                      'Every catalogued public-web link in one ranked volume — most reputable and impressive first, most spammy last')
        cv.setFont('Helvetica-Bold', 7.8)
        cv.drawString(LM, PAGE[1] - 40.5 * mm,
                      'Includes five headline reading paths:  P1 NETLABEL + COMPILATIONS · P2 MAGAZINES / ZINES · P3 NEWS & MEDIA · '
                      'P4 EXHIBITIONS & GALLERIES · P5 LITERARY & WRITING')
        cv.setFillColor(SOFT)
        cv.setFont('Helvetica', 7.6)
        cv.drawCentredString(PAGE[0] / 2, BM - 5.5 * mm,
                             f'Compiled {date.today():%d %B %Y} from the repository census · inclusion requires the exact string '
                             f'"Zazie Productions" or "Zazie Kanwar-Torge" · presence in this volume is documentation, not endorsement')
        cv.restoreState()

    def body_deco(self, cv, doc):
        cv.saveState()
        cv.setStrokeColor(RULE)
        cv.setLineWidth(0.5)
        cv.line(LM, PAGE[1] - 13.5 * mm, PAGE[0] - RM, PAGE[1] - 13.5 * mm)
        cv.setFont('Helvetica-Bold', 6.6)
        cv.setFillColor(INK)
        cv.drawString(LM, PAGE[1] - 11.6 * mm, 'ZAZIE EXACT-NAME MASTER DIRECTORY')
        cv.setFont('Helvetica', 6.6)
        cv.setFillColor(SOFT)
        cv.drawRightString(PAGE[0] - RM, PAGE[1] - 11.6 * mm, (self.section_title or '')[:150])
        cv.line(LM, BM - 3.4 * mm, PAGE[0] - RM, BM - 3.4 * mm)
        cv.drawString(LM, BM - 8 * mm, f'page {doc.page}')
        cv.drawRightString(PAGE[0] - RM, BM - 8 * mm, 'A/B = usable   C = context only   D = quarantine (never cite)')
        cv.restoreState()

    page_total_note = ''


def banner(text, colour=HEADBG, size=12, sub=None, right=None):
    inner = [[Paragraph(f'<font color="#ffffff" size="{size}"><b>{esc(text)}</b></font>',
                        S('b', fontSize=size, leading=size + 2.5, textColor=colors.white))]]
    if sub:
        inner.append([Paragraph(f'<font color="#dbe4ee" size="7">{esc(sub)}</font>',
                                S('b2', fontSize=7, leading=9, textColor=colors.HexColor('#dbe4ee')))])
    inner_w = CW * (0.62 if right else 0.99)
    cells = [Table(inner, colWidths=[inner_w],
                   style=TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                     ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))]
    if right:
        cells.append(Paragraph(f'<para alignment="right"><font color="#ffffff" size="7">{esc(right)}</font></para>',
                              S('br', fontSize=7, leading=9, alignment=TA_RIGHT, textColor=colors.white)))
    t = Table([cells], colWidths=[CW * 0.62, CW * 0.38] if right else [CW])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(colour) if isinstance(colour, str) else colour),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                           ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    return t


def grid(rows, widths, header=None, header_bg=HEADBG, zebra=True, font=6.5, aligns=None, extra=None):
    data = []
    if header:
        data.append([Paragraph(f'<b>{esc(h)}</b>', ST['th']) for h in header])
    for r in rows:
        line = []
        for i, c in enumerate(r):
            if hasattr(c, 'wrapOn'):
                line.append(c)
            else:
                al = (aligns or {}).get(i)
                line.append(Paragraph(str(c), S('g', fontSize=font, leading=font + 1.4, alignment=al or TA_LEFT)))
        data.append(line)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#dde4ea')),
          ('LEFTPADDING', (0, 0), (-1, -1), 2.6), ('RIGHTPADDING', (0, 0), (-1, -1), 2.6),
          ('TOPPADDING', (0, 0), (-1, -1), 1.8), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8)]
    if header:
        st += [('BACKGROUND', (0, 0), (-1, 0), header_bg), ('LINEBELOW', (0, 0), (-1, 0), 0.6, header_bg)]
    off = 1 if header else 0
    if zebra:
        for i in range(len(rows)):
            st.append(('BACKGROUND', (0, i + off), (-1, i + off),
                       colors.white if i % 2 == 0 else colors.HexColor('#f6f8fa')))
    t.setStyle(TableStyle(st + (extra or [])))
    return t


# --------------------------------------------------------------------------- data
payload = json.load(open(DATA, encoding='utf-8'))
recs = payload['records']
engines = payload['engine_endpoints']
by_section = defaultdict(list)
for r in recs:
    by_section[r['category']].append(r)
for k in by_section:
    by_section[k].sort(key=lambda r: (-r['raw'], r['host']))
sections = [s for s in SECTION_ORDER if s in by_section]
for s in by_section:
    if s not in sections:
        sections.append(s)

# ------------------------------------------------------------ five headline reading paths
# The reader asked for five thematic cuts of the whole corpus, each complete and each ranked
# from most reputable/impressive to least. They overlap: one link can appear on several paths.
READING_PATHS = [
    {'key': 'path:1', 'name': 'NETLABEL + COMPILATION FEATURES',
     'colour': '#e8710a',
     'sub': 'Every compilation, netlabel, split-release and V/A credit found anywhere in the census: Bandcamp '
            'compilations, independent netlabel catalogues, and the platform/database echoes of the same credits.',
     'filter': lambda r: r['topic'] == 'Bandcamp & netlabel compilation credits'
                         or r['category'] == 'Music Compilations',
     'main': 'Music Compilations'},
    {'key': 'path:2', 'name': 'MAGAZINE / ZINE FEATURES',
     'colour': '#c2185b',
     'sub': 'Dedicated features, reviews, interviews and profiles about the artist in independent magazines, zines '
            'and journals — the Phase-4 magazine/zine census pass united with every major press feature on record.',
     'filter': lambda r: any('magazine' in s.lower() for s in r['sources'])
                         or (r['category'] == 'Press & Editorial'
                             and r['topic'] == 'Major press features & interviews'),
     'main': 'Press & Editorial'},
    {'key': 'path:3', 'name': 'NEWS ARTICLES & MEDIA COVERAGE',
     'colour': '#d93025',
     'sub': 'The full news/editorial surface: every press and editorial article, review, report and feature, plus '
            'radio broadcasts and podcast episodes carrying the exact name.',
     'filter': lambda r: r['category'] in ('Press & Editorial', 'Podcasts & Broadcasts'),
     'main': 'Press & Editorial'},
    {'key': 'path:4', 'name': 'EXHIBITIONS, ART GALLERIES & FILM-FESTIVAL RECOGNITION',
     'colour': '#6a1b9a',
     'sub': 'Gallery shows, biennales, exhibitions, screenings and festival selections or awards — every page where '
            'the work was curated, programmed or honoured in public.',
     'filter': lambda r: r['category'] == 'Film, Festivals & Exhibitions'
                         or r['topic'] == 'Award-winning film & festival recognition',
     'main': 'Film, Festivals & Exhibitions'},
    {'key': 'path:5', 'name': 'LITERARY PUBLICATIONS & WRITING',
     'colour': '#00796b',
     'sub': 'Poems, anthologies, lit-mag issues, essays, bylines, contributor pages, contest placements, honours and '
            'institutional credit-roll pages — the published-writing record.',
     'filter': lambda r: r['topic'] == 'Literary, poetry & anthology publications'
                         or r['category'] == 'Publications & Recognition'
                         or any('PHASE3' in s for s in r['sources']),
     'main': 'Publications & Recognition'},
]
for p in READING_PATHS:
    p['rows'] = sorted([r for r in recs if p['filter'](r)], key=lambda r: (-r['raw'], r['host']))

N = len(recs)
tier_ct = Counter(r['tier'] for r in recs)
stat_ct = Counter(r['status'] for r in recs)
target_ct = Counter(r['target'] for r in recs)
host_ct = Counter(r['host'] for r in recs)
topic_ct = Counter(r['topic'] for r in recs)
flag_ct = Counter(f for r in recs for f in r.get('flags', []))
src_ct = Counter(s for r in recs for s in r['sources'])

COLW = [13.5 * mm, 7.5 * mm, 11.5 * mm, 15 * mm, 33 * mm, 94 * mm, 74 * mm, 17 * mm]
HEADERS = ['RANK', 'TIER', 'CRED', 'DATE', 'OUTLET · HOST', 'WHAT IT IS  ·  EVIDENCE, CONTEXT & INTEGRITY FLAGS',
           'FULL LINK (clickable)', 'STATUS']


def rec_row(r):
    tier = r['tier'] if r['tier'] in TIER else 'C'
    cfill, ctext = heat(r['score'])
    sfill, slab = STATUS.get(r['status'], (SOFT, (r['status'] or '?').upper()))
    parts = []
    if r['title']:
        parts.append(f'<b>{esc(r["title"])}</b>')
    if r['target'] and 'contextual' not in r['target']:
        parts.append(f'<font color="#3949ab"><b>exact name on page:</b> {esc(r["target"])}</font>')
    if r['notes']:
        parts.append(f'<font color="#4a5563">{esc(r["notes"][:360])}</font>')
    if r.get('flag_reasons'):
        parts.append('<font color="#8c1d18"><b>FLAG</b> ' + esc(' · '.join(r['flag_reasons'])[:300]) + '</font>')
    parts.append(f'<font color="#78909c">topic: {esc(r["topic"])} · in {len(r["sources"])} source file(s)</font>')
    url = r['url']
    return ([para(f'<para alignment="right"><font color="#78909c" size="6">{r["rank"]}</font></para>'),
             para(f'<para alignment="center"><font color="#ffffff" size="7.4"><b>{tier}</b></font></para>', colour=colors.white),
             para(f'<para alignment="center"><font color="{ctext}" size="6.8"><b>{r["score"]}</b></font></para>'),
             para(esc(r['date'][:17]) if r['date'] else '<font color="#b0bac4">n/d</font>'),
             para(f'<b>{esc(r["host"])}</b>'),
             para('<br/>'.join(parts)),
             para(f'<a href="{esc(url)}" color="#1a3d8f">{esc(url)}</a>', 'url'),
             para(f'<para alignment="center"><font color="#ffffff" size="5.6"><b>{slab}</b></font></para>',
                  colour=colors.white)],
            (TIER[tier][1], TIER[tier][0], cfill, sfill))


story = []

# =========================================================== COVER
stat_cells = [
    (str(N), 'links in the directory'),
    (str(len({r['norm'] for r in recs})), 'unique URLs'),
    (str(len(sections)), 'media-type sections'),
    (str(len(topic_ct)), 'subject topics'),
    (str(len(host_ct)), 'domains'),
    (str(tier_ct['A']), 'tier A · strongest'),
    (str(tier_ct['D']), 'tier D · quarantine'),
    (str(sum(1 for r in recs if r['status'] in ('verified', 'live', 'search-index verified'))), 'live / verified'),
]
row1 = [Paragraph(f'<para alignment="center"><font size="17" color="#0b6e4f"><b>{v}</b></font><br/>'
                  f'<font size="6.4" color="#5b6674">{esc(lbl)}</font></para>', ST['legend']) for v, lbl in stat_cells]
story += [Spacer(1, 34 * mm), Table([row1], colWidths=[CW / 8] * 8,
                                   style=TableStyle([('BOX', (0, 0), (-1, -1), 0.4, RULE),
                                                     ('INNERGRID', (0, 0), (-1, -1), 0.3, RULE),
                                                     ('TOPPADDING', (0, 0), (-1, -1), 4),
                                                     ('BOTTOMPADDING', (0, 0), (-1, -1), 5)])),
          Spacer(1, 7 * mm)]

legend_rows = []
for s in sections:
    rs = by_section[s]
    best = max(x['score'] for x in rs)
    tcount = Counter(x['tier'] for x in rs)
    legend_rows.append([para(f'<para alignment="center"><font color="#ffffff" size="6"><b>{s[0]}</b></font></para>',
                             colour=colors.white),
                        para(f'<b>{esc(s)}</b>'),
                        para(str(len(rs)), 'cell', TA_RIGHT),
                        para(f'A {tcount["A"]} · B {tcount["B"]} · C {tcount["C"]} · D {tcount["D"]}',
                             'cell', colour=SOFT),
                        para(esc(SECTION_BLURB[s][:150]) + ('…' if len(SECTION_BLURB[s]) > 150 else ''), 'cell')])
story += [banner('SECTION MAP — media type, from the most impressive kind of placement to the least trustworthy',
                 size=10, sub='the section order itself is the credibility ladder; rows inside each section are re-ranked individually'),
          Spacer(1, 2 * mm),
          grid(legend_rows, [7 * mm, 44 * mm, 14 * mm, 42 * mm, CW - 107 * mm],
               header=['', 'SECTION', 'LINKS', 'TIER SPLIT', 'WHAT BELONGS HERE'], zebra=True, font=6.6,
               extra=[('BACKGROUND', (0, i + 1), (0, i + 1), colors.HexColor(CAT_COLOR[sec]))
                      for i, sec in enumerate(sections)] +
                     [('TOPPADDING', (0, 0), (-1, -1), 2.4), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.4)]),
          Spacer(1, 4 * mm)]



COVER_NOTE = (
    '<b>WHAT THIS IS.</b> One volume holding every public-web location where the exact names '
    '<i>Zazie Productions</i> or <i>Zazie Kanwar-Torge</i> are indexed, credited, quoted, embedded or linked — '
    'press, film and festival records, publications and honours, platform profiles, streaming and catalogue pages, '
    'every compilation credit, the artist’s own channels, community pages, and finally the quarantined spam, '
    'scraper and SEO-poisoning material that has been attached to the name.'
    '<br/><br/><b>THE LADDER.</b> Section order is the credibility ladder: independent editorial press at the top, '
    'recognition and film next, then industry and platform records, then compilations and community surfaces, with '
    'embed farms, auto-generated mirrors and hacked-site doorways at the very end. Inside each section, rows are '
    're-ranked by a 0-100 credibility index shown on a coloured cell.'
    '<br/><br/><b>WHY THE SPAM IS PRINTED AT ALL.</b> Quarantined rows are evidence of contamination: they are what a '
    'reader may find on search engines, and what needs correcting or reporting. They are included with their URLs so '
    'nothing is hidden, and marked so nothing can be mistaken for coverage.')
cover_notes = Table([[Table([[para(COVER_NOTE, 'legend')]], colWidths=[CW - 2],
                            style=TableStyle([('BOX', (0, 0), (-1, -1), 0.4, RULE),
                                              ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f7f9fc')),
                                              ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                                              ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))]],
                     colWidths=[CW])
story += [Spacer(1, 5 * mm), cover_notes, NextPageTemplate('body'), PageBreak()]

# =========================================================== HOW TO READ
legend_block = []
for t in ['A', 'B', 'C', 'D']:
    n = tier_ct[t]
    legend_block.append([para(f'<para alignment="center"><font color="#ffffff" size="9"><b>{t}</b></font></para>',
                              colour=colors.white),
                         para(esc(TIER_LABEL[t])),
                         para(f'<b>{n}</b> links', 'cell'),
                         para({'A': 'top of the volume: institutional, award and independent-editorial records',
                               'B': 'trade, catalogue and platform records that support the story',
                               'C': 'bulk context: compilations, community pages, self-published surfaces',
                               'D': 'printed last, in the quarantine section only'}[t], 'cell', colour=SOFT)])
story += [banner('HOW TO READ THIS VOLUME', size=11,
                 sub='colour is data: each cell colour encodes one ranked dimension of the record'),
          Marker('front:howto', 'How to read this volume'),
          Spacer(1, 3 * mm)]


story.append(Spacer(1, 3 * mm))

scale_row = Table([[para(f'<b>CREDIBILITY INDEX</b> — one number per row, printed on a coloured cell: '
                         f'80+ deep green · 62-79 light green · 45-61 amber · 28-44 orange · under 28 red',
                         'legend')]], colWidths=[CW])
heat_cells = [[para(f'<para alignment="center"><font color="{heat(v)[1]}" size="8"><b>{v}+</b></font></para>',
                    colour=heat(v)[0]) for v in (95, 85, 75, 65, 55, 45, 35, 25, 15, 5)]]
ht = Table(heat_cells, colWidths=[CW / 10] * 10)
ht.setStyle(TableStyle([('BACKGROUND', (i, 0), (i, 0), heat(v)[0]) for i, v in enumerate((95, 85, 75, 65, 55, 45, 35, 25, 15, 5))]))

story += [grid(legend_block, [12 * mm, 78 * mm, 22 * mm, CW - 112 * mm],
               header=['TIER', 'MEANING', 'COUNT', 'WHERE IT SITS IN THE VOLUME'], zebra=False, font=7)]
story += [Spacer(1, 3 * mm), scale_row, ht, Spacer(1, 3 * mm)]

lab_ct = Counter((STATUS.get(r['status']) or (None, 'UNCHECKED'))[1] for r in recs)
status_rows, chip_fills = [], []
for lab in ['LIVE', 'IDX-OK', 'PARTIAL', 'UNCHECKED', 'DO-NOT-OPEN', 'BROKEN', 'LEAD']:
    fill = next(v[0] for k, v in STATUS.items() if v[1] == lab)
    status_rows.append([para(f'<para alignment="center"><font color="#ffffff" size="6"><b>{lab}</b></font></para>',
                             colour=colors.white),
                        para({'LIVE': 'page opened during the census and the exact string was seen on it',
                              'IDX-OK': 'the name still renders inside a search-index snapshot of the page',
                              'PARTIAL': 'page reached, but the exact string only appears in a module, list or caption',
                              'UNCHECKED': 'recorded from a repository file; not opened during the most recent pass',
                              'DO-NOT-OPEN': 'quarantined compromised host — kept as evidence, never fetched',
                              'BROKEN': 'resolved and found dead (404 / parked / removed)',
                              'LEAD': 'lead only: not counted as a record anywhere in this volume'}[lab], 'cell'),
                        para(f'<b>{lab_ct.get(lab, 0)}</b>', 'cell', TA_RIGHT)])
    chip_fills.append(fill)
st_tbl = grid(status_rows, [26 * mm, CW * 0.5, 14 * mm], header=['STATUS CHIP', 'WHAT THE STATUS MEANS', 'N'],
              zebra=False, font=6.8,
              extra=[('BACKGROUND', (0, i + 1), (0, i + 1), f) for i, f in enumerate(chip_fills)] +
                    [('VALIGN', (0, 1), (0, -1), 'MIDDLE'), ('TOPPADDING', (0, 1), (-1, -1), 3),
                     ('BOTTOMPADDING', (0, 1), (-1, -1), 3)])
story += [Table([[para('<b>STATUS CHIPS</b> — printed in the last column of every row', 'legend')],
                 [st_tbl]], colWidths=[CW],
                style=TableStyle([('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (0, 0), 2),
                                  ('LEFTPADDING', (0, 0), (-1, -1), 0)]))]

FLAG_DEF = {
    'PAY-TO-PLAY PR WIRE': 'self-issued press-release distribution, not independent editorial',
    'SELF-PUBLISHED PROPERTY': 'artist- or collective-owned surface: proves existence, not third-party recognition',
    'UNOFFICIAL FILM MIRROR': 'scraper/streamer replica of the same festival or TMDB record, not a separate placement',
    'WIKI MIRROR': 'machine mirror of a Wikipedia list page — the underlying record is the article itself',
    'EMBED / BACKLINK FARM': 'proxy player built to farm a backlink to one video',
    'PASTE / SELF-SERVE HOSTING': 'anonymous paste or self-serve page: provenance not established',
    'AUTO-GENERATED METADATA': 'algorithmically built artist/metadata page, not curated coverage',
    'SEO DOORWAY ON HIJACKED SITE': 'injected doorway on a compromised, unrelated site using the name as bait',
    'USER-GENERATED LIST / QUIZ / CHART': 'community list, quiz or chart: mentions rather than journalism',
    'SOCIAL / FORUM MENTION': 'social or forum mention: reach without editorial review',
    'ARCHIVE SNAPSHOT': 'archival snapshot of a primary record, not an independent placement',
    'PAY-TO-PLAY CREDS MERCHANT': 'paid listing / cred-marketing platform: listing purchased, not awarded',
    'SCRAPE / MIRRORED MUSIC DATABASE': 'auto-mirrored database entry or AI-listing clone',
}
flag_rows = [[para(f'<b>{esc(k)}</b>', 'cell'), para(f'{v}', 'cell', TA_RIGHT),
              para(esc(FLAG_DEF.get(k, '')), 'cell', colour=SOFT)] for k, v in flag_ct.most_common()]
story += [Spacer(1, 3.4 * mm),
          grid(flag_rows, [58 * mm, 14 * mm, CW - 96 * mm],
               header=['INTEGRITY FLAG (printed in red inside the row)', 'N', 'WHY THE ROW IS MARKED DOWN'],
               zebra=True, font=6.6)]

story.append(PageBreak())

# =========================================================== DASHBOARD
left_rows = [[para(f'<b>{esc(s)}</b>', 'cell'), para(str(len(by_section[s])), 'cell', TA_RIGHT),
              para(f'{sum(1 for x in by_section[s] if x["tier"] == "A")}', 'cell', TA_RIGHT),
              para(f'{sum(1 for x in by_section[s] if x["status"] in ("verified", "live"))}', 'cell', TA_RIGHT),
              para(str(len({x["host"] for x in by_section[s]})), 'cell', TA_RIGHT),
              para(f'{max(x["score"] for x in by_section[s])} / {min(x["score"] for x in by_section[s])}',
                   'cell', TA_RIGHT, colour=SOFT)] for s in sections]
dash_l = grid(left_rows, [52 * mm, 12 * mm, 12 * mm, 16 * mm, 14 * mm, 18 * mm],
              header=['SECTION', 'LINKS', 'TIER A', 'LIVE', 'HOSTS', 'CRED hi / lo'], zebra=True, font=6.6)

topic_rows = [[para(f'<b>{esc(t)}</b>', 'cell'), para(str(n), 'cell', TA_RIGHT),
               para(', '.join(f'{c.split(",")[0][:18]} {v}' for c, v in
                              Counter(x['category'] for x in recs if x['topic'] == t).most_common(3)),
                    'cell', colour=SOFT)]
              for t, n in topic_ct.most_common()]
dash_r = grid(topic_rows, [56 * mm, 12 * mm, CW * 0.36], header=['SUBJECT / TOPIC', 'N', 'WHERE IT CONCENTRATES'],
              zebra=True, font=6.5)

half = CW * 0.5 - 2 * mm
story += [Marker('front:dash', 'Dashboard'),
          banner('DASHBOARD — what the census actually contains', size=11,
                 sub='all counts are of unique URLs after de-duplication, truncation-collapse and quarantine re-bucketing'),
          Spacer(1, 3 * mm),
          Table([[dash_l, '', dash_r]], colWidths=[half, 4 * mm, half])]

# credibility ladder: one scaled A/B/C/D bar per section, laid out in two columns so the whole corpus fits one page
lad_rows, lad_extra = [], []
for i, sec in enumerate(sections):
    c = Counter(x['tier'] for x in by_section[sec])
    n = sum(c.values()) or 1
    cells, widths, colr = [], [], []
    for t in 'ABCD':
        if c[t]:
            frac = c[t] / n
            label = f'{t} {c[t]}' if frac > 0.2 else (t if frac > 0.09 else '')
            cells.append(para(f'<para alignment="center"><font color="#ffffff" size="5.2"><b>{label}</b></font></para>',
                              'cell', colour=colors.white))
            widths.append(66 * mm * frac)
            colr.append(TIER[t][0])
    bar = Table([cells], colWidths=widths, rowHeights=[4.0 * mm], hAlign='LEFT') if cells else para('', 'cell')
    if cells:
        bar.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                                 ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                                 ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                 ('GRID', (0, 0), (-1, -1), 0.4, colors.white)]
                                + [('BACKGROUND', (k, 0), (k, 0), colr[k]) for k in range(len(cells))]))
    rs = by_section[sec]
    live = sum(1 for x in rs if x['status'] in ('verified', 'live'))
    lad_rows.append([para(f'<b>{esc(sec)}</b><br/><font color="#5b6674" size="5.6">{len(rs)} links · '
                          f'{sum(1 for x in rs if x["score"] >= 62)} scoring 62+ · {live} live-verified</font>', 'cell'),
                     bar])
half = (len(lad_rows) + 1) // 2
lad_w = (CW - 8 * mm) / 2
lad_tbls = [grid(lad_rows[:half], [lad_w - 70 * mm, 70 * mm], header=['SECTION', 'TIER SPLIT — A USABLE, B SUPPORTING, C CONTEXT, D QUARANTINE'],
                 zebra=True, font=6.4, extra=[('VALIGN', (1, 1), (1, -1), 'MIDDLE')]),
            grid(lad_rows[half:], [lad_w - 70 * mm, 70 * mm], header=['SECTION', 'TIER SPLIT — A USABLE, B SUPPORTING, C CONTEXT, D QUARANTINE'],
                 zebra=True, font=6.4, extra=[('VALIGN', (1, 1), (1, -1), 'MIDDLE')])]
lad_pair = Table([[lad_tbls[0], '', lad_tbls[1]]], colWidths=[lad_w, 8 * mm, lad_w],
                 style=TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                                   ('RIGHTPADDING', (0, 0), (-1, -1), 0)]))

story += [Spacer(1, 4 * mm),
          banner('THE CREDIBILITY LADDER — how every section splits across tiers A to D', size=9.5,
                 sub='bar length is proportional to the tier mix of that section; the whole corpus in one picture',
                 right=f'{N} links'),
          Spacer(1, 2.2 * mm), lad_pair]

story.append(PageBreak())

# =========================================================== HALL OF FAME
hof = [r for r in recs if r['tier'] == 'A' and r['category'] != list(CAT_COLOR)[-1]]
hof.sort(key=lambda r: (-r['raw'], r['host']))
rows_h = []
for i, r in enumerate(hof[:40], 1):
    rows_h.append([para(f'<para alignment="right"><b>{i}</b></para>', 'cell'),
                   para(f'<b>{esc(r["host"])}</b>', 'cell'),
                   para(f'<b>{esc(r["title"][:110])}</b>' if r['title'] else '<i>—</i>', 'cell'),
                   para(esc(r['date'][:10]) or 'n/d', 'cell', colour=SOFT),
                   para(f'<font color="{heat(r["score"])[1]}"><b>{r["score"]}</b></font>', 'cell'),
                   para(f'<a href="{esc(r["url"])}" color="#1a3d8f">{esc(r["url"][:150])}</a>', 'url')])
story += [Marker('front:hall', 'Hall of Fame — the 40 strongest records'),
          banner('HALL OF FAME — the 40 strongest independent and institutional records in the whole census',
                 colour='#0b6e4f', size=11,
                 sub='tier A, not self-published, not quarantined: press, awards, festivals, museums, academic and platform-of-record entries'),
          Spacer(1, 3 * mm),
          grid(rows_h, [8 * mm, 34 * mm, 108 * mm, 15 * mm, 12 * mm, CW - 177 * mm],
               header=['RANK', 'OUTLET', 'RECORD', 'DATE', 'CRED', 'LINK'], zebra=True, font=6.6)]

story.append(PageBreak())

# =========================================================== CONTENTS
FRONT = [('F', 'Front matter · How to read this volume', 'colour legend: tiers, credibility bands, status chips, integrity flags', 'front:howto', '#5b6674'),
         ('F', 'Front matter · Dashboard', 'what the census contains, per section and per topic, with the credibility ladder', 'front:dash', '#5b6674'),
         ('F', 'Front matter · Hall of Fame', 'the forty strongest individual placements, ranked', 'front:hall', '#5b6674')]
PATHS_TOC = [(str(i), f'Reading path {i} · {p["name"].title()}', p['sub'],
              p['key'], ['#e8710a', '#c2185b', '#d93025', '#6a1b9a', '#00796b'][i - 1])
             for i, p in enumerate(READING_PATHS, 1)]
APS = [('A', 'Appendix A · Complete alphabetical link register', 'every one of the 715 links in one alphabetical run, two per row', 'app:A', '#0b5d8f'),
       ('B', 'Appendix B · Topic & subject cross-index', 'the same corpus re-cut by what each record is about, with its best rows', 'app:B', '#5e35b1'),
       ('C', 'Appendix C · Quarantine map by domain', 'the 116 quarantined rows grouped by the domain that poisoned them', 'app:C', '#616161'),
       ('D', 'Appendix D · Method, provenance & limits', 'how the census was built and scored, engines used, and what it does not claim', 'app:D', '#00695c')]
toc_rows = [[para(f'<para alignment="center"><b>{chip}</b></para>', 'cell', colour=colors.white),
             para(f'<b>{esc(title)}</b>', 'cell'),
             para(esc(blurb), 'cell', colour=SOFT), para('', 'cell'),
             para(f'<b>page {PAGEMAP.get(key, "—")}</b>', 'cell', TA_RIGHT, colour=INK if PAGEMAP.get(key) else SOFT)]
            for chip, title, blurb, key, _c in FRONT]
toc_rows += [[para(f'<para alignment="center"><font color="#ffffff" size="6"><b>{s[0]}</b></font></para>',
                  colour=colors.white),
             para(f'<b>{i}. {esc(s)}</b>', 'cell'),
             para(esc(SECTION_BLURB[s][:86]) + ('…' if len(SECTION_BLURB[s]) > 86 else ''), 'cell', colour=SOFT),
             para(str(len(by_section[s])), 'cell', TA_RIGHT),
             para(f'<b>page {PAGEMAP.get(f"section:{i}", "—")}</b>', 'cell', TA_RIGHT,
                  colour=INK if PAGEMAP.get(f'section:{i}') else SOFT)]
            for i, s in enumerate(sections, 1)] + [
            [para(f'<para alignment="center"><font color="#ffffff" size="6"><b>P{chip}</b></font></para>',
                  colour=colors.white),
             para(f'<b>{esc(title)}</b>', 'cell'),
             para(esc(blurb[:86]) + ('…' if len(blurb) > 86 else ''), 'cell', colour=SOFT),
             para(str(len(READING_PATHS[int(chip) - 1]['rows'])), 'cell', TA_RIGHT),
             para(f'<b>page {PAGEMAP.get(key, "—")}</b>', 'cell', TA_RIGHT, colour=INK if PAGEMAP.get(key) else SOFT)]
            for chip, title, blurb, key, _c in PATHS_TOC] + [
            [para(f'<para alignment="center"><b>{chip}</b></para>', 'cell', colour=colors.white),
             para(f'<b>{esc(title)}</b>', 'cell'),
             para(esc(blurb), 'cell', colour=SOFT), para('', 'cell'),
             para(f'<b>page {PAGEMAP.get(key, "—")}</b>', 'cell', TA_RIGHT, colour=INK if PAGEMAP.get(key) else SOFT)]
            for chip, title, blurb, key, _c in APS]
NF, NA, NS, NP = len(FRONT), len(APS), len(sections), len(PATHS_TOC)
toc_extra = [('BACKGROUND', (0, 1), (-1, NF), colors.HexColor('#eef2f7')),
             ('BACKGROUND', (0, NF + NS + NP + 1), (-1, NF + NS + NP + NA), colors.HexColor('#eef2f7')),
             ('BACKGROUND', (0, 1), (0, NF), colors.HexColor('#5b6674')),
             ('LINEABOVE', (0, NF + 1), (-1, NF + 1), 0.7, INK),
             ('LINEABOVE', (0, NF + NS + 1), (-1, NF + NS + 1), 0.7, colors.HexColor('#3949ab')),
             ('LINEABOVE', (0, NF + NS + NP + 1), (-1, NF + NS + NP + 1), 0.7, INK),
             ('VALIGN', (0, 1), (0, -1), 'MIDDLE'),
             ('TOPPADDING', (0, 1), (-1, -1), 3), ('BOTTOMPADDING', (0, 1), (-1, -1), 3)]
toc_extra += [('BACKGROUND', (0, NF + 1 + i), (0, NF + 1 + i), colors.HexColor(CAT_COLOR[sec]))
              for i, sec in enumerate(sections)]
toc_extra += [('BACKGROUND', (0, NF + NS + 1 + k), (0, NF + NS + 1 + k), colors.HexColor(c))
              for k, (_chip, _t, _b, _key, c) in enumerate(PATHS_TOC)]
toc_extra += [('BACKGROUND', (0, NF + NS + NP + 1 + k), (0, NF + NS + NP + 1 + k), colors.HexColor(c))
              for k, (_chip, _t, _b, _key, c) in enumerate(APS)]
story += [banner('CONTENTS', size=11,
                 sub='the fourteen sections run from the most reputable kind of placement to the quarantine bucket; the five '
                     'reading paths (P1-P5) cut the same corpus into the requested themes; the four appendices re-sort every one '
                     'of the 715 links by domain, by subject, by quarantine cluster and by method'),
          Spacer(1, 3 * mm),
          grid(toc_rows, [7 * mm, 62 * mm, CW - 141 * mm, 16 * mm, 24 * mm], zebra=True, font=7.4, extra=toc_extra)]
story.append(PageBreak())

# =========================================================== FIVE HEADLINE READING PATHS
# complete, self-contained, ranked ledgers for the five requested themes. Every row repeats
# (in richer form) inside the main numbered sections; these paths exist so each requested
# topic can be read start-to-finish without hunting across the volume.
story += [Marker('path:0', 'Five headline reading paths — the requested thematic cuts'),
          banner('FIVE HEADLINE READING PATHS', colour='#263238', size=12,
                 sub='the master directory is organized by media type; these five paths re-cut the same 715 records into the '
                     'requested themes — netlabel + compilation features, magazine / zine features, news articles & media, '
                     'exhibitions & art galleries, literary publications & writing. Each path is COMPLETE for its theme and '
                     'ranked from the most reputable and impressive placement to the least. Every row below also appears with '
                     'full evidence notes in the numbered section named in its banner.',
                 right=f'{sum(len(p["rows"]) for p in READING_PATHS)} path rows (with overlap) · {N} unique links in the volume')]

overview_rows = []
for i, p in enumerate(READING_PATHS, 1):
    prs = p['rows']
    tc = Counter(x['tier'] for x in prs)
    overview_rows.append([para(f'<para alignment="center"><font color="#ffffff" size="8"><b>P{i}</b></font></para>',
                               colour=colors.white),
                          para(f'<b>{esc(p["name"])}</b><br/><font color="#5b6674" size="5.8">{esc(p["sub"][:120])}…</font>',
                               'cell'),
                          para(f'<b>{len(prs)}</b>', 'cell', TA_RIGHT),
                          para(f'A {tc["A"]} · B {tc["B"]} · C {tc["C"]} · D {tc["D"]}', 'cell', colour=SOFT),
                          para(f'{sum(1 for x in prs if x["status"] in ("verified", "live", "search-index verified"))}',
                               'cell', TA_RIGHT),
                          para(f'page {PAGEMAP.get(p["key"], "—")}', 'cell', TA_RIGHT, colour=SOFT)])
story += [Spacer(1, 2.5 * mm),
          grid(overview_rows, [10 * mm, CW - 148 * mm, 14 * mm, 52 * mm, 16 * mm, 24 * mm],
               header=['PATH', 'THEME (complete cut — every link in the corpus matching it)', 'LINKS', 'TIER SPLIT · A best, D quarantine',
                       'LIVE', 'STARTS'],
               zebra=True, font=6.8,
               extra=[('BACKGROUND', (0, i), (0, i), colors.HexColor(p_['colour']))
                      for i, p_ in enumerate(READING_PATHS, 1)] +
                     [('TOPPADDING', (0, 0), (-1, -1), 2.6), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6),
                      ('VALIGN', (0, 0), (0, -1), 'MIDDLE')])]
story.append(PageBreak())

PATH_COLW = [10 * mm, 36 * mm, 79 * mm, 8 * mm, 11 * mm, 14 * mm, CW - 158 * mm]
sec_no = {s: i for i, s in enumerate(sections, 1)}
for pi, p in enumerate(READING_PATHS, 1):
    if pi > 1:
        story.append(PageBreak())
    prs = p['rows']
    tc = Counter(x['tier'] for x in prs)
    live_n = sum(1 for x in prs if x['status'] in ('verified', 'live', 'search-index verified'))
    main_page = PAGEMAP.get(f'section:{sec_no.get(p["main"], 0)}', '—')
    story.append(Marker(p['key'], f'Path {pi} — {p["name"].title()}'))
    story.append(banner(f'PATH P{pi} · {p["name"]}', colour=p['colour'], size=12,
                        sub=p['sub'],
                        right=f'{len(prs)} links · A {tc["A"]} · B {tc["B"]} · C {tc["C"]} · D {tc["D"]} · live {live_n}'))
    story.append(Spacer(1, 1.6 * mm))
    story.append(para(f'<font color="#5b6674">complete ranked cut for this theme — most reputable and impressive first. '
                       f'The bold number is the position inside this path; the small <i>vol</i> number under it is the row\'s '
                       f'rank in the whole volume; CRED is the 0-100 credibility index. Full evidence rows for these links: '
                       f'§{sec_no.get(p["main"], "?")} <b>{esc(p["main"])}</b> (page {main_page}); quarantined rows are '
                       f'expanded again by domain in Appendix C.</font>', 'legend'))
    story.append(Spacer(1, 1.6 * mm))
    # outlet cluster line for long paths
    if len(prs) > 24:
        hc = Counter(x['host'] for x in prs)
        chips = '  ·  '.join(f'<b>{esc(h)}</b> ({n})' for h, n in hc.most_common(16))
        more = len(hc) - 16
        story.append(Table([[para('OUTLETS / HOSTS ON THIS PATH:  ' + chips + (f'  ·  +{more} more' if more > 0 else ''),
                                   'legend', colour=SOFT)]], colWidths=[CW],
                           style=TableStyle([('BACKGROUND', (0, 0), (-1, -1), BAND),
                                             ('BOX', (0, 0), (-1, -1), 0.3, RULE),
                                             ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                                             ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)])))
        story.append(Spacer(1, 2.4 * mm))
    data = [[para('<b>#</b>', 'th', colour=colors.white, align=TA_CENTER),
             para('<b>OUTLET · HOST</b>', 'th', colour=colors.white),
             para('<b>FEATURE / APPEARANCE</b>', 'th', colour=colors.white),
             para('<b>TIER</b>', 'th', colour=colors.white, align=TA_CENTER),
             para('<b>CRED</b>', 'th', colour=colors.white, align=TA_CENTER),
             para('<b>STATUS</b>', 'th', colour=colors.white, align=TA_CENTER),
             para('<b>FULL LINK (clickable)</b>', 'th', colour=colors.white)]]
    styles = [('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(p['colour'])),
              ('VALIGN', (0, 0), (-1, -1), 'TOP'),
              ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#dde4ea')),
              ('LINEBELOW', (0, 0), (-1, 0), 0.6, HEADBG),
              ('LEFTPADDING', (0, 0), (-1, -1), 2.4), ('RIGHTPADDING', (0, 0), (-1, -1), 2.4),
              ('TOPPADDING', (0, 0), (-1, -1), 1.9), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.9)]
    for i, r in enumerate(prs, start=1):
        tier = r['tier'] if r['tier'] in TIER else 'C'
        cfill, ctext = heat(r['score'])
        sfill, slab = STATUS.get(r['status'], (SOFT, (r['status'] or '?').upper()))
        title_bits = []
        if r['title']:
            title_bits.append(f'<b>{esc(r["title"][:120])}</b>')
        if r['date']:
            title_bits.append(f'<font color="#78909c">{esc(r["date"][:10])}</font>')
        ctx = r['category'] if r['category'] != p['main'] else None
        if ctx:
            title_bits.append(f'<font color="#8a6d3b">also filed under: {esc(ctx[:60])}</font>')
        if r.get('flag_reasons'):
            title_bits.append('<font color="#8c1d18"><b>FLAG</b> ' + esc(r['flag_reasons'][0][:110]) + '</font>')
        data.append([para(f'<para alignment="right"><font color="#263238" size="6.8"><b>{i}</b></font><br/>'
                          f'<font color="#9aa7b2" size="5">vol {r["rank"]}</font></para>'),
                     para(f'<b>{esc(r["host"])}</b>', 'cell'),
                     para(' · '.join(title_bits) if title_bits else '<font color="#b0bac4">—</font>'),
                     para(f'<para alignment="center"><font color="#ffffff" size="7"><b>{tier}</b></font></para>',
                          colour=colors.white),
                     para(f'<para alignment="center"><font color="{ctext}" size="6.6"><b>{r["score"]}</b></font></para>'),
                     para(f'<para alignment="center"><font color="#ffffff" size="5.4"><b>{slab}</b></font></para>',
                          colour=colors.white),
                     para(f'<a href="{esc(r["url"])}" color="#1a3d8f">{esc(r["url"])}</a>', 'url')])
        styles += [('BACKGROUND', (0, i), (-1, i), TIER[tier][1]),
                   ('BACKGROUND', (3, i), (3, i), TIER[tier][0]),
                   ('BACKGROUND', (4, i), (4, i), cfill),
                   ('BACKGROUND', (5, i), (5, i), sfill),
                   ('LINEBEFORE', (0, i), (0, i), 2.2, colors.HexColor(p['colour']))]
    tbl = Table(data, colWidths=PATH_COLW, repeatRows=1)
    tbl.setStyle(TableStyle(styles))
    story.append(tbl)

story.append(PageBreak())
# =========================================================== SECTIONS
for si, s in enumerate(sections, 1):
    rs = by_section[s]
    if si > 1:
        story.append(PageBreak())
    colour = colors.HexColor(CAT_COLOR[s])
    band = banner(f'§{si}  {s}', colour=colour, size=12.5, sub=SECTION_BLURB[s],
                  right=f'{len(rs)} links · tier A {sum(1 for x in rs if x["tier"] == "A")} · B {sum(1 for x in rs if x["tier"] == "B")} · '
                        f'C {sum(1 for x in rs if x["tier"] == "C")} · D {sum(1 for x in rs if x["tier"] == "D")} · live {sum(1 for x in rs if x["status"] in ("verified", "live"))}')
    story.append(band)
    story.append(Marker(f'section:{si}', f'§{si} {s}'))
    story.append(Spacer(1, 1.6 * mm))
    story.append(para(f'<font color="#5b6674">rows are ordered by credibility — highest first; RANK is the position of the '
                       f'row in the whole volume, CRED is its 0-100 credibility index. Ties are broken alphabetically by host.</font>',
                       'legend'))
    story.append(Spacer(1, 1.6 * mm))

    # host cluster overview for long sections
    hc = Counter(x['host'] for x in rs)
    if len(hc) > 3:
        chips = [f'<b>{esc(h)}</b> ({n})' for h, n in hc.most_common(14)]
        extra = len(hc) - 14
        txt = ('OUTLETS / HOSTS IN THIS SECTION:  ' + '  ·  '.join(chips)
               + (f'  ·  +{extra} more' if extra > 0 else ''))
        box = Table([[para(txt, 'legend', colour=SOFT)]], colWidths=[CW])
        box.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), BAND), ('BOX', (0, 0), (-1, -1), 0.3, RULE),
                                 ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                                 ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
        story.append(box)
        story.append(Spacer(1, 2.6 * mm))

    data = [[para(f'<b>{h}</b>', 'th',
                  colour=colors.white,
                  align=TA_CENTER if i in (1, 2, 7) else TA_LEFT) for i, h in enumerate(HEADERS)]]
    styles = [('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(CAT_COLOR[s])),
              ('VALIGN', (0, 0), (-1, -1), 'TOP'),
              ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#dde4ea')),
              ('LINEBELOW', (0, 0), (-1, 0), 0.6, HEADBG),
              ('LEFTPADDING', (0, 0), (-1, -1), 2.4), ('RIGHTPADDING', (0, 0), (-1, -1), 2.4),
              ('TOPPADDING', (0, 0), (-1, -1), 2.0), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.0)]
    for i, r in enumerate(rs, start=1):
        row, meta = rec_row(r)
        tint, tier_fill, cfill, sfill = meta
        data.append(row)
        styles += [('BACKGROUND', (0, i), (-1, i), tint),
                   ('BACKGROUND', (1, i), (1, i), tier_fill),
                   ('BACKGROUND', (2, i), (2, i), cfill),
                   ('BACKGROUND', (7, i), (7, i), sfill),
                   ('LINEBEFORE', (0, i), (0, i), 2.2, colors.HexColor(CAT_COLOR[s]))]
    tbl = Table(data, colWidths=COLW, repeatRows=1)
    tbl.setStyle(TableStyle(styles))
    story.append(tbl)

# =========================================================== APPENDIX A — full alphabetical register
story.append(PageBreak())
by_host = defaultdict(list)
for r in recs:
    by_host[r['host']].append(r)

story.append(Marker('app:A', 'Appendix A — alphabetical link register'))
story.append(banner('APPENDIX A — COMPLETE ALPHABETICAL LINK REGISTER', size=11, colour='#0b5d8f',
                    sub=f'all {N} unique URLs printed in full and clickable, sorted by host then URL — the completeness '
                        'check for the volume; [#] is the ranked row number above',
                    right='tier · credibility · status in the right-hand mini-columns'))
story.append(Spacer(1, 3 * mm))

flat = []
for h in sorted(by_host):
    for r in sorted(by_host[h], key=lambda x: x['url']):
        flat.append(r)
half_n = (len(flat) + 1) // 2
left, right = flat[:half_n], flat[half_n:]


SHORT_STATUS = {'LIVE': 'LIVE', 'IDX-OK': 'IDX', 'PARTIAL': 'PART', 'UNCHECKED': 'UNCK',
                'DO-NOT-OPEN': 'SAFE', 'BROKEN': 'DEAD', 'LEAD': 'LEAD'}


def apx_line(r):
    tint = TIER[r['tier'] if r['tier'] in TIER else 'C'][1]
    return Table([[para(f'<font color="#0b5d8f"><b>{r["rank"]}</b></font>', 'cell'),
                   para(f'<b>{esc(r["host"])}</b>', 'cell'),
                   para(f'<a href="{esc(r["url"])}" color="#1a3d8f">{esc(r["url"])}</a>', 'apx'),
                   para(f'<font color="{heat(r["score"])[1]}"><b>{r["tier"]}</b> {r["score"]}</font>', 'cell'),
                   para(f'<font color="#5b6674">{SHORT_STATUS.get((STATUS.get(r["status"]) or (None, "UNCHECKED"))[1], "UNCK")}</font>', 'cell')]],
                 colWidths=[8.5 * mm, 26 * mm, CW / 2 - 56.5 * mm, 9 * mm, 13 * mm],
                 style=TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                   ('LEFTPADDING', (0, 0), (-1, -1), 1.6), ('RIGHTPADDING', (0, 0), (-1, -1), 2.4),
                                   ('TOPPADDING', (0, 0), (-1, -1), 1.1), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.1),
                                   ('BACKGROUND', (0, 0), (-1, -1), tint)]))


rows_a = []
for i in range(half_n):
    rows_a.append([apx_line(left[i]), apx_line(right[i]) if i < len(right) else ''])
tA = Table(rows_a, colWidths=[CW / 2, CW / 2],
           style=TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('ROWBACKGROUNDS', (0, 0), (-1, -1),
                            [colors.white, colors.HexColor('#f7f9fb')]),
                             ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 3),
                             ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0.8),
                             ('LINEAFTER', (0, 0), (0, -1), 0.4, RULE)]))
story.append(tA)


# =========================================================== APPENDIX B — topic / subject cross-index
story.append(PageBreak())
story.append(Marker('app:B', 'Appendix B — topic & subject cross-index'))
story.append(banner('APPENDIX B — TOPIC & SUBJECT CROSS-INDEX', size=11, colour='#5e35b1',
                    sub='the same 715 links re-cut by what they are about rather than where they live: each topic shows its '
                        'tier mix, the sections it spans and its strongest individual records',
                    right=f'{len(topic_ct)} topics'))
story.append(Spacer(1, 3 * mm))

by_topic = defaultdict(list)
for r in recs:
    by_topic[r['topic']].append(r)
tp_rows = []
for t, rs in sorted(by_topic.items(), key=lambda kv: -len(kv[1])):
    rs = sorted(rs, key=lambda x: -x['raw'])
    c = Counter(x['tier'] for x in rs)
    secs = Counter(x['category'] for x in rs)
    tier_html = '  '.join(f'<font color="{TIER[k][0].hexval().replace("0x", "#")[:7]}"><b>{k} {v}</b></font>'
                          for k, v in sorted(c.items()))
    sec_html = '<br/>'.join(f'<font color="#5b6674">{esc(k[:34])} <b>{v}</b></font>' for k, v in secs.most_common(5))
    best = rs[0]
    links_html = []
    for x in rs[:8]:
        head = esc((x['title'] or x['host'])[:78])
        links_html.append(f'<font color="#0b5d8f"><b>#{x["rank"]}</b></font> <b>{esc(x["host"])}</b> — {head} '
                          f'<a href="{esc(x["url"])}" color="#1a3d8f">{esc(x["url"][:150])}</a> '
                          f'<font color="{heat(x["score"])[1]}">[{x["tier"]}·{x["score"]}]</font>')
    rest = len(rs) - 8
    if rest > 0:
        links_html.append(f'<font color="#5b6674"><i>+ {rest} further rows in this topic — printed in the section tables above</i></font>')
    tp_rows.append([para(f'<b>{esc(t)}</b><br/><font color="#5b6674" size="5.8">{len(rs)} links</font>', 'cell'),
                    para(tier_html, 'cell'),
                    para(sec_html, 'cell'),
                    para('<br/>'.join(links_html), 'cell')])
story.append(grid(tp_rows, [40 * mm, 22 * mm, 34 * mm, CW - 96 * mm],
                  header=['TOPIC', 'TIER MIX', 'WHERE IT LIVES', 'STRONGEST RECORDS IN THIS TOPIC (clickable)'],
                  zebra=True, font=6.4,
                  extra=[('LINEBELOW', (0, 0), (-1, -1), 0.5, RULE)]))

# =========================================================== APPENDIX C — quarantined domain map
story.append(PageBreak())
spamrs = by_section.get('Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust', [])
sh = Counter(x['host'] for x in spamrs)
rows_q = []
for h, n in sh.most_common():
    rs = [x for x in spamrs if x['host'] == h]
    subs = Counter()
    for x in rs:
        for f in x.get('flags', []):
            subs[f] += 1
    rows_q.append([para(f'<b>{esc(h)}</b>', 'cell'), para(str(n), 'cell', TA_RIGHT),
                   para(esc(', '.join(f'{k} {v}' for k, v in subs.most_common(3))) or 'quarantine register row',
                        'cell', colour=SOFT),
                   para('<br/>'.join(f'<a href="{esc(x["url"])}" color="#8c1d18">{esc(x["url"][:120])}</a>'
                                     for x in sorted(rs, key=lambda y: y['url'])), ST['apx'])])
story.append(Marker('app:C', 'Appendix C — quarantine map by domain'))
story += [banner('APPENDIX C — QUARANTINE MAP BY DOMAIN', colour='#616161', size=11,
                 sub='what the contamination looks like, host by host. Nothing in this appendix is evidence of press, '
                      'credits or biography; it exists so the takedown/correction work and future dedupe have a source of truth.',
                 right=f'{len(spamrs)} quarantined links across {len(sh)} domains'),
          Spacer(1, 3 * mm),
          grid(rows_q, [40 * mm, 12 * mm, 62 * mm, CW - 114 * mm],
               header=['DOMAIN', 'LINKS', 'DOMINANT INTEGRITY FLAGS', 'EXACT URLS BEING QUARANTINED'],
               zebra=True, font=6.4)]

# =========================================================== APPENDIX D — method, provenance, endpoints
story.append(PageBreak())
story.append(Marker('app:D', 'Appendix D — method, provenance & limits'))
story.append(banner('APPENDIX D — HOW THIS VOLUME WAS BUILT, AND WHAT IT DOES NOT CLAIM', size=11,
                    colour='#0f9d8f', sub='read this before quoting any number in the directory'))
story.append(Spacer(1, 3 * mm))

METHOD = (
    '<b>SCOPE.</b> One row per unique public-web URL on which the exact strings <i>Zazie Productions</i> or '
    '<i>Zazie Kanwar-Torge</i> were observed or recorded by the census. Repository-wide inclusion rule: a handle without '
    'the space, the French singer Zazie, Zazie Films or any other same-name entity is <b>not</b> a record; variant '
    'spellings are kept only where the source itself prints the exact string.'
    '<br/><br/><b>SOURCES MERGED FOR THIS PDF.</b> {nsrc} source files contributed: the curated '
    '<font face="Courier">data/master/master_index.csv</font> (authoritative tier, category, status, date, notes), the '
    'structured <font face="Courier">Zazie_Media_Master (1).pdf</font> table rows (priority, publication, headline, '
    'exact-name field), the raw <font face="Courier">Random Zazie Productions links .pdf</font> annotations and text '
    'lines, the 2026 Accomplishment Register docx hyperlinks, the low-trust quarantine ledger, the magazine/zine feature '
    'directory, the regional and alt-engine pass, the web-presence expansion files, the phase-three editorial tables, '
    'the listen-link CSV and every registry markdown index. URLs that a registry had truncated for display were folded '
    'back into their full form rather than counted twice.'
    '<br/><br/><b>RANKING.</b> credibility = 46 + tier weight (A 42 / B 26 / C 10 / D -34) + section weight + '
    'host-authority weight + verification-status weight + exact-name-target weight - integrity-flag penalties, then '
    'min-max mapped onto 0-100 for the coloured cell. Sections run in credibility-ladder order (independent editorial '
    'press first, quarantine last) and rows inside every section are re-ranked by the same score, so the volume reads '
    'top-down from most impressive to most spammy.'
    '<br/><br/><b>QUARANTINE.</b> Tier D rows come from the repository\u2019s own low-trust register: hacked-site doorways, '
    'scraped clones, auto-generated metadata, paste reposts, embed farms and pirate mirrors. They are printed with their '
    'URLs so the contamination is documented and reportable; the text of those pages is never treated as information '
    'about the artist. Rows elsewhere that carry red <b>FLAG</b> text still count, but the flag states honestly what kind '
    'of placement they are (pay-to-play PR wire, self-published page, wiki mirror, archive snapshot, user quiz ...).'
    '<br/><br/><b>WHAT IS NOT CLAIMED.</b> No exhaustiveness: print-only, private, paywalled, deleted, unindexed or '
    'region-blocked presence cannot be enumerated, so absence in this volume means "not found on the census date", never '
    '"does not exist". Inclusion proves that a public record naming the artist exists; it does <b>not</b> validate any '
    'award, review, biography or claim made by that source. Search endpoints, API probes and archive lookups are method '
    'artefacts: they appear at the bottom of this appendix and are not counted as media features.'
)

story.append(Table([[para(METHOD.format(nsrc=len(src_ct)), 'legend')]], colWidths=[CW],
                   style=TableStyle([('BOX', (0, 0), (-1, -1), 0.4, RULE), ('BACKGROUND', (0, 0), (-1, -1), BAND),
                                     ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                                     ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)])))
story.append(Spacer(1, 4 * mm))

ROLE_NOTE = {
    'master_index': 'authoritative bucket, tier, status and evidence notes for every row it holds',
    'media_master_pdf': 'supplies Priority A/B/C, dates and publication headlines for the verified 133-record master',
    'link_dump_pdf': 'raw research dump: adds links the curated master never kept, and is where the quarantine material starts',
    'accomplishment_register_docx': 'register hyperlinks: relationship and outlet confirmations',
    'data/master/listen_links.csv': 'one listen link per compilation credit — fills the music-compilations section',
}
prov_rows = []
for k, v in src_ct.most_common():
    prov_rows.append([para('<font face="Courier">' + esc(k) + '</font>', 'cell'),
                      para(str(v), 'cell', TA_RIGHT),
                      para(esc(ROLE_NOTE.get(k, 'registry pass file: corroborating links, evidence notes and re-tiering')),
                           'cell', colour=SOFT)])
story.append(grid(prov_rows, [96 * mm, 14 * mm, CW - 110 * mm],
                  header=['SOURCE FILE CONTRIBUTING LINKS TO THIS VOLUME', 'LINKS', 'ROLE IN THE RANKING'],
                  zebra=True, font=6.6))
story.append(PageBreak())

en_rows = [[para(f'<b>{esc(e["host"])}</b>', 'cell'),
            para(f'<a href="{esc(e["url"])}" color="#1a3d8f">{esc(e["url"])}</a>', 'url'),
            para(esc(', '.join(e['sources'])[:120]), 'cell', colour=SOFT)] for e in engines]
story.append(banner('APPENDIX D.2 — SEARCH ENGINES, INDEX PROBES & ARCHIVE LOOKUPS USED BY THE CENSUS', size=10,
                    colour='#0f9d8f', sub='method endpoints, not media records — reproduced so the census can be re-run',
                    right=f'{len(engines)} endpoints'))
story.append(Spacer(1, 3 * mm))
story.append(grid(en_rows, [34 * mm, CW - 92 * mm, 58 * mm],
                  header=['ENDPOINT', 'QUERY / LOOKUP URL', 'LOGGED IN'], zebra=True, font=6.3))
story.append(Spacer(1, 4 * mm))
END_NOTE = (f'<font color="#ffffff"><b>END OF VOLUME.</b> {N} unique links · {tier_ct["A"]} tier A · {tier_ct["B"]} tier B · '
            f'{tier_ct["C"]} tier C · {tier_ct["D"]} quarantined · {len(host_ct)} domains · {len(topic_ct)} subject topics · '
            f'compiled from the repository census on {date.today():%d %B %Y}. Rebuild with '
            f'<font face="Courier">python3 scripts/ingest_all_links.py &amp;&amp; python3 scripts/build_master_directory_pdf.py</font></font>')
story.append(Table([[para(END_NOTE, 'legend', colour=colors.white)]], colWidths=[CW],
                   style=TableStyle([('BACKGROUND', (0, 0), (-1, -1), INK), ('LEFTPADDING', (0, 0), (-1, -1), 6),
                                     ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)])))


# --------------------------------------------------------------------------- build
doc = DirDoc(OUT, pagesize=PAGE, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
             title='Zazie Productions / Zazie Kanwar-Torge — Colour-Coded Master Directory of Media Features',
             author='Zazie Productions backlink census', subject='Exact-name public-web census, ranked by credibility')


def build():
    import io
    from reportlab.pdfgen import canvas as canvasmod

    class NCanvas(canvasmod.Canvas):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self._saved = []

        def showPage(self):
            self._saved.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            total = len(self._saved)
            for st in self._saved:
                self.__dict__.update(st)
                super().showPage()
            super().save()

    doc.build(story, canvasmaker=NCanvas)
    write_outline()


def write_outline():
    """Give the PDF a real bookmark tree using the page numbers measured during the build."""
    try:
        import pymupdf
    except Exception:
        return
    d = pymupdf.open(OUT)
    toc = [[1, title[:90], PAGEMAP[key]] for key, title in OUTLINE if key in PAGEMAP]
    if toc:
        d.set_toc(toc)
        d.set_metadata({'title': 'Zazie Productions / Zazie Kanwar-Torge — Colour-Coded Master Directory of Media Features',
                        'author': 'Zazie Productions backlink census',
                        'subject': 'Exact-name public-web census, 715 links ranked by credibility',
                        'keywords': 'backlinks, media features, credibility ranking, press, quarantine'})
        tmp = OUT + '.tmp'
        d.save(tmp, garbage=3, deflate=True)
        d.close()
        import os
        os.replace(tmp, OUT)
    else:
        d.close()


def page_count():
    import pymupdf
    return pymupdf.open(OUT).page_count


build()

if not HAVE_MAP and PAGEMAP:
    # pass 1 done: page numbers recorded — re-exec so the story is rebuilt from scratch with them
    with open(PAGEMAP_CACHE, 'w', encoding='utf-8') as fh:      # flushed before execv replaces the process
        json.dump(PAGEMAP, fh, indent=1)
    print('pass 1 complete: page map recorded, re-running for the contents page numbers')
    os.execv(sys.executable, [sys.executable, os.path.abspath(__file__)])

print('wrote', OUT, f'{os.path.getsize(OUT) / 1024:.0f} KB', '·', page_count(), 'pages ·',
      N, 'links ·', len(sections), 'sections')
