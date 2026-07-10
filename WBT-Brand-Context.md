# WBT Brand Context — Claude Design Ingestion Package

**Brand:** Work Better Together (WBT)
**Generated:** 2026-05-05
**Updated:** 2026-07-09 — reconciled against the production **workbettertogether.coach** build: added the `.lede-thin` deck role, the three-layer collage system, and the in-frame-parallax + hand-drawn-annotation motion patterns; clarified the headline-color rule; fixed internal color/weight inconsistencies.
**Use:** Paste this document into Claude Design as brand context before generating any components, pages, or layouts.

---

## Brand Overview

**Tagline:** Leadership is hard. Let's work on it.

**Value Proposition:** In the social impact space, transformation takes time. We coach leaders and their teams to build the mindset and capacity they need to get things done and create lasting change.

**Purpose:** Help leaders and organizations operate with greater ease, cohesion, and effectiveness — supporting them in their mission to drive social change.

**Promise:** We coach leaders to grow their capacity to lead, and we challenge teams to work better together.

**Audience:** Nonprofit leaders, social-sector organizations, team coaches, facilitators — people doing hard, high-stakes work.

---

## Brand Personality

> A trusted guide on a difficult stretch of terrain — nimble and confident, attuned to both the landscape and the people walking it. They blend head and heart. They listen first, name what others are circling around, and bring steadiness in moments of complexity or uncertainty.

**In one phrase:** Calm under pressure.

**Brand values:** Strategic · Supportive · Sincere · Confident · Approachable · Thorough · Trustworthy · Candid · Thoughtful · Agile · Curious · Connection-first

---

## Voice & Tone

**Voice:** Encouraging, steady, insightful, attuned. Confident without urgency.

| Attribute | Description |
|-----------|-------------|
| Strategic + Human | Speaks fluently about systems and power while always honoring lived experience |
| Guiding, not directing | Invites perspective-building — asks more than tells |
| Listens before naming | Connects first, then speaks; earns the right to name patterns |
| Anchored, not trendy | Engages complexity without trend-chasing or abstraction |

**Tone words:** Honest/Genuine · Grounded · Encouraging · Conversational · Good-Humored · Easygoing · Optimistic

**Write like this:**
- Full sentences. Short, clear, direct ones.
- Use "we" and "you" — this is a conversation, not a broadcast.
- Name what's actually happening, even when it's uncomfortable.
- Say the hard thing gently. Don't soften it into meaninglessness.

**Never write:**
- Corporate jargon: "leverage synergistic frameworks," "high-trust ecosystems"
- Urgency language: "Don't miss out," "Last chance," "Act now"
- Performative warmth: "We're SO excited to share…"
- Over-explained, multi-sentence what could be one

---

## Color System

### Palette

**Neutrals**

| Name | Hex | Emotion | Use |
|------|-----|---------|-----|
| Clear White | `#F9F8F2` | open, transparent, neutral | Primary page background; text on dark surfaces; slight warmth vs pure white keeps brand from feeling clinical |
| Grounded Black | `#1F1E1E` | solid, direct, stable | Body text, **headlines on light/cream backgrounds**, footers, high-contrast; use instead of pure black to maintain warmth; avoid as large background areas |

**Primary**

| Name | Hex | Emotion | Use |
|------|-----|---------|-----|
| Radiant Gold | `#CD9F36` | warm, insight, emphasis | Accent only — pull quotes, key stats, highlights, moments of insight; use sparingly; pairs strongly with all three blues |
| Intentional Blue | `#2531A5` | action, purpose, confidence | CTAs, buttons, interactive elements, focus rings; signals something is clickable |
| Steady Blue | `#061A49` | leadership, authority, safety | Primary brand color — hero/section **backgrounds** (surfaces), navigation, authoritative contexts, and **headlines reversed out on dark surfaces**. On light/cream backgrounds headlines are Grounded Black, *not* Steady Blue — see "Headline color" under Typography Rules. |

**Secondary**

| Name | Hex | Emotion | Use |
|------|-----|---------|-----|
| Calm Blue | `#ACCDD9` | listen, reflect, slow down | Reflective/editorial content — testimonials, coach bios, breathing room; text on dark at AAA |
| Clean Slate | `#1E4D5C` | foundation, nuance, trust | Section backgrounds, supporting panels, secondary containers |
| Honest Ochre | `#B55312` | tension, truth, vulnerability | Use with intention — moments of challenge, honesty, disruption; not a background at scale |

### Derived Colors

```
Slate Light:   #E0E8EB   (panels, callouts, annotation backgrounds)
Ochre Light:   #F5E8D8   (don't/warning blocks)
Success Light: #E8F0EB   (do/affirm panels)
Warning Light: #FDF0EA   (warn panels)
```

### Color Roles (Semantic)

```
Page background:        Clear White (#F9F8F2)
Body text:              Grounded Black (#1F1E1E) — always full ink, never muted
Muted/meta text:        #6B6B6B
Dividers/rules:         #E4E2DE
Card/panel background:  #FFFFFF
Primary brand surface:  Steady Blue (#061A49)
Action/interactive:     Intentional Blue (#2531A5)
Accent/emphasis:        Radiant Gold (#CD9F36)
Focus ring:             Intentional Blue (#2531A5), 2px solid
```

### Safe Color Combinations (WCAG)

| Text Color | Background | Large Text | Small Text |
|------------|-----------|------------|------------|
| Clear White | Steady Blue | AAA | AAA |
| Calm Blue | Steady Blue | AAA | AAA |
| Radiant Gold | Steady Blue | AAA | AA |
| Clear White | Clean Slate | AAA | AAA |
| Calm Blue | Clean Slate | AAA | AA |
| Clear White | Intentional Blue | AAA | AAA |
| Calm Blue | Intentional Blue | AAA | AA |
| Clear White | Grounded Black | AAA | AAA |
| Calm Blue | Grounded Black | AAA | AAA |
| Radiant Gold | Grounded Black | AAA | AA |
| Steady Blue | Calm Blue | AAA | AAA |
| Grounded Black | Calm Blue | AAA | AAA |
| Steady Blue | Radiant Gold | AAA | AA |
| Grounded Black | Radiant Gold | AAA | AA |
| Steady Blue | Clear White | AAA | AAA |
| Clean Slate | Clear White | AAA | AAA |
| Grounded Black | Clear White | AAA | AAA |

---

## Typography

### Font Stack

| Font | Role | Weights |
|------|------|---------|
| **League Spartan** | Display · Headlines · Labels · Decks | 400 Regular *(deck/subtitle role only — see below)*, 500 Medium, 700 Bold |
| **Lora** | Body · Editorial · Quotes | 400 Regular, 700 Bold, 400 Italic, 700 Italic |
| **Inconsolata** | Attributions · CTAs only | 500 Medium only (uppercase, tracked) |

### Type Scale

**Display & Headings (League Spartan)**

| Role | Size | Weight | Tracking | Leading | Use |
|------|------|--------|----------|---------|-----|
| Display | 80px | 700 | −0.03em | 0.95 | Hero text, covers |
| H1 | 56px | 700 | −0.025em | 1.0 | Page titles |
| H2 | 40px | 700 | −0.02em | 1.05 | Section headers |
| H3 | 28px | 700 | −0.01em | 1.1 | Sub-sections |
| H4 | 20px | 500 | 0 | 1.2 | Cards, panels |
| H5 | 16px | 500 | +0.01em | 1.3 | List titles, UI labels |
| Deck / Headline Support | `clamp(20px, 2.4vw, 26px)` | **400** | 0 | 1.42 | Subtitle/deck set directly under an H1/H2 — the `.lede-thin` role (sentence case, not uppercase) |

**Body (Lora)**

| Role | Size | Weight | Leading | Use |
|------|------|--------|---------|-----|
| Body Large | 19px | 400 | 1.75 | Intro paragraphs |
| Body | 16px | 400 | 1.75 | General body copy |
| Body Small | 14px | 400 | 1.65 | Footnotes, captions |
| Pull Quote | 22px | 400 Italic | 1.55 | Testimonials, callouts |

**Utility (Inconsolata)**

| Role | Size | Weight | Tracking | Case |
|------|------|--------|----------|------|
| Attribution / CTA | 11–14px | 500 | +0.18em | All caps |
| Caption | 12px | 400 | +0.04em | Title case |

### Typography Rules

- **Eyebrows/section labels:** League Spartan 500, uppercase, +0.18em — never Inconsolata
- **Supporting text / deck under a page headline:** League Spartan **Regular 400** at `clamp(20px, 2.4vw, 26px)`, line-height 1.42 — the `.lede-thin` **deck role** (sentence case). This is the *first* text block under an H1/H2. Serif Lora body copy (Body Large / Body) picks up *below* the deck, once the reader is past the headline zone. Rule of thumb: first block under a headline = League Spartan deck; further-down prose = Lora.
- **Headline color:** headlines on light/cream backgrounds are **Grounded Black** (`#1F1E1E`), not Steady Blue. Steady Blue headlines are only for text **reversed out on a dark/Steady-Blue surface** (e.g. a hero title over a photo or on a blue band). This keeps "one headline color per context" while honoring "body/headlines are full ink on light."
- **Lora italic:** reserved for quotes and callouts only — never general emphasis
- **Inconsolata:** stays small (10–14px), uppercase, never mixed-case prose
- **Buttons/CTAs:** Inconsolata 500 uppercase — this is the brand voice for actions
- **Body emphasis:** Lora 700 Bold (optionally + Intentional Blue color)
- **Weights:** League Spartan **500 / 700** for headlines & labels, plus **400 for the deck/subtitle role** only; Lora **400 / 700**. (Don't introduce other weights.)
- **Tight tracking at large sizes:** −0.02em to −0.03em for headlines
- **Positive tracking for small labels:** +0.14em to +0.18em at eyebrow/attribution sizes
- **Curly quotes only:** always use typographic quotes and apostrophes (`'` `'` `"` `"`), never straight ASCII (`'` `"`), in any reader-facing copy — prose, headlines, page titles, meta descriptions, and image alt text. (Straight quotes are correct *only* inside code/markup, never in copy.)
- **No single-word orphans:** the last line of a paragraph or list item should never be a single stranded word — glue the final two words with a non-breaking space so they wrap together.

### Text Markings & Emphasis

The brand marks up key words in running text with hand-drawn "ink" — a small, cohesive set of emphasis treatments used *instead of* a plain browser underline. Two families:

**Hand-drawn annotations** — animated, draw in on scroll (see *Motion → Scroll-linked patterns*):
- **Circle** — an open hand-drawn circle around a phrase. Intentional Blue, **double stroke**. Stays on one line.
- **Underline** — a wobbly hand-drawn underline. Intentional Blue, **single stroke**. May wrap across lines.

**SVG underlines** — static, a small stroke repeated under the phrase:
- **Wave** (`.u-wave`) — a smooth sine-wave underline. Intentional Blue (`#2531A5`), ~1.5px stroke.
- **Zigzag** (`.u-zigzag`) — a sharp zigzag underline. Intentional Blue (`#2531A5`), ~1.6px stroke, round joins.
- **Gold scratch** (`.u-wave-gold`) — a doubled, jagged hand-scratched underline in Radiant Gold (`#CD9F36`) — the "insight / highlight" mark.

Rules: use **sparingly** — one or two marks per passage, never every phrase. Blue is the default; **gold is reserved for insight/emphasis** (matching Radiant Gold's accent-only role). These marks are the "handwritten highlight" moment — they replace bold/italic for that gesture, not for structural emphasis.

---

## Logo & Mark

**Wordmark:** Full horizontal logo — primary use. Available in black (on light), white (on dark).

**Monogram:** WBT initials in a rounded outline — use when the wordmark is too wide (avatar, favicon, small stamps). The rounded outline is intended to suggest a mirror, because this work is about self-reflection.

**Size reference:**
- 2xs: 22px height (tight spaces)
- xs: 32px height
- sm: 48px height
- md: 72px height
- lg: 110px height
- xl: 180px height (hero/cover use)

**Logo rules:**
- Always clear space = minimum 1× the mark height on all sides
- Only approved file: flat SVG (no drop shadows, no outlines, no color modifications)
- Never place on a busy or low-contrast background
- Two colorways only: black on light, white on dark

---

## Spacing & Layout

**Base unit:** 8px

**Spacing scale:** 0 · 4 · 8 · 12 · 16 · 24 · 32 · 40 · 56 · 72 · 96

**Layout:**
- Max content width: 960px
- Page padding: 40px horizontal, 64px top
- Grid gap between sections: 2px (creates the "mosaic" editorial look)
- Card/panel internal padding: 20–40px depending on size

**Grid gap note:** The 2px gap between adjacent cards is a deliberate design choice — it creates a dense, editorial mosaic rather than floating cards.

**Offset / staggered "2-of-3" layout (a signature pattern).** Rather than a centered single column, content blocks are capped at ~two-thirds width and alternately hugged **left** then **right**, with the right-hand block dropped down (~60px) so the two stagger diagonally instead of stacking flush. Classes: `.offset-left` (`max-width: 66%`, hugs left) and `.offset-right` (`max-width: 66%`, hugs right, `margin-top: ~60px`). On mobile both go **full-width and stack** (offsets reset to 0, the drop shrinks to ~32px). Use it for intro-statement + supporting-list pairings — e.g. "what we work on" / "who we work with" sections — where a single centered column would feel static.

---

## Borders, Radius & Elevation

**Radius:**
- Default: 0 (sharp corners — editorial precision over softness)
- Badges/tags/inputs: 2px
- Buttons: 10px
- Pills/filter chips: 9999px (full pill)
- Palette strip: 4px 4px 0 0 (top corners only)

**Border widths:**
- Default divider/rule: 1px
- Card/panel borders: 1px solid `#E4E2DE`
- Emphasis border: 2px
- Left-border callouts: 3px

**Elevation (box shadows):**
- Low: `0 1px 3px rgba(31,30,30,0.06), 0 1px 2px rgba(31,30,30,0.04)`
- Medium: `0 4px 6px rgba(31,30,30,0.07), 0 2px 4px rgba(31,30,30,0.05)`
- High: `0 10px 15px rgba(31,30,30,0.08), 0 4px 6px rgba(31,30,30,0.05)`
- Overlay: `0 20px 25px rgba(31,30,30,0.10), 0 10px 10px rgba(31,30,30,0.06)`

---

## Components (Reference)

### Buttons

| Variant | Background | Text | Hover |
|---------|------------|------|-------|
| Primary | Intentional Blue (#2531A5) | Clear White | Darken 10% |
| Secondary | Transparent | Intentional Blue | Intentional Blue 10% fill |
| Ghost | Transparent | Grounded Black | Grounded Black 5% fill |
| Destructive | Honest Ochre (#B55312) | Clear White | Darken 10% |

Button font: Inconsolata 500, uppercase, +0.12em tracking, 14px
Button padding: 12px top/bottom, 24px sides (default)
Button radius: 10px

### Form Inputs

- Default border: 1px solid `#E4E2DE`
- Hover border: `#1F1E1E` (Grounded Black)
- Focus border: 2px solid `#2531A5` (Intentional Blue) — shadow `0 0 0 3px rgba(37,49,165,0.2)`
- Error border: `#B55312` (Honest Ochre)
- Disabled: 50% opacity
- Helper text: Lora 14px italic, `#6B6B6B`

### Cards

- Background: `#FFFFFF`
- Border: 1px solid `#E4E2DE`
- Hover: scale(1.01), shadow elevation-medium
- Selected: Intentional Blue 2px border, Intentional Blue 10% bg tint

### Accordion (Disclosure)

Native `<details>/<summary>` — **no custom JS**, inherently keyboard- and screen-reader-accessible. This is the standard for any expandable/disclosure UI (FAQ, expandable case-study details). Keep this pattern rather than building a custom toggle.

- **Item divider:** 1px rule (`--border-default`) between items — no card/box around each.
- **Question (summary):** League Spartan **700**, `clamp(18–22px)`, line-height 1.25; ~24px vertical padding; cursor pointer; the browser's default disclosure triangle is hidden.
- **Marker:** a League Spartan **`+`** in Intentional Blue at the top-right, which becomes **`–`** when open (240ms transition). Never a chevron or emoji.
- **Answer:** Lora **17px** / 1.75, max-width ~68ch, indented to clear the marker.

### Quote Carousel (Testimonials)

Shows **one testimonial at a time**, advanced with circular prev/next arrows and a row of dots. Use it wherever multiple voices would otherwise stack into a wall of quotes (homepage testimonials) — the single-slide focus keeps each voice weighty, and the controls read as hand-placed rather than utilitarian.

- **Quote:** Lora *italic*, `clamp(19–25px)` / 1.5.
- **Attribution:** League Spartan **500**, 13px, uppercase, +0.08em, Steady Blue (`#061A49`).
- **Arrow:** 48px circle, 1.5px `--border-default` border, card background, Steady Blue glyph (`‹` / `›`); on hover the circle **fills Steady Blue** and the glyph goes white.
- **Dots:** 8px circles; inactive Grounded Black 22%; active **Intentional Blue**, scaled 1.3×. Dots are clickable and jump to that slide.
- **Track:** slides are `flex: 0 0 100%`; advancing animates `transform: translateX()` over **420ms** ease.

### Callouts/Annotations

- Left border: 3px solid `--border-color`
- Background: light tint of border color
- Eyebrow: League Spartan 500, 10px, uppercase, +0.18em
- Body: Lora italic, 13px
- Info: Intentional Blue border/tint
- Success: Clean Slate border, Success Light bg
- Warning: Honest Ochre border, Warning Light bg
- Critical: Honest Ochre border, Warning Light bg

### Tags/Badges

- Neutral: Grounded Black 8% bg, Grounded Black text
- Info: Intentional Blue 10% bg, Intentional Blue text
- Success: Clean Slate 15% bg, Clean Slate text
- Warning: Honest Ochre 15% bg, Honest Ochre text
- Radius: 2px
- Font: League Spartan 500, 10px, uppercase

---

## Motion

**Principle:** Calm under pressure. Everything ≤ 480ms. No bouncy springs, no long choreography.

| Token | Duration | Use |
|-------|----------|-----|
| Instant | 80ms | Micro-interactions (switch toggle, checkbox) |
| Fast | 150ms | State changes (hover, focus, active) |
| Base | 240ms | Component transitions (appear, expand) |
| Slow | 400ms | Page transitions, modals, overlays |

**Easing:**
- State: `cubic-bezier(0.2, 0, 0, 1)` — default for hover/focus
- Enter: `cubic-bezier(0, 0, 0.2, 1)` — things appearing
- Exit: `cubic-bezier(0.4, 0, 1, 1)` — things leaving
- Emphasis: `cubic-bezier(0.4, 0, 0.2, 1)` — emphasis moments

### Scroll-linked motion patterns

**In-frame parallax (photos).** Any prominent photo (hero images, headshots, feature photos) can drift subtly *within its own frame* on scroll, so it feels alive without page-jump. Recipe: a fixed-aspect-ratio container with `overflow: hidden`; the `<img>` sized at **108–110%** with `object-fit: cover`, a slight negative inset, and **`max-width: none`** (a global `img { max-width: 100% }` reset will otherwise silently cancel the oversize and reintroduce edge gaps); plus a small `data-parallax` value (**0.08–0.14**). The image shifts a few pixels within its frame — enough to feel considered, never enough to reveal an edge. Decorative parallax is desktop-only by default (≥ 820px); bio-page collages are the deliberate exception (they keep their absolute layout at every width).

**Hand-drawn annotations.** Key phrases can be marked with sketch-style ink in **Intentional Blue** that draws in on scroll — an open **circle** around a phrase, or a wobbly **underline**. Rules:
- **Underline = single stroke** (one pass); **circle = double stroke** (two passes). Don't match them — a doubled underline reads as busy.
- Underlines **may wrap** across multiple lines (each visual line gets its own segment); circles stay on **one line** (a circle around wrapped text looks broken).
- Marks **animate once on first appearance, then persist** — they must not re-animate on scroll or on address-bar-driven mobile resize events.
- A stable random seed keeps the wobble consistent across reloads.

**Reduced motion:** All animations — including in-frame parallax and hand-drawn annotations — must be disabled or reduced under `prefers-reduced-motion: reduce`.

---

## Photography

**Style:** Authentic, portrait-focused, documentary. Captures real connection — not staged poses.

**Tone:** Warm, honest, present. People in genuine moments of thinking, listening, or conversing.

**Never use:** Stock-photo energy. Forced smiles. "Conference room" clichés. Diverse-but-obviously-posed group shots.

**Color treatment:** Natural, slightly warm. Avoid cold/desaturated looks. Images may use Calm Blue or Clean Slate tones in backgrounds naturally.

---

## Design Elements

**Watercolor spots & textures:** Torn/rough-edged single-color watercolor blobs ("spots") from the brand texture library, plus soft textures used as low-opacity (15–25%) background washes. Spots come in four named color families — **Calm Blue, Clean Slate, Honest Ochre, Radiant Gold** — each with ~9 numbered shape variants. Reuse the *same* numbered shape across a page for visual rhyme, or vary for texture.

**Collage system (three-layer) — the signature decorative motif.** Used on hero sections, service pages, bio pages, and card icons. Always **three layers, in this fixed stacking order**:
1. **Watercolor spot** (bottom) — a single-color blob; sets the color mood.
2. **Scribble** (middle) — a thin black hand-drawn loop/line weaving through or behind the focal element; adds motion and a sketched quality.
3. **Illustration or photo** (top) — the focal point (planet, cairn, telephone, compass, armillary sphere, etc., or a photo).

Everything overlaps and sits slightly off-center — a hand-placed, considered composition, not a symmetric grid. This is the brand's "mosaic of people and perspectives" quality made literal. (Production note: watercolor spots are *not* binary alpha masks — crop them to their content box using a **low** alpha threshold, ~10–30, or you'll silently clip half the organic edge; scale spots from their center, never a corner.)

**Bio-page "scrapbook" collage:** a hand-placed, tilted, overlapping photo collage (4 photos at varied sizes/rotations) layered with a colored spot + scribble bleeding from a corner. Give each subject a *different* named spot color to differentiate otherwise-identical layouts.

**Decorative bleed (spots & scribbles cropped off the page edges).** Beyond focal collages, large watercolor spots and looping scribbles are placed to **crop off the edges of a section** — a colored blob peeking in from one side, a scribble tail escaping the other — to add hand-made warmth and depth without competing with the content. Recipe: the section is `position: relative` with `overflow: hidden` (or `overflow-x: clip`); each deco is a `position: absolute`, `z-index: 0`, `pointer-events: none` image pushed off-frame with **negative offsets**; spots run 360–640px at opacity 0.55–0.92, scribbles 520–1128px, rotated or `scaleX(-1)` for a natural gesture. Content always sits above at `position: relative; z-index: 1`. Match the spot's colorway to the page. On mobile, **shrink the spot and drop the scribble** — a deco must never force horizontal scroll.

**Editorial grid:** 2px gaps between adjacent panels create a newspaper/magazine feel — intentional density, not whitespace-heavy SaaS.

**Shapes:** No decorative shapes, icons as background elements, or ornaments. Precision over decoration.

---

## Data Visualization

**Categorical palette (in order of perceptual distinction):**
1. Steady Blue `#061A49`
2. Radiant Gold `#CD9F36`
3. Clean Slate `#1E4D5C`
4. Honest Ochre `#B55312`
5. Intentional Blue `#2531A5`
6. Calm Blue `#ACCDD9`
7. Mid-neutral `#8C8C8C`
8. Grounded Black `#1F1E1E`

**4-series subset:** Steady Blue · Radiant Gold · Clean Slate · Honest Ochre

**Chart typography:** League Spartan 500 for axis labels and legend; Lora italic for chart callouts; Inconsolata for data values.

**Accessibility:** Never rely on color alone — always pair with pattern, shape, or label.

---

## Accessibility Floor

- Body text contrast: 4.5:1 minimum
- Large text contrast: 3:1 minimum
- Touch targets: 44px × 44px minimum
- Focus ring: 2px solid Intentional Blue (#2531A5), 2px offset, 3px shadow
- All interactive elements keyboard navigable
- All animations disabled under `prefers-reduced-motion: reduce`
- All non-decorative icons require aria-label

---

## CSS Design Tokens (Key Variables)

These variables are available via `tokens/tokens.css` — import this file to reference them directly.

```css
/* Colors */
--surface-canvas:         #F9F8F2  /* page bg — Clear White */
--surface-card:           #FFFFFF  /* card bg */
--surface-brand-primary:  #061A49  /* Steady Blue panels */
--surface-brand-secondary:#1E4D5C  /* Clean Slate panels */
--ink-default:            #1F1E1E  /* body text — Grounded Black, always full ink */
--ink-muted:              #6B6B6B  /* meta, captions, disabled */
--ink-on-brand:           #F9F8F2  /* text on dark brand surfaces */
--border-default:         #E4E2DE  /* dividers, card edges */
--border-focus:           #2531A5  /* focus rings */
--state-focus-ring:       rgba(37,49,165,0.3)

/* Spacing */
--space-1: 4px   --space-2: 8px   --space-3: 12px  --space-4: 16px
--space-6: 24px  --space-8: 32px  --space-10: 40px --space-14: 56px
--space-18: 72px --space-24: 96px

/* Typography */
--font-display: 'League Spartan', sans-serif
--font-body:    'Lora', serif
--font-mono:    'Inconsolata', monospace

/* Motion */
--motion-instant: 80ms    --motion-fast: 150ms
--motion-base:    240ms   --motion-slow:  400ms
--ease-state:   cubic-bezier(0.2, 0, 0, 1)
--ease-enter:   cubic-bezier(0, 0, 0.2, 1)
--ease-exit:    cubic-bezier(0.4, 0, 1, 1)
```

---

## Key Brand Decisions (Non-Obvious)

1. **Default radius is 0.** Sharp corners are intentional — editorial precision over softness. Only deviate for chrome elements (badges, inputs: 2px) and buttons (10px).

2. **Body text is always full ink.** `--ink-muted` (#6B6B6B) is only for meta, captions, and disabled states. Never muted body copy.

3. **Inconsolata locked to attributions and CTAs.** Buttons use Inconsolata **500** uppercase — that's the brand voice for actions. Eyebrows and labels use League Spartan 500, not mono. *(Inconsolata is 500-weight only; buttons are 500, +0.12em, 14px.)*

4. **Supporting text under a page headline uses League Spartan — the `.lede-thin` deck role** (Regular **400**, `clamp(20px, 2.4vw, 26px)`, line-height 1.42), *not* Lora. Lora body copy picks up at the next level, below the deck.

5. **Honest Ochre is the warning/tension color.** The brand runs warm — Ochre is the natural friction color. Clean Slate–derived colors are the affirm/info color.

6. **2px gap between panels is deliberate.** Don't increase it. The dense mosaic feel is intentional.

7. **Italic = quoting, not emphasis.** In Lora, italic means you're quoting or paraphrasing, not emphasizing. Use bold for emphasis.

8. **Radiant Gold is accent-only.** Never use as a large background. Use sparingly for highlights.

9. **Motion ≤ 480ms everywhere.** The brand is "calm under pressure" — this extends to animation. No bouncy springs, no long expressive choreography.

10. **Lucide icon library.** 1.5px stroke weight, round caps/joins, `currentColor`, 24px default viewport. Sizes: 16/20/24/32px.

11. **Headlines on light backgrounds are Grounded Black, not Steady Blue.** Steady Blue is a *surface/background* color and the color for headlines **reversed out on dark surfaces** — reach for black on cream/white, not blue. (An easy thing to get wrong: "Steady Blue is the primary brand color" does *not* mean blue headline text on light pages.)

12. **The collage motif is always three layers, in order: watercolor spot → scribble → illustration/photo.** Single named spot color per collage (Calm Blue / Clean Slate / Honest Ochre / Radiant Gold); overlap everything, keep it slightly off-center. See *Design Elements → Collage system*.

13. **Curly quotes always; single-word orphans never.** Typographic `'` `"` in all copy (never straight ASCII), and glue the last two words of any paragraph so a lone word never wraps to its own line. See *Typography Rules*.
