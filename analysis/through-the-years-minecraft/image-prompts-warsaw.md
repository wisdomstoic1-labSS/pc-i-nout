# Промпты картинок — 75 готовых блоков

Сгенерировано `tools/image_prompts.py` из `prompts-warsaw.md`.

Каждый блок — **целый промпт**: стиль, камера и инструкция кадра уже внутри.
Копировать целиком и вставлять, дописывать ничего не нужно.

**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:

```
smooth surfaces, rounded edges, curved walls, realistic geometry, photorealism, low-poly non-cubic shapes, sculpted terrain, HUD, crosshair, hotbar, inventory, user interface, text, letters, numbers, watermark, signature, logo, blurry, fisheye, distorted perspective, tilted horizon, changed art style
```

Кадр 1 генерится с нуля. Кадры 2-75 — правкой предыдущего кадра
(инструкционное редактирование, не text-to-image).
После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.

---

# ГРУППА A

### Кадр 1 · 8000 BC · Ice Age Valley

> Вход: ничего. Единственный кадр, который генерится с нуля (text-to-image).
> Это мастер-плита группы A — от неё зависят все 74 остальных кадра.
> Сгенерить 10-20 вариантов и выбрать вдумчиво, переделать потом = переделать всё.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

A post-glacial river valley with no humans and no buildings of any kind anywhere in the frame. The escarpment is bare: patches of gravel, sand and grey stone, sparse dwarf pines and thin birches, snow lying in the shaded hollows. The river is wide, pale and braided around gravel islands. Cold thin light, desaturated blue-grey palette, low pale sun.
```

### Кадр 2 · 3000 BC · Primeval Forest

> Вход: кадр 1 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Cover the escarpment and the far hills with dense primeval forest: tall dark oaks and limes in thick blocky canopy, no gaps, no clearings. Plant one huge solitary oak on the crest at the right third — taller and wider than all the others; it must stay in every following image. Still no humans and no buildings. Warm green summer palette.
```

### Кадр 3 · 1500 BC · First Clearing

> Вход: кадр 2 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Cut a small clearing into the forest at the centre of the crest. Place two low huts with thatched roofs and a small fenced pen. A thin column of smoke rises from one hut. Everything else stays exactly as before.
```

### Кадр 4 · 700 BC · Lusatian Settlement

> Вход: кадр 3 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Grow the clearing to about four times its size. Replace the two huts with eight timber houses arranged in a loose ring, surrounded by a low wooden palisade. Add small cultivated fields on the slope below and a footpath down to the river.
```

### Кадр 5 · 100 AD · Amber Route

> Вход: кадр 4 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Enlarge the settlement to about twenty houses. Add a beaten trade road running along the crest and out of the right side of the frame, with two loaded ox carts on it. Add a small landing stage with a log boat on the river bank.
```

### Кадр 6 · 400 · Abandoned

> Вход: кадр 5 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Destroy and abandon the settlement. The houses are burnt shells with collapsed roofs and blackened timbers; grass and saplings grow through the ruins; the palisade is broken and leaning. The fields are gone back to weeds. No people anywhere. Overcast grey light, desaturated palette.
```

### Кадр 7 · 700 · Slavic Settlement

> Вход: кадр 6 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Clear the ruins away. Build a new settlement of a different character on the same spot: fifteen sunken-floor huts with steep thatched roofs, a communal open space in the middle, a new palisade of split logs. Return warm summer light.
```

### Кадр 8 · 900 · The Stronghold

> Вход: кадр 7 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Build a proper stronghold on the crest: a high circular earth-and-timber rampart with a log palisade on top and a gate tower facing the river. The settlement moves inside the rampart. Add a defensive ditch on the landward side.
```

### Кадр 9 · 1000 · The First Cross

> Вход: кадр 8 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Add a small wooden church with a steep roof and a plain cross on the gable, standing just inside the stronghold gate. Add a small fenced graveyard beside it.
```

### Кадр 10 · 1100 · The Bridge

> Вход: кадр 9 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Build a long timber bridge on piles across the river, connecting the near bank to a track climbing the escarpment. Add a small suburb of a dozen houses outside the rampart on the slope.
```

### Кадр 11 · 1180 · The Mill

> Вход: кадр 10 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Add a water mill with a large wheel on the near bank at the left, and a small mill pond. Double the size of the suburb outside the rampart. Add more cultivated strips on the slope.
```

### Кадр 12 · 1230 · Jazdów

> Вход: кадр 11 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Replace the timber stronghold with a ducal seat: a two-storey timber-and-stone hall with a tiled roof inside the rampart, a stone gate tower, and a larger church with a bell turret. The suburb grows to thirty houses.
```

### Кадр 13 · 1262 · Raided

> Вход: кадр 12 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

The settlement has been raided and burnt. The ducal hall is a roofless shell, the palisade broken in three places, half the suburb houses reduced to charred frames. Fires still burning in two places, thick black smoke. Bodies of the dead are not shown. Ash on the ground.
```

### Кадр 14 · 1281 · Burnt Again

> Вход: кадр 13 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Total ruin. Even the stone gate tower is toppled, the rampart slumped and overgrown, nothing standing but broken walls and blackened stumps. The fires are out, only cold ash and grey light. The solitary oak on the right survives untouched.
```

### Кадр 15 · 1300 · Warszowa

> Вход: кадр 14 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Found a new town on the same crest, slightly to the left of the old ruined rampart, which stays visible as a grassy mound. The new town has a regular rectangular grid of forty timber houses with tiled roofs, a rectangular open market square in the middle, and a fresh timber palisade. Bright summer light.
```

### Кадр 16 · 1330 · Town Charter

> Вход: кадр 15 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Formalise the town: straight cobbled streets on the grid, a timber town hall in the centre of the market square, a weighhouse, and rows of narrow gabled merchant houses replacing the plain huts.
```

### Кадр 17 · 1350 · First Brick

> Вход: кадр 16 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Replace the twenty houses around the market square with brick ones — red brick walls, stepped gables, red tile roofs. Begin a large brick church at the north edge of the town: walls half-built, wooden scaffolding, a crane on top.
```

### Кадр 18 · 1370 · The Walls

> Вход: кадр 17 + мастер-плита группы A.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, wide establishing shot from a slightly elevated position on the flat east bank of a great river. The river runs across the lower third of the frame from the left edge to the right. Beyond it rises a wooded escarpment: a long steep bluff whose crest sits at 45% of frame height. The flattest point of that crest is dead centre of the frame. Low forested hills close the far background. 35mm equivalent field of view, no lens distortion, horizon perfectly level. Midday sun from the upper left, long soft shadows falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the lower left, the solitary oak on the crest at the right third.

Replace the timber palisade with a brick defensive wall with square towers and a gate house. Finish the church: tall brick nave and a slender tower with a spire. The town is now unmistakably a medieval brick town.
```

# ГРУППА B

### Кадр 19 · 1380 · Brick Town

> Вход: кадр 18. СМЕНА РАКУРСА — мастер-плита группы B.
> Сначала только переставить камеру (мир не трогать), результат сохранить
> как плиту B, и уже от неё вести цепочку дальше.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 20 · 1400 · The Collegiate

> Вход: кадр 19 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Enlarge the brick church into a tall Gothic collegiate: steep roof, high narrow windows, flying buttresses made of blocks, a taller spire that now dominates the skyline.
```

### Кадр 21 · 1408 · New Town

> Вход: кадр 20 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Add a second walled town immediately to the left, separated by a strip of open ground: its own smaller market square, its own church with a modest tower, its own gate.
```

### Кадр 22 · 1413 · Capital of Masovia

> Вход: кадр 21 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Replace the old ducal hall on the crest with a proper brick castle: four-storey main block, a tall square keep, crenellated walls, a courtyard, and a ducal banner on the keep.
```

### Кадр 23 · 1450 · Gothic

> Вход: кадр 22 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Raise every house in both towns to three storeys with steep tiled roofs and decorated stepped gables. Add a covered cloth hall in the main square.
```

### Кадр 24 · 1480 · The Barbican

> Вход: кадр 23 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Build a round brick barbican in front of the main gate, connected by a bridge over the moat. Thicken the walls and add three more towers.
```

### Кадр 25 · 1526 · Into the Crown

> Вход: кадр 24 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Replace the ducal banner on the keep with a royal one — a white eagle on red. Add a large stone royal coat of arms above the castle gate. Extend the castle with a new residential wing.
```

### Кадр 26 · 1550 · Renaissance

> Вход: кадр 25 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Renaissance rebuild: replace steep Gothic gables with flat decorative attic parapets, add arcaded loggias on the square, repaint the merchant houses in ochre, red, pale green and blue. Add a stone well in the middle of the market square.
```

### Кадр 27 · 1569 · The Sejm

> Вход: кадр 26 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Add a long low parliament hall with a colonnaded front beside the castle, and a large paved forecourt in front of it filled with parked carriages and horses.
```

### Кадр 28 · 1573 · Confederation

> Вход: кадр 27 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Add temporary wooden tribunes and rows of tents on the field outside the walls, with dozens of coloured banners of different noble houses.
```

### Кадр 29 · 1596 · The Court Arrives

> Вход: кадр 28 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Massively expand the castle: a new five-storey Renaissance front with a tall clock tower over the gate, formal gardens on the slope below. Cut down the solitary oak on the right — leave a wide fresh stump where it stood, to make room for the new wing.
```

### Кадр 30 · 1611 · Royal Residence

> Вход: кадр 29 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Finish the castle in early Baroque: symmetrical wings, a copper roof gone green, ornamental stone portal, guard posts. Pave the whole forecourt with fitted stone.
```

### Кадр 31 · 1620 · Baroque

> Вход: кадр 30 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Rebuild the merchant houses on the square in Baroque: curved decorative parapets, painted facades in cream, pink and pale blue, stone doorframes, shop signs hanging on iron brackets.
```

### Кадр 32 · 1637 · Expansion

> Вход: кадр 31 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Add three Baroque churches with domes and twin towers across the town, and two large noble palaces with courtyards and gated entrances.
```

### Кадр 33 · 1644 · The Column

> Вход: кадр 32 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

Erect a tall free-standing stone column in the middle of the castle forecourt, topped with a bronze statue of a crowned king holding a cross and a sabre. This column must appear in every following image.
```

### Кадр 34 · 1650 · Golden Age

> Вход: кадр 33 + мастер-плита группы B.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera on a locked tripod, medium-wide shot from the same direction as before but closer and slightly higher. The escarpment crest fills the middle band of the frame; the river shows only as a strip along the bottom edge. The ducal seat stands at the centre of the crest, the town spreads to the left. Horizon at 35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.

The city at its peak: every facade freshly painted, gilded details, flower boxes, full market, carriages everywhere, ships at the river landing. Bright warm golden light, richest colours of the whole video.
```

# ГРУППА C

### Кадр 35 · 1655 · THE DELUGE

> Вход: кадр 34. СМЕНА РАКУРСА — мастер-плита группы C.
> ВАЖНО: сначала отдельным шагом сгенерить МИРНЫЙ кадр 1650 года по камере C
> и сохранить его как плиту C. И уже этот мирный кадр разрушать промптом ниже —
> иначе пара «до/после» не сработает, зрителю нужно узнать те же здания.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

The same square, the same buildings, the same camera — sacked and burnt. Roofs collapsed, walls broken open, windows empty black holes, rubble across the cobbles, wrecked carts. The residence has lost its roof and one wing. Fires burning in three places, heavy black smoke across the sky. The column still stands, scorched but upright. Ash on everything, desaturated palette, red firelight.
```

### Кадр 36 · 1660 · Empty

> Вход: кадр 35 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

The fires are out. Cold grey ruins, ash washed grey by rain, weeds already growing between the cobbles, one leaning wall collapsed into the square. Flat overcast light, almost colourless. Two or three figures only.
```

### Кадр 37 · 1680 · Slow Rebuild

> Вход: кадр 36 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Rebuilding begins: scaffolding on three houses, fresh timber roof frames, stacks of brick and lime on the cobbles, a crane. Half the square is still ruins. Weak sunlight returning.
```

### Кадр 38 · 1700 · Baroque Restored

> Вход: кадр 37 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

The square is rebuilt in full Baroque: new roofs, cream and ochre facades, stone portals, the residence complete again with a green copper roof. Clean cobbles. Warm light returns.
```

### Кадр 39 · 1720 · Saxon Era

> Вход: кадр 38 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Heavier Baroque: add sculpted stone figures on the parapets, ornate iron lanterns on brackets, a decorative fountain at the left of the square. Guards in tall mitre caps at the residence gate.
```

### Кадр 40 · 1740 · The Lime Tree

> Вход: кадр 39 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Plant a young lime tree in a small stone surround at the right edge of the square. It must appear in every following image and grow steadily. Add formal clipped hedges along the residence wall.
```

### Кадр 41 · 1764 · Enlightenment

> Вход: кадр 40 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Add tall glazed shop windows at street level, painted signboards, a bookshop and a coffee house with tables on the cobbles. Street lamps on posts. The lime tree is now twice as tall.
```

### Кадр 42 · 1780 · Neoclassical

> Вход: кадр 41 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Reface the residence in neoclassical style: flat pilasters, a triangular pediment over the centre, restrained cream and white. Straighten and repave the square in a radial cobble pattern around the column.
```

### Кадр 43 · 1791 · Constitution Day

> Вход: кадр 42 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

A celebration: the square packed with people, garlands and flags strung between the buildings, decorative arches, banners on every facade. Bright festive light.
```

### Кадр 44 · 1794 · Uprising

> Вход: кадр 43 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Fighting in the square: overturned carts and paving stones built into barricades, smoke, broken windows, scattered debris, a torn flag on the barricade. Grim overcast light.
```

### Кадр 45 · 1795 · Occupied

> Вход: кадр 44 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Clear the barricades. Foreign soldiers in dark blue coats stand in formation across the square, a foreign eagle standard replaces the flags on the residence. Repaired but joyless facades, few civilians. Cold grey palette.
```

### Кадр 46 · 1807 · Duchy

> Вход: кадр 45 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Different foreign troops now: soldiers in blue and white with tall shakos, tricolour flags on the residence. Add a triumphal wooden arch at the left entrance to the square. Warmer light, more civilians back on the street.
```

### Кадр 47 · 1815 · Congress Kingdom

> Вход: кадр 46 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Another change of flags — a double-headed eagle standard on the residence. Add gas-free oil street lanterns on iron posts, a sentry box, and neat railings around the column base. Ordered, quiet, bureaucratic feel.
```

### Кадр 48 · 1831 · Uprising Crushed

> Вход: кадр 47 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

The square after the fighting: shell-pocked facades, one house roofless, broken lanterns, rubble against the residence wall, artillery pieces standing on the cobbles. Grey smoke, no celebration. The column stands undamaged.
```

### Кадр 49 · 1866 · Horse Trams

> Вход: кадр 48 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Industrial era arrives: repair everything, add a horse-drawn tram on rails crossing the square, telegraph poles with wires, large commercial shop windows, painted advertising on gable walls, gas street lamps.
```

### Кадр 50 · 1890 · Tenements

> Вход: кадр 49 + мастер-плита группы C.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level in the middle of an open cobbled city square. A tall free-standing column with a statue on top stands at the centre-left of the frame. The bulk of the royal residence closes the right half. A gate and the rooflines of the old town close the left. Sky occupies the top third. Horizon at 55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern of the square, the lime tree at the right edge of the square.

Raise the buildings on the left to five-storey tenements with iron balconies and elaborate stucco. Add awnings over the shopfronts, a newspaper kiosk, a flower stall at the column base. The lime tree is now full-grown.
```

# ГРУППА D

### Кадр 51 · 1900 · Belle Époque

> Вход: кадр 50. СМЕНА РАКУРСА — мастер-плита группы D.
> Сначала только переставить камеру, результат сохранить как плиту D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 52 · 1908 · Electric Trams

> Вход: кадр 51 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Replace horse trams with an electric tram: overhead wires and catenary poles across the square, a red-and-cream tram car with a pantograph. Add the first electric street lights.
```

### Кадр 53 · 1914 · War Begins

> Вход: кадр 52 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Mobilisation: recruitment posters pasted over the advertising, soldiers in grey with packs forming up, sandbags at the residence entrance, no civilian carriages. Cooler, drained palette.
```

### Кадр 54 · 1915 · Occupation

> Вход: кадр 53 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Occupation: foreign signage in a different alphabet over the shops, a checkpoint with a striped barrier at the left, few civilians, shuttered shops, ration queue along the residence wall. Bleak light.
```

### Кадр 55 · 1918 · Independence

> Вход: кадр 54 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Liberation: white-and-red flags on every single facade and on the residence, a huge crowd filling the square, banners, garlands. Bright breaking sunlight through the clouds.
```

### Кадр 56 · 1920 · Battle of Warsaw

> Вход: кадр 55 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Wartime again but defiant: sandbag emplacements, a field gun, military trucks, soldiers and volunteers including civilians with rifles, a field hospital tent with a red cross at the left. Smoke on the horizon beyond the roofs.
```

### Кадр 57 · 1926 · Recovery

> Вход: кадр 56 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Peacetime: clear all military presence, restore shopfronts, add early automobiles and a bus, new neon-lit signs, repaired facades, a newspaper vendor at the column.
```

### Кадр 58 · 1933 · Modernism

> Вход: кадр 57 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Add a tall modernist skyscraper of pale stone and glass rising behind the rooflines at the left — clearly the tallest thing in the city. Replace two facades with clean functionalist fronts. More cars, brighter neon.
```

### Кадр 59 · 1938 · Peak

> Вход: кадр 58 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

The city at its interwar best: everything clean and bright, full traffic, crowded pavements, glowing neon, flower stalls, awnings, the lime tree in full leaf. Warm golden late-afternoon light, rich saturated colour. Study this frame carefully — the next six frames destroy exactly these buildings.
```

### Кадр 60 · 1939 · The Bombing

> Вход: кадр 59 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

The same square under bombardment. Three buildings on the left are burning shells, the residence has lost its roof and the clock tower is broken off, craters in the cobbles, a wrecked tram on its side, fallen wires. Fires and heavy black smoke. The column still stands. Firelight and dust, desaturated except the flames.
```

### Кадр 61 · 1940 · Occupation

> Вход: кадр 60 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Occupied city: makeshift repairs with boarded windows, foreign flags on the residence, checkpoints with barriers, patrolling soldiers, occupation notices pasted on walls. Add a high brick wall topped with wire closing the left side of the square. Grey, drained palette.
```

### Кадр 62 · 1943 · Razed

> Вход: кадр 61 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Beyond the brick wall on the left, the entire district is flattened to an empty grey field of rubble stretching to the horizon — no standing buildings at all on that side. Smoke rising from it. The right side of the square still stands, boarded and grey.
```

### Кадр 63 · 1944 · Uprising

> Вход: кадр 62 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Street fighting: barricades of paving stones, overturned trams and furniture across the square, a white-and-red armband flag raised on the barricade, smoke everywhere, burning buildings, insurgents behind cover. The column is toppled — it lies broken across the cobbles, the statue face down.
```

### Кадр 64 · 1945 · Eighty-Five Percent

> Вход: кадр 63 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Total destruction. Not one intact building anywhere in frame. The residence is a jagged stump of wall. Every facade is a hollow shell or a mound of rubble. The square is buried under broken brick. The broken column lies where it fell. The lime tree is a blackened stump. Snow over the ruins, flat colourless winter light, no fires left, absolute silence.
```

### Кадр 65 · 1947 · Clearing

> Вход: кадр 64 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Rubble clearing: long human chains of civilians passing bricks hand to hand, sorted stacks of salvaged brick, narrow cleared paths through the debris, hand carts, a few tents. Still ruins, but organised. Weak spring light.
```

### Кадр 66 · 1953 · Rebuilt from Paintings

> Вход: кадр 65 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

The square rebuilt exactly as it looked in 1938 — same facades, same colours, same rooflines, but visibly brand new: crisp unweathered paint, fresh cobbles, new window frames. Scaffolding still on two buildings. The column is re-erected, repaired, standing again. Clear bright light.
```

### Кадр 67 · 1955 · The Palace

> Вход: кадр 66 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Add an enormous tiered stone tower with a spire rising far behind the rooflines at the right — monumental, far taller than anything else, dominating the whole skyline. Add period buses and a large propaganda banner across one facade.
```

### Кадр 68 · 1965 · Modernism

> Вход: кадр 67 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Add three plain concrete slab blocks behind the left rooflines, replace the old lamps with plain modern ones, add small boxy cars and a modern trolleybus, and plain state shop signage. The lime tree has regrown from its stump into a young tree again.
```

### Кадр 69 · 1980 · Strike

> Вход: кадр 68 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

A crowd rally in the square: hand-painted banners, a makeshift platform, thousands of people, no police visible. Damp cold light, drab clothing, but a dense determined crowd.
```

### Кадр 70 · 1989 · Transformation

> Вход: кадр 69 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

The first commercial signs appear over the plain state shops, a few Western cars among the boxy ones, market stalls with imported goods set up along the square, brighter clothing in the crowd.
```

### Кадр 71 · 2000 · Glass

> Вход: кадр 70 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Add two glass office towers rising behind the skyline at the left, replace the shopfronts with modern glazed ones and international brand signage, add modern street furniture, contemporary cars and a modern low-floor tram.
```

### Кадр 72 · 2015 · Skyline

> Вход: кадр 71 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Fill the background with a dense cluster of tall glass skyscrapers of varied heights. Add glass entrance pavilions for an underground station in the square, cycle lanes, planters and modern benches.
```

### Кадр 73 · 2026 · Present Day

> Вход: кадр 72 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Add one very tall slender tower clearly rising above all others at the back. Add outdoor café seating across the square, tourists with phones, food trucks, and the fully grown lime tree with a wide canopy. Warm bright day, the square fully pedestrianised.
```

### Кадр 74 · 2050 · Green Future

> Вход: кадр 73 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Near future: the towers are clad in vertical gardens and solar glass, the square has mature trees and water channels through the cobbles, silent driverless pods glide on a marked lane, drones move overhead, holographic information panels stand at the corners. The column and the lime tree are untouched and protected by a low rail. Clean bright optimistic light.
```

### Кадр 75 · 2075 · The Last Frame

> Вход: кадр 74 + мастер-плита группы D.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid seams on every face. No smooth curves, no rounded shapes, no organic silhouettes, no bevels, no sculpted detail. Rendered as a game screenshot through a modern shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky gradient, light atmospheric haze on the far background. No HUD, no crosshair, no hotbar, no interface, no hands, no held items, no text, no watermark, no signature.

Fixed camera at standing eye level, facing the royal residence head-on across the cobbled square. The facade and its clock tower fill the right two-thirds; the column stands at the left third with its statue against open sky. Horizon at 60% of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at the right edge.

Far future, and it has gone wrong: the green towers are dark and broken, vegetation overgrowing the square and pushing up through the cobbles, dead holographic panels flickering, a wrecked pod on its side, low mist, rain. The column still stands, weathered and leaning slightly. The lime tree is enormous, wilder than ever, roots cracking the stones. Dark blue-grey palette with cold neon glow from one dying sign.
```
