---
task: logo color tiles square downloadable social profile pictures
slug: 20260505-120000_logo-color-tiles-social-download
effort: standard
phase: complete
progress: 8/8
mode: interactive
started: 2026-05-05T12:00:00Z
updated: 2026-05-05T12:00:00Z
---

## Context

Section 03 of logo.html shows 9 monogram color variant tiles in a 3×3 grid. Each tile currently has a color name label (v-label, top-left) and a color pairing spec (v-spec, bottom-right). The user wants: annotations removed, tiles made square and tighter-cropped around the monogram, and each tile downloadable as a PNG for use as a social profile picture.

Only section 03 monogram grid is affected. Section 02 wordmark variants are untouched.

### Risks
- SVG-to-PNG download requires JS canvas approach — must handle SVG serialization correctly
- Tiles need clear-white border on the cream variant to stay visible
- Download filenames should be descriptive (color name)

## Criteria

- [x] ISC-1: v-label spans removed from all 9 monogram variant divs in section 03
- [x] ISC-2: v-spec spans removed from all 9 monogram variant divs in section 03
- [x] ISC-3: Monogram variant grid tiles have 1:1 aspect-ratio (square)
- [x] ISC-4: Monogram variant padding reduced — monogram fills ~60% of tile width
- [x] ISC-5: Each tile has a visible download button (hover overlay, bottom-right)
- [x] ISC-6: Clicking download triggers PNG export at 800×800 pixels
- [x] ISC-7: Downloaded file named descriptively (e.g. wbt-monogram-steady-blue.png)
- [x] ISC-8: Section 02 wordmark variant grid is unchanged

## Decisions

## Verification
