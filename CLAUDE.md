# WBT Brand Guide — Claude Instructions

This is the Work Better Together brand guide and toolkit, built as a collection of HTML/CSS/JS pages. Read this file before doing any work.

---

## Project Structure

```
WBT Brand Guide/
├── index.html              ← home/hub page with section nav
├── nav.js                  ← shared navigation injected into every page
├── deck-stage.js           ← deck builder utility
├── [page].html             ← brand guide pages (see Page Index below)
├── CLAUDE.md               ← you are here
├── README.md               ← human-readable version of this doc
├── WBT-Brand-Context.md    ← brand strategy and context document
│
├── assets/                 ← ALL brand assets — single source of truth
│   ├── Client Logos/       ← WBT-client-logo-{slug}.png
│   ├── Finished Collages/  ← WBT-collage-{description}.png
│   ├── Fonts/              ← variable TTF font files
│   ├── Illustrations/      ← Title-Case-Name.png
│   ├── Logos/              ← WBT-{YYYYMMDD}-{Description}.svg (dated)
│   ├── Photography/        ← WBT-{Description}.jpg / .png
│   ├── Reference/          ← screenshots, pasted images, temp files
│   ├── Reference Documents/← PDFs (proposals, brand DNA, etc.)
│   ├── Scribbles/          ← WBT-scribble-{description}.png
│   ├── Swag/               ← WBT-{Item-Description}.png
│   └── Watercolor Textures/
│       ├── Backgrounds/{Color Name}/  ← WBT-{YYYYMMDD}-{Color}-Watercolor-Background-{n}.jpg
│       └── Spots/{Color Name}/        ← WBT-{YYYYMMDD}-{Color}-Watercolor-Spots-{n}.png
│
├── deck-template/          ← standalone slide deck template
│   ├── deck-assets/        ← mirrors assets/ exactly — keep in sync
│   ├── fonts/              ← self-contained font copies (deck is standalone)
│   ├── reference/          ← sample deck PDFs
│   ├── DESIGN-RULES.md
│   └── index.html
│
├── chats/                  ← design session transcripts
├── newsletter/             ← newsletter template
└── tokens/                 ← design tokens
```

---

## Page Index

Brand guide pages are named as kebab-case slugs of their nav title.

| File | Title | Section |
|---|---|---|
| voice.html | Voice | Brand Guide |
| logo.html | Logo | Brand Guide |
| type.html | Type | Brand Guide |
| color.html | Color | Brand Guide |
| elements.html | Elements | Brand Guide |
| collages.html | Collages | Brand Guide |
| photos.html | Photos | Brand Guide |
| swag.html | Swag | Brand Guide |
| clients.html | Clients | Brand Guide |
| motion.html | Motion | Brand Guide |
| collage-maker.html | Collage Maker | Tools |
| deck-template/index.html | Deck Template | Tools |
| newsletter.html | Newsletter | Tools |
| social-maker.html | Social Maker | Tools |
| tokens.html | Tokens | Design System |
| components.html | Components | Design System |
| iconography.html | Iconography | Design System |
| data-viz.html | Data Viz | Design System |
| microcopy.html | Microcopy | Design System |

---

## Asset Rules

### assets/ is the single source of truth
- Never leave loose files in the project root or any page folder.
- Every asset belongs in the appropriate `assets/` subfolder.
- When you add a new file, put it in the right folder before referencing it.

### deck-template/deck-assets/ mirrors assets/
- `deck-assets/` should always be a complete mirror of `assets/`.
- When new assets are added to `assets/`, sync them to `deck-assets/` with:
  ```
  rsync -a assets/ deck-template/deck-assets/
  ```
- Do not add files to `deck-assets/` that don't also exist in `assets/`.
- `deck-template/fonts/` is intentionally separate — standalone decks must be self-contained.

### When moving or renaming any asset
1. Move/rename the file in `assets/`.
2. Move/rename the matching file in `deck-template/deck-assets/`.
3. Find and update every HTML/JS reference to the old path. Never leave broken refs.
4. Verify with grep that no old paths remain.

---

## Naming Conventions

Follow these exactly when adding new assets. Do not invent new patterns.

| Folder | Pattern | Example |
|---|---|---|
| Client Logos | `WBT-client-logo-{slug}.png` | `WBT-client-logo-casey-foundation.png` |
| Finished Collages | `WBT-collage-{description}.png` | `WBT-collage-moon-gold.png` |
| Illustrations | `{Title-Case-Name}.png` | `Nest-Bird.png` |
| Logos | `WBT-{YYYYMMDD}-{Description}.svg` | `WBT-20260502-WBT-Monogram-Black.svg` |
| Photography | `WBT-{Description}.jpg` | `WBT-Jenna-Headshot.jpg` |
| Scribbles | `WBT-scribble-{description}.png` | `WBT-scribble-cascading-ovals.png` |
| Swag | `WBT-{Item-Description}.png` | `WBT-Blue-Beanie.png` |
| Watercolor Spots | `WBT-{YYYYMMDD}-{Color}-Watercolor-Spots-{n}.png` | `WBT-20260403-Calm-Blue-Watercolor-Spots-1.png` |
| Watercolor Backgrounds | `WBT-{YYYYMMDD}-{Color}-Watercolor-Background-{n}.jpg` | `WBT-20260403-Steady-Blue-Watercolor-Background-1.jpg` |

### HTML page filenames
- Must be a kebab-case slug of the page's nav title.
- Example: "Collage Maker" → `collage-maker.html`
- When renaming a page, update `nav.js` (two places: ORDER array and the sidebar nav array) and all cross-page `href` references.

---

## Navigation

`nav.js` is injected into every page. It controls:
- The ORDER array (sequential pager — prev/next)
- The sidebar nav (full page list with sections)

When adding a new page, add it to both arrays in `nav.js` and create the `.html` file.

---

## Fonts

Fonts live in `assets/Fonts/` and are referenced in every root-level HTML page as:
```css
url('assets/Fonts/LeagueSpartan-Variable.ttf')
```

`deck-template/index.html` uses its own copy at `fonts/` (relative to deck-template/) — do not change those references.

---

## Reference vs Reference Documents

- `assets/Reference/` — screenshots, pasted images, temporary captures. Low-value, not linked from pages.
- `assets/Reference Documents/` — source PDFs (proposals, brand DNA). Substantive docs.
