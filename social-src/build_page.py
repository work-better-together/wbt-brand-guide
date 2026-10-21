"""Write social.html (the Social page) from social-src/all.json and the rendered assets/Social/*.jpg.
Makes 600px thumbnails in assets/Social/thumbs/. Run after build_social.py:  python3 social-src/build_page.py
"""
import json, os, html
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
S = 'assets/Social/'
D = '20261021'
items = json.load(open(os.path.join(HERE, 'all.json')))['items']
os.makedirs(os.path.join(ROOT, S, 'thumbs'), exist_ok=True)

def files(it):
    n = len(it['slides'])
    return [f"WBT-{D}-Social-{it['id']}" + (f"-{i + 1}" if n > 1 else '') + '.jpg' for i in range(n)]

def thumb(f):
    src, dst = os.path.join(ROOT, S, f), os.path.join(ROOT, S, 'thumbs', f)
    im = Image.open(src); im.thumbnail((600, 1100)); im.save(dst, quality=80, optimize=True, progressive=True)
    return S + 'thumbs/' + f

GROUND = {'#F9F8F2': 'Clear White', '#ACCDD9': 'Calm Blue', '#061A49': 'Steady Blue', '#1E4D5C': 'Clean Slate', '#2531A5': 'Intentional Blue'}
def ground_name(g):
    if g.startswith('wash:'):
        return g.split(':')[1].replace('-', ' ') + ' watercolor'
    return GROUND.get(g, g)

LAYOUT = {'collage': 'Collage', 'quote': 'Quote', 'stat': 'Stat', 'text': 'Type only'}
def tile(it):
    f = files(it)[0]
    sl = it['slides'][0]
    alt = html.escape(sl.get('headline') or sl.get('quote') or sl.get('stat', ''), quote=True)
    return (f'<figure class="sp-tile"><a href="{S}{f}" target="_blank" rel="noopener"><img src="{thumb(f)}" alt="{alt}" loading="lazy" width="600" height="750"></a>'
            f'<figcaption>{LAYOUT.get(sl["type"], sl["type"])} · {ground_name(it["ground"])}</figcaption></figure>')

def video(it):
    """The animated Story (render_stories.py), first in its row, playing only while in view."""
    v = f"stories/WBT-{D}-Social-{it['id']}.mp4"
    if not os.path.exists(os.path.join(ROOT, S, v)):
        return ''
    return (f'<figure class="sp-anim"><video src="{S}{v}" poster="{S}thumbs/{files(it)[0]}" muted loop playsinline preload="none" '
            f'aria-label="{html.escape(it.get("title", ""), quote=True)}, animated Story"></video><figcaption>Animated</figcaption></figure>')

def strip(it, cls):
    imgs = (video(it) if cls == 'sto' else '') + ''.join(f'<a href="{S}{f}" target="_blank" rel="noopener"><img src="{thumb(f)}" alt="{html.escape(it.get("title", ""), quote=True)}, slide {k + 1}" loading="lazy"></a>'
                   for k, f in enumerate(files(it)))
    return f'<div class="sp-set"><div class="sp-set-head">{html.escape(it.get("title", ""))} <span>{len(it["slides"])} {"slides" if cls == "car" else "frames"}</span></div><div class="sp-strip {cls}">{imgs}</div></div>'

groups = ['Services', 'Testimonials', 'Stats', 'Resources', 'Insights']
singles = {g: [i for i in items if i['kind'] == 'post' and i['group'] == g] for g in groups}
carousels = [i for i in items if i['kind'] == 'carousel']
case_stories = [i for i in items if i['kind'] == 'story' and i['group'] == 'Case studies']
res_stories = [i for i in items if i['kind'] == 'story' and i['group'] == 'Resources']

head = open(os.path.join(ROOT, 'downloads.html')).read()
head = head[:head.index('    .dl-head {')].replace('<title>Downloads — Work Better Together</title>', '<title>Social — Work Better Together</title>')
page = head + """
    .sp-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px 20px; }
    .sp-tile { margin: 0; }
    .sp-tile img, .sp-strip img { display: block; width: 100%; height: auto; }
    .sp-tile figcaption { font-family: var(--font-display); font-weight: 500; font-size: 13px; padding-top: 10px; }
    .sp-group { font-family: var(--font-display); font-weight: 700; font-size: 20px; margin: 40px 0 16px; }
    .sp-group:first-of-type { margin-top: 0; }
    .sp-set { margin-bottom: 36px; }
    .sp-set-head { font-family: var(--font-display); font-weight: 700; font-size: 18px; margin-bottom: 12px; }
    .sp-set-head span { font-weight: 500; font-size: 13px; margin-left: 8px; }
    .sp-strip { display: grid; grid-auto-flow: column; gap: 8px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 10px; }
    .sp-strip.car { grid-auto-columns: minmax(220px, 1fr); }
    .sp-strip.sto { grid-auto-columns: 190px; }
    .sp-strip a, .sp-anim { scroll-snap-align: start; }
    .sp-anim { margin: 0; position: relative; }
    .sp-anim video { display: block; width: 100%; aspect-ratio: 9 / 16; background: var(--border-subtle); }
    .sp-anim figcaption { position: absolute; left: 8px; top: 8px; font-family: var(--font-display); font-weight: 600; font-size: 12px; padding: 3px 8px; background: #F9F8F2; color: #061A49; }
    .sp-rules { columns: 2; column-gap: 48px; font-family: var(--font-body); font-size: 15px; line-height: 1.65; padding-left: 18px; }
    .sp-rules li { break-inside: avoid; margin-bottom: 10px; }
    .sp-prompts { list-style: none; border-top: 1px solid var(--border-subtle); }
    .sp-prompts li { font-family: var(--font-body); font-style: italic; font-size: 17px; padding: 14px 0; border-bottom: 1px solid var(--border-subtle); }
    .section-block a { color: inherit; }
    @media (max-width: 1000px) { .sp-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
    @media (max-width: 700px) { .sp-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px 12px; } .sp-rules { columns: 1; } .section-block { margin-bottom: 56px; } }
  </style>
</head>
<body>
<div class="page">

  <header class="page-header">
    <h1>Social</h1>
    <p>How Work Better Together shows up on Instagram and LinkedIn: posts, carousels and Stories, all made from our real words, collages and photos.</p>
  </header>

  <div class="section-block">
    <div class="section-label">Posts</div>
    <p class="section-intro">Single posts at 1080×1350. Collage posts sit on light grounds so the black scribble reads; quotes, stats and type-only posts can go dark. Most grounds are solid brand colors, with an occasional watercolor wash. Every word here comes from our site, case studies and resources. Click any post for the full-size file.</p>
""" + ''.join(f'    <h3 class="sp-group">{g}</h3>\n    <div class="sp-grid">\n      ' + '\n      '.join(tile(i) for i in singles[g]) + '\n    </div>\n' for g in groups if singles[g]) + """  </div>

  <div class="section-block">
    <div class="section-label">Case study carousels</div>
    <p class="section-intro">Every case study on our site becomes a carousel that walks through its beats: the photo and title, The Challenge, Our Approach, what shifted, the client in their own words, and the key takeaway. Where a case study tells a beat in prose rather than a list, the slide uses its opening sentences, word for word. Swipe through each row.</p>
""" + ''.join('    ' + strip(i, 'car') + '\n' for i in carousels) + """  </div>

  <div class="section-block">
    <div class="section-label">Stories</div>
    <p class="section-intro">Stories at 1080×1920, with text kept out of the top 250px and bottom 340px where the app's buttons sit. Case studies tell the same beats as their carousels; each free resource gets a short series ending on the link. The first tile in each row is the Story animated with <a href="motion.html">Come Together</a>: each frame's words gather line by line, hold long enough to read, then drift apart into the next.</p>
    <h3 class="sp-group">Case studies</h3>
""" + ''.join('    ' + strip(i, 'sto') + '\n' for i in case_stories) + """    <h3 class="sp-group">Free resources</h3>
""" + ''.join('    ' + strip(i, 'sto') + '\n' for i in res_stories) + """  </div>

  <div class="section-block">
    <div class="section-label">The rules</div>
    <ul class="sp-rules">
      <li><strong>Sizes.</strong> Headlines 64–92px, body 36px or more, eyebrows 30px, nothing below 26px on a 1080px card. Phones show cards at a third of their size.</li>
      <li><strong>Margins.</strong> 86px (8%) on every side. Text never touches the monogram: keep 24px clear around it.</li>
      <li><strong>Logo.</strong> The monogram, bottom right, 70px tall. Black on light grounds, Clear White on dark.</li>
      <li><strong>Collages.</strong> Spot, then scribble, then illustration, built from the real files. Scribbles stay black, so collage posts go on light grounds.</li>
      <li><strong>Color.</strong> Mostly solid brand colors; a watercolor wash now and then. On dark washes, a tint of the same color keeps text readable.</li>
      <li><strong>Words.</strong> Quotes and case study lines are word for word. Links go in the caption; on Stories, the web address and a link sticker.</li>
      <li><strong>Stats.</strong> Intentional Blue or Honest Ochre on light grounds, Radiant Gold on dark. Always name the source.</li>
      <li><strong>Motion.</strong> Posts can animate with <em>Come Together</em>: see <a href="motion.html">Motion</a>.</li>
    </ul>
  </div>

  <div class="section-block">
    <div class="section-label">Make your own</div>
    <p class="section-intro">Make posts like these with the WBT Brand skill in Claude (staff: download it from the Skills tab on tools.wbt.coach). It knows these layouts, sizes and colors, uses our real collage files, and checks its own work. Try:</p>
    <ul class="sp-prompts">
      <li>Make an Instagram post with a client quote from our website.</li>
      <li>Turn our latest case study into a six-slide carousel and a Story.</li>
      <li>Make a three-part Story announcing our After Action Review worksheet.</li>
      <li>Make a stat post with the 70% leadership figure, on Clear White.</li>
    </ul>
  </div>

</div>
<script src="nav.js"></script>
<script>
  // Animated Stories play while on screen and pause when scrolled away.
  const io = new IntersectionObserver(es => es.forEach(e => e.isIntersecting ? e.target.play().catch(() => {}) : e.target.pause()), { threshold: 0.5 });
  document.querySelectorAll('.sp-anim video').forEach(v => io.observe(v));
</script>
</body>
</html>
"""
open(os.path.join(ROOT, 'social.html'), 'w').write(page)
print('social.html written;', sum(len(files(i)) for i in items), 'images,', len(items), 'items')
