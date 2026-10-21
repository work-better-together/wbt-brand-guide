"""Prepare the whiteboard case study photos for the Social page (Oct 2026).

From the full-color originals in social-src/photos/originals/ (WBT's Cowbird Creative case study images):
  1. Brighten: levels so the paper reads near-white, gentle gamma for the midtones.
  2. Crop: pull in ~8% on every side so the board fills more of the frame.
  3. Marker colors: remap each marker family toward the WBT palette in Lab space, keeping each pixel's lightness
     (so strokes and anti-aliasing stay natural): pink/red → Honest Ochre, blue/purple → Intentional Blue,
     green/teal → Clean Slate. Black and the paper are left alone.
    python3 social-src/prep_photos.py
"""
import os
import numpy as np
from PIL import Image
from skimage import color

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, 'photos', 'originals')
PALETTE = {'ochre': '#B55312', 'blue': '#2531A5', 'slate': '#1E4D5C'}
TARGET_AB = {k: color.rgb2lab(np.array([[[int(v[i:i + 2], 16) / 255 for i in (1, 3, 5)]]]))[0, 0, 1:] for k, v in PALETTE.items()}
# Per-photo crops: Collaboration loses the grey wall at left but keeps its title whole at the top.
CROP = {'leading-together-under-pressure': (0.10, 0.12, 0.06, 0.06)}   # paper edge is ~9.5% from left, ~14% from top: keep the title whole
BOARDS = ['leading-together-under-pressure', 'developing-endurance-and-agency', 'building-conditions-for-results']

def family(hue):
    """Marker family from the Lab hue angle (degrees)."""
    h = hue % 360
    if h < 75 or h >= 330:      # reds, pinks, magentas, oranges
        return 'ochre'
    if 130 <= h < 230:          # greens and teals
        return 'slate'
    if 230 <= h < 330:          # blues and purples
        return 'blue'
    return None                 # yellows: leave

def prep(slug):
    im = Image.open(os.path.join(ORIG, slug + '.jpg')).convert('RGB')
    w, h = im.size
    l, t, r, b = CROP.get(slug, (0.08, 0.08, 0.08, 0.08))      # fractions trimmed from left, top, right, bottom
    im = im.crop((int(w * l), int(h * t), int(w * (1 - r)), int(h * (1 - b))))
    a = np.asarray(im).astype(float) / 255
    # 1 · levels: paper (92nd percentile of lightness) → white; slight gamma lift
    lum = a.mean(axis=2)
    hi, lo = np.percentile(lum, 92), np.percentile(lum, 1)
    a = np.clip((a - lo) / (hi - lo), 0, 1) ** 0.85
    # 2 · marker remap in Lab
    lab = color.rgb2lab(a)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    chroma = np.hypot(A, B); hue = np.degrees(np.arctan2(B, A))
    out = lab.copy()
    for fam, ab in TARGET_AB.items():
        sel = np.vectorize(lambda x: family(x) == fam)(hue) & (chroma > 12)
        strength = np.clip((chroma - 12) / 25, 0, 1)[sel]          # fade in, so faint tints aren't over-coloured
        tgt_chroma = np.hypot(*ab)
        scale = np.clip(chroma[sel] / max(tgt_chroma, 1), 0.6, 1.2)  # keep relative intensity
        out[..., 1][sel] = A[sel] * (1 - strength) + ab[0] * scale * strength
        out[..., 2][sel] = B[sel] * (1 - strength) + ab[1] * scale * strength
        # darken the remapped strokes a touch toward the palette's lightness, so ochre/slate read as ink, not highlighter
        tgt_L = color.rgb2lab(np.array([[[int(PALETTE[fam][i:i + 2], 16) / 255 for i in (1, 3, 5)]]]))[0, 0, 0]
        out[..., 0][sel] = L[sel] * (1 - 0.35 * strength) + tgt_L * 0.35 * strength
    rgb = np.clip(color.lab2rgb(out), 0, 1)
    Image.fromarray((rgb * 255).astype('uint8')).save(os.path.join(HERE, 'photos', slug + '.jpg'), quality=90)
    print('prepared', slug)

if __name__ == '__main__':
    for s in BOARDS:
        prep(s)
