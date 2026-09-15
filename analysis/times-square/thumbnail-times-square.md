# Превью Таймс-сквер — две пары «название + картинка»

Принцип: **название не повторяет превью, а договаривает его.** Картинка несёт то,
что видно; название — то, что увидеть нельзя. Порознь каждое работает вполсилы,
вместе дают законченный крючок.

Что уже несёт превью и чего в названии быть не должно: сами два состояния,
годы цифрами, флаг страны. Что может нести только название: где это происходит,
какой охват, и что случится дальше.

---

## ПАРА A — падение и возвращение

**Название — 48 знаков**
```
Times Square in Minecraft — One Street, 275 Years
```

**Превью:** сплит, слева 1980 (кадр 39), справа 2026 (кадр 56). Годы `1980 / 2026`,
флаг США диагональным углом справа сверху.

**Как они дополняют друг друга.** Картинка показывает два предела: заколоченная
грязная улица и световой каньон. Она не говорит ни где это, ни сколько всего таких
состояний. Название добавляет ровно это: одна улица и 275 лет между крайними точками.
Зритель понимает, что между двумя половинами превью спрятаны десятки других.

Левая половина сама по себе не читается как Таймс-сквер — заколоченная улица может
быть где угодно. Правая читается мгновенно. На этом и строится вопрос: как одно
стало другим. Название называет место и снимает первую половину вопроса, оставляя
вторую.

---

## ПАРА B — здание, которое похоронили

**Название — 43 знака**
```
Buried in Screens: Times Square in Minecraft
```

**Превью:** одиночный кадр 1904 года (кадр 10), формат с жёлтой плашкой.
Плашка: `TIMES SQUARE`. Подпись снизу: `1904 ⟶ 2075`.

**Как они дополняют друг друга.** На картинке — красивая каменная башня, только что
построенная, вокруг кареты и дуговые лампы. Ничего тревожного. Название говорит то,
чего на картинке нет и быть не может: это здание похоронят под экранами. Зритель
видит начало и узнаёт финал, но не видит как — за этим и кликает.

Это тот же приём withheld payoff, что у роликов с жёлтой плашкой в нише: показан
только ранний год, поздний живёт в подписи. Здесь он усилен тем, что название
раскрывает не дату, а судьбу.

---

## ПРОМПТ 1 — база 2026 (для пары A, правая половина)

Генерится с нуля. Эта же картинка потом правится в 1980.

```
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES:
- The whole world is 1-meter cubes on a strict grid. Nothing is smaller than one
  block. NO smooth curves: arches and rounded tops are built from stairs and
  slabs with clearly visible stair-stepping.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks.
- Every block face is FLAT and uniformly shaded with a coarse visible 16x16
  pixel texture. No smooth gradients, no sculptural shading.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.
- Minecraft scale: a villager is 2 blocks tall.
- Built from real Minecraft blocks: stone bricks, terracotta, smooth quartz,
  deepslate, glass panes, glass blocks, sea lanterns and glowstone for lit
  signage, cobblestone.

ALL SIGNAGE IS FICTIONAL: every sign and screen carries invented short words,
abstract blocks of colour and simple silhouettes. NEVER a real company name, a
real brand, a real logo or a real trademark of any kind.

SCENE: eye-level view in the middle of a wide street, looking south. Two broad
avenues converge in the middle distance and meet at a narrow wedge-shaped block
dead centre of the frame, its sharp point toward the camera. A tall narrow tower
stands on that wedge, its whole surface covered from the fourth storey to the
roof in large lit display boards. Every building on both sides is covered in
screens from pavement to roofline, so the street is a canyon of light. A stone
plaza with benches and planters fills the closed roadway in front of the wedge,
packed with a relaxed crowd. Yellow taxis beyond the bollards. Warm late
afternoon light behind the towers, long shadows down the avenues.

ONE single continuous scene. NO split screen, NO divider, NO collage, NO border.
NO text, NO letters, NO numbers, NO flag of any kind, NO logo, NO watermark,
NO HUD, no crosshair, no hotbar.

COMPOSITION: keep the wedge tower and the converging avenues in the central area
of the frame, the image will be cropped. Lower third kept simple.
```

**Негатив (для всех трёх генераций):**
```
real brand, real logo, trademark, recognisable company name, American flag on
buildings, smooth surfaces, curved walls, sculpted detail, sub-block detail,
carved ornament, photorealism, stylized voxel art, smooth gradients, high
resolution textures, HUD, crosshair, hotbar, text, letters, numbers, watermark,
logo, split screen, collage, border, frame, fisheye, tilted horizon
```

---

## ПРОМПТ 2 — 1980 (для пары A, левая половина)

**Приложить картинку 2026** и вставить блок.

```
BASE IMAGE: the present-day street is attached. Build this image by EDITING that
image. Keep the camera position, the framing, the horizon and the perspective
EXACTLY as they are. Keep the same Minecraft in-game rendering: vanilla 16x16
textures, strict block grid, flat block faces, no smooth curves, no sub-block
detail.

It must stay recognisably the SAME street with the SAME wedge block dead centre.
Do not redesign the layout.

CHANGE: it is now 1980 and the street has fallen apart. The screens are gone
completely - the buildings show bare grimy brick and stone instead, streaked and
stained. Only three small signs are still lit anywhere in the frame; every other
sign board is dark, broken, or missing blocks from its face. Shopfronts along
both sides are boarded over with rough planks. Dense spray-painted marks cover
the walls up to first-floor height, in blocks of colour with no readable words.
One building on the right has been demolished, leaving a flat vacant lot behind
a chain fence with rubbish blown against it. The wedge tower is a plain white
slab, stained grey, with no screens on it at all. The plaza is gone: the roadway
is open to traffic again, cracked and patched, with a few old cars and a bus.
Litter in the gutters, weeds in the pavement cracks, very few people. Flat
overcast daylight, drained washed-out colours.

Damage means MISSING CUBES: broken walls and boards end in clean square
block-shaped edges, never crumbled or jagged.

NO text, no numbers, no flag of any kind, no divider, no split screen.
```

---

## ПРОМПТ 3 — 1904 (для пары B, одиночный кадр)

Генерится с нуля.

```
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, Complementary shader pack. The whole world is 1-meter cubes on a
strict grid, nothing smaller than one block, no smooth curves, no sub-block
detail, flat uniformly shaded block faces with coarse pixel texture. Signs are
flat rectangles of coloured blocks. A villager is 2 blocks tall.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract blocks of colour and
simple silhouettes. NEVER a real company name, brand, logo or trademark.

SCENE: eye-level view in the middle of a wide cobbled street in 1904, looking
south. Two broad avenues converge in the middle distance and meet at a narrow
wedge-shaped block dead centre of the frame, its sharp point toward the camera.
On that wedge stands a brand-new tower: narrow, about 10 blocks wide at its
point and 26 blocks tall, faced in clean pale stone with tall arched windows, a
stepped cornice and a small ornamental turret on top. It is by far the tallest
thing in the frame and its stone is completely bare - no signs and no screens
on it anywhere. Four-storey brick buildings line both avenues with painted
wooden trade signs and a few small bulb-lit sign boards above the shopfronts.
Horse carriages and one early motor car on the cobbles, a cast-iron and glass
subway entrance kiosk at the kerb, arc lamps on tall brackets, telegraph wires
on poles. A crowd in long coats and hats on the pavements looking up at the new
tower. Bright clear morning, deep blue sky with blocky white clouds.

ONE single continuous scene. NO split screen, NO divider, NO collage, NO border.
NO text, NO letters, NO numbers, NO flag of any kind, NO logo, NO watermark,
NO HUD, no crosshair, no hotbar.

COMPOSITION: keep the top 20% and the bottom 15% of the frame calm - open sky
above the tower, open cobbles below - because a banner and a caption go there.
The tower sits dead centre.
```

---

## Сборка

```bash
# пара A — сплит
python3 tools/miniatura.py 1980.png 2026.png thumb-a.png 1980 2026 \
  --flag us --flag-corner tr --anchor-left 0.5 --anchor-right 0.5

# пара B — плашка и стрелка
python3 tools/miniatura_aerial.py 1904.png thumb-b.png "TIMES SQUARE" 1904 2075
```

Флага США в наборе `miniatura.py` пока нет — добавить полосы и синий угол.
Точки обрезки подбираются по готовым картинкам: клин в центре и башня должны
попасть в кадр и не уйти под цифры.

---

## Чек-лист

- [ ] На сгенерированных картинках нет ни одной буквы и цифры
- [ ] Ни одного настоящего бренда и логотипа
- [ ] Обе половины пары A — одна точка съёмки, клин на том же месте
- [ ] В паре B башня каменная и **без единого экрана** — в этом весь смысл
- [ ] В паре A башня белая и тоже без экранов: их повесили только в 1999
- [ ] Превью читается в размере 210×118 px
