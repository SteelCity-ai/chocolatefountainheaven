#!/usr/bin/env python3
"""Add responsive srcset/sizes to the Nov 21 photo set (STE-755).

Reads site/index.html and site/gallery.html, and for every <img src="img/*.jpg">
that has generated -480w/-960w derivatives, adds a srcset with the original as
the widest candidate plus a sizes attribute matched to the CSS layout.
Existing width/height/loading/alt/fetchpriority attributes are preserved.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'site', 'img')

DIMS = {}
for line in open(os.path.join(ROOT, 'scripts', 'img-dims.txt'), encoding='utf-8'):
    parts = line.split()
    if len(parts) == 3:
        DIMS[parts[0]] = (int(parts[1]), int(parts[2]))

# Layout-derived sizes. Hero portrait images need 480w on a phone; landscape
# images are object-fit:cover inside a tall arch, so a phone needs the 960w.
HERO_PORTRAIT = '(min-width: 961px) 33vw, 86vw'
HERO_LANDSCAPE = '(min-width: 961px) 40vw, 86vw'
HERO_SECONDARY = '(min-width: 961px) 15vw, 31vw'
PLATES = '(min-width: 821px) 31vw, (min-width: 521px) 48vw, 92vw'
LIGHTBOX = '(min-width: 961px) 80vw, 100vw'


def candidates(base):
    """Return [(path, width)] ascending, ending with the original."""
    name, ext = os.path.splitext(base)
    out = []
    natural = DIMS.get(base)
    for w in (240, 400, 480, 800, 960, 1200, 1600):
        path = 'img/%s-%dw%s' % (name, w, ext)
        if os.path.exists(os.path.join(ROOT, 'site', path)):
            out.append((path, w))
    if natural:
        out.append(('img/' + base, natural[0]))
    return out


def pick_sizes(tag, page):
    src = re.search(r'src="img/([^"]+)"', tag).group(1)
    natural = DIMS.get(src)
    if page == 'index.html':
        if src.startswith('cfh-rot-'):
            if natural and natural[0] >= natural[1]:
                return HERO_LANDSCAPE
            return HERO_PORTRAIT
        if re.match(r'g\d+\.jpg$', src):
            return HERO_SECONDARY
        return PLATES
    if 'data-full' in tag:
        return PLATES
    return LIGHTBOX


def transform(page):
    path = os.path.join(ROOT, 'site', page)
    html = open(path, encoding='utf-8').read()
    changed = 0

    def repl(m):
        nonlocal changed
        tag = m.group(0)
        if 'srcset=' in tag or 'src="img/' not in tag:
            return tag
        src = re.search(r'src="img/([^"]+)"', tag).group(1)
        if not src.endswith(('.jpg', '.jpeg')):
            return tag
        cands = candidates(src)
        if len(cands) < 2:
            return tag
        srcset = ', '.join('%s %dw' % (p, w) for p, w in cands)
        sizes = pick_sizes(tag, page)
        new = tag[:-1].rstrip() + ' srcset="%s" sizes="%s">' % (srcset, sizes)
        changed += 1
        return new

    html2 = re.sub(r'<img[^>]*>', repl, html)
    # Smaller wordmark: the 991x760 file was served into a 97x74 box.
    html2 = html2.replace('src="img/angels.webp"', 'src="img/angels-194w.webp"')
    for base in ('home-4', 'home-5'):
        html2 = html2.replace('srcset="img/%s-800w.jpg 800w' % base,
                              'srcset="img/%s-400w.jpg 400w, img/%s-800w.jpg 800w' % (base, base))
    open(path, 'w', encoding='utf-8').write(html2)
    print(page, 'img tags updated:', changed)


for page in ('index.html', 'gallery.html'):
    transform(page)
