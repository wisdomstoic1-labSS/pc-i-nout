#!/usr/bin/env python3
"""Собирает готовые к вставке промпты оживления из prompts-warsaw.md.

Источник правды — сам файл промптов: скрипт вытаскивает из него строки MOTION
и склеивает каждую с блоком MOTION LOCK. Правишь движение в prompts-warsaw.md,
перезапускаешь скрипт — оба файла остаются согласованными.
"""

import re
import sys
from pathlib import Path

LOCK = (
    "Static locked-off camera on a tripod. Absolutely no camera movement: no zoom, no "
    "pan, no tilt, no dolly, no truck, no orbit, no parallax, no handheld shake, no "
    "rack focus. The framing is identical in the first and the last frame. All "
    "architecture, terrain and the skyline hold their exact shape — nothing morphs, "
    "melts, grows, or disappears. Motion is slow, subtle and ambient only."
)

NEGATIVE = (
    "camera movement, camera pan, camera zoom, dolly, orbit, parallax, shaking, "
    "morphing buildings, changing architecture, warping geometry, melting structures, "
    "objects appearing or disappearing, style change, text, watermark"
)

PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}
HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")
MOTION = re.compile(r"^\*\*MOTION:\*\* `(.+)`$")


def parse(src):
    frames, cur = [], None
    for line in src.read_text(encoding="utf-8").splitlines():
        if m := HEAD.match(line):
            cur = {"n": int(m[1]), "year": m[2].strip(), "title": m[3].strip()}
        elif (m := MOTION.match(line)) and cur:
            frames.append({**cur, "motion": m[1]})
            cur = None
    return frames


def main():
    base = Path(__file__).resolve().parent.parent / "analysis" / "through-the-years-minecraft"
    frames = parse(base / "prompts-warsaw.md")

    if len(frames) != 75:
        sys.exit(f"ожидалось 75 кадров, разобрано {len(frames)} — проверь разметку источника")

    out = [
        "# Промпты оживления — 75 готовых блоков",
        "",
        "Сгенерировано `tools/motion_prompts.py` из `prompts-warsaw.md`.",
        "",
        "Каждый блок ниже — **целый промпт**, включая MOTION LOCK. Собирать ничего не нужно:",
        "берёшь картинку кадра, вставляешь блок в image-to-video, генеришь.",
        "",
        "**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:",
        "",
        "```",
        NEGATIVE,
        "```",
        "",
        "Длительность клипа — **8 секунд** (кадр 1 — 4 секунды).",
        "Если модель не умеет 8 с, генерь максимум и подрезай; тянуть ретаймингом",
        "допустимо только вверх и не больше чем в полтора раза.",
        "",
        "---",
        "",
    ]

    plate = None
    for f in frames:
        if (p := next(v for k, v in sorted(PLATES.items(), reverse=True) if f["n"] >= k)) != plate:
            plate = p
            out += [f"# ГРУППА {plate}", ""]

        dur = "4 секунды" if f["n"] == 1 else "8 секунд"
        out += [
            f"### Кадр {f['n']} · {f['year']} · {f['title']} — {dur}",
            "",
            "```",
            LOCK,
            "",
            f["motion"],
            "```",
            "",
        ]

    (base / "motion-prompts-warsaw.md").write_text("\n".join(out), encoding="utf-8")
    print(f"собрано блоков: {len(frames)}")


if __name__ == "__main__":
    main()
