"""Render every Story in social-src/all.json as an animated MP4 (Oct 2026).

Each frame of a Story plays post.html's animation mode (?anim=1: Come Together, then a hold long enough to read, then a
drift-out), and the frames are joined into one video per Story at 720×1280 (small enough for the guide; Instagram
upscales Stories cleanly). Needs the local server on :8791 at the repo root, node, ffmpeg and Chrome.
    python3 social-src/render_stories.py [id-filter]
Writes assets/Social/stories/WBT-20261021-Social-<id>.mp4.
"""
import json, os, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'assets', 'Social', 'stories')
RENDER = os.path.expanduser('~/.claude/skills/hkt-brand-guide-builder/scripts/render-timeline.mjs')
D, FPS = '20261021', 30
items = [i for i in json.load(open(os.path.join(HERE, 'all.json')))['items'] if i['format'] == 'story']
only = sys.argv[1] if len(sys.argv) > 1 else None
os.makedirs(OUT, exist_ok=True)

def story(it):
    tmp = tempfile.mkdtemp(prefix='wbt-story-')
    parts = []
    for i in range(len(it['slides'])):
        d = os.path.join(tmp, str(i))
        subprocess.run(['node', RENDER, f"http://localhost:8791/social-src/post.html?id={it['id']}&s={i}&anim=1", d, str(FPS), '1080', '1920'],
                       check=True, capture_output=True)
        parts.append(os.path.join(d, 'f', '%05d.jpg'))
    # one input per frame's image sequence, concatenated in order
    args = ['ffmpeg', '-loglevel', 'error', '-y']
    for p in parts:
        args += ['-framerate', str(FPS), '-i', p]
    args += ['-filter_complex', ''.join(f'[{k}:v]' for k in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0,scale=720:-2[v]',
             '-map', '[v]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '23', '-movflags', '+faststart',
             os.path.join(OUT, f"WBT-{D}-Social-{it['id']}.mp4")]
    subprocess.run(args, check=True)
    return it['id']

todo = [it for it in items if not only or only in it['id']]
with ThreadPoolExecutor(3) as ex:
    for done in ex.map(story, todo):
        print('rendered', done, flush=True)
print(len(todo), 'stories →', OUT)
