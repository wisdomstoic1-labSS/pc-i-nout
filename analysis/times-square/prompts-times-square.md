<!-- frames: 60 -->
# Таймс-сквер — 60 кадров, 7:56

Хронометраж: `4 с + 59 × 8 с = 476 с = 7:56`
Точка: перекрёсток Бродвея и Седьмой авеню, взгляд на юг, треугольный квартал в центре.
**Одна камера на весь ролик.** Смены ракурса нет ни разу.

Охват: короткий пролог с пустого места → 1872 → 2026 → три кадра будущего.

Переходы делаются в режиме «первый кадр — последний кадр»: см.
`transition-prompts-times-square.md`. Монтажных диссолвов нет.

---

## ГЛАВНЫЙ СЮЖЕТ

У Варшавы здание разрушали, у Рейхстага стирали трижды. Здесь другое:
**здание в центре кадра ни разу не сносили — его переодевали.**

```
1899  на треугольнике стоит отель
1903  отель сносят, роют котлован
1904  башня газеты: камень, узкая, с башенкой
1928  на неё вешают бегущую строку
1964  башню обдирают до каркаса и обшивают белым мрамором
1998  мрамор закрывают экранами
2026  от здания видна только реклама
```

Один и тот же дом в одном и том же месте, который к финалу исчезает под тем,
что на нём висит. Это и есть сквозной сюжет ролика.

---

## ДИСЦИПЛИНА ДЕТАЛЕЙ

**Реклама вымышленная.** Таймс-сквер состоит из реальных брендов, но просить
генератор их рисовать нельзя: логотипы он всё равно изуродует, а сам кадр станет
юридически мусорным. Поэтому во всех промптах: щиты и экраны несут **выдуманные
короткие слова, абстрактные цветовые блоки и силуэты**, никаких настоящих
названий и знаков. Эпоха читается по типу вывески, а не по бренду:

| Годы | Чем светится площадь |
|---|---|
| 1880–1895 | крашеные деревянные щиты, газовые фонари |
| 1895–1910 | дуговые лампы, первые щиты с лампами накаливания |
| 1910–1940 | тысячи ламп накаливания, «Великий белый путь» |
| 1942–1945 | затемнение: всё погашено |
| 1945–1975 | неоновые трубки, анимированные щиты |
| 1975–1995 | облезлый неон, щиты кинотеатров |
| 1995–2005 | первые пиксельные экраны рядом с неоном |
| 2005–2026 | сплошной LED от земли до крыш |

**Флаги.** Здесь американский флаг уместен и историчен, но описывать его надо
явно, а не словом «флаг»: `a flag with thirteen alternating red and white
horizontal stripes and a blue rectangle of white stars in its upper corner`.
И запрет на прочие: `no other nation's flag anywhere`.

**Транспорт по эпохам.** Конка — `an open tram car running on rails, pulled by two
horses in harness, no engine, no overhead wires`. Дальше электрический трамвай с
пантографом, потом автомобили эпохи, потом жёлтые такси.

---

## БЛОК STYLE — дословно в каждую генерацию

```
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
```

**NEGATIVE:**
```
real brand, real logo, trademark, corporate logo, recognisable company name,
American flag on buildings that do not have one, other nation's flag, smooth
surfaces, curved walls, sculpted detail, sub-block detail, carved ornament,
photorealism, stylized voxel art, smooth gradients, high resolution textures,
rounded topiary tree, horse next to a modern tram, HUD, crosshair, hotbar,
user interface, watermark, signature, blurry, fisheye, distorted perspective,
tilted horizon, changed art style, split screen, collage, border
```

---

## БЛОК КАМЕРЫ — один на все 60 кадров

### CAMERA A — кадры 1–60
```
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
```

---

## MOTION LOCK — на случай одиночного оживления кадра

```
Static locked-off camera on a tripod. Absolutely no camera movement: no zoom, no
pan, no tilt, no dolly, no orbit, no parallax, no shake. The framing is identical
in the first and the last frame. All architecture holds its exact shape - nothing
morphs, melts, grows or disappears. Motion is slow, subtle and ambient only.
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
```

#### NOTE 1
Вход: ничего. Единственный кадр с нуля (text-to-image). Это мастер-плита всего
ролика — от неё зависят 59 остальных. Сгенерить 10–20 вариантов и выбирать
придирчиво: важно, чтобы сходящиеся улицы и треугольник в центре встали ровно
так, как описано в камере, иначе поплывёт весь ролик.

---

# ПРОЛОГ

### 1 · 1800 · Woodland — **4 секунды** — МАСТЕР-ПЛИТА
Единственный кадр с нуля: `STYLE + CAMERA A + сцена ниже`.
**SCENE:** `Open countryside with no town of any kind. A rutted dirt road runs away from the camera and forks around a low wedge of rough grass and scrub dead centre of the frame, where a second track joins it. Scattered oaks and a small stream crossing the near ground. Split-rail fences, tall grass, a few grazing cows in the distance. Low wooded hills on the horizon. Bright clear morning, rich greens, nothing built anywhere.`
**MOTION:** `Grass and tree canopies sway. The stream flows. Cows shift in the far field. A bird crosses. Nothing else moves.`

### 2 · 1840 · The Farm
**EDIT:** `Add a working farm: a two-storey timber farmhouse with a shingled roof on the left side of the frame, a large red barn behind it, split-rail paddocks with horses, a well with a bucket, and ploughed strips beyond. The dirt road is wider and rutted with cart tracks. The central wedge of ground is still empty scrub.`
**TRANS:** `The farmhouse, the barn and the fences build themselves up out of the ground block by block, course by course, while the road widens and the ploughed strips appear as whole blocks of dark earth.`
**MOTION:** `Horses shift in the paddock. Smoke from the farmhouse chimney. Grass sways. A cart on the road.`

### 3 · 1860 · The Grid Arrives
**EDIT:** `The farm is gone. The land has been levelled and surveyed into a city grid: two wide graded dirt avenues now converge on the central wedge, marked out with wooden survey stakes and rope lines. Stacks of paving stone and timber at the roadside, a surveyor's tripod, a few labourers. Bare earth everywhere, no buildings yet, telegraph poles along one side.`
**TRANS:** `The farm buildings vanish as whole blocks lifting away. The ground flattens into a level surface of packed earth, then the two avenues appear as broad strips of graded dirt and the survey stakes pop into place along their edges.`
**MOTION:** `Dust drifts across the bare earth. Labourers work at the stakes. Telegraph wires sway. A cart crosses.`

### 4 · 1872 · Longacre Square
**EDIT:** `A carriage district has grown up: low three-storey brick buildings line both avenues, with carriage-works, stables and blacksmith shops at street level. Painted wooden trade signs above the doors carrying invented short words only. Hay wagons, horse troughs, piles of harness. Gas lamps on iron posts. The central wedge holds a small two-storey brick building with a flat roof. Cobbled roadways.`
**TRANS:** `Brick buildings rise along both avenues block by block from the ground up, the cobbles fill in across the dirt as whole blocks, and the gas lamps and painted signs appear last.`
**MOTION:** `Horses at the troughs. A hay wagon rolls past. Smoke from a forge. Gas lamps flickering. Sign boards swaying.`

---

# КАРЕТНАЯ ЭПОХА

### 5 · 1880 · Horsecars
**EDIT:** `Add a tram line down each avenue: steel rails set flush into the cobbles, with an open four-wheeled tram car running on them, pulled by two horses in harness walking between the rails. No engine, no overhead wires, no poles or cables above. A small wooden waiting shelter at the kerb. More people on the pavement, more painted trade signs.`
**MOTION:** `The two horses walk forward, drawing the tram car along the rails. Passengers on the open platform. Pedestrians crossing.`

### 6 · 1888 · The Carriage Trade
**EDIT:** `The district is at its busiest: long rows of finished carriages parked at the kerb, wide-open workshop doors showing wheels and frames inside, a five-storey brick carriage works on the left corner with big arched windows. Overhead a dense web of telegraph and telephone wires on tall poles crossing the avenues.`
**MOTION:** `Wires sway overhead. A carriage is wheeled out of a workshop. Horses stamp. Crowds on the pavements.`

### 7 · 1895 · The First Theatre
**EDIT:** `A large theatre appears on the left side: an ornate brick and stone facade four storeys tall with a wide canopy over the pavement and a row of tall arc lamps on brackets above it, throwing hard white light. The first electric sign in the frame sits above the canopy - a rectangle of glowing blocks with an invented short word on it. Evening light, the rest of the street still on gas.`
**TRANS:** `The old low buildings on the left lift away as whole blocks and the theatre builds up in their place course by course, its canopy last. The arc lamps and the lit sign switch on together at the end.`
**MOTION:** `Arc lamps flicker and buzz. The lit sign glows steadily. A queue forms under the canopy. Carriages pulling up.`

### 8 · 1899 · The Hotel on the Triangle
**EDIT:** `Replace the small brick building on the central wedge with a tall narrow hotel filling the whole triangle: nine storeys of dark brick with a steep mansard roof, bay windows and a corner entrance at its sharp point. It is now the tallest thing in the frame. Two more theatres along the avenues, more electric signs.`
**TRANS:** `The small building on the wedge vanishes block by block and the tall hotel rises in its place from the ground upward, storey by storey, the mansard roof going on last.`
**MOTION:** `Guests at the corner entrance. Carriages waiting. Lit signs glowing. Wires swaying.`

### 9 · 1903 · Digging
**EDIT:** `The hotel is gone. The central wedge is a deep excavation pit with stepped rock sides, timber hoardings around it, two tall wooden cranes, stacks of steel beams and a spoil chute. The avenues on both sides are torn open in long trenches for a subway, with timber shoring and plank walkways over them. Mud everywhere.`
**TRANS:** `The hotel comes down as whole blocks collapsing inward into a heap, then the heap clears away and the pit is dug out downward, layer by layer, the cranes and hoardings appearing around it at the end.`
**MOTION:** `A crane lifts a steel beam. Workers in the pit. Spoil carts on rails. Dust rising. Planks bouncing under foot traffic.`

---

# ЭПОХА БАШНИ

### 10 · 1904 · The Tower
**EDIT:** `On the wedge stands a new tower: narrow, about 10 blocks wide at its point and 26 blocks tall, faced in pale stone, with tall arched windows, a stepped cornice and a small ornamental turret on top. It is by far the tallest thing in the frame and must appear in every following image. The trenches are filled and the avenues repaved. Crowds below.`
**TRANS:** `The tower rises out of the pit course by course, from the foundations up to the turret, while the trenches in the avenues fill in as whole blocks of paving from both ends toward the centre.`
**MOTION:** `Crowds on the pavements looking up. Carriages and an early motor car. Flags of bunting on the tower base moving.`

### 11 · 1905 · The Subway
**EDIT:** `Add a cast-iron and glass subway entrance kiosk with a domed roof at the kerb in front of the tower, with steps leading down and an ornate railing. Newsstands on the corners. More pedestrians, a queue at the kiosk.`
**MOTION:** `People descending and emerging from the kiosk steps. Newsstand vendor moving. Traffic passing.`

### 12 · 1907 · The First Ball
**EDIT:** `Night. A dense crowd fills both avenues from edge to edge, tens of thousands of small figures. A glowing ball of lit blocks sits at the top of the tower's turret. Every window in the frame is lit. Confetti in the air. The lit signs are bright against a black sky.`
**MOTION:** `The glowing ball descends slowly down the turret. The crowd surges and waves. Confetti falling. Lights flickering.`

### 13 · 1910 · Electric Signs
**EDIT:** `Daytime. Large illuminated signs now cover the upper facades on both sides: rectangles of glowing blocks bordered by rows of small bright bulbs, each carrying an invented short word or an abstract silhouette. No real brands anywhere. Overhead trolley wires on catenary poles, an electric tram with a pantograph on the rails, the horses gone completely.`
**TRANS:** `The horse tram and its horses vanish as whole blocks, the catenary poles rise along the kerbs and the wires string between them, then the electric tram rolls in. The signs light up one after another across both facades.`
**MOTION:** `The electric tram glides along the rails. Bulb borders chase around the sign edges. Crowds. Wires swaying.`

### 14 · 1913 · Automobiles
**EDIT:** `The street is full of early motor cars with high bodies and spoked wheels, mixed with a few remaining horse carriages. A traffic policeman on a small stand in the road. Larger signs, more of them, and the first sign with moving light patterns.`
**MOTION:** `Cars and carriages crossing. The policeman signalling. Bulb patterns chasing on the big sign. Crowds.`

### 15 · 1917 · Wartime
**EDIT:** `Mobilisation: a column of soldiers in uniform marching down one avenue, a wooden recruiting booth on the pavement, crowds waving. One flag hangs from the tower with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its upper corner; no other nation's flag appears anywhere. Printed notices on boards carrying no readable words, only blocks of colour.`
**MOTION:** `The column marches. The striped flag lifts on the tower. Crowds waving hats. Notices flapping.`

### 16 · 1920 · Prohibition
**EDIT:** `Peacetime and prosperous: the soldiers gone, more cars, women in shorter coats, a policeman at the kerb. Signs are bigger and there are more of them, with the first animated sign showing a simple silhouette figure in motion. Basement stairways with plain unmarked doors under two buildings.`
**MOTION:** `Traffic flows. The animated sign cycles its silhouette. Crowds. Cigarette smoke from a doorway.`

### 17 · 1923 · The Great White Way
**EDIT:** `Night, and the whole frame is lit by signs: every upper facade on both sides is covered in glowing rectangles outlined by bulbs, so bright that there are no dark surfaces left anywhere. Theatre canopies below, all lit. The tower carries a large sign of its own. Dense evening crowd, cars nose to tail.`
**MOTION:** `Hundreds of bulbs chasing around the sign borders. The animated silhouettes cycling. Traffic crawling. Dense crowd flowing.`

### 18 · 1925 · Peak Bulbs
**EDIT:** `Even more: signs now stacked three high on some buildings and projecting out over the roadway on steel frames. A huge animated sign on the right shows a silhouette pouring from a jug, cycling in steps. Theatre marquees with rows of bulbs around them.`
**MOTION:** `The pouring silhouette cycles. Marquee bulbs chasing. Traffic and dense crowds. Everything moving.`

### 19 · 1928 · The Zipper
**EDIT:** `Add a continuous band of small lit blocks running all the way around the tower at the fourth-storey level, forming a moving news ribbon. It carries no readable words, only a running pattern of lit and unlit blocks. A crowd stands in the street below looking up at it.`
**TRANS:** `The lit band appears around the tower one block at a time, running all the way around it, and then begins to move.`
**MOTION:** `The pattern of lit blocks runs steadily around the tower. The crowd below watches, heads turned up. Traffic passing.`

### 20 · 1929 · The Crash
**EDIT:** `A large crowd packed in the street below the tower, all facing up at the news ribbon, still and silent rather than celebrating. Men in hats holding newspapers. Grey overcast day, the signs unlit in daylight, a heavy quiet mood.`
**MOTION:** `The news ribbon runs around the tower. The crowd stands almost motionless, faces up. A newspaper page blows across the road.`

---

# ДЕПРЕССИЯ И ВОЙНА

### 21 · 1931 · Burlesque
**EDIT:** `The street is shabbier: several shopfronts boarded, paint peeling on the signs, a soup queue along one pavement. Two theatre marquees have been converted, with cheap hand-painted boards and rows of bare bulbs, showing invented short words only. Fewer cars, more people standing about.`
**MOTION:** `The soup queue shuffles. Bare bulbs flickering unevenly. Loose boards knocking. Fewer vehicles passing.`

### 22 · 1934 · Grind Houses
**EDIT:** `Most theatres have become cheap cinemas: wide flat marquees with dense rows of bulbs and stacked boards, ticket booths on the pavement, posters in frames carrying only blocks of colour. A hot-dog cart. The upper signs are patchier, some dark.`
**MOTION:** `Marquee bulbs chasing unevenly, some burnt out. Queue at a ticket booth. Cart vendor working. Traffic.`

### 23 · 1937 · Swing
**EDIT:** `Livelier again: a dance hall on the left with a big lit sign, a queue of young people in coats and hats, more cars, cleaner pavements. Several dark signs relit. Night, warm bulb glow.`
**MOTION:** `Queue moving into the dance hall. Bulbs chasing. Cars pulling in. Crowd on the pavement.`

### 24 · 1939 · The Fair Year
**EDIT:** `Bright and confident: every sign lit and repainted, a new streamlined sign with rounded corners and horizontal lines, cleaner modern cars, flagpoles along the kerb each flying a flag with thirteen alternating red and white horizontal stripes and a blue rectangle of white stars in its corner. No other nation's flag anywhere.`
**MOTION:** `Rows of striped flags moving together. Bulbs chasing. Heavy traffic. Dense cheerful crowd.`

### 25 · 1942 · The Dimout
**EDIT:** `Every sign in the frame is DARK. Not one lit rectangle, not one glowing bulb anywhere. The street is lit only by weak hooded lamps with narrow slits and by car headlights masked down to thin strips. Windows blacked out. The tower is a black silhouette against a dark blue sky. A few uniformed figures on the pavement. The emptiest and darkest frame of the series.`
**TRANS:** `The signs go out in waves across the frame, section by section, until nothing is lit at all, and the hooded lamps come on as the last thing.`
**MOTION:** `Thin masked headlights crawling. One hooded lamp swaying. Very few figures moving. Deep stillness.`

### 26 · 1944 · Wartime Crowd
**EDIT:** `Still dark overhead, but the street is busy: servicemen and women in uniform on the pavements, a canteen booth at the kerb, a war bond stand. The signs remain unlit. One large flag with thirteen stripes and a blue corner of stars hangs from the tower, floodlit by a single lamp. No other flags.`
**MOTION:** `The flag lifts in the lit beam. Crowds of uniformed figures moving. The canteen queue shuffling.`

### 27 · 1945 · The Lights Come Back
**EDIT:** `Night, and every sign in the frame is blazing again, brighter than before. An enormous crowd fills both avenues completely, hats in the air, confetti and paper falling from the upper windows. The tower's news ribbon is running. The single most crowded frame of the series.`
**TRANS:** `The signs come back on in a wave that spreads outward across the whole frame, one board after another, and as the last one lights the crowd floods into the street from both sides.`
**MOTION:** `Every bulb border chasing at once. Paper and confetti pouring down. The crowd surging and cheering. The ribbon running.`

### 28 · 1947 · Postwar
**EDIT:** `Daylight, prosperous and busy: new cars with rounded bodies, clean pavements, repainted signs, a new sign with a smoking silhouette that puffs rings. Shop windows full. A traffic light on a pole replaces the policeman's stand.`
**MOTION:** `The smoking silhouette puffs a ring every few seconds. Traffic flows and stops at the light. Busy pavements.`

---

# ПОСЛЕВОЕННЫЙ ПИК

### 29 · 1950 · Neon
**EDIT:** `Neon replaces bulbs on most signs: glowing coloured tubes bent into shapes and invented short words, in reds, blues and greens, layered over the older bulb boards. Richer, more saturated night light than before.`
**TRANS:** `Bulb boards go dark one by one and neon tubes light up in their place, colour by colour, until the whole frame is neon.`
**MOTION:** `Neon tubes flickering on and off in sequence. The smoking silhouette puffing. Traffic. Crowds.`

### 30 · 1953 · Bigger Boards
**EDIT:** `The signs grow to cover entire building faces, projecting out on steel frames over the pavement. An animated waterfall of lit blocks pours down one facade. More neon colours, denser stacking.`
**MOTION:** `The waterfall of lit blocks pours continuously. Neon flickering. Dense traffic. Crowds.`

### 31 · 1956 · Cinemascope
**EDIT:** `Cinema marquees widened and modernised, with sweeping horizontal fins and big block letters of invented short words. Long finned cars in bright two-tone colours at the kerb. A crowd queueing along the block.`
**MOTION:** `Marquee bulbs chasing. Finned cars cruising past. Long queue shuffling. Neon glow.`

### 32 · 1959 · Chrome
**EDIT:** `Peak of the era: the widest cars, the brightest neon, every facade covered, a new sign with a rotating silhouette. Pavements crowded with people in bright clothes. Warm dense night.`
**MOTION:** `The rotating silhouette turns steadily. Neon and bulbs both running. Heavy cruising traffic. Dense crowd.`

### 33 · 1962 · Stripped
**EDIT:** `The tower is being reclad: its stone facade is gone, stripped back to a bare structural frame of dark columns and beams with the floors visible between them, wrapped in scaffolding and safety netting. A crane beside it. The signs around it are unchanged and still lit, which makes the bare frame look stranger.`
**TRANS:** `The tower's stone facade comes away in whole blocks from the top down, storey by storey, leaving the dark frame standing, and the scaffolding rises around it as it goes.`
**MOTION:** `Safety netting billowing. A crane arm swinging slowly. Sparks from a cutting torch. Neon running around it.`

### 34 · 1964 · White Marble
**EDIT:** `The tower is reclad: a smooth flat skin of white panels covering it from top to bottom, with narrow slit windows, no cornice and no turret. It is now a plain white slab and looks nothing like the ornate stone tower it was, though it stands in exactly the same footprint and is exactly the same height.`
**TRANS:** `White panels go up over the dark frame course by course from the bottom upward, and the scaffolding comes away in sections as they pass.`
**MOTION:** `The last scaffold section lifting away. Neon around it. Traffic. Crowds.`

---

# УПАДОК

### 35 · 1967 · Fraying
**EDIT:** `The first signs of decline: two dark unlit boards, a boarded shopfront, litter at the kerb, cracked pavement. The neon that still works looks tired. Fewer well-dressed people, more standing about.`
**MOTION:** `Litter blowing. One neon tube flickering badly. Sparse traffic. Figures loitering.`

### 36 · 1970 · Grind
**EDIT:** `Cinema marquees now carry crude hand-lettered boards with invented short words and blocks of colour, several with bare unshaded bulbs. More boarded windows, a pawnbroker with barred glass, graffiti at street level. Grimy, cluttered.`
**MOTION:** `Bare bulbs flickering. Litter drifting. A few figures under the marquees. Thin traffic.`

### 37 · 1973 · The Low Point
**EDIT:** `Heavy decay: half the upper signs dark or broken with missing blocks, boarded and graffitied shopfronts along both sides, rubbish piled at the kerb, a burnt-out car, weeds in the pavement cracks. The white tower is streaked and stained. Overcast grey day, drained colours.`
**MOTION:** `Rubbish blowing along the gutter. A broken sign sparking intermittently. Almost no traffic. Few figures.`

### 38 · 1977 · Blackout Summer
**EDIT:** `Night with every sign and window dark, the street lit only by car headlights and a few torch beams. Not a blackout of war but of failure: broken shopfronts, scattered goods on the pavement, figures moving in the dark. Hot summer haze.`
**TRANS:** `The signs and the street lamps all cut out at once across the whole frame, leaving only headlights, and the scene goes dark in a single moment rather than gradually.`
**MOTION:** `Headlight beams sweeping. Torch beams moving. Figures crossing in the dark. Nothing lit above street level.`

### 39 · 1980 · Bottom
**EDIT:** `Daylight on the worst of it: boarded frontages the full length of both sides, dense graffiti to first-floor height, a vacant lot behind a chain fence where a building was demolished, rubbish, cracked road. Only three signs still lit. The tower stained grey.`
**MOTION:** `Rubbish blowing across the vacant lot. Chain fence rattling. A bus passing. Few pedestrians.`

### 40 · 1984 · Hoardings
**EDIT:** `Redevelopment begins: tall painted hoardings enclose two blocks, with printed boards showing abstract colour blocks only. A demolition crane behind one hoarding. The rest of the street is unchanged and still shabby.`
**MOTION:** `The crane swings behind the hoarding. Dust rising. Hoarding boards flapping at a corner. Traffic.`

### 41 · 1988 · Demolition
**EDIT:** `A whole block on the right is coming down: the buildings half demolished with floors open to the air, a wrecking machine, dust clouds, and a great gap of open sky where they stood. The signs that were on them are gone completely.`
**TRANS:** `The buildings on the right collapse as whole blocks falling inward, floor by floor, and a dust cloud rolls up as the sky opens behind them.`
**MOTION:** `Dust rolling up from the demolition. The machine working. Blocks tumbling. Onlookers at a fence.`

### 42 · 1991 · Empty Lots
**EDIT:** `Two cleared lots behind chain fencing, used as flat parking with painted bays. The remaining buildings are shabby but tidier, some hoardings repainted. Fewer boarded fronts than before but the street feels thin and gap-toothed. Cold light.`
**MOTION:** `Cars pulling into the lot bays. Chain fence rattling. Thin pedestrian traffic. Paper blowing.`

---

# ВОЗРОЖДЕНИЕ

### 43 · 1994 · Cleanup
**EDIT:** `Visible repair: new street lamps, fresh paving, planters, a police post at the corner, scaffolding on two restored theatre facades with their marquees being rebuilt. Graffiti painted out. A handful of bright new signs among the old.`
**MOTION:** `Workers on a marquee scaffold. New lamps lit. More pedestrians. Traffic flowing properly.`

### 44 · 1997 · The Theatres Return
**EDIT:** `Restored theatre fronts on the left with new lit marquees in period style, a queue of families, souvenir stands, clean pavements. The cleared lots on the right now hold construction cores with tower cranes above them.`
**MOTION:** `Tower cranes turning. Marquee bulbs chasing. Family crowds queueing. Busy traffic.`

### 45 · 1999 · Screens On The Tower
**EDIT:** `The tower's white panels are hidden: large flat display boards of lit coloured blocks now cover its whole front from the fourth storey to the roof, carrying invented short words and abstract patterns. Its shape is unchanged underneath, but the building itself is no longer visible as a building.`
**TRANS:** `Display boards go up over the white tower panel by panel from the bottom upward, each one lighting as it locks into place, until the white skin is completely hidden.`
**MOTION:** `Patterns cycling across the tower boards. Marquees chasing. Dense evening crowd. Traffic.`

### 46 · 2001 · Millennium Bright
**EDIT:** `New glass towers now fill the sky gap on the right, their lower floors wrapped in lit display boards. Every facade in the frame carries screens or signs. Clean, safe, busy, brightly lit day and night. Tour buses at the kerb.`
**MOTION:** `Boards cycling patterns everywhere. Tour buses pulling in. Heavy pedestrian crowds. Steady traffic.`

### 47 · 2004 · Full Colour
**EDIT:** `The displays are bigger and smoother, covering entire building faces edge to edge with moving blocks of colour. Neon has almost vanished. A giant wraparound board turns the corner of one building. Night, the whole frame lit by screens alone.`
**MOTION:** `Colour fields sweeping across the giant boards. The wraparound cycling around the corner. Dense night crowd.`

### 48 · 2007 · The Canyon
**EDIT:** `Screens now run from street level to rooftop on both sides with no gaps, so the street is a canyon of light. Pavements packed with tourists, costumed street performers, ticket booths. Yellow taxis nose to tail.`
**MOTION:** `Screens cycling on every surface. Taxis crawling. Performers moving on the pavement. Very dense crowd.`

### 49 · 2009 · Chairs In The Road
**EDIT:** `The roadway in front of the wedge has been closed to traffic: rows of simple folding chairs and small tables stand directly on the asphalt where cars used to drive, with planters and bollards marking the edge. People sitting in the middle of what was a street. Taxis now stop at the new boundary.`
**TRANS:** `The taxis clear out of the central roadway, bollards and planters drop into place along a new line, and then chairs and tables appear across the empty asphalt in rows.`
**MOTION:** `People settling into the chairs. Taxis queueing at the new boundary. Screens cycling. Pigeons on the asphalt.`

### 50 · 2012 · The Plazas
**EDIT:** `The temporary chairs are gone, replaced by a permanent stone plaza: pale granite paving across the whole central roadway, long fixed benches, low steel bollards, planting beds and a raised platform of wide steps. Cleaner and more deliberate.`
**TRANS:** `The chairs lift away, the asphalt is replaced by pale granite paving spreading outward block by block, and the benches, bollards and steps rise out of it.`
**MOTION:** `Crowds flowing across the plaza. People on the steps and benches. Screens cycling. Buses beyond the bollards.`

---

# СОВРЕМЕННОСТЬ

### 51 · 2016 · Wraparound
**EDIT:** `The largest display yet: a single enormous board running the entire height and width of one building face and turning both corners. Screens on every other surface, brighter and more saturated. Dense tourist crowd at all hours, selfie sticks, costumed performers.`
**MOTION:** `A single image sweeping across the giant wraparound board. Every other screen cycling. Packed crowd.`

### 52 · 2019 · Peak Crowd
**EDIT:** `The busiest daytime frame: the plaza and both pavements completely packed with people, tour groups with flags on poles, food carts, pedicabs decorated with lights, queues at every booth. Screens at full brightness even in daylight.`
**MOTION:** `Dense crowd flowing in all directions. Pedicabs threading through. Tour flags bobbing. Screens cycling.`

### 53 · 2020 · Empty
**EDIT:** `The same place with almost nobody in it: the plaza bare, chairs and carts gone, shutters down on the shops, theatre marquees dark and blank. But every giant screen is still running at full brightness above the empty street. Two masked figures far apart. Flat grey daylight. The strangest frame of the series.`
**TRANS:** `The crowd thins out and disappears as figures walk out of frame in every direction, the carts and chairs lift away, the shutters roll down, and the marquees go dark - while the big screens above keep cycling unchanged.`
**MOTION:** `Screens cycling brightly over an empty street. A single figure crossing far away. Paper blowing across the plaza. Very still.`

### 54 · 2022 · Coming Back
**EDIT:** `People are back in numbers though not yet packed: reopened marquees lit again, food carts returned, outdoor seating, plenty of tourists but room to walk. A few masks. Bright normal day.`
**MOTION:** `Moderate crowd flowing. Carts serving. Marquees chasing. Taxis at the boundary.`

### 55 · 2024 · Normal
**EDIT:** `Fully recovered and slightly greener: new planters with small trees along the plaza, more benches, cycle racks, a bike lane marked at the edge. Screens denser than ever. Big crowd, relaxed.`
**MOTION:** `Crowd flowing. Cyclists in the lane. Small trees swaying. Screens cycling everywhere.`

### 56 · 2026 · Present Day
**EDIT:** `The square today, at its brightest: screens covering every available surface from pavement to roofline including all four faces of the wedge tower, a packed relaxed crowd, mature planters, food carts, performers, yellow taxis beyond the bollards. Warm late-afternoon light behind the towers, long shadows down the avenues.`
**MOTION:** `Every screen cycling. Dense crowd flowing across the plaza. Taxis crawling. Performers working. Pigeons lifting.`

---

# БУДУЩЕЕ

### 57 · 2040 · Layers of Light
**EDIT:** `Near future: the flat screens are joined by free-standing holographic figures three storeys tall standing in the air above the plaza, translucent and made of glowing blocks. Driverless pods glide silently on a marked lane. Vertical gardens climb two facades. The crowd carries no phones, wearing thin visors instead.`
**MOTION:** `Holographic figures turning slowly in the air. Pods gliding silently. Garden foliage swaying. Crowd flowing.`

### 58 · 2055 · The Green Canyon
**EDIT:** `Plants have taken over the architecture: every facade carries dense planting between the screens, trees grow from terraces at four levels, water runs in channels through the plaza paving. The screens are dimmer and fewer, the light softer and greener. Fewer people, more slowly moving.`
**MOTION:** `Foliage swaying at every level. Water running in the channels. A few pods gliding. Calm, unhurried crowd.`

### 59 · 2070 · The Screens Go Dark
**EDIT:** `Every screen in the frame is dead: blank grey rectangles covering the buildings, with cracked and missing panels on several. The planting has run wild and hangs untrimmed over the facades. No pods, no crowd, a handful of figures. Low mist. The wedge tower stands blank and grey.`
**TRANS:** `The screens go out one after another across the frame, section by section, until every surface is a dead grey rectangle, and the crowd walks out of frame as they go.`
**MOTION:** `Mist drifting between the buildings. Overgrown branches swaying heavily. One panel hanging loose and swinging. A single figure crossing.`

### 60 · 2075 · The Last Frame
**EDIT:** `Long abandoned: the plaza cracked apart with trees growing through it, the roadways gone to grass, vines covering the lower storeys, dead screens hanging in broken sheets from the facades. One screen on the wedge tower still flickers faintly with a pattern. Rain falling, dark blue-grey palette, cold light from that one flickering panel.`
**MOTION:** `Rain falling steadily. The one surviving panel flickering. Vines and branches swaying. Water running through the cracked paving. A bird crosses. Then stillness - the final frame, cut to black from here.`
