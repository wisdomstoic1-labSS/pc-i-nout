#!/usr/bin/env python3
"""Титры под раскладку «переходами», а не покадрово.

  python3 tools/titles_transitions.py analysis/times-square/prompts-times-square.md

В режиме «первый кадр — последний кадр» на таймлайне лежат не кадры, а клипы:
клип k держит кадр k и в последней трети превращает его в кадр k+1. Поэтому
титр живёт поперёк стыка клипов, а не внутри одного клипа, и покадровая
раскладка из titles_from_prompts.py тут не годится.

Год меняется в точке SWITCH от начала клипа — уже внутри морфинга, так что
смена года читается как причина изменения, а не как подпись к нему.

На выходе: таблица под монтаж, CSV, три SRT и голый столбик годов.
"""

import argparse
import re
import sys
from pathlib import Path

CLIP = 8.0      # длительность одного клипа, с
SWITCH = 0.8    # доля клипа, на которой год меняется на следующий
TAIL = 4.0      # сколько держать последний кадр после конца последнего клипа
HEAD = re.compile(r"^### (\d+) · (.+?) · (.+?)(?: — .*)?$")


def parse(src):
    frames = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if m := HEAD.match(line):
            frames.append((int(m[1]), m[2].strip(), m[3].strip()))
    if not frames:
        sys.exit(f"в источнике не найдено ни одного заголовка кадра: {src}")
    if [n for n, _, _ in frames] != list(range(1, len(frames) + 1)):
        sys.exit("нумерация кадров в источнике идёт не подряд")
    return frames


def tc(sec, sep=","):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def short(sec):
    m, s = divmod(sec, 60)
    return f"{int(m)}:{s:04.1f}".replace(".0", ".0")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="файл сценария кадров, prompts-*.md")
    ap.add_argument("--clip", type=float, default=CLIP)
    ap.add_argument("--switch", type=float, default=SWITCH)
    ap.add_argument("--tail", type=float, default=TAIL)
    a = ap.parse_args()

    src = Path(a.source).resolve()
    frames = parse(src)
    n = len(frames)
    base, city = src.parent, src.stem.replace("prompts-", "")

    # Границы титров. Первый год стоит от нуля, каждый следующий въезжает
    # в точке смены своего клипа и держится ровно один клип.
    cuts = [0.0] + [(k - 1) * a.clip + a.switch * a.clip for k in range(1, n)]
    total = (n - 1) * a.clip + a.tail
    spans = [(i + 1, cuts[i], cuts[i + 1] if i + 1 < n else total) for i in range(n)]

    for suffix, line in [
        ("", lambda f: f"{f[1]}\n{f[2]}"),
        ("-year", lambda f: f[1]),
        ("-era", lambda f: f[2]),
    ]:
        out = [f"{i}\n{tc(s)} --> {tc(e)}\n{line(frames[i - 1])}\n" for i, s, e in spans]
        (base / f"titles-{city}-clips{suffix}.srt").write_text("\n".join(out), encoding="utf-8")

    csv = ["clip,from_frame,to_frame,clip_in,clip_out,switch_at,year_before,year_after,era_after"]
    for k in range(1, n):
        ci, co = (k - 1) * a.clip, k * a.clip
        csv.append(
            f"{k},{k},{k + 1},{tc(ci, '.')},{tc(co, '.')},{tc(ci + a.switch * a.clip, '.')},"
            f'"{frames[k - 1][1]}","{frames[k][1]}","{frames[k][2]}"'
        )
    (base / f"titles-{city}-clips.csv").write_text("\n".join(csv) + "\n", encoding="utf-8")

    md = [
        f"# Годы под клипы — {city.replace('-', ' ').title()}",
        "",
        f"Сгенерировано `tools/titles_transitions.py` из `{src.name}`.",
        "",
        f"Кадров {n}, клипов {n - 1}. Клип {a.clip:.0f} с, хвост на последнем кадре "
        f"{a.tail:.0f} с. Итого **{total:.0f} с = {int(total) // 60}:{int(total) % 60:02d}**.",
        "",
        f"Год меняется на {a.switch * 100:.0f}% клипа, то есть в {a.switch * a.clip:.1f} с "
        f"от его начала — уже внутри морфинга. Поэтому титр всегда лежит поперёк стыка: "
        f"въезжает в конце одного клипа и уезжает в конце следующего.",
        "",
        "## Столбик годов",
        "",
        "Просто по порядку, кадр за кадром:",
        "",
        "```",
        *[f[1] for f in frames],
        "```",
        "",
        "## Титры на таймлайне",
        "",
        "Вот это и режется в монтаже: один титр = одна строка.",
        "",
        "| Кадр | Год | Подпись | Вход | Выход | Длит. |",
        "|---|---|---|---|---|---|",
    ]
    for i, s, e in spans:
        md.append(f"| {i} | **{frames[i - 1][1]}** | {frames[i - 1][2]} | "
                  f"{short(s)} | {short(e)} | {e - s:.1f} с |")
    md += [
        "",
        "## Клипы: что генерится и какой год на нём",
        "",
        "Номер клипа совпадает с номером перехода в файле промптов переходов.",
        "",
        "| Клип | Кадры | Клип в таймлайне | Год в начале | Смена | Год к концу |",
        "|---|---|---|---|---|---|",
    ]
    for k in range(1, n):
        ci = (k - 1) * a.clip
        md.append(f"| {k} | {k}→{k + 1} | {short(ci)} – {short(ci + a.clip)} | "
                  f"**{frames[k - 1][1]}** | {short(ci + a.switch * a.clip)} | "
                  f"**{frames[k][1]}** |")
    md += [
        "",
        f"Последний клип кончается на {short((n - 1) * a.clip)}. Дальше — стоп-кадр "
        f"{frames[-1][1]} на {a.tail:.0f} с, иначе последний год мелькнёт на "
        f"{a.clip - a.switch * a.clip:.1f} с и его никто не прочтёт.",
        "",
        "## Файлы рядом",
        "",
        f"- `titles-{city}-clips.srt` — год и подпись, две строки",
        f"- `titles-{city}-clips-year.srt` — только год",
        f"- `titles-{city}-clips-era.srt` — только подпись",
        f"- `titles-{city}-clips.csv` — по клипам, под таблицу",
        "",
    ]
    (base / f"titles-{city}-clips.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"кадров: {n}   клипов: {n - 1}   итого: {total:.0f} с = "
          f"{int(total) // 60}:{int(total) % 60:02d}")


if __name__ == "__main__":
    main()
