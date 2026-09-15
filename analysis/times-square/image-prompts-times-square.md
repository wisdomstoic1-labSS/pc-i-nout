# Промпты картинок — Times-square, 75 готовых блоков

Сгенерировано `tools/image_prompts.py` из `prompts-times-square.md`.
Стиль, камеры и якоря взяты из того же файла — правишь их там, перезапускаешь скрипт.

Каждый блок — **целый промпт**. Копировать целиком, дописывать ничего не нужно.

**Негатив у всех 75 кадров одинаковый**, вбить один раз и не менять:

```
real brand, real logo, trademark, corporate logo, recognisable company name,
American flag on buildings that do not have one, other nation's flag, smooth
surfaces, curved walls, sculpted detail, sub-block detail, carved ornament,
photorealism, stylized voxel art, smooth gradients, high resolution textures,
rounded topiary tree, horse next to a modern tram, HUD, crosshair, hotbar,
user interface, watermark, signature, blurry, fisheye, distorted perspective,
tilted horizon, changed art style, split screen, collage, border
```

## Самое важное

**Кадр 1 генерится с нуля. Кадры 2-75 — только правкой предыдущего кадра.**
В Gemini это значит: прикрепить картинку предыдущего кадра и вставить блок.
Без приложенной картинки модель будет каждый раз выдумывать объекты заново —
это предел технологии, промптом он не обходится.

После каждой генерации вернуть фон и якоря композитом из мастер-плиты группы.

---

### Кадр 1 · 1800 · Woodland

> Вход: ничего. Единственный кадр с нуля (text-to-image). Это мастер-плита всего
> ролика — от неё зависят 59 остальных. Сгенерить 10–20 вариантов и выбирать
> придирчиво: важно, чтобы сходящиеся улицы и треугольник в центре встали ровно
> так, как описано в камере, иначе поплывёт весь ролик.
> 
> ---
> 
> # ПРОЛОГ

```
BASE IMAGE: none. This is the first frame of the series - generate it from scratch.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Open countryside with no town of any kind. A rutted dirt road runs away from the camera and forks around a low wedge of rough grass and scrub dead centre of the frame, where a second track joins it. Scattered oaks and a small stream crossing the near ground. Split-rail fences, tall grass, a few grazing cows in the distance. Low wooded hills on the horizon. Bright clear morning, rich greens, nothing built anywhere.
```

### Кадр 2 · 1840 · The Farm

> Вход: кадр 1 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Add a working farm: a two-storey timber farmhouse with a shingled roof on the left side of the frame, a large red barn behind it, split-rail paddocks with horses, a well with a bucket, and ploughed strips beyond. The dirt road is wider and rutted with cart tracks. The central wedge of ground is still empty scrub.
```

### Кадр 3 · 1860 · The Grid Arrives

> Вход: кадр 2 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The farm is gone. The land has been levelled and surveyed into a city grid: two wide graded dirt avenues now converge on the central wedge, marked out with wooden survey stakes and rope lines. Stacks of paving stone and timber at the roadside, a surveyor's tripod, a few labourers. Bare earth everywhere, no buildings yet, telegraph poles along one side.
```

### Кадр 4 · 1872 · Longacre Square

> Вход: кадр 3 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
A carriage district has grown up: low three-storey brick buildings line both avenues, with carriage-works, stables and blacksmith shops at street level. Painted wooden trade signs above the doors carrying invented short words only. Hay wagons, horse troughs, piles of harness. Gas lamps on iron posts. The central wedge holds a small two-storey brick building with a flat roof. Cobbled roadways.
```

### Кадр 5 · 1880 · Horsecars

> Вход: кадр 4 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Add a tram line down each avenue: steel rails set flush into the cobbles, with an open four-wheeled tram car running on them, pulled by two horses in harness walking between the rails. No engine, no overhead wires, no poles or cables above. A small wooden waiting shelter at the kerb. More people on the pavement, more painted trade signs.
```

### Кадр 6 · 1888 · The Carriage Trade

> Вход: кадр 5 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The district is at its busiest: long rows of finished carriages parked at the kerb, wide-open workshop doors showing wheels and frames inside, a five-storey brick carriage works on the left corner with big arched windows. Overhead a dense web of telegraph and telephone wires on tall poles crossing the avenues.
```

### Кадр 7 · 1895 · The First Theatre

> Вход: кадр 6 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
A large theatre appears on the left side: an ornate brick and stone facade four storeys tall with a wide canopy over the pavement and a row of tall arc lamps on brackets above it, throwing hard white light. The first electric sign in the frame sits above the canopy - a rectangle of glowing blocks with an invented short word on it. Evening light, the rest of the street still on gas.
```

### Кадр 8 · 1899 · The Hotel on the Triangle

> Вход: кадр 7 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Replace the small brick building on the central wedge with a tall narrow hotel filling the whole triangle: nine storeys of dark brick with a steep mansard roof, bay windows and a corner entrance at its sharp point. It is now the tallest thing in the frame. Two more theatres along the avenues, more electric signs.
```

### Кадр 9 · 1903 · Digging

> Вход: кадр 8 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The hotel is gone. The central wedge is a deep excavation pit with stepped rock sides, timber hoardings around it, two tall wooden cranes, stacks of steel beams and a spoil chute. The avenues on both sides are torn open in long trenches for a subway, with timber shoring and plank walkways over them. Mud everywhere.
```

### Кадр 10 · 1904 · The Tower

> Вход: кадр 9 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
On the wedge stands a new tower: narrow, about 10 blocks wide at its point and 26 blocks tall, faced in pale stone, with tall arched windows, a stepped cornice and a small ornamental turret on top. It is by far the tallest thing in the frame and must appear in every following image. The trenches are filled and the avenues repaved. Crowds below.
```

### Кадр 11 · 1905 · The Subway

> Вход: кадр 10 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Add a cast-iron and glass subway entrance kiosk with a domed roof at the kerb in front of the tower, with steps leading down and an ornate railing. Newsstands on the corners. More pedestrians, a queue at the kiosk.
```

### Кадр 12 · 1907 · The First Ball

> Вход: кадр 11 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Night. A dense crowd fills both avenues from edge to edge, tens of thousands of small figures. A glowing ball of lit blocks sits at the top of the tower's turret. Every window in the frame is lit. Confetti in the air. The lit signs are bright against a black sky.
```

### Кадр 13 · 1910 · Electric Signs

> Вход: кадр 12 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Daytime. Large illuminated signs now cover the upper facades on both sides: rectangles of glowing blocks bordered by rows of small bright bulbs, each carrying an invented short word or an abstract silhouette. No real brands anywhere. Overhead trolley wires on catenary poles, an electric tram with a pantograph on the rails, the horses gone completely.
```

### Кадр 14 · 1913 · Automobiles

> Вход: кадр 13 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The street is full of early motor cars with high bodies and spoked wheels, mixed with a few remaining horse carriages. A traffic policeman on a small stand in the road. Larger signs, more of them, and the first sign with moving light patterns.
```

### Кадр 15 · 1917 · Wartime

> Вход: кадр 14 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Mobilisation: a column of soldiers in uniform marching down one avenue, a wooden recruiting booth on the pavement, crowds waving. One flag hangs from the tower with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its upper corner; no other nation's flag appears anywhere. Printed notices on boards carrying no readable words, only blocks of colour.
```

### Кадр 16 · 1920 · Prohibition

> Вход: кадр 15 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Peacetime and prosperous: the soldiers gone, more cars, women in shorter coats, a policeman at the kerb. Signs are bigger and there are more of them, with the first animated sign showing a simple silhouette figure in motion. Basement stairways with plain unmarked doors under two buildings.
```

### Кадр 17 · 1923 · The Great White Way

> Вход: кадр 16 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Night, and the whole frame is lit by signs: every upper facade on both sides is covered in glowing rectangles outlined by bulbs, so bright that there are no dark surfaces left anywhere. Theatre canopies below, all lit. The tower carries a large sign of its own. Dense evening crowd, cars nose to tail.
```

### Кадр 18 · 1925 · Peak Bulbs

> Вход: кадр 17 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Even more: signs now stacked three high on some buildings and projecting out over the roadway on steel frames. A huge animated sign on the right shows a silhouette pouring from a jug, cycling in steps. Theatre marquees with rows of bulbs around them.
```

### Кадр 19 · 1928 · The Zipper

> Вход: кадр 18 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 20 · 1929 · The Crash

> Вход: кадр 19 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
A large crowd packed in the street below the tower, all facing up at the news ribbon, still and silent rather than celebrating. Men in hats holding newspapers. Grey overcast day, the signs unlit in daylight, a heavy quiet mood.
```

### Кадр 21 · 1931 · Burlesque

> Вход: кадр 20 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The street is shabbier: several shopfronts boarded, paint peeling on the signs, a soup queue along one pavement. Two theatre marquees have been converted, with cheap hand-painted boards and rows of bare bulbs, showing invented short words only. Fewer cars, more people standing about.
```

### Кадр 22 · 1934 · Grind Houses

> Вход: кадр 21 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Most theatres have become cheap cinemas: wide flat marquees with dense rows of bulbs and stacked boards, ticket booths on the pavement, posters in frames carrying only blocks of colour. A hot-dog cart. The upper signs are patchier, some dark.
```

### Кадр 23 · 1937 · Swing

> Вход: кадр 22 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Livelier again: a dance hall on the left with a big lit sign, a queue of young people in coats and hats, more cars, cleaner pavements. Several dark signs relit. Night, warm bulb glow.
```

### Кадр 24 · 1939 · The Fair Year

> Вход: кадр 23 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Bright and confident: every sign lit and repainted, a new streamlined sign with rounded corners and horizontal lines, cleaner modern cars, flagpoles along the kerb each flying a flag with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its corner. No other nation's flag anywhere.
```

### Кадр 25 · 1942 · The Dimout

> Вход: кадр 24 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Every sign in the frame is DARK. Not one lit rectangle, not one glowing bulb anywhere. The street is lit only by weak hooded lamps with narrow slits and by car headlights masked down to thin strips. Windows blacked out. The tower is a black silhouette against a dark blue sky. A few uniformed figures on the pavement. The emptiest and darkest frame of the series.
```

### Кадр 26 · 1944 · Wartime Crowd

> Вход: кадр 25 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Still dark overhead, but the street is busy: servicemen and women in uniform on the pavements, a canteen booth at the kerb, a war bond stand. The signs remain unlit. One large flag with thirteen stripes and a blue corner of stars hangs from the tower, floodlit by a single lamp. No other flags.
```

### Кадр 27 · 1945 · The Lights Come Back

> Вход: кадр 26 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Night, and every sign in the frame is blazing again, brighter than before. An enormous crowd fills both avenues completely, hats in the air, confetti and paper falling from the upper windows. The tower's news ribbon is running. The single most crowded frame of the series.
```

### Кадр 28 · 1947 · Postwar

> Вход: кадр 27 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Daylight, prosperous and busy: new cars with rounded bodies, clean pavements, repainted signs, a new sign with a smoking silhouette that puffs rings. Shop windows full. A traffic light on a pole replaces the policeman's stand.
```

### Кадр 29 · 1950 · Neon

> Вход: кадр 28 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Neon replaces bulbs on most signs: glowing coloured tubes bent into shapes and invented short words, in reds, blues and greens, layered over the older bulb boards. Richer, more saturated night light than before.
```

### Кадр 30 · 1953 · Bigger Boards

> Вход: кадр 29 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The signs grow to cover entire building faces, projecting out on steel frames over the pavement. An animated waterfall of lit blocks pours down one facade. More neon colours, denser stacking.
```

### Кадр 31 · 1956 · Cinemascope

> Вход: кадр 30 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Cinema marquees widened and modernised, with sweeping horizontal fins and big block letters of invented short words. Long finned cars in bright two-tone colours at the kerb. A crowd queueing along the block.
```

### Кадр 32 · 1959 · Chrome

> Вход: кадр 31 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Peak of the era: the widest cars, the brightest neon, every facade covered, a new sign with a rotating silhouette. Pavements crowded with people in bright clothes. Warm dense night.
```

### Кадр 33 · 1962 · Stripped

> Вход: кадр 32 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The tower is being reclad: its stone facade is gone, stripped back to a bare structural frame of dark columns and beams with the floors visible between them, wrapped in scaffolding and safety netting. A crane beside it. The signs around it are unchanged and still lit, which makes the bare frame look stranger.
```

### Кадр 34 · 1964 · White Marble

> Вход: кадр 33 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The tower is reclad: a smooth flat skin of white panels covering it from top to bottom, with narrow slit windows, no cornice and no turret. It is now a plain white slab and looks nothing like the ornate stone tower it was, though it stands in exactly the same footprint and is exactly the same height.
```

### Кадр 35 · 1967 · Fraying

> Вход: кадр 34 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The first signs of decline: two dark unlit boards, a boarded shopfront, litter at the kerb, cracked pavement. The neon that still works looks tired. Fewer well-dressed people, more standing about.
```

### Кадр 36 · 1970 · Grind

> Вход: кадр 35 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Cinema marquees now carry crude hand-lettered boards with invented short words and blocks of colour, several with bare unshaded bulbs. More boarded windows, a pawnbroker with barred glass, graffiti at street level. Grimy, cluttered.
```

### Кадр 37 · 1973 · The Low Point

> Вход: кадр 36 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Heavy decay: half the upper signs dark or broken with missing blocks, boarded and graffitied shopfronts along both sides, rubbish piled at the kerb, a burnt-out car, weeds in the pavement cracks. The white tower is streaked and stained. Overcast grey day, drained colours.
```

### Кадр 38 · 1977 · Blackout Summer

> Вход: кадр 37 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Night with every sign and window dark, the street lit only by car headlights and a few torch beams. Not a blackout of war but of failure: broken shopfronts, scattered goods on the pavement, figures moving in the dark. Hot summer haze.
```

### Кадр 39 · 1980 · Bottom

> Вход: кадр 38 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Daylight on the worst of it: boarded frontages the full length of both sides, dense graffiti to first-floor height, a vacant lot behind a chain fence where a building was demolished, rubbish, cracked road. Only three signs still lit. The tower stained grey.
```

### Кадр 40 · 1984 · Hoardings

> Вход: кадр 39 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Redevelopment begins: tall painted hoardings enclose two blocks, with printed boards showing abstract colour blocks only. A demolition crane behind one hoarding. The rest of the street is unchanged and still shabby.
```

### Кадр 41 · 1988 · Demolition

> Вход: кадр 40 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
A whole block on the right is coming down: the buildings half demolished with floors open to the air, a wrecking machine, dust clouds, and a great gap of open sky where they stood. The signs that were on them are gone completely.
```

### Кадр 42 · 1991 · Empty Lots

> Вход: кадр 41 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Two cleared lots behind chain fencing, used as flat parking with painted bays. The remaining buildings are shabby but tidier, some hoardings repainted. Fewer boarded fronts than before but the street feels thin and gap-toothed. Cold light.
```

### Кадр 43 · 1994 · Cleanup

> Вход: кадр 42 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Visible repair: new street lamps, fresh paving, planters, a police post at the corner, scaffolding on two restored theatre facades with their marquees being rebuilt. Graffiti painted out. A handful of bright new signs among the old.
```

### Кадр 44 · 1997 · The Theatres Return

> Вход: кадр 43 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Restored theatre fronts on the left with new lit marquees in period style, a queue of families, souvenir stands, clean pavements. The cleared lots on the right now hold construction cores with tower cranes above them.
```

### Кадр 45 · 1999 · Screens On The Tower

> Вход: кадр 44 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The tower's white panels are hidden: large flat display boards of lit coloured blocks now cover its whole front from the fourth storey to the roof, carrying invented short words and abstract patterns. Its shape is unchanged underneath, but the building itself is no longer visible as a building.
```

### Кадр 46 · 2001 · Millennium Bright

> Вход: кадр 45 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
New glass towers now fill the sky gap on the right, their lower floors wrapped in lit display boards. Every facade in the frame carries screens or signs. Clean, safe, busy, brightly lit day and night. Tour buses at the kerb.
```

### Кадр 47 · 2004 · Full Colour

> Вход: кадр 46 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The displays are bigger and smoother, covering entire building faces edge to edge with moving blocks of colour. Neon has almost vanished. A giant wraparound board turns the corner of one building. Night, the whole frame lit by screens alone.
```

### Кадр 48 · 2007 · The Canyon

> Вход: кадр 47 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Screens now run from street level to rooftop on both sides with no gaps, so the street is a canyon of light. Pavements packed with tourists, costumed street performers, ticket booths. Yellow taxis nose to tail.
```

### Кадр 49 · 2009 · Chairs In The Road

> Вход: кадр 48 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The roadway in front of the wedge has been closed to traffic: rows of simple folding chairs and small tables stand directly on the asphalt where cars used to drive, with planters and bollards marking the edge. People sitting in the middle of what was a street. Taxis now stop at the new boundary.
```

### Кадр 50 · 2012 · The Plazas

> Вход: кадр 49 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The temporary chairs are gone, replaced by a permanent stone plaza: pale granite paving across the whole central roadway, long fixed benches, low steel bollards, planting beds and a raised platform of wide steps. Cleaner and more deliberate.
```

### Кадр 51 · 2016 · Wraparound

> Вход: кадр 50 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Same world, same buildings, same time of day and same art style as the reference image — only the camera is repositioned, exactly as described above. Nothing in the world is added, removed or rebuilt in this step.
```

### Кадр 52 · 2019 · Peak Crowd

> Вход: кадр 51 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The busiest daytime frame: the plaza and both pavements completely packed with people, tour groups with flags on poles, food carts, pedicabs decorated with lights, queues at every booth. Screens at full brightness even in daylight.
```

### Кадр 53 · 2020 · Empty

> Вход: кадр 52 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The same place with almost nobody in it: the plaza bare, chairs and carts gone, shutters down on the shops, theatre marquees dark and blank. But every giant screen is still running at full brightness above the empty street. Two masked figures far apart. Flat grey daylight. The strangest frame of the series.
```

### Кадр 54 · 2022 · Coming Back

> Вход: кадр 53 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
People are back in numbers though not yet packed: reopened marquees lit again, food carts returned, outdoor seating, plenty of tourists but room to walk. A few masks. Bright normal day.
```

### Кадр 55 · 2024 · Normal

> Вход: кадр 54 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Fully recovered and slightly greener: new planters with small trees along the plaza, more benches, cycle racks, a bike lane marked at the edge. Screens denser than ever. Big crowd, relaxed.
```

### Кадр 56 · 2026 · Present Day

> Вход: кадр 55 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
The square today, at its brightest: screens covering every available surface from pavement to roofline including all four faces of the wedge tower, a packed relaxed crowd, mature planters, food carts, performers, yellow taxis beyond the bollards. Warm late-afternoon light behind the towers, long shadows down the avenues.
```

### Кадр 57 · 2040 · Layers of Light

> Вход: кадр 56 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Near future: the flat screens are joined by free-standing holographic figures three storeys tall standing in the air above the plaza, translucent and made of glowing blocks. Driverless pods glide silently on a marked lane. Vertical gardens climb two facades. The crowd carries no phones, wearing thin visors instead.
```

### Кадр 58 · 2055 · The Green Canyon

> Вход: кадр 57 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Plants have taken over the architecture: every facade carries dense planting between the screens, trees grow from terraces at four levels, water runs in channels through the plaza paving. The screens are dimmer and fewer, the light softer and greener. Fewer people, more slowly moving.
```

### Кадр 59 · 2070 · The Screens Go Dark

> Вход: кадр 58 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Every screen in the frame is dead: blank grey rectangles covering the buildings, with cracked and missing panels on several. The planting has run wild and hangs untrimmed over the facades. No pods, no crowd, a handful of figures. Low mist. The wedge tower stands blank and grey.
```

### Кадр 60 · 2075 · The Last Frame

> Вход: кадр 59 + мастер-плита.

```
BASE IMAGE: the previous frame is attached. Build this image by EDITING that image, not by drawing a new scene from scratch. Keep its camera position, framing, horizon line, perspective, lighting and every anchor object exactly as they already are. Change only what is listed under CHANGE below.

STYLE:
A raw in-game screenshot from Minecraft Java Edition, vanilla 16x16 block
textures, rendered with a shader pack such as Complementary or BSL.

STRICT BLOCK RULES - this is what makes it read as the real game:
- The whole world is made of 1-meter cubes on a strict grid. Every wall, roof,
  sign and object snaps to that grid. Nothing is smaller than one block.
- NO smooth curves anywhere. Arches and rounded tops are approximated with
  stairs and slabs, and the stair-stepping is clearly visible.
- NO sub-block detail: no thin mouldings, no carved ornament, no fine window
  frames. A window is one or two glass-pane blocks. A cornice is one row of
  stair blocks.
- Every block face is FLAT and uniformly shaded, carrying a visible coarse
  16x16 pixel texture. No smooth gradients, no baked sculptural shading.
- Trees are Minecraft trees: a straight 1x1 trunk of log blocks and a blocky
  cloud of cubic leaf blocks. Never rounded topiary.
- Minecraft scale: a villager is 2 blocks tall; buildings are counted in blocks.
- Signs and screens are flat rectangles of coloured blocks on the block grid,
  never smooth panels.

Built from real Minecraft blocks: stone bricks, red brick, terracotta in many
colours, smooth quartz, deepslate, glass panes, glass blocks, sea lanterns and
glowstone for lit signage, oak and spruce planks, cobblestone.

DETAIL DISCIPLINE - follow these exactly:
- ALL signage is FICTIONAL. Signs and screens carry invented short words,
  abstract blocks of colour and simple silhouettes. NEVER a real company name,
  a real brand, a real logo or a real trademark of any kind.
- Draw NO flag that is not described in the CHANGE text below, and never any
  other nation's flag.
- Every vehicle is the kind named in the CHANGE text and nothing else.

No HUD, no crosshair, no hotbar, no hearts, no interface, no hands, no held
items, no watermark.

CAMERA:
Fixed camera on a locked tripod at standing eye level in the middle of a wide
street, looking south along it. Two broad avenues converge in the middle
distance and meet at a narrow wedge-shaped block that sits DEAD CENTRE of the
frame, its sharp point facing the camera. Buildings line both sides of the
frame and run away toward that wedge, so the whole composition funnels to the
centre. The horizon sits at 58% of frame height, with open sky above the wedge
filling the upper third. 35mm equivalent, no lens distortion, horizon perfectly
level. 16:9.

THE CAMERA NEVER MOVES. The same position, the same angle, the same framing and
the same focal length in every single image of the series.

ANCHOR OBJECTS - the same physical things in every image. Never move them,
never change their position or footprint:

- THE WEDGE: the narrow triangular block dead centre of the frame, where the two
  avenues meet, with its sharp point toward the camera. Whatever stands on it
  over the years, that wedge of ground keeps exactly the same shape, size and
  position. It is the subject of the whole series.

- THE TOWER, from the year it is built onward: a narrow tall building standing
  on the wedge, about 10 blocks wide at its point and 26 blocks tall, far taller
  than its neighbours. Its SKIN changes completely over the years - stone, then
  white panels, then screens - but its silhouette, its height and its footprint
  never change.

- THE TWO AVENUES: the left and right roadways converging on the wedge. Their
  width and the angle at which they meet never change, whatever surface they
  carry.

- THE LEFT CORNER BLOCK: a solid masonry building filling the left edge of the
  frame. It is refaced and resigned over the years but never demolished.

- THE SKY GAP: the open sky above and to the right of the wedge, which slowly
  fills in with taller buildings as the decades pass.

ALL SIGNAGE IS FICTIONAL: invented short words, abstract colour blocks and
simple silhouettes. Never a real brand, name, logo or trademark.

FLAG RULE: draw only a flag described in the CHANGE text. When none is
described, there are no flags in the frame.

CHANGE:
Long abandoned: the plaza cracked apart with trees growing through it, the roadways gone to grass, vines covering the lower storeys, dead screens hanging in broken sheets from the facades. One screen on the wedge tower still flickers faintly with a pattern. Rain falling, dark blue-grey palette, cold light from that one flickering panel.
```
