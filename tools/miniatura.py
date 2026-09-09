#!/usr/bin/env python3
"""Собирает превью формата «Through the Years»: сплит 50/50 + годы + флаг углом.

  python3 tools/miniatura.py LEFT.png RIGHT.png OUT.png 1945 2026
  python3 tools/miniatura.py L.png R.png OUT.png 1945 2026 --flag-corner tl

Текст и флаг рисуются здесь, а не генератором: AI врёт в цифрах и в пропорциях
флага. Картинки на вход должны быть без единой буквы.
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
DIVIDER = 6                    # белая полоса по центру, px
LEG_X, LEG_Y = 0.29, 0.44      # катеты флагового угла в долях кадра
YEAR_CAP = 0.165               # высота цифры в долях высоты кадра
YEAR_CX = (0.26, 0.76)         # центры годов по X
YEAR_CY = 0.785                # центр годов по Y
SHADOW = (0, 0, 0, 110)

# Флаг сверху вниз; первая полоса ложится в самый угол.
FLAGS = {
    "pl": [(255, 255, 255), (0xDC, 0x14, 0x3C)],
    "de": [(0, 0, 0), (0xDD, 0x00, 0x00), (0xFF, 0xCE, 0x00)],
    "jp": [(255, 255, 255)],
    "ua": [(0x00, 0x57, 0xB7), (0xFF, 0xD7, 0x00)],
    "cz": [(255, 255, 255), (0xD7, 0x14, 0x1A)],
}

FONTS = [
    "fonts/Anton.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(path, cap_px):
    """Подбирает кегль так, чтобы высота прописной цифры совпала с cap_px."""
    size = int(cap_px * 1.3)
    for _ in range(80):
        f = ImageFont.truetype(path, size)
        box = f.getbbox("0")
        cap = box[3] - box[1]
        if abs(cap - cap_px) <= 1:
            return f
        size += 1 if cap < cap_px else -1
        size = max(8, size)
    return ImageFont.truetype(path, size)


def pick_font():
    """Первый шрифт из списка, который реально открывается.

    Файл может существовать и при этом не быть шрифтом: в fonts/ лежат
    сохранённые страницы ошибок вместо Anton и Oswald.
    """
    for p in FONTS:
        if not Path(p).exists():
            continue
        try:
            ImageFont.truetype(p, 24)
            return p
        except OSError:
            print(f"пропущен битый шрифт: {p}")
    raise SystemExit("не найден ни один рабочий шрифт из списка FONTS")


def half(img_path, box_w, box_h, anchor=0.5):
    """Вписывает картинку в половину кадра, без искажения пропорций.

    anchor — куда сдвинуть окно обрезки по горизонтали: 0 левый край,
    0.5 центр, 1 правый. Нужен, когда важный объект стоит не по центру
    исходника и при центральной обрезке вылетает из кадра.
    """
    im = Image.open(img_path).convert("RGB")
    scale = max(box_w / im.width, box_h / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    left = round((im.width - box_w) * min(max(anchor, 0.0), 1.0))
    top = (im.height - box_h) // 2
    return im.crop((left, top, left + box_w, top + box_h))


def draw_flag(canvas, code, corner, outline=True):
    """Рисует флаг диагональным углом: полосы концентричны от вершины угла."""
    stripes = FLAGS[code]
    lx, ly = int(W * LEG_X), int(H * LEG_Y)
    vx, vy = (W, 0) if corner == "tr" else (0, 0)
    sx = -1 if corner == "tr" else 1

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # От самой длинной к самой короткой: каждая следующая перекрывает середину,
    # так получаются полосы, параллельные гипотенузе.
    for i in range(len(stripes) - 1, -1, -1):
        s = (i + 1) / len(stripes)
        d.polygon(
            [(vx, vy), (vx + sx * lx * s, vy), (vx, vy + ly * s)],
            fill=stripes[i],
        )
    if outline:
        d.line(
            [(vx + sx * lx, vy), (vx, vy + ly)],
            fill=(0, 0, 0, 90),
            width=3,
        )
    canvas.alpha_composite(layer)


def draw_year(canvas, text, cx, font):
    box = font.getbbox(text)
    w, h = box[2] - box[0], box[3] - box[1]
    pad = 24
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    ox, oy = -box[0] + pad, -box[1] + pad
    d.text((ox + 6, oy + 7), text, font=font, fill=SHADOW)     # тень
    d.text((ox, oy), text, font=font, fill=(255, 255, 255, 255))
    canvas.alpha_composite(
        layer, (int(cx - layer.width / 2), int(H * YEAR_CY - layer.height / 2))
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("left"), ap.add_argument("right"), ap.add_argument("out")
    ap.add_argument("year_left"), ap.add_argument("year_right")
    ap.add_argument("--flag", default="pl", choices=sorted(FLAGS))
    ap.add_argument("--flag-corner", default="tr", choices=["tl", "tr"])
    ap.add_argument("--no-flag", action="store_true")
    ap.add_argument("--anchor-left", type=float, default=0.5,
                    help="точка обрезки левой половины: 0 левый край, 0.5 центр, 1 правый")
    ap.add_argument("--anchor-right", type=float, default=0.5,
                    help="то же для правой половины")
    ap.add_argument("--font", default=None)
    a = ap.parse_args()

    hw = W // 2
    canvas = Image.new("RGBA", (W, H))
    canvas.paste(half(a.left, hw, H, a.anchor_left), (0, 0))
    canvas.paste(half(a.right, W - hw, H, a.anchor_right), (hw, 0))

    d = ImageDraw.Draw(canvas)
    d.rectangle([hw - DIVIDER // 2, 0, hw + DIVIDER // 2, H], fill=(255, 255, 255))

    if not a.no_flag:
        draw_flag(canvas, a.flag, a.flag_corner)

    font = load_font(a.font or pick_font(), int(H * YEAR_CAP))
    draw_year(canvas, a.year_left, W * YEAR_CX[0], font)
    draw_year(canvas, a.year_right, W * YEAR_CX[1], font)

    canvas.convert("RGB").save(a.out, quality=95)
    print(f"{a.out}  {W}x{H}  {a.year_left} | {a.year_right}  флаг: "
          f"{'нет' if a.no_flag else a.flag + ' ' + a.flag_corner}")


if __name__ == "__main__":
    main()
