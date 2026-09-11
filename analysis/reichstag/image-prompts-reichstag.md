# Промпты картинок — Reichstag, 75 готовых блоков

Сгенерировано `tools/image_prompts.py` из `prompts-reichstag.md`.
Стиль, камеры и якоря взяты из того же файла — правишь их там, перезапускаешь скрипт.

Каждый блок — **целый промпт**. Копировать целиком, дописывать ничего не нужно.

**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:

```
American flag, stars and stripes, union jack, tricolour, generic flag, wrong
flag, smooth surfaces, curved walls, rounded domes, smooth arches, sculpted
detail, sub-block detail, carved ornament, thin mouldings, marble sculpture,
realistic statue, detailed face, cloth folds, high-poly, realistic geometry,
photorealism, stylized voxel art, smooth gradients, soft rounded edges, high
resolution textures, smooth terrain slope, rounded topiary tree, horse next to
a modern tram, HUD, crosshair, hotbar, user interface, text, letters, numbers,
watermark, signature, logo, blurry, fisheye, distorted perspective, tilted
horizon, changed art style, split screen, collage, border
```

## Самое важное

**Кадр 1 генерится с нуля. Кадры 2-75 — только правкой предыдущего кадра.**
В Gemini это значит: прикрепить картинку предыдущего кадра и вставить блок.
Без приложенной картинки модель будет каждый раз выдумывать объекты заново —
это предел технологии, промптом он не обходится.

После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.

---

### Кадр 1 · 1700 · Marshland

> Вход: ничего. Единственный кадр, который генерится с нуля (text-to-image).
> Это мастер-плита всего ролика — от неё зависят все 59 остальных кадров,
> и переснять её потом означает переснять всё. Сгенерить 10–20 вариантов
> и выбирать придирчиво: важно, чтобы линия горизонта, деревья слева и
> пустое пятно справа встали ровно так, как описано в камере.
> 
> ---
> 
> # ПРОЛОГ · пустое место

```
BASE IMAGE: none. This is the first frame of the series - generate it from scratch.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A flat marshy clearing on the edge of a great oak forest, with no buildings of any kind anywhere in the frame. Reed beds and standing pools of dark water across the open ground, tussocks of coarse grass, a few dead birches. The dense forest treeline closes the far left. Nothing at all stands on the open ground in the centre-right. Overcast pale sky, muted green and brown palette.
```

### Кадр 2 · 1790 · The Parade Ground

> Вход: кадр 1 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The marsh has been drained and levelled into a flat sandy exercise ground. The pools and reeds are gone, replaced by bare packed sand and gravel with cart ruts across it. A low wooden post-and-rail fence runs along the left side. One small wooden guardhouse with a shingled roof stands at the far left edge. The plot in the centre-right is still completely empty. Clear pale sky.
```

### Кадр 3 · 1850 · Königsplatz

> Вход: кадр 2 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The ground is now a formal city square: raked gravel, a low stone kerb around its edge, and a double row of young Minecraft lime trees planted along the left side. Gas lamps on iron posts stand at intervals. A long low theatre building of pale stone with a columned front stands far back on the left, beyond the trees. The plot in the centre-right is still empty ground. Clear bright day.
```

### Кадр 4 · 1871 · The Empire

> Вход: кадр 3 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square is decorated for a celebration: a temporary wooden triumphal arch of painted timber stands at the left, garlands of greenery strung between the lime trees, and rows of flagpoles along the kerb. Every flag on those poles has three horizontal bands - black on top, white in the middle, red at the bottom - and there are NO other flags of any kind in the frame. A festive crowd in top hats and bonnets fills the gravel. The plot in the centre-right is still empty.
```

### Кадр 5 · 1873 · The Victory Column

> Вход: кадр 4 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Erect a tall fluted stone column on a square stepped stone base in the LEFT third of the square, with a small gilded figure standing on its top. It is far taller than the lime trees and must appear in every following image until it is explicitly removed. The temporary arch and garlands are gone; the square is back to ordinary use with carriages and pedestrians.
```

### Кадр 6 · 1877 · The Old Palace

> Вход: кадр 5 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
An older building now stands on the plot in the centre-right: a wide three-storey palace of pale plastered stone with a low pitched roof, a modest columned entrance and regular tall windows. It is clearly an older, plainer building than a parliament. The square and the column are unchanged.
```

### Кадр 7 · 1884 · Foundations

> Вход: кадр 6 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The old palace is gone. In its place a large rectangular excavation pit with stepped earth sides, surrounded by a timber hoarding. Stacks of pale sandstone blocks, timber piles and two tall wooden cranes stand around the pit. Rails for spoil carts run across the site. The column and the square are unchanged.
```

### Кадр 8 · 1886 · The First Courses

> Вход: кадр 7 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The excavation is finished and filled with a massive stone foundation. The first three courses of pale sandstone wall now stand above ground level all round the plot, so the full rectangular footprint of the building is visible for the first time. Low timber scaffolding along the walls, two cranes, stacks of dressed stone and a mortar mixing area. The column and the square are unchanged.
```

### Кадр 9 · 1888 · Walls Rising

> Вход: кадр 8 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The walls of the new building stand to the height of the first storey, in pale sandstone blocks, wrapped in a forest of timber scaffolding with plank walkways at three levels. Three cranes rise above it. The outline of the six-column portico is already recognisable at the centre of the west front.
```

### Кадр 10 · 1891 · The Shell

> Вход: кадр 9 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building has reached its full height of 16 blocks to the cornice, with all four square corner towers built. The six-column portico and its triangular pediment are complete. Scaffolding remains only around the centre of the roof, where a stepped ring of copper and glass is being assembled.
```

### Кадр 11 · 1894 · Finished

> Вход: кадр 10 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
All scaffolding is gone. The building is complete: pale sandstone facade, six-column portico over a wide flight of stone stairs, four corner towers with small stepped copper roofs, and a large stepped dome of glass blocks and copper stairs standing directly above the centre. One flagpole on the roof flies a flag with three horizontal bands - black on top, white in the middle, red at the bottom. No other flag anywhere in the frame. Bright clear day, the building at its cleanest.
```

### Кадр 12 · 1898 · The Square Laid Out

> Вход: кадр 11 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square in front is relaid: pale stone paving replacing the gravel, formal hedged flower beds, a stone basin with a low fountain at the left, and taller lime trees. More gas lamps, iron benches, and a row of waiting carriages along the kerb.
```

### Кадр 13 · 1900 · The Empire at Its Height

> Вход: кадр 12 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square at its most prosperous: the flower beds in full bloom, the fountain running, every gas lamp lit at dusk, a long rank of polished carriages, officers and ladies in formal dress on the entrance stairs, a military band playing at the left. The building is new and spotless, the flag on the roof with three horizontal bands - black on top, white in the middle, red at the bottom - and no other flag anywhere.
```

### Кадр 14 · 1902 · First Motor Cars

> Вход: кадр 13 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Add three early motor cars with high bodies and spoked wheels parked at the kerb among the carriages, and electric street lamps on taller plain posts replacing some of the gas lamps. Pedestrians in longer coats.
```

### Кадр 15 · 1906 · The Horse Tram

> Вход: кадр 14 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A tram line now crosses the square: two steel rails set flush into the paving, with an open four-wheeled tram car running on them, pulled by two horses in harness walking between the rails in front of it. The car has no engine, no overhead wires and no pantograph, and there are no poles or cables of any kind above it. A small wooden tram stop shelter stands at the kerb.
```

### Кадр 16 · 1910 · Electric Trams

> Вход: кадр 15 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Replace the horse tram with an electric one: a closed red-and-cream tram car on the same rails with a pantograph on its roof, overhead wires strung on plain catenary poles along the line. The horses are gone completely. More motor cars, fewer carriages, a newspaper kiosk at the kerb.
```

### Кадр 17 · 1914 · Mobilisation

> Вход: кадр 16 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A huge crowd packs the square and the entrance stairs. Printed notices are pasted on boards at the kerb and on the tram shelter. Families waving, men with suitcases. The flag on the roof has three horizontal bands - black, white, red - and there is no other flag in the frame. Bright hard summer light.
```

### Кадр 18 · 1916 · The Inscription

> Вход: кадр 17 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Add a row of large plain bronze capital letters fixed to the frieze above the six columns of the portico, reading DEM DEUTSCHEN VOLKE. These are the ONLY letters anywhere in the image. The square is quieter, fewer people, no motor cars, a shabbier look.
```

### Кадр 19 · 1918 · The Republic

> Вход: кадр 18 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 20 · 1919 · Black, Red, Gold

> Вход: кадр 19 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The red banners are gone. One flag flies from the roof flagpole with three horizontal bands - black on top, red in the middle, gold at the bottom - and no other flag appears anywhere in the frame. The square is orderly again, the paving swept, a few motor cars and a tram, ordinary pedestrians.
```

### Кадр 21 · 1923 · Hard Times

> Вход: кадр 20 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square looks poor: a long queue of people along the kerb, handcarts, shabby coats, bare flower beds gone to weeds, two broken gas lamps, paper litter blowing across the paving. Fewer vehicles. Grey overcast light, drained colours. The black-red-gold flag still flies on the roof.
```

### Кадр 22 · 1926 · The Twenties

> Вход: кадр 21 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Prosperity returns: the flower beds replanted, new clean paving, a line of taxis, a double-decker bus, an advertising column at the kerb, well-dressed crowds with hats and umbrellas, a photographer with a tripod on the stairs.
```

### Кадр 23 · 1930 · Depression

> Вход: кадр 22 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Hard times again and visibly political: rows of printed paper posters pasted over the advertising column and along the hoardings, a queue at a soup cart, men standing about with nothing to do, fewer vehicles. The posters carry no readable words, only blocks of colour. Cold flat light.
```

### Кадр 24 · 1933 · The Fire

> Вход: кадр 23 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building is burning. Flames pour from the windows of the whole central section and from the base of the dome; the glass of the dome is shattered and its copper ribs stand black against the fire. Heavy black smoke rolls across the sky to the right. Two horse-drawn fire pumps and one motor fire engine stand on the square with hoses running to the stairs. No flags anywhere: the roof flagpole is bare. Night, orange firelight on the facade and on the snow.
```

### Кадр 25 · 1934 · Burnt Out

> Вход: кадр 24 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The fire is out. The central section is a blackened shell: window openings empty and soot-streaked, the dome reduced to a bare skeleton of copper ribs with no glass left in it, the roof behind it collapsed. Rough timber boards nailed over the ground-floor windows and doors. A plain wire fence around the stairs. The flagpole is bare and no flag appears anywhere. Grey winter light, soot on the snow.
```

### Кадр 26 · 1937 · Empty

> Вход: кадр 25 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building stands unused: boards still over the windows, the bare dome skeleton above, weeds growing through the cracks of the entrance stairs, streaked soot stains down the facade. The square in front is neatly kept but empty of people. No flags anywhere in the frame. Flat overcast daylight.
```

### Кадр 27 · 1939 · The Column Is Gone

> Вход: кадр 26 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The tall fluted victory column and its stepped base have been removed from the left third of the square completely - there is now only a circle of fresh pale paving where it stood, and open sky where its figure used to be. Everything else is unchanged. This absence must persist in every following image.
```

### Кадр 28 · 1941 · Blackout

> Вход: кадр 27 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building is prepared for air raids: large nets with green and brown cloth strips stretched over the roof and the dome skeleton, sandbags stacked around the base of the portico columns, the boarded windows painted dark, the street lamps hooded with narrow slits. An anti-aircraft gun on a sandbag emplacement stands on the square. No flags anywhere. Cold grey light.
```

### Кадр 29 · 1944 · Bomb Damage

> Вход: кадр 28 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building is badly damaged: a large section of the roof has fallen in, several window openings are torn into ragged holes with missing blocks around them, the portico pediment is chipped and one column is scarred. Bomb craters in the paving of the square, a burnt-out lorry, the camouflage netting hanging in shreds. Drifting dust. No flags anywhere.
```

### Кадр 30 · 1945 · The Battle

> Вход: кадр 29 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Heavy fighting damage: the facade pocked and scarred all over, most window openings blown out, the roof largely gone, the dome skeleton twisted and half collapsed, deep craters across the square, wrecked vehicles and scattered blocks. Thick smoke drifting across the whole frame, small fires in the ruins. No flags anywhere yet.
```

### Кадр 31 · 1945 · The Flag on the Roof

> Вход: кадр 30 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The fighting is over. The building stands gutted and roofless, its facade scarred, the dome skeleton a twisted ruin. One plain red flag - plain red cloth with no emblem, no symbol and no lettering on it - flies from a pole on the broken roof. It is the only flag in the frame. Rubble and wrecked vehicles across the square, a few small figures picking through the debris. Flat colourless light, no fires left.
```

### Кадр 32 · 1945 · The Ruin in Daylight

> Вход: кадр 31 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Clear summer daylight on the gutted building for the first time: no smoke, no fires, every scar on the pale sandstone facade sharply visible, the window openings empty, the roof gone, the dome a twisted stump. The plain red flag still on its pole. Soldiers and civilians stand about on the rubble of the square, several of them photographing the ruin, a jeep parked at the foot of the stairs. Bright hard light.
```

### Кадр 33 · 1946 · Vegetable Gardens

> Вход: кадр 32 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square in front has been dug up into small fenced vegetable plots with neat rows of green crops, garden sheds of salvaged boards, and water barrels. The gutted building stands behind it unchanged, roofless and scarred. The flagpole is bare. Warm summer light over the incongruous gardens.
```

### Кадр 34 · 1948 · The Great Rally

> Вход: кадр 33 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
An enormous crowd fills the whole square in front of the ruin, tens of thousands of small figures packed shoulder to shoulder, with a wooden speaker's platform set up at the foot of the entrance stairs. The gardens are gone. The building behind is still the gutted ruin. Plain black-red-gold flags on two poles at the platform and no other flags anywhere. Cold autumn light.
```

### Кадр 35 · 1951 · Clearing

> Вход: кадр 34 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Rubble clearing across the square: sorted stacks of salvaged brick and stone, a light railway with spoil tips, hand carts, teams of workers in lines. The ruined building behind is being made safe, with rough timber props against two walls and a plain wire fence around it.
```

### Кадр 36 · 1954 · The Dome Comes Down

> Вход: кадр 35 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The twisted dome skeleton is being demolished: half of its copper ribs already gone, a tall crane lifting a section clear, the rest cut back to a low stump above the roofline. After this year the building has NO dome at all until it is explicitly rebuilt. The facade is still scarred and the windows still empty.
```

### Кадр 37 · 1957 · The Bare Ruin

> Вход: кадр 36 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square is fully cleared and sown with rough grass. The building stands as a plain roofless shell with a flat stump where the dome was, its facade cleaned of soot but still pitted, window openings boarded. Nothing else on the square: no trees on the right, no traffic, no fences. Very empty. Flat daylight.
```

### Кадр 38 · 1961 · The Wall

> Вход: кадр 37 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A grey concrete barrier wall with a rounded top now runs across the frame immediately behind and to the right of the building, cutting the view off. A tall watchtower stands behind it and a cleared strip of raked sand runs in front of it. The building is unchanged, still a roofless shell. The square in front is empty grass.
```

### Кадр 39 · 1964 · Reconstruction

> Вход: кадр 38 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building is wrapped in modern tubular steel scaffolding with safety netting, and a tower crane stands beside it. The roof is being rebuilt flat, with no dome. Contractor huts and stacks of materials on the grass. The wall and watchtower behind are unchanged.
```

### Кадр 40 · 1967 · Halfway

> Вход: кадр 39 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Reconstruction well advanced: the scaffolding now covers only the upper half of the building, the new flat roof is finished and watertight, and the lower facade has been cleaned to bare pale stone with new glass already in the ground-floor windows. A tower crane still stands beside it. Contractor huts and a muddy access road across the grass.
```

### Кадр 41 · 1971 · Reopened

> Вход: кадр 40 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The scaffolding is gone. The building is restored but visibly simplified: the sandstone facade cleaned to a uniform pale colour, the six-column portico and the inscription intact, but a plain flat roof with NO dome at all, and the four corner towers rebuilt lower and plainer. New clear glass in every window. A flag with three horizontal bands - black, red, gold - on a pole at the front, and no other flag in the frame. Neat lawns and new paving in front.
```

### Кадр 42 · 1976 · The Death Strip

> Вход: кадр 41 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Behind the building the barrier is now a full system: the concrete wall in front, a wide raked sand strip, a second inner wall, floodlight masts and two watchtowers. On this side, a wooden tourist viewing platform with a flight of steps stands at the right edge of the square, with visitors on top looking over. Tour coaches at the kerb.
```

### Кадр 43 · 1982 · Graffiti

> Вход: кадр 42 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The western face of the concrete wall is now covered in dense multicoloured spray-painted graffiti from end to end - blocks of colour and shapes only, no readable words or letters anywhere. A second viewing platform has been built. More tourists, souvenir stands, parked cars.
```

### Кадр 44 · 1987 · Anniversary

> Вход: кадр 43 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square is decorated for a city anniversary: rows of flagpoles along the kerb, all flying the same three-band black, red and gold flag and nothing else, banners of plain colour between the lime trees, a temporary stage at the left, market stalls and a crowd. The building and the wall behind are unchanged.
```

### Кадр 45 · 1989 · The Wall Falls

> Вход: кадр 44 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
An enormous crowd fills the square and people are standing on top of the concrete wall itself, dozens of figures along it, with more climbing up. Camera flashes, plain black-red-gold flags waving in the crowd and no other flags. A section of the wall has been broken open. Cold night, hard floodlight from the platforms, breath steaming.
```

### Кадр 46 · 1990 · Reunification

> Вход: кадр 45 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A vast crowd fills the square in front of the building at night. One very large flag with three horizontal bands - black, red, gold - is being raised on a tall new pole directly in front of the entrance stairs, lit by floodlights. No other flag of any kind appears in the frame. Fireworks in the sky above the roofline.
```

### Кадр 47 · 1991 · The Wall Comes Down

> Вход: кадр 46 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The concrete wall is being demolished: long sections already gone leaving a raw strip of churned earth, a crane lifting a painted slab onto a lorry, the watchtowers cut down to stumps. Beyond the gap, ordinary streets and buildings are visible for the first time.
```

### Кадр 48 · 1993 · The Scar

> Вход: кадр 47 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The wall is gone completely. Where it stood there is a wide strip of bare ground and temporary gravel, with survey pegs and orange netting. The building stands plain and domeless, clean, with the black-red-gold flag on its pole. Ordinary traffic crossing behind.
```

### Кадр 49 · 1995 · Wrapped

> Вход: кадр 48 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The entire building is completely wrapped in shimmering silvery fabric, from the ground to the roofline, tied with dark blue rope in long vertical lines. The portico, the columns, the towers and the windows are all hidden under the cloth, so only the soft blocky shape of the building remains. A huge relaxed crowd sits and stands on the grass of the square looking at it. Bright summer day.
```

### Кадр 50 · 1995 · Unwrapped

> Вход: кадр 49 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The fabric and ropes are gone. The building stands bare and empty, its windows dark, with modern tubular scaffolding going up around the west front and a tower crane beside it. Contractor hoardings around the base. The crowd is gone; the grass is trampled.
```

### Кадр 51 · 1997 · Rebuilding

> Вход: кадр 50 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 52 · 1999 · The Glass Dome

> Вход: кадр 51 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
All scaffolding is gone. The building is fully restored and above its centre stands a NEW dome, completely different from the old one: a large stepped hemisphere built from clear glass blocks with a visible spiral ramp of stone stairs winding up inside it, bright and transparent against the sky. The facade is clean pale sandstone, the inscription intact, the black-red-gold flag on its pole. New lawns and paving in front.
```

### Кадр 53 · 2001 · The Queue

> Вход: кадр 52 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A long queue of visitors winds across the square to the entrance, with rope barriers and a security cabin. Tour coaches in a rank at the kerb, souvenir stalls, people photographing the dome from the lawn.
```

### Кадр 54 · 2005 · The Government Quarter

> Вход: кадр 53 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Behind and to the right of the building, where the wall once stood, a row of large modern government buildings in white concrete and glass now closes the view, connected by a long horizontal block. A new pedestrian bridge crosses in the distance. The square in front is finished with clean paving and mature lawns.
```

### Кадр 55 · 2006 · The Fan Zone

> Вход: кадр 54 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
A football festival fills the square: two enormous screens on scaffold towers facing a sea of tens of thousands of people, temporary barriers, food and drink stands along the edges. The crowd is waving small flags with three horizontal bands - black, red and gold - and no other nation's flag appears anywhere in the frame. Summer evening, screen glow on the faces, the building and its glass dome lit behind.
```

### Кадр 56 · 2010 · Solar and Cycles

> Вход: кадр 55 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Add rows of dark solar panels on the flat roof sections either side of the dome, a marked cycle lane across the square with a bicycle stand, modern benches and litter bins, and a line of young replacement trees. More casual visitors, fewer coaches.
```

### Кадр 57 · 2015 · Full Season

> Вход: кадр 56 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
Peak tourist season: the lawns covered with people sitting and picnicking, a long entrance queue, ice cream carts, segway tours, dozens of raised phones. Everything green and well kept. Bright warm day.
```

### Кадр 58 · 2020 · Empty

> Вход: кадр 57 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The square is almost deserted: the entrance closed with a barrier and a sign board carrying no readable words, only blocks of colour, the lawns empty, a handful of masked figures far apart, no coaches, no stalls. The building itself is unchanged and immaculate. Flat grey light.
```

### Кадр 59 · 2023 · Life Returns

> Вход: кадр 58 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
People are back: a moderate queue, groups on the lawns, cycle traffic, food trucks at the kerb, new flower planters. More greenery than before, some of the lawn replaced with wildflower meadow.
```

### Кадр 60 · 2026 · Present Day

> Вход: кадр 59 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
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
- Terrain rises in whole-block steps, never as a smooth slope.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.

Built from real Minecraft blocks: sandstone and smooth quartz for the stone
facade, oxidised copper for green roofs, red brick, stone bricks, deepslate,
cobblestone, spruce and oak planks, glass panes, glass blocks.

DETAIL DISCIPLINE - follow these exactly:
- Draw NO flag that is not described in the CHANGE text below. Never an American
  flag, never stars, never stripes of any other nation, never a generic flag.
- Draw NO lettering, NO signage and NO numbers unless the CHANGE text asks for it.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level on a large open square,
looking at the plot from a three-quarter angle: the wide west front of the
building faces the camera slightly turned to the left, so that both the long
front facade AND the shorter south side are visible, giving the building depth.
The building sits in the centre-right of the frame and its full height fits
with clear sky above it. The open square fills the foreground and the left
third. A dense treeline closes the far left. Open sky fills the right third
above a low horizon at 62% of frame height. 35mm equivalent, no lens
distortion, horizon perfectly level. Midday sun from the upper left, long soft
shadows falling to the lower right. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them,
never move them, never change their size or position:

- THE PLOT: the rectangular piece of ground in the centre-right of the frame.
  It is empty at the start, then holds the building for the rest of the series.
  Its footprint and position never change.

- THE BUILDING, from the year it is finished onward: a massive rectangular
  parliament building of pale sandstone blocks, 56 blocks wide and 16 blocks
  tall to the cornice. A projecting entrance portico of six tall square columns
  under a plain triangular pediment stands at the centre of the west front,
  reached by a wide flight of stone stairs. One square corner tower with a small
  stepped copper roof rises at each of the four corners. Regular rows of
  identical 1x2 glass-pane windows along the whole facade. Always this exact
  build on this exact spot.

- THE DOME, only in the years when it exists: a stepped dome built from glass
  blocks and copper stairs, standing directly above the centre of the building,
  clearly visible against the sky.

- THE TREELINE: a dense band of Minecraft trees closing the far left of the
  frame, the edge of a large park. Always there, in the same place.

- THE SQUARE: open ground in the foreground and left third, changing between
  gravel, grass and stone paving over the years but always the same open space.

- THE VICTORY COLUMN, only in the years when it stands: a tall fluted stone
  column on a square stepped stone base, standing in the LEFT third of the
  square, with a small gilded figure on top. It is erected in one year and
  removed in another, and in between it appears in every image, unchanged.

FLAG RULE: draw only the flag described in the CHANGE text, and nothing else.
Never an American flag, never stars, never any other nation's flag. When no
flag is described, the flagpoles are bare.

When the building is damaged or destroyed in a given year, it is still THIS
build in a damaged state: the same facade with blocks missing, the same portico,
the same corner towers. Never replace it with a different building, and never
make the ruins smooth or sculpted.

CHANGE:
The building today, at its best: clean pale sandstone, the glass dome bright above it, the black-red-gold flag on its pole and no other flag anywhere. Mature trees, wildflower meadow and lawns, modern benches, cycle lanes, a busy but relaxed crowd, the government quarter complete behind. Warm bright late-afternoon light, long shadows, the richest frame of the series.
```
