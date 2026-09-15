# Промпты переходов — Times Square, 59 блоков

Сгенерировано `tools/transition_prompts.py` из `prompts-times-square.md`.

Режим «первый кадр — последний кадр»: на вход два соседних кадра, на выходе
клип, который превращает один в другой. Переходов на один меньше, чем кадров.

Каждый клип: примерно две трети удержания, затем морфинг. Так сетка 8 секунд
на эпоху сохраняется, и зритель успевает рассмотреть кадр до того, как он начнёт
меняться.

**Негатив у всех переходов одинаковый:**

```
camera movement, camera pan, camera zoom, dolly, orbit, parallax, shaking,
drifting framing, cross-fade, dissolve, melting, organic morphing, smooth
shape-shifting, warping geometry, buildings sliding sideways, changing art style,
text, letters, numbers, watermark, HUD, crosshair, hotbar
```

---

### Переход 1→2 · 1800 → 1840 · The Farm

> Первый кадр: 1. Последний кадр: 2.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The farmhouse, the barn and the fences build themselves up out of the ground block by block, course by course, while the road widens and the ploughed strips appear as whole blocks of dark earth.
```

### Переход 2→3 · 1840 → 1860 · The Grid Arrives

> Первый кадр: 2. Последний кадр: 3.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The farm buildings vanish as whole blocks lifting away. The ground flattens into a level surface of packed earth, then the two avenues appear as broad strips of graded dirt and the survey stakes pop into place along their edges.
```

### Переход 3→4 · 1860 → 1872 · Longacre Square

> Первый кадр: 3. Последний кадр: 4.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
Brick buildings rise along both avenues block by block from the ground up, the cobbles fill in across the dirt as whole blocks, and the gas lamps and painted signs appear last.
```

### Переход 4→5 · 1872 → 1880 · Horsecars

> Первый кадр: 4. Последний кадр: 5.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Add a tram line down each avenue: steel rails set flush into the cobbles, with an open four-wheeled tram car running on them, pulled by two horses in harness walking between the rails. No engine, no overhead wires, no poles or cables above. A small wooden waiting shelter at the kerb. More people on the pavement, more painted trade signs.
```

### Переход 5→6 · 1880 → 1888 · The Carriage Trade

> Первый кадр: 5. Последний кадр: 6.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The district is at its busiest: long rows of finished carriages parked at the kerb, wide-open workshop doors showing wheels and frames inside, a five-storey brick carriage works on the left corner with big arched windows. Overhead a dense web of telegraph and telephone wires on tall poles crossing the avenues.
```

### Переход 6→7 · 1888 → 1895 · The First Theatre

> Первый кадр: 6. Последний кадр: 7.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The old low buildings on the left lift away as whole blocks and the theatre builds up in their place course by course, its canopy last. The arc lamps and the lit sign switch on together at the end.
```

### Переход 7→8 · 1895 → 1899 · The Hotel on the Triangle

> Первый кадр: 7. Последний кадр: 8.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The small building on the wedge vanishes block by block and the tall hotel rises in its place from the ground upward, storey by storey, the mansard roof going on last.
```

### Переход 8→9 · 1899 → 1903 · Digging

> Первый кадр: 8. Последний кадр: 9.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The hotel comes down as whole blocks collapsing inward into a heap, then the heap clears away and the pit is dug out downward, layer by layer, the cranes and hoardings appearing around it at the end.
```

### Переход 9→10 · 1903 → 1904 · The Tower

> Первый кадр: 9. Последний кадр: 10.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The tower rises out of the pit course by course, from the foundations up to the turret, while the trenches in the avenues fill in as whole blocks of paving from both ends toward the centre.
```

### Переход 10→11 · 1904 → 1905 · The Subway

> Первый кадр: 10. Последний кадр: 11.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Add a cast-iron and glass subway entrance kiosk with a domed roof at the kerb in front of the tower, with steps leading down and an ornate railing. Newsstands on the corners. More pedestrians, a queue at the kiosk.
```

### Переход 11→12 · 1905 → 1907 · The First Ball

> Первый кадр: 11. Последний кадр: 12.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Night. A dense crowd fills both avenues from edge to edge, tens of thousands of small figures. A glowing ball of lit blocks sits at the top of the tower's turret. Every window in the frame is lit. Confetti in the air. The lit signs are bright against a black sky.
```

### Переход 12→13 · 1907 → 1910 · Electric Signs

> Первый кадр: 12. Последний кадр: 13.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The horse tram and its horses vanish as whole blocks, the catenary poles rise along the kerbs and the wires string between them, then the electric tram rolls in. The signs light up one after another across both facades.
```

### Переход 13→14 · 1910 → 1913 · Automobiles

> Первый кадр: 13. Последний кадр: 14.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The street is full of early motor cars with high bodies and spoked wheels, mixed with a few remaining horse carriages. A traffic policeman on a small stand in the road. Larger signs, more of them, and the first sign with moving light patterns.
```

### Переход 14→15 · 1913 → 1917 · Wartime

> Первый кадр: 14. Последний кадр: 15.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Mobilisation: a column of soldiers in uniform marching down one avenue, a wooden recruiting booth on the pavement, crowds waving. One flag hangs from the tower with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its upper corner; no other nation's flag appears anywhere. Printed notices on boards carrying no readable words, only blocks of colour.
```

### Переход 15→16 · 1917 → 1920 · Prohibition

> Первый кадр: 15. Последний кадр: 16.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Peacetime and prosperous: the soldiers gone, more cars, women in shorter coats, a policeman at the kerb. Signs are bigger and there are more of them, with the first animated sign showing a simple silhouette figure in motion. Basement stairways with plain unmarked doors under two buildings.
```

### Переход 16→17 · 1920 → 1923 · The Great White Way

> Первый кадр: 16. Последний кадр: 17.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Night, and the whole frame is lit by signs: every upper facade on both sides is covered in glowing rectangles outlined by bulbs, so bright that there are no dark surfaces left anywhere. Theatre canopies below, all lit. The tower carries a large sign of its own. Dense evening crowd, cars nose to tail.
```

### Переход 17→18 · 1923 → 1925 · Peak Bulbs

> Первый кадр: 17. Последний кадр: 18.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Even more: signs now stacked three high on some buildings and projecting out over the roadway on steel frames. A huge animated sign on the right shows a silhouette pouring from a jug, cycling in steps. Theatre marquees with rows of bulbs around them.
```

### Переход 18→19 · 1925 → 1928 · The Zipper

> Первый кадр: 18. Последний кадр: 19.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The lit band appears around the tower one block at a time, running all the way around it, and then begins to move.
```

### Переход 19→20 · 1928 → 1929 · The Crash

> Первый кадр: 19. Последний кадр: 20.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: A large crowd packed in the street below the tower, all facing up at the news ribbon, still and silent rather than celebrating. Men in hats holding newspapers. Grey overcast day, the signs unlit in daylight, a heavy quiet mood.
```

### Переход 20→21 · 1929 → 1931 · Burlesque

> Первый кадр: 20. Последний кадр: 21.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The street is shabbier: several shopfronts boarded, paint peeling on the signs, a soup queue along one pavement. Two theatre marquees have been converted, with cheap hand-painted boards and rows of bare bulbs, showing invented short words only. Fewer cars, more people standing about.
```

### Переход 21→22 · 1931 → 1934 · Grind Houses

> Первый кадр: 21. Последний кадр: 22.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Most theatres have become cheap cinemas: wide flat marquees with dense rows of bulbs and stacked boards, ticket booths on the pavement, posters in frames carrying only blocks of colour. A hot-dog cart. The upper signs are patchier, some dark.
```

### Переход 22→23 · 1934 → 1937 · Swing

> Первый кадр: 22. Последний кадр: 23.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Livelier again: a dance hall on the left with a big lit sign, a queue of young people in coats and hats, more cars, cleaner pavements. Several dark signs relit. Night, warm bulb glow.
```

### Переход 23→24 · 1937 → 1939 · The Fair Year

> Первый кадр: 23. Последний кадр: 24.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Bright and confident: every sign lit and repainted, a new streamlined sign with rounded corners and horizontal lines, cleaner modern cars, flagpoles along the kerb each flying a flag with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its corner. No other nation's flag anywhere.
```

### Переход 24→25 · 1939 → 1942 · The Dimout

> Первый кадр: 24. Последний кадр: 25.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The signs go out in waves across the frame, section by section, until nothing is lit at all, and the hooded lamps come on as the last thing.
```

### Переход 25→26 · 1942 → 1944 · Wartime Crowd

> Первый кадр: 25. Последний кадр: 26.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Still dark overhead, but the street is busy: servicemen and women in uniform on the pavements, a canteen booth at the kerb, a war bond stand. The signs remain unlit. One large flag with thirteen stripes and a blue corner of stars hangs from the tower, floodlit by a single lamp. No other flags.
```

### Переход 26→27 · 1944 → 1945 · The Lights Come Back

> Первый кадр: 26. Последний кадр: 27.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The signs come back on in a wave that spreads outward across the whole frame, one board after another, and as the last one lights the crowd floods into the street from both sides.
```

### Переход 27→28 · 1945 → 1947 · Postwar

> Первый кадр: 27. Последний кадр: 28.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Daylight, prosperous and busy: new cars with rounded bodies, clean pavements, repainted signs, a new sign with a smoking silhouette that puffs rings. Shop windows full. A traffic light on a pole replaces the policeman's stand.
```

### Переход 28→29 · 1947 → 1950 · Neon

> Первый кадр: 28. Последний кадр: 29.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
Bulb boards go dark one by one and neon tubes light up in their place, colour by colour, until the whole frame is neon.
```

### Переход 29→30 · 1950 → 1953 · Bigger Boards

> Первый кадр: 29. Последний кадр: 30.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The signs grow to cover entire building faces, projecting out on steel frames over the pavement. An animated waterfall of lit blocks pours down one facade. More neon colours, denser stacking.
```

### Переход 30→31 · 1953 → 1956 · Cinemascope

> Первый кадр: 30. Последний кадр: 31.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Cinema marquees widened and modernised, with sweeping horizontal fins and big block letters of invented short words. Long finned cars in bright two-tone colours at the kerb. A crowd queueing along the block.
```

### Переход 31→32 · 1956 → 1959 · Chrome

> Первый кадр: 31. Последний кадр: 32.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Peak of the era: the widest cars, the brightest neon, every facade covered, a new sign with a rotating silhouette. Pavements crowded with people in bright clothes. Warm dense night.
```

### Переход 32→33 · 1959 → 1962 · Stripped

> Первый кадр: 32. Последний кадр: 33.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The tower's stone facade comes away in whole blocks from the top down, storey by storey, leaving the dark frame standing, and the scaffolding rises around it as it goes.
```

### Переход 33→34 · 1962 → 1964 · White Marble

> Первый кадр: 33. Последний кадр: 34.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
White panels go up over the dark frame course by course from the bottom upward, and the scaffolding comes away in sections as they pass.
```

### Переход 34→35 · 1964 → 1967 · Fraying

> Первый кадр: 34. Последний кадр: 35.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The first signs of decline: two dark unlit boards, a boarded shopfront, litter at the kerb, cracked pavement. The neon that still works looks tired. Fewer well-dressed people, more standing about.
```

### Переход 35→36 · 1967 → 1970 · Grind

> Первый кадр: 35. Последний кадр: 36.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Cinema marquees now carry crude hand-lettered boards with invented short words and blocks of colour, several with bare unshaded bulbs. More boarded windows, a pawnbroker with barred glass, graffiti at street level. Grimy, cluttered.
```

### Переход 36→37 · 1970 → 1973 · The Low Point

> Первый кадр: 36. Последний кадр: 37.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Heavy decay: half the upper signs dark or broken with missing blocks, boarded and graffitied shopfronts along both sides, rubbish piled at the kerb, a burnt-out car, weeds in the pavement cracks. The white tower is streaked and stained. Overcast grey day, drained colours.
```

### Переход 37→38 · 1973 → 1977 · Blackout Summer

> Первый кадр: 37. Последний кадр: 38.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The signs and the street lamps all cut out at once across the whole frame, leaving only headlights, and the scene goes dark in a single moment rather than gradually.
```

### Переход 38→39 · 1977 → 1980 · Bottom

> Первый кадр: 38. Последний кадр: 39.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Daylight on the worst of it: boarded frontages the full length of both sides, dense graffiti to first-floor height, a vacant lot behind a chain fence where a building was demolished, rubbish, cracked road. Only three signs still lit. The tower stained grey.
```

### Переход 39→40 · 1980 → 1984 · Hoardings

> Первый кадр: 39. Последний кадр: 40.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Redevelopment begins: tall painted hoardings enclose two blocks, with printed boards showing abstract colour blocks only. A demolition crane behind one hoarding. The rest of the street is unchanged and still shabby.
```

### Переход 40→41 · 1984 → 1988 · Demolition

> Первый кадр: 40. Последний кадр: 41.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The buildings on the right collapse as whole blocks falling inward, floor by floor, and a dust cloud rolls up as the sky opens behind them.
```

### Переход 41→42 · 1988 → 1991 · Empty Lots

> Первый кадр: 41. Последний кадр: 42.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Two cleared lots behind chain fencing, used as flat parking with painted bays. The remaining buildings are shabby but tidier, some hoardings repainted. Fewer boarded fronts than before but the street feels thin and gap-toothed. Cold light.
```

### Переход 42→43 · 1991 → 1994 · Cleanup

> Первый кадр: 42. Последний кадр: 43.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Visible repair: new street lamps, fresh paving, planters, a police post at the corner, scaffolding on two restored theatre facades with their marquees being rebuilt. Graffiti painted out. A handful of bright new signs among the old.
```

### Переход 43→44 · 1994 → 1997 · The Theatres Return

> Первый кадр: 43. Последний кадр: 44.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Restored theatre fronts on the left with new lit marquees in period style, a queue of families, souvenir stands, clean pavements. The cleared lots on the right now hold construction cores with tower cranes above them.
```

### Переход 44→45 · 1997 → 1999 · Screens On The Tower

> Первый кадр: 44. Последний кадр: 45.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
Display boards go up over the white tower panel by panel from the bottom upward, each one lighting as it locks into place, until the white skin is completely hidden.
```

### Переход 45→46 · 1999 → 2001 · Millennium Bright

> Первый кадр: 45. Последний кадр: 46.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: New glass towers now fill the sky gap on the right, their lower floors wrapped in lit display boards. Every facade in the frame carries screens or signs. Clean, safe, busy, brightly lit day and night. Tour buses at the kerb.
```

### Переход 46→47 · 2001 → 2004 · Full Colour

> Первый кадр: 46. Последний кадр: 47.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The displays are bigger and smoother, covering entire building faces edge to edge with moving blocks of colour. Neon has almost vanished. A giant wraparound board turns the corner of one building. Night, the whole frame lit by screens alone.
```

### Переход 47→48 · 2004 → 2007 · The Canyon

> Первый кадр: 47. Последний кадр: 48.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Screens now run from street level to rooftop on both sides with no gaps, so the street is a canyon of light. Pavements packed with tourists, costumed street performers, ticket booths. Yellow taxis nose to tail.
```

### Переход 48→49 · 2007 → 2009 · Chairs In The Road

> Первый кадр: 48. Последний кадр: 49.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The taxis clear out of the central roadway, bollards and planters drop into place along a new line, and then chairs and tables appear across the empty asphalt in rows.
```

### Переход 49→50 · 2009 → 2012 · The Plazas

> Первый кадр: 49. Последний кадр: 50.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The chairs lift away, the asphalt is replaced by pale granite paving spreading outward block by block, and the benches, bollards and steps rise out of it.
```

### Переход 50→51 · 2012 → 2016 · Wraparound

> Первый кадр: 50. Последний кадр: 51.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The largest display yet: a single enormous board running the entire height and width of one building face and turning both corners. Screens on every other surface, brighter and more saturated. Dense tourist crowd at all hours, selfie sticks, costumed performers.
```

### Переход 51→52 · 2016 → 2019 · Peak Crowd

> Первый кадр: 51. Последний кадр: 52.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The busiest daytime frame: the plaza and both pavements completely packed with people, tour groups with flags on poles, food carts, pedicabs decorated with lights, queues at every booth. Screens at full brightness even in daylight.
```

### Переход 52→53 · 2019 → 2020 · Empty

> Первый кадр: 52. Последний кадр: 53.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The crowd thins out and disappears as figures walk out of frame in every direction, the carts and chairs lift away, the shutters roll down, and the marquees go dark - while the big screens above keep cycling unchanged.
```

### Переход 53→54 · 2020 → 2022 · Coming Back

> Первый кадр: 53. Последний кадр: 54.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: People are back in numbers though not yet packed: reopened marquees lit again, food carts returned, outdoor seating, plenty of tourists but room to walk. A few masks. Bright normal day.
```

### Переход 54→55 · 2022 → 2024 · Normal

> Первый кадр: 54. Последний кадр: 55.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Fully recovered and slightly greener: new planters with small trees along the plaza, more benches, cycle racks, a bike lane marked at the edge. Screens denser than ever. Big crowd, relaxed.
```

### Переход 55→56 · 2024 → 2026 · Present Day

> Первый кадр: 55. Последний кадр: 56.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: The square today, at its brightest: screens covering every available surface from pavement to roofline including all four faces of the wedge tower, a packed relaxed crowd, mature planters, food carts, performers, yellow taxis beyond the bollards. Warm late-afternoon light behind the towers, long shadows down the avenues.
```

### Переход 56→57 · 2026 → 2040 · Layers of Light

> Первый кадр: 56. Последний кадр: 57.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Near future: the flat screens are joined by free-standing holographic figures three storeys tall standing in the air above the plaza, translucent and made of glowing blocks. Driverless pods glide silently on a marked lane. Vertical gardens climb two facades. The crowd carries no phones, wearing thin visors instead.
```

### Переход 57→58 · 2040 → 2055 · The Green Canyon

> Первый кадр: 57. Последний кадр: 58.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Plants have taken over the architecture: every facade carries dense planting between the screens, trees grow from terraces at four levels, water runs in channels through the plaza paving. The screens are dimmer and fewer, the light softer and greener. Fewer people, more slowly moving.
```

### Переход 58→59 · 2055 → 2070 · The Screens Go Dark

> Первый кадр: 58. Последний кадр: 59.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
The screens go out one after another across the frame, section by section, until every surface is a dead grey rectangle, and the crowd walks out of frame as they go.
```

### Переход 59→60 · 2070 → 2075 · The Last Frame

> Первый кадр: 59. Последний кадр: 60.

```
SHOT TYPE: this is a transition between two still images. The FIRST frame and
the LAST frame are both attached and both are fixed points: the clip must start
exactly on the first image and end exactly on the last image, with no drift at
either end.

TIMING: hold the first image almost completely still for the first two thirds of
the clip, with only faint ambient motion. Then, in the final third, carry out the
change described below so that the last image is reached exactly as the clip ends.

CAMERA: absolutely locked off. No zoom, no pan, no tilt, no dolly, no orbit, no
parallax, no shake. The framing, the horizon and the focal length are identical
in every frame of the clip. Anything that is present in both images - the ground,
the sky line, the buildings that do not change - stays perfectly still and does
not slide, wobble or breathe.

HOW THINGS CHANGE: this is a Minecraft world, so change happens BLOCK BY BLOCK.
Structures build up as whole cubes appearing in place, course by course, from the
ground upward. Things that are removed vanish as whole cubes, never fading out.
Damage collapses as whole blocks falling. Nothing dissolves, cross-fades, morphs
organically or melts. No smooth shape-shifting of any kind.

THE CHANGE:
By the end of the clip the scene must match the last image exactly: Long abandoned: the plaza cracked apart with trees growing through it, the roadways gone to grass, vines covering the lower storeys, dead screens hanging in broken sheets from the facades. One screen on the wedge tower still flickers faintly with a pattern. Rain falling, dark blue-grey palette, cold light from that one flickering panel.
```
