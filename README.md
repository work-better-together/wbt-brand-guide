# Work Better Together — Brand Guide & Toolkit

A living brand guide and production toolkit for Work Better Together, built as a collection of HTML/CSS/JS pages. Open `index.html` in a browser to navigate the full guide.

---

## Project Structure

```
WBT Brand Guide/
├── index.html              ← start here
├── nav.js                  ← shared navigation (injected into every page)
├── motion-src/             ← sources + render script for the Motion videos
├── downloads-src/          ← script that builds assets/Downloads/
├── deck-stage.js           ← deck builder utility
├── [page].html             ← brand guide and tool pages
│
├── assets/                 ← all brand assets — organized library
│   ├── Client Logos/
│   ├── Downloads/          ← generated (logo kit, motion kit, fonts, starter deck)
│   ├── Finished Collages/
│   ├── Fonts/
│   ├── Frames/  Shapes/  Patterns/
│   ├── Generated Illustrations/  ← saved from the Collage Maker
│   ├── Illustrations/
│   ├── Logos/
│   ├── Motion/             ← generated end cards, stings, social loops
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
│   ├── deck-assets/        ← the deck's own copies of the files it uses
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

### Design System
| Page | File |
|---|---|
| Voice | voice.html |
| Logo | logo.html |
| Type | type.html |
| Color | color.html |
| Elements | elements.html |
| Collages | collages.html |
| Photos | photos.html |
| Patterns | patterns.html |
| Components | components.html |
| Iconography | iconography.html |
| Swag | swag.html |
| Clients | clients.html |
| Motion | motion.html |
| Social | social.html |
| Data Viz | data-viz.html |
| Microcopy | microcopy.html |
| Tokens | tokens.html (Type Scale: type-scale.html) |

### Tools
| Page | File |
|---|---|
| Collage Maker | collage-maker.html |
| Deck Template | deck-template/index.html |
| Newsletter | newsletter.html |
| Downloads | downloads.html |

---

## Adding Assets

All assets go in `assets/` — no loose files anywhere else. Follow the naming conventions below. `Downloads/` and `Motion/` are generated: change the source and rebuild (see CLAUDE.md › Generated files).

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

`deck-assets/` holds copies of only the files the deck uses (some under the deck's own names). When the deck needs a new file, copy that one file in; don't sync the whole library.

---

## Hosting

Live at https://brand.wbt.coach (Netlify site `wbtbrand`, Hyperakt's team), deployed automatically from `main` of `github.com/work-better-together/wbt-brand-guide`. Details, previews and the build-credit caveat are in `CLAUDE.md`.
