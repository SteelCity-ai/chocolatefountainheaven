# Chocolate Fountain Heaven

## Direction

An editorial event-service site: warm paper, espresso typography, restrained brass details, and the client's own reception photographs. The large serif headings, numbered chapters and fountain price rows give the business a distinct visual identity. Keep actual packages easy to scan and contact details easy to find.

Hermes created and refined the seven-page design. Codex applied the **Frontend UI Engineering** skill for the final design, responsive and interaction review. This document records the implemented design; it does not claim the initial draft was generated with that skill.

## Visual system

- Paper `#fbf7ef`, cream `#f4ecdd`, espresso `#150d09`, cocoa `#43261a`.
- Brass `#86602e` for text and controls on paper; light brass `#cfa46a` for dark sections. The darker brass preserves the palette while improving normal-text contrast.
- Bodoni Moda for display, Cormorant Garamond for editorial copy, Jost for navigation and body text. System serif/sans fallbacks remain available.
- Hairline dividers, square controls, open layouts and real images; avoid decorative card grids and heavy shadows.
- Shared styles live in `site/css/style.css`; shared behavior in `site/js/main.js`. The static `site/` files are authoritative and require no build step.

## Interaction and accessibility

Use one H1 per page, labeled form fields, keyboard skip links and visible focus styles. The mobile menu reports its expanded state, moves focus inside, contains keyboard focus while open and restores focus on close. The gallery viewer supports keyboard opening, previous/next, Escape, contained focus and return to its originating photograph. Respect reduced motion.

Inner pages use dark navigation on paper. Home uses light navigation over the photograph and switches to dark text after scrolling. Keep real business content and source images; client approval is required for final pricing and claims.

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
