# Visual Specification — Xince Industrial-Tech PPTX

## Original source
The visual language is abstracted from a 36-slide, 16:9 semiconductor equipment pitch deck. No proprietary slides, client information, source photography, or original slide screenshots are published here. Original slides were rasterized; font identities and theme palette cannot be forensically extracted.

## Exact canonical palette
| Name | HEX | Use |
|---|---|---|
| Navy | `#081727` | Dominant background |
| Tech blue | `#174765` | Navigation and panels |
| Cyan | `#24CDDF` | HUD borders, pointers, engineering highlights |
| Electric blue | `#4C85D7` | Data, flow arrows, secondary emphasis |
| Champagne gold | `#DFC48C` | Single key conclusion or metric |
| Cool white | `#F1F6FA` | Primary text and titles |
| Alert red | `#D62832` | Risks and failures only |
| Verified green | `#28AA83` | Evidence-based pass/completed only |

Exact values in `assets/design-tokens.json` are authoritative. Suggested visual distribution: navy 70–80%, cool-white text 10–18%, cyan/electric-blue 7–10%, gold 2–4%, red/green only for meaning.

## Background and visual effects
- Dark navy foundation with restrained, low-contrast blue layering and subtle circuit motif.
- Tech-blue navigation and HUD panels with cyan 1–1.5pt straight borders.
- Delicate cyan accent glow, never a continuous distracting neon halo.
- Use connecting lines and arrows only to convey information flow.
- Real equipment, PCB screenshots, factory evidence, technical diagrams: prefer these over stock decorations.
- Put a one-sentence champagne-gold conclusion in a narrow bottom ribbon.

## Typography
- Chinese: Microsoft YaHei, Source Han Sans or PingFang; English: Aptos or Arial.
- Main title ~28–36pt; section 26–30pt; charts 17–21pt; main text 16–20pt; big numbers 30–50pt.
- Decorative brush lettering may appear as a limited cover treatment, never for body text.
- Avoid text shadows on ordinary copy, fake 3D labels, excess bolding, and small unreadable captions.

## Layout grammar
- `NAV`: up to nine top-level chapters, highlight current; reduce to 4–6 on short decks.
- `HUD_CARD`: dark panel, fine cyan border, meaningful label, inner padding.
- `PHOTO_CARD`: consistent aspect ratio and crop; concise caption.
- `EVIDENCE_ISLAND`: clear screenshots and diagrams with subtle blue frame.
- `METRIC`: prominent verified value, units, concise explanation.
- `CLAIM_RIBBON`: bottom gold/white conclusion with business meaning.

## Modes
**faithful** preserves navigation, denser engineering modules, and gold takeaway; still ensures legibility. **refined** (default) reduces decoration, limits each slide to one proposition and 2–3 information modules, and maximizes projection readability.

Anti-patterns: saturated purple/red game-poster cyberpunk, too much neon, logos without context, invented engineering evidence, data without dates/units, full-slide bitmap as an allegedly editable PowerPoint.
