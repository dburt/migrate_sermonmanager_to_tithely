---
name: St Alfred's Sermons Archive
description: A quiet, church-led reading room for a 20-year sermon archive.
colors:
  primary: "#0099ce"
  primary-hover: "#00739b"
  primary-border: "#0086b5"
  secondary: "#00506c"
  secondary-hover: "#002a39"
  secondary-border: "#003d52"
  link: "#00506c"
  tertiary: "#f7931d"
  canvas: "#f4f4f4"
  surface: "#ffffff"
  surface-muted: "#f1f1f1"
  border: "#e6e6e6"
  text: "#333333"
  text-strong: "#222222"
  text-muted: "#666666"
  text-muted-on-dark: "#80a8b6"
  text-subtle-on-dark: "#9dc1d1"
typography:
  display:
    fontFamily: "Montserrat, sans-serif"
    fontSize: "clamp(32px, 3.906vw, 40px)"
    fontWeight: 800
    lineHeight: 1.55
    letterSpacing: "0"
  headline:
    fontFamily: "Roboto, sans-serif"
    fontSize: "clamp(28px, 2.734vw, 28px)"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  title:
    fontFamily: "Roboto, sans-serif"
    fontSize: "clamp(18px, 2.344vw, 24px)"
    fontWeight: 600
    lineHeight: 1.55
    letterSpacing: "0"
  lede:
    fontFamily: "Roboto, sans-serif"
    fontSize: "clamp(16px, 1.953vw, 20px)"
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: "0"
  body:
    fontFamily: "Roboto, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  label:
    fontFamily: "Montserrat, sans-serif"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: "0.2px"
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
rounded:
  xs: "2px"
  sm: "4px"
  md: "6px"
  pill: "30px"
  circle: "50%"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "20px"
  xl: "40px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
  button-secondary-hover:
    backgroundColor: "{colors.secondary-hover}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
  button-tertiary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    height: "37px"
    padding: "6px 12px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
---

# Design System: St Alfred's Sermons Archive

## Overview

**Creative North Star: "The Quiet Reading Room"**

This is not a brand looking for attention. It is a room off the side of the church
where twenty years of sermons are shelved, findable, and readable. The interface
should feel like good light and a clear index: calm, unremarkable in the best way,
and always deferring to the church's own identity and to the recorded voice of the
sermon itself. The archive presents as "St Alfred's Sermons Archive" for St Alfred's
Anglican Church and invents no visual or verbal identity of its own — it borrows the
church's logo, favicon, Montserrat / Roboto pairing, and palette wholesale, in its own
stylesheet, and stays deliberately subordinate while Tithely remains the production
site.

Density is generous rather than tight. Reading (a transcript, a description) is the
primary act, so line-height is uniform at 1.55 across every role and type is never
packed. The palette is the church's: one confident cyan-blue for interaction, a deep
teal for links and structure, a single warm amber for the rare tertiary action, and
otherwise white and neutral grey doing the work. Color is functional, not expressive;
the accent appears on the seasonal event card and the primary button, nowhere else by
habit.

Motion is quiet and short — 200–500ms `ease-in-out` on state only, never on entry.
Depth is flat by default: surfaces separate through tonal layering (canvas `#F4F4F4`
behind white panels) and hairline borders; a lift appears only as a response to hover
or focus. The result should read as considered, not decorated.

**Key Characteristics:**
- Church-led identity, subordinate by intent — no separate brand voice.
- Reading-first, generous 1.55 line-height everywhere.
- One interactive accent (Harbour Cyan), one structural color (Deep Teal), one rare tertiary (Warm Amber).
- Flat at rest, lift on interaction.
- Single static page: a faceted, year-grouped index and a reading view.

## Colors

The palette is the church theme's: a cool harbour cyan carrying interaction, deep teal
carrying links and headers, a single warm amber reserved for tertiary action, on white
and neutral grey.

### Primary
- **Harbour Cyan** (`#0099ce`): the one interactive accent. Primary buttons
  (`.bg-primary`, `.btn-primary`, `.text-primary`) and the form-control focus border.
  Hover deepens it to `#00739b` (border `#0086b5`). It is the only color that should
  ever read as "click me."
- **Harbour Cyan — Hairline** (`#00b0ed`): a lighter tint used strictly for rules and
  border accents on a primary-colored surface (`.bg-primary hr`), never for text.

### Secondary
- **Deep Teal** (`#00506c`): the default link color and the structural dark. It carries
  body links, `.btn-link`, the secondary button, and the active-state underline on nav
  items. Hover darkens to `#002a39`; the secondary button border is `#003d52`.

### Tertiary
- **Warm Amber** (`#f7931d`): a single, deliberately rare action color — the tertiary
  button only (`.btn-tertiary`, border `#f28709`). If it appears more than once on a
  screen, something has gone wrong.

### Neutral
- **Reading White** (`#ffffff`): card, panel, and button-text surfaces.
- **Canvas Grey** (`#f4f4f4`): the archive page background; the sermon list rests on it.
- **Muted Surface** (`#f1f1f1`): the theme's resting panel tone and hairline fill.
- **Body Charcoal** (`#333333`): default body text and `.text-body`.
- **Strong Charcoal** (`#222222`): the darkest text step.
- **Muted Charcoal** (`#666666`): secondary and meta text on light surfaces.
- **Field Border Grey** (`#e6e6e6`): the 1px stroke on inputs and dividers.
- **Muted on Dark** (`#80a8b6`): muted text placed on a Deep Teal surface, for large or
  non-essential text only.
- **Subtle on Dark** (`#9dc1d1`): the readable step for body-size text on Deep Teal — any
  small print on the header band. `#80a8b6` fails contrast at 15px (3.5:1), so small text
  on teal uses this step (4.7:1).

### Named Rules
**The One Accent Rule.** Harbour Cyan is used on ≤10% of any screen. Its scarcity is
what makes the primary action legible; secondary actions use Deep Teal or a border, not
more cyan.

**The Accent-Legibility Rule.** Harbour Cyan `#0099ce` is 3.26:1 on white but only
2.96:1 on the `#f4f4f4` canvas and 2.73:1 on the teal masthead. Any cyan that has to be
*seen* — a focus ring, a rule, a bar marking state — uses `#00739b` instead (4.86:1 on
canvas, 5.35:1 on white), or white where the ground is the masthead. Harbour Cyan itself
is reserved for places where it is not being measured: the search field's focus border
against the white field inside it, and the cyan glow. Cyan is never the sole carrier of a
state; weight or a fill always carries it too.

**The No-Invented-Blue Rule.** The archive's own inline CSS must not hardcode
`#007bff` or `#0000ee` link blue. Links are Deep Teal (`#00506c`); interaction is
Harbour Cyan. Any blue that isn't the church palette is a defect.

## Typography

**Display Font:** Montserrat (with `sans-serif`)
**Body Font:** Roboto (with `sans-serif`)

**Character:** A confident geometric for the rare display moment, set against a
neutral, highly legible grotesque for everything read. Montserrat is reserved for the
display heading and button labels; Roboto carries headings, titles, ledes, body, and
every long transcript.

### Hierarchy
- **Display** (Montserrat 800, `clamp(32px, 3.906vw, 40px)`, 1.55): the page's single
  hero heading and primary callouts. Used sparingly.
- **Headline** (Roboto 400, `clamp(28px, 2.734vw, 28px)`, 1.55): section headings.
- **Title** (Roboto 600, `clamp(18px, 2.344vw, 24px)`, 1.55): card and sub-section
  headings, e.g. a sermon title.
- **Lede** (Roboto 300, `clamp(16px, 1.953vw, 20px)`, 1.55): introductory or hero body
  copy on colored surfaces.
- **Body** (Roboto 400, 15px, 1.55): all running text — descriptions, metadata, and
  transcripts. Keep transcript measure to roughly 65–75ch.
- **Caption** (Roboto 400, 12px, 1.55): the small print of the index — dates, passage
  references, counts, timestamps, and other annotation that is read alongside a title,
  never instead of one. It is the only size below Body.
- **Label** (Montserrat 500, 15px, 1.55): button labels and small UI labels.

Steps are deliberately few: 12 / 15 / 18 / 24 / 28 / 32–40. Never introduce a size that
sits between two of them.

### Named Rules
**The Uniform 1.55 Rule.** Every type role uses `line-height: 1.55` with
`letter-spacing: 0`. This is the system's most load-bearing decision; never tighten it
for a heading or a card.

**The Reads-In-Roboto Rule.** Anything meant to be read more than a glance is Roboto.
Montserrat only appears for display headings and button labels.

**The Few-Steps Rule.** Type is set at 12 / 15 / 18 / 24 / 28 / 32–40 and nothing else. A
new size needs a role in the hierarchy above, not a free hand.

## Layout

Single static page, no build step, and now no imported theme stylesheet: the archive ships
its own `stalfreds.css`, built from the tokens above, and loads Montserrat / Roboto from
Google Fonts exactly as the church site does. Behaviour lives in a separate unbundled
`stalfreds.js`, loaded with `defer`; the HTML carries no inline script. Content is constrained to a centered 1200px
container with 20px side padding, sitting on the `#f4f4f4` canvas.

The composition is **the back matter of a hymnal**, in three bands:

1. a thin top links bar (`#f4f4f4`, hairline bottom border) for podcast feed links;
2. a full-width Deep Teal header band (`#00506c`) carrying the church logo, the archive
   `h1`, and the search field;
3. the page body, a `260px minmax(0, 1fr)` two-column grid — a sticky facet rail on the
   left, the register on the right.

The register is one continuous, year-grouped index (day and month, title, passage ·
series · speaker) with sticky year headings and no pagination; it is the page. A fixed year rail on the right edge (desktop only) jumps to a year and marks the
current one. Opening a sermon replaces the register with a 46rem reading view — facts,
description, audio, transcript, related sermons — and the URL carries the slug hash, so
every sermon is linkable and Back returns to the exact scroll position.

The archive's own breakpoints are `600 / 900 / 1200`, not the church theme's: below 900px
the facet rail collapses into per-facet toggles and the year rail is dropped; below 600px
everything is single-column. The page must never scroll horizontally. Spacing follows the
4/8/16/20/40 rhythm, with 20px as the default gap between panels and list items.

## Elevation & Depth

Flat by default. Surfaces are separated by tonal layering — white panels on the
`#f4f4f4` canvas — and by hairline `#e6e6e6` borders, not by resting shadows. Shadow
appears only as a response to state: an interactive row or card lifts on hover, and a
focused field emits a cyan glow. The church theme also defines a soft Bootstrap shadow
vocabulary, which may be used for ephemeral overlays (dropdowns, modals) but not for
static page furniture.

### Shadow Vocabulary
- **Resting panel** (`box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05)`): the church theme's
  `.panel` shadow; acceptable on a white panel that needs a hair of separation.
- **Hover lift** (`box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)`):
  interactive cards/rows on hover only.
- **Focus glow** (`box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(0, 153, 206, 0.6)`):
  the church theme's `.form-control:focus` treatment.

### Named Rules
**The Flat-By-Default Rule.** Static surfaces are flat. If a shadow is visible on a
resting element that isn't a transient overlay, remove it.

## Shapes

A restrained, slightly-soft form language. Corners are gently rounded at 4px for the
default control (`.btn`, `.form-control`, `.panel`, `.alert`), stepping to 6px on
large buttons and 2px on hairline accents. Pills reach 30px and are reserved for
filters/tags; circles (`50%`) are used for avatars and icon buttons. Borders are
hairline (1px) and low-contrast (`#e6e6e6`); the church theme's buttons carry a
same-family darker border (`#0086b5`, `#003d52`) rather than a neutral stroke. There
is no hard-edged, square-cornered element in the interface.

## Components

### Buttons
- **Shape:** gently rounded (4px radius; 6px on large).
- **Primary:** Harbour Cyan fill, white label, Montserrat 500, border `#0086b5`, padding
  `10px 16px` (large).
- **Hover / Focus:** darken to `#00739b`; transition ~200ms `ease-in-out`. Focus uses
  the cyan ring (`0 0 0 3px #0099ce`) on white and neutral grounds. A cyan **label** on
  a cyan fill is illegal at any size below 19px/600 (3.26:1), so a 15px primary label must
  use `#00739b` (5.35:1) instead.
- **Secondary:** Deep Teal fill (`#00506c`, hover `#002a39`), white label — the right
  choice for routine actions so cyan stays scarce.
- **Tertiary:** Warm Amber (`#f7931d`) — use at most once per screen.
- **Link / Ghost:** text in Deep Teal with no fill.

### Chips
- **Style:** pill-shaped (30px radius), white with a hairline `#e6e6e6` border, Caption
  type, label on the left and a circular remove control on the right (minimum 24px
  target).
- **State:** a chip is the record of one applied filter ("Series: Praying the Psalms") or
  of the current search ("Search: grace"). Removing a chip removes exactly that filter;
  "Clear all" clears everything and stays visually secondary.

### Facet Rail
- **Style:** a sticky rail, 260px, hairline borders between sections, one collapsible
  section per facet (series, preacher, year, topic). It has **no panel of its own** — it
  sits directly on the canvas, which is why any mark in it must clear 3:1 on `#f4f4f4`.
- **Options:** a full-width row of Roboto Body text in Deep Teal with a right-aligned count
  in Caption. An applied option is marked three ways at once: a 3px `#00739b` bar in the
  left gutter, a weight change to 700, and near-black (`#222222`) text. Never a cyan fill —
  that would put white text on a ground it cannot legally sit on — and never a recoloured
  link. The bar is the one place cyan marks position at rest; it borrows `#00739b` rather
  than Harbour Cyan because the ground is the canvas, and the weight change carries the
  same state for anyone who cannot see the bar.
- **Counts:** each option's count reflects what is reachable with the *other* facets
  applied, so the rail narrows as you choose.

### Cards / Containers
- **Corner Style:** 4px radius.
- **Background:** white on the `#f4f4f4` canvas.
- **Shadow Strategy:** flat at rest; optional hover lift (see Elevation & Depth).
- **Border:** hairline `#e6e6e6` or none when tonal separation already reads.
- **Internal Padding:** 16–20px.

### Inputs / Fields
- **Style:** white field, 1px `#e6e6e6` stroke, 4px radius, 37px tall, 6px/12px padding,
  15px Roboto, text `#666666`.
- **Focus:** border shifts to Harbour Cyan plus the cyan glow (see Elevation & Depth).
  **On the teal masthead the ring is white, not cyan** — cyan on `#00506c` is 2.73:1,
  below the 3:1 floor for a focus indicator, while white is 8.88:1.
- **Disabled:** `#f1f1f1` background, reduced opacity.

### Navigation
- **Style:** a single top links bar (thin, `#f4f4f4`, hairline bottom border) above the
  Deep Teal header band carrying the church logo, the archive `h1` and the search field.
  Bar links are Roboto Caption in Deep Teal; the current year in the right-edge year
  rail is a weight change, never a color swap to cyan.

### Signature Component — The Register Row
- The archive's distinctive unit: one row of the index, laid out as day and month ·
  title · meta, with a hairline rule beneath and a faint cyan tint on hover. The gutter
  is tabular Caption in muted grey; the year is carried by the year-group heading rather
  than repeated on all 1,489 rows, with the full date kept in the `<time>` element for
  assistive tech. No card, no shadow, no thumbnail — the archive has no imagery and must
  not imply it is missing. There is no transcript badge on the row: availability is
  discovered in the reading view, not advertised twice.

### Signature Component — Sermon Detail & Transcript
- A sermon row opens into a 46rem reading view: facts as a definition list (Date, Series,
  Speaker, Reading, Topics — series and speaker are links that apply that filter back on
  the index), the description, the audio player, a collapsible transcript, related
  sermons by series and speaker, and a link out to the original stalfreds.org listing.
- The transcript is the longest read in the system, so it is pure Roboto body at
  15px/1.55 in a 68ch measure, paragraphised for reading, lazily fetched, and labelled
  a machine-generated finding aid, not an authoritative text.

## Do's and Don'ts

### Do:
- **Do** lead with the church's identity — logo, favicon, Montserrat/Roboto, and the
  harbour-cyan / deep-teal palette — and invent nothing of your own.
- **Do** keep all type at `line-height: 1.55` and `letter-spacing: 0`.
- **Do** make links Deep Teal (`#00506c`) and reserve Harbour Cyan (`#0099ce`) for the
  one primary action per view.
- **Do** separate surfaces with tonal layering and hairline borders; lift only on
  hover/focus.
- **Do** keep the index legible before any interaction — it is the page, not a preview of
  one. Put complexity in the pipeline, not the interface.

### Don't:
- **Don't** hardcode `#007bff`, `#0000ee`, or any off-palette blue for links or
  controls — that is the browser default leaking through, not a design decision.
- **Don't** use Warm Amber (`#f7931d`) for anything but the single tertiary action.
- **Don't** add resting shadows to static cards or panels.
- **Don't** introduce a second typeface, a display serif, or a weight outside the
  Montserrat/Roboto roles above.
- **Don't** assume sermon or preacher imagery exists — the export carries none, so no
  layout may depend on it.
