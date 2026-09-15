#!/usr/bin/env python3
"""Прожигает год и подпись эпохи в готовые клипы переходов.

  python3 tools/burn_years.py --titles analysis/times-square/titles-times-square.csv \
      --clips ./flow-out --out ./labelled

В клипе перехода N→N+1 год меняется прямо внутри клипа: первые ~80% времени
стоит год N, дальше год N+1. При склейке подпись перещёлкивается ровно там, где
меняется сцена, и отдельная дорожка титров в монтажке не нужна.

Генератору год показывать не нужно: цифры он искажает, а здесь они одинаковые
во всех клипах и стоят точно на месте.
"""

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
MARGIN = 0.055        # отступ от краёв кадра
YEAR_H = 0.085        # высота цифр в долях высоты кадра
ERA_H = 0.036         # высота подписи эпохи
GAP = 0.018           # зазор между строками


def esc(s):
    """Экранирует текст для фильтра drawtext."""
    return s.replace("\\", r"\\\\").replace(":", r"\:").replace("'", r"\'").replace("%", r"\%")


def natural(p):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-show_entries", "format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    st = d["streams"][0]
    return st["width"], st["height"], float(d["format"]["duration"])


def layer(text, size, x, y, start=None, end=None):
    f = (f"drawtext=fontfile={FONT}:text='{esc(text)}':fontcolor=white"
         f":fontsize={size}:x={x}:y={y}")
    if start is not None or end is not None:
        cond = []
        if start is not None:
            cond.append(f"gte(t\\,{start:.3f})")
        if end is not None:
            cond.append(f"lt(t\\,{end:.3f})")
        f += ":enable='" + "*".join(cond) + "'"
    return f


def build_filter(h, switch, before, after):
    """Две пары строк: до переключения и после. Обе прижаты к правому верху."""
    ys, es, gap, m = int(h * YEAR_H), int(h * ERA_H), int(h * GAP), int(h * MARGIN)
    top = m
    parts = []
    for (year, era), a, b in ((before, None, switch), (after, switch, None)):
        parts.append(layer(year, ys, f"w-tw-{m}", top, a, b))
        if era:
            parts.append(layer(era, es, f"w-tw-{m}", top + ys + gap, a, b))
    return ",".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--titles", required=True, help="titles-*.csv с колонками year и era")
    ap.add_argument("--clips", required=True, help="папка с клипами переходов")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lead", default=None,
                    help="отдельный клип первого кадра, если он есть")
    ap.add_argument("--switch", type=float, default=0.8,
                    help="доля клипа, после которой год меняется на следующий")
    ap.add_argument("--glob", default="*.mp4")
    ap.add_argument("--no-era", action="store_true", help="только год, без подписи эпохи")
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg не найден в PATH")

    with open(a.titles, encoding="utf-8") as f:
        rows = [(r["year"], "" if a.no_era else r["era"]) for r in csv.DictReader(f)]

    clips = sorted(Path(a.clips).glob(a.glob), key=natural)
    need = len(rows) - 1
    if len(clips) != need:
        sys.exit(f"кадров в таблице {len(rows)}, значит переходов нужно {need}, "
                 f"а клипов найдено {len(clips)} — проверь папку и маску")

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    jobs = []
    if a.lead:
        jobs.append((Path(a.lead), rows[0], rows[0], out / f"00-{rows[0][0]}.mp4"))
    for i, clip in enumerate(clips):
        jobs.append((clip, rows[i], rows[i + 1],
                     out / f"{i + 1:02d}-{rows[i][0]}-{rows[i + 1][0]}.mp4"))

    for src, before, after, dst in jobs:
        _, h, dur = probe(src)
        vf = build_filter(h, dur * a.switch, before, after)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
             "-vf", vf, "-c:a", "copy", "-c:v", "libx264", "-crf", "16",
             "-preset", "medium", "-pix_fmt", "yuv420p", str(dst)],
            check=True)
        print(f"  {dst.name}   {before[0]} → {after[0]}")

    print(f"\nготово: {len(jobs)} файлов в {out}")


if __name__ == "__main__":
    main()
