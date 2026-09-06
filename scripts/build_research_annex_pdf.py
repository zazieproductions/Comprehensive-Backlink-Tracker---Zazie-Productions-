#!/usr/bin/env python3
"""Build the colour-coded Research Annex PDF — the companion volume to the Master Directory.

Input : data/master/consolidated_directory.json  (counts + engine endpoints)
        data/master/*.csv, data/research/*.csv, registry/**/*.csv   (all pass registries)
Output: Zazie_Research_Annex_COLOUR_CODED.pdf    (repository root)

Everything that used to live in the repository's markdown research notes — the engine
audits, the pass reports, the evidence ledgers, the quarantine charter, the register
link map, the listen links and the query inventories — is printed here as long,
organised, colour-coded tables with every link clickable. The volume is the durable
PDF form of the census's research record; the CSV registries remain the machine-readable
source of truth.

Usage:  python3 scripts/build_research_annex_pdf.py
"""
import csv
import glob
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
from reportlab.platypus import (BaseDocTemplate, Frame, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'Zazie_Research_Annex_COLOUR_CODED.pdf')

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

GREEN = colors.HexColor('#188038')
LGREEN = colors.HexColor('#eaf6ef')
AMBER = colors.HexColor('#b06000')
LAMBER = colors.HexColor('#fdf4e5')
RED = colors.HexColor('#b3261e')
LRED = colors.HexColor('#fbeceb')
GREY = colors.HexColor('#7b8794')
LGREY = colors.HexColor('#eef1f4')
SLATE = colors.HexColor('#546e7a')
LSLATE = colors.HexColor('#eceff1')
BLUE = colors.HexColor('#1a73e8')
LBLUE = colors.HexColor('#eaf1fc')
BROWN = colors.HexColor('#8a6d3b')

CAT_COLOR = {'Press & Editorial': '#d93025', 'Publications & Recognition': '#7b1fa2',
             'Film, Festivals & Exhibitions': '#d81b60', 'Podcasts & Broadcasts': '#3949ab',
             'Profiles & Catalogs': '#1a73e8', 'Music Discography': '#c2185b',
             'Streaming & Music Platforms': '#039be5', 'Lyrics & Music Databases': '#00897b',
             'Music Compilations': '#e8710a', 'Official Properties & Channels': '#2e7d32',
             'Community, Wiki & Fan Indexes': '#188038', 'Search-Engine Index': '#0f9d8f',
             'Video Mirror / Backlink Sites': '#607d8b',
             'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust': '#616161'}

MEDIA_EMOJI = [('🔴', 'PRESS', '#d93025'), ('🌸', 'FILM', '#d81b60'), ('🟣', 'RECOGN', '#7b1fa2'),
               ('🔵', 'PROFILE', '#1a73e8'), ('🟠', 'MUSIC', '#e8710a'), ('🩵', 'DATA', '#0f9d8f'),
               ('🟢', 'SOCIAL', '#188038'), ('📼', 'MIRROR', '#607d8b'), ('🖤', 'SPAM', '#616161'),
               ('🎙', 'PODCAST', '#3949ab')]

SUBTYPE_COLOR = {
    'TOOL-MIRROR': SLATE, 'SUSPICIOUS-MIRROR': SLATE, 'UNKNOWN-MIRROR': SLATE,
    'TYPOSQUAT-MIRROR': SLATE, 'LEGACY-MIRROR': SLATE, 'SYNDICATION-MIRROR': SLATE,
    'TOOL-PROFILE-MIRROR': SLATE, 'EMBED-CANONICAL': SLATE,
    'DOORWAY-INJECT': colors.HexColor('#8c1d18'), 'INJECTED-EMBED': colors.HexColor('#8c1d18'),
    'AUTOGEN-METADATA': colors.HexColor('#5d4037'), 'AUTOGEN-SEARCHURL': colors.HexColor('#5d4037'),
    'PASTE-REPUB': AMBER, 'PLATFORM-REPUB': AMBER, 'PR-FEED-REPUB': AMBER,
    'FABRICATED-ATTRIB': colors.HexColor('#4a148c'), 'MISATTRIB-FLAG': colors.HexColor('#4a148c'),
    'KEPT-BORDERLINE': colors.HexColor('#37474f'),
}

# --------------------------------------------------------------------------- styles
def S(name, **kw):
    kw.setdefault('fontName', 'Helvetica')
    kw.setdefault('fontSize', 7)
    kw.setdefault('leading', 8.4)
    kw.setdefault('textColor', INK)
    return ParagraphStyle(name, **kw)


ST = {
    'body': S('body', fontSize=8.4, leading=11),
    'cell': S('cell', fontSize=6.5, leading=7.8),
    'tiny': S('tiny', fontSize=5.8, leading=6.9),
    'url': S('url', fontName='Courier', fontSize=5.9, leading=7.0, wordWrap='CJK',
             textColor=colors.HexColor('#1a3d8f')),
    'th': S('th', fontName='Helvetica-Bold', fontSize=6.3, leading=7.6, textColor=colors.white),
    'legend': S('legend', fontSize=7.4, leading=9.6),
}

SPECIAL = {'‘': "'", '’': "'", '“': '"', '”': '"', '–': '-', '—': '-', '…': '...',
           '·': '-', ' ': ' ', '•': '-', '°': ' ', 'é': 'e', 'è': 'e', 'à': 'a',
           'ü': 'u', 'ö': 'o', 'ä': 'a', 'ñ': 'n', 'å': 'a', 'ß': 'ss', '±': '+-',
           '£': 'GBP ', '€': 'EUR ', '→': '->', '»': '>>', '«': '<<', '‚': "'",
           '„': '"', '◎': '(o)', '✔': '(v)', '○': '( )', '⛧': '*', 'Δ': 'D',
           'Ω': 'O', 'ø': 'o', '⬜': '', '✅': '', '❌': '', '🟡': '', '🔎': ''}


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
    t = ''.join(out)
    t = re.sub(r' {2,}', ' ', t)
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


URL_RX = re.compile(r'(https?://[^\s,;"\')\]>&]+(?:&amp;[^\s,;"\')\]>&]+)*)')


def linkify(t, colour='#1a3d8f'):
    """Escape text, then make every URL inside it clickable."""
    e = esc(t)
    return URL_RX.sub(lambda m: f'<a href="{m.group(1)}" color="{colour}">{m.group(1)}</a>', e)


def para(text, style='cell', align=None, colour=None):
    base = ST.get(style) if isinstance(style, str) else style
    st = dict(fontName=base.fontName, fontSize=base.fontSize, leading=base.leading,
              textColor=colour or base.textColor)
    if getattr(base, 'wordWrap', None):
        st['wordWrap'] = base.wordWrap
    if align:
        st['alignment'] = align
    return Paragraph(text, S('tmp', **st))


def chip(label, fill, size=5.6):
    return (para(f'<para alignment="center"><font color="#ffffff" size="{size}"><b>{esc(label)}</b></font></para>',
                 colour=colors.white), fill)


def access_chip(status):
    s = (status or '').lower()
    if s.startswith('worked') or '✅' in (status or '') or s == 'ok' or s.startswith('ok'):
        return chip('WORKED', GREEN)
    if s.startswith('blocked') or '❌' in (status or ''):
        return chip('BLOCKED', RED)
    if s.startswith('unreachable') or 'dead' in s or 'discontinued' in s or 'not testable' in s:
        return chip('UNREACHABLE', GREY)
    if 'zero' in s or 'no exact-name' in s or 'negative' in s or 'no relevant' in s:
        return chip('NO HITS', SLATE)
    if '⚠' in (status or '') or s.startswith('accessible') or 'login' in s or s.startswith('limited') \
            or 'partial' in s or 'reachable' in s:
        return chip('PARTIAL', AMBER)
    return chip((status or '?')[:12].upper(), GREY)


def live_chip(status):
    s = (status or '').lower()
    if s.startswith('verified') or s == 'live' or s.startswith('live') or 'confirmed' in s:
        return chip('LIVE', GREEN)
    if s.startswith('search-index'):
        return chip('IDX-OK', colors.HexColor('#0f9d58'))
    if 'partial' in s:
        return chip('PARTIAL', AMBER)
    if 'broken' in s or 'dead' in s or '404' in s:
        return chip('BROKEN', RED)
    if 'not-probed' in s or 'safety' in s:
        return chip('DO-NOT-OPEN', BROWN)
    if 'archived' in s:
        return chip('ARCHIVED', SLATE)
    if s.startswith('lead') or 'hunt' in s:
        return chip('LEAD', SLATE)
    if 'auth' in s:
        return chip('AUTH-GATED', GREY)
    if 'label' in s:
        return chip('LABEL', BLUE)
    if 'linked' in s:
        return chip('LINKED', GREEN)
    if 'unresolved' in s:
        return chip('UNRESOLVED', AMBER)
    return chip((status or 'UNCHECKED')[:12].upper() or 'UNCHECKED', GREY)


def tier_chip(tier):
    t = (tier or '').strip()
    m = re.search(r'\b([ABCD])\b', t)
    key = m.group(1) if m else (t[:1].upper() if t[:1].upper() in TIER else 'C')
    fill, tint = TIER.get(key, TIER['C'])
    p, _ = chip(key, fill)
    return p, fill, tint


PRIORITY_MAP = {'🥇': 'A', '🥈': 'B', '🥉': 'C', '🔎': 'LEAD'}


def priority_chip(p):
    p = p or ''
    for em, lab in PRIORITY_MAP.items():
        if em in p:
            fill = {'A': GREEN, 'B': BLUE, 'C': AMBER, 'LEAD': SLATE}[lab]
            return chip(lab, fill)
    if p.strip().upper().startswith('A'):
        return chip('A', GREEN)
    if p.strip().upper().startswith('B'):
        return chip('B', BLUE)
    return chip('C', AMBER)


def media_tags(cell):
    """Turn the emoji media column into coloured text tags."""
    tags = []
    for em, lab, col in MEDIA_EMOJI:
        if em in (cell or ''):
            tags.append(f'<font color="{col}"><b>{lab}</b></font>')
    return para(' '.join(tags) if tags else esc(cell or ''), 'cell')


def status_emoji_chip(cell):
    c = cell or ''
    if '✅' in c:
        return chip('LIVE', GREEN)[0]
    if '🟡' in c:
        return chip('PARTIAL', AMBER)[0]
    if '❌' in c:
        return chip('BROKEN', RED)[0]
    if '🔎' in c:
        return chip('LEAD', SLATE)[0]
    if '⬜' in c:
        return chip('UNCHECKED', GREY)[0]
    return para(esc(c), 'cell')


# --------------------------------------------------------------------------- document
PAGEMAP_CACHE = os.path.normpath(os.path.join(BASE, 'data', 'master', '.annex_pagemap.json'))
PAGEMAP = {}
HAVE_MAP = False
if os.path.exists(PAGEMAP_CACHE):
    try:
        PAGEMAP = json.load(open(PAGEMAP_CACHE, encoding='utf-8'))
        HAVE_MAP = bool(PAGEMAP)
    except Exception:
        PAGEMAP = {}
OUTLINE = []


class Marker(Paragraph):
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


def header_for_page(pageno):
    """Running-header title from the pass-1 page map (empty on pass 1 itself)."""
    best = ''
    for key, title in OUTLINE:
        p = PAGEMAP.get(key)
        if p and p <= pageno:
            best = title
    return best


class AnnexDoc(BaseDocTemplate):
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
        xs = ['#1a73e8', '#0f9d8f', '#5e35b1', '#c2185b', '#7b1fa2', '#00796b',
              '#616161', '#e8710a', '#039be5', '#2e7d32', '#8a6d3b', '#0b5d8f']
        w = PAGE[0] / len(xs)
        for i, c in enumerate(xs):
            cv.setFillColor(colors.HexColor(c))
            cv.rect(i * w, PAGE[1] - 47 * mm, w - 1.5, 3 * mm, stroke=0, fill=1)
        cv.setFillColor(colors.white)
        cv.setFont('Helvetica-Bold', 20)
        cv.drawString(LM, PAGE[1] - 20 * mm, 'ZAZIE PRODUCTIONS  ·  ZAZIE KANWAR-TORGE')
        cv.setFont('Helvetica', 12.5)
        cv.drawString(LM, PAGE[1] - 28.5 * mm,
                      'Research Annex — Engine Audits, Discovery Passes, Evidence Ledgers, Quarantine Register, Link Maps & Listen Links')
        cv.setFont('Helvetica', 9)
        cv.drawString(LM, PAGE[1] - 35 * mm,
                      'The complete research record of the exact-name census in one colour-coded volume — companion to the Master Directory of media features')
        cv.setFont('Helvetica-Bold', 7.8)
        cv.drawString(LM, PAGE[1] - 40.5 * mm,
                      'Every engine probed · every pass reported · every lead logged · every quarantine row documented · every link clickable')
        cv.setFillColor(SOFT)
        cv.setFont('Helvetica', 7.6)
        cv.drawCentredString(PAGE[0] / 2, BM - 5.5 * mm,
                             f'Compiled {date.today():%d %B %Y} from the repository census registries · research baseline dated through 2026-09-05')
        cv.restoreState()

    def body_deco(self, cv, doc):
        cv.saveState()
        cv.setStrokeColor(RULE)
        cv.setLineWidth(0.5)
        cv.line(LM, PAGE[1] - 13.5 * mm, PAGE[0] - RM, PAGE[1] - 13.5 * mm)
        cv.setFont('Helvetica-Bold', 6.6)
        cv.setFillColor(INK)
        cv.drawString(LM, PAGE[1] - 11.6 * mm, 'ZAZIE EXACT-NAME CENSUS — RESEARCH ANNEX')
        cv.setFont('Helvetica', 6.6)
        cv.setFillColor(SOFT)
        cv.drawRightString(PAGE[0] - RM, PAGE[1] - 11.6 * mm, header_for_page(doc.page)[:150])
        cv.line(LM, BM - 3.4 * mm, PAGE[0] - RM, BM - 3.4 * mm)
        cv.drawString(LM, BM - 8 * mm, f'page {doc.page}')
        cv.drawRightString(PAGE[0] - RM, BM - 8 * mm,
                           'companion volume to Zazie_Master_Directory_COLOUR_CODED.pdf')
        cv.restoreState()


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


def notebox(text, bg='#f7f9fc'):
    return Table([[para(text, 'legend')]], colWidths=[CW],
                 style=TableStyle([('BOX', (0, 0), (-1, -1), 0.4, RULE),
                                   ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(bg)),
                                   ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                                   ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))


def read_csv(*rel):
    p = os.path.join(BASE, *rel)
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8-sig', errors='replace') as fh:
        return list(csv.DictReader(fh))


# --------------------------------------------------------------------------- data
payload = json.load(open(os.path.join(BASE, 'data', 'master', 'consolidated_directory.json'), encoding='utf-8'))
RECS = payload['records']
ENDPOINTS = payload.get('engine_endpoints', [])
N_LINKS = len(RECS)
cat_ct = Counter(r['category'] for r in RECS)
tier_ct = Counter(r['tier'] for r in RECS)

ENGINE_AUDIT = read_csv('data', 'research', 'engine_audit.csv')
ENGINE_MATRIX = read_csv('registry', 'regional_alt_engine_pass_2026-09-05', 'ENGINE_ACCESS_MATRIX.csv')
REGIONAL_CANDIDATES = read_csv('registry', 'regional_alt_engine_pass_2026-09-05', 'candidate_ledger.csv')
REGIONAL_QUERIES = read_csv('registry', 'regional_alt_engine_pass_2026-09-05', 'query_inventory.csv')
REGIONAL_ACCESS = read_csv('registry', 'regional_alt_engine_pass_2026-09-05', 'source_access_log.csv')
MD_FEATURES = read_csv('registry', 'magazine_zine_features', 'feature_directory.csv')
MD_VISIBILITY = read_csv('registry', 'magazine_zine_features', 'visibility_matrix.csv')
MD_CANDIDATES = read_csv('registry', 'magazine_zine_features', 'candidate_ledger.csv')
MD_TIERC = read_csv('registry', 'magazine_zine_features', 'tier_c_mentions.csv')
MD_LEADS = read_csv('registry', 'magazine_zine_features', 'unresolved_leads.csv')
MD_QUERIES = read_csv('registry', 'magazine_zine_features', 'query_inventory.csv')
MD_ACCESS = read_csv('registry', 'magazine_zine_features', 'source_access_log.csv')
MD_DUPES = read_csv('registry', 'magazine_zine_features', 'duplicate_map.csv')
P3_LEDGER = read_csv('registry', 'phase3_editorial_literary', 'editorial_ledger.csv')
WP_DISCOVERIES = read_csv('registry', 'web_presence_expansion', 'discoveries.csv')
WP_BACKLINKS = read_csv('registry', 'web_presence_expansion', 'backlinks.csv')
WP_ENTITY = read_csv('registry', 'web_presence_expansion', 'entity_map.csv')
WP_HISTORICAL = read_csv('registry', 'web_presence_expansion', 'historical_records.csv')
WP_ARCHAEOLOGY = read_csv('registry', 'web_presence_expansion', 'web_archaeology.csv')
WP_LOG = read_csv('registry', 'web_presence_expansion', 'research_log.csv')
LT_LEDGER = read_csv('registry', 'spam_scraper_syndication_lowtrust_2026-09-05', 'lowtrust_ledger.csv')
LT_QUERIES = read_csv('registry', 'spam_scraper_syndication_lowtrust_2026-09-05', 'queries_run.csv')
LT_ACCESS = read_csv('registry', 'spam_scraper_syndication_lowtrust_2026-09-05', 'source_access_log.csv')
MX_VISIBILITY = read_csv('registry', 'maxdepth_pass_2026-09-05', 'engine_visibility.csv')
MX_REVERIFIED = read_csv('registry', 'maxdepth_pass_2026-09-05', 'reverified_urls.csv')
MX_LEADS = read_csv('registry', 'maxdepth_pass_2026-09-05', 'discovery_ledger.csv')
REGISTER_MAP = read_csv('data', 'master', 'register_link_map.csv')
LISTEN = read_csv('data', 'master', 'listen_links.csv')
SEED_DOMAINS = read_csv('registry', 'seed', 'seed_domain_summary.csv')

story = []

# =========================================================== COVER
stat_cells = [
    (str(N_LINKS), 'links in the master volume'),
    (str(len(ENGINE_AUDIT) + len(ENGINE_MATRIX) + len(MX_VISIBILITY)), 'engine probes logged'),
    ('11', 'research passes reported'),
    (str(len(MD_FEATURES)), 'magazine / zine features'),
    (str(len(P3_LEDGER)), 'editorial-literary ledger rows'),
    (str(len(LT_LEDGER)), 'quarantine register rows'),
    (str(len(LISTEN)), 'compilation listen links'),
    (str(len(SEED_DOMAINS)), 'seed domains indexed'),
]
row1 = [Paragraph(f'<para alignment="center"><font size="17" color="#0b6e4f"><b>{v}</b></font><br/>'
                  f'<font size="6.4" color="#5b6674">{esc(lbl)}</font></para>', ST['legend']) for v, lbl in stat_cells]
story += [Spacer(1, 34 * mm), Table([row1], colWidths=[CW / 8] * 8,
                                     style=TableStyle([('BOX', (0, 0), (-1, -1), 0.4, RULE),
                                                       ('INNERGRID', (0, 0), (-1, -1), 0.3, RULE),
                                                       ('TOPPADDING', (0, 0), (-1, -1), 4),
                                                       ('BOTTOMPADDING', (0, 0), (-1, -1), 5)])),
          Spacer(1, 7 * mm)]

WHAT = (
    '<b>WHAT THIS VOLUME IS.</b> The Master Directory prints every catalogued link, ranked and colour-coded by media '
    'type. This annex prints the <i>research record behind it</i>: which search engines and databases were probed and '
    'what each one returned, what every discovery pass found and how each finding was verified, the full editorial and '
    'literary evidence ledger, the web-presence expansion (backlinks, entity records, historical pages, web archaeology), '
    'the complete low-trust quarantine register with its safety charter, the map from the 2026 Accomplishment Register '
    'to public links, a listen link for every compilation credit, the seed-domain coverage of the original link dump, '
    'and every query and source-access log the passes produced.'
    '<br/><br/><b>HOW IT IS ORGANISED.</b> One colour-coded section per research register, ordered from method (rules, '
    'engine audits) through the discovery passes in the order they ran, to the cross-cutting registers (quarantine, '
    'link map, listen links, seed coverage) and the process appendices (queries, access logs, endpoints). Chips carry '
    'status: <font color="#188038"><b>green = worked / live</b></font>, <font color="#b06000"><b>amber = partial</b></font>, '
    '<font color="#b3261e"><b>red = blocked / broken</b></font>, <font color="#7b8794"><b>grey = unreach­able / uncheck­ed</b></font>, '
    '<font color="#546e7a"><b>slate = lead or archive-only</b></font>. Every URL is printed in full and clickable.'
    '<br/><br/><b>PROVENANCE.</b> These tables are rendered directly from the machine-readable registries under '
    '<font face="Courier">data/</font> and <font face="Courier">registry/</font> — the CSV and JSON files are the source '
    'of truth; this PDF is their organised, permanent reading edition.')
story += [Spacer(1, 2 * mm), notebox(WHAT), NextPageTemplate('body'), PageBreak()]

# =========================================================== CONTENTS
TOC = [
    ('1', 'Census rules, colour code & method', 'exact-name targets, inclusion rule, tiers, statuses, categories — the compact rulebook', 'sec:1', '#37424e'),
    ('2', 'Search-engine audit — Passes 1-8', 'every mainstream, meta and independent engine probed, what each returned, what blocked bots', 'sec:2', '#1a73e8'),
    ('3', 'Regional & alt-engine sweep — Pass 9', '62 regional, independent, archival and scholarly interfaces with access verdicts', 'sec:3', '#0f9d8f'),
    ('4', 'Maximum-Depth Research Pass — 2026-09-05', 'engine visibility per target, re-verified anchors, discovery ledger of all 20 leads, follow-up queue', 'sec:4', '#5e35b1'),
    ('5', 'Magazine & zine features registry', '19 qualified editorial features with evidence, engine visibility matrix, Tier-C mentions, unresolved leads', 'sec:5', '#c2185b'),
    ('6', 'Editorial & literary evidence ledger — Phase 3', 'every literary/editorial surface checked with exact evidence quotes and discovery route', 'sec:6', '#7b1fa2'),
    ('7', 'Web-presence blind-spot expansion — Pass 11', 'backlinks, visual surfaces, social, entity records, historical/deleted pages, web archaeology', 'sec:7', '#00796b'),
    ('8', 'Low-trust quarantine register — Pass 10', '89 spam / scraper / syndication / SEO-poisoning rows, safety charter, queries and access log', 'sec:8', '#616161'),
    ('9', 'Accomplishment Register to link map', 'the 2026 register entries mapped to their public links, with HUNT / AUTH / lead states', 'sec:9', '#e8710a'),
    ('10', 'Listen links — every compilation appearance', 'one listen link per compilation credit, confirmed / label-root / unresolved', 'sec:10', '#039be5'),
    ('11', 'Seed index & domain coverage', 'the original raw-dump seed: 260 URLs across 230 domains', 'sec:11', '#2e7d32'),
    ('12', 'Query inventories & source-access logs', 'every exact query string run per pass and every fetch logged with its outcome', 'sec:12', '#8a6d3b'),
    ('A', 'Appendix — tools, endpoints & query templates', 'all search endpoints, APIs and archive lookups used by the census, clickable', 'sec:A', '#0b5d8f'),
]
toc_rows = []
toc_extra = []
for i, (num, title, blurb, key, col) in enumerate(TOC, start=1):
    toc_rows.append([para(f'<para alignment="center"><font color="#ffffff" size="7"><b>{esc(num)}</b></font></para>', colour=colors.white),
                     para(f'<b>{esc(title)}</b>', 'cell'),
                     para(esc(blurb), 'cell', colour=SOFT),
                     para(f'<b>page {PAGEMAP.get(key, "-")}</b>', 'cell', TA_RIGHT,
                          colour=INK if PAGEMAP.get(key) else SOFT)])
    toc_extra.append(('BACKGROUND', (0, i), (0, i), colors.HexColor(col)))
story += [banner('CONTENTS', size=11, sub='twelve colour-coded registers plus the endpoint appendix — rendered from the CSV/JSON registries'),
          Spacer(1, 3 * mm),
          grid(toc_rows, [9 * mm, 74 * mm, CW - 111 * mm, 28 * mm], zebra=True, font=7.2,
               extra=toc_extra + [('VALIGN', (0, 1), (0, -1), 'MIDDLE'),
                                  ('TOPPADDING', (0, 1), (-1, -1), 3), ('BOTTOMPADDING', (0, 1), (-1, -1), 3)])]
story.append(PageBreak())


def section(num, title, colour, sub, right=None):
    story.append(Marker(f'sec:{num}', f'{num}. {title}'))
    story.append(banner(f'{num}  ·  {title}', colour=colour, size=12.5, sub=sub, right=right))
    story.append(Spacer(1, 2.4 * mm))


# =========================================================== §1 RULES & METHOD
section('1', 'CENSUS RULES, COLOUR CODE & METHOD', '#37424e',
        'the compact rulebook every pass ran under — targets, inclusion rule, evidence standard, tiers, statuses and the category colour code',
        right=f'master volume: {N_LINKS} links · A {tier_ct["A"]} · B {tier_ct["B"]} · C {tier_ct["C"]} · D {tier_ct["D"]}')

RULES_TXT = (
    '<b>THE TWO TARGETS.</b> One person / one artist project: <i>Zazie Kanwar-Torge</i> (composer, film scorer, '
    'experimental/noise musician, filmmaker, writer, multimedia artist) and the project name <i>Zazie Productions</i>. '
    'The census deliberately excludes the unrelated French singer "Zazie", the company "Zazie Films", Zazie Beetz and '
    'every other same-name entity.'
    '<br/><br/><b>EXACT-NAME INCLUSION RULE (Pass-7 standard).</b> Countable evidence must render the exact string '
    '<font face="Courier">Zazie Productions</font> — the contiguous "Productions" sequence in any spacing or case '
    '(<font face="Courier">ZazieProductions, Zazie_Productions, zazieproductions</font> and platform-URL forms such as '
    '<font face="Courier">github.com/zazieproductions</font> all count on their own) — or the exact person string '
    '<font face="Courier">Zazie Kanwar-Torge</font>. The no-space person variant (<font face="Courier">ZazieKanwar-Torge</font>) '
    'and the en-dash form do <b>not</b> count on their own; handles and slugs are recorded as leads only.'
    '<br/><br/><b>EVIDENCE STANDARD.</b> A record counts when the exact string was (i) seen on the fetched page, '
    '(ii) returned inside the platform\'s own structured API or index response, or (iii) confirmed in a search-index '
    'snapshot of the page. Search-engine snippets alone produce <i>leads</i>, never records. "Verified" is only claimed '
    'when the live page was opened and the exact name read on it. Mirrors of one original deduplicate to a single primary '
    'row; truncated display URLs were folded back to their full form, never counted twice.'
    '<br/><br/><b>TRUST TIERS.</b> <font color="#0b6e4f"><b>A</b></font> verified institutional or independent-press '
    'record · <font color="#1a73e8"><b>B</b></font> supporting platform, catalogue or trade record · '
    '<font color="#b06000"><b>C</b></font> community, compilation or self-published context · '
    '<font color="#8c1d18"><b>D</b></font> quarantined spam / scraper / syndication / poisoned (never counted as coverage).'
    '<br/><br/><b>WHAT IS NOT CLAIMED.</b> No exhaustiveness: print-only, private, paywalled, deleted, unindexed or '
    'region-blocked presence cannot be enumerated — absence means "not found on the census date", never "does not exist". '
    'Inclusion proves a public exact-name record exists; it does not independently validate every promotional, '
    'biographical, award or review claim made by that source. No addresses, phone numbers or emails are stored as data.')
story.append(notebox(RULES_TXT))
story.append(Spacer(1, 3 * mm))

legend_rows = []
for cat, colr in CAT_COLOR.items():
    legend_rows.append([para(f'<para alignment="center"><font color="#ffffff" size="6"><b>{esc(cat[0])}</b></font></para>', colour=colors.white),
                        para(f'<b>{esc(cat)}</b>', 'cell'),
                        para(f'<font face="Courier" color="#5b6674">{colr}</font>', 'cell'),
                        para(str(cat_ct.get(cat, 0)), 'cell', TA_RIGHT),
                        para({'Press & Editorial': 'reviews, features, interviews, articles, press coverage',
                              'Publications & Recognition': 'awards, anthologies, honours, institutional credit pages, published writing',
                              'Film, Festivals & Exhibitions': 'festival selections, screenings, exhibitions, film-credit records',
                              'Podcasts & Broadcasts': 'radio broadcasts, podcast episodes and show notes',
                              'Profiles & Catalogs': 'artist / composer / professional profile and directory pages',
                              'Music Discography': 'catalogue and discography database records (label, master, release)',
                              'Streaming & Music Platforms': 'streaming services, music-identification apps, audio catalogues',
                              'Lyrics & Music Databases': 'lyrics and music-metadata database entries',
                              'Music Compilations': 'compilation, netlabel and split-release credit appearances',
                              'Official Properties & Channels': 'artist-owned storefronts, channels, repositories, self-published pages',
                              'Community, Wiki & Fan Indexes': 'wikis, fan lists, forums, quizzes, charts, community pages',
                              'Search-Engine Index': 'search-engine result surfaces and redirect artefacts holding the name',
                              'Video Mirror / Backlink Sites': 'video-proxy and embed surfaces reading as ordinary listings',
                              'Spam, Scraper, Syndication, SEO-Poisoning & Low-Trust': 'QUARANTINE — hacked-site doorways, scraped clones, auto-generated metadata, paste reposts, mirror farms; documented, never cited'}[cat], 'cell', colour=SOFT)])
story.append(grid(legend_rows, [7 * mm, 66 * mm, 17 * mm, 14 * mm, CW - 104 * mm],
                  header=['', 'CATEGORY (as colour-coded in the master volume)', 'HEX', 'LINKS', 'WHAT BELONGS HERE'],
                  zebra=True, font=6.6,
                  extra=[('BACKGROUND', (0, i + 1), (0, i + 1), colors.HexColor(c))
                         for i, c in enumerate(CAT_COLOR.values())] +
                        [('TOPPADDING', (0, 0), (-1, -1), 2.4), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.4)]))
story.append(PageBreak())

# =========================================================== §2 ENGINE AUDIT PASSES 1-8
section('2', 'SEARCH-ENGINE AUDIT — PASSES 1-8', '#1a73e8',
        'how widely and where the exact names are indexed: every mainstream, meta and independent engine probed with the same two exact-phrase queries, and what each returned',
        right=f'{len(ENGINE_AUDIT)} engine rows')

story.append(notebox(
    '<b>HEADLINE FINDINGS (audit of 2026-09-04).</b> The two names are indexed on every major engine and on at least two '
    'independent crawlers (Marginalia, Brave\'s own crawler). Meta-search behaviour mattered more than engine choice: '
    '<b>Yahoo returned the richest exact-match set</b>; Bing\'s direct SERP served weak AI-generated results although its '
    'index clearly holds the name; <b>Marginalia surfaced track-level netlabel/Bandcamp pages the mainstream engines '
    'deprioritized</b> — the single biggest obscure-engine win. <b>DuckDuckGo, Startpage, Yandex, Mojeek and most public '
    'SearXNG instances block headless bots</b> (captcha / JS proof-of-work) and need a browser session or a self-hosted '
    'instance; opnxng.com and baresearch.org were the working public SearXNG workhorses. Later passes (4-8) broadened the '
    'inclusion rule to the contiguous "Productions" sequence, resolved register entry #64 (Infinite Self Pavilion / The '
    'Wrong Biennale), catalogued the DistroKid-family platform artist pages, and folded 16 + 9 + 7 new verified surfaces '
    'into the master index pass by pass.', '#eaf1fc'))
story.append(Spacer(1, 3 * mm))

rows = []
extra = []
for i, r in enumerate(ENGINE_AUDIT, start=1):
    c, fill = access_chip(r.get('Accessible', ''))
    rows.append([para(f'<b>{esc(r.get("Engine", ""))}</b>', 'cell'),
                 para(esc(r.get('AccessMethod', '')), 'cell', colour=SOFT),
                 c,
                 para(linkify(r.get('Notes', '')), 'cell')])
    extra.append(('BACKGROUND', (2, i), (2, i), fill))
    extra.append(('VALIGN', (2, i), (2, i), 'MIDDLE'))
story.append(grid(rows, [42 * mm, 46 * mm, 22 * mm, CW - 110 * mm],
                  header=['ENGINE', 'ACCESS METHOD', 'ACCESSIBLE?', 'NOTES / WHAT IT SURFACED'],
                  zebra=True, font=6.5, extra=extra))
story.append(PageBreak())

# =========================================================== §3 PASS 9 REGIONAL MATRIX
section('3', 'REGIONAL & ALT-ENGINE SWEEP — PASS 9 (2026-09-05)', '#0f9d8f',
        '62 regional, independent, archival and scholarly engines and interfaces run against both exact names — Baidu to Leit.is, national web archives, scholarly APIs',
        right=f'{len(ENGINE_MATRIX)} engines logged')

story.append(notebox(
    '<b>PASS OUTCOMES.</b> Mail.ru confirmed as a captcha-free access path into the Yandex index (surfaced the OK.ru artist '
    'page, Yandex Music artist and playlist links, an artchive.ru bio and a GitHub profile-repo). 360 Search (China) '
    'surfaced two Douyin/Qishui track pages; Seznam (Czechia) returned deep-tail pages on its own full-text index; '
    'Yahoo! JAPAN and Walla! confirmed Google-backed coverage from their interfaces. <b>+15 Internet Archive full-text '
    'records</b> entered the master, including the IA Public Domain Day Remix Contest 2026 film, a zines-collection item '
    'and the two Mystery File Dumps. Ghostery Search confirmed discontinued (closed beta 2026-06). Clean negatives were '
    'logged for OpenAlex, Europe PMC, Zenodo, Library of Congress and Arquivo.pt. Sogou, Mojeek, Trove and Rambler '
    'blocked; BIGLOBE, Excite JP, GiveWater, Stract, BoardReader, Ask, AOL and HotBot were dead or down. Blocked or '
    'snippet-only hits were classified as leads, never records.', '#e6f4f2'))
story.append(Spacer(1, 3 * mm))

rows, extra = [], []
for i, r in enumerate(ENGINE_MATRIX, start=1):
    c, fill = access_chip(r.get('AccessStatus', ''))
    rows.append([para(f'<b>{esc(r.get("Engine", ""))}</b>', 'cell'),
                 para(esc(r.get('Class', '')), 'tiny', colour=SOFT),
                 para(esc(r.get('Region_Language', '')), 'tiny', colour=SOFT),
                 para(linkify(r.get('EndpointTested', ''), '#1a3d8f'), 'tiny'),
                 c,
                 para(esc(r.get('EngineConfig_Backend', '')), 'tiny', colour=SOFT),
                 para(linkify(r.get('Notes', '')), 'tiny')])
    extra += [('BACKGROUND', (4, i), (4, i), fill), ('VALIGN', (4, i), (4, i), 'MIDDLE')]
story.append(grid(rows, [38 * mm, 24 * mm, 15 * mm, 62 * mm, 21 * mm, 30 * mm, CW - 190 * mm],
                  header=['ENGINE', 'CLASS', 'REGION', 'ENDPOINT TESTED (clickable)', 'ACCESS', 'BACKEND', 'NOTES / WHAT IT SURFACED'],
                  zebra=True, font=5.9, extra=extra))
story.append(PageBreak())

# =========================================================== §4 MAXDEPTH PASS
section('4', 'MAXIMUM-DEPTH RESEARCH PASS — 2026-09-05', '#5e35b1',
        'the deepest single-pass sweep: 54 new records entered the master directory, 11 repo URLs re-verified live, 20 leads logged — every search executed and date-bounded on 2026-09-05',
        right='54 new records · 11 re-verified · 20 leads')

story.append(notebox(
    '<b>WHAT THE PASS FOUND (all now printed in the master volume).</b> Two new Bandcamp releases where the exact name is '
    'the artist credit: the artist-run netlabel <i>The Vanishing Point Syndicate — Dissonance Index Vol. 1</i> (track 1 '
    '"Pyrogenesis" by Zazie Productions) and <i>909 Dead Batteries — Winter 2025</i> (track 7 by <b>Zazie Kanwar-Torge</b> — '
    'the only new personal-name-exact music release located). Two new compilation appearances: Camembert Electrique '
    '<i>SHIPPAI</i> ("Grief is a Hot Commodity") and the arrhythNia <i>aNr124</i> split (also a new Discogs release). '
    '14 album/track URLs on the artist\'s own Bandcamp store. A MusicBrainz Person record listing 7 V/A compilation '
    'releases; the Discogs label "Not On Label (Zazie Productions Self-released)" plus two release records; the '
    'Apple/iTunes 25-track exact-name catalogue (artistId 1623719351). <b>19 Internet Archive items</b> including '
    '<i>Instructions for Clean Living</i> — the only IA item matching the personal name exactly ("developed and produced '
    'by Zazie Kanwar-Torge, working as Zazie Productions") — and the self-uploaded <i>Phantom Requiem</i> film. Listen '
    'Notes podcast indexing rendered both exact names on one page. Negatives logged (never claimed exhaustive): no '
    'Wikidata entity, no Wikipedia article, no GitHub repo under the exact name, no npm / PyPI / HuggingFace / OpenLibrary '
    'presence, no MusicBrainz record under the personal name.', '#f1ecfa'))
story.append(Spacer(1, 2.5 * mm))

story.append(para('<b>4.1 — Engine visibility per target (this pass)</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(MX_VISIBILITY, start=1):
    c, fill = access_chip(r.get('Status', ''))
    rows.append([para(f'<b>{esc(r.get("Engine", ""))}</b>', 'cell'),
                 para(esc(r.get('TargetA', '')), 'cell'),
                 para(esc(r.get('TargetB', '')), 'cell'),
                 c])
    extra += [('BACKGROUND', (3, i), (3, i), fill), ('VALIGN', (3, i), (3, i), 'MIDDLE')]
story.append(grid(rows, [64 * mm, (CW - 64 * mm - 24 * mm) * 0.5, (CW - 64 * mm - 24 * mm) * 0.5, 24 * mm],
                  header=['ENGINE / INDEX', 'TARGET A — "Zazie Productions"', 'TARGET B — "Zazie Kanwar-Torge"', 'STATUS'],
                  zebra=True, font=6.2, extra=extra))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>4.2 — Repo anchors re-verified live on 2026-09-05</b> (already in the master volume; re-opened and exact string confirmed)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(MX_REVERIFIED, start=1):
    st = (r.get('HTTPStatus') or '').strip()
    fill = LGREEN if st == '200' else LRED
    rows.append([para(r.get('N', ''), 'cell', TA_RIGHT, colour=SOFT),
                 para(f'<a href="{esc(r.get("RepoURL", ""))}" color="#1a3d8f">{esc(r.get("RepoURL", ""))}</a>', 'url'),
                 para(esc(r.get('What', '')), 'cell', colour=SOFT),
                 para(f'<para alignment="center"><font color="#0b6e4f" size="6.4"><b>{esc(st)}</b></font></para>')])
    extra.append(('BACKGROUND', (0, i), (-1, i), fill))
story.append(grid(rows, [8 * mm, 105 * mm, CW - 133 * mm, 20 * mm],
                  header=['#', 'URL (clickable)', 'WHAT WAS CONFIRMED', 'HTTP'],
                  zebra=False, font=6.4, extra=extra))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>4.3 — Discovery ledger: all 20 leads</b> (blocked, broken, duplicate or rejected — none counted as master records)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(MX_LEADS, start=1):
    s = (r.get('Status') or '').lower()
    fill = LRED if ('broken' in s or 'blocked' in s or 'rejected' in s) else (LGREY if 'duplicate' in s or 'context' in s or 'cluster' in s or 'negative' in s else LAMBER)
    url = r.get('LeadURL', '')
    rows.append([para(f'<b>{esc(r.get("LeadID", ""))}</b>', 'cell'),
                 para(linkify(r.get('Lead', '')), 'cell'),
                 para(f'<a href="{esc(url)}" color="#1a3d8f">{esc(url)}</a>', 'url') if url.startswith('http') else para('', 'cell'),
                 para(f'<b>{esc(r.get("Status", ""))}</b>', 'cell'),
                 para(esc(r.get('WhyNotInMaster', '')), 'cell', colour=SOFT)])
    extra.append(('BACKGROUND', (0, i), (-1, i), fill))
story.append(grid(rows, [16 * mm, 78 * mm, 74 * mm, 34 * mm, CW - 202 * mm],
                  header=['LEAD ID', 'LEAD', 'URL (clickable where known)', 'STATUS', 'WHY NOT IN THE MASTER DIRECTORY'],
                  zebra=False, font=6.1, extra=extra))
story.append(PageBreak())

story.append(para('<b>4.4 — Method, identity links and follow-up queue</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
story.append(notebox(
    '<b>METHOD.</b> Baseline: 437 normalized URLs from the seed registry, the 133 Media Master link annotations and the '
    '278 URIs inside the raw link dump; a candidate counted as "already in repo" only on exact normalized-URL equality '
    '(one verified redirect equivalence applied). Discovery layers: general exact-name queries, role/work-title pivots, '
    'direct platform searches (Bandcamp, Discogs, MusicBrainz WS2, iTunes API, archive.org advancedsearch, Wikidata, '
    'Wikipedia, GitHub, npm, PyPI, HuggingFace, Open Library, Common Crawl collinfo, Wayback CDX), variant queries and '
    'old-web site: sweeps. Verification required the exact string in fetched content, a platform API response, a platform '
    'index page, or URL+title confirmed on a fetched page — snippets alone produced ledger leads only.'
    '<br/><br/><b>THE TWO PUBLIC IDENTITY STATEMENTS located (the only B-to-A links on the open web):</b> the Pebbles '
    'Underground film page — "Director, artist, producer: Zazie Kanwar-Torge (A.K.A Zazie Productions)" — and the IA item '
    '<i>Instructions for Clean Living</i> — "developed and produced by Zazie Kanwar-Torge, working as Zazie Productions". '
    'Both re-opened live on 2026-09-05. Key clusters: Phantom Requiem spans the festival page, the Visualcontainer awards '
    'announcement and the IA film item; the aNr124 split spans Bandcamp, Discogs 36415555, the IA arrhythNia '
    'label-discography and the SoundBetter credit block; the MusicBrainz artist entity lists the 7 V/A releases; the '
    'Bandcamp store root\'s discography block enumerates the 14 new release URLs.'
    '<br/><br/><b>FOLLOW-UP QUEUE.</b> (1) Reddit r/noisemusic thread — fetch from a residential session. (2) 100Subtexts '
    'blogspot Issue-31 feature — JS session. (3) The two Visualcontainer press-release PDFs — parse locally. (4) Experiments '
    'on the Witch House — enumerate the Zazie track. (5) Register pivots with no live page found: Ecstatic Feedback II, '
    'Drama Recorder Vol. 4, 23SECONDS OV TIME, Poseidon\'s Dial Tone, Camembert Electrique August comp ("Subduction Choir"), '
    'Mountains To Sea Vol. 2, Sonic Saturday 2026 (Linz), EXiS 2026, Dark Descent anthology, Milkweed Poetry Journal, '
    'Barb issue 3, The Wrong Biennale catalogue. (6) Tidal artist 33032080 (Target-B sameAs from Songstats). '
    '(7) Behance zaziediya (variant handle). (8) Marginalia / DDG / Mojeek / SearXNG re-runs from a browser session.'
    '<br/><br/><b>QC RESIDUAL RISKS (stated by the pass).</b> Bandcamp store-release rows rest on the platform search index '
    'plus the fetched 18-release discography block rather than per-page fetches; five IA items rest on full-text index '
    'matches pending per-file enumeration; the opaque general-search backend is not engine-attributable and was '
    'cross-checked against at least one directly reachable source wherever possible.', '#f1ecfa'))
story.append(PageBreak())

# =========================================================== §5 MAGAZINE & ZINE PASS
section('5', 'MAGAZINE & ZINE FEATURES REGISTRY — PASS OF 2026-09-05', '#c2185b',
        'the authoritative editorial-feature inventory: substantial public magazine, zine, journal and periodical features separated from brief mentions and non-editorial records',
        right=f'{len(MD_FEATURES)} qualified features · {len(MD_TIERC)} Tier-C mentions · {len(MD_LEADS)} unresolved leads')

story.append(notebox(
    '<b>DISCIPLINE.</b> Every Tier A/B entry contains the complete exact target phrase visibly on the destination page, '
    'PDF or a verified archive snapshot, and meets the substantial-feature threshold: a dedicated feature, review, '
    'interview, profile, contributor page or published work — not a tracklist line, tag page, roster mention or press '
    'release. Tier C rows below are verified exact-phrase pages that fall below that threshold; they remain useful for '
    'visibility but are not features. Press releases (PRFree), hosted self-publishing (telegra.ph) and podcast rows are '
    'non-editorial for this register and live in the master volume under their own categories.', '#fceef4'))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>5.1 — Qualified features (Tier A / B)</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(sorted(MD_FEATURES, key=lambda x: (x.get('Tier', ''), x.get('ID', ''))), start=1):
    tc, tchipfill, tint = tier_chip(r.get('Tier', ''))
    lc, lfill = live_chip(r.get('LiveStatus', ''))
    link = r.get('Link', '')
    arch = r.get('ArchiveLink', '')
    linkcell = para(f'<a href="{esc(link)}" color="#1a3d8f">{esc(link)}</a>', 'url') if link.startswith('http') else para(esc(link), 'cell')
    rows.append([para(f'<b>{esc(r.get("ID", ""))}</b>', 'cell'),
                 tc,
                 para(f'<b>{esc(r.get("Publication", ""))}</b><br/><font color="#5b6674" size="5.8">{esc(r.get("Format", ""))} · {esc(r.get("Date", ""))}</font>', 'cell'),
                 para(f'<b>{esc(r.get("FeatureTitle", "")[:150])}</b><br/><font color="#5b6674" size="5.8">{esc(r.get("Target", ""))}</font>', 'cell'),
                 linkcell,
                 para(f'<a href="{esc(arch)}" color="#546e7a">archive</a>', 'cell') if arch.startswith('http') else para('', 'cell'),
                 lc,
                 para(esc((r.get('EvidenceExcerpt') or '')[:300]), 'tiny', colour=SOFT)])
    extra += [('BACKGROUND', (0, i), (-1, i), tint), ('BACKGROUND', (1, i), (1, i), tchipfill),
              ('BACKGROUND', (6, i), (6, i), lfill), ('VALIGN', (1, i), (1, i), 'MIDDLE'), ('VALIGN', (6, i), (6, i), 'MIDDLE')]
story.append(grid(rows, [15 * mm, 10 * mm, 40 * mm, 58 * mm, 66 * mm, 13 * mm, 17 * mm, CW - 219 * mm],
                  header=['ID', 'TIER', 'PUBLICATION', 'FEATURE', 'LINK (clickable)', 'ARCH.', 'LIVE', 'EVIDENCE EXCERPT'],
                  zebra=False, font=6.1, extra=extra))
story.append(PageBreak())

story.append(para('<b>5.2 — Engine visibility per feature</b> (which search systems surface each canonical feature URL)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
ENGINES_COLS = ['Google_WebSearch', 'Bing', 'Yahoo', 'Brave', 'Marginalia', 'Mojeek', 'DirectSiteFetch', 'SiteRestrictedSearch', 'FiletypePDFSearch', 'ArchiveSearch']
rows, extra = [], []
for i, r in enumerate(MD_VISIBILITY, start=1):
    line = [para(f'<b>{esc(r.get("Publication", ""))}</b><br/><font color="#5b6674" size="5.4">{esc(r.get("FeatureID", ""))}</font>', 'cell'),
            para(linkify(r.get('CanonicalURL', '')), 'tiny')]
    for j, col in enumerate(ENGINES_COLS):
        v = (r.get(col) or '').strip()
        hit = bool(v) and v.lower() not in ('same', 'n/a', '-', '—')
        same = v.lower() == 'same'
        lab = 'HIT' if hit and not same else ('same' if same else '-')
        fill = LGREEN if hit else (LBLUE if same else LGREY)
        line.append(para(f'<para alignment="center"><font size="5" color="#37424e"><b>{esc(lab)}</b></font></para>'))
        extra.append(('BACKGROUND', (2 + j, i), (2 + j, i), fill))
    rows.append(line)
w = [34 * mm, 62 * mm] + [(CW - 96 * mm) / 10] * 10
story.append(grid(rows, w, header=['PUBLICATION', 'CANONICAL URL'] + [c.replace('_', ' ')[:11] for c in ENGINES_COLS],
                  zebra=True, font=5.6, extra=extra + [('VALIGN', (2, 1), (-1, -1), 'MIDDLE')]))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>5.3 — Verified Tier-C publication mentions</b> (exact phrase on page, below the substantial-feature threshold — excluded from the feature count with a stated reason)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in MD_TIERC:
    url = r.get('PageURL', '')
    rows.append([para(f'<b>{esc(r.get("StableID", ""))}</b>', 'cell'),
                 para(f'<b>{esc(r.get("Publication", ""))}</b><br/><font color="#5b6674" size="5.8">{esc(r.get("Date", ""))} · {esc(r.get("MentionType", ""))}</font>', 'cell'),
                 para(f'<a href="{esc(url)}" color="#1a3d8f">{esc(url)}</a>', 'url') if url.startswith('http') else para(esc(r.get('PageTitle', '')), 'cell'),
                 para(esc(r.get('ExactNameContext', '')), 'tiny', colour=SOFT),
                 para(esc(r.get('ReasonExcluded', '')), 'tiny', colour=SOFT)])
story.append(grid(rows, [16 * mm, 56 * mm, 84 * mm, (CW - 156 * mm) * 0.5, (CW - 156 * mm) * 0.5],
                  header=['ID', 'PUBLICATION', 'LINK (clickable)', 'EXACT-NAME CONTEXT', 'WHY NOT A FEATURE'],
                  zebra=True, font=6.1))
story.append(PageBreak())

story.append(para('<b>5.4 — Unresolved magazine / zine leads</b> (high-value exact-string leads that could not yet be verified as qualifying features)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in MD_LEADS:
    url = r.get('LeadURL', '')
    rows.append([para(f'<b>{esc(r.get("LeadID", ""))}</b>', 'cell'),
                 para(esc(r.get('TargetPhrase', '')), 'cell'),
                 para(f'<b>{esc(r.get("PublicationHost", ""))}</b>', 'cell'),
                 para(esc((r.get('PageTitleOrSnippet') or '')[:220]), 'tiny', colour=SOFT),
                 para(f'<a href="{esc(url)}" color="#1a3d8f">{esc(url)}</a>', 'url') if url.startswith('http') else para(esc(url), 'tiny'),
                 para(esc((r.get('WhyMayQualify') or '')[:220]), 'tiny', colour=SOFT)])
story.append(grid(rows, [16 * mm, 26 * mm, 52 * mm, 74 * mm, 60 * mm, CW - 228 * mm],
                  header=['LEAD', 'TARGET', 'PUBLICATION / HOST', 'PAGE TITLE OR SNIPPET', 'URL (clickable where known)', 'WHY IT MAY QUALIFY'],
                  zebra=True, font=6.0))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>5.5 — Duplicate / mirror clusters</b> (one canonical row per feature; mirrors never counted twice)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in MD_DUPES:
    rows.append([para(f'<b>{esc(r.get("ClusterID", ""))}</b>', 'cell'),
                 para(linkify(r.get('CanonicalURL', '')), 'tiny'),
                 para(linkify(r.get('DuplicateURLs', '')), 'tiny'),
                 para(esc(r.get('Type', '')), 'cell'),
                 para(esc(r.get('Status', '')), 'cell'),
                 para(esc((r.get('Notes') or '')[:200]), 'tiny', colour=SOFT)])
story.append(grid(rows, [18 * mm, 78 * mm, 92 * mm, 26 * mm, 20 * mm, CW - 234 * mm],
                  header=['CLUSTER', 'CANONICAL URL', 'DUPLICATE / MIRROR URLS', 'TYPE', 'STATUS', 'NOTES'],
                  zebra=True, font=5.9))
story.append(PageBreak())

# =========================================================== §6 PHASE 3 EDITORIAL LEDGER
section('6', 'EDITORIAL & LITERARY EVIDENCE LEDGER — PHASE 3', '#7b1fa2',
        'every literary / editorial surface checked in the phase-3 pass, with the exact evidence quote, discovery route and counting decision — sections A (new countable finds), A2 (self-published poetry pages), B (partial / handle-only, not counted), C (register-named publications still unresolved), D (incidental non-editorial profiles)',
        right=f'{len(P3_LEDGER)} ledger rows')

SEC_CHIP = {'A': ('A · COUNTED', GREEN), 'A2': ('A2 · SELF-PUB', colors.HexColor('#5f8b3a')),
            'B': ('B · PARTIAL', AMBER), 'C': ('C · LEAD', SLATE), 'D': ('D · INCIDENTAL', GREY)}
rows, extra = [], []
sec_order = {'A': 0, 'A2': 1, 'B': 2, 'C': 3, 'D': 4}
for i, r in enumerate(sorted(P3_LEDGER, key=lambda x: (sec_order.get(x.get('Section', ''), 9), x.get('PageURL', ''))), start=1):
    sec = r.get('Section', '')
    lab, fill = SEC_CHIP.get(sec, (sec, GREY))
    url = r.get('PageURL', '')
    if sec == 'C':
        rows.append([para(f'<para alignment="center"><font color="#ffffff" size="5.6"><b>{esc(lab)}</b></font></para>', colour=colors.white),
                     para(f'<b>{esc(r.get("Name", ""))}</b>', 'cell'),
                     para(linkify(r.get('Evidence', '')), 'cell'),
                     para(linkify(r.get('NextAction', '')), 'cell', colour=SOFT),
                     para('', 'cell'), para('', 'cell')])
    else:
        pr = priority_chip(r.get('Priority', ''))
        rows.append([para(f'<para alignment="center"><font color="#ffffff" size="5.6"><b>{esc(lab)}</b></font></para>', colour=colors.white),
                     para(linkify(url), 'url') if url.startswith('http') else para(f'<b>{esc(r.get("Name", ""))}</b>', 'cell'),
                     para(esc(r.get('Evidence', '')), 'tiny'),
                     para(esc(r.get('FoundOn', '')), 'tiny', colour=SOFT),
                     pr[0],
                     status_emoji_chip(r.get('Status', ''))])
    extra += [('BACKGROUND', (0, i), (0, i), fill), ('VALIGN', (0, i), (0, i), 'MIDDLE')]
    if sec != 'C':
        extra += [('BACKGROUND', (4, i), (4, i), pr[1]), ('VALIGN', (4, i), (5, i), 'MIDDLE')]
story.append(grid(rows, [20 * mm, 92 * mm, CW - 20 * mm - 92 * mm - 46 * mm - 16 * mm - 18 * mm, 46 * mm, 16 * mm, 18 * mm],
                  header=['LEDGER', 'URL (clickable) / TARGET', 'EXACT EVIDENCE ON PAGE', 'FOUND ON', 'PRI', 'STATUS'],
                  zebra=True, font=6.0, extra=extra))
story.append(PageBreak())

# =========================================================== §7 WEB PRESENCE EXPANSION
section('7', 'WEB-PRESENCE BLIND-SPOT EXPANSION — PASS 11 (2026-09-05)', '#00796b',
        'six blind-spot areas swept beyond keyword search: inbound backlinks, visual surfaces, social, machine-readable entity records, historical / deleted pages, and web archaeology of the spam clusters',
        right=f'{len(WP_DISCOVERIES)} discoveries · {len(WP_BACKLINKS)} backlinks · {len(WP_ENTITY)} entity records · {len(WP_HISTORICAL)} historical · {len(WP_ARCHAEOLOGY)} archaeology clusters')

story.append(notebox(
    '<b>HIGHLIGHTS.</b> The <b>VisualcontainerTV Winter-2024 press-release PDF</b> (Tier A) names both exact forms and '
    'carries the Jury Special Mention plus the February 2025 broadcast. The <b>deleted PVTV Fringe Flicks April-2025 page '
    'was recovered from the Wayback Machine</b> (Deaf Orphans of Streamcast, Liverpool, 4 Apr 2025 — live page now 404, '
    '6 captures). Eight IMDb title IDs were mapped and the TMDB / IMDb identity split documented. Five Discogs releases '
    'missing from the master were added. A legitimate five-post <b>clongclongmoo.org backlink cluster</b> was verified as '
    'real independent coverage. The BMC / Levinson spam cluster was traced to one unchanged Black Mountain College page '
    '(Dec 2021) and characterised as a doorway network via Common Crawl — zero independence, Tier D retained.', '#e7f2f0'))
story.append(Spacer(1, 3 * mm))

AREA_COLOR = {'1-backlinks': BLUE, '2-visual': colors.HexColor('#d81b60'), '3-social': GREEN,
              '4-entity': colors.HexColor('#7b1fa2'), '5-historical': AMBER, '6-archaeology': SLATE}
story.append(para('<b>7.1 — Discoveries by area</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(WP_DISCOVERIES, start=1):
    area = r.get('area', '')
    acol = AREA_COLOR.get(area.split(' ')[0], GREY)
    tc, tchipfill, tint = tier_chip(r.get('trust_tier', ''))
    lc, lfill = live_chip(r.get('status', ''))
    rows.append([para(f'<b>{esc(r.get("id", ""))}</b>', 'cell'),
                 para(f'<para alignment="center"><font color="#ffffff" size="5.4"><b>{esc(area[:14])}</b></font></para>', colour=colors.white),
                 para(linkify(r.get('url', '')), 'tiny'),
                 tc,
                 para(f'<b>{esc((r.get("summary") or "")[:190])}</b><br/><font color="#5b6674" size="5.6">{esc((r.get("best_use") or "")[:120])}</font>', 'cell'),
                 lc])
    extra += [('BACKGROUND', (1, i), (1, i), acol), ('BACKGROUND', (0, i), (0, i), tint),
              ('BACKGROUND', (3, i), (3, i), tchipfill),
              ('BACKGROUND', (5, i), (5, i), lfill), ('VALIGN', (1, i), (1, i), 'MIDDLE'),
              ('VALIGN', (3, i), (3, i), 'MIDDLE'), ('VALIGN', (5, i), (5, i), 'MIDDLE')]
story.append(grid(rows, [14 * mm, 20 * mm, 78 * mm, 9 * mm, CW - 143 * mm, 22 * mm],
                  header=['ID', 'AREA', 'URL (clickable)', 'TIER', 'SUMMARY / BEST USE', 'STATUS'],
                  zebra=False, font=6.0, extra=extra))
story.append(PageBreak())

story.append(para('<b>7.2 — Inbound backlink register</b> (who links to the work, with anchor text, independence and authority verdicts)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(WP_BACKLINKS, start=1):
    lc, lfill = live_chip(r.get('live_status', ''))
    rows.append([para(f'<b>{esc(r.get("id", ""))}</b>', 'cell'),
                 para(linkify(r.get('source_url', '')), 'tiny'),
                 para(linkify(r.get('destination_url', '')), 'tiny'),
                 para(esc(r.get('anchor_text', '')), 'tiny'),
                 para(f'<b>{esc(r.get("independence", ""))}</b><br/><font color="#5b6674" size="5.6">{esc(r.get("link_type", ""))} · authority {esc(r.get("authority", ""))}</font>', 'cell'),
                 para(esc((r.get('context') or '')[:160]), 'tiny', colour=SOFT),
                 lc])
    extra += [('BACKGROUND', (6, i), (6, i), lfill), ('VALIGN', (6, i), (6, i), 'MIDDLE')]
story.append(grid(rows, [12 * mm, 74 * mm, 74 * mm, 34 * mm, 40 * mm, CW - 258 * mm, 24 * mm],
                  header=['ID', 'SOURCE URL (the page that links)', 'DESTINATION URL', 'ANCHOR TEXT', 'INDEPENDENCE / TYPE', 'CONTEXT', 'LIVE'],
                  zebra=True, font=5.8, extra=extra))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>7.3 — Machine-readable entity map</b> (identifiers the platforms hold for the two targets, and the conflicts between them)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in WP_ENTITY:
    rows.append([para(f'<b>{esc(r.get("system", ""))}</b>', 'cell'),
                 para(esc(r.get('entity_name', '')), 'cell'),
                 para(f'<font face="Courier" size="5.8">{esc(r.get("identifier", ""))}</font>', 'cell'),
                 para(linkify(r.get('url', '')), 'tiny'),
                 para(esc(r.get('record_type', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('conflict_or_duplicate') or '')[:150]), 'tiny', colour=SOFT),
                 para(esc((r.get('notes') or '')[:150]), 'tiny', colour=SOFT)])
story.append(grid(rows, [30 * mm, 42 * mm, 34 * mm, 76 * mm, 24 * mm, (CW - 206 * mm) * 0.5, (CW - 206 * mm) * 0.5],
                  header=['SYSTEM', 'ENTITY NAME', 'IDENTIFIER', 'URL (clickable)', 'RECORD TYPE', 'CONFLICT / DUPLICATE', 'NOTES'],
                  zebra=True, font=5.9))
story.append(PageBreak())

story.append(para('<b>7.4 — Historical & deleted-page register</b> (what the archives hold, including pages now dead on the live web)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
for i, r in enumerate(WP_HISTORICAL, start=1):
    lc, lfill = live_chip(r.get('status_now', ''))
    rows.append([para(f'<b>{esc(r.get("id", ""))}</b>', 'cell'),
                 para(esc(r.get('year', '')), 'cell', colour=SOFT),
                 para(linkify(r.get('url_or_asset', '')), 'tiny'),
                 para(f'<b>{esc((r.get("event") or "")[:120])}</b><br/><font color="#5b6674" size="5.6">{esc(r.get("source", ""))}</font>', 'cell'),
                 para(esc((r.get('notes') or '')[:170]), 'tiny', colour=SOFT),
                 lc])
    extra += [('BACKGROUND', (5, i), (5, i), lfill), ('VALIGN', (5, i), (5, i), 'MIDDLE')]
story.append(grid(rows, [13 * mm, 12 * mm, 88 * mm, 74 * mm, CW - 213 * mm, 26 * mm],
                  header=['ID', 'YEAR', 'URL / ASSET (clickable)', 'EVENT · SOURCE', 'NOTES', 'STATUS NOW'],
                  zebra=True, font=5.9, extra=extra))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>7.5 — Web archaeology: anatomy of the spam clusters</b> (how the doorway networks were traced and why they carry zero independence)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in WP_ARCHAEOLOGY:
    rows.append([para(f'<b>{esc(r.get("cluster_id", ""))}</b>', 'cell'),
                 para(linkify(r.get('member_urls_or_hosts', '')), 'tiny'),
                 para(esc(r.get('member_count', '')), 'cell', TA_RIGHT),
                 para(f'<b>{esc(r.get("copy_source", ""))}</b><br/><font color="#5b6674" size="5.6">{esc(r.get("injection_pattern", ""))} · {esc(r.get("domain_purpose", ""))}</font>', 'cell'),
                 para(f'<b>{esc(r.get("independence_verdict", ""))}</b><br/><font color="#5b6674" size="5.6">{esc(r.get("live_status", ""))} · {esc(r.get("evidence_level", ""))}</font>', 'cell'),
                 para(esc((r.get('notes') or '')[:260]), 'tiny', colour=SOFT)])
story.append(grid(rows, [22 * mm, 84 * mm, 12 * mm, 62 * mm, 58 * mm, CW - 238 * mm],
                  header=['CLUSTER', 'MEMBER URLS / HOSTS (clickable)', 'N', 'COPY SOURCE · INJECTION PATTERN', 'INDEPENDENCE VERDICT', 'NOTES'],
                  zebra=True, font=5.8))
story.append(PageBreak())

# =========================================================== §8 LOW-TRUST QUARANTINE
section('8', 'LOW-TRUST QUARANTINE REGISTER — PASS 10 (2026-09-05)', '#616161',
        'every spam / scraper / syndication / SEO-poisoning / text-injection occurrence of the exact strings — an evidence-preservation bucket that is never counted as coverage, credit, profile, release or biography',
        right=f'{len(LT_LEDGER)} quarantined rows · {len(set(r.get("Host", "") for r in LT_LEDGER))} hosts')

story.append(notebox(
    '<b>CHARTER.</b> This register documents contamination, it does not endorse it. Rows are hacked-site doorways '
    '(the "Black Mountain College / Ira and Ruth Levinson Museum" injection family), YouTube-mirror and tool-proxy farms '
    'built around one video id, auto-generated metadata pages, RSS / PR republications, paste reposts and fabricated '
    'attributions (invented personas and non-existent journals). <b>Safety protocol:</b> quarantined compromised hosts '
    'were documented from search-index snapshots and Common Crawl only and <b>never visited directly</b> — 15 rows carry '
    'the DO-NOT-OPEN status for exactly that reason. <b>Reclassification:</b> the former "SEO Spam / Link Farm" category '
    'and all 38 Tier-D video-mirror rows were folded into this register, together with 16 misfiled rows pulled out of the '
    'community / profile / streaming / press categories (including two A-tier PR-republication demotions). Nothing in '
    'Tier D ever counts toward totals; the master volume prints these rows last, in the quarantine section, so a reader '
    'can see exactly what a search engine may surface — and what needs correcting or reporting.', '#eeeeee'))
story.append(Spacer(1, 3 * mm))

rows, extra = [], []
for i, r in enumerate(sorted(LT_LEDGER, key=lambda x: (x.get('Cluster', ''), x.get('EntryID', ''))), start=1):
    sub = (r.get('Subtype') or '').strip()
    scol = SUBTYPE_COLOR.get(sub, colors.HexColor('#616161'))
    lc, lfill = live_chip(r.get('LiveStatus_2026-09-05', ''))
    rows.append([para(f'<b>{esc(r.get("EntryID", ""))}</b>', 'tiny'),
                 para(f'<b>{esc(r.get("Cluster", ""))}</b>', 'tiny'),
                 para(f'<para alignment="center"><font color="#ffffff" size="5"><b>{esc(sub[:16])}</b></font></para>', colour=colors.white),
                 para(linkify(r.get('URL', ''), '#7a1f1a'), 'tiny'),
                 para(esc(r.get('Target', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('Origin') or '')[:60]), 'tiny', colour=SOFT),
                 lc,
                 para(esc((r.get('Notes') or '')[:200]), 'tiny', colour=SOFT)])
    extra += [('BACKGROUND', (2, i), (2, i), scol), ('BACKGROUND', (6, i), (6, i), lfill),
              ('VALIGN', (2, i), (2, i), 'MIDDLE'), ('VALIGN', (6, i), (6, i), 'MIDDLE')]
story.append(grid(rows, [13 * mm, 24 * mm, 26 * mm, 88 * mm, 20 * mm, 26 * mm, 21 * mm, CW - 218 * mm],
                  header=['ENTRY', 'CLUSTER', 'SUBTYPE', 'URL (clickable — do not treat as coverage)', 'TARGET', 'ORIGIN', 'LIVE STATUS', 'NOTES'],
                  zebra=True, font=5.7, extra=extra))
story.append(PageBreak())

# =========================================================== §9 REGISTER LINK MAP
section('9', 'ACCOMPLISHMENT REGISTER TO LINK MAP', '#e8710a',
        'the 2026 Accomplishment Register (203 records, 10 sections, originally zero URLs) mapped to public links — resolved rows carry a clickable link; HUNT rows still miss a public exact-name page; AUTH rows sit behind login or paywall; leads render only a variant of the name',
        right=f'{len(REGISTER_MAP)} mapped rows')

rows, extra = [], []
for i, r in enumerate(REGISTER_MAP, start=1):
    lc, lfill = live_chip(r.get('Status', ''))
    links = [u for u in (r.get('LinkList') or '').split(';') if u.strip()]
    linkcell = para('<br/>'.join(f'<a href="{esc(u.strip())}" color="#1a3d8f">{esc(u.strip())}</a>' for u in links), 'url') if links else para(esc(r.get('LinkDisplay', '')), 'tiny')
    rows.append([para(esc(r.get('Section', '').replace('Section ', 'S')), 'tiny', colour=SOFT),
                 para(f'<b>{esc(r.get("EntryNo", ""))}</b>', 'cell'),
                 para(f'<b>{esc(r.get("RegisterEntry", ""))}</b>', 'cell'),
                 linkcell,
                 lc,
                 para(esc((r.get('Notes') or '')[:140]), 'tiny', colour=SOFT)])
    extra += [('BACKGROUND', (4, i), (4, i), lfill), ('VALIGN', (4, i), (4, i), 'MIDDLE')]
story.append(grid(rows, [12 * mm, 10 * mm, 74 * mm, 96 * mm, 24 * mm, CW - 216 * mm],
                  header=['SEC', '#', 'REGISTER ENTRY', 'PUBLIC LINK(S) — clickable', 'STATE', 'NOTES'],
                  zebra=True, font=6.0, extra=extra))
story.append(Spacer(1, 2.5 * mm))
story.append(notebox(
    '<b>STILL-HUNTED PLATFORMS (register claims with no public exact-name page located as of 2026-09-05):</b> Pandora, '
    'Audiomack, Facebook / TikTok surfaces, Claro Musica, Saavn / JioSaavn, Snapchat, NetEase, Tencent / QQ / Kugou / '
    'Kuwo / WeSing, Pretzel, TouchTunes, JOOX, Kuack, MediaNet, Dubset, Roblox and Soundtrack by Twitch. These remain '
    'open reconciliation rows against the known-ground-truth register, not counted records.', '#fdf4e5'))
story.append(PageBreak())

# =========================================================== §10 LISTEN LINKS
section('10', 'LISTEN LINKS — EVERY COMPILATION APPEARANCE', '#039be5',
        'one listen link per compilation the artist is credited on (Discogs artist 11354435; the 60 compilation rows of the Media Master), found through public SearXNG instances (opnxng.com, baresearch.org, search.inetol.net) and direct label pages',
        right=f'{len(LISTEN)} rows · {sum(1 for r in LISTEN if (r.get("listen_status") or "").startswith("confirmed"))} confirmed direct')

rows, extra = [], []
for i, r in enumerate(LISTEN, start=1):
    st = (r.get('listen_status') or '').strip()
    if st.startswith('confirmed'):
        fill, lab = LGREEN, 'CONFIRMED'
    elif st.startswith('label'):
        fill, lab = LBLUE, 'LABEL ROOT'
    else:
        fill, lab = LAMBER, 'UNRESOLVED'
    listen = (r.get('listen_url') or '').strip()
    discogs = (r.get('discogs') or '').strip()
    rows.append([para(esc(r.get('#', '')), 'cell', TA_RIGHT, colour=SOFT),
                 para(f'<b>{esc(r.get("compilation", ""))}</b>', 'cell'),
                 para(esc(r.get('track', '')), 'cell'),
                 para(esc(r.get('label', '')), 'cell', colour=SOFT),
                 para(f'<a href="{esc(discogs)}" color="#1a3d8f">discogs</a>', 'cell') if discogs.startswith('http') else para('', 'cell'),
                 para(f'<a href="{esc(listen)}" color="#1a3d8f">{esc(listen)}</a>', 'url') if listen.startswith('http') else para(f'<i>{esc(listen) if listen else "—"}</i>', 'tiny', colour=SOFT),
                 para(f'<para alignment="center"><font size="5.4" color="#37424e"><b>{lab}</b></font></para>'),
                 para(esc(r.get('found_via', '')), 'tiny', colour=SOFT)])
    extra += [('BACKGROUND', (6, i), (6, i), fill), ('VALIGN', (6, i), (6, i), 'MIDDLE')]
story.append(grid(rows, [7 * mm, 62 * mm, 44 * mm, 32 * mm, 14 * mm, 76 * mm, 20 * mm, CW - 255 * mm],
                  header=['#', 'COMPILATION', 'TRACK', 'LABEL', 'DISCOGS', 'LISTEN LINK (clickable)', 'STATE', 'FOUND VIA'],
                  zebra=True, font=5.9, extra=extra))
story.append(PageBreak())

# =========================================================== §11 SEED DOMAINS
section('11', 'SEED INDEX & DOMAIN COVERAGE', '#2e7d32',
        'the starting set of the census: 260 unique URLs auto-extracted from the raw link dump, clustered across 230 domains — every one of them consolidated into the master volume',
        right=f'{len(SEED_DOMAINS)} domains')

sd = sorted(SEED_DOMAINS, key=lambda r: (-int(r.get('unique_url_count') or 0), r.get('domain', '')))
third = (len(sd) + 2) // 3
cols = [sd[:third], sd[third:2 * third], sd[2 * third:]]
rows = []
for i in range(max(len(c) for c in cols)):
    line = []
    for c in cols:
        if i < len(c):
            n = int(c[i].get('unique_url_count') or 0)
            line += [para(esc(c[i].get('domain', '')), 'tiny'),
                     para(f'<para alignment="right"><b>{n}</b></para>', 'tiny', colour=SOFT)]
        else:
            line += [para('', 'tiny'), para('', 'tiny')]
    rows.append(line)
wcol = (CW - 6 * mm) / 3
story.append(grid(rows, [wcol - 12 * mm, 12 * mm] * 3,
                  header=['DOMAIN', 'URLS', 'DOMAIN', 'URLS', 'DOMAIN', 'URLS'],
                  zebra=True, font=5.7))
story.append(PageBreak())

# =========================================================== §12 QUERY INVENTORIES & ACCESS LOGS
section('12', 'QUERY INVENTORIES & SOURCE-ACCESS LOGS', '#8a6d3b',
        'the process record: every exact query string each pass ran, and every source fetch logged with its outcome — so any row of this census can be re-run and re-checked',
        right=f'{len(MD_QUERIES) + len(REGIONAL_QUERIES) + len(LT_QUERIES)} queries · {len(MD_ACCESS) + len(REGIONAL_ACCESS) + len(LT_ACCESS) + len(WP_LOG)} fetch/log rows')

story.append(para('<b>12.1 — Magazine / zine pass query inventory</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in MD_QUERIES:
    rows.append([para(f'<b>{esc(r.get("QueryID", ""))}</b>', 'tiny'),
                 para(f'<font face="Courier" size="5.6">{esc(r.get("ExactQuery", ""))}</font>', 'tiny'),
                 para(esc(r.get('Engine_Family', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('Outcome') or '')[:70]), 'tiny', colour=SOFT)])
half = (len(rows) + 1) // 2
pairs = [[rows[i][0], rows[i][1], rows[i][2], rows[i][3],
          *(rows[i + half] if i + half < len(rows) else [para('', 'tiny')] * 4)] for i in range(half)]
cw = (CW - 6 * mm) / 2
story.append(grid(pairs, [13 * mm, cw - 13 * mm - 30 * mm - 34 * mm, 30 * mm, 34 * mm] * 2,
                  header=['QID', 'EXACT QUERY', 'ENGINE FAMILY', 'OUTCOME', 'QID', 'EXACT QUERY', 'ENGINE FAMILY', 'OUTCOME'],
                  zebra=True, font=5.5))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>12.2 — Regional / alt-engine pass query inventory</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in REGIONAL_QUERIES:
    q = r.get('ExactQuery') or r.get('ExactQuery_Or_Navigation') or ''
    rows.append([para(f'<b>{esc(r.get("QueryID", ""))}</b>', 'tiny'),
                 para(f'<font face="Courier" size="5.6">{esc(q)}</font>', 'tiny'),
                 para(esc(r.get('Engine_Family', '') or r.get('Engine', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('Outcome') or r.get('Notes') or '')[:80]), 'tiny', colour=SOFT)])
half = (len(rows) + 1) // 2
pairs = [[rows[i][0], rows[i][1], rows[i][2], rows[i][3],
          *(rows[i + half] if i + half < len(rows) else [para('', 'tiny')] * 4)] for i in range(half)]
story.append(grid(pairs, [13 * mm, cw - 13 * mm - 30 * mm - 34 * mm, 30 * mm, 34 * mm] * 2,
                  header=['QID', 'EXACT QUERY', 'ENGINE', 'OUTCOME', 'QID', 'EXACT QUERY', 'ENGINE', 'OUTCOME'],
                  zebra=True, font=5.5))
story.append(PageBreak())

story.append(para('<b>12.3 — Quarantine-pass queries</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in LT_QUERIES:
    rows.append([para(f'<b>{esc(r.get("QueryID", ""))}</b>', 'tiny'),
                 para(f'<font face="Courier" size="5.6">{esc(r.get("ExactQuery", ""))}</font>', 'tiny'),
                 para(esc(r.get('Engine', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('HitsOfInterest') or '')[:60]), 'tiny', colour=SOFT),
                 para(esc((r.get('Disposition') or '')[:90]), 'tiny', colour=SOFT)])
story.append(grid(rows, [13 * mm, 110 * mm, 40 * mm, 44 * mm, CW - 207 * mm],
                  header=['QID', 'EXACT QUERY', 'ENGINE', 'HITS OF INTEREST', 'DISPOSITION'],
                  zebra=True, font=5.7))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>12.4 — Source-access logs</b> (every direct fetch across the magazine, regional, quarantine and web-presence passes)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows, extra = [], []
LOGS = ([('magazine', r) for r in MD_ACCESS] + [('regional', r) for r in REGIONAL_ACCESS] +
        [('quarantine', r) for r in LT_ACCESS])
for i, (pas, r) in enumerate(LOGS, start=1):
    outcome = r.get('HTTPStatus') or r.get('Outcome') or ''
    ol = str(outcome).lower()
    fill = LGREEN if ol.startswith('200') or 'worked' in ol or 'ok' == ol.strip() else (LRED if ol.startswith(('4', '5')) or 'block' in ol or 'fail' in ol else LGREY)
    rows.append([para(esc(pas), 'tiny', colour=SOFT),
                 para(esc((r.get('TimestampUTC') or '')[:19]), 'tiny', colour=SOFT),
                 para(linkify(r.get('URL', '')), 'tiny'),
                 para(esc((r.get('QueryOrNavigation') or r.get('Method') or '')[:80]), 'tiny', colour=SOFT),
                 para(f'<b>{esc(str(outcome)[:26])}</b>', 'tiny'),
                 para(esc((r.get('ErrorNotes') or '')[:90]), 'tiny', colour=SOFT)])
    extra.append(('BACKGROUND', (4, i), (4, i), fill))
story.append(grid(rows, [17 * mm, 24 * mm, 92 * mm, 62 * mm, 24 * mm, CW - 219 * mm],
                  header=['PASS', 'TIMESTAMP (UTC)', 'URL FETCHED (clickable)', 'QUERY / NAVIGATION', 'RESULT', 'ERROR NOTES'],
                  zebra=True, font=5.5, extra=extra))
story.append(PageBreak())

story.append(para('<b>12.5 — Web-presence expansion research log</b>', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for r in WP_LOG:
    rows.append([para(esc(r.get('date', '')), 'tiny', colour=SOFT),
                 para(f'<b>{esc(r.get("area", ""))}</b>', 'tiny'),
                 para(linkify(r.get('system_or_query', '')), 'tiny'),
                 para(esc(r.get('target_phrase', '')), 'tiny', colour=SOFT),
                 para(esc((r.get('result') or '')[:90]), 'tiny'),
                 para(esc((r.get('outcome') or '')[:60]), 'tiny', colour=SOFT),
                 para(esc((r.get('notes') or '')[:120]), 'tiny', colour=SOFT)])
story.append(grid(rows, [16 * mm, 20 * mm, 78 * mm, 24 * mm, 62 * mm, 36 * mm, CW - 236 * mm],
                  header=['DATE', 'AREA', 'SYSTEM / QUERY (clickable)', 'TARGET', 'RESULT', 'OUTCOME', 'NOTES'],
                  zebra=True, font=5.5))
story.append(PageBreak())

# =========================================================== APPENDIX — ENDPOINTS & TOOLS
section('A', 'APPENDIX — TOOLS, ENDPOINTS & QUERY TEMPLATES', '#0b5d8f',
        'every search endpoint, API probe, archive lookup and research tool the census used — method artefacts, not media records; reproduced so the census can be re-run exactly',
        right=f'{len(ENDPOINTS)} logged endpoints')

TOOLS = [
    ('https://maxintel.org', 'OSINT research tool referenced by the census operator (retired note file "resource1")'),
    ('https://cachedview.nl/', 'cache-viewer front-end for archived / cached copies of pages'),
    ('https://chatgpt.com/', 'AI-search layer probed for name surfacing (not a citable index)'),
    ('https://r.jina.ai/https://URL', 'reader-proxy template used to render JS-gated pages as text'),
    ('https://web.archive.org/cdx/search/cdx?url=DOMAIN&output=json&fl=timestamp', 'Wayback CDX API template — capture transience checks per domain'),
    ('https://web.archive.org/web/2026/https://URL', 'Wayback calendar template — deleted-page recovery (used for the PVTV Fringe Flicks page)'),
    ('http://index.commoncrawl.org/CC-MAIN-2026-*?url=DOMAIN', 'Common Crawl index template — doorway-network characterisation (latest crawl CC-MAIN-2026-34)'),
    ('https://archive.org/search?query=%22Zazie+Productions%22', 'Internet Archive full-text search — the Pass-9 main win (+15 IA records)'),
    ('https://itunes.apple.com/lookup?id=1623719351', 'Apple iTunes Search API — 25-track exact-name catalogue (Maximum-Depth pass ZP26-034)'),
    ('https://musicbrainz.org/ws/2/release?artist=b610b4cb-87da-44d7-a262-2bd65fb8098c&fmt=json', 'MusicBrainz WS2 — the 7 V/A compilation releases listed on the Person record'),
    ('https://search.brave.com/search?q=%22Zazie+Productions%22', 'Brave Search query template (directly scrapable)'),
    ('https://search.yahoo.com/search?p=%22Zazie+Productions%22', 'Yahoo query template — richest exact-match set of the audit'),
    ('https://html.duckduckgo.com/html/?q=%22Zazie+Productions%22', 'DuckDuckGo HTML endpoint template (bot-challenged; browser needed)'),
    ('https://opnxng.com/search?q=%22Zazie+Productions%22', 'working public SearXNG instance used for the listen-link hunt'),
    ('https://baresearch.org/search?q=%22Zazie+Productions%22', 'fallback public SearXNG instance'),
    ('https://search.inetol.net/search?q=%22Zazie+Productions%22', 'reachable but low-coverage SearXNG instance'),
    ('https://priv.au/search?q=%22Zazie+Productions%22', 'SearXNG instance probed by the Maximum-Depth pass (JS-empty)'),
    ('https://searx.be/tiekoetter', 'public SearXNG instance (tiekoetter) probed in Pass 9 — captcha-blocked headless; browser session only'),
]
rows = []
for u, why in TOOLS:
    rows.append([para(f'<a href="{esc(u)}" color="#1a3d8f">{esc(u)}</a>', 'url'),
                 para(esc(why), 'cell', colour=SOFT)])
story.append(grid(rows, [120 * mm, CW - 120 * mm], header=['TOOL / TEMPLATE URL (clickable)', 'ROLE IN THE CENSUS'],
                  zebra=True, font=6.2, header_bg=colors.HexColor('#0b5d8f')))
story.append(Spacer(1, 3 * mm))

story.append(para('<b>A.2 — Logged search endpoints, index probes & archive lookups</b> (harvested from the pass registries)', 'legend'))
story.append(Spacer(1, 1.2 * mm))
rows = []
for e in sorted(ENDPOINTS, key=lambda x: x['host']):
    rows.append([para(f'<b>{esc(e["host"])}</b>', 'tiny'),
                 para(f'<a href="{esc(e["url"])}" color="#1a3d8f">{esc(e["url"])}</a>', 'url'),
                 para(esc(', '.join(s.split("/")[-1] for s in e.get('sources', []))[:110]), 'tiny', colour=SOFT)])
half = (len(rows) + 1) // 2
cwe = (CW - 4 * mm) / 2
pairs = []
for i in range(half):
    left = rows[i]
    right = rows[i + half] if i + half < len(rows) else [para('', 'tiny')] * 3
    pairs.append([left[0], left[1], right[0], right[1]])
story.append(grid(pairs, [24 * mm, cwe - 24 * mm, 24 * mm, cwe - 24 * mm],
                  header=['HOST', 'ENDPOINT (clickable)', 'HOST', 'ENDPOINT (clickable)'],
                  zebra=True, font=5.5, header_bg=colors.HexColor('#0b5d8f')))
story.append(Spacer(1, 4 * mm))

END_NOTE = (f'<font color="#ffffff"><b>END OF ANNEX.</b> {N_LINKS} catalogued links live in the companion master volume · '
            f'{len(ENGINE_MATRIX) + len(ENGINE_AUDIT) + len(MX_VISIBILITY)} engine probes logged across passes 1-9 · '
            f'{len(LT_LEDGER)} quarantine rows documented · compiled from the registry CSV/JSON files on '
            f'{date.today():%d %B %Y}. Rebuild with <font face="Courier">python3 scripts/build_research_annex_pdf.py</font></font>')
story.append(Table([[para(END_NOTE, 'legend', colour=colors.white)]], colWidths=[CW],
                   style=TableStyle([('BACKGROUND', (0, 0), (-1, -1), INK), ('LEFTPADDING', (0, 0), (-1, -1), 6),
                                     ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)])))

# --------------------------------------------------------------------------- build
doc = AnnexDoc(OUT, pagesize=PAGE, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
               title='Zazie Productions / Zazie Kanwar-Torge — Research Annex: Engines, Passes, Evidence & Quarantine',
               author='Zazie Productions backlink census',
               subject='Research record of the exact-name public-web census')


def build():
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
    try:
        import pymupdf
    except Exception:
        return
    d = pymupdf.open(OUT)
    toc = [[1, title[:90], PAGEMAP[key]] for key, title in OUTLINE if key in PAGEMAP]
    if toc:
        d.set_toc(toc)
        d.set_metadata({'title': 'Zazie Productions / Zazie Kanwar-Torge — Research Annex: Engines, Passes, Evidence & Quarantine',
                        'author': 'Zazie Productions backlink census',
                        'subject': f'Research record of the exact-name census — {N_LINKS} catalogued links in the companion master volume',
                        'keywords': 'engine audit, discovery passes, evidence ledger, quarantine register, listen links, backlinks'})
        tmp = OUT + '.tmp'
        d.save(tmp, garbage=3, deflate=True)
        d.close()
        os.replace(tmp, OUT)
    else:
        d.close()


def page_count():
    import pymupdf
    return pymupdf.open(OUT).page_count


build()

if not HAVE_MAP and PAGEMAP:
    with open(PAGEMAP_CACHE, 'w', encoding='utf-8') as fh:
        json.dump(PAGEMAP, fh, indent=1)
    print('pass 1 complete: page map recorded, re-running for the contents page numbers')
    os.execv(sys.executable, [sys.executable, os.path.abspath(__file__)])

print('wrote', OUT, f'{os.path.getsize(OUT) / 1024:.0f} KB', '·', page_count(), 'pages ·',
      len(TOC), 'sections')
