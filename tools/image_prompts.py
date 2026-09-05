#!/usr/bin/env python3
"""Собирает цельные промпты картинок из prompts-warsaw.md.

Каждый блок на выходе — законченный промпт: стиль, камера и инструкция кадра
уже склеены, вставлять как есть. Источник правды — prompts-warsaw.md;
поправил инструкцию там, перезапустил скрипт.
"""

import re
import sys
from pathlib import Path

STYLE = (
    "Minecraft-style voxel world. Every object is built from uniform 1-meter cubic "
    "blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid "
    "seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, "
    "no bevels, no sculpted detail. Rendered as a game screenshot through a modern "
    "shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp "
    "saturated colours, smooth sky gradient, light atmospheric haze on the far "
    "background. No HUD, no crosshair, no hotbar, no interface, no hands, no held "
    "items, no text, no watermark, no signature."
)

NEGATIVE = (
    "smooth surfaces, rounded edges, curved walls, realistic geometry, photorealism, "
    "low-poly non-cubic shapes, sculpted terrain, HUD, crosshair, hotbar, inventory, "
    "user interface, text, letters, numbers, watermark, signature, logo, blurry, "
    "fisheye, distorted perspective, tilted horizon, changed art style"
)

CAMERAS = {
    "A": (
        "Fixed camera on a locked tripod, wide establishing shot from a slightly elevated "
        "position on the flat east bank of a great river. The river runs across the lower "
        "third of the frame from the left edge to the right. Beyond it rises a wooded "
        "escarpment: a long steep bluff whose crest sits at 45% of frame height. The "
        "flattest point of that crest is dead centre of the frame. Low forested hills "
        "close the far background. 35mm equivalent field of view, no lens distortion, "
        "horizon perfectly level. Midday sun from the upper left, long soft shadows "
        "falling to the lower right. 16:9.\n"
        "NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the "
        "lower left, the solitary oak on the crest at the right third."
    ),
    "B": (
        "Fixed camera on a locked tripod, medium-wide shot from the same direction as "
        "before but closer and slightly higher. The escarpment crest fills the middle band "
        "of the frame; the river shows only as a strip along the bottom edge. The ducal "
        "seat stands at the centre of the crest, the town spreads to the left. Horizon at "
        "35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.\n"
        "NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line."
    ),
    "C": (
        "Fixed camera at standing eye level in the middle of an open cobbled city square. "
        "A tall free-standing column with a statue on top stands at the centre-left of the "
        "frame. The bulk of the royal residence closes the right half. A gate and the "
        "rooflines of the old town close the left. Sky occupies the top third. Horizon at "
        "55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.\n"
        "NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern "
        "of the square, the lime tree at the right edge of the square."
    ),
    "D": (
        "Fixed camera at standing eye level, facing the royal residence head-on across the "
        "cobbled square. The facade and its clock tower fill the right two-thirds; the "
        "column stands at the left third with its statue against open sky. Horizon at 60% "
        "of frame height. 35mm equivalent, level horizon. 16:9.\n"
        "NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at "
        "the right edge."
    ),
}

PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}

REFRAME = (
    "Same world, same buildings, same time of day and same art style as the reference "
    "image — only the camera is repositioned, exactly as described above. Nothing in the "
    "world is added, removed or rebuilt in this step."
)

NOTES = {
    1: "Вход: ничего. Единственный кадр, который генерится с нуля (text-to-image).\n"
       "Это мастер-плита группы A — от неё зависят все 74 остальных кадра.\n"
       "Сгенерить 10-20 вариантов и выбрать вдумчиво, переделать потом = переделать всё.",
    19: "Вход: кадр 18. СМЕНА РАКУРСА — мастер-плита группы B.\n"
        "Сначала только переставить камеру (мир не трогать), результат сохранить\n"
        "как плиту B, и уже от неё вести цепочку дальше.",
    35: "Вход: кадр 34. СМЕНА РАКУРСА — мастер-плита группы C.\n"
        "ВАЖНО: сначала отдельным шагом сгенерить МИРНЫЙ кадр 1650 года по камере C\n"
        "и сохранить его как плиту C. И уже этот мирный кадр разрушать промптом ниже —\n"
        "иначе пара «до/после» не сработает, зрителю нужно узнать те же здания.",
    51: "Вход: кадр 50. СМЕНА РАКУРСА — мастер-плита группы D.\n"
        "Сначала только переставить камеру, результат сохранить как плиту D.",
}

HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")
BODY = re.compile(r"^\*\*(EDIT|SCENE):\*\* `(.+)`$")


def parse(src):
    frames, cur = [], None
    for line in src.read_text(encoding="utf-8").splitlines():
        if m := HEAD.match(line):
            cur = {"n": int(m[1]), "year": m[2].strip(), "title": m[3].strip()}
        elif (m := BODY.match(line)) and cur:
            frames.append({**cur, "body": m[2].replace("**", "")})
            cur = None
    return frames


def main():
    base = Path(__file__).resolve().parent.parent / "analysis" / "through-the-years-minecraft"
    frames = parse(base / "prompts-warsaw.md")

    if len(frames) != 75:
        sys.exit(f"ожидалось 75 кадров, разобрано {len(frames)} — проверь разметку источника")

    out = [
        "# Промпты картинок — 75 готовых блоков",
        "",
        "Сгенерировано `tools/image_prompts.py` из `prompts-warsaw.md`.",
        "",
        "Каждый блок — **целый промпт**: стиль, камера и инструкция кадра уже внутри.",
        "Копировать целиком и вставлять, дописывать ничего не нужно.",
        "",
        "**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:",
        "",
        "```",
        NEGATIVE,
        "```",
        "",
        "Кадр 1 генерится с нуля. Кадры 2-75 — правкой предыдущего кадра",
        "(инструкционное редактирование, не text-to-image).",
        "После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.",
        "",
        "---",
        "",
    ]

    plate = None
    for f in frames:
        n = f["n"]
        p = next(v for k, v in sorted(PLATES.items(), reverse=True) if n >= k)
        if p != plate:
            plate = p
            out += [f"# ГРУППА {plate}", ""]

        out += [f"### Кадр {n} · {f['year']} · {f['title']}", ""]
        out += [f"> {NOTES[n].replace(chr(10), chr(10) + '> ')}", ""] if n in NOTES \
            else [f"> Вход: кадр {n - 1} + мастер-плита группы {plate}.", ""]

        parts = [STYLE, "", CAMERAS[plate], ""]
        if n in (19, 51):
            parts += [REFRAME]
        else:
            parts += [f["body"]]

        out += ["```", *parts, "```", ""]

    (base / "image-prompts-warsaw.md").write_text("\n".join(out), encoding="utf-8")
    print(f"собрано блоков: {len(frames)}")


if __name__ == "__main__":
    main()
