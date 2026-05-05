# WBT Design System — Handoff

**Status:** Foundation complete. Ready for Claude Design ingestion and engineering implementation.

**Generated:** 2026-05-05 overnight session.

---

## TL;DR

Built a token-driven design system on top of the existing WBT Brand Guide. Three deliverables matter most:

1. **`tokens/tokens.css`** — canonical CSS custom properties. Engineering imports this.
2. **`tokens/tokens.json`** — same content in W3C Design Tokens format. Tools like Claude Design / Style Dictionary / Tokens Studio ingest this.
3. **Five new brand-guide pages** documenting the system visually for designers and stakeholders.

---

## What was built

### Token files (the source of truth)

| File | Purpose |
|---|---|
| `tokens/tokens.css` | All tokens as CSS variables. Three tiers: primitives → semantic → component. 350+ tokens. Linkable from any page via `<link rel="stylesheet" href="tokens/tokens.css">`. |
| `tokens/tokens.json` | Same tokens in W3C Design Tokens Community Group format. Use this with Style Dictionary, Tokens Studio (Figma), or any DTCG-compliant pipeline. |

### New brand-guide pages

| Page | What it documents |
|---|---|
| `Tokens.html` | Visual reference for every token category — color (surface, ink, border, status), spacing, radius, type roles, motion (with live demos), elevation, layout, accessibility floor. |
| `Components.html` | Component library with full state coverage — Button (4 variants × 5 states), Input/Form fields, Card, Tag/Badge, Callout (4 variants), Modal, Tooltip, Toast (4 variants), Nav, Tabs. Each with token-mapping table. |
| `Motion.html` | Four principles, four duration tokens with live demos, four easing curves with SVG visualizations, six named animations (fade-in, rise-in, slide-in, scale-in, pulse, shimmer), hover behavior catalog, reduced-motion contract. |
| `Iconography.html` | Library recommendation (**Lucide**) + alternatives considered, stroke discipline, four-size scale, color usage rules, 24-icon starter set, accessibility rules, code reference. |
| `Data Viz.html` | 8-color categorical palette, 4-color subset, four single-hue sequential ramps, 11-stop divergent ramp, four sample charts, accessibility/colorblind notes. |
| `Microcopy.html` | Voice-in-UI principles, marketing-vs-UI voice comparison, length budgets, six core patterns (button label, field error, system error, empty state, modal confirmation, loading), reusable standard messages, vocabulary do/don't, tone shifts by moment. |

### Index + nav

- `Brand Guide Index.html` — added a **Design System** group between Guidelines and Tools. Five cards: Tokens, Components, Iconography, Data Viz, Microcopy.
- `nav.js` — added Motion (12), Tokens (14), Components (15), Iconography (16), Data Viz (17), Microcopy (18) to the page-pager so prev/next navigation flows through all of them.

---

## How to feed this into Claude Design

### Option A: ingest tokens.json directly

If Claude Design accepts W3C Design Tokens format, point it at:

```
work-better-together-brand-guide/project/tokens/tokens.json
```

The file uses standard `$value`, `$type`, and reference syntax (`{path.to.token}`). Should drop in cleanly.

### Option B: convert via Style Dictionary

If Claude Design wants a custom format (Tailwind config, Theme UI, MUI theme, etc.):

```bash
npm i -D style-dictionary
npx style-dictionary build --config sd.config.js
```

Use `tokens.json` as the source. Output any platform format Style Dictionary supports.

### Option C: copy CSS variables directly

For prototyping or framework-agnostic HTML:

```html
<link rel="stylesheet" href="tokens/tokens.css">
```

Then reference any `var(--surface-canvas)` etc. in component code.

---

## Token system architecture

```
PRIMITIVES   (raw values — the truth source)
    │
    └─→ SEMANTIC   (role-based — surface.canvas, ink.default, border.focus)
            │
            └─→ COMPONENT   (per-component overrides — btn.radius, input.padding)
```

**Rule:** components reference semantic tokens, never primitives. Primitives can change without breaking components if the semantic mapping is correct.

---

## Engineering quickstart

```css
/* Import once at the top of your global CSS */
@import url('tokens/tokens.css');

/* Then use in components */
.my-button {
  background: var(--btn-primary-bg);
  color: var(--btn-primary-ink);
  padding: var(--btn-padding-y) var(--btn-padding-x);
  border-radius: var(--btn-radius);
  transition: background var(--motion-state);
}

.my-button:hover { background: var(--btn-primary-bg-hover); }

.my-button:focus-visible {
  outline: var(--state-focus-ring-width) solid var(--state-focus-ring);
  outline-offset: var(--state-focus-ring-offset);
}
```

---

## Decisions made (you can reverse any of these)

1. **Color names are emotional, semantic names are role-based.** "Steady Blue" stays as the brand color name; component code uses `--surface-brand-primary` or `--ink-accent`. Two-layer naming protects both audiences.

2. **Default radius is 0.** The brand favors editorial precision over softness — sharp corners are the default; `radius.sm` (2px) is reserved for chrome (badges, tags, inputs); `radius.pill` only for filter pills. Reverse if you want a rounder feel system-wide.

3. **Default state is direct, hover is darker, pressed is darker still.** Standard pattern. The themed cards on the Brand Guide Index break this rule (they fully invert on hover) — that's a deliberate brand-expression moment, not a system rule.

4. **Inconsolata is locked to attributions and CTAs.** Buttons use Inconsolata 700 uppercase as the brand voice for actions. Eyebrows and labels stay in League Spartan.

5. **Body text is full ink, always.** No `--ink-muted` for body copy. Muted is reserved for meta, captions, and disabled state. This was a hard-fought rule from earlier brand-guide work — preserved.

6. **Lucide for icons.** Open-source, MIT, 1.5px stroke at 24px viewport, round caps/joins. Pairs with the editorial weight of Lora.

7. **Honest Ochre as the warning/critical color.** Slate-derived greens for success felt wrong — the brand has a warm palette; Ochre is the natural friction color. Slate is the affirm/info color.

8. **Motion ≤ 480ms for everything.** "Calm under pressure" extends to motion. No bouncy springs, no long expressive choreography. Short, direct, intentional.

9. **8-base spacing.** Picked because the existing brand pages use 4/8/16/24/32/40/56/72 — already an 8-base de facto system. Tokens codify what's already there.

10. **Focus ring is Intentional Blue.** The most action-coded color in the palette is the most natural focus indicator.

---

## Still pending (your decision after review)

These are *not* gaps in the foundation — the foundation is complete. These are the *next* layers:

| Layer | Notes |
|---|---|
| **Table component** | Listed in Components → "Not yet documented." Patterns: sortable header, sticky header, dense vs comfortable, zebra striping decisions. |
| **Pagination, Breadcrumb** | Standard patterns, low risk. |
| **Date picker, Slider** | Higher complexity — defer until a product needs them. |
| **Avatar** | Could leverage the portrait photography styling. |
| **Empty state component** | Pattern's documented in Microcopy; needs visual treatment using collage spots from Design Elements. |
| **Skeleton loader** | Animation is in Motion (`shimmer`); just needs the pattern wrapper. |
| **Style Dictionary config** | If you want generated platform exports (iOS, Android, React Native), this is the next deliverable. |
| **Figma library** | Mirror tokens into Tokens Studio for designer parity. Not a build I can do — needs Figma. |
| **Real Lucide install** | The Iconography page shows Lucide icons inline (SVG). Engineering still needs to `npm i lucide-react` and replace the inline SVGs in Components.html with library imports. |

---

## Verification

All pages were verified rendering correctly:

- ✅ Tokens.html — 14 sections, 24 swatches, tokens.css linked
- ✅ Components.html — 12 sections, 31 buttons, 10 input fields, no JS errors
- ✅ Motion.html — duration/easing demos animating, reduced-motion media query in place
- ✅ Iconography.html — 24-icon starter set rendering inline
- ✅ Data Viz.html — categorical, sequential, divergent palettes + 4 sample charts rendering
- ✅ Microcopy.html — pattern library + standard messages + tone shifts complete
- ✅ Brand Guide Index — Design System group renders with all 5 cards, all link targets return 200
- ✅ nav.js — page pager flows through all 18 pages

---

## Files created / modified

**New:**
```
project/Tokens.html
project/Components.html
project/Motion.html
project/Iconography.html
project/Data Viz.html
project/Microcopy.html
project/tokens/tokens.css
project/tokens/tokens.json
project/tokens/HANDOFF.md  ← this file
```

**Modified:**
```
project/Brand Guide Index.html  (added Design System group, Motion converted from coming-soon to active)
project/nav.js                  (added 6 entries to page-pager order)
```

---

## Contact for changes

This system is a foundation, not a finished product. The right way to evolve it: when a real component need surfaces, add the component, add any new tokens it requires, and update the relevant guide page. Avoid adding tokens speculatively — every token should justify its existence by a real consumer.

Look for:
- Components that re-derive values that should be tokens → promote
- Tokens that no component references → consider deprecating
- Tier-3 component tokens that always equal a tier-2 semantic → simplify by deleting the override

The design system is alive when it changes with the product. It's dead when nobody touches it.
