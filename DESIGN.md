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
