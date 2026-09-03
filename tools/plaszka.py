#!/usr/bin/env python3
"""Накладывает брендовую плашку на превью 1280x720.

  python3 tools/plaszka.py IN.png OUT.png "TEKST"
  python3 tools/plaszka.py IN.png OUT.png "WRZESIEN" "MARZEC"   # вариант BEFORE/AFTER
"""
import sys
from PIL import Image, ImageDraw, ImageFont

GREEN  = (0x2A, 0x4A, 0x33)
BORDO  = (0x7A, 0x15, 0x20)
WHITE  = (255, 255, 255)
FONT   = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BAR    = 0.14   # высота плашки от кадра
CAP    = 0.65   # высота прописных от плашки
SQUEEZE= 0.78   # сжатие по горизонтали -> узкий гротеск


def fit_font(target_cap):
    """Подбирает кегль так, чтобы высота прописной = target_cap."""
    size = int(target_cap * 1.4)
    for _ in range(60):
        f = ImageFont.truetype(FONT, size)
        box = f.getbbox("H")
        cap = box[3] - box[1]
        if abs(cap - target_cap) <= 1:
            return f
        size += 1 if cap < target_cap else -1
        size = max(8, size)
    return ImageFont.truetype(FONT, size)


def draw_text(canvas, text, cx, cy, font, max_w):
    """Рисует сжатый по горизонтали текст с центром в (cx, cy)."""
    box = font.getbbox(text)
    w, h = box[2] - box[0], box[3] - box[1]
    layer = Image.new("RGBA", (w + 4, h + 4), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((-box[0] + 2, -box[1] + 2), text, font=font, fill=WHITE)
    nw = int(layer.width * SQUEEZE)
    if nw > max_w:                       # длинная строка — дожимаем по ширине
        nw = max_w
    layer = layer.resize((nw, layer.height), Image.LANCZOS)
    canvas.paste(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)), layer)


def main():
    src, dst, *texts = sys.argv[1:]
    im = Image.open(src).convert("RGB")
    W, H = im.size
    bar = int(H * BAR)
    d = ImageDraw.Draw(im)

    if len(texts) == 2:                  # BEFORE/AFTER: левая половина бордовая
        d.rectangle([0, 0, W // 2, bar], fill=BORDO)
        d.rectangle([W // 2, 0, W, bar], fill=GREEN)
    else:
        d.rectangle([0, 0, W, bar], fill=GREEN)

    font = fit_font(bar * CAP)
    if len(texts) == 2:
        draw_text(im, texts[0].upper(), W * 0.25, bar / 2, font, int(W * 0.44))
        draw_text(im, texts[1].upper(), W * 0.75, bar / 2, font, int(W * 0.44))
    else:
        draw_text(im, texts[0].upper(), W / 2, bar / 2, font, int(W * 0.94))

    im.save(dst)
    print(f"{dst}  плашка {bar}px  прописные {int(bar*CAP)}px")


if __name__ == "__main__":
    main()
