# Chocolate Fountain Heaven

## Direction

"Blush Modern" (chosen from three concepts, B2). A bold, warm event-service site: ivory paper, cocoa panels, raspberry, gold, mint and lilac color blocks, big Instrument Serif headlines, arch-shaped photo frames, and gentle motion so the site feels alive. Actual packages stay easy to scan and contact details easy to find. All copy, prices and client edits (STE tickets) are unchanged from the earlier editorial build; only the look changed.

## Visual system

- Ink/cocoa `#2b1710`, paper `#fbf6f1`, blush `#f3dcd3`, raspberry `#e0245e` (fills) and `#c40f4d` (text on light), gold `#f7b32b`, mint `#c9ebd2`, lilac `#e2d3f6`, sun `#ffe9b8`.
- Instrument Serif for display, Inter for text. Rounded 30px cards, pill buttons, soft color glows behind the page.
- Header: the original full-width bar (two-line wordmark, uppercase links, Reserve button), restyled; it gains a frosted background after scrolling. Not a floating pill.
- Home hero: arch-framed photo rotation (the five client photos, STE-553) plus a second small rotating frame, floating info chips, count-up numbers. Fountains are a bento grid. Venue names run in a tilted raspberry band.
- A floating "Reserve a date" button appears after the first screen on every page except Contact.
- Shared styles live in `site/css/style.css`; shared behavior in `site/js/main.js`. The static `site/` files are authoritative and require no build step.

## Interaction and accessibility

Use one H1 per page, labeled form fields, keyboard skip links and visible focus styles. The mobile menu reports its expanded state, moves focus inside, contains keyboard focus while open and restores focus on close. The gallery viewer supports keyboard opening, previous/next, Escape, contained focus and return to its originating photograph. Respect reduced motion.

All pages use the same dark-on-light header. Keep real business content and source images; client approval is required for final pricing and claims.

## Photo reuse

Never show the same photograph twice on one page — not in two content sections, and not in a section plus the gallery teaser. If a page needs another image, use a different photograph. An explicit client instruction is the only exception, and it must be quoted in the ticket.

`python3 tools/check-duplicate-images.py` enforces this rule across `site/*.html` and must pass before a release candidate is merged. It catches a repeated filename and two different filenames with identical file bytes; a cropped or resized copy of the same photo still needs a reviewer's eye.

## Review boundary

This is a client-review draft. The inquiry form opens an email draft in the visitor's mail app; the visitor must send it there. No inquiry backend is installed. Original production is not replaced by this work.

## Design 2.0 — “Confectionery Editorial” (STE-355)

Mike's review: the first remodel reads as bland. The refresh keeps the strong editorial bones — serif display type, chapter rhythm, generous space, real photography — and turns up the colour so the brand feels celebratory, stylish and contemporary rather than restrained.

### What changed
- Chocolate is now a deep cocoa noir (`#1e0f0b`) instead of near-black. Berry (`#b3154e`), strawberry (`#f05a7a`), champagne (`#e7b45b`) and pistachio (`#7fae6e`) carry the accents.
- A five-pixel four-colour ribbon runs across the top of every page.
- The home hero is a chocolate-to-berry gradient with a champagne glow; the hero rail, strip and primary button use champagne.
- Sections alternate paper, warm cream, pistachio-soft, rose, champagne-soft and a dark berry gradient. The “how it works” and “book” bands are berry rather than espresso.
- Prices, labels, rules, chapter numerals and gallery captions use berry or champagne. The menu hover is a soft berry wash.
- Buttons keep the crisp editorial edge but use berry or champagne fills. Dark-section buttons switch to champagne so they stay visible.
- Footer sits on cocoa noir with champagne headings and strawberry link hovers.

### Files
- `site/css/style-2.0.css` is the new layer. It loads after `site/css/style.css`, so the original layout, type scale and responsive rules are preserved. Revert by removing the extra stylesheet link.
- `site/js/main.js` is unchanged. The mobile drawer, lightbox, focus management, skip link and reduced-motion behaviour are inherited.

### Accessibility checks
Text pairs were checked against WCAG 2.1 AA:
- Berry `#b3154e` on paper `#fffbf2`: 6.49:1.
- Berry on cream `#fff4e6`: 6.17:1.
- Cream on berry: 6.17:1; cream on berry-deep `#8e1f4b`: 7.9:1.
- Champagne `#e7b45b` on cocoa `#1e0f0b`: 9.82:1; on berry-deep: 4.53:1.
- Ink on champagne-soft `#f7e6b8`: 15.04:1; ink on pistachio-soft `#ddebdc`: 15.06:1.
- Strawberry is used as a decorative accent and for hover states, not for small body text on light fields. Cream on strawberry (2.94:1) is deliberately avoided for text.

### Review boundary
This is still a client-review draft. Pricing, claims and publication require client approval. The inquiry form continues to open an email draft; no backend was added. The new layer is a visual refresh, not a structural rebuild. The original production site is not replaced by this work.

## Design 2.1 — “Brighter & Bolder” (STE-355, accepted direction)

Mike reviewed 2.0 and chose **brighter and bolder**. The 2.1 layer repaints the palette only: brighter berry, hotter strawberry, brighter champagne, fresher pistachio and bolder colour blocks. Layout, type scale, navigation, photography, copy and interaction are unchanged, so 2.1 is a colour layer, not a rebuild.

### Decision record
- 2026-11-09 — owner answer on interaction `e50ef537`: colour direction **brighter**.
- 2026-11-12 — owner note: “keep moving things ahead, remove any gates.” Design acceptance and the internal review holds are closed on that instruction; the direction below is the accepted design.

### Palette (2.1 layer)

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1b0b10` | body and display text on light fields |
| `--paper` | `#fffdf8` | default page field |
| `--cream` | `#fff8ea` | alternating sections, text on dark fields |
| `--berry` / `--berry-deep` | `#d81b60` / `#a30d4f` | buttons, prices, rules, chapter numerals, bands |
| `--berry-bright` | `#e01b63` | hero strip gradient end |
| `--strawberry` | `#ff5c7a` | ribbon, hover accents, decorative only |
| `--champagne` | `#ffd166` | accents, headings on dark fields, hover on berry |
| `--pistachio` / `--pistachio-deep` | `#7ed957` / `#4f8f3f` | ribbon end, soft section fields |
| `--rose`, `--berry-soft`, `--pistachio-soft`, `--champagne-soft` | `#ffd9e4`, `#ffe3ec`, `#e2f5da`, `#fff0c2` | alternating section fields |

### Files and rollback
- `site/css/style-2.1.css` (7,920 bytes) loads after `style.css` and `style-2.0.css` on all seven pages: `index.html`, `fountains.html`, `ranch.html`, `gallery.html`, `weddings.html`, `faq.html`, `contact.html`.
- Rollback: remove the `style-2.1.css` link from the seven pages. 2.0 returns with no other change.

> **Status 2026-11-17 (STE-644):** Design 2.0 and 2.1 are removed from the preview. Mike confirmed 2.1 was only a prototype and must not be served on `cf.steelcity-ai.com`. The seven pages no longer link `style-2.0.css` or `style-2.1.css`, and both files are deleted from the branch `codex/STE-644`. The layer survives in git history on `codex/STE-355` and in the `site.prev3-20261117T025413Z` preview backup. This section is kept as the historical record of the prototype.
- `site/js/main.js` is unchanged. Skip link, focus styles, mobile drawer, gallery viewer, form behaviour and reduced-motion handling are inherited.

### Accessibility (WCAG 2.1 AA, computed)

Body and small text are at or above 4.5:1; large display text is at or above 3:1. Worst cases after five colour corrections made during QA:

| Pair | Ratio |
|---|---|
| Paper on `--berry-bright` (hero strip, corrected) | 4.58:1 |
| Cream `.86` on brightest footer gradient end | 5.01:1 |
| Champagne hover on `--berry-deep` footer | 4.67:1 |
| Ink `.62` gallery caption on `--berry-soft` | 5.04:1 |
| Berry `#d81b60` on paper | 4.87:1 |
| Berry-deep `#a30d4f` on paper | 7.57:1 |
| Cream `#fff8ea` on berry | 4.68:1 |
| Cream on berry-deep | 7.28:1 |
| Champagne on ink | 13.22:1 |
| Berry-deep on champagne | 5.34:1 |
| Ink on paper | 18.75:1 |

Strawberry `#ff5c7a` is decorative and hover-only. It is not used for small text on light fields and cream on strawberry is deliberately avoided.

### Verification record
- Public review build `https://cf.steelcity-ai.com/design-2-1/`: all seven pages and `style-2.1.css` were byte-identical (SHA-256) to commit `541f79d05b0d442d807eb7deba6119e37191d58e` when checked on 2026-11-13. This build and the `/design-2/` build were removed from the preview on 2026-11-17 by STE-644.
- Browser checks: desktop 1440×1000 and mobile 390×844 show no horizontal overflow, no broken images and no console errors on home, gallery, contact and weddings.
- No motion was added; reduced-motion, focus visibility and keyboard behaviour are unchanged from 2.0.

### Delivery boundary
- Pricing and factual claims remain the client's words; they were not edited by this design work and must stay as the business states them.
- The inquiry form still opens an email draft in the visitor's mail app. No backend, analytics or tracking was added.
- Publishing to the customer's live domain is a deployment step, not a further design decision. The source is complete on branch `codex/STE-355` and the review build above shows exactly that source.
