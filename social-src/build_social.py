"""Build the Social page examples (Oct 2026).

  1. python3 social-src/extract.py        (verbatim beats from the website and resources repos → beats.json)
  2. python3 -m http.server 8791           (in the repo root)
  3. python3 social-src/build_social.py    (writes social-src/all.json, renders assets/Social/*.jpg, prints a summary)

Single posts come from posts.json. Each case study becomes a carousel (cover → The Challenge → Our Approach → What
Shifted → client quote → Key takeaway) and a Story with the same beats. Each resource becomes a multi-part Story.
All copy is verbatim from the site; labels (“The Challenge”, “Key takeaway”) are the case studies' own section names.
"""
import json, os, re, subprocess, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'assets', 'Social')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
D = '20261021'
posts = json.load(open(os.path.join(HERE, 'posts.json')))['posts']
beats = json.load(open(os.path.join(HERE, 'beats.json')))

def first_sentence(t):
    m = re.match(r'(.+?[.!?])(\s|$)', t)
    return (m.group(1) if m else t).strip()

def whole_sentences(t, limit=32):
    """Complete sentences from the start of a quote, as many as fit in `limit` words (never cut mid-sentence)."""
    out = []
    for s in re.findall(r'[^.!?]+[.!?]+[”"]?', t):
        if len(' '.join(out + [s]).split()) > limit:
            break
        out.append(s.strip())
    return ' '.join(out)

import math
import numpy as np
_CAT = open(os.path.expanduser('~/.claude/skills/wbt-brand/references/asset-catalog.md')).read()
_INK = {n: [int(v) / 100 for v in b] for n, *b in re.findall(r'`([^`]+\.png)` \d+×\d+ ink (\d+)–(\d+)%×(\d+)–(\d+)%', _CAT)}
_MASS = {}
def mass(path):
    """Darkness-weighted ink coverage of a file's canvas (0..1)."""
    if path not in _MASS:
        im = Image.open(path).convert('RGBA'); im.thumbnail((400, 400)); a = np.asarray(im).astype(float) / 255
        _MASS[path] = float((a[..., 3] * (1 - (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]))).mean())
    return _MASS[path]
def visual_weight(c, iw):
    """Optical weight of a collage: geometric mean of the illustration's outline area and its ink, plus half the spot's ink."""
    ink = _INK.get(c['illus'], [0, 1, 0, 1]); w, h = iw * (ink[1] - ink[0]), iw * (ink[3] - ink[2]); L = max(w, h)
    m_i = mass(os.path.join(ROOT, 'assets/Illustrations', c['illus'])) * iw * iw
    folder, file, n = c['spot']; sp = f'WBT-20260403-{file}-Watercolor-Spots-{n}.png'
    si = _INK.get(sp, [.05, .95, .05, .95]); sw = L / max(si[1] - si[0], (si[3] - si[2]) * 1.057)
    m_s = mass(os.path.join(ROOT, 'assets/Watercolor Textures/Spots', folder, sp)) * sw * sw * 1.057
    return math.sqrt(w * h * m_i) + 0.5 * m_s
# Target: the Leadership moon collage at a 430px illustration, which reads balanced next to the resources.wbt.coach collages.
_TARGET = visual_weight({'illus': 'Full-Moon.png', 'spot': ['Radiant Gold', 'Gold', 2]}, 430)
def balance(c, base=496):
    return round(max(.75, min(1.3, math.sqrt(_TARGET / visual_weight(c, base)))), 3)

items = []
# 1 · Single posts (case studies become carousels instead)
for p in posts:
    if p['layout'] == 'case':
        continue
    sl = dict(p, type=p['layout'])
    if sl.get('collage'):
        sl['collage'] = dict(sl['collage'], scale=balance(sl['collage']))
    items.append({'id': p['id'], 'group': p['group'], 'kind': 'post', 'format': 'post', 'ground': p['ground'], 'tone': p['tone'], 'slides': [sl]})

# 2 · Case study carousels + stories
CASE_STYLE = {   # ground, tone, photo object-position
    'leading-together-under-pressure': ('#061A49', 'dark', '50% 0%'),   # top-anchored: keep the “Collaboration” title
    'developing-endurance-and-agency': ('#F9F8F2', 'light', '50% 45%'),
    'building-conditions-for-results': ('#F9F8F2', 'light', '50% 25%'),
    'repairing-a-ruptured-relationship': ('#ACCDD9', 'light', '50% 35%'),
    'choosing-the-culture-we-build-on-campaigns': ('#1E4D5C', 'dark', '50% 40%'),
    'building-trust-and-motivation-in-one-day': ('#2531A5', 'dark', '50% 40%'),
    'campaign-team-retreat-to-align-at-the-start': ('#F9F8F2', 'light', '50% 35%'),
    'co-leading-an-organization': ('#ACCDD9', 'light', '50% 0%'),   # overhead shot: keep both heads in
    'coaching-to-support-leadership-development': ('#061A49', 'dark', '50% 40%'),
    'facilitation-to-prepare-for-uncertainty': ('#F9F8F2', 'light', '50% 35%'),
    'individual-coaching-for-each-team-member': ('#1E4D5C', 'dark', '50% 35%'),
    'moving-from-stress-to-strategy-with-a-team': ('#F9F8F2', 'light', '50% 40%'),
}
# The live “Moving From Stress to Strategy” page repeats the “Individual Coaching” body word for word (Oct 2026), so its
# carousel leads with its own cover and key takeaway and adds one beat in between: Our Approach as a text slide (the copied
# page lists the approach, so “Individual Coaching” shows it as a list; this one quotes the paragraph instead).
BODY_IS_COPY = {'moving-from-stress-to-strategy-with-a-team'}
ROLE = {'leading-together-under-pressure': 'PPFA Policy Team', 'building-conditions-for-results': 'Development team, Empower'}

def beat(c, key, headline):
    """One slide per case study beat: a list when the page lists it, else the section's opening sentences as a text slide."""
    items = [first_sentence(re.sub(r'^\d+\.\s*', '', x)) for x in c[key]]
    if len(items) >= 2:
        if key == 'shifted':
            items = items[:4] if sum(len(x) for x in items[:4]) < 340 else items[:3]
        return {'type': 'list', 'eyebrow': c['title'], 'headline': headline, 'items': items[:5 if key == 'approach' else 4]}
    fill = lambda p: whole_sentences(p, 42) if len(whole_sentences(p, 42).split()) >= 20 else whole_sentences(p, 58)   # a slide's worth, not one thin line
    para = next((fill(p) for p in c[key + '_p'] if not p.rstrip().endswith(':') and fill(p)), '')
    short = next((whole_sentences(p, 30) for p in c[key + '_p'] if not p.rstrip().endswith(':') and len(whole_sentences(p, 30).split()) >= 10), '')
    return {'type': 'text', 'eyebrow': c['title'], 'headline': headline, 'body': para, **({'story_body': short} if short else {})} if para else None

def excerpt(t, limit=32):
    """Whole sentences from a quote, as many as fit in `limit` words: from the start when the opening sentence fits,
    else from the first later sentence that does (still word for word, never cut mid-sentence)."""
    sents = re.findall(r'[^.!?…]+[.!?…]+[”"]?', t)
    for i in range(len(sents)):
        out = whole_sentences(' '.join(x.strip() for x in sents[i:]), limit)
        if out and len(out.split()) >= 18:
            return out
    return ''

def for_story(slides):
    """Stories get less reading per screen than carousels (about 30 words a frame, at most two frames a beat). A long list
    packs into frames of a point or two, leaving out any single point too long for one screen; a long paragraph splits into
    frames of whole sentences, leaving out a sentence too long to read at a glance. Word for word; only selection and pacing change."""
    W = 30
    out = []
    for sl in slides:
        if sl['type'] == 'list' and len(' '.join(sl['items']).split()) > 24:
            frames, cur = [], []
            for x in (x for x in sl['items'] if len(x.split()) <= 26):
                if cur and (len(' '.join(cur + [x]).split()) > W or len(cur) == 2):
                    frames.append(cur); cur = []
                cur.append(x)
            frames.append(cur)
            out += [dict(sl, items=f) for f in frames[:2] if f]
        elif sl['type'] == 'text' and sl.get('story_body') and len(sl['body'].split()) > W and \
                not any(len(ch.split()) <= W + 4 for ch in re.findall(r'[^.!?]+[.!?]+[”"]?', sl['body'])):
            out.append(dict(sl, body=sl['story_body']))   # every sentence of the carousel's paragraph is too long: use a shorter passage from the same section
        elif sl['type'] == 'text' and sl.get('body') and len(sl['body'].split()) > W:
            chunks, cur = [], []
            for sent in re.findall(r'[^.!?]+[.!?]+[”"]?', sl['body']):
                if cur and len(' '.join(cur + [sent]).split()) > W:
                    chunks.append(' '.join(x.strip() for x in cur)); cur = []
                cur.append(sent)
            chunks.append(' '.join(x.strip() for x in cur))
            short = [ch for ch in chunks if len(ch.split()) <= W + 4] or chunks[:1]
            out += [dict(sl, body=ch) for ch in short[:2]]
        else:
            out.append(sl)
    return out

def head_for(name):
    f = 'head-' + re.sub(r'[^a-z]+', '-', name.lower()).strip('-') + '.jpg'
    return f if os.path.exists(os.path.join(HERE, 'photos', f)) else None

for c in beats['cases']:
    ground, tone, pos = CASE_STYLE[c['slug']]
    slides = [{'type': 'cover', 'photo': c['slug'] + '.jpg', 'pos': pos, 'eyebrow': 'Case study · ' + c['service'], 'headline': c['title'], 'deck': c['lede'], 'cta': 'Swipe →'}]
    if c['slug'] in BODY_IS_COPY:
        para = next((whole_sentences(p, 58) for p in c['approach_p'] if not p.rstrip().endswith(':') and whole_sentences(p, 58)), '')
        if para:
            slides.append({'type': 'text', 'eyebrow': c['title'], 'headline': 'Our Approach', 'body': para})
    else:
        slides += [b for b in (beat(c, 'challenge', 'The Challenge'), beat(c, 'approach', 'Our Approach'),
                               beat(c, 'shifted', re.sub(r'^The ', '', c['shift_label']) if c['shift_label'] else 'What Shifted')) if b]
        named = [q for q in c['quotes'] if q['role'] and q['name'] and not q['name'].startswith('—') and excerpt(q['text'])]
        if named:   # named people with their own role line (and headshot when we have one): up to two voices
            for q in named[:2]:
                slides.append({'type': 'quote', 'quote': excerpt(q['text']), 'name': q['name'], 'role': q['role'], **({'head': head_for(q['name'])} if head_for(q['name']) else {})})
        else:
            q = next((q for q in c['quotes'] if excerpt(q['text'])), None)
            if q:
                cite = q['name'].lstrip('— ').strip()
                slides.append({'type': 'quote', 'quote': excerpt(q['text']), 'name': 'In their words',
                               'role': ROLE.get(c['slug']) or (cite if cite and cite != 'Client' else '') or c['client'] or 'Client'})
    # the asterisk takes the eyebrow's color (gold on dark, ochre on light, Clean Slate on Calm Blue), so takeaways keep the carousel's ground
    slides.append({'type': 'takeaway', 'eyebrow': 'Key takeaway', 'headline': c['takeaway'], 'cta': 'Read the case study at workbettertogether.coach'})
    for fmt in ('post', 'story'):
        items.append({'id': f"case-{c['slug']}-{fmt}", 'group': 'Case studies', 'kind': 'carousel' if fmt == 'post' else 'story',
                      'format': fmt, 'ground': ground, 'tone': tone, 'title': c['title'], 'slides': slides if fmt == 'post' else for_story(slides)})

# 3 · Resource stories
RES_COVER = {p['id']: p for p in posts if p['group'] == 'Resources'}
RES_MAP = {'leaders/values-and-energy': 'resource-values-energy', 'teams/after-action-review': 'resource-after-action',
           'teams/role-clarity': 'resource-role-clarity', 'retreats/retreat-planning-checklist': 'resource-retreat',
           'career-transitions/career-timeline': 'resource-career', 'campaign-leaders': 'resource-campaign'}
for r in beats['resources']:
    cover = dict(RES_COVER[RES_MAP[r['path']]]); cover['type'] = cover['layout']; cover.pop('cta', None)
    if cover.get('collage'):
        cover['collage'] = dict(cover['collage'], scale=balance(cover['collage']))
    paras = [p for p in r['paras'] if 'Load saved' not in p and 'Step 1 of' not in p and len(p.split()) >= 12]   # a real description, not a label
    slides = [cover]
    if paras:
        slides.append({'type': 'text', 'eyebrow': cover['headline'], 'headline': '', 'body': paras[0]})
    heads = [h for h in r['heads'] if not re.search(r'resources?$|^Start here', h)][:5]
    if heads:
        slides.append({'type': 'list', 'eyebrow': cover['headline'], 'headline': 'What’s inside', 'items': heads})
    slides.append({'type': 'text', 'eyebrow': 'Free resource', 'headline': 'resources.wbt.coach', 'deck': 'Free when you join our newsletter.', 'cta': 'Tap the link →'})
    items.append({'id': 'story-' + RES_MAP[r['path']], 'group': 'Resources', 'kind': 'story', 'format': 'story',
                  'ground': cover['ground'], 'tone': cover['tone'], 'title': cover['headline'], 'slides': slides})

# Ink bounds (fractions of each file's canvas) from the WBT skill's asset catalog, so collages place the real ink, not the canvas.
CAT = os.path.expanduser('~/.claude/skills/wbt-brand/references/asset-catalog.md')
INK = {name: [int(v) / 100 for v in box] for name, *box in re.findall(r'`([^`]+\.png)` \d+×\d+ ink (\d+)–(\d+)%×(\d+)–(\d+)%', open(CAT).read())}
# Corner spots: on plain light grounds, some inside slides get a watercolor spot bleeding off the bottom-right corner,
# under the logo. Light spots keep the dark logo; darker spots knock the logo out to Clear White. Not on every slide.
SERVICE_SPOT = {'Team Coaching': ['Intentional Blue', 'Intentional-Blue', 7, True], 'Leadership Coaching': ['Radiant Gold', 'Gold', 1, False], '2:2 Coaching': ['Intentional Blue', 'Intentional-Blue', 7, True],
                'Facilitation + Training': ['Honest Ochre', 'Honest-Ochre', 7, True]}   # brushstroke shape 7; textured wash 1 for gold
LIGHT_SPOT = {'Calm Blue': False, 'Radiant Gold': False}
for it in items:
    if len(it['slides']) < 2 or it['tone'] != 'light' or it['ground'].startswith('wash:'):
        continue
    first = it['slides'][0]
    if first.get('collage'):
        folder, file, n = first['collage']['spot']; spot = [folder, file, 1 if folder in LIGHT_SPOT else 7, not LIGHT_SPOT.get(folder, False)]
    else:
        svc = next((v for k, v in SERVICE_SPOT.items() if k in (first.get('eyebrow') or '')), None)
        if not svc:
            continue
        spot = svc
    for i, sl in enumerate(it['slides']):
        if i % 2 == 1 and sl.get('type') not in ('cover', 'collage') and (sl.get('tone') or it['tone']) == 'light':
            sl['corner'] = spot
json.dump({'items': items, 'ink': INK}, open(os.path.join(HERE, 'all.json'), 'w'), indent=1, ensure_ascii=False)

# Render every slide
os.makedirs(OUT, exist_ok=True)
only = sys.argv[1] if len(sys.argv) > 1 else None
n = 0
for it in items:
    if only and only not in it['id']:
        continue
    h = 1920 if it['format'] == 'story' else 1350
    for i, _ in enumerate(it['slides']):
        name = f"WBT-{D}-Social-{it['id']}" + (f"-{i + 1}" if len(it['slides']) > 1 else '')
        png = os.path.join(OUT, name + '.png')
        subprocess.run([CHROME, '--headless=new', '--hide-scrollbars', '--force-device-scale-factor=1', '--virtual-time-budget=9000',
                        f'--window-size=1080,{h}', f'--screenshot={png}', f'http://localhost:8791/social-src/post.html?id={it["id"]}&s={i}'],
                       capture_output=True, check=True)
        dom = subprocess.run([CHROME, '--headless=new', '--virtual-time-budget=9000', f'--window-size=1080,{h}', '--dump-dom',
                              f'http://localhost:8791/social-src/post.html?id={it["id"]}&s={i}'], capture_output=True, text=True).stdout
        if 'data-collision="1"' in dom:
            print('COLLISION (text still reaches the CTA/logo):', name)
        im = Image.open(png).convert('RGB')
        im.save(os.path.join(OUT, name + '.jpg'), quality=84, optimize=True, progressive=True)
        os.replace(png, os.path.join(os.environ.get('TMPDIR', '/tmp'), os.path.basename(png)))
        n += 1
print(len(items), 'items,', n, 'slides rendered →', OUT)
print({k: sum(1 for i in items if i['kind'] == k) for k in ('post', 'carousel', 'story')})
