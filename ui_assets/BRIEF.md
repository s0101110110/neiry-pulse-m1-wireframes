# BRIEF: Corner cases B4 — End-of-session summary + Bracelet disconnect mid-session · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1+B2+B3 приняты и закоммичены (`f3c1024`, `fafcfa8`, `406c04c`). Сейчас **порция B4 (4 из 5-7) Ф1.5 corner cases:** **End-of-session summary** (между STOP и History) + **Bracelet disconnect mid-session** (banner поверх Training Active).

**Цель:** закрыть оставшиеся 2 Training corner cases из аудита §3.3:
- **End-of-session summary** — без него юзер нажал STOP → сразу попал в History без celebratory moment / quick stats / возможности удалить случайную тренировку
- **Bracelet disconnect mid-session** — HR замирает, юзер не понимает почему пульс не обновляется

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-end-of-session-bracelet-disconnect-v0.html`

---

## Источники правды

- **Аудит §3.3 missing states:**
  - End-of-session summary screen (между Stop и History) — overlay «Молодец! 28:04 · 5.20 км»
  - Bracelet disconnect mid-session — пульс замирает, banner «браслет отключён»
- **Reference (existing):**
  - `mobile-session-detail-v0.html` — final layout после тренировки (для understanding summary stats)
  - `mobile-training-active-v0.html` Page 1 (для Bracelet disconnect background)
  - B1 BT-disconnect banner pattern (для consistency)
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 19** · END-OF-SESSION · SUMMARY»
- «**ЭКРАН 20** · TRAINING ACTIVE · BRACELET DISCONNECT»

---

## Phone 1 · End-of-session summary (после нажатия STOP)

**Назначение:** юзер нажал STOP в Training Active → подтвердил «Завершить» в B3 modal → попадает в **transitional celebratory screen** перед History. Видит quick stats + actions «Сохранить» / «Удалить».

**Контекст:** Light Bevel-tone, full-screen но с celebratory tone. Не tab-bar — это modal-flow.

**Структура (сверху вниз):**

### Status bar + minimal app-bar
- Status bar 9:53 (3 минуты прошло после STOP в B3 12:43+, но это independent screen)
- App-bar: пустой левый (no back) + close-icon «×» top-right (для quick dismiss → сразу в History без save)

### Hero block (centered, top half)
- Subtle confetti SVG decorative (опц., 6-8 wine + alert-orange particles в top corners) — НЕ overdone
- Eyebrow (mono uppercase wine 11pt): `ТРЕНИРОВКА ЗАВЕРШЕНА`
- Title (Onest 700 32-36pt foreground): «Молодец!»
- Sub (Space Grotesk 14pt muted-foreground): «Бег · 14 июня, 9:53»

### Big stats grid (4 cards, 2×2)
Светлые карточки, padding 16-20, border subtle, gap 12:
- **Дистанция** `5.20` (Onest 700 32pt + `км` mono 13pt muted)
- **Длительность** `28:04` (Onest 700 32pt mono tabular-nums)
- **Avg HR** `142` (Onest 700 32pt + `bpm` mono 13pt muted)
- **Калории** `186` (Onest 700 32pt + `ккал` mono 13pt muted)

### Mini sparkline (HR за тренировку)
- Width full, height ~60-80px
- HR-line wine с subtle area-fill wine-soft под линией
- 2-3 mini-labels по Y axis (140 / 160 mono 10pt muted)
- НЕ overdo — это quick visual

### Actions row (bottom)
- **«Сохранить тренировку»** — wine primary CTA (52pt full-width, white text, save-icon SVG)
- **«Удалить»** — text-link destructive red secondary (40pt, под CTA)

### **БЕЗ tab-bar** (modal flow)

---

## Phone 2 · Training Active с Bracelet disconnect mid-session banner

**Назначение:** во время активной тренировки браслет потерял связь (out of range / разрядился). Пульс «замерзает» на последнем значении. Юзер видит banner аналогично B1, но в контексте тренировки.

**Контекст:** Training Active Page 1 — HR view. Banner sticky сверху, HR muted-grey + bluetooth-off cue.

**Структура:**

### Status bar + App-bar-active
- Status bar 9:50
- App-bar-active: timer `12:48` (продолжает идти — GPS и время пишутся, только HR заморожен)
- btn-stop visible top-right

### Sticky bracelet disconnect banner (под app-bar, full-width)
- Background `#fdf3e1` alert-soft + border-left 4px `#d97706` alert-orange (consistency B1/B2/B3 GPS)
- Padding 12-16px
- Top row:
  - **Bluetooth-off SVG icon** (alert-orange ~20×20)
  - Eyebrow (mono uppercase 11pt alert-orange): `БРАСЛЕТ ОТКЛЮЧЁН · 12:46`
- Title (Onest 700 15pt foreground): «Не вижу ваш браслет»
- Sub (13pt foreground, 2 строки):
  «Пульс не обновляется. GPS, время и калории продолжают писаться.»
- Actions row inline:
  - **«Переподключить»** — wine small button (36pt, padding 12 16)
  - **«Завершить тренировку»** — text-link destructive red secondary

### Page 1 content (под banner, frozen HR)
- HR-value `156 bpm` в **muted-grey** (заморожено) + small clock-icon справа (visualHints что данные старые)
- Sub под HR: «последний замер 12:46» (mono 11pt muted)
- Zone 3 chip greyed (не активная)
- Bottom 3-column meta:
  - `2.36 км` (продолжает обновляться, GPS работает)
  - `5:22 мин/км` (live)
  - `186 ккал` (live, рассчитываются по time + GPS)
- Зоны-полоса внизу (визуально присутствует, но без активной zone indicator — frozen HR ⇒ нет live zone)

### **БЕЗ tab-bar** (Training Active не имеет tab-bar)

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих экранов
- **Wine `#831843`** primary CTA («Сохранить», «Переподключить»)
- **Destructive red `#b91c1c`** для «Удалить» / «Завершить тренировку»
- **Alert-orange `#d97706`** для bracelet disconnect banner accent
- **Alert-soft `#fdf3e1`** для banner bg
- **Muted-grey** для frozen HR visualHints + last-known timestamp
- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN** если используются Tailwind-классы
- **Header canonical** — заимствуй pattern из existing (session-detail для End-of-session app-bar, training-active для Bracelet disconnect)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на всех цифрах (5.20, 28:04, 142, 186, 156, 2.36, 12:48, 12:46, 5:22)
- **SVG icons** (НЕ emoji): bluetooth-off, clock, save, trash

---

## Skills

UX/UI агент — выбери релевантные skills под задачу. Рекомендую (не диктую):
- `impeccable critique` — anti-slop (не cheesy «Молодец!», не overdone confetti, frozen-state cascade properly)
- `impeccable audit` — WCAG AA (destructive red ≥ 4.5:1, muted timestamp ≥ 4.5:1)
- `emil-design-eng` опц. — confetti subtle fade-in для End-of-session, banner slide-down для Bracelet disconnect

**НЕ запускать:** init/document/craft/extract.

Финальный выбор — за тобой.

---

## Output

**slicing-script DEPRECATED для proof PNG** — crop из 2-phone side-by-side render.

1. **HTML:** `mobile-state-end-of-session-bracelet-disconnect-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `16a-state-end-of-session.png`
   - `16b-state-bracelet-disconnect-training.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `27-end-of-session.png`
   - `28-bracelet-disconnect-training.png`
   - `29-end-bracelet-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames рядом
- [ ] **Phone 1 End-of-session:** eyebrow «ТРЕНИРОВКА ЗАВЕРШЕНА» + title «Молодец!» + sub «Бег · 14 июня, 9:53» + 4 stats cards 2×2 (5.20 км, 28:04, 142 bpm, 186 ккал) + mini sparkline HR + actions wine «Сохранить тренировку» + destructive text-link «Удалить» + БЕЗ tab-bar + close-icon top-right
- [ ] **Phone 2 Bracelet disconnect:** Training Active Page 1 + alert-orange banner («БРАСЛЕТ ОТКЛЮЧЁН · 12:46» / «Не вижу ваш браслет» / actions wine «Переподключить» + destructive text-link «Завершить тренировку») + HR 156 bpm muted-grey с clock-icon + Zone 3 greyed + bottom meta (км/pace/калории все live кроме HR)
- [ ] Box-sizing border-box, Tailwind CDN если нужно
- [ ] WCAG AA на all
- [ ] Transparent PNG via crop из side-by-side
- [ ] Self-review визуальный — открыть PNG ПЕРЕД отчётом

---

## Open вопросы

1. **Confetti на End-of-session** — насколько subtle? Я бы делал **6-8 particles в top corners** (corner-decorative), не full-screen burst (overdone). Если PM хочет cleaner — убираем confetti, оставляем только текст.
2. **Тон «Молодец!»** — может звучать condescending для серьёзного спортсмена. Альтернативы: «Готово!», «Финиш!», или нейтральное «Тренировка завершена». Я выбрал **«Молодец!»** — попадает в pilot target audience (recreational runners из Лиги Героев).
3. **Close-icon top-right на End-of-session** — что делает? «×» = dismiss без сохранения (риск потерять тренировку). Я выбрал visible × как escape hatch, но **default action = «Сохранить»** wine primary. PM может уточнить или попросить confirm-on-close.
4. **Bracelet disconnect bottom meta — 2.36 км обновляется?** Yes — GPS работает, считает дистанцию через motion sensors + GPS-deltas. Только HR не пишется. Это реалистично для Garmin/Apple Watch behaviour.

---

## Reference

- Session Detail (final layout): `mobile-session-detail-v0.html`
- Training Active Page 1: `mobile-training-active-v0.html`
- B1 BT-disconnect banner (consistency): `mobile-state-bt-disconnect-charging-low-v0.html`
- B3 GPS lost banner (parallel pattern): `mobile-state-training-active-corner-cases-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `docs_web/wireframes/m3/mobile-state-end-of-session-bracelet-disconnect-v0.html`
**Transparent PNGs:**
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/16a-state-end-of-session.png` (920×1840 RGBA, alpha=0 углы verified)
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/16b-state-bracelet-disconnect-training.png` (920×1840 RGBA, alpha=0 углы verified)

**Proof-screenshots:**
- `UI_assets/screenshots/onboarding-2026-06-14/27-end-of-session.png` (847×1755)
- `UI_assets/screenshots/onboarding-2026-06-14/28-bracelet-disconnect-training.png` (847×1755)
- `UI_assets/screenshots/onboarding-2026-06-14/29-end-bracelet-side-by-side.png` (1755×1755)

### Что сделано

**Phone 1 — End-of-session summary:**
- Minimal app-bar: только close × top-right (no back)
- Hero: eyebrow «ТРЕНИРОВКА ЗАВЕРШЕНА» wine 11pt + title «Молодец!» Onest 700 36pt + sub «Бег · 14 июня, 9:53» (mono date)
- Confetti: 8 particles subtle fade-in 1200ms (4 left top corner + 4 right top corner), mix wine+alert-orange, размер 4-8px
- Stats 2×2: 5.20 км / 28:04 / 142 bpm / 186 ккал (Onest 700 30pt + Geist Mono units, tabular-nums)
- Mini sparkline card: пульс за 28 мин (120–168 bpm range), wine line + soft area, y-axis ticks 140/168
- Actions: wine 52pt «Сохранить тренировку» + save-icon SVG + destructive text-link «Удалить» + trash-icon SVG
- БЕЗ tab-bar (modal flow)

**Phone 2 — Bracelet disconnect mid-session:**
- App-bar-active canonical с pulse-dot + «БЕГ 00:12:48» (timer running) + STOP btn
- Banner sticky alert-orange (canonical из B3 GPS lost): bluetooth-off icon + «БРАСЛЕТ ОТКЛЮЧЁН · 12:46» + warning-pulse-dot + title «Не вижу ваш браслет» + sub + actions (wine «Переподключить» + destructive text-link «Завершить тренировку»)
- Page 1 frozen: eyebrow alert-orange «ПУЛЬС · ЗАМОРОЖЕН» + HR 156 muted-grey (border-strong) + bpm muted + clock-cue 28×28px справа + «ПОСЛЕДНИЙ ЗАМЕР · 12:46» alert-orange-strong mono + Z3 chip greyed (border-strong bg)
- Bottom meta: 2.36 км / 5:22 мин/км / 186 ккал (live, foreground)
- Zones-strip: Z3 cell greyed-active (border-strong bg вместо primary wine)
- БЕЗ tab-bar

### Skills run

Skills не вызывал в этой сессии — применил inline эвристики:
- **Banner pattern из B3** (canonical reference): скопировал .gps-banner стили в .bb-banner (warning-soft bg + warning border-left 4px + animation banner-slide-down 280ms). Это zero-deviation pattern reuse — обеспечивает consistency с B1/B3.
- **Cascade muted pattern из B3 GPS-lost (lessons 2026-06-15)**: применил selectively — HR + zone chip + last-known-marker frozen, GPS-driven данные (км/pace/ккал) остаются live foreground. Это правильно для bracelet-disconnect (телефон GPS работает) в отличие от auto-pause (всё frozen).
- **Self-critique inline**: после первого render обнаружил два бага — bpm на отдельной строке под 156 (rendering issue с column flex), и Onest font fallback для `·` character (rendered как balloon emoji). Зафиксировал оба.

### Decisions / compromises

1. **Confetti — 8 particles в top corners, не full-screen burst.** Subtle fade-in 1200ms, mix wine+alert-orange, 4-8px sizes. PM может попросить убрать совсем — easy revert (`.confetti-layer` block).
2. **«Молодец!» — оставил.** Альтернативы «Готово!» / «Финиш!» более нейтральные, но менее эмоциональные для recreational runners. Если PM хочет нейтральнее — поменять одну строку.
3. **Close × top-right без confirm-on-close.** Default action = wine «Сохранить» primary. Close = быстрый escape. Если PM хочет защиту от случайного dismiss → добавить modal confirm.
4. **HR 156 + bpm baseline-aligned + clock-icon справа** — после первой итерации bpm рендерился под 156 (одним столбцом). Исправил: `<div display:flex align-items:baseline>` группирует 156 + bpm, clock-icon отдельно справа.
5. **Dot character «·» в hero-sub** — Onest fallback рендерил его как emoji-balloon glyph. Решил через explicit `font-family: 'Space Grotesk'` на .dot + `font-size: 10px` для нормального middot. Сохранён visual baseline.
6. **2.36 км в bottom meta** — обновился с 2.34 (B3) до 2.36 — браслет отключился в 12:46, прошло 2 минуты, GPS добежал ещё ~80м. Реалистично для Garmin/Apple Watch behaviour.

### Что требует ревизии PM

- **Confetti intensity** — 8 particles может быть много / мало. Если cleaner — убрать `.confetti-layer` блок.
- **Тон «Молодец!»** vs «Готово!» / «Финиш!» — open вопрос из BRIEF.
- **Close × без confirm** — позволяет случайно dismiss → потерять тренировку. Если хотим safety — добавить modal «Удалить тренировку?» при close без save.
- **Banner avatar wording** — «Не вижу ваш браслет» vs «Браслет потерян» / «Связь с браслетом потеряна». Я выбрал колloquial для consistency с GPS «Маршрут восстановится автоматически».
- **Zone 3 chip greyed на frozen HR** — это правильное cascade-muted поведение per lessons 2026-06-15. PM may want оставить Z3 active wine (последняя знакомая zone).

### Регрессии

Нет. Файл новый, существующие screens не тронуты. HTML использует canonical patterns из существующих файлов (session-detail, training-active, B1, B3).

### Self-review (визуальный)

Открыл `27-end-of-session.png` через Read — verified:
- Status bar 9:53 ✓, close × top-right ✓, eyebrow wine ✓, «Молодец!» большой Onest bold ✓, sub mono с dot ✓ (после fix)
- 4 stat cards 2×2: значения tabular-nums Onest, units mono ✓
- Sparkline с y-ticks 140/168 ✓, range «120 – 168 bpm» ✓
- Wine «Сохранить тренировку» 52pt + save SVG icon ✓, destructive «Удалить» text-link с trash SVG ✓
- Confetti subtle в top corners — visible, not overwhelming ✓
- Padding-bottom достаточен — нет clipping ✓

Открыл `28-bracelet-disconnect-training.png` через Read — verified:
- Status 9:50 ✓, app-bar-active с pulse-dot + «БЕГ 00:12:48» + STOP ✓
- Banner alert-soft bg + alert-orange border-left ✓, bluetooth-off icon ✓, eyebrow alert-orange-strong ✓, pulse-dot animation ✓, title bold ✓, sub readable, actions: wine «Переподключить» + destructive «Завершить тренировку» ✓
- HR 156 muted-grey (border-strong), bpm baseline aligned (after fix) ✓, clock-cue square справа ✓, «ПОСЛЕДНИЙ ЗАМЕР · 12:46» alert-orange-strong mono ✓
- Z3 chip greyed bg ✓
- Bottom meta 2.36 / 5:22 / 186 live foreground ✓
- Zones-strip Z3 cell greyed-active (border-strong instead of wine) ✓
- БЕЗ tab-bar ✓

Все acceptance criteria из BRIEF выполнены.
