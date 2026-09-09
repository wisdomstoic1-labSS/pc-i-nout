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

### Почему картинки не похожи на игру

Формулировка «Minecraft-style voxel world» читается моделью как «стилизованный
воксель-арт», а это другой жанр: гладкие скруглённые формы, запечённое освещение,
сколь угодно мелкая деталь. Отсюда все провалы. Что именно выдаёт подделку:

| Что не так | Как в игре на самом деле |
|---|---|
| Статуя вылеплена: доспех, складки плаща, лицо | Чурбаны из блоков, узнаётся только издали |
| Круглые купола и арки | Ступеньки из лестниц и плит, ступенчатый силуэт |
| Тонкие карнизы, наличники, лепнина | Ничего мельче одного блока не существует |
| Гладкие градиенты по поверхности | Каждая грань плоская, с грубой текстурой 16×16 |
| Плавные склоны рельефа | Рельеф поднимается ступенями в целый блок |
| Круглая стриженая крона дерева | Ствол 1×1 из брёвен, кубическое облако листвы |

Отсюда три приёма, которые чинят картинку:

1. **Просить скриншот, а не стиль.** `A raw in-game screenshot from Minecraft
   Java Edition, vanilla 16x16 textures` вместо `Minecraft-style`.
2. **Считать в блоках.** Не «четырёхэтажный дворец», а «40 блоков в длину,
   10 блоков до карниза». Числа привязывают модель к сетке.
3. **Называть настоящие блоки игры.** `oxidised copper`, `red terracotta`,
   `stone bricks`, `glass panes`, `spruce planks`. Это самый сильный сигнал:
   модель знает палитру Minecraft по названиям.

### Блок BLOCK RULES — вставлять в оба промпта дословно

```
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated
  with stairs and slabs, and the stair-stepping is clearly visible in the
  silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients across a surface, no baked
  sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a
  flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: red terracotta and bricks, smooth stone and
quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone
bricks, deepslate, cobblestone, glass panes.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.
```

### Блок якорей — вставлять в оба промпта дословно

```
ANCHOR OBJECTS - the SAME physical objects in both images, and every one of them
is a BUILD made of blocks, never a sculpture:

- THE COLUMN AND ITS STATUE: the column is a 2x2 shaft of smooth stone blocks,
  16 blocks tall, on a stepped stone-brick plinth 6 blocks wide. On top stands a
  crude blocky figure assembled from oxidised copper blocks, about 8 blocks
  tall: the body is a 2x1 column of blocks, each arm is a single 1x1 column of
  blocks, the head is one block with a small crown of copper stairs on it. The
  RIGHT arm holds a cross made of five blocks in a plus shape. The LEFT arm
  holds a sabre made of three blocks stepped diagonally. It reads as a crowned
  king only from a distance, exactly the way a player-built Minecraft statue
  does. NO face, NO armour detail, NO cloth folds, NO smooth curves, NO sculpted
  anatomy. NEVER an angel, an eagle, an orb, a globe, a woman or a soldier.

- THE PALACE: a rectangular building 40 blocks long and 10 blocks tall to the
  eaves, walls of red terracotta and brick blocks with smooth quartz corner
  columns. Windows are identical 1x2 glass-pane openings in a regular row. The
  roof is oxidised copper blocks and copper stairs in a simple stepped gable, no
  curves. One square clock tower 8 blocks wide rises 12 blocks above the roof,
  with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets at the roof ends.

- THE LIME TREE: one Minecraft tree at the right edge of the square - a straight
  1x1 trunk of oak logs with a blocky cloud of cubic leaf blocks above it.

In the ruined version these are still THESE builds in a damaged state: the same
block statue lying broken on the ground with its blocks scattered, the same
palace burnt out, the same tree reduced to a bare trunk. Never swap them for a
different design, and never make the ruins smooth or sculpted.
```

### 3.3 Негатив для обеих

```
smooth surfaces, curved walls, rounded domes, smooth arches, sculpted detail,
sub-block detail, carved ornament, thin mouldings, marble sculpture, realistic
statue, detailed face, cloth folds, sculpted anatomy, high-poly, realistic
geometry, photorealism, stylized voxel art, smooth gradients, soft rounded
edges, high resolution textures, smooth terrain slope, rounded topiary tree,
HUD, crosshair, hotbar, user interface, text, letters, numbers, watermark,
signature, logo, flag, split screen, collage, border, frame, blurry, fisheye,
distorted perspective, tilted horizon, different statue, different building,
angel statue, eagle statue, orb, globe
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
