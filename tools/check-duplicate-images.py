#!/usr/bin/env python3
"""Fail when one page shows the same photograph more than once.

Client rule (Mike, 2026-11-25): a photo must never appear in two sections of
the same page unless a ticket explicitly asks for that repeat.

Usage:
    python3 tools/check-duplicate-images.py [site_dir]

Exit codes: 0 = clean, 1 = duplicate found, 2 = no HTML found.
"""
import collections
import glob
import os
import re
import sys

IMG_TAG = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
SRC_ATTR = re.compile(r'\bsrc="([^"]+)"', re.IGNORECASE)


def main(argv):
    site = argv[1] if len(argv) > 1 else 'site'
    pages = sorted(glob.glob(os.path.join(site, '*.html')))
    if not pages:
        print(f'No HTML pages found in {site!r}', file=sys.stderr)
        return 2

    failures = 0
    for page in pages:
        with open(page, encoding='utf-8') as handle:
            html = handle.read()
        sources = []
        for tag in IMG_TAG.findall(html):
            # data-check-skip marks viewer/lightbox placeholders, not page content.
            if 'data-check-skip' in tag.lower():
                continue
            match = SRC_ATTR.search(tag)
            if match and not match.group(1).startswith('data:'):
                sources.append(match.group(1))
        repeated = {
            src: count
            for src, count in collections.Counter(sources).items()
            if count > 1
        }
        name = os.path.basename(page)
        if repeated:
            failures += 1
            for src, count in sorted(repeated.items()):
                print(f'FAIL {name}: {src} appears {count} times')
        else:
            print(f'ok   {name}: {len(sources)} images, no repeats')

    if failures:
        print(
            f'\n{failures} page(s) repeat a photo. Use a different photograph '
            'or get an explicit ticket exception.',
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
