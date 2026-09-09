#!/usr/bin/env python3
"""Превью формата «аэросъёмка + жёлтая плашка + стрелка лет».

  python3 tools/miniatura_aerial.py IN.png OUT.png WARSAW 1300 2026

Показывается только ранний год; поздний живёт лишь в подписи — в этом весь хук
формата. Текст рисуется здесь, генератору его не показывать.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

from miniatura import load_font, pick_font

W, H = 1280, 720

YELLOW = (0xFF, 0xE4, 0x00)
BLACK = (0x0A, 0x0A, 0x0A)
WHITE = (255, 255, 255)

BAR_TOP = 0.042        # отступ плашки сверху, доля высоты
BAR_H = 0.155          # высота плашки
BAR_CAP = 0.60         # высота прописной от высоты плашки
BAR_PAD = 34           # горизонтальные поля внутри плашки, px

YEAR_CAP = 0.100       # высота цифры, доля высоты кадра
YEAR_CY = 0.895        # центр строки лет по вертикали
YEAR_STROKE = 7        # чёрная обводка цифр, px
ARROW_LEN = 0.24       # длина стрелки, доля ширины
ARROW_GAP = 38         # зазоры вокруг стрелки, px
ARROW_BAR = 15         # толщина древка, px
ARROW_HEAD_L = 40      # длина наконечника, px
ARROW_HEAD_H = 46      # половина высоты наконечника, px

SERIF = [
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]


def cover(img_path):
    """Вписывает картинку в кадр 1280x720 по центру, без искажения пропорций."""
    im = Image.open(img_path).convert("RGB")
    scale = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2,
                    (im.width - W) // 2 + W, (im.height - H) // 2 + H))


def draw_bar(canvas, text, font):
    box = font.getbbox(text)
    tw, th = box[2] - box[0], box[3] - box[1]
    bar_h = int(H * BAR_H)
    bar_w = tw + BAR_PAD * 2
    x0, y0 = (W - bar_w) // 2, int(H * BAR_TOP)

    d = ImageDraw.Draw(canvas)
    d.rectangle([x0, y0, x0 + bar_w, y0 + bar_h], fill=YELLOW)
    d.text((x0 + BAR_PAD - box[0], y0 + (bar_h - th) // 2 - box[1]),
           text, font=font, fill=BLACK)


def draw_arrow(d, x, cy):
    """Стрелка вправо: древко плюс наконечник, белая с чёрной обводкой."""
    length = int(W * ARROW_LEN)
    tail_end = x + length - ARROW_HEAD_L
    shaft = [x, cy - ARROW_BAR // 2, tail_end, cy + ARROW_BAR // 2]
    head = [(tail_end, cy - ARROW_HEAD_H), (x + length, cy), (tail_end, cy + ARROW_HEAD_H)]
    o = 4
    d.rectangle([shaft[0] - o, shaft[1] - o, shaft[2] + o, shaft[3] + o], fill=BLACK)
    d.polygon([(head[0][0] - o, head[0][1] - o), (head[1][0] + o, head[1][1]),
               (head[2][0] - o, head[2][1] + o)], fill=BLACK)
    d.rectangle(shaft, fill=WHITE)
    d.polygon(head, fill=WHITE)
    return length


def draw_years(canvas, y_from, y_to, font):
    d = ImageDraw.Draw(canvas)
    b1, b2 = font.getbbox(y_from), font.getbbox(y_to)
    w1, w2 = b1[2] - b1[0], b2[2] - b2[0]
    total = w1 + ARROW_GAP + int(W * ARROW_LEN) + ARROW_GAP + w2
    x = (W - total) // 2
    cy = int(H * YEAR_CY)

    def text(s, box, left):
        d.text((left - box[0], cy - (box[3] + box[1]) // 2), s, font=font,
               fill=WHITE, stroke_width=YEAR_STROKE, stroke_fill=BLACK)

    text(y_from, b1, x)
    x += w1 + ARROW_GAP
    x += draw_arrow(d, x, cy) + ARROW_GAP
    text(y_to, b2, x)


def main():
    ap = argparse.ArgumentParser()
    for name in ("image", "out", "city", "year_from", "year_to"):
        ap.add_argument(name)
    ap.add_argument("--bar-font", default=None, help="шрифт плашки, по умолчанию антиква")
    ap.add_argument("--year-font", default=None, help="шрифт лет, по умолчанию антиква")
    a = ap.parse_args()

    def serif():
        for p in SERIF:
            if Path(p).exists():
                return p
        return pick_font()

    canvas = cover(a.image)
    draw_bar(canvas, a.city.upper(),
             load_font(a.bar_font or serif(), int(H * BAR_H * BAR_CAP)))
    draw_years(canvas, a.year_from, a.year_to,
               load_font(a.year_font or serif(), int(H * YEAR_CAP)))
    canvas.save(a.out, quality=95)
    print(f"{a.out}  {W}x{H}  {a.city.upper()}  {a.year_from} -> {a.year_to}")


if __name__ == "__main__":
    main()
