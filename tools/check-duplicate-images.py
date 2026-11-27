#!/usr/bin/env python3
"""Fail when one page shows the same photograph more than once.

Client rule (Mike, 2026-11-25): a photo must never appear in two sections of
the same page unless a ticket explicitly asks for that repeat.

Two checks per page:
  1. the same `src` used by more than one <img>
  2. two different `src` values whose files are byte-identical (same photo
     saved under two names)

Visually identical crops or resizes are not detectable this way; the DESIGN.md
rule covers those and reviewers must still look at the page.

Usage:
    python3 tools/check-duplicate-images.py [site_dir]

Exit codes: 0 = clean, 1 = duplicate found, 2 = no HTML found.
"""
import collections
import glob
import hashlib
import os
import re
import sys

IMG_TAG = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
SRC_ATTR = re.compile(r'\bsrc="([^"]+)"', re.IGNORECASE)


def file_hash(site, src):
    path = os.path.join(site, src)
    try:
        with open(path, 'rb') as handle:
            return hashlib.sha256(handle.read()).hexdigest()
    except OSError:
        return None


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

        name = os.path.basename(page)
        problems = []
        for src, count in sorted(collections.Counter(sources).items()):
            if count > 1:
                problems.append(f'{src} appears {count} times')

        by_hash = collections.defaultdict(set)
        for src in set(sources):
            digest = file_hash(site, src)
            if digest:
                by_hash[digest].add(src)
        for digest, names in sorted(by_hash.items()):
            if len(names) > 1:
                problems.append(
                    'same image bytes under different names: ' + ', '.join(sorted(names))
                )

        if problems:
            failures += 1
            for problem in problems:
                print(f'FAIL {name}: {problem}')
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
