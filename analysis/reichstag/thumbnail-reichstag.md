# Превью — Рейхстаг, четыре варианта

Порядок работы один для всех сплитов: **сначала база 2026, потом каждая вторая
половина делается ПРАВКОЙ этой базы.** Так здание, купол, ракурс и стиль совпадут
между вариантами, и превью можно честно A/B-тестить — меняется только левая половина.

Годы, флаг и разделитель накладываются скриптом. Генератору их не показывать:
он врёт в цифрах и в порядке полос флага.

---

## Варианты

| | Слева | Справа | Ставка |
|---|---|---|---|
| **A** | 1945, руина | 2026, стеклянный купол | классика ниши, самый понятный контраст |
| **B** | 1995, здание в серебристой ткани | 2026 | **этого нет ни у кого**, сильнейший «что это вообще?» |
| **C** | 1933, пожар | 2026 | максимальная драма, но тема тяжёлая |
| **D** | одиночный кадр 1884, стройка | — | формат с жёлтой плашкой и стрелкой лет |

Рекомендую выкатывать **A и B**. A — безопасный базовый, B — разрыв шаблона: в ленте,
где все показывают «старое здание против нового», обёрнутый в ткань дом заставляет
остановиться, а объяснение можно получить только кликнув.

---

## ШАГ 1 — база 2026 (генерится один раз, с нуля)

```
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES:
- The whole world is 1-meter cubes on a strict grid. Nothing is smaller than one
  block. NO smooth curves: domes and arches are built from stairs and slabs with
  clearly visible stair-stepping in the silhouette.
- NO sub-block detail: no carved ornament, no thin mouldings, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded with a coarse visible 16x16
  pixel texture. No smooth gradients, no sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks with a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall.
- Built from real Minecraft blocks: pale sandstone and smooth quartz, oxidised
  copper, glass blocks, glass panes, stone bricks, cobblestone.

THE BUILDING - remember it exactly, it must be identical in the second image:
a massive rectangular parliament building of pale sandstone blocks, 56 blocks
wide and 16 blocks tall to the cornice. A projecting entrance portico of six
tall square columns under a plain triangular pediment stands at the centre of
the west front, reached by a wide flight of stone stairs. One square corner
tower with a small stepped copper roof at each of the four corners. Regular rows
of identical 1x2 glass-pane windows along the whole facade. Above the centre
stands a large stepped dome built from clear glass blocks with a visible spiral
ramp of stone stairs winding up inside it.

SCENE: eye-level three-quarter view from the open square, the building turned
slightly to the left so both the long west front and the shorter south side are
visible. Present day: clean pale stone, the glass dome bright against the sky,
mature Minecraft trees closing the far left, mown lawns and wildflower meadow,
modern benches, a cycle lane, a relaxed crowd of villagers on the grass, modern
government buildings low behind the roofline on the right. Warm bright
late-afternoon light, deep blue sky with blocky white clouds.

ONE single continuous scene. NO split screen, NO divider, NO collage, NO border.
NO text, NO letters, NO numbers, NO flag of any kind, NO logo, NO watermark,
NO HUD, no crosshair, no hotbar, no interface.

COMPOSITION: keep the portico and the dome in the central area of the frame,
the image will be cropped. Lower third kept simple.
```

**Негатив (для всех генераций):**
```
American flag, stars and stripes, generic flag, smooth surfaces, curved walls,
rounded domes, sculpted detail, sub-block detail, carved ornament, thin
mouldings, photorealism, stylized voxel art, smooth gradients, high resolution
textures, rounded topiary tree, HUD, crosshair, hotbar, text, letters, numbers,
watermark, logo, split screen, collage, border, frame, fisheye, tilted horizon
```

---

## ШАГ 2 — вторые половины, каждая правкой базы

Ко всем трём: **приложить картинку 2026** и вставить блок целиком.

### Вариант A — 1945, руина

```
BASE IMAGE: the present-day building is attached. Build this image by EDITING
that image. Keep the camera position, the framing, the horizon and the
perspective EXACTLY as they are. Keep the same Minecraft in-game rendering:
vanilla 16x16 textures, strict block grid, flat block faces, no smooth curves,
no sub-block detail.

It must stay recognisably the SAME building, only ruined. Do not redesign it.

CHANGE: it is now 1945 and the building has been gutted by fighting and fire.
The roof is gone and the glass dome above the centre has been destroyed
completely - only a twisted stump of copper ribs remains where it stood. The
pale sandstone facade is pocked and scarred all over, blackened above the
window openings, and most windows are empty dark holes with blocks missing
around their edges. The six-column portico still stands but is chipped and
soot-stained. Damage means MISSING CUBES: broken walls end in clean square
block-shaped edges, never crumbled or jagged. Rubble is whole 1-meter blocks
and slabs lying on the ground in the same stone textures as the walls.
Bomb craters in the ground, a burnt-out vehicle, dead bare trees on the left.
Overcast winter sky using the same blocky rectangular clouds as the attached
image, only grey. Snow-layer blocks in whole-block patches over the rubble.
Desaturated grey-brown palette, no people, no fires.

NO text, no numbers, no flag of any kind, no divider, no split screen.
```

### Вариант B — 1995, здание в ткани

```
BASE IMAGE: the present-day building is attached. Build this image by EDITING
that image. Keep the camera position, the framing, the horizon and the
perspective EXACTLY as they are. Keep the same Minecraft in-game rendering:
vanilla 16x16 textures, strict block grid, flat block faces, no smooth curves.

CHANGE: it is now 1995 and the entire building has been wrapped in shimmering
silvery-grey fabric for an art installation. The cloth covers everything from
the ground to the roofline: the portico, the columns, the corner towers and
every window are hidden beneath it, so only the soft blocky mass of the building
remains, with its overall shape still readable. Dark blue rope runs in long
vertical lines down the wrapped facade, tying the cloth. There is NO dome at all
in this image - the wrapping predates it, so the roofline is flat under the
fabric. The square in front is grass with a large relaxed summer crowd sitting
and standing on it, looking at the building. Bright summer day with the same
blocky clouds as the attached image.

Render the fabric in Minecraft terms: flat block faces of pale silver-grey wool
blocks following the building's blocky shape, not smooth draped cloth.

NO text, no numbers, no flag of any kind, no divider, no split screen.
```

### Вариант C — 1933, пожар

```
BASE IMAGE: the present-day building is attached. Build this image by EDITING
that image. Keep the camera position, the framing, the horizon and the
perspective EXACTLY as they are. Keep the same Minecraft in-game rendering:
vanilla 16x16 textures, strict block grid, flat block faces, no smooth curves.

It must stay recognisably the SAME building. Do not redesign it.

CHANGE: it is now a winter night in 1933 and the building is on fire. Flames
pour from the windows of the whole central section. In place of the glass dome
there is an older dome of glass and copper whose panes have shattered, its bare
copper ribs standing black against the flames burning inside it. Heavy black
smoke rolls across the sky to the right. Two horse-drawn fire pumps and one
early motor fire engine stand on the square with hoses running to the entrance
stairs, and small firefighter figures around them. The trees on the left are
bare. Snow-layer blocks on the ground. Night sky, orange firelight across the
pale stone facade, no other light source.

NO text, no numbers, no flag of any kind, no divider, no split screen.
```

---

## ШАГ 3 — вариант D, одиночный кадр с плашкой

Другой формат: сплита нет, показан только ранний год, а 2026 живёт в подписи.
Генерится с нуля, не правкой.

```
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, Complementary shader pack. The whole world is 1-meter cubes on a
strict grid, nothing smaller than one block, no smooth curves, no sub-block
detail, flat uniformly shaded block faces with coarse pixel texture. Trees are
straight 1x1 log trunks with blocky cubic leaf crowns. A villager is 2 blocks
tall.

SCENE: a large city building site in 1884, seen at eye level across an open
square. In the centre-right, a huge rectangular excavation pit with stepped
earth sides surrounded by a timber hoarding. Stacks of pale sandstone blocks,
timber piles, mortar tubs and two tall wooden cranes stand around the pit. Rails
for spoil carts run across the site. Workers in period clothes, a horse cart
delivering stone. On the LEFT third of the square stands a tall fluted stone
column on a stepped square base with a small gilded figure on top. Behind the
square, a dense Minecraft treeline. Raked gravel, gas lamps on iron posts,
a few horse carriages. Bright clear day, deep blue sky with blocky white clouds.

There is NO finished parliament building anywhere in the frame - only the pit
and the cranes.

ONE single continuous scene. NO split screen, NO divider, NO collage, NO border.
NO text, NO letters, NO numbers, NO flag of any kind, NO logo, NO watermark,
NO HUD, no crosshair, no hotbar.

COMPOSITION: keep the top 20% and the bottom 15% of the frame calm - open sky
above, open gravel below - because a banner and a caption go there. The pit and
cranes sit right of centre, the column left of centre.
```

---

## Сборка

Флаг Германии: чёрная полоса ложится в самый угол, за ней красная, снаружи
золотая — как в берлинском превью конкурента, с которого снята формула.

```bash
# варианты A, B, C — сплит
python3 tools/miniatura.py LEFT.png RIGHT_2026.png thumb.png 1945 2026 \
  --flag de --flag-corner tr --anchor-left 0.5 --anchor-right 0.5

# вариант D — плашка и стрелка
python3 tools/miniatura_aerial.py IN.png OUT.png REICHSTAG 1884 2026
```

Годы под варианты: A — `1945 / 2026`, B — `1995 / 2026`, C — `1933 / 2026`.

Точки обрезки `--anchor-left` и `--anchor-right` подбираются по готовым
картинкам: нужно, чтобы портик и купол попали в кадр и не залезли под цифры.

---

## Чек-лист

- [ ] Обе половины — одна точка съёмки: портик и угловые башни на одной высоте
- [ ] Здание узнаётся как одно и то же: шесть колонн, четыре угловые башни
- [ ] В варианте B нет купола — он появился только в 1999
- [ ] В варианте A купол разрушен, а не просто отсутствует
- [ ] На сгенерированных картинках нет ни одной буквы, цифры и ни одного флага
- [ ] Полосы немецкого флага идут от угла: чёрная, красная, золотая
- [ ] Превью читается в размере 210×118 px
