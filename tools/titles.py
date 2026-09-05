#!/usr/bin/env python3
"""Генерирует титры для ролика «Through the Years: Warsaw».

Раскладка: кадр 1 = 4 с, кадры 2-75 = по 8 с. Итого 596 с (9:56).
На выходе: markdown-таблица, CSV и три SRT (совмещённый, только годы,
только подписи эпох) — SRT импортируется в монтажку и расставляет титры сам.
"""

from pathlib import Path

FIRST = 4.0   # длительность первого кадра
STEP = 8.0    # длительность остальных

# (год на экране, подпись EN, подпись PL)
FRAMES = [
    ("8000 BC", "Ice Age Valley",        "Dolina polodowcowa"),
    ("3000 BC", "Primeval Forest",       "Puszcza pierwotna"),
    ("1500 BC", "First Clearing",        "Pierwsza polana"),
    ("700 BC",  "Lusatian Settlement",   "Osada łużycka"),
    ("100 AD",  "The Amber Route",       "Szlak bursztynowy"),
    ("400",     "Abandoned",             "Opuszczona"),
    ("700",     "Slavic Settlement",     "Osada słowiańska"),
    ("900",     "The Stronghold",        "Gród"),
    ("1000",    "The First Cross",       "Pierwszy krzyż"),
    ("1100",    "The Bridge",            "Most"),
    ("1180",    "The Mill",              "Młyn"),
    ("1230",    "Jazdów",                "Jazdów"),
    ("1262",    "Raided",                "Najazd"),
    ("1281",    "Burnt Again",           "Znów spalony"),
    ("1300",    "Warszowa",              "Warszowa"),
    ("1330",    "Town Charter",          "Prawa miejskie"),
    ("1350",    "First Brick",           "Pierwsza cegła"),
    ("1370",    "The Town Walls",        "Mury miejskie"),
    ("1380",    "Brick Town",            "Miasto z cegły"),
    ("1400",    "The Collegiate",        "Kolegiata"),
    ("1408",    "New Town",              "Nowe Miasto"),
    ("1413",    "Capital of Masovia",    "Stolica Mazowsza"),
    ("1450",    "Gothic",                "Gotyk"),
    ("1480",    "The Barbican",          "Barbakan"),
    ("1526",    "Into the Crown",        "Wcielenie do Korony"),
    ("1550",    "Renaissance",           "Renesans"),
    ("1569",    "The Sejm",              "Sejm walny"),
    ("1573",    "The Confederation",     "Konfederacja warszawska"),
    ("1596",    "The Court Arrives",     "Przeniesienie dworu"),
    ("1611",    "Royal Residence",       "Rezydencja królewska"),
    ("1620",    "Baroque",               "Barok"),
    ("1637",    "Expansion",             "Rozbudowa"),
    ("1644",    "The Column",            "Kolumna Zygmunta"),
    ("1650",    "Golden Age",            "Złoty wiek"),
    ("1655",    "The Deluge",            "Potop szwedzki"),
    ("1660",    "Empty",                 "Miasto puste"),
    ("1680",    "Slow Rebuild",          "Powolna odbudowa"),
    ("1700",    "Baroque Restored",      "Barok odbudowany"),
    ("1720",    "The Saxon Era",         "Czasy saskie"),
    ("1740",    "The Lime Tree",         "Lipa na rynku"),
    ("1764",    "Enlightenment",         "Oświecenie"),
    ("1780",    "Neoclassical",          "Klasycyzm"),
    ("1791",    "Constitution Day",      "Konstytucja 3 maja"),
    ("1794",    "Kościuszko Uprising",   "Insurekcja kościuszkowska"),
    ("1795",    "The Third Partition",   "III rozbiór"),
    ("1807",    "Duchy of Warsaw",       "Księstwo Warszawskie"),
    ("1815",    "Congress Kingdom",      "Królestwo Kongresowe"),
    ("1831",    "November Uprising",     "Powstanie listopadowe"),
    ("1866",    "Horse Trams",           "Tramwaj konny"),
    ("1890",    "Tenements",             "Kamienice"),
    ("1900",    "Belle Époque",          "Belle Époque"),
    ("1908",    "Electric Trams",        "Tramwaj elektryczny"),
    ("1914",    "War Begins",            "Wybuch wojny"),
    ("1915",    "Under Occupation",      "Okupacja niemiecka"),
    ("1918",    "Independence",          "Niepodległość"),
    ("1920",    "Battle of Warsaw",      "Bitwa Warszawska"),
    ("1926",    "Recovery",              "Odbudowa"),
    ("1933",    "The Skyscraper",        "Prudential"),
    ("1938",    "The Last Summer",       "Ostatnie lato"),
    ("1939",    "The Bombing",           "Oblężenie Warszawy"),
    ("1940",    "Occupied City",         "Miasto okupowane"),
    ("1943",    "Razed",                 "Zrównane z ziemią"),
    ("1944",    "Warsaw Uprising",       "Powstanie Warszawskie"),
    ("1945",    "85% Destroyed",         "85% zniszczone"),
    ("1947",    "Clearing the Rubble",   "Odgruzowywanie"),
    ("1953",    "Rebuilt from Paintings", "Odbudowa wg Canaletta"),
    ("1955",    "The Palace",            "Pałac Kultury"),
    ("1965",    "Concrete",              "Wielka płyta"),
    ("1980",    "Solidarity",            "Solidarność"),
    ("1989",    "Transformation",        "Transformacja"),
    ("2000",    "Glass",                 "Szkło"),
    ("2015",    "Skyline",               "Panorama"),
    ("2026",    "Present Day",           "Dzisiaj"),
    ("2050",    "Green Future",          "Zielona przyszłość"),
    ("2075",    "The Last Frame",        "Ostatni kadr"),
]

PLATES = {1: "A", 19: "B", 35: "C", 51: "D"}
PAIRS = {14, 35, 60, 64}   # вторые кадры пар катастрофы


def spans():
    """(индекс, начало, конец) для каждого кадра."""
    t = 0.0
    for i, _ in enumerate(FRAMES, start=1):
        dur = FIRST if i == 1 else STEP
        yield i, t, t + dur
        t += dur


def tc(sec, sep=","):
    """Секунды -> HH:MM:SS,mmm"""
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def short(sec):
    """Секунды -> M:SS для таблицы."""
    return f"{int(sec) // 60}:{int(sec) % 60:02d}"


def write_srt(path, line_fn):
    out = []
    for i, start, end in spans():
        out.append(f"{i}\n{tc(start)} --> {tc(end)}\n{line_fn(FRAMES[i - 1])}\n")
    path.write_text("\n".join(out), encoding="utf-8")


def main():
    base = Path(__file__).resolve().parent.parent / "analysis" / "through-the-years-minecraft"
    base.mkdir(parents=True, exist_ok=True)

    write_srt(base / "titles-warsaw.srt",      lambda f: f"{f[0]}\n{f[1]}")
    write_srt(base / "titles-warsaw-year.srt",  lambda f: f[0])
    write_srt(base / "titles-warsaw-era.srt",   lambda f: f[1])

    rows = ["frame,tc_in,tc_out,duration_s,plate,year,era_en,era_pl,catastrophe"]
    for i, start, end in spans():
        year, en, pl = FRAMES[i - 1]
        plate = next(p for k, p in sorted(PLATES.items(), reverse=True) if i >= k)
        rows.append(
            f'{i},{tc(start, ".")},{tc(end, ".")},{end - start:.0f},{plate},'
            f'"{year}","{en}","{pl}",{"yes" if i in PAIRS else ""}'
        )
    (base / "titles-warsaw.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")

    md = [
        "# Титры — Варшава, 75 кадров",
        "",
        "Сгенерировано `tools/titles.py`. Кадр 1 — 4 с, кадры 2–75 — по 8 с. Итого **596 с = 9:56**.",
        "",
        "Титр меняется ровно на границе кадров, то есть в середине секундного диссолва — так же, как в референсе.",
        "",
        "Готовые файлы для импорта в монтажку лежат рядом:",
        "",
        "| Файл | Для чего |",
        "|---|---|",
        "| `titles-warsaw-year.srt` | только годы — на верхний слой, крупным кеглем |",
        "| `titles-warsaw-era.srt` | только подписи эпох — на нижний слой, мелким |",
        "| `titles-warsaw.srt` | обе строки в одном титре — если верстать одним текстовым слоем |",
        "| `titles-warsaw.csv` | таблица со всеми полями, включая польские подписи |",
        "",
        "---",
        "",
        "| # | Вход | Выход | Длит. | Плита | Год | Подпись (EN) | Подпись (PL) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, start, end in spans():
        year, en, pl = FRAMES[i - 1]
        plate = next(p for k, p in sorted(PLATES.items(), reverse=True) if i >= k)
        mark = " 💥" if i in PAIRS else ""
        md.append(
            f"| {i} | {short(start)} | {short(end)} | {end - start:.0f} с | {plate} | "
            f"**{year}** | {en}{mark} | {pl} |"
        )
    md += [
        "",
        "💥 — второй кадр пары катастрофы. Первый кадр каждой пары: 13, 34, 59, 63.",
        "",
        "---",
        "",
        "## Оформление титра",
        "",
        "| Параметр | Значение |",
        "|---|---|",
        "| Позиция | правый верхний угол, отступ 8% от краёв |",
        "| Год | крупно, белая антиква |",
        "| Подпись эпохи | под годом, ~40% кегля года |",
        "| Обводка и тень | нет |",
        "| Анимация | нет — подмена мгновенная, на границе кадров |",
        "| Присутствие | весь ролик без пропусков |",
        "",
        "## Импорт SRT",
        "",
        "**DaVinci Resolve.** File → Import → Subtitle, положить дорожку над видео,",
        "выделить все клипы субтитров и задать шрифт, кегль и позицию разом.",
        "Для двух кеглей импортировать `-year` и `-era` на две отдельные дорожки.",
        "",
        "**Premiere Pro.** File → Import, выбрать .srt, затем Captions → Create captions",
        "from file. Стиль задаётся один раз в Essential Graphics и применяется ко всей дорожке.",
        "",
        "Если титры поедут — проверить частоту кадров проекта: SRT таймкодирован в реальных",
        "секундах, при 29.97 drop-frame возможен сдвиг. При 24, 25 и 30 fps сходится точно.",
    ]
    (base / "titles-warsaw.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    total = sum(e - s for _, s, e in spans())
    print(f"кадров: {len(FRAMES)}   итого: {total:.0f} с = {short(total)}")


if __name__ == "__main__":
    main()
