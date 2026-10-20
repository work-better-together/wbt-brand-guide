"""Build assets/Downloads/ for downloads.html from the official files (draft for review, Oct 2026).

  Logos   wordmark + monogram in each approved ink (logo.html pairings), SVG (fill swapped from the black master)
          + 1000px-wide transparent PNG (headless Chrome); one ZIP of everything
  Motion  the end cards, stings and social loops from assets/Motion/ as one ZIP
  Fonts   League Spartan, Lora, Inconsolata (SIL Open Font License) + their OFL files as one ZIP
  Deck    the starter deck .pptx from the WBT design skill build
Re-run after a logo, motion or font change:  python3 downloads-src/build_downloads.py
"""
import os, re, shutil, subprocess, zipfile, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'assets')
OUT = os.path.join(A, 'Downloads')
SKILL = os.path.expanduser('~/.claude/skills/wbt-brand-designer')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
D = '20261020'

INKS = {   # approved inks, from the logo page's colorway pairings
    'Grounded-Black': '#1F1E1E', 'Intentional-Blue': '#2531A5', 'Clean-Slate': '#1E4D5C', 'Calm-Blue': '#ACCDD9',
    'Steady-Blue': '#061A49', 'Radiant-Gold': '#CD9F36', 'Clear-White': '#F9F8F2',
}
MARKS = {'Wordmark': 'WBT-20260502-Work-Better-Together-Wordmark-Black.svg', 'Monogram': 'WBT-20260502-WBT-Monogram-Black.svg'}

def png(svg_path, out, width=1000):
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', open(svg_path).read()).group(1).split()]
    h = round(width * vb[3] / vb[2])
    html = os.path.join(tempfile.gettempdir(), os.path.basename(out) + '.html')
    open(html, 'w').write(f'<html><body style="margin:0;background:transparent"><img src="file://{svg_path}" style="display:block;width:{width}px;height:{h}px"></body></html>')
    subprocess.run([CHROME, '--headless=new', '--hide-scrollbars', '--default-background-color=00000000', '--force-device-scale-factor=1',
                    f'--window-size={width},{h}', f'--screenshot={out}', 'file://' + html], check=True, capture_output=True)

def zipdir(files, out):
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for f, arc in files:
            z.write(f, arc)
    return out

os.makedirs(os.path.join(OUT, 'Logos'), exist_ok=True)
made = []
for mark, master in MARKS.items():
    src = open(os.path.join(A, 'Logos', master)).read()
    assert 'fill="#1f1e1e"' in src
    for ink, hexv in INKS.items():
        base = f'WBT-{D}-{mark}-{ink}'
        svg = os.path.join(OUT, 'Logos', base + '.svg')
        open(svg, 'w').write(src.replace('fill="#1f1e1e"', f'fill="{hexv}"'))
        png(svg, os.path.join(OUT, 'Logos', base + '.png'))
        made += [svg, os.path.join(OUT, 'Logos', base + '.png')]

kits = {
    f'WBT-{D}-Logo-Kit.zip': [(f, 'WBT-Logo-Kit/' + os.path.basename(f)) for f in sorted(made)],
    f'WBT-{D}-Motion-Kit.zip': [(os.path.join(A, 'Motion', f), 'WBT-Motion-Kit/' + f) for f in sorted(os.listdir(os.path.join(A, 'Motion'))) if f.endswith('.mp4')],
    f'WBT-{D}-Fonts.zip': [(os.path.join(SKILL, 'assets', 'fonts', f), 'WBT-Fonts/' + f) for f in sorted(os.listdir(os.path.join(SKILL, 'assets', 'fonts')))],
}
for name, files in kits.items():
    zipdir(files, os.path.join(OUT, name))
shutil.copy(os.path.join(SKILL, 'assets', 'templates', 'wbt-starter-deck.pptx'), os.path.join(OUT, f'WBT-{D}-Starter-Deck.pptx'))

for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    if os.path.isfile(p):
        print(f'{f:42} {os.path.getsize(p)/1e6:6.2f} MB')
print(len(made), 'logo files')
