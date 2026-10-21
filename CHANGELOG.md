# WBT Brand Guide — Changelog

Notable changes to the brand guide site (brand.wbt.coach). Newest first.

---

## 2026-10-21 — Motion, Downloads, Social Maker fixes, generic-UI cleanup (branch `guide-v2`, in review)

### Claude skill download (`downloads.html#claude-skill`)
- The WBT Brand skill ZIP is now a download on the guide itself, with step-by-step install for Claude (web/desktop: Settings › Capabilities › Skills › Upload skill) and Claude Code (unzip into `~/.claude/skills/`). The Social page links there. `downloads-src/build_downloads.py` copies the ZIP from the skill's build.

### Motion (`motion.html`)
- New sections at the top: **the motion idea** (“Calm under pressure. Hold steady, then move with intent.”), **logo animation** (*Come Together*: the letters start spaced out, fade in and come together; wordmark and monogram) with end cards in 16:9, 9:16 and 1:1 on Clear White and Steady Blue, **social posts in motion** (*Collage Gather* + *Line Rise* on the headline, quote and stat posts), and a **move library** naming all six moves. Videos play only while visible, with a page-level Pause and poster frames; reduced motion shows the still logo.
- Sources in `motion-src/` (`logo-moves.html`, `social-moves.html`, `render-all.sh`); output in `assets/Motion/`.

### Downloads (`downloads.html`, new)
- Wordmark and monogram in all seven approved inks (SVG + 1000px transparent PNG) on their paired grounds, a logo-kit ZIP, the motion kit, the fonts (OFL), the 8-slide starter deck (.pptx) and a pointer to the WBT Claude skill on tools.wbt.coach. Built by `downloads-src/build_downloads.py`; added to `nav.js` and the home page.
- New Clear White logo masters in `assets/Logos/` (fill swapped from the black masters).

### Social Card Maker
- The line under a headline is now League Spartan 400 (was Lora), the quote mark is Lora italic 700 in Radiant Gold (was Georgia), the handle is @wbtcoaching (was @workbettertogether), and template thumbnails use the real watercolor and a WBT photo instead of CSS imitations.

### Social (`social.html`, replaces the Social Card Maker)
- The maker is retired (staff make cards with the WBT Brand skill in Claude); `/social-maker` redirects to `/social`. The page shows 21 single posts (services, testimonials, stats, resources, Insights), 5 case study carousels (cover → The Challenge → Our Approach → what shifted → client quote → key takeaway) with matching Stories, and a Story series for each of 6 free resources: 100 frames, all copy verbatim from the site. Mostly solid brand grounds with a few watercolor washes (tinted for contrast on dark), text never under 26px. Built from `social-src/`.
- Social posts and the logo share one move, *Come Together*.
- **Every case study** on the site (12) now has a carousel and a matching Story. Beats the page writes as prose use its opening sentences word for word; named quotes carry the person's name, role and round headshot (Eli Northrup, Courtney Curd). Six of the new seven covers use Cowbird's full-color originals; *Coaching to Support Leadership Development* keeps the website's duotone (no original found). *Moving From Stress to Strategy* shows only its cover and key takeaway, because its page body currently repeats *Individual Coaching for Each Team Member* word for word.
- **Animated Stories:** each Story is also an MP4 (`assets/Social/stories/`, built by `social-src/render_stories.py`) using *Come Together*: words gather line by line, bullets appear with their line, a hold to read, then a drift-out. They're the first tile in each Story row and play only while on screen.
- **Instagram grid:** posts, carousels and Stories sit three across with 3px gutters, like a profile grid. Carousels page one slide at a time (swipe, or hover for arrows; 1/n counter). Stories show only the animated version, with a play/pause button (one plays at a time).
- **Lighter Stories:** about 30 words a screen; a long beat runs over two frames, and a point or sentence too long for one screen is left out of the Story (it stays in the carousel). *Moving From Stress to Strategy* gains an Our Approach slide.
- **Type:** supporting lines are one size on every card (60px posts, 64px Stories) and never shrink; when text runs long, the picture gives way first (shorter photo, smaller collage). Stat supporting lines are 60px. No single-word orphans anywhere (last two words glued, `text-wrap: pretty`). Case-study cover photos are shorter so the line under the title can be bigger, and crops keep heads in (Co-leading anchored to the top).
- **Consistent pictures:** every case-study cover photo is one height (640px posts, 820px Stories) and every Story collage one scale, sized so no title shrinks. Story covers hold ~2.5s. Animated text keeps the still's exact line breaks, so motion never pushes text into the CTA or logo (all 106 Story frames checked).
- Corner spots drop out of any slide whose text would reach them; the Collaboration whiteboard photo is cropped clean on the top and right.

### No boxed text
- Text groups (voice attributes, values, principles, spec and length cards, usage notes) are open columns with a hairline instead of bordered boxes.

### Generic-UI cleanup
- Removed decorative 01/02 numbering (Logo and Swag section heads, Photos labels, the Elements menu, Motion and Microcopy principles), dashed boxes and dividers, and a faded label. Kept on purpose: Data Viz series order, checkerboards, clearspace guides, photo scrims, white behind client logos and products.

### Notes
- `CLAUDE.md` and `README.md` brought up to date: the repo is `work-better-together/wbt-brand-guide`, the site is the Netlify site `wbtbrand` (not GitHub Pages), branch previews, build-credit caveat, full page index, generated folders, `deck-assets/` described as the deck's own copies (not a mirror), and the `wbt-brand` Claude skill.

---

## 2026-07-10 — Reconcile with the live site, add the Patterns page, ship a copy/download system, and rebuild the homepage

A large session that (a) reconciled the guide against the production **workbettertogether.coach** build, (b) documented every pattern the site uses, (c) split the big layout patterns onto their own page, (d) added a consistent copy/download component across every asset page, and (e) simplified the homepage. Everything below pulled its exact values from the live site source, not from eyeballing.

### New: `patterns.html` (Layout Patterns)
- Split the larger, expressive layout patterns off the Components page into their own **Patterns** page, ordered: **Headline-over-image → Big Feature Heading → Decorative Bleed → Offset "2-of-3" staggered → Quote carousel → Editorial quotes → Card carousel → Accordion → Timeline → Data table**. Components is now just UI elements (button, form, card, tag, callout, nav, tabs, modal, tooltip, toast).
- Documented each with live demos pulled from the site / the `leadtowin` + `empower` case-study microsites: the **quote carousel** (gold quote mark + 56px avatar + name + mono role, Steady-Blue circular arrows, dots **between** the arrows), **editorial quotes** (gold inline mark; blue **asterisk-mark asset** pull quotes + key takeaway), **card carousel** (scroll-snap multi-format cards in alternating colorways, Eli Northrup + Courtney Curd headshots, soft shadow), **timeline** (Clean-Slate surface, gold "target" markers), **data table** (dark surface, Calm-Blue heads, gold band + notes), **headline-reversed-over-image**, **big feature heading**, **decorative bleed**, **accordion**.

### Copy / Download component (`actions.js`) — applied everywhere
- One shared component (identical button style + behavior) rolled out to every asset page:
  - **Colors** — "Copy hex" on each swatch (adapts to the swatch's own colorway).
  - **Clients** — Copy + Download on each logo's title bar; added the **Eli for NY** client logo (guide + deck-template, size-capped since the mark is near-square).
  - **Watercolor / scribbles / illustrations / photos** — hover Copy/Download overlays (downloads track the live color selection).
  - **Collages** — Save/Download.
  - **Logos** — a universal **inline-SVG → PNG renderer** (resolves the referenced `#wbt-wordmark`/`#wbt-monogram` symbol, resolves `currentColor` to the tile color so exports are the right color, not black) with Copy/Download on every wordmark & monogram colorway tile; plus **transparent-background SVG** downloads for the primary wordmark + monogram.

### Type-rule reconciliation (site-accurate)
- **Eyebrows** standardized to the site rule everywhere: League Spartan 500, **14px**, +0.16em, uppercase, Honest Ochre on light / Radiant Gold on dark. Section-labels bumped to 14px/0.16em sitewide; documented an Eyebrow row + a **Sans-serif Lede** row in the Type page/scale.
- **Newsletter** brought onto the rules: eyebrow → 14px Honest Ochre, headings → Grounded Black on light (were Steady Blue), remaining steady-blue type → ink, larger masthead.
- Converted the guide's **own copy to curly quotes** (it violated its own rule), fixed `--ink` from off-brand `#1a1a1a` → Grounded Black `#1F1E1E`, widened the page container to **1175px**.
- Motion page: added **live scroll-parallax demos** (decorative collage + in-frame) using the site's exact parallax math.
- Collages page: added a live **three-layer collage example** (Calm-Blue spot + scribble + armillary) under the three-layer-system section.

### Homepage + nav
- Reorganized both menus into **two groups — Design System and Tools** (was Guidelines/Tools/Design System). Order: Voice, Logo, Type, Color, Elements, Collages, Photos, **Patterns, Components, Iconography**, Swag, Clients, Motion, **Data Viz**, **Microcopy, Tokens**; Tools = Collage Maker, Deck Template, Newsletter, Social Maker. Updated the drawer (`GROUPS`), pager (`ORDER`), and homepage grid together.
- **Simplified the homepage menu** — removed the tile boxes; page links now float as plain League-Spartan text on the watercolor. **Black hairlines** under group labels; **Tools sits as an aligned 4th column** beside the 3-column Design System (`align-content:start` so its leading matches). Hero lede → 26px (capped at 480px so it clears the illustration); "Explore the Guide" → 14px.

### Docs
- Added the **`wbt-brand-designer`** skill — an expert that designs materials to these exact rules and defers to `wbt-collage` for collages. See `.claude/skills/wbt-brand-designer/`.

---

## 2026-07-09 — Self-hosted illustrations, secure save, unified Concept Image Library

A large rework across `elements.html`, `collage-maker.html`, and a new Cloudflare Worker. Summary of everything that changed:

### Security — removed exposed API tokens
- **Deleted two secrets that were embedded in the public pages** and viewable in source on brand.wbt.coach:
  - an **Airtable personal access token** (used to fetch the concept library live), and
  - a **write-scoped GitHub PAT** (used by the collage maker's "save to gallery" feature).
- Both tokens were **rotated/revoked**. No API tokens live in any page anymore.

### Collage save → Cloudflare Worker
- Added **`collage-save-worker/`** — a Cloudflare Worker that holds the GitHub token as a server-side secret and performs the commit on the page's behalf. The page POSTs the rendered collage to it.
- Deployed at **`wbt-collage-save.workbettertogether.workers.dev`**. Secrets (`GITHUB_TOKEN`, `SHARED_SECRET`) are set via `wrangler secret put` — never in source.
- Save UX is unchanged: build a collage → **Save** → enter the shared passphrase (once, stored in localStorage) → it commits the PNG + updates `assets/Generated Illustrations/manifest.json`. The gallery (`collages.html`) reads that manifest over a plain public URL.
- Deploy/rotate instructions: `collage-save-worker/README.md`.

### Concept illustrations now served locally (no Airtable)
- Both the elements page and the collage maker previously **fetched the concept library live from Airtable**. They now serve illustrations from **`assets/Illustrations/`**.
- Vendored the **63 concept illustrations** (previously Airtable-hosted) into the repo.

### `elements.html` — one unified "Concept Image Library"
- Merged the old **"Vintage Etched Illustration Set"** and **"Concept Library"** sections into a single **Concept Image Library**.
- Reorganized into **one A–Z index of concepts**, rendered from a single **`CONCEPTS`** array — etched + photographic illustrations and duplicate concepts merged into 30 base concepts.
- Added the three **service concepts** — **Leadership Coaching, Team Coaching, Facilitation + Training** — each showing the plain B&W cut-out used in its service collage (Full-Moon, Bees-Pair, Lightbulb-Glowing). Those three images appear **only** under their service concept (de-duplicated from their thematic homes).
- Removed **`Heart-Tablet-2.png`** — a corrupt export (top ~25% content, rest solid black); no clean copy existed anywhere.
- Removed the "Local / Served from repo" stat from the stats bar.
- **Result: 33 concepts, 102 unique illustrations.**

### `collage-maker.html` — picker synced to the full set
- Concept picker now offers the **same 102 illustrations** as the elements library.
- Added the 5 that were missing from its source lists: **`Armillary`** (→ Cosmos & Wonder) and the four layout accents **`Blue-Blob`, `Pink-Blob`, `Pink-Torn-Paper-1`, `Pink-Torn-Paper-2`** (→ new "Layout Accents & Textures" group).

### Workflow / docs
- Documented the **repo ↔ Drive** relationship and switched to a **repo-first workflow**: edit in `~/Projects/hkt-client-brand-guides/wbt-brand-guide`, deploy from it, then mirror to the Google Drive copy. See `CLAUDE.md`.

---

_Older history predates this changelog; see git log for the repo._
