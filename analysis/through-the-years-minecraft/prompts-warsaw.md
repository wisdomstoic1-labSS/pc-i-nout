# Варшава — 75 кадров, 9:56. Полный набор промптов

Хронометраж: `4 с + 74 × 8 с = 596 с = 9:56`
Город: Варшава. Точка: край вислинской скарпы, на которой встанет Королевский замок.

---

## КАК ЭТИМ ПОЛЬЗОВАТЬСЯ

Стиль держится **не промптом, а цепочкой**. Один только блок стиля даёт разъезжающуюся картинку к 10-й эпохе. Работает связка из трёх вещей:

1. **Блок STYLE копируется дословно в каждую генерацию.** Ни одного слова не менять — ни синонимов, ни перестановок.
2. **На вход подаётся предыдущий кадр** + мастер-плита своей группы. Не text-to-image, а инструкционное редактирование (Nano Banana Pro / Flux Kontext / Seedream / Qwen Image Edit).
3. **После каждой генерации — композит:** фон и якорные объекты возвращаются из мастер-плиты поверх результата. Это то, что даёт попиксельное совпадение кадров.

Сборка промпта на эпоху N:

```
[STYLE]  +  [CAMERA той группы]  +  [EDIT эпохи N]     → картинка
[MOTION LOCK]  +  [MOTION эпохи N]                     → видео из картинки
```

Кадр 1 генерится с нуля (это мастер-плита группы A), остальные 74 — правкой предыдущего.

---

## БЛОК STYLE — дословно в каждую генерацию

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic
blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid
seams on every face. No smooth curves, no rounded shapes, no organic silhouettes,
no bevels, no sculpted detail. Rendered as a game screenshot through a modern
shader pack: volumetric god rays, soft contact shadows, gentle bloom, crisp
saturated colours, smooth sky gradient, light atmospheric haze on the far
background. No HUD, no crosshair, no hotbar, no interface, no hands, no held
items, no text, no watermark, no signature.
```

**NEGATIVE (тоже дословно):**
```
smooth surfaces, rounded edges, curved walls, realistic geometry, photorealism,
low-poly non-cubic shapes, sculpted terrain, HUD, crosshair, hotbar, inventory,
user interface, text, letters, numbers, watermark, signature, logo, blurry,
fisheye, distorted perspective, tilted horizon, changed art style
```

---

## БЛОКИ КАМЕРЫ — по одному на группу

### CAMERA A — эпохи 1–18
```
Fixed camera on a locked tripod, wide establishing shot from a slightly elevated
position on the flat east bank of a great river. The river runs across the lower
third of the frame from the left edge to the right. Beyond it rises a wooded
escarpment: a long steep bluff whose crest sits at 45% of frame height. The
flattest point of that crest is dead centre of the frame. Low forested hills
close the far background. 35mm equivalent field of view, no lens distortion,
horizon perfectly level. Midday sun from the upper left, long soft shadows
falling to the lower right. 16:9.
NEVER CHANGE: the bend of the river, the grey boulder on the near bank at the
lower left, the solitary oak on the crest at the right third.
```

### CAMERA B — эпохи 19–34
```
Fixed camera on a locked tripod, medium-wide shot from the same direction as
before but closer and slightly higher. The escarpment crest fills the middle band
of the frame; the river shows only as a strip along the bottom edge. The ducal
seat stands at the centre of the crest, the town spreads to the left. Horizon at
35% of frame height. 35mm equivalent, level horizon, midday sun upper left. 16:9.
NEVER CHANGE: the solitary oak at the right third, the silhouette of the crest line.
```

### CAMERA C — эпохи 35–50
```
Fixed camera at standing eye level in the middle of an open cobbled city square.
A tall free-standing column with a statue on top stands at the centre-left of the
frame. The bulk of the royal residence closes the right half. A gate and the
rooflines of the old town close the left. Sky occupies the top third. Horizon at
55% of frame height. 35mm equivalent, level horizon, sun upper left. 16:9.
NEVER CHANGE: the column, the corner tower of the residence, the cobble pattern
of the square, the lime tree at the right edge of the square.
```

### CAMERA D — эпохи 51–75
```
Fixed camera at standing eye level, facing the royal residence head-on across the
cobbled square. The facade and its clock tower fill the right two-thirds; the
column stands at the left third with its statue against open sky. Horizon at 60%
of frame height. 35mm equivalent, level horizon. 16:9.
NEVER CHANGE: the column, the clock tower, the cobble pattern, the lime tree at
the right edge.
```

---

## MOTION LOCK — дословно в каждый видеопромпт

```
Static locked-off camera on a tripod. Absolutely no camera movement: no zoom, no
pan, no tilt, no dolly, no truck, no orbit, no parallax, no handheld shake, no
rack focus. The framing is identical in the first and the last frame. All
architecture, terrain and the skyline hold their exact shape — nothing morphs,
melts, grows, or disappears. Motion is slow, subtle and ambient only.
```

**NEGATIVE:**
```
camera movement, camera pan, camera zoom, dolly, orbit, parallax, shaking,
morphing buildings, changing architecture, warping geometry, melting structures,
objects appearing or disappearing, style change, text, watermark
```

---

## ЯКОРНЫЕ ОБЪЕКТЫ

Пять объектов, которые зритель будет отслеживать через весь ролик. Именно они дали лучшие комментарии у референса.

| Якорь | Живёт | Судьба |
|---|---|---|
| Излучина реки | 1–34 | не меняется никогда |
| Серый валун на берегу | 1–18 | не меняется никогда |
| Одинокий дуб на скарпе | 2–34 | стоит 3300 лет, срубают в 1596 под замок |
| Колонна со статуей | 33–75 | ставят 1644, валят 1944, поднимают 1949 |
| Липа у правого края площади | 40–75 | сажают 1740, сгорает до пня 1944, отрастает к 1965, огромная в 2026 |

---

# ГРУППА A · CAMERA A · эпохи 1–18

### 1 · 8000 BC · Ice Age Valley — **4 секунды** — МАСТЕР-ПЛИТА
Единственный кадр, который генерится с нуля: `STYLE + CAMERA A + сцена ниже`. Всё остальное — правки.
**SCENE:** `A post-glacial river valley with no humans and no buildings of any kind anywhere in the frame. The escarpment is bare: patches of gravel, sand and grey stone, sparse dwarf pines and thin birches, snow lying in the shaded hollows. The river is wide, pale and braided around gravel islands. Cold thin light, desaturated blue-grey palette, low pale sun.`
**MOTION:** `Only the river water flows slowly around the gravel islands. Thin mist drifts low over the water. A few birds cross the sky far away. Nothing else moves.`

### 2 · 3000 BC · Primeval Forest
**EDIT:** `Cover the escarpment and the far hills with dense primeval forest: tall dark oaks and limes in thick blocky canopy, no gaps, no clearings. Plant one huge solitary oak on the crest at the right third — taller and wider than all the others; it must stay in every following image. Still no humans and no buildings. Warm green summer palette.`
**MOTION:** `The forest canopy sways very slightly in a light breeze. The river flows. A herd of aurochs drinks at the near bank, barely moving. Birds circle above the treeline.`

### 3 · 1500 BC · First Clearing
**EDIT:** `Cut a small clearing into the forest at the centre of the crest. Place two low huts with thatched roofs and a small fenced pen. A thin column of smoke rises from one hut. Everything else stays exactly as before.`
**MOTION:** `Smoke rises straight up from the hut. Two villagers move slowly across the clearing. The forest sways lightly. The river flows.`

### 4 · 700 BC · Lusatian Settlement
**EDIT:** `Grow the clearing to about four times its size. Replace the two huts with eight timber houses arranged in a loose ring, surrounded by a low wooden palisade. Add small cultivated fields on the slope below and a footpath down to the river.`
**MOTION:** `Smoke from three roofs. Villagers walk between the houses. Wheat in the fields ripples. Water flows at the bank.`

### 5 · 100 AD · Amber Route
**EDIT:** `Enlarge the settlement to about twenty houses. Add a beaten trade road running along the crest and out of the right side of the frame, with two loaded ox carts on it. Add a small landing stage with a log boat on the river bank.`
**MOTION:** `An ox cart moves very slowly along the road. Smoke from several roofs. The boat rocks gently at the landing. Villagers cross the settlement.`

### 6 · 400 · Abandoned
**EDIT:** `Destroy and abandon the settlement. The houses are burnt shells with collapsed roofs and blackened timbers; grass and saplings grow through the ruins; the palisade is broken and leaning. The fields are gone back to weeds. No people anywhere. Overcast grey light, desaturated palette.`
**MOTION:** `Thin smoke still drifts from one blackened ruin. Tall weeds bend in the wind. Crows circle and settle on a broken beam. Grey clouds move slowly.`

### 7 · 700 · Slavic Settlement
**EDIT:** `Clear the ruins away. Build a new settlement of a different character on the same spot: fifteen sunken-floor huts with steep thatched roofs, a communal open space in the middle, a new palisade of split logs. Return warm summer light.`
**MOTION:** `Smoke from a central communal fire. Villagers gather around it. Chickens and goats move in the pens. Forest sways.`

### 8 · 900 · The Stronghold
**EDIT:** `Build a proper stronghold on the crest: a high circular earth-and-timber rampart with a log palisade on top and a gate tower facing the river. The settlement moves inside the rampart. Add a defensive ditch on the landward side.`
**MOTION:** `Guards pace slowly on the rampart walkway. Smoke from inside the stronghold. A banner on the gate tower moves in the wind.`

### 9 · 1000 · The First Cross
**EDIT:** `Add a small wooden church with a steep roof and a plain cross on the gable, standing just inside the stronghold gate. Add a small fenced graveyard beside it.`
**MOTION:** `A procession of villagers walks slowly toward the church door. Smoke rises from the houses. The banner moves.`

### 10 · 1100 · The Bridge
**EDIT:** `Build a long timber bridge on piles across the river, connecting the near bank to a track climbing the escarpment. Add a small suburb of a dozen houses outside the rampart on the slope.`
**MOTION:** `A cart crosses the bridge very slowly. Water flows around the piles. Smoke from the suburb. People walk the slope track.`

### 11 · 1180 · The Mill
**EDIT:** `Add a water mill with a large wheel on the near bank at the left, and a small mill pond. Double the size of the suburb outside the rampart. Add more cultivated strips on the slope.`
**MOTION:** `The mill wheel turns slowly. Water falls from the paddles. Carts on the bridge. Smoke from many roofs.`

### 12 · 1230 · Jazdów
**EDIT:** `Replace the timber stronghold with a ducal seat: a two-storey timber-and-stone hall with a tiled roof inside the rampart, a stone gate tower, and a larger church with a bell turret. The suburb grows to thirty houses.`
**MOTION:** `The ducal banner snaps on the hall roof. Guards at the gate. Villagers and carts on the road. Mill wheel turns.`

### 13 · 1262 · Raided
**EDIT:** `The settlement has been raided and burnt. The ducal hall is a roofless shell, the palisade broken in three places, half the suburb houses reduced to charred frames. Fires still burning in two places, thick black smoke. Bodies of the dead are not shown. Ash on the ground.`
**MOTION:** `Fires burn and flicker. Thick black smoke rolls upward and drifts right. Embers float. Crows circle. No people.`

### 14 · 1281 · Burnt Again
**EDIT:** `Total ruin. Even the stone gate tower is toppled, the rampart slumped and overgrown, nothing standing but broken walls and blackened stumps. The fires are out, only cold ash and grey light. The solitary oak on the right survives untouched.`
**MOTION:** `Ash drifts in the wind. Thin cold smoke from the ground. Weeds bend. The oak's canopy sways. No people.`

### 15 · 1300 · Warszowa
**EDIT:** `Found a new town on the same crest, slightly to the left of the old ruined rampart, which stays visible as a grassy mound. The new town has a regular rectangular grid of forty timber houses with tiled roofs, a rectangular open market square in the middle, and a fresh timber palisade. Bright summer light.`
**MOTION:** `Market crowd moves in the square. Smoke from many chimneys. Carts enter through the town gate. The oak sways.`

### 16 · 1330 · Town Charter
**EDIT:** `Formalise the town: straight cobbled streets on the grid, a timber town hall in the centre of the market square, a weighhouse, and rows of narrow gabled merchant houses replacing the plain huts.`
**MOTION:** `Busy market: stalls, moving crowd, a horse cart crossing the square. Pigeons take off from the town hall roof.`

### 17 · 1350 · First Brick
**EDIT:** `Replace the twenty houses around the market square with brick ones — red brick walls, stepped gables, red tile roofs. Begin a large brick church at the north edge of the town: walls half-built, wooden scaffolding, a crane on top.`
**MOTION:** `Builders move on the scaffolding, the crane wheel turns slowly, a stone is lifted. Market crowd below. Dust drifts.`

### 18 · 1370 · The Walls
**EDIT:** `Replace the timber palisade with a brick defensive wall with square towers and a gate house. Finish the church: tall brick nave and a slender tower with a spire. The town is now unmistakably a medieval brick town.`
**MOTION:** `Guards on the wall walkway. Banners on the gate towers move. Market crowd. Birds around the church spire.`

---

# ГРУППА B · CAMERA B · эпохи 19–34

> Кадр 19 — **мастер-плита группы B**. Генерится из кадра 18 инструкцией: `Same world, same town, same time of day — move the camera closer and slightly higher, per CAMERA B.` Дальше цепочка идёт от него.

### 19 · 1380 · Brick Town
**EDIT:** `Same town seen closer per CAMERA B. Complete the brick walls all round with a deep dry moat and a drawbridge at the gate. The solitary oak still stands at the right third.`
**MOTION:** `Guards pace the wall. Banners move. The drawbridge chains sway slightly. Crowd at the gate.`

### 20 · 1400 · The Collegiate
**EDIT:** `Enlarge the brick church into a tall Gothic collegiate: steep roof, high narrow windows, flying buttresses made of blocks, a taller spire that now dominates the skyline.`
**MOTION:** `Bells swing in the spire opening. Pigeons wheel around the tower. Crowd on the church steps.`

### 21 · 1408 · New Town
**EDIT:** `Add a second walled town immediately to the left, separated by a strip of open ground: its own smaller market square, its own church with a modest tower, its own gate.`
**MOTION:** `Traffic moves along the road between the two towns. Smoke from both. Two banners in the wind.`

### 22 · 1413 · Capital of Masovia
**EDIT:** `Replace the old ducal hall on the crest with a proper brick castle: four-storey main block, a tall square keep, crenellated walls, a courtyard, and a ducal banner on the keep.`
**MOTION:** `The ducal banner flies from the keep. Guards in the courtyard. Riders arrive at the castle gate.`

### 23 · 1450 · Gothic
**EDIT:** `Raise every house in both towns to three storeys with steep tiled roofs and decorated stepped gables. Add a covered cloth hall in the main square.`
**MOTION:** `Dense market crowd. Carts. Smoke from dozens of chimneys. Laundry lines move between the houses.`

### 24 · 1480 · The Barbican
**EDIT:** `Build a round brick barbican in front of the main gate, connected by a bridge over the moat. Thicken the walls and add three more towers.`
**MOTION:** `Guards on the barbican. Crowd and carts crossing the bridge in both directions. Banners.`

### 25 · 1526 · Into the Crown
**EDIT:** `Replace the ducal banner on the keep with a royal one — a white eagle on red. Add a large stone royal coat of arms above the castle gate. Extend the castle with a new residential wing.`
**MOTION:** `The royal banner flies. A procession of riders and a carriage approach the castle gate. Crowd watching.`

### 26 · 1550 · Renaissance
**EDIT:** `Renaissance rebuild: replace steep Gothic gables with flat decorative attic parapets, add arcaded loggias on the square, repaint the merchant houses in ochre, red, pale green and blue. Add a stone well in the middle of the market square.`
**MOTION:** `Crowd around the well drawing water. Market stalls. Pigeons on the parapets. Laundry moving.`

### 27 · 1569 · The Sejm
**EDIT:** `Add a long low parliament hall with a colonnaded front beside the castle, and a large paved forecourt in front of it filled with parked carriages and horses.`
**MOTION:** `Nobles in long coats walk toward the parliament doors. Carriages arrive. Horses shift. Banners.`

### 28 · 1573 · Confederation
**EDIT:** `Add temporary wooden tribunes and rows of tents on the field outside the walls, with dozens of coloured banners of different noble houses.`
**MOTION:** `Dozens of banners move in the wind. Crowd fills the field. Riders move between the tents. Dust.`

### 29 · 1596 · The Court Arrives
**EDIT:** `Massively expand the castle: a new five-storey Renaissance front with a tall clock tower over the gate, formal gardens on the slope below. **Cut down the solitary oak on the right** — leave a wide fresh stump where it stood, to make room for the new wing.`
**MOTION:** `Clock tower banner flies. Long procession of carriages and mounted guards entering the castle gate. Crowd lining the road.`

### 30 · 1611 · Royal Residence
**EDIT:** `Finish the castle in early Baroque: symmetrical wings, a copper roof gone green, ornamental stone portal, guard posts. Pave the whole forecourt with fitted stone.`
**MOTION:** `Guards change post in slow steps. Carriages waiting. Flags on the towers. Crowd at the edge of the square.`

### 31 · 1620 · Baroque
**EDIT:** `Rebuild the merchant houses on the square in Baroque: curved decorative parapets, painted facades in cream, pink and pale blue, stone doorframes, shop signs hanging on iron brackets.`
**MOTION:** `Hanging shop signs swing gently. Dense market crowd. Carriages crossing. Pigeons.`

### 32 · 1637 · Expansion
**EDIT:** `Add three Baroque churches with domes and twin towers across the town, and two large noble palaces with courtyards and gated entrances.`
**MOTION:** `Bells in two towers. Carriages at the palace gates. Crowd. Smoke from many chimneys.`

### 33 · 1644 · The Column
**EDIT:** `Erect a tall free-standing stone column in the middle of the castle forecourt, topped with a bronze statue of a crowned king holding a cross and a sabre. This column must appear in every following image.`
**MOTION:** `Crowd gathered around the base of the new column, looking up. Banners. Pigeons settle on the statue.`

### 34 · 1650 · Golden Age
**EDIT:** `The city at its peak: every facade freshly painted, gilded details, flower boxes, full market, carriages everywhere, ships at the river landing. Bright warm golden light, richest colours of the whole video.`
**MOTION:** `Very busy: crowds, carriages, market stalls, laundry, flags, pigeons, boats on the river. The liveliest frame so far.`

---

# ГРУППА C · CAMERA C · эпохи 35–50

> Кадр 35 — **мастер-плита группы C**, но с оговоркой: сначала сгенерировать по CAMERA C **мирный кадр 1650** (тот же город с уровня площади), и уже его разрушить. Иначе пара «до/после» не сработает: зрителю нужно узнать те же здания.

### 35 · 1655 · THE DELUGE — пара катастрофы A
**EDIT:** `The same square, the same buildings, the same camera — sacked and burnt. Roofs collapsed, walls broken open, windows empty black holes, rubble across the cobbles, wrecked carts. The residence has lost its roof and one wing. Fires burning in three places, heavy black smoke across the sky. **The column still stands, scorched but upright.** Ash on everything, desaturated palette, red firelight.`
**MOTION:** `Fires burn and flicker. Heavy black smoke rolls across the sky from left to right. Embers and ash drift down through the frame. A loose shutter swings. No people at all.`

### 36 · 1660 · Empty
**EDIT:** `The fires are out. Cold grey ruins, ash washed grey by rain, weeds already growing between the cobbles, one leaning wall collapsed into the square. Flat overcast light, almost colourless. Two or three figures only.`
**MOTION:** `Rain falls lightly. Weeds bend. A tattered cloth flaps on a broken beam. Two figures cross the empty square slowly.`

### 37 · 1680 · Slow Rebuild
**EDIT:** `Rebuilding begins: scaffolding on three houses, fresh timber roof frames, stacks of brick and lime on the cobbles, a crane. Half the square is still ruins. Weak sunlight returning.`
**MOTION:** `Builders on the scaffolding. The crane turns slowly. Dust drifts. A cart delivers bricks.`

### 38 · 1700 · Baroque Restored
**EDIT:** `The square is rebuilt in full Baroque: new roofs, cream and ochre facades, stone portals, the residence complete again with a green copper roof. Clean cobbles. Warm light returns.`
**MOTION:** `Carriages cross the square. Crowd at the shop doors. Shop signs swing. Pigeons on the column.`

### 39 · 1720 · Saxon Era
**EDIT:** `Heavier Baroque: add sculpted stone figures on the parapets, ornate iron lanterns on brackets, a decorative fountain at the left of the square. Guards in tall mitre caps at the residence gate.`
**MOTION:** `Fountain water falls. Guards stand and shift. Carriages. Lanterns sway slightly.`

### 40 · 1740 · The Lime Tree
**EDIT:** `Plant a young lime tree in a small stone surround at the right edge of the square. It must appear in every following image and grow steadily. Add formal clipped hedges along the residence wall.`
**MOTION:** `The young lime's leaves move in the breeze. Fountain runs. Carriages and crowd. Guards at the gate.`

### 41 · 1764 · Enlightenment
**EDIT:** `Add tall glazed shop windows at street level, painted signboards, a bookshop and a coffee house with tables on the cobbles. Street lamps on posts. The lime tree is now twice as tall.`
**MOTION:** `People sitting at the coffee house tables. Crowd browsing shop windows. Lamp glass reflects. Lime leaves move.`

### 42 · 1780 · Neoclassical
**EDIT:** `Reface the residence in neoclassical style: flat pilasters, a triangular pediment over the centre, restrained cream and white. Straighten and repave the square in a radial cobble pattern around the column.`
**MOTION:** `Carriages circling the column. Crowd. Guards. Lime tree moving. Pigeons.`

### 43 · 1791 · Constitution Day
**EDIT:** `A celebration: the square packed with people, garlands and flags strung between the buildings, decorative arches, banners on every facade. Bright festive light.`
**MOTION:** `Dense celebrating crowd moving and waving. Dozens of flags and garlands in the wind. Confetti drifting. The most crowded frame of the video.`

### 44 · 1794 · Uprising
**EDIT:** `Fighting in the square: overturned carts and paving stones built into barricades, smoke, broken windows, scattered debris, a torn flag on the barricade. Grim overcast light.`
**MOTION:** `Smoke drifts across the square. The torn flag flaps hard. Small groups of figures move behind the barricade. Debris blows.`

### 45 · 1795 · Occupied
**EDIT:** `Clear the barricades. Foreign soldiers in dark blue coats stand in formation across the square, a foreign eagle standard replaces the flags on the residence. Repaired but joyless facades, few civilians. Cold grey palette.`
**MOTION:** `Soldiers stand in formation, barely shifting. The foreign standard flaps. A patrol marches slowly across the square. Few civilians hurry past.`

### 46 · 1807 · Duchy
**EDIT:** `Different foreign troops now: soldiers in blue and white with tall shakos, tricolour flags on the residence. Add a triumphal wooden arch at the left entrance to the square. Warmer light, more civilians back on the street.`
**MOTION:** `Troops march through the arch. Tricolour flags move. Civilians watch from the pavement. Drummers.`

### 47 · 1815 · Congress Kingdom
**EDIT:** `Another change of flags — a double-headed eagle standard on the residence. Add gas-free oil street lanterns on iron posts, a sentry box, and neat railings around the column base. Ordered, quiet, bureaucratic feel.`
**MOTION:** `A sentry stands almost still in his box. Carriages pass. The standard moves. Lime tree, now large, sways.`

### 48 · 1831 · Uprising Crushed
**EDIT:** `The square after the fighting: shell-pocked facades, one house roofless, broken lanterns, rubble against the residence wall, artillery pieces standing on the cobbles. Grey smoke, no celebration. **The column stands undamaged.**`
**MOTION:** `Smoke drifts low. Soldiers move slowly among the guns. A shutter bangs. Ash falls. Crows on the broken roof.`

### 49 · 1866 · Horse Trams
**EDIT:** `Industrial era arrives: repair everything, add a horse-drawn tram on rails crossing the square, telegraph poles with wires, large commercial shop windows, painted advertising on gable walls, gas street lamps.`
**MOTION:** `The horse tram crosses slowly on its rails. Pedestrians in top hats and bonnets. Gas lamps flicker. Wires sway.`

### 50 · 1890 · Tenements
**EDIT:** `Raise the buildings on the left to five-storey tenements with iron balconies and elaborate stucco. Add awnings over the shopfronts, a newspaper kiosk, a flower stall at the column base. The lime tree is now full-grown.`
**MOTION:** `Busy street: trams, carriages, pedestrians, awnings flapping. The flower stall vendor moves. Lime canopy sways.`

---

# ГРУППА D · CAMERA D · эпохи 51–75

> Кадр 51 — **мастер-плита группы D**. Генерится из кадра 50: `Same square, same buildings, same light — move the camera to face the residence head-on, per CAMERA D.`

### 51 · 1900 · Belle Époque
**EDIT:** `Same square head-on per CAMERA D. Add elaborate iron and glass shop canopies, ornate street lamps, a bench circle around the lime tree, and dense enamel advertising signs on the facades.`
**MOTION:** `Pedestrians in period dress cross the frame. A carriage passes. Canopy fabric ripples. Pigeons on the column.`

### 52 · 1908 · Electric Trams
**EDIT:** `Replace horse trams with an electric tram: overhead wires and catenary poles across the square, a red-and-cream tram car with a pantograph. Add the first electric street lights.`
**MOTION:** `The electric tram glides through slowly, pantograph sparking once. Wires sway. Crowd on the pavement. Lamps glow.`

### 53 · 1914 · War Begins
**EDIT:** `Mobilisation: recruitment posters pasted over the advertising, soldiers in grey with packs forming up, sandbags at the residence entrance, no civilian carriages. Cooler, drained palette.`
**MOTION:** `Soldiers form up and shuffle. Posters flap at the corners. A crowd of families watching. Grey clouds move.`

### 54 · 1915 · Occupation
**EDIT:** `Occupation: foreign signage in a different alphabet over the shops, a checkpoint with a striped barrier at the left, few civilians, shuttered shops, ration queue along the residence wall. Bleak light.`
**MOTION:** `The ration queue shuffles forward. The barrier lifts for a truck. Snow or cold rain. Steam from breath.`

### 55 · 1918 · Independence
**EDIT:** `Liberation: white-and-red flags on every single facade and on the residence, a huge crowd filling the square, banners, garlands. Bright breaking sunlight through the clouds.`
**MOTION:** `Enormous celebrating crowd waving. Dozens of flags snapping. Hats thrown in the air. Confetti falling.`

### 56 · 1920 · Battle of Warsaw
**EDIT:** `Wartime again but defiant: sandbag emplacements, a field gun, military trucks, soldiers and volunteers including civilians with rifles, a field hospital tent with a red cross at the left. Smoke on the horizon beyond the roofs.`
**MOTION:** `Trucks move slowly. Soldiers loading. Distant smoke drifts on the horizon. Red cross flag moves. Dust.`

### 57 · 1926 · Recovery
**EDIT:** `Peacetime: clear all military presence, restore shopfronts, add early automobiles and a bus, new neon-lit signs, repaired facades, a newspaper vendor at the column.`
**MOTION:** `Cars and a bus cross the square slowly. Neon signs flicker on. Pedestrians. Lime canopy moving.`

### 58 · 1933 · Modernism
**EDIT:** `Add a tall modernist skyscraper of pale stone and glass rising behind the rooflines at the left — clearly the tallest thing in the city. Replace two facades with clean functionalist fronts. More cars, brighter neon.`
**MOTION:** `Traffic flows. Neon signs pulse. Lights in the skyscraper windows. Crowd on the pavement.`

### 59 · 1938 · Peak — **пара катастрофы B, кадр «до»**
**EDIT:** `The city at its interwar best: everything clean and bright, full traffic, crowded pavements, glowing neon, flower stalls, awnings, the lime tree in full leaf. Warm golden late-afternoon light, rich saturated colour. **Study this frame carefully — the next six frames destroy exactly these buildings.**`
**MOTION:** `The busiest, warmest frame of the modern half: cars, tram, dense crowd, neon, pigeons, flags, awnings. Everything alive.`

### 60 · 1939 · The Bombing
**EDIT:** `The same square under bombardment. Three buildings on the left are burning shells, the residence has lost its roof and the clock tower is broken off, craters in the cobbles, a wrecked tram on its side, fallen wires. Fires and heavy black smoke. **The column still stands.** Firelight and dust, desaturated except the flames.`
**MOTION:** `Fires burn hard. Black smoke rolls upward. Dust and embers fall through the frame. Fallen wires sway. Debris shifting. No crowd.`

### 61 · 1940 · Occupation
**EDIT:** `Occupied city: makeshift repairs with boarded windows, foreign flags on the residence, checkpoints with barriers, patrolling soldiers, occupation notices pasted on walls. Add a high brick wall topped with wire closing the left side of the square. Grey, drained palette.`
**MOTION:** `Patrol marches across the frame. Notices flap on the walls. Barrier lifts for a vehicle. Cold grey clouds move.`

### 62 · 1943 · Razed
**EDIT:** `Beyond the brick wall on the left, the entire district is flattened to an empty grey field of rubble stretching to the horizon — no standing buildings at all on that side. Smoke rising from it. The right side of the square still stands, boarded and grey.`
**MOTION:** `Smoke drifts across the rubble field. Ash falls. The wall stands still. A single patrol at the barrier. Very still, very quiet frame.`

### 63 · 1944 · Uprising
**EDIT:** `Street fighting: barricades of paving stones, overturned trams and furniture across the square, a white-and-red armband flag raised on the barricade, smoke everywhere, burning buildings, insurgents behind cover. **The column is toppled — it lies broken across the cobbles, the statue face down.**`
**MOTION:** `Fires burn. Thick smoke crosses the frame. The flag on the barricade whips hard. Figures move low behind cover. Debris and sparks.`

### 64 · 1945 · Eighty-Five Percent — **пара катастрофы B, кадр «после»**
**EDIT:** `Total destruction. Not one intact building anywhere in frame. The residence is a jagged stump of wall. Every facade is a hollow shell or a mound of rubble. The square is buried under broken brick. **The broken column lies where it fell. The lime tree is a blackened stump.** Snow over the ruins, flat colourless winter light, no fires left, absolute silence.`
**MOTION:** `Snow falls slowly over the ruins. Thin cold smoke from one point. A loose sheet of metal shifts. One or two tiny figures pick their way through the rubble. The stillest frame in the video.`

### 65 · 1947 · Clearing
**EDIT:** `Rubble clearing: long human chains of civilians passing bricks hand to hand, sorted stacks of salvaged brick, narrow cleared paths through the debris, hand carts, a few tents. Still ruins, but organised. Weak spring light.`
**MOTION:** `The human chain passes bricks steadily. Carts move. Dust rises. People working across the whole frame.`

### 66 · 1953 · Rebuilt from Paintings
**EDIT:** `The square rebuilt exactly as it looked in 1938 — same facades, same colours, same rooflines, but visibly brand new: crisp unweathered paint, fresh cobbles, new window frames. Scaffolding still on two buildings. **The column is re-erected, repaired, standing again.** Clear bright light.`
**MOTION:** `Builders finishing the last scaffolded facade. Crowd walking the new square, looking up. Flags. Pigeons returning to the column.`

### 67 · 1955 · The Palace
**EDIT:** `Add an enormous tiered stone tower with a spire rising far behind the rooflines at the right — monumental, far taller than anything else, dominating the whole skyline. Add period buses and a large propaganda banner across one facade.`
**MOTION:** `Buses cross the square. Crowd. The banner ripples. Clouds move behind the tower spire. Lights coming on.`

### 68 · 1965 · Modernism
**EDIT:** `Add three plain concrete slab blocks behind the left rooflines, replace the old lamps with plain modern ones, add small boxy cars and a modern trolleybus, and plain state shop signage. **The lime tree has regrown from its stump into a young tree again.**`
**MOTION:** `Boxy cars and a trolleybus move. Pedestrians in period coats. The young lime moves. Grey clouds.`

### 69 · 1980 · Strike
**EDIT:** `A crowd rally in the square: hand-painted banners, a makeshift platform, thousands of people, no police visible. Damp cold light, drab clothing, but a dense determined crowd.`
**MOTION:** `Huge crowd moving and raising banners. Hand-painted cloth banners ripple. Steam from breath. Flags.`

### 70 · 1989 · Transformation
**EDIT:** `The first commercial signs appear over the plain state shops, a few Western cars among the boxy ones, market stalls with imported goods set up along the square, brighter clothing in the crowd.`
**MOTION:** `Mixed traffic. Market stalls busy. New signs. Crowd in colourful clothes. Awnings flapping.`

### 71 · 2000 · Glass
**EDIT:** `Add two glass office towers rising behind the skyline at the left, replace the shopfronts with modern glazed ones and international brand signage, add modern street furniture, contemporary cars and a modern low-floor tram.`
**MOTION:** `Modern traffic and tram. Crowd with shopping bags. Reflections moving in the glass towers. Lime tree large again.`

### 72 · 2015 · Skyline
**EDIT:** `Fill the background with a dense cluster of tall glass skyscrapers of varied heights. Add glass entrance pavilions for an underground station in the square, cycle lanes, planters and modern benches.`
**MOTION:** `People flowing in and out of the station pavilions. Cyclists. Traffic. Reflections travelling across the glass towers.`

### 73 · 2026 · Present Day
**EDIT:** `Add one very tall slender tower clearly rising above all others at the back. Add outdoor café seating across the square, tourists with phones, food trucks, and the fully grown lime tree with a wide canopy. Warm bright day, the square fully pedestrianised.`
**MOTION:** `Tourists photographing the column. Café crowd. Cyclists. Wide lime canopy swaying. Pigeons. Very lively.`

### 74 · 2050 · Green Future
**EDIT:** `Near future: the towers are clad in vertical gardens and solar glass, the square has mature trees and water channels through the cobbles, silent driverless pods glide on a marked lane, drones move overhead, holographic information panels stand at the corners. **The column and the lime tree are untouched and protected by a low rail.** Clean bright optimistic light.`
**MOTION:** `Driverless pods glide silently. Drones cross the sky. Holographic panels flicker and change. Water runs in the channels. Foliage sways.`

### 75 · 2075 · The Last Frame
**EDIT:** `Far future, and it has gone wrong: the green towers are dark and broken, vegetation overgrowing the square and pushing up through the cobbles, dead holographic panels flickering, a wrecked pod on its side, low mist, rain. **The column still stands, weathered and leaning slightly. The lime tree is enormous, wilder than ever, roots cracking the stones.** Dark blue-grey palette with cold neon glow from one dying sign.`
**MOTION:** `Rain falls. One dying neon sign flickers. Mist drifts through the ruins. Overgrown branches sway heavily. A single bird crosses. Then stillness — the final frame of the video, cut to black from here.`

---

## СБОРКА

| Параметр | Значение |
|---|---|
| Кадр 1 | 4 с |
| Кадры 2–75 | 8 с каждый |
| Итого | 596 с = **9:56** |
| Переход | кросс-диссолв **1.0 с**, единственный тип |
| Титр | правый верх, год крупно + название эпохи мелко, белая антиква, без анимации |
| Смена плиты | кадры 19, 35, 51 — единственные места, где рамка меняется |

**Пары катастрофы** — не трогать тайминг, это хребет ролика:
- 13 → 14 (1262 → 1281)
- 34 → 35 (1650 → 1655) — Потоп
- 59 → 60 (1938 → 1939) — бомбардировка
- 63 → 64 (1944 → 1945) — 85% разрушено

**Музыкальные зоны:** эмбиент (1–8) → фолк (9–22) → ренессанс/оркестр (23–34) → мрачный оркестр (35–48) → индустриальный (49–58) → военный (59–65) → восстановление (66–72) → синт (73–75).

**Шумовой слой** меняется каждый кадр, −18…−22 dB под музыкой. Полная тишина кроме ветра — только в кадре 64.
