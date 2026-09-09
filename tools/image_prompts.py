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

ANCHORS = {
    "A": """ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.""",

    "B": """ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.""",

    "CD": """ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE: one tall round-shafted stone column of smooth grey-brown
  stone, standing on a square two-step stone plinth. On top stands ONE bronze statue
  of a crowned king: dark weathered green-bronze, in armour and a long cloak, holding
  a tall thin cross upright in his RIGHT hand and a curved sabre pointing downward in
  his LEFT hand. It is ALWAYS this same statue - same crown, same cross in the right
  hand, same sabre in the left, same green-bronze colour, same proportions, same
  height. NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a
  soldier, a horse, or any other figure.
- THE PALACE: a long rectangular palace, 4 storeys, warm terracotta-red brick walls
  with pale cream stone corner quoins and window frames, a steep green oxidised-copper
  roof. One square clock tower rises from the centre of the facade, with a round clock
  face on its front and a slim copper-green spire topped by a golden ball. Two smaller
  copper-domed turrets, one at each end of the roof. Always this exact building in
  this exact place.
- THE LIME TREE: one broad-crowned lime tree at the right edge of the square, in a
  small square stone surround. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.""",
}

BASE_FIRST = """BASE IMAGE: none. This is the first frame of the series - generate it from scratch."""

BASE_EDIT = """BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below."""


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
        "## Самое важное",
        "",
        "**Кадр 1 генерится с нуля. Кадры 2-75 — только правкой предыдущего кадра.**",
        "В Gemini это значит: прикрепить картинку предыдущего кадра к запросу и",
        "вставить блок промпта. Если генерить каждый кадр по одному тексту, без",
        "приложенной картинки, модель будет каждый раз выдумывать заново и статую,",
        "и здание — это предел технологии, промптом он не обходится.",
        "",
        "В каждом блоке есть раздел ANCHOR OBJECTS с точным описанием повторяющихся",
        "объектов: колонны со статуей короля, дворца с часовой башней, липы. Он",
        "нужен, чтобы модель не изобретала новую статую на каждом кадре. Не сокращать.",
        "",
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

        change = REFRAME if n in (19, 51) else f["body"]
        parts = [
            BASE_FIRST if n == 1 else BASE_EDIT, "",
            "STYLE:", STYLE, "",
            "CAMERA:", CAMERAS[plate], "",
            ANCHORS["CD" if plate in ("C", "D") else plate], "",
            "CHANGE:", change,
        ]
        out += ["```", *parts, "```", ""]

    (base / "image-prompts-warsaw.md").write_text("\n".join(out), encoding="utf-8")
    print(f"собрано блоков: {len(frames)}")


if __name__ == "__main__":
    main()
