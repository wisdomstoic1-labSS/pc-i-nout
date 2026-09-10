#!/usr/bin/env python3
"""Собирает цельные промпты картинок из файла сценария города.

  python3 tools/image_prompts.py analysis/through-the-years-berlin/prompts-berlin.md

Каждый блок на выходе — законченный промпт: стиль, камера, якоря и инструкция
кадра уже склеены. ВСЁ берётся из файла-источника, в скрипте не зашито ничего
привязанного к конкретному городу.
"""

import argparse
import re
import sys
from pathlib import Path

PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}

REFRAME = (
    "Same world, same buildings, same time of day and same art style as the reference "
    "image — only the camera is repositioned, exactly as described above. Nothing in the "
    "world is added, removed or rebuilt in this step."
)

HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")
BODY = re.compile(r"^\*\*(EDIT|SCENE):\*\* `(.+)`$")


def block_after(text, heading, what):
    """Содержимое первого ``` блока после заголовка."""
    m = re.search(heading + r".*?\n```\n(.*?)\n```", text, re.S | re.M)
    if not m:
        sys.exit(f"в источнике не найден блок: {what}")
    return m[1].strip()


def parse_frames(text):
    frames, cur = [], None
    for line in text.splitlines():
        if m := HEAD.match(line):
            cur = {"n": int(m[1]), "year": m[2].strip(), "title": m[3].strip()}
        elif (m := BODY.match(line)) and cur:
            frames.append({**cur, "body": m[2].replace("**", "")})
            cur = None
    return frames


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?",
                    default="analysis/through-the-years-minecraft/prompts-warsaw.md")
    ap.add_argument("out", nargs="?", default=None)
    a = ap.parse_args()

    src = Path(a.source).resolve()
    text = src.read_text(encoding="utf-8")

    style = block_after(text, r"^## БЛОК STYLE", "STYLE")
    negative = block_after(text, r"^\*\*NEGATIVE:\*\*", "NEGATIVE")
    cameras = {p: block_after(text, rf"^### CAMERA {p} ", f"CAMERA {p}") for p in "ABCD"}
    anchors = {k: block_after(text, rf"^### ANCHORS {k}$", f"ANCHORS {k}")
               for k in ("A", "B", "CD")}
    notes = {int(m[1]): m[2].strip().replace("\n", "\n> ")
             for m in re.finditer(r"^#### NOTE (\d+)\n(.*?)(?=\n#### |\n## |\n### |\Z)",
                                  text, re.S | re.M)}

    frames = parse_frames(text)
    if len(frames) != 75:
        sys.exit(f"ожидалось 75 кадров, разобрано {len(frames)}")

    city = src.stem.replace("prompts-", "")
    out = [
        f"# Промпты картинок — {city.capitalize()}, 75 готовых блоков",
        "",
        f"Сгенерировано `tools/image_prompts.py` из `{src.name}`.",
        "Стиль, камеры и якоря взяты из того же файла — правишь их там, перезапускаешь скрипт.",
        "",
        "Каждый блок — **целый промпт**. Копировать целиком, дописывать ничего не нужно.",
        "",
        "**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:",
        "", "```", negative, "```", "",
        "## Самое важное",
        "",
        "**Кадр 1 генерится с нуля. Кадры 2-75 — только правкой предыдущего кадра.**",
        "В Gemini это значит: прикрепить картинку предыдущего кадра и вставить блок.",
        "Без приложенной картинки модель будет каждый раз выдумывать объекты заново —",
        "это предел технологии, промптом он не обходится.",
        "",
        "После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.",
        "", "---", "",
    ]

    plate = None
    for f in frames:
        n = f["n"]
        p = next(v for k, v in sorted(PLATES.items(), reverse=True) if n >= k)
        if p != plate:
            plate = p
            out += [f"# ГРУППА {plate}", ""]

        out += [f"### Кадр {n} · {f['year']} · {f['title']}", ""]
        out += [f"> {notes[n]}", ""] if n in notes else \
               [f"> Вход: кадр {n - 1} + мастер-плита группы {plate}.", ""]

        out += ["```",
                "BASE IMAGE: none. This is the first frame of the series - generate it "
                "from scratch." if n == 1 else
                "BASE IMAGE: the previous frame is attached. Build this image by EDITING "
                "that image, not by drawing a new scene from scratch. Keep its camera "
                "position, framing, horizon line, perspective, lighting and every anchor "
                "object exactly as they already are. Change only what is listed under "
                "CHANGE below.",
                "", "STYLE:", style,
                "", "CAMERA:", cameras[plate],
                "", anchors["CD" if plate in ("C", "D") else plate],
                "", "CHANGE:", REFRAME if n in (19, 51) else f["body"],
                "```", ""]

    Path(a.out or src.parent / src.name.replace("prompts", "image-prompts")).write_text(
        "\n".join(out), encoding="utf-8")
    print(f"собрано блоков: {len(frames)}   город: {city}")


if __name__ == "__main__":
    main()
