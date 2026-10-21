"""Write social.html (the Social page) from social-src/all.json and the rendered assets/Social/*.jpg.
Makes 860px phone-size copies in assets/Social/phone/ (and Story posters in thumbs/). Run after build_social.py:  python3 social-src/build_page.py
"""
import json, os, html
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
S = 'assets/Social/'
D = '20261021'
items = json.load(open(os.path.join(HERE, 'all.json')))['items']
os.makedirs(os.path.join(ROOT, S, 'thumbs'), exist_ok=True)
os.makedirs(os.path.join(ROOT, S, 'phone'), exist_ok=True)

def files(it):
    n = len(it['slides'])
    return [f"WBT-{D}-Social-{it['id']}" + (f"-{i + 1}" if n > 1 else '') + '.jpg' for i in range(n)]

def phone(f):
    """An 860px copy for the page: posts show at phone size (390px wide, as Instagram shows them), sharp on 2x screens."""
    src, dst = os.path.join(ROOT, S, f), os.path.join(ROOT, S, 'phone', f)
    im = Image.open(src); im.thumbnail((860, 1600)); im.save(dst, quality=82, optimize=True, progressive=True)
    return S + 'phone/' + f

def thumb(f):   # small poster for the animated Stories
    src, dst = os.path.join(ROOT, S, f), os.path.join(ROOT, S, 'thumbs', f)
    im = Image.open(src); im.thumbnail((600, 1100)); im.save(dst, quality=80, optimize=True, progressive=True)
    return S + 'thumbs/' + f

GROUND = {'#F9F8F2': 'Clear White', '#ACCDD9': 'Calm Blue', '#061A49': 'Steady Blue', '#1E4D5C': 'Clean Slate', '#2531A5': 'Intentional Blue'}
def ground_name(g):
    if g.startswith('wash:'):
        return g.split(':')[1].replace('-', ' ') + ' watercolor'
    return GROUND.get(g, g)

LAYOUT = {'collage': 'Collage', 'quote': 'Quote', 'stat': 'Stat', 'text': 'Type only'}
def alt(it, k):
    sl = it['slides'][k]
    return html.escape(sl.get('headline') or sl.get('quote') or sl.get('stat') or sl.get('body') or it.get('title', ''), quote=True)

def post(it, caption):
    """A post as it sits in the Instagram feed: one slide at a time, swipe or arrows, a 1/n counter and dots."""
    fs = files(it); n = len(fs)
    imgs = ''.join(f'<img src="{phone(f)}" alt="{alt(it, k)}" loading="lazy" width="860" height="1075">' for k, f in enumerate(fs))
    nav = (f'<span class="ig-count">1/{n}</span><button class="ig-prev" aria-label="Previous slide" hidden></button><button class="ig-next" aria-label="Next slide"></button>'
           if n > 1 else '')
    dots = f'<div class="ig-dots">{"<i></i>" * n}</div>' if n > 1 else ''
    return (f'<figure class="ig"><div class="ig-frame"><div class="ig-track">{imgs}</div>{nav}</div>{dots}'
            f'<figcaption>{caption}</figcaption></figure>')

def story(it):
    """A Story at phone size, animated (render_stories.py), with a play/pause button."""
    fs = files(it)
    v = f"stories/WBT-{D}-Social-{it['id']}.mp4"
    title = html.escape(it.get("title", ""), quote=True)
    return (f'<figure class="ig story"><div class="ig-frame"><video src="{S}{v}" poster="{phone(fs[0])}" muted playsinline preload="none" '
            f'aria-label="{title}, animated Story"></video><button class="ig-play" aria-label="Play {title}"></button></div>'
            f'<figcaption><b>{html.escape(it.get("title", ""))}</b> · {len(fs)} frames</figcaption></figure>')

groups = ['Services', 'Testimonials', 'Stats', 'Resources', 'Insights']
singles = {g: [i for i in items if i['kind'] == 'post' and i['group'] == g] for g in groups}
carousels = [i for i in items if i['kind'] == 'carousel']
case_stories = [i for i in items if i['kind'] == 'story' and i['group'] == 'Case studies']
res_stories = [i for i in items if i['kind'] == 'story' and i['group'] == 'Resources']

head = open(os.path.join(ROOT, 'downloads.html')).read()
head = head[:head.index('    .dl-head {')].replace('<title>Downloads — Work Better Together</title>', '<title>Social — Work Better Together</title>')
page = head + """
    /* Phone size: Instagram shows a 1080px post about 390px wide on a phone, so that's how big they are here. */
    .ig-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(0, 390px)); gap: 40px 32px; }
    .ig { margin: 0; width: 100%; max-width: 390px; }
    .ig-frame { position: relative; aspect-ratio: 4 / 5; overflow: hidden; background: #F9F8F2; }
    .ig.story .ig-frame { aspect-ratio: 9 / 16; cursor: pointer; background: #061A49; }
    .ig-track { display: flex; height: 100%; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }
    .ig-track::-webkit-scrollbar { display: none; }
    .ig-track img { flex: 0 0 100%; width: 100%; height: 100%; object-fit: cover; scroll-snap-align: start; display: block; }
    .ig.story img, .ig.story video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
    .ig-count { position: absolute; top: 12px; right: 12px; font: 600 12px/1 var(--font-display); color: #fff; background: rgba(6, 26, 73, .62); padding: 6px 9px; border-radius: 12px; }
    .ig-prev, .ig-next { position: absolute; top: 50%; width: 30px; height: 30px; margin-top: -15px; border: 0; border-radius: 50%; background: rgba(249, 248, 242, .88); cursor: pointer; padding: 0; }
    .ig-prev { left: 10px; } .ig-next { right: 10px; }
    .ig-prev::before, .ig-next::before { content: ''; position: absolute; left: 50%; top: 50%; width: 8px; height: 8px; border: solid #061A49; border-width: 2px 2px 0 0; }
    .ig-next::before { transform: translate(-65%, -50%) rotate(45deg); } .ig-prev::before { transform: translate(-35%, -50%) rotate(-135deg); }
    .ig-dots { display: flex; justify-content: center; gap: 4px; padding-top: 12px; }
    .ig-dots i { width: 6px; height: 6px; border-radius: 50%; background: #C9CCD6; }
    .ig-dots i.on { background: #2531A5; }
    .ig-play { position: absolute; left: 14px; bottom: 14px; width: 44px; height: 44px; border: 0; border-radius: 50%; background: rgba(249, 248, 242, .92); cursor: pointer; padding: 0; }
    .ig-play::before { content: ''; position: absolute; left: 17px; top: 13px; border: solid transparent; border-width: 9px 0 9px 14px; border-left-color: #061A49; }
    .ig-play.on::before { left: 15px; top: 14px; width: 4px; height: 16px; border: 0; border-left: 4px solid #061A49; border-right: 4px solid #061A49; box-sizing: content-box; }
    .ig figcaption { font-family: var(--font-display); font-weight: 500; font-size: 13px; padding-top: 10px; }
    .ig figcaption b { font-weight: 700; }
    .sp-group { font-family: var(--font-display); font-weight: 700; font-size: 20px; margin: 48px 0 18px; }
    .sp-group:first-of-type { margin-top: 0; }
    .ig-stories { display: grid; grid-template-columns: repeat(auto-fill, minmax(0, 390px)); gap: 48px 32px; }
    .ig-pair { display: contents; }
    .sp-rules { columns: 2; column-gap: 48px; font-family: var(--font-body); font-size: 15px; line-height: 1.65; padding-left: 18px; }
    .sp-rules li { break-inside: avoid; margin-bottom: 10px; }
    .sp-prompts { list-style: none; border-top: 1px solid var(--border-subtle); }
    .sp-prompts li { font-family: var(--font-body); font-style: italic; font-size: 17px; padding: 14px 0; border-bottom: 1px solid var(--border-subtle); }
    .section-block a { color: inherit; }
    @media (max-width: 700px) { .ig-grid, .ig-stories { grid-template-columns: minmax(0, 1fr); justify-items: center; } .sp-rules { columns: 1; } .section-block { margin-bottom: 56px; } }
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
    <p class="section-intro">Single posts at 1080×1350. Collage posts sit on light grounds so the black scribble reads; quotes, stats and type-only posts can go dark. Most grounds are solid brand colors, with an occasional watercolor wash. Every word here comes from our site, case studies and resources. Shown at phone size, as they appear in the feed.</p>
""" + ''.join(f'    <h3 class="sp-group">{g}</h3>\n    <div class="ig-grid">\n      ' + '\n      '.join(post(i, f"{LAYOUT.get(i['slides'][0]['type'], i['slides'][0]['type'])} · {ground_name(i['ground'])}") for i in singles[g]) + '\n    </div>\n' for g in groups if singles[g]) + """  </div>

  <div class="section-block">
    <div class="section-label">Case study carousels</div>
    <p class="section-intro">Every case study on our site becomes a carousel that walks through its beats: the photo and title, The Challenge, Our Approach, what shifted, the client in their own words, and the key takeaway. Where a case study tells a beat in prose rather than a list, the slide uses its opening sentences, word for word. Swipe, or use the arrows, as on Instagram.</p>
    <div class="ig-grid">
""" + ''.join('      ' + post(i, f"<b>{html.escape(i['title'])}</b> · {len(i['slides'])} slides") + '\n' for i in carousels) + """    </div>
""" + """  </div>

  <div class="section-block">
    <div class="section-label">Stories</div>
    <p class="section-intro">Stories at 1080×1920, with text kept out of the top 250px and bottom 340px where the app's buttons sit. Case studies tell the same beats as their carousels; each free resource gets a short series ending on the link. Stories carry less reading than carousels: about 30 words a screen, so a long beat runs over two frames. Shown at phone size and animated with <a href="motion.html">Come Together</a>: each frame's words gather line by line, hold long enough to read, then drift apart into the next. Press play.</p>
    <h3 class="sp-group">Case studies</h3>
    <div class="ig-stories">
""" + ''.join('      ' + story(i) + '\n' for i in case_stories) + """    </div>
    <h3 class="sp-group">Free resources</h3>
    <div class="ig-stories">
""" + ''.join('      ' + story(i) + '\n' for i in res_stories) + """    </div>
""" + """  </div>

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
  // Carousels: swipe (scroll-snap) or arrows; the 1/n counter, dots and arrows follow the slide in view.
  document.querySelectorAll('.ig').forEach(fig => {
    const track = fig.querySelector('.ig-track'); if (!track || track.children.length < 2) return;
    const n = track.children.length, dots = fig.querySelectorAll('.ig-dots i'), count = fig.querySelector('.ig-count');
    const prev = fig.querySelector('.ig-prev'), next = fig.querySelector('.ig-next');
    const show = () => { const k = Math.round(track.scrollLeft / track.clientWidth);
      dots.forEach((d, i) => d.classList.toggle('on', i === k)); count.textContent = `${k + 1}/${n}`; prev.hidden = k === 0; next.hidden = k === n - 1; };
    prev.onclick = () => track.scrollBy({ left: -track.clientWidth, behavior: 'smooth' });
    next.onclick = () => track.scrollBy({ left: track.clientWidth, behavior: 'smooth' });
    track.addEventListener('scroll', () => requestAnimationFrame(show), { passive: true }); show();
  });
  // Stories: one play/pause button each; only one plays at a time, and it pauses when scrolled away.
  const vids = [...document.querySelectorAll('.ig.story video')];
  const sync = v => { const b = v.nextElementSibling, on = !v.paused; b.classList.toggle('on', on); b.setAttribute('aria-label', (on ? 'Pause ' : 'Play ') + v.getAttribute('aria-label')); };
  vids.forEach(v => {
    v.nextElementSibling.onclick = () => { if (v.paused) { vids.forEach(o => o !== v && o.pause()); v.play().catch(() => {}); } else v.pause(); };
    ['play', 'pause', 'ended'].forEach(e => v.addEventListener(e, () => sync(v)));
  });
  const io = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) e.target.pause(); }), { threshold: 0.2 });
  vids.forEach(v => io.observe(v));
</script>
</body>
</html>
"""
open(os.path.join(ROOT, 'social.html'), 'w').write(page)
print('social.html written;', sum(len(files(i)) for i in items), 'images,', len(items), 'items')
