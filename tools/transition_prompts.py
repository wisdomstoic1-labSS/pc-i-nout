#!/usr/bin/env python3
"""Промпты переходов для режима «первый кадр — последний кадр» (Google Flow).

  python3 tools/transition_prompts.py analysis/times-square/prompts-times-square.md

На N кадров получается N-1 переходов. Каждый описывает, как предыдущий кадр
превращается в следующий: сначала удержание, потом морфинг.

Механику перехода берём из строки `**TRANS:**` кадра-цели, если она есть.
Если её нет — собираем из строки `**EDIT:**`: что должно стать правдой в конце.
"""

import argparse
import re
import sys
from pathlib import Path

HOLD = """SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind."""

NEG = """camera movement, camera pan, camera zoom, dolly, orbit, parallax, shaking,
drifting framing, cross-fade, dissolve, melting, organic morphing, smooth
shape-shifting, warping geometry, buildings sliding sideways, changing art style,
text, letters, numbers, watermark, HUD, crosshair, hotbar"""

HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")
BODY = re.compile(r"^\*\*(EDIT|SCENE|TRANS):\*\* `(.+)`$")


def parse(text):
    frames, cur = [], None
    for line in text.splitlines():
        if m := HEAD.match(line):
            cur = {"n": int(m[1]), "year": m[2].strip(), "title": m[3].strip()}
            frames.append(cur)
        elif (m := BODY.match(line)) and cur is not None:
            cur[m[1].lower()] = m[2].replace("**", "")
    return frames


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("out", nargs="?", default=None)
    a = ap.parse_args()

    src = Path(a.source).resolve()
    text = src.read_text(encoding="utf-8")
    frames = parse(text)

    declared = re.search(r"^<!-- frames: (\d+) -->$", text, re.M)
    if declared and len(frames) != int(declared[1]):
        sys.exit(f"ожидалось {declared[1]} кадров, разобрано {len(frames)}")
    if [f["n"] for f in frames] != list(range(1, len(frames) + 1)):
        sys.exit("нумерация кадров идёт не подряд")

    city = src.stem.replace("prompts-", "")
    out = [
        f"# Промпты переходов — {city.replace('-', ' ').title()}, {len(frames) - 1} блоков",
        "",
        f"Сгенерировано `tools/transition_prompts.py` из `{src.name}`.",
        "",
        "Режим «первый кадр — последний кадр»: на вход два соседних кадра, на выходе",
        "клип, который превращает один в другой. Переходов на один меньше, чем кадров.",
        "",
        "Каждый клип: примерно две трети удержания, затем морфинг. Так сетка 8 секунд",
        "на эпоху сохраняется, и зритель успевает рассмотреть кадр до того, как он начнёт",
        "меняться.",
        "",
        "**Негатив у всех переходов одинаковый:**",
        "", "```", NEG, "```", "", "---", "",
    ]

    for prev, cur in zip(frames, frames[1:]):
        change = cur.get("trans") or (
            f"By the end of the clip the scene must match the last image exactly: "
            f"{cur.get('edit', cur.get('scene', ''))}"
        )
        out += [
            f"### Переход {prev['n']}→{cur['n']} · {prev['year']} → {cur['year']} · {cur['title']}",
            "",
            f"> Первый кадр: {prev['n']}. Последний кадр: {cur['n']}.",
            "",
            "```", HOLD, "", "THE CHANGE:", change, "```", "",
        ]

    dst = Path(a.out or src.parent / src.name.replace("prompts", "transition-prompts"))
    dst.write_text("\n".join(out), encoding="utf-8")
    print(f"переходов: {len(frames) - 1}   город: {city}")


if __name__ == "__main__":
    main()
