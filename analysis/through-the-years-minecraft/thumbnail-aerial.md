# Превью, формат 2: аэросъёмка со стрелкой лет

Разбор трёх референсов (Los Angeles 1781, Chicago 1673, Manhattan 1624) и промпт под Варшаву в майнкрафт-стиле.

---

## 1. Формула

| Элемент | Как сделано |
|---|---|
| Композиция | **один кадр, никакого сплита и разделителя** |
| Ракурс | высокая аэросъёмка с наклоном 30–45°, широкий ландшафт до горизонта |
| Что показано | **только ранний год** |
| Плашка | жёлтый прямоугольник по центру сверху, название города чёрным капсом |
| Шрифт плашки | тяжёлая антиква (у Чикаго гротеск — 2 из 3 всё же антиква) |
| Низ | `1781 ——▶ 2026`: белые цифры с чёрной обводкой, длинная стрелка между ними |
| Чего нет | сплита, флага, лиц, рамок, любого намёка на современность |

### Чем этот формат отличается от сплита

Сплит показывает «до и после» сразу. Этот **прячет вторую половину**: в кадре только болото на месте Чикаго или поля на месте Лос-Анджелеса, а 2026 существует лишь как обещание в подписи. Зритель кликает, чтобы увидеть развязку.

Отсюда следствие для картинки: **ранний кадр должен быть максимально «пустым» и при этом узнаваемым по географии**. Чикаго узнаётся по излучине реки у озера, Манхэттен — по форме острова. Работает контраст между тем, что зритель знает о городе сегодня, и тем, что он видит.

Для Варшавы такой опознавательный знак — **излучина Вислы и обрыв скарпы**.

---

## 2. Какие годы

Конкуренты берут год основания: LA 1781, Chicago 1673, Manhattan 1624.

| Вариант | Подпись | Ставка |
|---|---|---|
| **A** (основной) | `1300 ⟶ 2026` | точное попадание в конвенцию: 1300 — основание Варшавы, кадр 15 нашей сетки |
| **B** (A/B) | `1300 ⟶ 2075` | обещает будущее, которого нет ни у одного конкурента |

B честнее по отношению к ролику: у нас последние два кадра именно про будущее. Но 2075 может читаться как фантастика и отпугнуть часть аудитории — поэтому в тест, а не сразу.

---

## 3. Промпт картинки

Один кадр. Ни букв, ни плашки, ни стрелки — всё накладывается скриптом.

```
Minecraft-style voxel world. Every object is built from uniform 1-meter cubic
blocks with 16x16 pixel-art textures. Hard-edged blocky geometry, visible grid
seams on every face. No smooth curves, no rounded shapes, no organic silhouettes,
no bevels. Rendered as a game screenshot through a modern shader pack: volumetric
god rays, soft contact shadows, gentle bloom, crisp saturated colours, smooth sky
gradient, light atmospheric haze on the far background. No HUD, no crosshair, no
hotbar, no interface, no hands, no held items.

CAMERA: high aerial view from a drone, looking down at roughly 40 degrees, wide
landscape reaching to a distant horizon. The horizon sits at about 20% of frame
height, so most of the frame is land seen from above. 24mm equivalent wide angle,
level horizon, no fisheye. 16:9.

SCENE: the site of a European capital in the year 1300, long before the city
existed. A wide river winds through the middle of the frame from the top to the
bottom right, with one large distinctive bend curving toward the viewer. Along
its west bank rises a long wooded escarpment - a steep bluff separating the low
water meadows from the flat plateau above.

On the crest of that bluff stands ONE small town: about forty timber houses with
red tile roofs laid out on a rectangular grid, a small open market square in the
middle, and a wooden palisade with a single gate tower around it. Below the bluff,
a timber bridge on piles crosses the river. A few strips of ploughed field and
pasture around the town, a water mill on the near bank.

EVERYTHING ELSE IS WILDERNESS: dense dark forest covering the whole plateau and
the far hills, marshy meadows along the water, no roads except two dirt tracks,
no other settlements anywhere, absolutely nothing modern.

Bright clear late-summer morning, low warm sun from the left casting long
shadows, deep blue sky with blocky white clouds, rich greens.

NO text, NO letters, NO numbers, NO banner, NO arrow, NO watermark, NO logo,
NO split screen, NO collage, NO border.

COMPOSITION: keep the top 20% of the frame and the bottom 15% relatively calm -
sky above, open meadow below - because a banner and a caption go there. The town
sits slightly right of centre, the river bend slightly left.
```

**Негатив:**
```
smooth surfaces, rounded edges, realistic geometry, photorealism, low-poly
non-cubic shapes, HUD, crosshair, hotbar, user interface, text, letters, numbers,
watermark, signature, logo, banner, arrow, split screen, collage, border, frame,
modern buildings, skyscrapers, cars, roads, power lines, blurry, fisheye,
tilted horizon
```

Требование про спокойные верхние 20% и нижние 15% — не украшательство: туда лягут плашка и строка лет, и если там окажется лес или город, текст утонет.

---

## 4. Наложение

```bash
python3 tools/miniatura_aerial.py IN.png OUT.png WARSAW 1300 2026
```

Скрипт делает: вписывает кадр в 1280×720, рисует жёлтую плашку по центру сверху (ширина подгоняется под текст), внизу строку `год ——▶ год` белым с чёрной обводкой.

Ключи `--bar-font` и `--year-font` — если положишь настоящую антикву в `fonts/`. Сейчас берётся Liberation Serif Bold: у референсов начертание тяжелее, ближе Playfair Display Black или Merriweather Black.

---

## 5. Чек-лист

- [ ] В кадре нет ни одной сгенерированной буквы
- [ ] Нет ничего современного: ни дорог, ни проводов, ни зданий выше трёх этажей
- [ ] Излучина реки и обрыв читаются — это опознавательный знак места
- [ ] Верх и низ кадра спокойные, текст не тонет
- [ ] Превью читается в размере 210×118 px
- [ ] Жёлтая плашка не перекрывает город и излучину
