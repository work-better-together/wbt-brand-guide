# WBT Brand Guide — Changelog

Notable changes to the brand guide site (brand.wbt.coach). Newest first.

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
- Documented the **repo ↔ Drive** relationship and switched to a **repo-first workflow**: edit in `~/Projects/wbt-brand-guide`, deploy from it, then mirror to the Google Drive copy. See `CLAUDE.md`.

---

_Older history predates this changelog; see git log for the repo._
