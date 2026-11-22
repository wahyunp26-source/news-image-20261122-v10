#!/usr/bin/env python3
"""Crop the 13 sliced v10 panels to their display aspect, resize, quantize
to a 256-colour palette PNG, and save as scenes/*.png for the v10 repo.

Display sizes (from the layout): heroes 304x150, mids 186x96.
Each scene gets (squash_y, fy): squash_y shrinks the panel vertically first
(the wide hero panels and the tall mid panels pack their content into a
band taller than the 2:1 display window, so a mild vertical squash keeps
globe + thermometer + clock + delegates, drones + skyline + fires, towers
+ tanks + ship together); fy then picks the crop window's vertical position
(0 = top, 1 = bottom) inside the squashed panel.
"""
import os
from PIL import Image

PANELS = "/home/hatch/workspace/makefun/news-image-20261122-v10-entry/scenes_raw/panels"
OUT = "/home/hatch/workspace/makefun/news-image-20261122-v10-entry/scenes"
os.makedirs(OUT, exist_ok=True)

# name -> (panel file, display_w, display_h, squash_y, fy)
SCENES = {
    "hero1-cop31": ("hero1w.png", 304, 150, 0.80, 0.40),
    "hero2-kyiv": ("hero2w.png", 304, 150, 0.84, 0.50),
    "hero3-bahrain": ("hero3w.png", 304, 150, 0.85, 0.72),
    "mid4-ship": ("mid4-ship.png", 186, 96, 1.00, 0.70),
    "mid5-kryvyi": ("mid5-kryvyi.png", 186, 96, 1.00, 0.60),
    "mid6-boat": ("mid6-boat.png", 186, 96, 1.00, 0.72),
    "mid7-jerusalem": ("mid7-jerusalem.png", 186, 96, 1.00, 0.70),
    "mid8-gaza": ("mid8-gaza.png", 186, 96, 1.00, 0.72),
    "mid9-chapo": ("mid9-chapo.png", 186, 96, 1.00, 0.45),
    "mid10-tehran": ("mid10-tehran.png", 186, 96, 1.00, 0.30),
    "mid11-nvidia": ("mid11-nvidia.png", 186, 96, 1.00, 0.35),
    "mid12-bolsonaro": ("mid12-bolsonaro.png", 186, 96, 1.00, 0.45),
    "mid13-aukus": ("mid13-aukus.png", 186, 96, 1.00, 0.58),
}

total = 0
for name, (panel, dw, dh, sq, fy) in SCENES.items():
    im = Image.open(os.path.join(PANELS, panel)).convert("RGB")
    w, h = im.size
    if sq != 1.0:
        im = im.resize((w, int(h * sq)), Image.LANCZOS)
        w, h = im.size
    cw = w
    ch = int(w * dh / dw)
    y0 = int((h - ch) * fy)
    y0 = max(0, min(h - ch, y0))
    crop = im.crop((0, y0, w, y0 + ch))
    crop = crop.resize((dw, dh), Image.LANCZOS)
    pal = crop.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
    path = os.path.join(OUT, name + ".png")
    pal.save(path, optimize=True)
    n = os.path.getsize(path)
    total += n
    print(f"{name}: panel {w}x{h} squash={sq} crop y0={y0} h={ch} -> {dw}x{dh} {n} bytes")
print("TOTAL scenes bytes:", total)
