#!/usr/bin/env python3
"""Slice the v10 heroes-wide sheet into 3 panels (white-gutter logic)."""
import glob
import os
from PIL import Image

SRC = "/home/hatch/workspace/makefun/news-image-20261122-v10-entry/scenes_raw"
OUT = os.path.join(SRC, "panels")
os.makedirs(OUT, exist_ok=True)


def white_bands(im):
    g = im.convert("L")
    px = g.load()
    w, h = g.size
    bands = []
    y0, y1 = h // 4, 3 * h // 4
    n = (y1 - y0) // 4 + 1
    for x in range(w):
        white = sum(1 for y in range(y0, y1, 4) if px[x, y] > 235)
        if white / n > 0.98:
            bands.append(x)
    ranges = []
    for i in bands:
        if ranges and i == ranges[-1][1] + 1:
            ranges[-1][1] = i
        else:
            ranges.append([i, i])
    return [(a, b) for a, b in ranges if b - a >= 4]


def segments(size, bands):
    segs, cur = [], 0
    for a, b in bands:
        if a - cur >= 200:
            segs.append((cur, a))
        cur = b + 1
    if size - cur >= 200:
        segs.append((cur, size))
    return segs


def is_paper(r, g, b):
    return r > 200 and g > 190 and b > 180 and (r - b) < 45


def trim_white(im):
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


wide = glob.glob(os.path.join(SRC, "media-generation-v10-heroes-wide-*.webp"))
assert len(wide) == 1, wide
im = Image.open(wide[0]).convert("RGB")
bands = white_bands(im)
segs = segments(im.size[0], bands)
print(os.path.basename(wide[0]), im.size, "-> segs:", segs)
names = ["hero1w", "hero2w", "hero3w"]
assert len(segs) == 3, segs
for (x0, x1), name in zip(segs, names):
    panel = trim_white(im.crop((x0, 0, x1, im.size[1])))
    panel.save(os.path.join(OUT, name + ".png"))
    print("  ", name, panel.size)
print("done")
