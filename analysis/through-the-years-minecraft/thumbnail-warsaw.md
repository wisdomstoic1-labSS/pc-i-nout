# Превью — разбор конкурентов и промпты под Варшаву

## 1. Формула, снятая с двух превью

Оба превью (Токио и Берлин) собраны по одной жёсткой схеме. Отклоняться от неё не нужно — она и есть узнаваемость ниши.

| Элемент | Как сделано |
|---|---|
| Композиция | вертикальный сплит ровно 50/50 |
| Разделитель | белая полоса ~6 px по центру |
| Левая половина | старый год |
| Правая половина | 2026 |
| Ракурс | **уровень глаз, обе половины с одной точки** — в берлинском превью колоннада видна в обеих |
| Флаг | диагональный угол сверху; у Токио слева, у Берлина справа |
| Годы | огромные белые цифры внизу, левая у левого края, правая у правого |
| Шрифт | тяжёлый геометрический гротеск, лёгкая тень |
| Свет | яркий день, голубое небо, блочные облака |
| Интерфейс | отсутствует полностью |

Два наблюдения, которые важнее остального:

**Обе половины — одно место с одной точки.** В берлинском превью это видно прямо: те же колонны, тот же угол, слева трамвай и старые дома, справа телебашня и зелень. Это тот же приём, что и в самом ролике, — и именно он делает превью читаемым за полсекунды.

**Оба конкурента взяли 1926 vs 2026.** Ровно сто лет. Цифры симметричные и мгновенно понятные.

---

## 2. Какие годы брать нам

**Рекомендация: 1945 vs 2026.**

В ленте, где все превью ниши показывают «старый город против нового», единственное превью с **руинами** слева — это разрыв шаблона. Плюс это буквально уникальная история Варшавы: 85% разрушено и отстроено заново. Контраст «серые развалины / живой цветной город» на маленьком превью читается сильнее, чем «старые дома / новые дома».

Кадры для него уже есть в ролике: **64 (1945) и 73 (2026)** — обе из группы D, то есть с одной точки. Совпадение ракурса получается само.

**A/B-партнёр: 1926 vs 2026.** Безопасный, дословно повторяет схему конкурентов, симметричные цифры. Имеет смысл выкатить вторым вариантом и сравнить CTR.

| Вариант | Слева | Справа | Ставка |
|---|---|---|---|
| **A** (основной) | 1945, руины | 2026, живой город | разрыв шаблона в ленте |
| **B** (контроль) | 1926, довоенный город | 2026 | точное попадание в норму ниши |

---

## 3. Промпты

Генерить **две половины отдельно**, не одной картинкой: модель не удержит сплит и всё равно наврёт в границе. Формат каждой половины — **квадрат 1:1**, дальше инструмент сам обрежет по центру до 8:9.

В промптах нет ни года, ни флага, ни единой буквы — всё это накладывается скриптом. Модель врёт в цифрах и в пропорциях флага, доверять ей это нельзя.

Блок стиля — тот же, что во всём ролике. Иначе превью не сойдётся с содержимым.

### 3.1 Левая половина — 1945

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic
blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid
seams on every face. No smooth curves, no rounded shapes, no organic silhouettes,
no bevels, no sculpted detail. Rendered as a game screenshot through a modern
shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp
saturated colours, smooth sky gradient, light atmospheric haze on the far
background. No HUD, no crosshair, no hotbar, no interface, no hands, no held
items, no text, no watermark, no signature.

Eye-level view across a ruined cobbled city square in a destroyed European
capital in 1945. In the right half of the frame stands the burnt-out shell of a
large royal palace: roof gone, upper floors collapsed, empty black window holes,
one jagged corner tower still standing tall enough to read as a silhouette. A
tall stone column with a statue lies broken across the foreground rubble, its
sculpted figure face down on the cobbles. Mounds of broken brick fill the square.
A blackened tree stump at the right edge. Thin cold smoke, drifting ash, patches
of snow. Overcast winter sky, desaturated grey-brown palette, no fires.
Composition: strong readable silhouettes against the sky, the lower third of the
frame kept simple and dark. Square 1:1 composition.
```

### 3.2 Правая половина — 2026

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic
blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid
seams on every face. No smooth curves, no rounded shapes, no organic silhouettes,
no bevels, no sculpted detail. Rendered as a game screenshot through a modern
shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp
saturated colours, smooth sky gradient, light atmospheric haze on the far
background. No HUD, no crosshair, no hotbar, no interface, no hands, no held
items, no text, no watermark, no signature.

Eye-level view across the SAME cobbled city square, fully rebuilt and alive in
2026, from the exact same camera position and the same angle. In the right half
of the frame stands the restored royal palace: warm terracotta and cream facade,
green copper roof, the corner clock tower complete and standing in the same
place as the ruined one. The tall stone column stands upright and whole at the
left, its statue against open sky. Colourful restored townhouses close the left
edge. A big leafy lime tree at the right edge. Outdoor cafe tables, tourists,
flower stalls, a modern glass skyscraper cluster far behind the rooflines.
Bright summer day, deep blue sky with blocky white clouds, rich saturated
colours. Composition: strong readable silhouettes against the sky, the lower
third of the frame kept simple. Square 1:1 composition.
```

### 3.3 Негатив для обеих

```
smooth surfaces, rounded edges, curved walls, realistic geometry, photorealism,
low-poly non-cubic shapes, HUD, crosshair, hotbar, user interface, text, letters,
numbers, watermark, signature, logo, flag, split screen, collage, border, frame,
blurry, fisheye, distorted perspective, tilted horizon
```

`split screen, collage, border, frame` в негативе обязательны: без них модель регулярно сама рисует сплит внутри половины.

### 3.4 Вариант B — левая половина 1926

Тот же блок стиля, дальше:

```
Eye-level view across a cobbled city square in a European capital in 1926. In the
right half of the frame stands a large royal palace with a cream neoclassical
facade, green copper roof and a corner clock tower. A tall stone column with a
statue stands at the left against open sky. An old red tram on rails crosses the
foreground, gas street lamps on iron posts, people in long coats and hats,
a horse cart. Grey overcast morning, muted period palette, no modern objects
of any kind. Composition: strong readable silhouettes against the sky, the lower
third of the frame kept simple. Square 1:1 composition.
```

---

## 4. Сборка

```bash
python3 tools/miniatura.py L.png R.png thumb.png 1945 2026 --flag pl --flag-corner tl
```

Скрипт делает: сплит 50/50, белый разделитель 6 px, годы в нижней трети, флаг диагональным углом.

**Флаг: проверено на готовых картинках — лучше правый верхний угол (`tr`).**
Изначально я поставил левый, опасаясь, что белая полоса польского флага утонет в
светлом небе. На сгенерированных кадрах вышло наоборот: насыщенное синее небо
половины 2026 держит белое лучше, чем блёклое сепийное небо руин. Оба варианта
собраны, `warsaw-A-tr.png` и `warsaw-A-tl.png` — смотреть и выбирать глазами,
на других кадрах баланс может смениться.

Обрезка половин задаётся ключами `--anchor-left` и `--anchor-right`
(0 левый край, 0.5 центр, 1 правый). Нужны потому, что генератор ставит
ключевой объект не по центру: в кадре 2026 колонна стоит у левого края и при
центральной обрезке вылетала из превью. Рабочие значения: `0.50` и `0.36`.

Ключи: `--flag pl|de|jp|ua|cz`, `--flag-corner tl|tr`, `--no-flag`, `--font ПУТЬ`,
`--anchor-left`, `--anchor-right`.

### Что уже сделано

Обе половины сгенерированы через vidIQ (`vidiq_generate_thumbnail`, 16:9,
референс — превью берлинского ролика) и лежат в `thumbnails/`:

| Файл | Что |
|---|---|
| `warsaw-half-1945.png` | сырая левая половина |
| `warsaw-half-2026.png` | сырая правая половина |
| `warsaw-A-tr.png` | готовое превью, флаг справа |
| `warsaw-A-tl.png` | готовое превью, флаг слева |

Команда сборки:

```bash
python3 tools/miniatura.py \
  thumbnails/warsaw-half-1945.png thumbnails/warsaw-half-2026.png \
  thumbnails/warsaw-A-tr.png 1945 2026 \
  --flag pl --flag-corner tr --anchor-left 0.50 --anchor-right 0.36
```

**Про оценку vidIQ.** Скорер выставил половинам 24 и 36 из 100 с замечанием
«сравнение непонятно, используйте сплит-скрин». Он оценивал каждую половину
как самостоятельное превью и просил ровно то, что из них потом и собрано.
На готовом превью эта оценка смысла не имеет, гнаться за ней не нужно.

---

## 5. Что проверить перед публикацией

- [ ] Обе половины — одна точка съёмки: колонна и башня палаца на одной высоте и примерно на том же месте
- [ ] Линия горизонта совпадает по обе стороны разделителя
- [ ] На сгенерированных картинках нет ни одной буквы и цифры
- [ ] Превью читается в размере 210×118 px (лента мобильного) — открыть уменьшенным и посмотреть
- [ ] Годы не наезжают на важные силуэты
- [ ] Белая полоса флага не сливается с фоном

---

## 6. Побочное: битые шрифты в репозитории

`fonts/Anton.ttf` — это JSON на 378 байт, `fonts/Oswald.ttf` — HTML-страница на 1.6 КБ. При скачивании сохранились страницы ошибок вместо самих шрифтов. `plaszka.py` этого не замечает, потому что в нём жёстко прописан DejaVu.

`miniatura.py` битые файлы отсеивает и берёт следующий рабочий из списка, поэтому работает и сейчас — но на Liberation Sans, а не на том шрифте, который был задуман.

Точное попадание в шрифт конкурентов даёт **Poppins ExtraBold** или **Montserrat Black** — широкий геометрический гротеск. Скачать настоящий файл, положить в `fonts/` и передать через `--font fonts/Poppins-ExtraBold.ttf`.
