# Промпты картинок — 75 готовых блоков

Сгенерировано `tools/image_prompts.py` из `prompts-warsaw.md`.

Каждый блок — **целый промпт**: стиль, камера и инструкция кадра уже внутри.
Копировать целиком и вставлять, дописывать ничего не нужно.

**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:

```
smooth surfaces, curved walls, rounded domes, smooth arches, sculpted detail, sub-block detail, carved ornament, thin mouldings, marble sculpture, realistic statue, detailed face, cloth folds, high-poly, realistic geometry, photorealism, stylized voxel art, smooth gradients, soft rounded edges, high resolution textures, smooth terrain slope, rounded topiary tree, HUD, crosshair, hotbar, user interface, text, letters, numbers, watermark, signature, logo, blurry, fisheye, distorted perspective, tilted horizon, changed art style
```

## Самое важное

**Кадр 1 генерится с нуля. Кадры 2-75 — только правкой предыдущего кадра.**
В Gemini это значит: прикрепить картинку предыдущего кадра к запросу и
вставить блок промпта. Если генерить каждый кадр по одному тексту, без
приложенной картинки, модель будет каждый раз выдумывать заново и статую,
и здание — это предел технологии, промптом он не обходится.

В каждом блоке есть раздел ANCHOR OBJECTS с точным описанием повторяющихся
объектов: колонны со статуей короля, дворца с часовой башней, липы. Он
нужен, чтобы модель не изобретала новую статую на каждом кадре. Не сокращать.

После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.

---

# ГРУППА A

### Кадр 1 · 8000 BC · Ice Age Plain

> Вход: ничего. Единственный кадр, который генерится с нуля (text-to-image).
> Это мастер-плита группы A — от неё зависят все 74 остальных кадра.
> Сгенерить 10-20 вариантов и выбрать вдумчиво, переделать потом = переделать всё.

```
BASE IMAGE: none. This is the first frame of the series - generate it from scratch.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
A post-glacial river plain with no humans and no buildings anywhere. The wide shallow river braids around a bare sandy island of gravel and dune grass. Sparse dwarf pines and birches, patches of bare sand, snow in the shaded hollows. One huge grey glacial boulder on the near bank at the lower left. Cold thin light, desaturated blue-grey palette, low pale sun.
```

### Кадр 2 · 3000 BC · Primeval Forest

> Вход: кадр 1 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Cover the plain and the island with dense primeval forest of oak, lime and pine in thick blocky canopy. Plant one huge solitary oak on the island's north tip at the right third, far taller and wider than the rest; it must stay in every following image. Marshy reed beds along both banks. Still no humans, no buildings. Warm green summer palette.
```

### Кадр 3 · 1000 BC · First Fishers

> Вход: кадр 2 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Cut a small clearing on the island's south end. Place three low huts with reed-thatched roofs, a drying rack hung with fish, two dugout log boats pulled up on the sand. A thin column of smoke.
```

### Кадр 4 · 200 BC · Germanic Settlement

> Вход: кадр 3 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Grow the clearing to about ten timber longhouses with steep thatched roofs, a low wooden fence, small fields of barley on the mainland bank, a pen with cattle.
```

### Кадр 5 · 400 · Abandoned

> Вход: кадр 4 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Destroy and abandon the settlement. Burnt shells with collapsed roofs and blackened timbers, saplings growing through the ruins, the fence broken and leaning. Fields gone to weeds. No people. Overcast grey light, desaturated palette.
```

### Кадр 6 · 600 · The Sprevane

> Вход: кадр 5 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Clear the ruins. Build a new Slavic settlement of a different character on the island: fifteen small square huts with steep roofs, sunken floors, a communal open space, a palisade of split logs around the south end. Warm summer light returns.
```

### Кадр 7 · 800 · The Fishing Village

> Вход: кадр 6 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Extend the settlement along the whole east shore of the island. Add a plank landing stage with six boats, drying nets on frames, fish traps in the shallows, a track worn along the bank.
```

### Кадр 8 · 950 · The Stronghold

> Вход: кадр 7 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Build a stronghold on the island's high south end: a circular earth-and-timber rampart with a log palisade on top and a gate tower facing the water. The settlement moves inside. A defensive ditch cut across the island.
```

### Кадр 9 · 1100 · The Ford

> Вход: кадр 8 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Build a timber causeway and ford crossing both arms of the river, linking the island to each bank. Add a small suburb of a dozen houses on the west bank and a track climbing away from the water.
```

### Кадр 10 · 1157 · The Margrave

> Вход: кадр 9 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Replace the timber gate tower with a squat stone one flying a margrave's banner. Add a small stone chapel with a plain cross inside the rampart and a stone-walled enclosure for the garrison.
```

### Кадр 11 · 1200 · German Settlers

> Вход: кадр 10 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Add a planned grid of forty timber houses with tiled roofs on the west bank, and a second grid of thirty on the east bank: two separate new towns facing each other across the water. Straight streets, a market square in each.
```

### Кадр 12 · 1237 · Cölln

> Вход: кадр 11 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Fortify the west-bank town with a timber palisade and a gate, and build a brick parish church with a squat tower at its market square. Add a proper timber bridge on piles replacing the ford.
```

### Кадр 13 · 1244 · Berlin

> Вход: кадр 12 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Fortify the east-bank town the same way, with its own palisade, gate and brick church with a taller tower. The two towns now mirror each other across the river.
```

### Кадр 14 · 1280 · The Twin Towns

> Вход: кадр 13 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Raise every house in both towns to two storeys with steep tiled roofs and stepped brick gables. Replace both palisades with a low brick wall. Add a covered market hall on each square.
```

### Кадр 15 · 1307 · United

> Вход: кадр 14 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Build a single shared town hall on the bridge itself, straddling the water between the two towns, with a tall slender tower and one large clock. Both towns now fly the same banner.
```

### Кадр 16 · 1350 · Brick Gothic

> Вход: кадр 15 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
Rebuild both churches as tall brick Gothic halls with steep roofs and slender spires that dominate the skyline. Raise the town walls to full height with square towers and three gates.
```

### Кадр 17 · 1380 · The Great Fire

> Вход: кадр 16 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
A large part of the east-bank town has burnt. Twenty houses are charred frames with collapsed roofs, two streets are ash, one church tower is blackened and roofless. Fires still burning in three places, heavy black smoke rolling across the sky. The west-bank town is untouched. The solitary oak survives.
```

### Кадр 18 · 1400 · Rebuilt in Brick

> Вход: кадр 17 + мастер-плита группы A.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

ANCHOR OBJECTS - the same physical objects in every image of this group.
Never redesign them, never move them, never change their size or shape:
- THE RIVER: a wide river crossing the lower third of the frame from the left edge
  to the right, with one distinctive bend curving toward the viewer. The bend keeps
  exactly the same shape in every image.
- THE BOULDER: one large grey rounded boulder, about 2 blocks wide, lying on the
  near bank at the lower left. Always in the same spot, never moved, never removed.
- THE OAK: one huge solitary oak on the crest at the right third, far taller and
  wider than any other tree, thick dark trunk, broad rounded canopy. Always the
  same tree in the same place.

CHANGE:
The burnt quarter is rebuilt entirely in red brick with tiled roofs — visibly newer and more regular than the rest. Scaffolding still on two buildings. The blackened church tower is repaired with a new spire. Clean bright light.
```

# ГРУППА B

### Кадр 19 · 1443 · The Elector's Castle

> Вход: кадр 18. СМЕНА РАКУРСА — мастер-плита группы B.
> Сначала только переставить камеру (мир не трогать), результат сохранить
> как плиту B, и уже от неё вести цепочку дальше.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 20 · 1451 · The Residence

> Вход: кадр 19 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Finish the castle: a compact brick fortress with four corner towers, crenellations, a gatehouse with a drawbridge over a water channel, and the Elector's banner on the tallest tower.
```

### Кадр 21 · 1465 · The Chapel

> Вход: кадр 20 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Add a tall Gothic chapel against the castle's river side, with high narrow windows and a slender spire. Add a walled garden between the castle and the water.
```

### Кадр 22 · 1500 · Gothic Complete

> Вход: кадр 21 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Extend the castle into a full quadrangle around a courtyard, all in brick with stepped gables. Both towns behind it grow denser, three storeys, new brick warehouses along the waterfront.
```

### Кадр 23 · 1538 · Renaissance

> Вход: кадр 22 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Rebuild the castle in Renaissance style: replace the stepped Gothic gables with flat decorative attic parapets, add arcaded loggias on the courtyard side, sandstone window surrounds, and repaint the walls pale ochre. A round stair tower on the front.
```

### Кадр 24 · 1573 · The Lustgarten

> Вход: кадр 23 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Lay out a large formal garden on the flat ground north of the castle: geometric hedged beds, gravel paths in a grid, a low stone balustrade along the river edge, rows of young clipped trees.
```

### Кадр 25 · 1600 · Prosperity

> Вход: кадр 24 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Both towns at their Renaissance best: painted facades in ochre, red and pale green, arcades along the market squares, a stone fountain in each, ships at the waterfront. Bright warm light.
```

### Кадр 26 · 1618 · War Begins

> Вход: кадр 25 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Fortify everything: earthwork bastions with pointed corners thrown up around both towns, cannon on the ramparts, soldiers drilling on the Lustgarten, supply wagons parked in rows. The gardens are trampled.
```

### Кадр 27 · 1637 · Plague and Occupation

> Вход: кадр 26 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
The towns are half empty and grey. Many houses stand shuttered with white marks painted on the doors, roofs are falling in, weeds grow in the market squares, a burial cart stands in the street. Foreign soldiers camp in the trampled Lustgarten. Overcast, drained palette, very few people.
```

### Кадр 28 · 1648 · Peace

> Вход: кадр 27 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
The soldiers are gone and the camp is cleared, but the damage stays: gaps where houses collapsed, patched roofs, the bastions eroding, the Lustgarten a weed field. A few people return, carts of belongings on the bridge. Weak sunlight breaking through.
```

### Кадр 29 · 1660 · The Great Elector

> Вход: кадр 28 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Rebuild in force: new star-shaped stone fortifications with proper bastions and a moat around both towns, repaired houses, a new arsenal building, the Lustgarten replanted in a strict geometric pattern.
```

### Кадр 30 · 1685 · The Huguenots

> Вход: кадр 29 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
A whole new quarter of neat identical French-style houses appears on the west bank, with a plain new church. The streets are busier and more prosperous. Cut down the solitary oak on the island's north tip — leave a fresh wide stump where it stood, to clear ground for building.
```

### Кадр 31 · 1695 · The Arsenal

> Вход: кадр 30 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
Build a large square baroque arsenal of pale sandstone with a courtyard, on the mainland beside the bridge. Add the first straight tree-lined avenue running west out of the frame.
```

### Кадр 32 · 1699 · Schlüter Begins

> Вход: кадр 31 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
The Renaissance castle is being wrapped in a new baroque shell: the north wing already rebuilt in pale sandstone with tall regular windows and a heavy cornice; the rest still in old brick and covered in scaffolding.
```

### Кадр 33 · 1701 · Kingdom of Prussia

> Вход: кадр 32 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
A coronation celebration: banners on every facade, garlands strung across the streets, a huge crowd filling the Lustgarten and the bridge, a procession of carriages and mounted guards. Bright festive light.
```

### Кадр 34 · 1713 · The Baroque Palace

> Вход: кадр 33 + мастер-плита группы B.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

ANCHOR OBJECTS - the same physical objects in every image. Never redesign them:
- THE OAK: one huge solitary oak at the right third, thick dark trunk, broad rounded
  canopy, far larger than any other tree. Same tree, same place, until the year it
  is explicitly cut down.
- THE CREST LINE: the silhouette of the escarpment edge keeps exactly the same
  profile in every image.
- THE PALACE, once it exists: a long rectangular palace, 4 storeys, warm terracotta-red
  brick walls with pale cream stone corner quoins and window frames, a steep green
  oxidised-copper roof. One square clock tower rises from the centre of the facade
  with a round clock face and a slim copper-green spire. Two smaller copper-domed
  turrets, one at each end of the roof. Always this exact building.

CHANGE:
The palace is finished: a huge rectangular baroque block of pale sandstone around a courtyard, three storeys of tall regular windows, a heavy cornice, sculpted parapet figures, a grand portal. It dominates the island completely. Golden warm light, the richest frame of the group.
```

# ГРУППА C

### Кадр 35 · 1740 · Frederick the Great

> Вход: кадр 34. СМЕНА РАКУРСА — мастер-плита группы C.
> ВАЖНО: сначала отдельным шагом сгенерить МИРНЫЙ кадр 1650 года по камере C
> и сохранить его как плиту C. И уже этот мирный кадр разрушать промптом ниже —
> иначе пара «до/после» не сработает, зрителю нужно узнать те же здания.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Same palace seen from the square per CAMERA C. Add a guard house with sentries at the palace portal, ranks of soldiers in tricorn hats drilling on the paving, and a row of clipped lime trees along the Lustgarten balustrade.
```

### Кадр 36 · 1750 · The First Cathedral

> Вход: кадр 35 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Build a modest baroque cathedral at the far end of the Lustgarten: a plain rectangular block of pale stone with a small copper dome and a columned porch.
```

### Кадр 37 · 1770 · Enlightenment

> Вход: кадр 36 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Add tall glazed shop windows and painted signboards along the street at the left, an opera house facade visible in the distance, oil street lamps on iron posts, and well-dressed people walking the Lustgarten paths.
```

### Кадр 38 · 1791 · The Gate

> Вход: кадр 37 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
A new columned triumphal gate topped with a four-horse chariot appears far in the distance at the end of the long straight avenue, small but clearly visible on the horizon.
```

### Кадр 39 · 1806 · Napoleon

> Вход: кадр 38 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Occupation: foreign troops in blue coats with tall shakos drawn up in ranks across the square, a foreign eagle standard on the palace, artillery parked by the balustrade, few civilians and those hurrying. The distant gate stands stripped — its chariot is gone. Cold grey light.
```

### Кадр 40 · 1814 · The Quadriga Returns

> Вход: кадр 39 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Celebration: the chariot is back on the distant gate, Prussian flags on every facade, garlands, a crowd filling the square and the Lustgarten, a returning column of troops marching in. Plant a young lime tree at the left edge of the Lustgarten in a stone surround — it must appear in every following image and grow steadily.
```

### Кадр 41 · 1830 · Schinkel

> Вход: кадр 40 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Build a long neoclassical museum along the north side of the Lustgarten: a wide flight of steps and a screen of eighteen tall columns under a plain entablature. Re-lay the Lustgarten as a flat open parade ground with a granite bowl in the centre.
```

### Кадр 42 · 1848 · Revolution

> Вход: кадр 41 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Fighting on the square: barricades of overturned carts, paving stones and furniture, black-red-gold flags on the barricades, broken windows, smoke drifting, scattered debris, troops facing the barricades from the palace side. Grim overcast light.
```

### Кадр 43 · 1853 · The Dome

> Вход: кадр 42 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Clear the barricades and repair the square. Add a tall stepped copper dome with a lantern on top over the palace's grand portal — it changes the palace silhouette completely and must appear in every following image.
```

### Кадр 44 · 1871 · The Empire

> Вход: кадр 43 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Imperial celebration: black-white-red flags on every facade and on the palace dome, a victory parade of troops and captured cannon crossing the square, dense crowd behind barriers, garlands on the museum columns.
```

### Кадр 45 · 1880 · Gründerzeit

> Вход: кадр 44 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Wealth: gas lamps on ornate posts, a horse tram on rails crossing the square, hackney carriages in a rank, elaborate stone facades with sculpture on the street at the left, painted advertising on gable walls.
```

### Кадр 46 · 1894 · Cleared

> Вход: кадр 45 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The old baroque cathedral is gone — in its place a fenced building site with foundation trenches, stacks of stone, a tall wooden crane and rails for spoil carts. The far end of the Lustgarten is open sky.
```

### Кадр 47 · 1905 · The Cathedral

> Вход: кадр 46 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Complete the new cathedral: a massive stone building with a huge oxidised-copper dome on a drum, four smaller corner domes, and a wide flight of steps down to the Lustgarten. It is now the tallest thing in the frame and must appear in every following image.
```

### Кадр 48 · 1910 · Electric

> Вход: кадр 47 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Replace the horse tram with an electric one: overhead wires and catenary poles across the square, a red-and-cream tram car with a pantograph. Add the first motor cars, electric street lights, and a newspaper kiosk.
```

### Кадр 49 · 1914 · War Begins

> Вход: кадр 48 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Mobilisation: a huge crowd packed onto the square and the Lustgarten steps, mobilisation posters pasted over the kiosk and the walls, columns of soldiers in field grey marching past with packs, families waving.
```

### Кадр 50 · 1918 · The Republic

> Вход: кадр 49 + мастер-плита группы C.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
November: a dense crowd filling the square in winter coats, red flags everywhere, a speaker on the palace balcony above the portal, soldiers with red armbands and no officers, a truck with armed men. Cold grey light, bare trees.
```

# ГРУППА D

### Кадр 51 · 1920 · Weimar

> Вход: кадр 50. СМЕНА РАКУРСА — мастер-плита группы D.
> Сначала только переставить камеру, результат сохранить как плиту D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 52 · 1926 · Golden Twenties

> Вход: кадр 51 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Add neon signs on the buildings at the left, a cinema front, taxis in a rank, well-dressed crowds, a flower stall, and the first traffic tower with signal lights in the middle of the square.
```

### Кадр 53 · 1933 · The Flags

> Вход: кадр 52 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Long red banners with a black emblem hang the full height of the palace facade and from every building. A torchlit column marches across the square in ranks. Crowd behind barriers with raised arms. Dark evening light, orange torch glow.
```

### Кадр 54 · 1936 · The Games

> Вход: кадр 53 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Olympic decoration: five-ring banners alongside the red ones, flagpoles in a long row across the square, visitors with cameras, tour buses, everything scrubbed and repainted. Bright summer light.
```

### Кадр 55 · 1939 · War Again

> Вход: кадр 54 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Sandbags stacked around the palace portal and the cathedral doors, windows taped in crosses, blackout paint on the lamps, an anti-aircraft gun on the Lustgarten, ration queue along the wall, almost no cars. Grey drained palette.
```

### Кадр 56 · 1943 · Burning

> Вход: кадр 55 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The palace is on fire: the roof burning along its whole length, flames out of the upper windows, the copper dome blackened and half collapsed, heavy black smoke across the sky. Craters in the square, a wrecked tram, fallen wires. The cathedral dome is damaged but standing. Firelight and dust.
```

### Кадр 57 · 1945 · Ruins

> Вход: кадр 56 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Total ruin. The palace is a roofless burnt-out shell of blackened walls with empty window openings, the dome gone, rubble across the square. The cathedral stands hollow, its big dome pierced and open to the sky. Wrecked vehicles, a Soviet flag on the palace, snow over the rubble. Flat colourless winter light, no fires left.
```

### Кадр 58 · 1947 · Clearing

> Вход: кадр 57 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Rubble clearing: long chains of women passing bricks hand to hand, sorted stacks of salvaged brick, narrow cleared paths through the debris, hand carts, a light railway with spoil tips. The ruins still stand behind. Weak spring light.
```

### Кадр 59 · 1950 · Demolition

> Вход: кадр 58 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The palace ruin is being blown up and pulled down: one wing already gone to a low heap, the rest half demolished with a wrecking crew and a demolition charge dust cloud, a bulldozer, spectators behind a rope. This is deliberate, organised destruction, not war damage. The cathedral shell still stands at the left.
```

### Кадр 60 · 1951 · Marx-Engels-Platz

> Вход: кадр 59 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The plot is completely empty: a vast flat parade ground of grey concrete slabs where the palace stood, marked with white lines for formations, a reviewing stand along one edge, flagpoles in a row. Nothing at all in the centre of the frame. The repaired cathedral stands alone at the left.
```

### Кадр 61 · 1961 · The Wall

> Вход: кадр 60 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Add a grey concrete barrier wall with a rounded top running across the far background beyond the river, with a watchtower and a cleared strip of raked sand in front of it. Border guards. The parade ground is unchanged and empty.
```

### Кадр 62 · 1969 · The Tower

> Вход: кадр 61 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
A tall slender concrete television tower with a steel sphere near its top rises far behind the rooflines, dominating the whole skyline. Add boxy cars, a modern tram, and plain concrete blocks along the far side of the square.
```

### Кадр 63 · 1976 · Palace of the Republic

> Вход: кадр 62 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
A completely different building now fills the empty plot: a wide low modernist block, four storeys, a flat roof, and a continuous facade of bronze mirror glass reflecting the sky. White lettering above the entrance. Fountains and concrete planters in front. It is not the old palace and looks nothing like it.
```

### Кадр 64 · 1980 · Everyday

> Вход: кадр 63 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Ordinary GDR life: queues at a kiosk, families with prams, a Trabant parked at the kerb, a propaganda banner across one facade, plain state signage, litter bins, unkempt planters.
```

### Кадр 65 · 1989 · The Wall Falls

> Вход: кадр 64 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Celebration: an enormous crowd packed across the square, people on top of the distant wall, flags, banners, cameras, champagne, a section of the wall broken open with a crowd pouring through. Cold night light, flash-lit faces, breath steaming.
```

### Кадр 66 · 1990 · Reunification

> Вход: кадр 65 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The wall is gone, only a line of different paving where it stood. Black-red-gold flags on the Palace of the Republic and the cathedral. Western cars among the Trabants, new advertising, market stalls with imported goods.
```

### Кадр 67 · 1995 · Closed

> Вход: кадр 66 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The Palace of the Republic is shut: doors chained, windows dark, hazard tape across the entrance, warning signs on a fence around it, weeds in the cracked plaza, the bronze glass dulled. Everything around it is modernising.
```

### Кадр 68 · 2003 · Stripped

> Вход: кадр 67 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The Palace of the Republic is gutted to its bare steel frame: all the bronze glass removed, floors and walls stripped out, the skeleton open to the sky, wrapped in scaffolding and safety netting. Contractor huts and machinery around it.
```

### Кадр 69 · 2008 · Empty Again

> Вход: кадр 68 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The plot is empty for the second time in the video: a flat expanse of rough grass and gravel where the building stood, a temporary path across it, a few benches, a construction hoarding along one side. Nothing in the centre of the frame. The cathedral at the left is fully restored and gleaming.
```

### Кадр 70 · 2013 · Rebuilding

> Вход: кадр 69 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
A deep excavation and a forest of tower cranes on the plot, concrete cores rising, the first sandstone facade panels going up on the corner — clearly a reconstruction of the old baroque palace, its window rhythm already recognisable. Hoardings printed with the finished design.
```

### Кадр 71 · 2020 · The Palace Returns

> Вход: кадр 70 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The palace stands again: the same pale sandstone baroque facade, the same window rhythm, the same grand portal and the stepped dome with its lantern — but one side is a plain modern facade of glass and pale concrete, deliberately different. New paving, young trees, visitors on the steps.
```

### Кадр 72 · 2026 · Present Day

> Вход: кадр 71 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Add outdoor cafe seating on the square, food carts, tourists with phones, cycle lanes, planters and modern benches, a cluster of glass towers far behind the rooflines, the lime tree at the left now fully grown with a wide canopy. Warm bright day.
```

### Кадр 73 · 2040 · Green City

> Вход: кадр 72 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The square is planted with mature trees and water channels through the paving, the far towers are clad in vertical gardens and solar glass, silent driverless pods glide on a marked lane, drones overhead, holographic information panels at the corners. The palace and the cathedral are untouched.
```

### Кадр 74 · 2055 · High Water

> Вход: кадр 73 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
The river has risen: a tall flood barrier of glass and steel runs along the river edge where the balustrade was, water standing high against it, the lower square raised on a new deck. More greenery, fewer vehicles, solar canopies over the paving. Overcast, humid light.
```

### Кадр 75 · 2075 · The Last Frame

> Вход: кадр 74 + мастер-плита группы D.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that
image, not by drawing a new scene from scratch. Keep its camera position, framing,
horizon line, perspective, lighting and every anchor object exactly as they already
are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block textures, rendered with a shader pack such as Complementary or BSL.
STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof, step and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Domes, arches and round towers are approximated with stairs and slabs, and the stair-stepping is clearly visible in the silhouette.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window frames. A window is one or two glass-pane blocks. A cornice is one row of stairs.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse 16x16 pixel texture. No smooth gradients across a surface, no baked sculptural shading.
- Terrain rises in whole-block steps, never as a smooth slope. Water sits as a flat surface at block level.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky cloud of cubic leaf blocks with noisy leaf texture. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
Built from real Minecraft blocks: red terracotta and bricks, smooth stone and quartz for trim, oxidised copper for green roofs, spruce and oak planks, stone bricks, deepslate, cobblestone, glass panes.
No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held items, no text, no watermark.

CAMERA:
Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

ANCHOR OBJECTS - these are the SAME physical objects in every single image.
Never redesign them, never invent a different version of them:
- THE COLUMN AND ITS STATUE, and it must look BUILT out of blocks, never sculpted:
  the column is a 2x2 shaft of smooth stone blocks, 16 blocks tall, on a wide stepped
  stone-brick plinth of 4 tiers. On top stands a figure built from oxidised copper
  blocks, 10 blocks tall, which must READ CLEARLY AS A CROWNED KING even though it is
  built from cubes. Silhouette from top to bottom: a crown of 4 copper stairs facing
  outward; below it ONE block for the head; below that shoulders 3 blocks wide; a body
  2 blocks wide and 4 blocks tall widening to 4 blocks at the base like a stiff robe.
  THE TWO ARMS ARE NOT SYMMETRICAL: the RIGHT arm is RAISED as a 1x1 column of 3
  blocks with a cross of five blocks in a plus shape above it; the LEFT arm HANGS DOWN
  along the body as a 1x1 column of 3 blocks with a sabre of three blocks stepping
  diagonally away from it. One arm up with a cross, one arm down with a sabre - never
  both arms in the same pose. NO face, NO armour detail, NO cloth folds, NO smooth
  curves, NO sculpted anatomy. It is ALWAYS this same build - same crown, same block cross in
  the right hand, same block sabre in the left, same copper colour, same height.
  NEVER replace it with an angel, an eagle, an orb, a globe, a woman, a soldier, a
  horse, or any other figure.
- THE PALACE, a Minecraft build on the block grid: a rectangular building 40 blocks
  long and 10 blocks tall to the eaves, walls of red terracotta and brick blocks with
  smooth quartz corner columns. Windows are identical 1x2 glass-pane openings in a
  regular row. The roof is oxidised copper blocks and copper stairs in a simple
  stepped gable, no curves. One square clock tower 8 blocks wide rises 12 blocks above
  the roof, with a flat square clock face on its front and a stepped copper spire of
  stairs and slabs above it. Two smaller stepped copper turrets, one at each end of
  the roof. Always this exact build in this exact place.
- THE LIME TREE: one Minecraft tree at the right edge of the square, in a small square
  stone surround - a straight 1x1 trunk of oak logs with a blocky cloud of cubic leaf
  blocks above it. Never a smooth rounded topiary. Always the same tree in the same spot.
- THE COBBLES: the square is paved in grey cobblestone in a radial pattern around the
  column. Same paving in every image.

When an anchor is damaged or destroyed in a given year, it is still THIS object in a
damaged state: the same statue lying broken on the ground, the same palace burnt out,
the same tree reduced to a charred stump. Never swap it for a different design.

CHANGE:
Far future, gone wrong: the green towers dark and broken, vegetation overgrowing the square and pushing through the paving, dead holographic panels flickering, the flood barrier breached with water across part of the square, a wrecked pod on its side. The palace still stands, weathered and stained. The cathedral dome is green and overgrown. The lime tree is enormous and wild, its roots cracking the stones. Low mist, rain, dark blue-grey palette with cold neon from one dying sign.
```
