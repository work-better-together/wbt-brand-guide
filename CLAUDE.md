# Work Better Together — Client Context

This folder contains all Hyperakt work for Work Better Together. AI context here is shared across all sub-projects for this client.

## Client Overview
Work Better Together (WBT; its Google Workspace also runs as womensbraintrust.com) is Jenna Shapiro and Stacy Berger's leadership-coaching, team-coaching and facilitation practice for the social-impact sector. Tagline: “Leadership is hard. Let’s work on it.” Site: workbettertogether.coach.

**Relationship:** Hyperakt client

## Sub-Project Structure
Sub-folders follow the convention: `WBT [Project Name]`

## Notes for AI
- All client information is confidential
- Apply Hyperakt's inside-out approach to all strategy and copy work
- Refer to parent HKT AI/CLAUDE.md for Hyperakt philosophy

---

# WBT Brand Guide — Claude Instructions

This is the Work Better Together brand guide and toolkit, built as a collection of HTML/CSS/JS pages. Read this file before doing any work.

---

## ⚠️ Deployment & Workflow (read first)

**Work in the git repo and deploy from it.** The repo is the single source of truth.

- **Working copy (EDIT HERE):** `~/Projects/hkt-client-brand-guides/wbt-brand-guide` → remote `github.com/work-better-together/wbt-brand-guide` (moved from `deroyperaza/`, which still redirects), branch `main`.
- **Live site:** https://brand.wbt.coach — the **Netlify** site `wbtbrand` in Hyperakt's team ("deroyperaza's team"), building automatically from `main` of that repo (no build command; publishes the repo root). It is **not** GitHub Pages. `CNAME` is a leftover.
- **Netlify build credits:** when the Hyperakt team is out of credits, Netlify pauses production deploys, so a push to `main` silently doesn't go live. Check the last published deploy (`npx netlify-cli api getSite --data '{"site_id":"wbtbrand.netlify.app"}'`) and see `~/Projects/hkt-tools-landing/DEPLOY.md` (Oct 20 2026) for the draft-then-publish workaround.
- **Preview a branch without touching live:** from a clean worktree of the branch, `npx netlify-cli deploy --no-build --dir=. --site=wbtbrand --json` gives a draft URL (`https://<id>--wbtbrand.netlify.app`).
- **This Google Drive folder** (`Work Better Together/Brand/2026 WBT Brand Guide`) holds a copy of the files for browsing. Don't edit there; it's slow, and tools can't delete files in it.
- `.github/workflows/update-last-updated.yml` rewrites `last-updated.json` on every push to `main`, so origin moves ahead of you after each push.

**To ship a change:**
1. **Edit in the repo** (on a branch for anything a reviewer should see first; `guide-v2`, the Oct 2026 Motion / Downloads / Social work, was merged and published Oct 21 2026).
2. **Verify locally**: `python3 -m http.server 8791` in the repo root, then check in a browser at 1440 and 375 wide (drive the actual UI; don't trust a syntax check alone).
3. `git add …` → **`git pull --rebase origin main`** first (the collage maker and the last-updated workflow both commit to `main`) → `git push origin main`.
4. Netlify publishes in ~1 min. **Verify against the live URL**, not just the push.

**Collage save (collage-maker.html):** saving a collage POSTs to a Cloudflare Worker — `wbt-collage-save.workbettertogether.workers.dev` (source in `collage-save-worker/`) — which holds the GitHub token server-side. **No API tokens live in any page.** Worker secrets (`GITHUB_TOKEN`, `SHARED_SECRET`) are set via `wrangler secret put`; never hard-code them. The gallery (`collages.html`) reads `assets/Generated Illustrations/manifest.json` over a plain public URL.

**Concept illustrations** are served locally from `assets/Illustrations/`, not from Airtable. `elements.html` renders a single A–Z **`CONCEPTS`** array (the "Concept Image Library"); `collage-maker.html` builds its picker from `STATIC_CONCEPTS` + `LIBRARY_CONCEPTS`. Keep the two illustration sets in sync (both currently offer the same 102 illustrations). See `CHANGELOG.md` for the full history of this rework.

---

## Project Structure

```
WBT Brand Guide/
├── index.html              ← home/hub page with section nav
├── nav.js                  ← shared navigation injected into every page (ORDER pager + drawer groups)
├── motion-src/             ← sources for the Motion page videos (logo-moves.html, social-moves.html, render-all.sh)
├── downloads-src/          ← build_downloads.py: makes assets/Downloads/ (logo kit, motion kit, fonts, starter deck)
├── social-src/             ← Social page examples: extract.py (verbatim beats) → build_social.py (render) → render_stories.py (animated Story MP4s) → build_page.py (social.html)
├── _redirects              ← Netlify redirects (old /social-maker → /social)
├── deck-stage.js           ← deck builder utility
├── [page].html             ← brand guide pages (see Page Index below)
├── CLAUDE.md               ← you are here
├── README.md               ← human-readable version of this doc
├── WBT-Brand-Context.md    ← brand strategy and context document
│
├── assets/                 ← ALL brand assets — single source of truth
│   ├── Client Logos/       ← WBT-client-logo-{slug}.png
│   ├── Downloads/          ← GENERATED by downloads-src/build_downloads.py; don't hand-edit
│   ├── Finished Collages/  ← WBT-collage-{description}.png
│   ├── Frames/, Shapes/, Patterns/  ← hand-drawn frames, cut-paper shapes, repeat patterns
│   ├── Generated Illustrations/     ← collages saved from the Collage Maker (+ manifest.json)
│   ├── Fonts/              ← variable TTF font files
│   ├── Illustrations/      ← Title-Case-Name.png
│   ├── Logos/              ← WBT-{YYYYMMDD}-{Description}.svg (dated; Black and Clear White masters)
│   ├── Motion/             ← GENERATED by motion-src/render-all.sh: end cards, stings, social loops (+ -poster.jpg)
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
│   ├── deck-assets/        ← the deck's own copies of the files it uses (NOT a mirror of assets/)
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

Brand guide pages are named as kebab-case slugs of their nav title. Nav groups as in `nav.js`.

| File | Title | Nav group |
|---|---|---|
| voice.html | Voice | Design System |
| logo.html | Logo | Design System |
| type.html | Type | Design System |
| color.html | Color | Design System |
| elements.html | Elements | Design System |
| collages.html | Collages | Design System |
| photos.html | Photos | Design System |
| patterns.html | Layout Patterns (nav: Patterns) | Design System |
| components.html | Components | Design System |
| iconography.html | Iconography | Design System |
| swag.html | Swag | Design System |
| clients.html | Clients | Design System |
| motion.html | Motion | Design System |
| social.html | Social (posts, carousels, Stories; built from `social-src/`) | Design System |
| data-viz.html | Data Viz | Design System |
| microcopy.html | Microcopy | Design System |
| tokens.html | Tokens | Design System |
| collage-maker.html | Collage Maker | Tools |
| deck-template/index.html | Deck Template | Tools |
| newsletter.html | Newsletter | Tools |
| downloads.html | Downloads | Tools |
| type-scale.html | Type Scale | not in nav; linked from Tokens |

---

## Asset Rules

### assets/ is the single source of truth
- Never leave loose files in the project root or any page folder.
- Every asset belongs in the appropriate `assets/` subfolder.
- When you add a new file, put it in the right folder before referencing it.

### deck-template/deck-assets/ is the deck's own copy
- The deck template is standalone, so it carries copies of only the files it uses, some under its own names (`bg-steady-blue-1.jpg`, `spot-gold-2.png`). It is **not** a mirror of `assets/` (they differ by ~500 MB) — don't rsync the whole library into it.
- When the deck needs a new file, copy that file into `deck-assets/` and reference it there.
- `deck-template/fonts/` is intentionally separate — standalone decks must be self-contained.

### When moving or renaming any asset
1. Move/rename the file in `assets/`.
2. If the deck template uses that file, update its copy in `deck-template/deck-assets/` too.
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

## Generated files (edit the source, then rebuild)

- `assets/Motion/*.mp4` + posters ← `motion-src/*.html` via `bash motion-src/render-all.sh` (needs the local server on :8791, node, ffmpeg, Chrome). Version filenames when re-rendering a published video.
- `assets/Social/` + `social.html` ← `social-src/` (`extract.py`, then `build_social.py` with the :8791 server running, then `render_stories.py` for the animated Stories in `assets/Social/stories/`, then `build_page.py`). `post.html` is the renderer for every card (`?id=&s=`, `&anim=1` for motion, `&probe=1` to QA animated text). Copy comes word for word from workbettertogether.coach and resources.wbt.coach.
- `assets/Downloads/` ← `python3 downloads-src/build_downloads.py` (logo kit = wordmark + monogram in the 7 approved inks; starter deck and fonts come from the WBT design skill at `~/.claude/skills/wbt-brand`).

## The WBT design skill

The Claude skill `wbt-brand` (one version for everyone) lives at `~/.claude/skills/wbt-brand`; build notes in its `build/README.md`. WBT staff get it from tools.wbt.coach › Skills (repo `work-better-together/wbt-tools`; publishing that site is Jenna's: it's in WBT's own Netlify team). The guide's Downloads page also offers the ZIP publicly with install steps (`downloads.html#claude-skill`, copied by `build_downloads.py`). When the guide's rules change, update the skill too.

## Reference vs Reference Documents

- `assets/Reference/` — screenshots, pasted images, temporary captures. Low-value, not linked from pages.
- `assets/Reference Documents/` — source PDFs (proposals, brand DNA). Substantive docs.
