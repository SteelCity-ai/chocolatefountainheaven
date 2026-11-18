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

## Review boundary

This is a client-review draft. The inquiry form opens an email draft in the visitor's mail app; the visitor must send it there. No inquiry backend is installed. Original production is not replaced by this work.
