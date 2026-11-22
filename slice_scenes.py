#!/usr/bin/env python3
"""Slice the 3 generated v10 scene sheets into 13 panels.

Detects white gutter bands (columns that are >98% white) and takes the
segments between them as panels, then trims each panel's own white/cream
frame by finding the bounding box of non-paper pixels.
Sheets are .webp (media tool output); PIL opens them fine.
"""
import glob
import os
from PIL import Image

SRC = "/home/hatch/workspace/makefun/news-image-20261122-v10-entry/scenes_raw"
OUT = os.path.join(SRC, "panels")
os.makedirs(OUT, exist_ok=True)


def white_bands(im, axis):
    """Return list of (start, end) index ranges that are >=98% white."""
    g = im.convert("L")
    px = g.load()
    w, h = g.size
    bands = []
    if axis == "x":
        y0, y1 = h // 4, 3 * h // 4
        n = (y1 - y0) // 4 + 1
        for x in range(w):
            white = sum(1 for y in range(y0, y1, 4) if px[x, y] > 235)
            if white / n > 0.98:
                bands.append(x)
    else:
        x0, x1 = w // 4, 3 * w // 4
        n = (x1 - x0) // 4 + 1
        for y in range(h):
            white = sum(1 for x in range(x0, x1, 4) if px[x, y] > 235)
            if white / n > 0.98:
                bands.append(y)
    ranges = []
    for i in bands:
        if ranges and i == ranges[-1][1] + 1:
            ranges[-1][1] = i
        else:
            ranges.append([i, i])
    return [(a, b) for a, b in ranges if b - a >= 4]


def segments(size, bands):
    """Segments of [0, size) split by bands (with 2px safety margin)."""
    segs, cur = [], 0
    for a, b in bands:
        if a - cur >= 200:
            segs.append((cur, a))
        cur = b + 1
    if size - cur >= 200:
        segs.append((cur, size))
    return segs


def is_paper(r, g, b):
    """Cream paper or white: bright with a small red-blue gap."""
    return r > 200 and g > 190 and b > 180 and (r - b) < 45


def trim_white(im):
    """Crop to bounding box of rows/cols with >2% non-paper pixels."""
    px = im.convert("RGB").load()
    w, h = im.size
    xs, ys = [], []
    for x in range(w):
        frac = sum(1 for y in range(0, h, 3) if not is_paper(*px[x, y])) / (h // 3 + 1)
        if frac > 0.02:
            xs.append(x)
    for y in range(h):
        frac = sum(1 for x in range(0, w, 3) if not is_paper(*px[x, y])) / (w // 3 + 1)
        if frac > 0.02:
            ys.append(y)
    if not xs or not ys:
        return im
    return im.crop((max(0, xs[0] - 2), max(0, ys[0] - 2),
                    min(w, xs[-1] + 3), min(h, ys[-1] + 3)))


def slice_strip(path, names):
    im = Image.open(path).convert("RGB")
    bands = white_bands(im, "x")
    segs = segments(im.size[0], bands)
    print(os.path.basename(path), im.size, "xbands:", bands, "-> segs:", segs)
    assert len(segs) == len(names), (len(segs), len(names))
    for (x0, x1), name in zip(segs, names):
        panel = trim_white(im.crop((x0, 0, x1, im.size[1])))
        panel.save(os.path.join(OUT, name + ".png"))
        print("  ", name, panel.size)


heroes = glob.glob(os.path.join(SRC, "media-generation-v10-heroes-*.webp"))
mids_a = glob.glob(os.path.join(SRC, "media-generation-v10-mids-a-*.webp"))
mids_b = glob.glob(os.path.join(SRC, "media-generation-v10-mids-b-*.webp"))
assert len(heroes) == 1 and len(mids_a) == 1 and len(mids_b) == 1, (heroes, mids_a, mids_b)
slice_strip(heroes[0], ["hero1-cop31", "hero2-kyiv", "hero3-bahrain"])
slice_strip(mids_a[0], ["mid4-ship", "mid5-kryvyi", "mid6-boat", "mid7-jerusalem", "mid8-gaza"])
slice_strip(mids_b[0], ["mid9-chapo", "mid10-tehran", "mid11-nvidia", "mid12-bolsonaro", "mid13-aukus"])
print("done")
