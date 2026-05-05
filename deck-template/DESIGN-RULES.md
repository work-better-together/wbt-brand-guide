# WBT Design Rules

Distilled from the design decisions made while building the deck templates, brand guide pages, and Collage Builder. These are not generic best practices — every rule traces to a specific decision, correction, or constraint we hit. Drop relevant sections into the brand guide; pass the whole file to AI when generating new templates.

---

## Typography

**Inconsolata is for attributions and CTAs. Nothing else.**
**Why:** When used for eyebrows, section numbers, or labels, it read as "tech/code" against editorial display type. Reserving it for two specific roles preserves its meaning. Eyebrows specifically moved to League Spartan.
**Rule:** Inconsolata is for: (1) quote attributions like `— MAYA CARRINGTON, EXECUTIVE DIRECTOR, CENTER FOR REPRODUCTIVE EQUITY` (uppercase, tracked, smaller-than-body), and (2) CTAs / button labels (uppercase, tracked). It is NOT for eyebrows, section labels, page metadata, or any other UI chrome.

**Eyebrows are League Spartan 500, not Inconsolata.**
**Why:** This is the specific correction to the Inconsolata-pullback that earlier versions of these rules got wrong. Eyebrows belong with the display-type system, not the mono accent system.
**Rule:** Every eyebrow class — `.page-header .label`, `.section-label`, `.demo-eyebrow`, `.pairing-label`, `.font-role`, `.rule-tag`, page metadata, agenda eyebrows — uses League Spartan 500, uppercase, with positive tracking.

**League Spartan 500 is the default label weight.**
**Why:** 500 reads as confident structure without competing with 700 titles. Anything lighter (300, 400) felt thin against the watercolor textures.
**Rule:** Eyebrows, category labels, section numbers, agenda times, page headers, bio eyebrows → League Spartan, weight 500.

**League Spartan 700 is reserved for titles.**
**Why:** Two-weight hierarchy (500 label / 700 title) carries the whole system. Adding a third weight muddied it.
**Rule:** Display titles use 700. Don't introduce 600, 800, or 900 weights.

**Lora is primarily roman. Italics are reserved.**
**Why:** Italics carry meaning in this system — quotation, paraphrasing, special callout, annotation. Used for general emphasis, italics dilute and stop reading as "this is special." Roman Lora is the default body voice.
**Rule:** Body copy is Lora roman (not italic). Use Lora italic only for: (1) the quote text itself (e.g. the slide-11 purpose statement), (2) paraphrasing or restating someone else's framing, (3) deliberate special callouts, (4) annotations — small explanatory notes attached to an example or specimen (e.g. weight-grid notes, specimen captions, element callouts). Never as general emphasis on a word inside a normal sentence.

**Body emphasis is bold, optionally with a hand-drawn annotation.**
**Why:** With italic reserved for quotation/paraphrasing/callout, the body needs a different vocabulary for "this phrase matters." That vocabulary is Lora bold (700) — sometimes alone, sometimes amplified by a hand-drawn intentional-blue scribble (an ellipse around the phrase, or an underline beneath it). The hand-drawn mark is the brand's signature emphasis device and reads as deliberate human attention, not auto-formatting.
**Rule:** To emphasize a phrase in body prose, use Lora **bold** (weight 700, same family as surrounding text — do not switch to League Spartan). For *additional* weight, layer a hand-drawn intentional-blue annotation: an ellipse around the bolded phrase (key concept), or an underline beneath it (definite specificity). Do NOT use italic for general-emphasis. Do NOT use color shifts for general emphasis. The two emphasis tools are bold and scribble — used together when the phrase truly carries weight.

**Button CTA: filled Intentional Blue, white Inconsolata.**
**Why:** Buttons need to read as interactive at a glance. Solid Intentional Blue with white uppercase tracked text is the unmistakable "primary action" signal — distinct from body, distinct from links.
**Rule:** Primary CTAs are a solid Intentional Blue (`#2531A5`) rounded rectangle (radius ~10px), white text, Inconsolata uppercase, font-size ~14px, letter-spacing ~0.18em, generous padding (e.g. 18px 36px). Example label: `LET'S GET TO WORK`. Hover may darken slightly; the text/face never inverts to a different color system.

**Text CTA: Inconsolata uppercase, underlined, hover shifts to Intentional Blue.**
**Why:** Text CTAs are the lower-emphasis sibling of the filled button — used inline in copy or as a secondary action. Black-on-page reads as confident; the Intentional-Blue hover state signals interactivity without claiming primary attention.
**Rule:** Text CTAs are Inconsolata uppercase, Grounded Black, letter-spacing ~0.2em, with a thin underline (1px). On hover, color shifts to Intentional Blue (`#2531A5`); underline stays. Example label: `LEARN MORE`.

**Inline links: Lora bold, Intentional Blue, underlined.**
**Why:** Inline links live inside body prose. They need to be visibly interactive without breaking the body's reading rhythm — bold + Intentional Blue + underline is the unambiguous link signal that pairs cleanly with Lora roman.
**Rule:** Links inside Lora body copy use weight 700 bold, color Intentional Blue (`#2531A5`), with underline. Example: "Take our **Leadership Reflection Survey** to determine if coaching is right." This is the *one* place body text breaks the "no color shift" rule — and only because color is functioning as a state/role signal, not decorative emphasis.

**Color shifts ARE allowed on interactive elements.**
**Why:** This is the explicit exception that makes the "no color shift on body text" rule consistent. Links and CTAs are not body text — they are interactive surfaces. Color is signaling role (clickable) or state (hover), not styling words for emphasis.
**Rule:** Color shifts are allowed for: link colors, hover/active/focus states, button fills, and form-element states. Color shifts are NOT allowed for: emphasizing words inside prose, fading body text, or differentiating sentences within a paragraph.

**Big stats: massive Intentional-Blue numeral, Lora qualifier with bolded subject.**
**Why:** Stats are punch lines. The number does the heavy lifting visually; a short Lora roman qualifier underneath provides the meaning. Bolding the grammatical subject (the first 2–3 words: `of people`, `of leaders`, `of teams`) anchors the reader before the qualifier explains what was measured.
**Rule:** Stat figure is League Spartan 700, very large (e.g. 200–280px on slide, 120px+ in body), color Intentional Blue (`#2531A5`). The qualifier line is Lora roman, 18–22px, full ink, on a separate line below. Bold the first short noun phrase (`of people`, `of leaders`) and leave the rest roman. Example:
> **80%**
> **of people** who receive coaching report increased self-confidence.

**Always use curly quotes. Never straight quotes.**
**Why:** Straight quotes (`"..."`, `'...'`) are typewriter holdovers — they read as low-quality typesetting. Curly quotes (`"..."`, `'...'`) are part of the brand's editorial polish.
**Rule:** Use `"` `"` for double, `'` `'` for single, and `'` for the apostrophe in contractions. Never `"` or `'`. This applies to slides, brand-guide pages, web pages, copy decks — everywhere.

**The opening quote mark hangs outside the text block.**
**Why:** When a quote opens a justified or left-aligned block, the opening `"` mark sits flush with the text edge by default — but visually that creates a ragged-looking left edge because the quote mark is small. Hanging the opening mark outside the column makes the first letter of the first word align with the rest of the text block. It's a small detail with big impact on perceived editorial quality.
**Rule:** Any block-level quote (`.quote-text`, pull quotes, large display quotes) uses CSS `hanging-punctuation: first` plus a negative `text-indent` (~`-0.44em`) so the opening curly quote hangs into the left margin. The first letter of the first word aligns with the body's left edge.

**No color shift + italic on the same span.**
**Why:** Combining italic and color on a word inside prose creates two simultaneous "this is special" signals that fight each other and read as design noise. Pick one treatment, not both.
**Rule:** If a word/phrase needs emphasis, choose italic OR color, never both. The "_intentionally_" pattern (italic + green) is wrong.

**Supporting text under main headlines is sans serif.**
**Why:** When a page-level headline is followed by a lead/supporting paragraph, switching to Lora creates an unnecessary serif/sans context shift. The lead should feel like a continuation of the headline's voice.
**Rule:** The first paragraph immediately under a page-level headline (e.g. `.page-header p`, hero subtitle) is League Spartan in a body weight (400–500), roman, full ink. Lora picks up at the next level of body content.

**Text is full-strength ink. No greys, no opacity fades.**
**Why:** Greyed body text and opacity fades read as "this is less important" — but if it's on the page, it's important. Hierarchy comes from size, weight, and tracking, not from washing out text.
**Rule:** Body and supporting text use full ink color (e.g. `--ink: #1a1a1a` or near-black). Do not use `--ink-muted` for content. Do not use `opacity: 0.x` to fade text. The smallest functional UI labels (e.g. spec-label at 9px) are the only allowable exception.

**Section divider numbers and titles are restrained.**
**Why:** Originally `divider-title` was 188px and `divider-num` was 42px — they competed with the cover. Scaling down let the dividers feel like a beat, not a peak.
**Rule:** `.divider-title` = 104px, `.divider-num` = 22px (matches cover eyebrow scale). Divider-num weight: 500.

---

## Color

**Brand-only palette. Eight colors plus transparent. No custom hex.**
**Why:** The whole system relies on the named colors carrying their attribute meanings. Any custom hex breaks that semantic layer.
**Rule:** Pickers expose only: Clean Slate, Calm Blue, Radiant Gold, Honest Ochre, Steady Blue, Intentional Blue, Clear White, Grounded Black + Transparent. No hex inputs, no eyedropper.

**Every color carries an attribute.**
**Why:** Color isn't decorative — it's the brand's vocabulary for emotional/strategic states.
**Rule:** Surface the attribute alongside the color in any tool/picker (tooltip is fine). Examples: Calm Blue → reflection · Honest Ochre → vulnerability · Radiant Gold → insight/warmth · Clean Slate → foundation · Steady Blue → default ground · Intentional Blue → resolve.

**Concept → background color is curated, not arbitrary.**
**Why:** Random pairings produced "off" combinations. The mapping makes the tool feel like the studio is in the room.
**Rule:** Use these defaults; deviate only with reason.
- Perception & Bias → Calm Blue
- Emotional Intelligence → Honest Ochre
- Time & Pacing → Clean Slate
- Growth & Development → Radiant Gold
- Renewal & Resilience → Calm Blue
- Light, Energy & Spotlight → Radiant Gold
- (Other / Airtable concepts) → Steady Blue fallback

**Default spot color is Grounded Black.**
**Why:** Black silhouette reads as "the spot" before color is applied. Reading the shape first is what lets us mix-and-match shape × color.
**Rule:** New spot picks render in Grounded Black. Color is a separate, deliberate choice.

**User color choice is sticky.**
**Why:** Users got frustrated when picking a concept overwrote a background they had just chosen.
**Rule:** Once the user manually picks a background, concept switches must NOT overwrite it. Track this as `userPickedBg` flag.

---

## Watercolor Spots

**Curated 9-spot library, not the full upload set.**
**Why:** The full library had visual duplicates (e.g., spot-gold-1 ≈ spot-calm-blue-1 in shape; orange-stacked ≈ calm-blue-2). Showing all of them made the tool feel like a folder, not a kit.
**Rule:** Spot picker shows 9 visually-unique shapes in a 3×3 grid. Skip perceptual duplicates. Skip boxed-background spots (e.g., gold-on-black) — they're for different uses.

**Spot recoloring preserves alpha edge feathering.**
**Why:** A flat-fill recolor kills the watercolor character — it stops being a watercolor.
**Rule:** Recoloring blends color over the alpha channel of the source PNG. Verify partial-alpha pixels survive (visible feathering at edges). Don't replace with solid SVG silhouettes.

**Spot bleeds off the edge — it doesn't sit in a frame.**
**Why:** The bio slide originally cropped a steady-blue spot inside a 420×340 box at 180% — heavy, square crop, looked stuck. Letting it bleed makes it feel painted onto the page.
**Rule:** When a spot anchors a slide (bio, cover, purpose statement), size it so it bleeds off at least one edge. Reference: bio-spot 760px, calm-blue-1, top-left bleed; quote-spot 560px granular-gold, rotated 160°, top-left bleed.

**Rotation is allowed on deck slides; it's NOT a Collage Builder feature.**
**Why:** Slides are art-directed one-offs where rotation can be tuned. The Collage Builder v1 deliberately omitted rotation to keep the user-facing tool simple.
**Rule:** In `index.html` deck slides, `transform: rotate()` on a spot is fair game when it improves composition. In Collage Builder, rotation stays out — even when users ask, point to the deck templates as the place for that.

---

## Section Dividers

**Five colorways, each a curated combo — not infinite.**
**Why:** A 21-slide deck needs only a handful of section beats. More variation overwhelmed; less felt repetitive.
**Rule:** Five fixed section-divider variants. Each combines (background image + spot + text color):
- A · Steady Blue — navy + bg-steady-blue-1 + spot-gold-2 + white text
- B · Clean Slate — teal + bg-clean-slate-1 + spot-calm-blue-2 + white text
- C · Calm Blue Light — cream base + bg-calm-blue-1 + spot-gold-1 + dark text
- D · Warm/Cream — cream + bg-calm-blue-2 (low opacity) + spot-ochre-1 + dark text
- E · Intentional Blue — `#2531A5` solid + spot-calm-blue-1 + scribble-sweep + white text

**Section dividers stay quiet.**
**Why:** Adding decorative `divider-illus` and `divider-scribble-corner` ornaments overworked them — "they aren't quite working yet and they'll need more thinking."
**Rule:** Default a divider to `bg + spot + (large) num + title`. Don't add illustration ornaments or corner scribbles unless deliberately designed for a specific variation (variation E's full sweep scribble is the only intentional one).

---

## Layout & Composition

**Slide grid is 1920 × 1080.**
**Why:** Standard widescreen. `deck-stage.js` auto-scales to viewport.
**Rule:** Author at 1920×1080. Use the `<deck-stage>` web component — don't bypass it.

**Collage Builder canvas is 1:1.**
**Why:** Output is for social/header use. 1:1 covers the most channels with one aspect.
**Rule:** Collage Builder export is 2400×2400. No aspect-ratio toggle in v1.

**Max three illustrations per collage composition.**
**Why:** Past three, compositions stopped reading as "a collage" and started reading as "a clip-art pile."
**Rule:** Hard cap at 3. The 4th click replaces the most-recently-selected illustration, never the user's earlier choices.

**Each layer is independently drag/resize/remove. Same controls everywhere.**
**Why:** Layer-specific controls forced users to relearn each layer. One control vocabulary works across spot/scribble/illustration.
**Rule:** Spot, scribble, and illustration layers all use: drag-to-position, corner-handle resize, X to remove. Handles always visible at low opacity, full opacity on hover/select.

---

## Delivery / Tooling

**No build step. Ever.**
**Why:** Internal teams (Jenna, Stacy) need to open files in a browser without dev tooling. Brand guide must work from `file://`.
**Rule:** Static HTML/CSS/JS only. No bundlers, no preprocessors, no install step. If a feature needs a build, it doesn't ship.

**Self-contained per file.**
**Why:** Brand guide pages get linked, copied, forwarded. Cross-file dependencies break that.
**Rule:** Each top-level page (`index.html`, `Collage Builder.html`, brand guide pages) carries its own CSS in a `<style>` block. Shared assets are flat folders (`fonts/`, `deck-assets/`, `uploads/`).

**Original source files preserved alongside delivered ones.**
**Why:** Future re-implementation needs the original handoff intact.
**Rule:** Delivered file (e.g., `index.html`) is a copy or rename — leave the source bundle untouched.

**No screenshots in the brand guide.**
**Why:** Per the original handoff README — screenshots become stale and substitute for the real artifact.
**Rule:** Reference the live HTML, not images of it.

---

## Anti-Rules (these were considered and rejected — keep them out)

- **No off-brand colors** in any picker.
- **No custom hex / eyedropper** in the Collage Builder.
- **No rotation, z-order UI, or multi-instance layers** in Collage Builder v1.
- **No more than 3 illustrations** per Collage Builder composition.
- **No flat-fill recolors** that kill watercolor edge feathering.
- **No third font weight** beyond 500/700 in League Spartan.
- **No mono font** for paragraph-shaped text.
- **No Inconsolata for eyebrows** — eyebrows are League Spartan 500.
- **No Lora italic on attributions** — attributions are Inconsolata uppercase.
- **No general-emphasis italic** in Lora prose — emphasis is bold (Lora 700), optionally with a hand-drawn intentional-blue scribble (ellipse or underline). Italic is reserved for quotes/paraphrasing/callouts.
- **No straight quotes** — always curly (`"`, `"`, `'`, `'`).
- **No flush opening quotes on block quotes** — the opening curly quote hangs outside the text column.
- **No color shift + italic** on the same span.
- **No greyed body text, no opacity fades** on content.
- **No serif Lora for the lead paragraph** under a page-level headline — that's sans serif.
- **No decorative ornament** layers added to section dividers.
- **No backend** for any tool in this kit.

---

## Source PRDs

- `20260504-171007_fetch-design-implement-deck-templates`
- `20260504-171600_section-cover-resize-5-variations`
- `20260504-171800_inconsolata-pullback`
- `20260504-180000_bio-spot-fix-divider-cleanup`
- `20260504-183319_wbt-collage-builder` (iteration 2)
- `20260504-191000_apply-type-rules-brand-guide`
- `20260504-193000_apply-missed-rules` (this PRD — corrects attributions/eyebrows/grey-text/italic-color/sans-serif-supporting rules)
- Today's quote-spot session (granular gold + 160° rotation + 560px sizing)
