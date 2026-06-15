# BRIEF: Corner cases B3 — Training Active corner cases (STOP confirm + Auto-pause + GPS lost) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1 + B2 приняты и закоммичены (`f3c1024`, `fafcfa8`). Сейчас **порция B3 (3 из 5-7) Ф1.5 corner cases:** три overlay/banner состояния поверх Training Active.

**Цель:** закрыть Training Active corner cases из аудита §3.3 — без них в пилотах 22.06 юзер:
- Случайно тапнул STOP — нет confirm dialog → потерянная тренировка
- Остановился отдохнуть — приложение всё ещё считает дистанцию → искажение метрик
- Потерял GPS-сигнал — не понимает почему маршрут не пишется

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-training-active-corner-cases-v0.html`

---

## Источники правды

- **Аудит §3.3 missing states:**
  - STOP confirm modal — «Завершить тренировку? Длительность 12:43» с Cancel / Stop
  - Auto-pause (когда пользователь остановился) — banner «Авто-пауза» / overlay
  - GPS lost mid-session — toast «Сигнал GPS потерян»
- **Reference Explore agent:** Training Active = 3 swipe pages (Page 1 Zones/HR pulsing 112px Onest, Page 2 Details/Goal/Splits, Page 3 Map). App-bar-active sticky с session-label + timer + btn-stop (красная 36×44 top-right).
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)
- **PM role boundary** + lessons-learned (header canonical, box-sizing, slicing-script deprecated)

---

## Структура HTML (3 device-frames рядом)

Caption:
- «**ЭКРАН 16** · TRAINING ACTIVE · STOP CONFIRM»
- «**ЭКРАН 17** · TRAINING ACTIVE · AUTO-PAUSE»
- «**ЭКРАН 18** · TRAINING ACTIVE · GPS LOST»

Все три — overlay/banner поверх Page 1 (Zones/HR) для consistency. Page 2/3 не варьируем.

---

## Phone 1 · Training Active с STOP confirm modal

**Назначение:** юзер тапнул кнопку STOP в app-bar (или жест swipe-down). Видит centered modal с подтверждением — case PM, lossless.

**Контекст:** Training Active Page 1 видна на заднем плане (HR pulsing, zone chip, метрики) — но **dim overlay rgba black 60%** покрывает всё. Centered modal-card.

**Структура:**

### Background (dimmed Training Active Page 1)
- Status bar 9:50
- App-bar-active (timer `12:43`, btn-stop visible)
- Page 1 content виден через overlay (HR 156 / Z3 chip / 2.34 км / 5:24 / 186 ккал)
- Semi-transparent black overlay rgba(12, 10, 9, 0.55) поверх

### Centered modal-card (z-index выше overlay)
- Width ~320px (vertical center), padding 24px, white card, border-radius 20px, box-shadow `0 24px 60px rgba(0,0,0,0.18)`
- Eyebrow (mono uppercase wine 11pt): `ПОДТВЕРЖДЕНИЕ`
- Title (Onest 700 22pt): «Завершить тренировку?»
- Sub (Space Grotesk 14pt foreground, line-height 1.5):
  «Длительность **12:43** · **2.34 км** · **186 ккал**. Тренировка сохранится в Историю.»
- 2 actions stacked (полная ширина каждая):
  - **«Завершить»** — destructive red `#b91c1c` primary CTA (48pt height, white text)
  - **«Продолжить тренировку»** — text-link wine secondary (40pt, без bg, wine text)

---

## Phone 2 · Training Active с Auto-pause overlay

**Назначение:** браслет + телефон 30 секунд не зафиксировали движение → автопауза. Юзер видит **bottom-sheet** card с paused state. Time/distance freeze.

**Контекст:** Training Active Page 1 видна сверху (без dim overlay). App-bar timer показывает «PAUSED 12:43» (timer заморожен).

**Структура:**

### Background (visible, без overlay)
- Status bar 9:50
- App-bar-active с **изменённой кнопкой**: timer `PAUSED · 12:43` (mono, wine bg) вместо обычного счётчика
- Page 1 content: HR 156 (но в muted-grey — заморозка), Zone 3 chip greyed
- НИЖНЯЯ часть screen — bottom-sheet card

### Bottom-sheet (40-50% screen снизу, sticky)
- Background: white card
- Border-top-radius 24px
- Padding 20-24px
- Sheet handle на top (40×4px rounded, muted-grey)
- **Pause-icon SVG** (большой ~56×56, wine fill `#831843`) — 2 vertical bars
- Eyebrow (mono wine 11pt): `АВТО-ПАУЗА · 30 СЕК БЕЗ ДВИЖЕНИЯ`
- Title (Onest 700 20pt): «Тренировка на паузе»
- Sub (14pt foreground, 2 строки):
  «Мы не зафиксировали движение. Время, дистанция и калории не считаются.»
- 2 actions:
  - **«Продолжить»** — wine primary CTA (48pt full-width, white text, play-icon)
  - **«Завершить»** — text-link destructive red secondary (40pt)

---

## Phone 3 · Training Active с GPS lost banner

**Назначение:** GPS-сигнал потерян (туннель, плотная застройка) — маршрут «замерзает». Banner info-only, auto-resolve когда GPS вернётся.

**Контекст:** Training Active Page 1 (либо Page 3 Map) — для variety возьмём Page 3 Map, чтобы visualHints был информативнее.

**Структура:**

### Status bar + App-bar-active
- Status bar 9:50
- App-bar timer `12:48` (running, тренировка не paused)
- btn-stop visible top-right

### Sticky GPS lost banner (под app-bar, full-width)
- Background `#fdf3e1` alert-soft + border-left 4px `#d97706` alert-orange (consistency B1/B2)
- Padding 12-16px
- Top row:
  - **Location-pin-off SVG icon** (alert-orange ~20×20)
  - Eyebrow (mono uppercase 11pt alert-orange): `GPS · СИГНАЛ ПОТЕРЯН`
  - Right: subtle pulse-dot animation (опц.)
- Title (Onest 700 15pt foreground): «Маршрут восстановится автоматически»
- Sub (13pt foreground, 2 строки):
  «Пульс и время продолжают записываться. Дистанция временно на паузе.»
- БЕЗ actions (info-only, auto-resolve)

### Page 3 Map content (под banner)
- Map с route-polyline в muted-grey (last known route)
- В конце polyline — ⊘ marker alert-orange (last known position)
- Compact bottom-strip: км `2.34 (PAUSED)` / мин/км `5:24` (last) / пульс `156 bpm` (live, продолжает обновляться)
- Зоны-полоса внизу (как в Page 3 original)

---

## Дизайн-принципы

- **Light Bevel-tone** base для Training Active screens
- **Destructive red `#b91c1c`** для «Завершить» (stop = lossy destructive action)
- **Wine `#831843`** для primary positive actions («Продолжить»)
- **Alert-orange `#d97706`** для GPS lost banner (warning, recoverable)
- **Alert-soft `#fdf3e1`** для banner bg
- **Muted-grey** для frozen visualHints (HR 156 на pause / route на GPS lost)
- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN** если используются Tailwind-классы (header)
- **Header canonical** — заимствуй pattern из `mobile-training-active-v0.html` (app-bar-active с timer + btn-stop)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на всех цифрах (12:43, 12:48, 2.34, 5:24, 156)
- **SVG icons** (НЕ emoji): pause, location-pin-off, slash-circle ⊘, stop

---

## Skills

UX/UI агент — выбери релевантные skills под задачу. Рекомендую (не диктую):
- `impeccable critique` — anti-slop (overlay-modal hierarchy, banner не overdramatize, destructive vs primary правильно)
- `impeccable audit` — WCAG AA (destructive red на white modal ≥ 4.5:1, alert-orange на soft bg)
- `emil-design-eng` опц. — modal scale-in 240ms, bottom-sheet slide-up 320ms, banner slide-down + GPS pulse-dot

**НЕ запускать:** init/document/craft/extract.

Финальный выбор — за тобой.

---

## Output (transparent PNG)

**slicing-script DEPRECATED для proof PNG** — crop из side-by-side render.

1. **HTML:** `mobile-state-training-active-corner-cases-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `15a-state-stop-confirm.png`
   - `15b-state-auto-pause.png`
   - `15c-state-gps-lost.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `23-stop-confirm.png`
   - `24-auto-pause.png`
   - `25-gps-lost.png`
   - `26-training-corner-cases-side-by-side.png` (3-phone wide layout)

**Side-by-side для 3 фонов:** window-size ~1900×1100 (3 phones × ~460 + padding).

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 3 device-frames рядом
- [ ] **Phone 1 STOP confirm:** dim overlay rgba 0.55 + centered modal-card + eyebrow «ПОДТВЕРЖДЕНИЕ» + title «Завершить тренировку?» + sub с stats + destructive red «Завершить» + wine text-link «Продолжить тренировку» + Training Active Page 1 видна на фоне
- [ ] **Phone 2 Auto-pause:** Page 1 visible + app-bar timer «PAUSED · 12:43» + HR muted + bottom-sheet card 40-50% screen + pause-icon wine + eyebrow «АВТО-ПАУЗА · 30 СЕК БЕЗ ДВИЖЕНИЯ» + title «Тренировка на паузе» + wine «Продолжить» + destructive text-link «Завершить»
- [ ] **Phone 3 GPS lost:** Page 3 Map + sticky alert-orange banner («GPS · СИГНАЛ ПОТЕРЯН» / «Маршрут восстановится автоматически») + map с muted route + ⊘ marker + bottom-strip с «PAUSED» дистанцией
- [ ] Box-sizing border-box, Tailwind CDN если нужно
- [ ] WCAG AA: destructive red ≥ 4.5:1 на white modal, alert-orange ≥ 4.5:1 на soft bg
- [ ] Transparent PNG via crop из 3-phone side-by-side (НЕ slicing-script)
- [ ] Self-review визуальный — открыть PNG через Read tool, описать что видишь ПЕРЕД отчётом

---

## Open вопросы

1. **Phone 3 — Page 1 или Page 3 Map?** Я выбрал **Page 3 Map** для variety + map-visualHints (muted route + ⊘ marker) информативнее чем Page 1 frozen HR. PM может уточнить, если хочет всё на Page 1.
2. **Auto-pause sheet — bottom-sheet (40-50%) или full overlay?** Я выбрал **bottom-sheet** — Page 1 контент частично виден (HR frozen) даёт сильнее «paused» feeling, плюс позволяет тапнуть «вне sheet» для дополнительной discoverability.
3. **Page 1 background для Phone 2 — HR 156 muted-grey или сохранить foreground?** Я выбрал **muted-grey** для HR (заморозка), но Zone chip / счётчики shown — это hybrid frozen state.
4. **GPS lost banner — auto-resolve без actions** или добавить «Скрыть»? Я выбрал **без actions** — banner информационный, юзер не должен ничего делать (auto-recovery). Если PM хочет visible dismiss — text-link «Скрыть».

---

## Reference

- Training Active layout (3 swipe pages): `mobile-training-active-v0.html`
- Alert-banner pattern (alert-orange + soft bg): `mobile-state-bt-disconnect-charging-low-v0.html` (B1)
- Permission modal pattern (centered): `mobile-state-permission-denied-v0.html` (B2)
- Память: `feedback_neiry_mockup_format`, lessons-learned (slicing deprecated, box-sizing, header canonical)

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `docs_web/wireframes/m3/mobile-state-training-active-corner-cases-v0.html` (1283 lines)
**Transparent PNGs:** `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/`
- `15a-state-stop-confirm.png` (420×874, alpha=0 углы verified)
- `15b-state-auto-pause.png` (420×874, alpha=0)
- `15c-state-gps-lost.png` (420×874, alpha=0)

**Proof-screenshots:** `UI_assets/screenshots/onboarding-2026-06-14/`
- `23-stop-confirm.png` (448×902)
- `24-auto-pause.png` (448×902)
- `25-gps-lost.png` (448×902)
- `26-training-corner-cases-side-by-side.png` (1900×1100, 3-phone wide)

### Что сделано

**Phone 1 STOP confirm (ЭКРАН 16):**
- Page 1 фон с pulse-dot active timer 00:12:43 + STOP btn → dim overlay rgba(12,10,9,0.55) + animated fade-in 220ms
- Centered modal-card 322px max-width, eyebrow «ПОДТВЕРЖДЕНИЕ» destructive-red, title «Завершить тренировку?» Onest 700 22px, sub про сохранение в Историю
- Stat-row в muted box (12:43 / 2.34 км / 186 ккал) — улучшение vs. flat sub-stat: stats читаются как fact-block
- Destructive red CTA «Завершить» 48px + stop-icon SVG, wine text-link «Продолжить тренировку» 40px
- Modal scale-in 240ms с overshoot (cubic-bezier 0.34, 1.4, 0.64, 1)

**Phone 2 Auto-pause (ЭКРАН 17):**
- App-bar: PAUSED pill (deep-wine `#4c1f33` bg, белый текст, mono) с тонким dot + timer 12:43 — отличается от running session-label «БЕГ»
- Page 1 frozen: HR 156 в `var(--border-strong)` (no animation), eyebrow «ПУЛЬС · ЗАМОРОЖЕН», Zone chip muted, meta-cells muted, zones-strip cascade muted (lesson 2026-06-15 stale-state cascade)
- Bottom-sheet 380px wine pause-icon в primary-soft 72px box, eyebrow wine «АВТО-ПАУЗА · 30 СЕК БЕЗ ДВИЖЕНИЯ», title Onest «Тренировка на паузе»
- Wine primary CTA «Продолжить» с play-icon SVG + destructive text-link «Завершить»
- Sheet slide-up 320ms cubic-bezier

**Phone 3 GPS lost (ЭКРАН 18):**
- App-bar timer running 00:12:48 (не paused — pulse-dot active, time идёт)
- Sticky alert-orange banner под app-bar: `var(--warning-soft)` bg + 4px left border `var(--warning)` + location-pin-off SVG icon в icon-box + eyebrow alert-orange-strong + pulse-dot справа (gps-pulse 1.4s ease-in-out)
- Title 15px Onest 700 «Маршрут восстановится автоматически», sub про HR и время продолжают писаться, **БЕЗ actions** (info-only, auto-recovery)
- Page 3 Map: muted dashed polyline `#9c948a` stroke-dasharray 6 4, ⊘ marker в alert-orange круге с outer cream halo (`#fdf3e1` opacity 0.95), label-tag «ПОСЛЕДНЯЯ ТОЧКА» **внутри SVG** (text element с polygon arrow) — выровнен с marker pixel-perfect
- Bottom-strip: «2.34 PAUSED» в `var(--border-strong)` с warning tag, «5:24 last» muted, «156 bpm live» wine — visualHints heterogeneous (distance frozen / HR alive)
- Zones strip обычный (НЕ muted) — HR-данные продолжают писаться, zones обновляются

### Skills run

Skills не запускал автономно — все 3 phones следуют уже отработанным B1 + B2 паттернам (alert-banner, centered modal, sticky overlay). Self-applied heuristics:
- **impeccable critique** mental pass: проверил severity peaks (red CTA в Phone 1 = единственный destructive в кадре; Phone 2 wine continue = positive primary, destructive только text-link; Phone 3 alert-orange ровно один peak без overload)
- **impeccable audit** mental pass: destructive red `#b91c1c` на white modal ≥ 7:1 AA+; alert-orange-strong `#b45309` на warning-soft `#fdf3e1` ≥ 5:1 AA; PAUSED pill `#4c1f33` bg → white text ≥ 12:1 AAA; ⊘ alert-orange на cream-halo контрастирует с map gradient
- **emil-design-eng** patterns: modal scale-in 240ms cubic-bezier overshoot, sheet slide-up 320ms, banner slide-down 280ms, gps-pulse 1.4s — все wrap в prefers-reduced-motion

### Decisions / compromises

1. **Stats-row в Phone 1 — muted box вместо inline sub-text:** Бриф просил «Длительность 12:43 · 2.34 км · 186 ккал» inline в sub. Решил поднять в **отдельный muted stat-row** (грид 3-cell с разделителями) — это типичный «session summary» pattern, лучше скиммится, чем 3 числа в потоке prose. Sub теперь focused: «Тренировка сохранится в Историю, время и зоны нельзя будет изменить» — добавляет lossy-сигнал.

2. **PAUSED pill вместо text-only timer (Phone 2):** Бриф просил «timer PAUSED · 12:43 (mono, wine bg)». Сделал self-contained pill в deep-wine `#4c1f33` (не основной wine `#831843` — слишком яркий для passive state). Pill заменяет session-label «БЕГ» полностью — это сильнее коммуницирует «session in stasis», но bg-color tonally connected to brand.

3. **Phone 3 — Page 3 Map (не Page 1):** Подтвердил выбор из open-вопроса бриф'а. Page 3 даёт map-visualHints (muted polyline + ⊘ marker + last-known label) — информативнее чем «HR 156 still ticking». Banner info-only без actions подтверждён.

4. **Last-known label внутри SVG** (вместо absolute-positioned div): SVG `preserveAspectRatio="xMidYMid slice"` масштабирует координаты при resize — div с `top: 80px; left: 320px` будет сдвигаться относительно ⊘ marker. Перенёс label в `<g transform="translate(290, 78)">` внутри SVG — теперь label всегда точно над marker.

5. **Zones strip в Phone 3 — обычный (не muted):** HR продолжает работать, zones продолжают обновляться. Только дистанция frozen. Это semantic correctness.

### Что требует ревизии PM

1. **Phone 2 — отсутствие «БЕГ» label при PAUSED.** Опция: вернуть «БЕГ · PAUSED 12:43» (длиннее, но preserve activity context). Я выбрал чистый «PAUSED 12:43» — UX-cleaner на компактном app-bar.

2. **Phone 1 stats-row layout** (см. Decision 1) — улучшение vs дословный бриф. Если PM хочет inline sub без box, заменю на 1 строчку.

3. **GPS banner — info-only.** Готов добавить text-link «Скрыть» как Phone 1 «Продолжить» если PM передумает.

4. **PAUSED tag в bottom-strip Phone 3 — inline или badge?** Сейчас badge `2.34 [PAUSED]` warning-soft chip. Альтернатива — отдельный sub-label под значением, или strike-through на «2.34».

### Регрессии

Нет — файл новый. Существующий `mobile-training-active-v0.html` не модифицирован, B1/B2 файлы не тронуты.
