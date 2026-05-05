# Work Better Together — Brand Guide & Toolkit

A living brand guide and production toolkit for Work Better Together, built as a collection of HTML/CSS/JS pages. Open `index.html` in a browser to navigate the full guide.

---

## Project Structure

```
WBT Brand Guide/
├── index.html              ← start here
├── nav.js                  ← shared navigation (injected into every page)
├── deck-stage.js           ← deck builder utility
├── [page].html             ← brand guide and tool pages
│
├── assets/                 ← all brand assets — organized library
│   ├── Client Logos/
│   ├── Finished Collages/
│   ├── Fonts/
│   ├── Illustrations/
│   ├── Logos/
│   ├── Photography/
│   ├── Reference/
│   ├── Reference Documents/
│   ├── Scribbles/
│   ├── Swag/
│   └── Watercolor Textures/
│       ├── Backgrounds/{Color}/
│       └── Spots/{Color}/
│
├── deck-template/          ← standalone slide deck template
│   ├── deck-assets/        ← mirrors assets/ — always keep in sync
│   ├── fonts/              ← self-contained (decks are standalone)
│   ├── reference/          ← sample deck PDFs
│   └── index.html
│
├── chats/                  ← design session transcripts
├── newsletter/             ← newsletter template
└── tokens/                 ← design tokens
```

---

## Pages

### Brand Guide
| Page | File |
|---|---|
| Voice | voice.html |
| Logo | logo.html |
| Type | type.html |
| Color | color.html |
| Elements | elements.html |
| Collages | collages.html |
| Photos | photos.html |
| Swag | swag.html |
| Clients | clients.html |
| Motion | motion.html |

### Tools
| Page | File |
|---|---|
| Collage Maker | collage-maker.html |
| Deck Template | deck-template/index.html |
| Newsletter | newsletter.html |
| Social Maker | social-maker.html |

### Design System
| Page | File |
|---|---|
| Tokens | tokens.html |
| Components | components.html |
| Iconography | iconography.html |
| Data Viz | data-viz.html |
| Microcopy | microcopy.html |

---

## Adding Assets

All assets go in `assets/` — no loose files anywhere else. Follow the naming conventions below, then sync to `deck-template/deck-assets/`:

```
rsync -a assets/ deck-template/deck-assets/
```

### Naming Conventions

| Folder | Pattern |
|---|---|
| Client Logos | `WBT-client-logo-{slug}.png` |
| Finished Collages | `WBT-collage-{description}.png` |
| Illustrations | `{Title-Case-Name}.png` |
| Logos | `WBT-{YYYYMMDD}-{Description}.svg` |
| Photography | `WBT-{Description}.jpg` |
| Scribbles | `WBT-scribble-{description}.png` |
| Swag | `WBT-{Item-Description}.png` |
| Watercolor Spots | `WBT-{YYYYMMDD}-{Color}-Watercolor-Spots-{n}.png` |
| Watercolor Backgrounds | `WBT-{YYYYMMDD}-{Color}-Watercolor-Background-{n}.jpg` |

---

## Adding Pages

1. Create `{slug}.html` — filename must be a kebab-case slug of the page title.
2. Add the page to both arrays in `nav.js` (ORDER array + sidebar nav array).
3. Link it from `index.html` if it belongs in the home grid.

---

## deck-template

The deck template is designed to be copied out as a standalone project. It does not depend on the brand guide folder — all assets are self-contained in `deck-assets/` and fonts are in its own `fonts/` folder.

When the brand guide's `assets/` library grows, sync changes into `deck-assets/`:
```
rsync -a assets/ deck-template/deck-assets/
```
