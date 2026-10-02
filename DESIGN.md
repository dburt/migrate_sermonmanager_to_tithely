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
church's logo, favicon, theme stylesheet, and Montserrat / Roboto pairing wholesale,
and stays deliberately subordinate while Tithely remains the production site.

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
- Single static page: filters, a sermon list, and a detail/transcript view.

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
- **Muted on Dark** (`#80a8b6`): muted text placed on a Deep Teal surface.

### Named Rules
**The One Accent Rule.** Harbour Cyan is used on ≤10% of any screen. Its scarcity is
what makes the primary action legible; secondary actions use Deep Teal or a border, not
more cyan.

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
- **Label** (Montserrat 500, 15px, 1.55): button labels and small UI labels.

### Named Rules
**The Uniform 1.55 Rule.** Every type role uses `line-height: 1.55` with
`letter-spacing: 0`. This is the system's most load-bearing decision; never tighten it
for a heading or a card.

**The Reads-In-Roboto Rule.** Anything meant to be read more than a glance is Roboto.
Montserrat only appears for display headings and button labels.

## Layout

Single static page, no build step. Content is constrained to a centered container —
the church theme's container is 1160px with 10px gutters; the archive page uses a
1200px container with 20px side padding and sits on the `#f4f4f4` canvas. The
composition is one column: a top links bar, a header band with the church logo, a
filter panel, then the sermon list, with a paginated rhythm below.

The church theme's breakpoints are the reference: `320 / 414 / 768 / 991 / 1024 / 1199
/ 1200`. Below 768px the filter panel collapses (accordion toggles) and the list goes
single-column; the page must never scroll horizontally. Spacing follows a light
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
  the cyan ring (`0 0 0 3px #0099ce`).
- **Secondary:** Deep Teal fill (`#00506c`, hover `#002a39`), white label — the right
  choice for routine actions so cyan stays scarce.
- **Tertiary:** Warm Amber (`#f7931d`) — use at most once per screen.
- **Link / Ghost:** text in Deep Teal with no fill.

### Chips
- **Style:** pill-shaped (30px radius), on white or `#f1f1f1`; the active filter link
  is bold rather than recolored.
- **State:** passive filter values in a left list read as plain Deep Teal links; the
  currently applied filter is emphasized by weight, and "Clear All Filters" is the
  destructive action (red) and should be visually secondary.

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
- **Disabled:** `#f1f1f1` background, reduced opacity.

### Navigation
- **Style:** a single top links bar (thin, `#f4f4f4`, hairline bottom border) above a
  full-width header band carrying the church logo. Nav text is Roboto 15px; links are
  Deep Teal. Active state is a weight/underline change, never a color swap to cyan.

### Signature Component — Sermon Detail & Transcript
- The archive's distinctive unit: a sermon row that expands into a detail view with
  metadata, a related-sermons list, and a collapsible transcript
  (`.transcript-toggle` / `.transcript-section`). The transcript is the longest read in
  the system, so it is pure Roboto body at 15px/1.55 in a 65–75ch measure, with a
  quiet, bordered container. It is a finding aid, not an authoritative text.

## Do's and Don'ts

### Do:
- **Do** lead with the church's identity — logo, favicon, Montserrat/Roboto, and the
  harbour-cyan / deep-teal palette — and invent nothing of your own.
- **Do** keep all type at `line-height: 1.55` and `letter-spacing: 0`.
- **Do** make links Deep Teal (`#00506c`) and reserve Harbour Cyan (`#0099ce`) for the
  one primary action per view.
- **Do** separate surfaces with tonal layering and hairline borders; lift only on
  hover/focus.
- **Do** keep the page single-column and simple; put complexity in the pipeline, not
  the interface.

### Don't:
- **Don't** hardcode `#007bff`, `#0000ee`, or any off-palette blue for links or
  controls — that is the browser default leaking through, not a design decision.
- **Don't** use Warm Amber (`#f7931d`) for anything but the single tertiary action.
- **Don't** add resting shadows to static cards or panels.
- **Don't** introduce a second typeface, a display serif, or a weight outside the
  Montserrat/Roboto roles above.
- **Don't** assume sermon or preacher imagery exists — the export carries none, so no
  layout may depend on it.
