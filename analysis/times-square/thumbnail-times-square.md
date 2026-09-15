# Превью Таймс-сквер — две пары «название + картинка»

Принцип: **название не повторяет превью, а договаривает его.** Картинка несёт то,
что видно; название — то, что увидеть нельзя.

| | Название | Что несёт картинка | Что добавляет название |
|---|---|---|---|
| **A** | `Times Square in Minecraft — One Street, 275 Years` (48 зн.) | два предела: мёртвая улица и световой каньон | место и охват — одна улица, 275 лет |
| **B** | `Buried in Screens: Times Square in Minecraft` (43 зн.) | красивая новая каменная башня 1904 года | её судьбу — её похоронят под экранами |

Ниже два **цельных** промпта. Каждый отдаёт законченное превью 1280×720:
сцена, надписи, флаг, плашка — всё внутри одной генерации. Копировать целиком.

---

## ПРОМПТ A — сплит 1980 / 2026

```
Create ONE finished YouTube thumbnail image, 16:9 landscape, 1280x720 pixels.
The picture itself must look like a raw in-game screenshot from Minecraft Java
Edition with vanilla 16x16 block textures and a shader pack such as
Complementary or BSL. Only the graphics overlay described in section 5 is flat
2D artwork on top of it.

===== 1. HOW THE WORLD IS BUILT (both halves, no exceptions) =====
- Everything is 1-meter cubes on a strict grid. Nothing is smaller than one
  block.
- NO smooth curves. Arches and rounded tops are built from stairs and slabs
  with clearly visible stair-stepping.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks.
- Every block face is FLAT and uniformly shaded with a coarse visible 16x16
  pixel texture. No smooth gradients, no sculptural shading, no photorealism,
  no stylized voxel art.
- Signs and screens are flat rectangles of coloured blocks sitting on the block
  grid, never smooth panels.
- Minecraft scale: a villager is 2 blocks tall.
- Real Minecraft blocks only: stone bricks, terracotta, smooth quartz,
  deepslate, glass panes, glass blocks, sea lanterns and glowstone for lit
  signage, cobblestone, oak planks, iron bars.
- ALL SIGNAGE IS FICTIONAL: every sign and screen carries invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.

===== 2. LAYOUT =====
The frame is divided exactly down the middle into two vertical halves by a
straight WHITE VERTICAL BAR about 6 pixels wide, running from the top edge to
the bottom edge. Left half = the year 1980. Right half = the year 2026.

Both halves show THE SAME PLACE FROM THE SAME CAMERA: eye level, standing in
the middle of a wide street looking south, where two broad avenues converge in
the middle distance and meet at a narrow wedge-shaped block with a tall narrow
tower standing on it, its sharp point toward the camera.

In each half the wedge tower stands near the INNER edge of that half, close to
the white bar, so the two towers face each other across it. Same building line,
same street width, same horizon height in both halves - the horizon sits just
below the middle of the frame and runs level and continuous across the bar. It
must be instantly obvious that this is one street photographed twice.

===== 3. LEFT HALF - 1980, the street has fallen apart =====
Bare grimy brick and stone walls, streaked and stained. NO screens anywhere:
every sign board is dark, broken, or missing blocks from its face, and only one
or two small signs are still lit. Shopfronts boarded over with rough oak
planks. Dense spray-painted marks up to first-floor height, as blocks of colour
with NO readable words. One building demolished, leaving a flat vacant lot
behind a chain fence with rubbish blown against it. The wedge tower here is a
plain white slab, stained grey, with NO screens on it at all. The roadway is
open to traffic, cracked and patched, with a few old boxy cars and a bus.
Litter in the gutters, weeds in the pavement cracks, very few people, no crowd.
Flat overcast daylight, drained washed-out colours, cold grey-brown palette.

Any damage means MISSING CUBES: broken walls and torn boards end in clean
square block-shaped edges, never crumbled, never jagged.

===== 4. RIGHT HALF - 2026, a canyon of light =====
Every building on both avenues is covered in large lit display boards from
pavement to roofline. The wedge tower is covered from the fourth storey to the
roof in glowing screens. The screens are flat blocks of saturated colour -
reds, blues, cyan, magenta - made of glowstone and sea lanterns, throwing
coloured light onto the street below. A stone plaza with benches and planters
fills the closed roadway in front of the wedge, packed with a relaxed crowd.
Yellow taxis beyond the bollards. Warm late afternoon light behind the towers,
long shadows down the avenue. Rich saturated palette - the exact opposite of
the left half.

===== 5. TEXT AND GRAPHICS OVERLAY (flat 2D on top, sharp, NOT blocky) =====

a) THE YEARS - the only words or digits anywhere in the image.
   "1980" centred horizontally inside the LEFT half.
   "2026" centred horizontally inside the RIGHT half.
   Both sit on the SAME baseline, in the lower quarter of the frame, with their
   centres about 78% of the way down from the top. Digit height about 16% of
   the image height. Heavy bold condensed sans-serif, pure white, with a hard
   black drop shadow offset down and to the right. No box, no panel, no outline
   behind them.
   Spell them EXACTLY: one-nine-eight-zero on the left, two-zero-two-six on the
   right. Four digits each. No other digits anywhere in the image.

b) THE FLAG OF THE UNITED STATES, top-right corner, as a diagonal wedge.
   It is a right triangle whose right angle sits exactly in the top-right
   corner of the image: one leg runs about 29% of the image width leftward
   along the top edge, the other about 44% of the image height downward along
   the right edge, and the hypotenuse is the long diagonal between their ends.
   Inside it the stripes run PARALLEL TO THAT DIAGONAL: seven bands
   alternating deep red and white, the outermost band red. A navy blue triangle
   fills the corner point itself and takes about a third of the wedge.
   Flat solid colours, sharp edges, no waving cloth, no folds, no shading, no
   stars needed.

c) NOTHING ELSE. No title text, no channel name, no logo, no watermark, no
   arrows, no play button, no borders or frames around the image.

===== 6. FORBIDDEN =====
No real brand, no real logo, no trademark, no recognisable company name. No
smooth surfaces, no curved walls, no sculpted or sub-block detail, no
photorealism, no smooth gradients, no high-resolution textures. No HUD, no
crosshair, no hotbar. No collage of more than two panels. No tilted horizon, no
fisheye. No text other than the two four-digit years.
```

**Что где стоит, по разделам.** 1 — материал: почему это выглядит как игра, а не
как «воксельный арт». 2 — каркас: белая полоса по центру, одинаковая камера,
башня у внутреннего края каждой половины, общая линия горизонта. 3 и 4 — две
эпохи, специально описанные через противопоставление: голый кирпич против
экранов, серое против насыщенного, пустая улица против толпы. 5 — вся графика:
годы на одной линии на высоте 78%, флаг углом справа сверху с точными катетами
29% и 44%, и прямой запрет на что-либо ещё. 6 — негатив.

---

## ПРОМПТ B — одиночный кадр 1904 с жёлтой плашкой

```
Create ONE finished YouTube thumbnail image, 16:9 landscape, 1280x720 pixels.
The picture itself must look like a raw in-game screenshot from Minecraft Java
Edition with vanilla 16x16 block textures and a shader pack such as
Complementary or BSL. Only the graphics overlay described in section 4 is flat
2D artwork on top of it.

===== 1. HOW THE WORLD IS BUILT =====
- Everything is 1-meter cubes on a strict grid, nothing smaller than one block.
- NO smooth curves: arches and rounded tops are built from stairs and slabs
  with clearly visible stair-stepping.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks.
- Every block face is FLAT and uniformly shaded with a coarse visible 16x16
  pixel texture. No smooth gradients, no photorealism, no stylized voxel art.
- Minecraft scale: a villager is 2 blocks tall.
- Real Minecraft blocks only: stone bricks, smooth quartz, terracotta,
  cobblestone, oak planks, glass panes, iron bars.
- ALL SIGNAGE IS FICTIONAL: invented short words, abstract blocks of colour and
  simple silhouettes. NEVER a real company name, brand, logo or trademark.

===== 2. THE SCENE - the year 1904 =====
Eye-level view in the middle of a wide cobbled street, looking south. Two broad
avenues converge in the middle distance and meet at a narrow wedge-shaped block
DEAD CENTRE of the frame, its sharp point toward the camera.

On that wedge stands a BRAND-NEW TOWER: narrow, about 10 blocks wide at its
point and 26 blocks tall, faced in clean pale stone, with tall arched windows
built from stairs and slabs, a stepped cornice and a small ornamental turret on
top. It is by far the tallest thing in the frame. Its stone is COMPLETELY BARE:
no signs, no boards and NO SCREENS on it anywhere - this is the whole point of
the picture.

Four-storey brick buildings line both avenues, with painted wooden trade signs
and a few small bulb-lit sign boards above the shopfronts. Horse carriages and
one early motor car on the cobbles. A cast-iron and glass subway entrance kiosk
at the kerb. Arc lamps on tall brackets, telegraph wires on poles. A crowd in
long coats and hats on the pavements, looking up at the new tower. Bright clear
morning, deep blue sky with blocky white clouds.

===== 3. COMPOSITION =====
The tower stands dead centre and its top must stay clear of the banner. Keep
the top 15% of the frame as open sky and the bottom 15% as open cobbles and
empty pavement - graphics go there and nothing important may sit underneath.

===== 4. TEXT AND GRAPHICS OVERLAY (flat 2D on top, sharp, NOT blocky) =====

a) THE BANNER. A solid saturated yellow horizontal bar across the FULL width of
   the image, flush with the top edge, about 15% of the image height, with a
   thin black line along its bottom edge. Inside it, horizontally centred and
   vertically centred, the words

       TIMES SQUARE

   in heavy bold BLACK uppercase condensed sans-serif, letter height about 55%
   of the banner height, with slight letter spacing. Spelled exactly: T-I-M-E-S
   space S-Q-U-A-R-E. Two words, nothing else in the banner.

b) THE YEARS. Near the bottom, on one baseline with their centres about 86% of
   the way down from the top:

       1904   >   2075

   "1904" to the left of centre, "2075" to the right of centre, and between
   them one thick white RIGHT-POINTING TRIANGULAR ARROW as a simple solid
   shape, about the same height as the digits. Digits in heavy bold white
   condensed sans-serif, height about 14% of the image height, each with a hard
   black drop shadow offset down and to the right. No box or panel behind them.
   Spell them EXACTLY: one-nine-zero-four and two-zero-seven-five. These eight
   digits are the only numbers in the image.

c) NOTHING ELSE. No other text, no channel name, no logo, no watermark, no
   flag, no play button, no border or frame around the image.

===== 5. FORBIDDEN =====
No real brand, no real logo, no trademark, no recognisable company name. No
screens or modern display boards anywhere in the scene. No smooth surfaces, no
curved walls, no sculpted or sub-block detail, no photorealism, no
high-resolution textures. No HUD, no crosshair, no hotbar. No split screen, no
collage, no divider. No tilted horizon, no fisheye. No text other than the
banner words and the two four-digit years.
```

**Что где стоит.** 1 — материал. 2 — сцена, и в ней жирным выделено главное:
башня **без единого экрана**, иначе пара разваливается. 3 — резерв места:
верхние 15% под плашку, нижние 15% под годы, чтобы графика не легла на башню.
4 — плашка во всю ширину сверху, годы со стрелкой снизу на высоте 86%. 5 —
негатив, включая прямой запрет экранов в сцене.

---

## Если Джемени врёт в цифрах

Это его обычная слабость: сцену делает верно, а «1980» превращает в «I98O».
Тогда генерим ту же сцену **без пункта 5 / пункта 4** (просто удалить блок
с надписями и добавить `NO text, NO letters, NO numbers anywhere`) и добиваем
скриптом — он рисует текст и флаг математически точно:

```bash
# пара A — сплит
python3 tools/miniatura.py 1980.png 2026.png thumb-a.png 1980 2026 \
  --flag us --flag-corner tr --anchor-left 0.5 --anchor-right 0.5

# пара B — плашка и стрелка
python3 tools/miniatura_aerial.py 1904.png thumb-b.png "TIMES SQUARE" 1904 2075
```

Флаг США в `miniatura.py` есть: семь полос вместо тринадцати (в размере превью
тринадцать сливаются в рябь) и синий крыж на треть угла.

Для сплита половины лучше получаются, если генерить не два отдельных кадра, а
сначала 2026, а потом **править** его в 1980 с приложенной картинкой — камера,
горизонт и клин тогда не уезжают. Можно взять готовые кадры из самого ролика:
1980 — кадр 39, 2026 — кадр 56, 1904 — кадр 10.

---

## Чек-лист перед заливкой

- [ ] В паре B башня каменная и **без единого экрана** — в этом весь смысл
- [ ] В паре A левая башня белая и тоже без экранов: их повесили только в 1999
- [ ] Обе половины пары A — одна камера, клин у белой полосы, горизонт на месте
- [ ] Цифры читаются побуквенно: 1980, 2026 / 1904, 2075 — без подмен
- [ ] Ни одного настоящего бренда и логотипа
- [ ] Флаг США: полосы вдоль диагонали, синий угол на месте
- [ ] Превью читается в размере 210×118 px
