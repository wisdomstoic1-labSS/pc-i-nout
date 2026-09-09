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

### Порядок генерации — это главное

Не генерить обе половины по отдельности с нуля. Так модель каждый раз изобретает
новую статую и новое здание, и превью разваливается: слева один памятник, справа
другой.

Правильный порядок:

```
1. Сгенерировать половину 2026 с нуля — она самая детальная.
2. Выбрать удачный вариант.
3. Приложить эту картинку к запросу и попросить ПЕРЕДЕЛАТЬ её в 1945:
   те же здания, тот же ракурс, но в руинах.
```

Тогда разрушенный дворец гарантированно окажется тем же дворцом, а поваленная
статуя — той же статуей. На этом и держится приём «до/после».

### Блок якорей — вставлять в оба промпта дословно

```
ANCHOR OBJECTS - the SAME physical objects in both images. Never redesign them,
never invent a different version:
- THE COLUMN AND ITS STATUE: one tall round-shafted stone column of smooth
  grey-brown stone on a square two-step stone plinth. On top stands ONE bronze
  statue of a crowned king: dark weathered green-bronze, in armour and a long
  cloak, holding a tall thin cross upright in his RIGHT hand and a curved sabre
  pointing downward in his LEFT hand. ALWAYS this same statue - same crown, same
  cross in the right hand, same sabre in the left, same green-bronze colour, same
  proportions. NEVER replace it with an angel, an eagle, an orb, a globe, a woman,
  a soldier, a horse, or any other figure.
- THE PALACE: a long rectangular palace, 4 storeys, warm terracotta-red brick walls
  with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade,
  with a round clock face and a slim copper-green spire topped by a golden ball.
  Two smaller copper-domed turrets, one at each end of the roof.
- THE LIME TREE: one broad-crowned lime tree at the right edge of the square.

In the ruined version these are still THESE objects in a damaged state: the same
statue lying broken on the ground, the same palace burnt out, the same tree as a
charred stump. Never swap them for a different design.
```

### 3.1 Первая генерация — половина 2026

Блок стиля, затем блок якорей, затем:

```
ONE single continuous scene filling the whole frame. NO split screen, NO divider,
NO collage, NO before/after comparison, NO border, NO text, NO letters, NO numbers,
NO flag, NO logo.

Eye-level view across a cobbled city square in a European capital, fully rebuilt
and alive in 2026. The palace described above stands in the centre-right of the
frame, its clock tower a strong silhouette against the sky. The column with its
statue stands upright and whole at the left, against open sky. Colourful restored
townhouses close the left edge. The lime tree at the right edge. Outdoor cafe
tables, tourists, flower stalls, a cluster of modern glass skyscrapers far behind
the rooflines. Bright summer day, deep blue sky with blocky white clouds, rich
saturated colours.

COMPOSITION: keep the column and the clock tower in the central area of the frame,
the image will be cropped. Strong readable silhouettes against the sky.
```

### 3.2 Вторая генерация — половина 1945, правкой первой

**Приложить к запросу картинку 2026.** Блок стиля, блок якорей, затем:

```
BASE IMAGE: the 2026 square is attached. Build this image by EDITING that image.
Keep the camera position, the framing, the horizon line and the perspective
EXACTLY as they are. The buildings must stay recognisably the same buildings.

CHANGE: it is now 1945 and the city has been destroyed. The palace is a burnt-out
shell of the SAME building: roof gone, upper floors collapsed, empty black window
holes, but the corner clock tower still standing tall enough to recognise. The
SAME column has been toppled - it lies broken across the foreground rubble, and
the SAME crowned king statue lies face down on the cobbles, still holding its
cross and sabre. The townhouses on the left are hollow shells. The lime tree is a
blackened stump. Mounds of broken brick fill the square. Thin cold smoke, drifting
ash, patches of snow. Overcast winter sky, desaturated grey-brown palette, no
fires, no people.
```

### 3.3 Негатив для обеих

```
smooth surfaces, rounded edges, curved walls, realistic geometry, photorealism,
low-poly non-cubic shapes, HUD, crosshair, hotbar, user interface, text, letters,
numbers, watermark, signature, logo, flag, split screen, collage, border, frame,
blurry, fisheye, distorted perspective, tilted horizon, different statue,
different building, angel statue, eagle statue, orb, globe
```

`split screen, collage, border, frame` обязательны: без них модель регулярно
рисует сплит внутри одной половины. `different statue, angel statue, eagle statue,
orb, globe` — прямая страховка от подмены памятника.

### 3.4 Вариант B — половина 1926

Тоже правкой картинки 2026, с тем же блоком якорей:

```
BASE IMAGE: the 2026 square is attached. Keep the camera, framing, horizon and
perspective exactly. The palace, the column with its statue and the townhouses
stay the SAME buildings.

CHANGE: it is now 1926. Remove every modern object: no glass skyscrapers, no cafe
tables, no tourists in modern clothes, no flower stalls. An old red tram on rails
crosses the foreground, gas street lamps on iron posts, people in long coats and
hats, a horse cart. The facades are darker and soot-stained. Grey overcast
morning, muted period palette.
```

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

### Готовое превью

Обе половины сгенерированы в Gemini по промптам из §3 — сначала 2026 с нуля,
затем 1945 правкой этой картинки. Блок якорей сработал: статуя коронованного
короля в обеих половинах одна и та же, крест в правой руке, сабля в левой.

| Файл | Что |
|---|---|
| `thumbnails/warsaw-src-1945.png` | исходная половина, 2000×1091 |
| `thumbnails/warsaw-src-2026.png` | исходная половина, 2000×1091 |
| `thumbnails/warsaw-final-tr.png` | **готовое превью, флаг справа** |
| `thumbnails/warsaw-final-tl.png` | готовое превью, флаг слева |

```bash
python3 tools/miniatura.py \
  thumbnails/warsaw-src-1945.png thumbnails/warsaw-src-2026.png \
  thumbnails/warsaw-final-tr.png 1945 2026 \
  --flag pl --flag-corner tr --anchor-left 0.42 --anchor-right 0.34
```

**Про значения обрезки.** `0.42` и `0.34` подобраны не наугад: они ставят обе
статуи по разные стороны разделителя — поваленная у нижнего края левой половины,
стоящая во весь рост в правой. Читается как пара «упала / стоит», и это главный
смысловой узел превью.

При `0.48` и выше поваленная статуя заезжает под цифры «1945», и теряются оба
элемента сразу. Если будешь менять обрезку — следи, чтобы под годами оставалась
пустая брусчатка, как в превью конкурентов.

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
