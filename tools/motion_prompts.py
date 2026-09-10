#!/usr/bin/env python3
"""Собирает готовые к вставке промпты оживления из prompts-warsaw.md.

Источник правды — сам файл промптов: скрипт вытаскивает из него строки MOTION
и склеивает каждую с блоком MOTION LOCK. Правишь движение в prompts-warsaw.md,
перезапускаешь скрипт — оба файла остаются согласованными.
"""

import argparse
import re
import sys
from pathlib import Path

PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}
def block_after(text, heading, what):
    """Содержимое первого ``` блока после заголовка."""
    m = re.search(heading + r".*?\n```\n(.*?)\n```", text, re.S | re.M)
    if not m:
        sys.exit(f"в источнике не найден блок: {what}")
    return m[1].strip()


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
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?",
                    default="analysis/through-the-years-minecraft/prompts-warsaw.md",
                    help="файл-источник со сценарием кадров")
    ap.add_argument("out", nargs="?", default=None,
                    help="куда писать результат; по умолчанию рядом с источником")
    a = ap.parse_args()
    src = Path(a.source).resolve()
    base = src.parent
    text = src.read_text(encoding="utf-8")
    lock = block_after(text, r"^## MOTION LOCK", "MOTION LOCK")
    negative = block_after(text, r"^\*\*NEGATIVE:\*\*(?![\s\S]{0,40}smooth surfaces)",
                           "MOTION NEGATIVE")
    frames = parse(src)

    if len(frames) != 75:
        sys.exit(f"ожидалось 75 кадров, разобрано {len(frames)} — проверь разметку источника")

    out = [
        "# Промпты оживления — 75 готовых блоков",
        "",
        f"Сгенерировано `tools/motion_prompts.py` из `{src.name}`.",
        "",
        "Каждый блок ниже — **целый промпт**, включая MOTION LOCK. Собирать ничего не нужно:",
        "берёшь картинку кадра, вставляешь блок в image-to-video, генеришь.",
        "",
        "**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:",
        "",
        "```",
        negative,
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
            lock,
            "",
            f["motion"],
            "```",
            "",
        ]

    Path(a.out or base / src.name.replace("prompts", "motion-prompts")).write_text("\n".join(out), encoding="utf-8")
    print(f"собрано блоков: {len(frames)}")


if __name__ == "__main__":
    main()
