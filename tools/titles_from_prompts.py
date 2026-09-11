#!/usr/bin/env python3
"""Титры из файла сценария кадров.

  python3 tools/titles_from_prompts.py analysis/through-the-years-berlin/prompts-berlin.md

Годы и подписи эпох берутся из заголовков `### N · ГОД · Подпись`, поэтому
третьего списка заводить не нужно: правишь сценарий — титры едут следом.
Раскладка 4 с + N×8 с. На выходе таблица, CSV и три SRT.
"""

import argparse
import re
import sys
from pathlib import Path

FIRST, STEP = 4.0, 8.0
PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}
HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")


def parse(src):
    frames = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if m := HEAD.match(line):
            frames.append((int(m[1]), m[2].strip(), m[3].strip()))
    if [n for n, _, _ in frames] != list(range(1, len(frames) + 1)):
        sys.exit("нумерация кадров в источнике идёт не подряд")
    return frames


def spans(n):
    t = 0.0
    for i in range(1, n + 1):
        dur = FIRST if i == 1 else STEP
        yield i, t, t + dur
        t += dur


def tc(sec, sep=","):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def short(sec):
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def plate(i, single=False):
    return "A" if single else next(v for k, v in sorted(PLATES.items(), reverse=True) if i >= k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="файл сценария кадров, prompts-*.md")
    a = ap.parse_args()
    src = Path(a.source).resolve()
    text = src.read_text(encoding="utf-8")
    single = [p for p in "ABCD" if re.search(rf"^### CAMERA {p} ", text, re.M)] == ["A"]
    frames = parse(src)
    base, city = src.parent, src.stem.replace("prompts-", "")
    rows = list(spans(len(frames)))

    for suffix, line in [
        ("", lambda f: f"{f[1]}\n{f[2]}"),
        ("-year", lambda f: f[1]),
        ("-era", lambda f: f[2]),
    ]:
        out = [f"{i}\n{tc(s)} --> {tc(e)}\n{line(frames[i - 1])}\n" for i, s, e in rows]
        (base / f"titles-{city}{suffix}.srt").write_text("\n".join(out), encoding="utf-8")

    csv = ["frame,tc_in,tc_out,duration_s,plate,year,era"]
    md = [
        f"# Титры — {city.capitalize()}, {len(frames)} кадров",
        "",
        f"Сгенерировано `tools/titles_from_prompts.py` из `{src.name}`.",
        f"Кадр 1 — 4 с, остальные по 8 с. Итого **{int(rows[-1][2])} с = {short(rows[-1][2])}**.",
        "",
        "Титр меняется на границе кадров, то есть в середине секундного диссолва.",
        "SRT рядом: `-year` только годы, `-era` только подписи, без суффикса — обе строки.",
        "",
        "| # | Вход | Выход | Плита | Год | Подпись |",
        "|---|---|---|---|---|---|",
    ]
    for i, s, e in rows:
        _, year, era = frames[i - 1]
        csv.append(f'{i},{tc(s, ".")},{tc(e, ".")},{e - s:.0f},{plate(i, single)},"{year}","{era}"')
        md.append(f"| {i} | {short(s)} | {short(e)} | {plate(i, single)} | **{year}** | {era} |")

    (base / f"titles-{city}.csv").write_text("\n".join(csv) + "\n", encoding="utf-8")
    (base / f"titles-{city}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"кадров: {len(frames)}   итого: {int(rows[-1][2])} с = {short(rows[-1][2])}")


if __name__ == "__main__":
    main()
