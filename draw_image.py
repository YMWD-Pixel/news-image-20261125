#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news image (1024x1024, PNG).
Six verified stories from 25 Nov 2026, laid out as a newspaper front page.
Run: python3 draw_image.py  -> entry.png in this directory."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
NAVY = (13, 27, 62)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
GREY = (90, 90, 90)
LIGHT = (245, 242, 235)
WHITE = (255, 255, 255)

def font(name, size):
    for p in [f"/usr/share/fonts/truetype/dejavu/{name}",
              f"/usr/share/fonts/truetype/liberation/{name}"]:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()

F_TITLE = font("DejaVuSerif-Bold.ttf", 64)
F_DATE = font("DejaVuSans-Bold.ttf", 30)
F_KICK = font("DejaVuSans-Bold.ttf", 22)
F_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_HEAD_SM = font("DejaVuSans-Bold.ttf", 26)
F_BODY = font("DejaVuSans.ttf", 24)
F_BODY_SM = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans-Bold.ttf", 20)

img = Image.new("RGB", (W, H), LIGHT)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 150], fill=NAVY)
d.text((32, 22), "WORLD NEWS", font=F_TITLE, fill=WHITE)
d.text((32, 100), "WEDNESDAY  •  25 NOVEMBER 2026", font=F_DATE, fill=GOLD)
d.text((W - 32, 100), "ONE DAY, SIX STORIES", font=F_FOOT, fill=WHITE, anchor="ra")

def wrap(draw, text, fnt, width, x, y, fill, spacing=6):
    for line in textwrap.wrap(text, width=width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y

# Lead story
d.rectangle([24, 164, W - 24, 360], fill=WHITE, outline=RED, width=4)
d.rectangle([24, 164, W - 24, 204], fill=RED)
d.text((40, 172), "LEAD  •  STRAIT OF HORMUZ", font=F_KICK, fill=WHITE)
wrap(d, "Two oil tankers hit mines and caught fire", F_HEAD, 34, 40, 216, INK)
wrap(d, "Iran says the vessels struck naval mines; fires burned as fears for shipping grew.", F_BODY, 52, 40, 288, GREY)

stories = [
    ("01  UKRAINE", NAVY, "Drones hit Russian refineries",
     "Ukraine hit two Russian refineries and sank a Russian warship off Libya."),
    ("02  SAUDI ARABIA", RED, "Houthi strikes on Riyadh and refinery",
     "Houthis hit the Ras Tanura refinery and a Riyadh tower, injuring 11."),
    ("03  UNITED STATES", NAVY, "Huawei convicted in New York",
     "A US jury convicted Huawei of bank fraud and stealing trade secrets."),
    ("04  MARKETS", RED, "Asian stocks plunge; Dow tops 50,000",
     "KOSPI fell 6.2%, Nikkei 2.8%; the Dow closed above 50,000."),
    ("05  SPACE & PACIFIC", NAVY, "Shenzhou-24 docks; Pacific treaty",
     "Shenzhou-24 docked with Tiangong; Australia signed a Pacific treaty."),
    ("06  CLIMATE", RED, "COP31 talks fail to agree",
     "UN climate talks ended without a deal; Pope Leo warned of extreme weather."),
]

# 2 columns x 3 rows
x0, y0 = 24, 376
cw, ch, gap = 476, 192, 16
for i, (kick, col, head, body) in enumerate(stories):
    x = x0 + (i % 2) * (cw + gap)
    y = y0 + (i // 2) * (ch + gap)
    d.rectangle([x, y, x + cw, y + ch], fill=WHITE, outline=(200, 200, 200), width=2)
    d.rectangle([x, y, x + cw, y + 34], fill=col)
    d.text((x + 12, y + 5), kick, font=F_KICK, fill=WHITE)
    yy = wrap(d, head, F_HEAD_SM, 26, x + 12, y + 44, INK, spacing=4)
    wrap(d, body, F_BODY_SM, 32, x + 12, yy + 2, GREY, spacing=4)

d.text((32, H - 28), "All six stories happened or were first reported on 25 November 2026.", font=F_FOOT, fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
