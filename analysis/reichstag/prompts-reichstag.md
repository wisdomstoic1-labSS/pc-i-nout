<!-- frames: 60 -->
# Рейхстаг — 60 кадров, 7:56

Хронометраж: `4 с + 59 × 8 с = 476 с = 7:56`
Точка: Площадь Республики (Кёнигсплац), западный фасад Рейхстага, три четверти.
**Одна камера на весь ролик.** Смены ракурса нет ни разу.

Охват: короткий пролог с пустого места → 1871 → 2026. Будущего нет.
Периоды, где на площади ничего не менялось, выброшены.

---

## ДИСЦИПЛИНА ДЕТАЛЕЙ

Два правила появились после реальных ошибок в прошлом ролике и вшиты в каждый промпт.

**Флаги.** Модель по умолчанию рисует звёздно-полосатый флаг, если не сказано иное.
Поэтому: ни одного слова «флаг» без описания полос и цветов, и в каждом таком кадре
явный запрет на любые другие. Точная хронология флагов на здании:

| Годы | Что на флагштоке |
|---|---|
| 1871–1918 | три горизонтальные полосы: чёрная сверху, белая в середине, красная снизу |
| 1919–1933 | три горизонтальные полосы: чёрная, красная, золотая |
| 1933–1945 | флагов в кадре нет — период показан через само здание |
| 1945 | одно простое красное полотнище на крыше, без символов |
| 1949–2026 | три горизонтальные полосы: чёрная, красная, золотая |

**Транспорт.** Конка — это вагон на рельсах, который тянут лошади, а не лошадь рядом
с трамваем. Формулировка `horse tram` даёт ровно вторую картинку, поэтому в промптах
она расписана целиком: `an open four-wheeled tram car running on rails, pulled by two
horses in harness, with no engine, no overhead wires and no pantograph`.

---

## БЛОК STYLE — дословно в каждую генерацию

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
```

**NEGATIVE:**
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

---

## БЛОК КАМЕРЫ — один на все 60 кадров

### CAMERA A — кадры 1–60
```
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

## БЛОКИ ЯКОРЕЙ

### ANCHORS A
```
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
```

#### NOTE 1
Вход: ничего. Единственный кадр, который генерится с нуля (text-to-image).
Это мастер-плита всего ролика — от неё зависят все 59 остальных кадров,
и переснять её потом означает переснять всё. Сгенерить 10–20 вариантов
и выбирать придирчиво: важно, чтобы линия горизонта, деревья слева и
пустое пятно справа встали ровно так, как описано в камере.

---

# ПРОЛОГ · пустое место

### 1 · 1700 · Marshland — **4 секунды** — МАСТЕР-ПЛИТА
Единственный кадр с нуля: `STYLE + CAMERA A + сцена ниже`.
**SCENE:** `A flat marshy clearing on the edge of a great oak forest, with no buildings of any kind anywhere in the frame. Reed beds and standing pools of dark water across the open ground, tussocks of coarse grass, a few dead birches. The dense forest treeline closes the far left. Nothing at all stands on the open ground in the centre-right. Overcast pale sky, muted green and brown palette.`
**MOTION:** `Reeds bend slowly in the wind. Water ripples in the pools. A heron lifts off from the far side. The forest canopy sways. Nothing else moves.`

### 2 · 1790 · The Parade Ground
**EDIT:** `The marsh has been drained and levelled into a flat sandy exercise ground. The pools and reeds are gone, replaced by bare packed sand and gravel with cart ruts across it. A low wooden post-and-rail fence runs along the left side. One small wooden guardhouse with a shingled roof stands at the far left edge. The plot in the centre-right is still completely empty. Clear pale sky.`
**MOTION:** `Dust drifts across the sand in a light wind. A single cart crosses in the far distance. The treeline sways. Very empty and still.`

### 3 · 1850 · Königsplatz
**EDIT:** `The ground is now a formal city square: raked gravel, a low stone kerb around its edge, and a double row of young Minecraft lime trees planted along the left side. Gas lamps on iron posts stand at intervals. A long low theatre building of pale stone with a columned front stands far back on the left, beyond the trees. The plot in the centre-right is still empty ground. Clear bright day.`
**MOTION:** `Young trees sway. A carriage crosses the gravel. Two figures walk the kerb line. Gas lamp glass catches the sun.`

### 4 · 1871 · The Empire
**EDIT:** `The square is decorated for a celebration: a temporary wooden triumphal arch of painted timber stands at the left, garlands of greenery strung between the lime trees, and rows of flagpoles along the kerb. Every flag on those poles has three horizontal bands - black on top, white in the middle, red at the bottom - and there are NO other flags of any kind in the frame. A festive crowd in top hats and bonnets fills the gravel. The plot in the centre-right is still empty.`
**MOTION:** `Dozens of striped banners lift and fall in the wind. The crowd moves and waves hats. Garlands sway between the trees.`

---

# СТРОИТЕЛЬСТВО И ИМПЕРИЯ

### 5 · 1873 · The Victory Column
**EDIT:** `Erect a tall fluted stone column on a square stepped stone base in the LEFT third of the square, with a small gilded figure standing on its top. It is far taller than the lime trees and must appear in every following image until it is explicitly removed. The temporary arch and garlands are gone; the square is back to ordinary use with carriages and pedestrians.`
**MOTION:** `A small crowd stands at the base of the new column, looking up. Carriages cross the gravel. Pigeons settle on the figure. Trees sway.`

### 6 · 1877 · The Old Palace
**EDIT:** `An older building now stands on the plot in the centre-right: a wide three-storey palace of pale plastered stone with a low pitched roof, a modest columned entrance and regular tall windows. It is clearly an older, plainer building than a parliament. The square and the column are unchanged.`
**MOTION:** `Carriages wait at the palace entrance. Pedestrians cross the gravel. The column stands still. Trees sway.`

### 7 · 1884 · Foundations
**EDIT:** `The old palace is gone. In its place a large rectangular excavation pit with stepped earth sides, surrounded by a timber hoarding. Stacks of pale sandstone blocks, timber piles and two tall wooden cranes stand around the pit. Rails for spoil carts run across the site. The column and the square are unchanged.`
**MOTION:** `Spoil carts run on the rails. A crane wheel turns and lifts a stone. Workers move in the pit. Dust rising.`

### 8 · 1886 · The First Courses
**EDIT:** `The excavation is finished and filled with a massive stone foundation. The first three courses of pale sandstone wall now stand above ground level all round the plot, so the full rectangular footprint of the building is visible for the first time. Low timber scaffolding along the walls, two cranes, stacks of dressed stone and a mortar mixing area. The column and the square are unchanged.`
**MOTION:** `A crane lowers a dressed block into place. Masons working along the low walls. A horse cart delivering stone. Dust drifting.`

### 9 · 1888 · Walls Rising
**EDIT:** `The walls of the new building stand to the height of the first storey, in pale sandstone blocks, wrapped in a forest of timber scaffolding with plank walkways at three levels. Three cranes rise above it. The outline of the six-column portico is already recognisable at the centre of the west front.`
**MOTION:** `Builders move along the scaffold walkways. Cranes turn slowly. A stone block is lifted. Dust drifts across the site.`

### 10 · 1891 · The Shell
**EDIT:** `The building has reached its full height of 16 blocks to the cornice, with all four square corner towers built. The six-column portico and its triangular pediment are complete. Scaffolding remains only around the centre of the roof, where a stepped ring of copper and glass is being assembled.`
**MOTION:** `Work concentrated on the roof ring. A crane lifts a glass section. Builders on the upper scaffold. Pigeons on the finished towers.`

### 11 · 1894 · Finished
**EDIT:** `All scaffolding is gone. The building is complete: pale sandstone facade, six-column portico over a wide flight of stone stairs, four corner towers with small stepped copper roofs, and a large stepped dome of glass blocks and copper stairs standing directly above the centre. One flagpole on the roof flies a flag with three horizontal bands - black on top, white in the middle, red at the bottom. No other flag anywhere in the frame. Bright clear day, the building at its cleanest.`
**MOTION:** `The striped flag lifts and falls on the roof. A crowd on the entrance stairs. Carriages at the kerb. Pigeons around the dome.`

### 12 · 1898 · The Square Laid Out
**EDIT:** `The square in front is relaid: pale stone paving replacing the gravel, formal hedged flower beds, a stone basin with a low fountain at the left, and taller lime trees. More gas lamps, iron benches, and a row of waiting carriages along the kerb.`
**MOTION:** `The fountain runs. Carriages waiting, horses shifting. People on the benches. Pigeons at the basin.`

### 13 · 1900 · The Empire at Its Height
**EDIT:** `The square at its most prosperous: the flower beds in full bloom, the fountain running, every gas lamp lit at dusk, a long rank of polished carriages, officers and ladies in formal dress on the entrance stairs, a military band playing at the left. The building is new and spotless, the flag on the roof with three horizontal bands - black on top, white in the middle, red at the bottom - and no other flag anywhere.`
**MOTION:** `The band plays, small figures swaying. Carriages arriving and departing. The striped flag lifting. Fountain running. Warm lamp glow.`

### 14 · 1902 · First Motor Cars
**EDIT:** `Add three early motor cars with high bodies and spoked wheels parked at the kerb among the carriages, and electric street lamps on taller plain posts replacing some of the gas lamps. Pedestrians in longer coats.`
**MOTION:** `A motor car pulls away slowly. Carriages alongside. Pedestrians crossing. Electric lamps glowing faintly.`

### 15 · 1906 · The Horse Tram
**EDIT:** `A tram line now crosses the square: two steel rails set flush into the paving, with an open four-wheeled tram car running on them, pulled by two horses in harness walking between the rails in front of it. The car has no engine, no overhead wires and no pantograph, and there are no poles or cables of any kind above it. A small wooden tram stop shelter stands at the kerb.`
**MOTION:** `The two horses walk slowly forward, drawing the tram car along the rails. Passengers on the open platform. Pedestrians crossing behind it.`

### 16 · 1910 · Electric Trams
**EDIT:** `Replace the horse tram with an electric one: a closed red-and-cream tram car on the same rails with a pantograph on its roof, overhead wires strung on plain catenary poles along the line. The horses are gone completely. More motor cars, fewer carriages, a newspaper kiosk at the kerb.`
**MOTION:** `The electric tram glides along the rails, pantograph sparking once. Wires sway. Motor cars pass. Crowd at the kiosk.`

### 17 · 1914 · Mobilisation
**EDIT:** `A huge crowd packs the square and the entrance stairs. Printed notices are pasted on boards at the kerb and on the tram shelter. Families waving, men with suitcases. The flag on the roof has three horizontal bands - black, white, red - and there is no other flag in the frame. Bright hard summer light.`
**MOTION:** `The crowd surges and waves. Notices flap on the boards. Hats raised. Dust over the paving.`

### 18 · 1916 · The Inscription
**EDIT:** `Add a row of large plain bronze capital letters fixed to the frieze above the six columns of the portico, reading DEM DEUTSCHEN VOLKE. These are the ONLY letters anywhere in the image. The square is quieter, fewer people, no motor cars, a shabbier look.`
**MOTION:** `A few figures on the stairs looking up at the new letters. The striped flag on the roof. Wind across the empty paving.`

---

# ВЕЙМАР

### 19 · 1918 · The Republic
**EDIT:** `A dense crowd in winter coats fills the square, looking up at one open window of the building where a small figure stands speaking. Plain red banners hang from two balconies - plain cloth, with no emblem, no symbol and no lettering on them. The roof flagpole is bare. Cold grey light, bare lime trees, breath steaming.`
**MOTION:** `The crowd presses forward and raises hands. The plain red banners lift in a cold wind. Breath steaming. The speaker gestures.`

### 20 · 1919 · Black, Red, Gold
**EDIT:** `The red banners are gone. One flag flies from the roof flagpole with three horizontal bands - black on top, red in the middle, gold at the bottom - and no other flag appears anywhere in the frame. The square is orderly again, the paving swept, a few motor cars and a tram, ordinary pedestrians.`
**MOTION:** `The black-red-gold flag lifts and falls on the roof. A tram passes. Pedestrians crossing. Trees in early leaf.`

### 21 · 1923 · Hard Times
**EDIT:** `The square looks poor: a long queue of people along the kerb, handcarts, shabby coats, bare flower beds gone to weeds, two broken gas lamps, paper litter blowing across the paving. Fewer vehicles. Grey overcast light, drained colours. The black-red-gold flag still flies on the roof.`
**MOTION:** `The queue shuffles slowly forward. Litter blows across the paving. The flag hangs limp. Grey clouds move.`

### 22 · 1926 · The Twenties
**EDIT:** `Prosperity returns: the flower beds replanted, new clean paving, a line of taxis, a double-decker bus, an advertising column at the kerb, well-dressed crowds with hats and umbrellas, a photographer with a tripod on the stairs.`
**MOTION:** `Traffic flows around the square. The bus pulls away. Crowds crossing. The photographer works under his cloth.`

### 23 · 1930 · Depression
**EDIT:** `Hard times again and visibly political: rows of printed paper posters pasted over the advertising column and along the hoardings, a queue at a soup cart, men standing about with nothing to do, fewer vehicles. The posters carry no readable words, only blocks of colour. Cold flat light.`
**MOTION:** `Posters flap at the corners. The soup queue shuffles. Men standing still, shoulders hunched. Dead leaves blowing.`

---

# ТЁМНЫЕ ГОДЫ · только здание

### 24 · 1933 · The Fire
**EDIT:** `The building is burning. Flames pour from the windows of the whole central section and from the base of the dome; the glass of the dome is shattered and its copper ribs stand black against the fire. Heavy black smoke rolls across the sky to the right. Two horse-drawn fire pumps and one motor fire engine stand on the square with hoses running to the stairs. No flags anywhere: the roof flagpole is bare. Night, orange firelight on the facade and on the snow.`
**MOTION:** `Fires burn hard in the windows and the dome. Black smoke rolls upward. Embers rise and drift. Hoses jetting water. Firelight flickering on the stone.`

### 25 · 1934 · Burnt Out
**EDIT:** `The fire is out. The central section is a blackened shell: window openings empty and soot-streaked, the dome reduced to a bare skeleton of copper ribs with no glass left in it, the roof behind it collapsed. Rough timber boards nailed over the ground-floor windows and doors. A plain wire fence around the stairs. The flagpole is bare and no flag appears anywhere. Grey winter light, soot on the snow.`
**MOTION:** `Thin smoke still drifts from one opening. Loose boards creak. Snow falling lightly. Crows on the dome ribs. No people.`

### 26 · 1937 · Empty
**EDIT:** `The building stands unused: boards still over the windows, the bare dome skeleton above, weeds growing through the cracks of the entrance stairs, streaked soot stains down the facade. The square in front is neatly kept but empty of people. No flags anywhere in the frame. Flat overcast daylight.`
**MOTION:** `Weeds bend on the stairs. A single caretaker crosses the square. Clouds move slowly. Very still and quiet.`

### 27 · 1939 · The Column Is Gone
**EDIT:** `The tall fluted victory column and its stepped base have been removed from the left third of the square completely - there is now only a circle of fresh pale paving where it stood, and open sky where its figure used to be. Everything else is unchanged. This absence must persist in every following image.`
**MOTION:** `Wind across the empty paving circle. Trees sway. Two workmen loading the last stones onto a cart. Very open and bare on the left.`

### 28 · 1941 · Blackout
**EDIT:** `The building is prepared for air raids: large nets with green and brown cloth strips stretched over the roof and the dome skeleton, sandbags stacked around the base of the portico columns, the boarded windows painted dark, the street lamps hooded with narrow slits. An anti-aircraft gun on a sandbag emplacement stands on the square. No flags anywhere. Cold grey light.`
**MOTION:** `The camouflage netting billows slowly. The gun crew shifts at the emplacement. Hooded lamps glowing faintly. Heavy clouds.`

### 29 · 1944 · Bomb Damage
**EDIT:** `The building is badly damaged: a large section of the roof has fallen in, several window openings are torn into ragged holes with missing blocks around them, the portico pediment is chipped and one column is scarred. Bomb craters in the paving of the square, a burnt-out lorry, the camouflage netting hanging in shreds. Drifting dust. No flags anywhere.`
**MOTION:** `Torn netting flaps. Dust drifts from the broken roof. Loose blocks shift and fall. Smoke on the far horizon.`

### 30 · 1945 · The Battle
**EDIT:** `Heavy fighting damage: the facade pocked and scarred all over, most window openings blown out, the roof largely gone, the dome skeleton twisted and half collapsed, deep craters across the square, wrecked vehicles and scattered blocks. Thick smoke drifting across the whole frame, small fires in the ruins. No flags anywhere yet.`
**MOTION:** `Smoke rolls across the frame. Small fires flicker in the openings. Dust falling. Loose blocks tumbling. No people visible.`

### 31 · 1945 · The Flag on the Roof
**EDIT:** `The fighting is over. The building stands gutted and roofless, its facade scarred, the dome skeleton a twisted ruin. One plain red flag - plain red cloth with no emblem, no symbol and no lettering on it - flies from a pole on the broken roof. It is the only flag in the frame. Rubble and wrecked vehicles across the square, a few small figures picking through the debris. Flat colourless light, no fires left.`
**MOTION:** `The plain red flag lifts slowly on the roof. Thin cold smoke from one point. Two small figures moving through the rubble. Dust settling. The stillest frame so far.`

---

# ПОСЛЕ ВОЙНЫ

### 32 · 1945 · The Ruin in Daylight
**EDIT:** `Clear summer daylight on the gutted building for the first time: no smoke, no fires, every scar on the pale sandstone facade sharply visible, the window openings empty, the roof gone, the dome a twisted stump. The plain red flag still on its pole. Soldiers and civilians stand about on the rubble of the square, several of them photographing the ruin, a jeep parked at the foot of the stairs. Bright hard light.`
**MOTION:** `Small groups moving over the rubble. A photographer crouching to frame a shot. The plain red flag lifting. Dust in the sunlight.`

### 33 · 1946 · Vegetable Gardens
**EDIT:** `The square in front has been dug up into small fenced vegetable plots with neat rows of green crops, garden sheds of salvaged boards, and water barrels. The gutted building stands behind it unchanged, roofless and scarred. The flagpole is bare. Warm summer light over the incongruous gardens.`
**MOTION:** `People working the vegetable rows, bent over. A watering can pouring. Crops swaying. Smoke from a small fire.`

### 34 · 1948 · The Great Rally
**EDIT:** `An enormous crowd fills the whole square in front of the ruin, tens of thousands of small figures packed shoulder to shoulder, with a wooden speaker's platform set up at the foot of the entrance stairs. The gardens are gone. The building behind is still the gutted ruin. Plain black-red-gold flags on two poles at the platform and no other flags anywhere. Cold autumn light.`
**MOTION:** `The vast crowd moves and raises hands. Black-red-gold flags snap at the platform. Breath steaming. The speaker gestures.`

### 35 · 1951 · Clearing
**EDIT:** `Rubble clearing across the square: sorted stacks of salvaged brick and stone, a light railway with spoil tips, hand carts, teams of workers in lines. The ruined building behind is being made safe, with rough timber props against two walls and a plain wire fence around it.`
**MOTION:** `Spoil carts run on the light rails. Workers passing blocks along a chain. Dust rising. A crane arm swinging slowly.`

### 36 · 1954 · The Dome Comes Down
**EDIT:** `The twisted dome skeleton is being demolished: half of its copper ribs already gone, a tall crane lifting a section clear, the rest cut back to a low stump above the roofline. After this year the building has NO dome at all until it is explicitly rebuilt. The facade is still scarred and the windows still empty.`
**MOTION:** `The crane lifts a rib section away slowly. Dust falls from the cut. Workers on the roof deck. Spectators at the fence.`

### 37 · 1957 · The Bare Ruin
**EDIT:** `The square is fully cleared and sown with rough grass. The building stands as a plain roofless shell with a flat stump where the dome was, its facade cleaned of soot but still pitted, window openings boarded. Nothing else on the square: no trees on the right, no traffic, no fences. Very empty. Flat daylight.`
**MOTION:** `Long grass bends in the wind across the square. A single figure walking. Clouds moving. Silent and open.`

### 38 · 1961 · The Wall
**EDIT:** `A grey concrete barrier wall with a rounded top now runs across the frame immediately behind and to the right of the building, cutting the view off. A tall watchtower stands behind it and a cleared strip of raked sand runs in front of it. The building is unchanged, still a roofless shell. The square in front is empty grass.`
**MOTION:** `A guard patrol walks the raked strip behind the wall. Wind across the grass. Grey clouds moving. Nothing else.`

### 39 · 1964 · Reconstruction
**EDIT:** `The building is wrapped in modern tubular steel scaffolding with safety netting, and a tower crane stands beside it. The roof is being rebuilt flat, with no dome. Contractor huts and stacks of materials on the grass. The wall and watchtower behind are unchanged.`
**MOTION:** `The tower crane swings slowly. Safety netting billows. Workers on the scaffold decks. Machinery below.`

### 40 · 1967 · Halfway
**EDIT:** `Reconstruction well advanced: the scaffolding now covers only the upper half of the building, the new flat roof is finished and watertight, and the lower facade has been cleaned to bare pale stone with new glass already in the ground-floor windows. A tower crane still stands beside it. Contractor huts and a muddy access road across the grass.`
**MOTION:** `The tower crane swings a load slowly. Workers on the upper scaffold. A lorry on the muddy access road. Netting billowing.`

### 41 · 1971 · Reopened
**EDIT:** `The scaffolding is gone. The building is restored but visibly simplified: the sandstone facade cleaned to a uniform pale colour, the six-column portico and the inscription intact, but a plain flat roof with NO dome at all, and the four corner towers rebuilt lower and plainer. New clear glass in every window. A flag with three horizontal bands - black, red, gold - on a pole at the front, and no other flag in the frame. Neat lawns and new paving in front.`
**MOTION:** `The black-red-gold flag lifts on its pole. Visitors on the entrance stairs. A coach parked at the kerb. Trees in full leaf.`

---

# РАЗДЕЛЁННЫЙ ГОРОД

### 42 · 1976 · The Death Strip
**EDIT:** `Behind the building the barrier is now a full system: the concrete wall in front, a wide raked sand strip, a second inner wall, floodlight masts and two watchtowers. On this side, a wooden tourist viewing platform with a flight of steps stands at the right edge of the square, with visitors on top looking over. Tour coaches at the kerb.`
**MOTION:** `Visitors climbing the viewing platform and pointing. A patrol on the strip beyond. Floodlight masts still. Coaches idling.`

### 43 · 1982 · Graffiti
**EDIT:** `The western face of the concrete wall is now covered in dense multicoloured spray-painted graffiti from end to end - blocks of colour and shapes only, no readable words or letters anywhere. A second viewing platform has been built. More tourists, souvenir stands, parked cars.`
**MOTION:** `Tourists on both platforms. A souvenir stand awning flapping. Cars pulling in. A patrol visible beyond the wall.`

### 44 · 1987 · Anniversary
**EDIT:** `The square is decorated for a city anniversary: rows of flagpoles along the kerb, all flying the same three-band black, red and gold flag and nothing else, banners of plain colour between the lime trees, a temporary stage at the left, market stalls and a crowd. The building and the wall behind are unchanged.`
**MOTION:** `Rows of black-red-gold flags moving together. Crowd at the stalls. Stage bunting swaying. Busy and cheerful.`

### 45 · 1989 · The Wall Falls
**EDIT:** `An enormous crowd fills the square and people are standing on top of the concrete wall itself, dozens of figures along it, with more climbing up. Camera flashes, plain black-red-gold flags waving in the crowd and no other flags. A section of the wall has been broken open. Cold night, hard floodlight from the platforms, breath steaming.`
**MOTION:** `The crowd surges and cheers. People climbing the wall. Flags waving. Camera flashes popping. Breath steaming in the cold.`

### 46 · 1990 · Reunification
**EDIT:** `A vast crowd fills the square in front of the building at night. One very large flag with three horizontal bands - black, red, gold - is being raised on a tall new pole directly in front of the entrance stairs, lit by floodlights. No other flag of any kind appears in the frame. Fireworks in the sky above the roofline.`
**MOTION:** `The large flag rises slowly up the pole and unfurls. Fireworks bursting above. The crowd looking up. Floodlight beams on the facade.`

### 47 · 1991 · The Wall Comes Down
**EDIT:** `The concrete wall is being demolished: long sections already gone leaving a raw strip of churned earth, a crane lifting a painted slab onto a lorry, the watchtowers cut down to stumps. Beyond the gap, ordinary streets and buildings are visible for the first time.`
**MOTION:** `The crane lifts a painted wall slab slowly. An excavator working the earth strip. Dust. Onlookers at a rope line.`

### 48 · 1993 · The Scar
**EDIT:** `The wall is gone completely. Where it stood there is a wide strip of bare ground and temporary gravel, with survey pegs and orange netting. The building stands plain and domeless, clean, with the black-red-gold flag on its pole. Ordinary traffic crossing behind.`
**MOTION:** `Orange netting flutters on the pegs. Traffic crossing the bare strip. The flag lifting. Dust from the gravel.`

---

# НОВОЕ ВРЕМЯ

### 49 · 1995 · Wrapped
**EDIT:** `The entire building is completely wrapped in shimmering silvery fabric, from the ground to the roofline, tied with dark blue rope in long vertical lines. The portico, the columns, the towers and the windows are all hidden under the cloth, so only the soft blocky shape of the building remains. A huge relaxed crowd sits and stands on the grass of the square looking at it. Bright summer day.`
**MOTION:** `The silver fabric ripples slowly over the whole facade in the breeze. Ropes sway. The crowd sitting and walking on the grass. A very calm frame.`

### 50 · 1995 · Unwrapped
**EDIT:** `The fabric and ropes are gone. The building stands bare and empty, its windows dark, with modern tubular scaffolding going up around the west front and a tower crane beside it. Contractor hoardings around the base. The crowd is gone; the grass is trampled.`
**MOTION:** `A crane lifting a scaffold section. Workers erecting frames. Trampled grass. A few passers-by.`

### 51 · 1997 · Rebuilding
**EDIT:** `Deep reconstruction: the building is stripped inside, its roof opened up, two tower cranes above it, and a large circular steel ring is being assembled at the centre of the roof - the base of a new dome. Scaffolding covers the whole facade. Hoardings along the square.`
**MOTION:** `Two cranes swing slowly. A curved steel section is lifted into the ring. Sparks from welding. Safety netting billowing.`

### 52 · 1999 · The Glass Dome
**EDIT:** `All scaffolding is gone. The building is fully restored and above its centre stands a NEW dome, completely different from the old one: a large stepped hemisphere built from clear glass blocks with a visible spiral ramp of stone stairs winding up inside it, bright and transparent against the sky. The facade is clean pale sandstone, the inscription intact, the black-red-gold flag on its pole. New lawns and paving in front.`
**MOTION:** `Tiny figures moving up the spiral ramp inside the glass dome. The flag lifting. Visitors on the entrance stairs. Clouds reflected in the glass.`

### 53 · 2001 · The Queue
**EDIT:** `A long queue of visitors winds across the square to the entrance, with rope barriers and a security cabin. Tour coaches in a rank at the kerb, souvenir stalls, people photographing the dome from the lawn.`
**MOTION:** `The queue shuffles forward. Coaches pulling in. Visitors photographing. Figures moving inside the glass dome.`

### 54 · 2005 · The Government Quarter
**EDIT:** `Behind and to the right of the building, where the wall once stood, a row of large modern government buildings in white concrete and glass now closes the view, connected by a long horizontal block. A new pedestrian bridge crosses in the distance. The square in front is finished with clean paving and mature lawns.`
**MOTION:** `Reflections travelling across the modern glass. Pedestrians on the bridge. The queue at the entrance. The flag lifting.`

### 55 · 2006 · The Fan Zone
**EDIT:** `A football festival fills the square: two enormous screens on scaffold towers facing a sea of tens of thousands of people, temporary barriers, food and drink stands along the edges. The crowd is waving small flags with three horizontal bands - black, red and gold - and no other nation's flag appears anywhere in the frame. Summer evening, screen glow on the faces, the building and its glass dome lit behind.`
**MOTION:** `The vast crowd jumping and waving. Thousands of small black-red-gold flags moving. Screen light flickering over the crowd. The dome glowing behind.`

### 56 · 2010 · Solar and Cycles
**EDIT:** `Add rows of dark solar panels on the flat roof sections either side of the dome, a marked cycle lane across the square with a bicycle stand, modern benches and litter bins, and a line of young replacement trees. More casual visitors, fewer coaches.`
**MOTION:** `Cyclists crossing the square. Visitors on the benches. Figures in the dome. Panels catching the light.`

### 57 · 2015 · Full Season
**EDIT:** `Peak tourist season: the lawns covered with people sitting and picnicking, a long entrance queue, ice cream carts, segway tours, dozens of raised phones. Everything green and well kept. Bright warm day.`
**MOTION:** `Dense relaxed crowd on the lawns. Queue shuffling. Carts serving. Phones raised. The busiest frame of the series.`

### 58 · 2020 · Empty
**EDIT:** `The square is almost deserted: the entrance closed with a barrier and a sign board carrying no readable words, only blocks of colour, the lawns empty, a handful of masked figures far apart, no coaches, no stalls. The building itself is unchanged and immaculate. Flat grey light.`
**MOTION:** `Wind across the empty lawns. Two distant figures crossing far apart. The flag lifting. The stillest modern frame.`

### 59 · 2023 · Life Returns
**EDIT:** `People are back: a moderate queue, groups on the lawns, cycle traffic, food trucks at the kerb, new flower planters. More greenery than before, some of the lawn replaced with wildflower meadow.`
**MOTION:** `Queue moving. Cyclists. Food truck serving. Wildflowers swaying. Figures in the dome.`

### 60 · 2026 · Present Day
**EDIT:** `The building today, at its best: clean pale sandstone, the glass dome bright above it, the black-red-gold flag on its pole and no other flag anywhere. Mature trees, wildflower meadow and lawns, modern benches, cycle lanes, a busy but relaxed crowd, the government quarter complete behind. Warm bright late-afternoon light, long shadows, the richest frame of the series.`
**MOTION:** `Visitors spiralling up inside the glass dome. Crowd on the lawns. Cyclists passing. The flag lifting and falling. Swallows over the roofline. Then stillness — the final frame, cut to black from here.`
