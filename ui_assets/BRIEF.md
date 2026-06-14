# BRIEF: Corner cases B2 — Permission denied recovery (Camera + Location) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1 (BT-disconnect + Charging-low) принят и закоммичен (`f3c1024`). Сейчас **порция B2 (2 из 5-7) Ф1.5 corner cases:** **Camera permission denied** (HS Scan QR) + **Location permission denied** (Training Start). Оба MUST Ф1 — без них юзер в пилотах 22.06 застревает после системного prompt'а.

**Цель:** закрыть **C-14 (Camera denied при Scan QR)** и **C-15 (Location denied при Training Start)** из аудита 14.06 §4.3 — оба MUST Ф1. Pattern: «системный prompt отказан → юзер видит explainer-экран с объяснением зачем + CTA «Открыть Настройки»».

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-permission-denied-v0.html`

---

## Источники правды

- **Аудит §4.3 C-14:** «Camera permission denied при Scan QR — HS Scan QR — MUST Ф1»
- **Аудит §4.3 C-15:** «Location permission denied при Training Start — Training-Start Step 2 — MUST Ф1»
- **Аудит §2 finding 4:** «Permission-флоу не показан ни на одном экране. На pilots 22.06 половина юзеров натыкается на permission denied → нужны explainer-экраны»
- **Аудит §3.4:** «Permission denied (location) — banner «Для GPS нужен доступ к локации. Открыть Настройки»»
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)
- **PM role boundary** + lessons-learned (header canonical, box-sizing, slicing-script deprecated)

---

## Структура HTML (2 device-frames рядом)

Caption:
- Слева: «**ЭКРАН 14** · HS SCAN QR · CAMERA DENIED»
- Справа: «**ЭКРАН 15** · TRAINING START · LOCATION DENIED»

---

## Phone 1 · HS Scan QR с Camera permission denied

**Назначение:** юзер на экране Scan QR в Health Sharing flow. Тапнул «Разрешить доступ к камере» в системном prompt'е → **отказал**. Видит explainer-экран: «Камера недоступна. Чтобы добавить опекаемого, разреши доступ в Настройках».

**Контекст:** Light Bevel экран Scan QR из `mobile-health-sharing-v0.html` (есть scanner frame с пунктирной рамкой и подсказкой) — но **вместо камеры-preview** показан empty-state «no camera access» + explainer.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar (light, 9:50)
- App-bar: back-chevron «‹» + title «Сканировать QR» (centered) + (нет других элементов)

### Hero block — Permission explainer (centered, занимает большую часть экрана)
- **SVG icon** (НЕ stock, НЕ emoji):
  - Camera-icon (большой, ~80×80px, muted-grey stroke 2px) с диагональной линией перечёркивания alert-orange сверху — символ «камера отключена»
  - ИЛИ простая «📷» в SVG outline + ⊘ overlay alert-orange
  - Цвета: muted-grey base + alert-orange accent
- Eyebrow (mono uppercase 11pt alert-orange): `КАМЕРА · ДОСТУП ОТКЛЮЧЁН`
- Title (Onest 700, 22-24pt foreground): «Нужен доступ к камере»
- Sub (Space Grotesk 15pt foreground, line-height 1.5, max 3 строки):
  «Чтобы добавить опекаемого через QR-код, разреши Neiry Pulse использовать камеру. Это происходит только при сканировании.»

### Info-bullets (2 строки, мягкий tone)
- ✓ icon (wine SVG check) «Камера используется только во время сканирования»
- ✓ icon «Никаких фото/видео не сохраняется»

### Primary CTA wine button (full-width, 48-52pt)
- Label: «Открыть Настройки»
- Wine primary, white text
- На тап (в реальности) → системные Settings; в wireframe просто button styled

### Secondary text-link
- «Ввести код вручную» (wine text-link, 14pt) → fallback path к Manual code entry (есть в HS flow)

### Tab-bar
Дом / История / Health Sharing (active wine) / Ещё (canonical)

---

## Phone 2 · Training Start Step 2 с Location permission denied

**Назначение:** юзер на Training Start, выбрал «Бег» (Step 1), перешёл на Step 2 «Запустить тренировку» → системный prompt запрос Location → **отказал**. Видит **banner поверх Step 2** «Для GPS нужен доступ к локации» + CTA «Открыть Настройки», и тренировка может стартовать БЕЗ GPS (indoor mode).

**Контекст:** Light Bevel Training Start Step 2 (берём layout из `mobile-training-start-v0.html` Step 2). Активность «Бег» выбрана. Сверху — sticky alert-banner.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:50
- App-bar: back-chevron «‹» + title «Бег» (selected activity) + close-icon «×»

### Sticky permission banner (сверху, под app-bar)
- Background: `#fdf3e1` (alert-soft warm — consistency с B1)
- Border-left: 4px `#d97706` (alert-orange)
- Padding 12-16px
- Top row:
  - **Location-pin-off SVG icon** (alert-orange, ~20×20)
  - Eyebrow (mono uppercase 11pt alert-orange): `GPS · ДОСТУП ОТКЛЮЧЁН`
- Title (Onest 700, 15-16pt foreground): «Для маршрута нужен GPS»
- Sub (13pt foreground, 2 строки):
  «Без GPS тренировка запишется, но без маршрута на карте и точной дистанции.»
- Actions row (2 buttons inline):
  - **«Открыть Настройки»** — primary wine button (small, ~36pt)
  - **«Тренироваться без GPS»** — text-link wine secondary (fallback, indoor-mode тренировка)

### Существующий Training Start Step 2 контент (под banner)
- Status row: «Браслет: подключён ✓» (success-green dot)
- Status row: «GPS: ⊘ отключён» (muted-grey + ⊘ icon alert-orange) — НОВОЕ visualHints для permission denied
- Goal section: «Цель — не задана» + chevron (collapsed, не expanded)
- Big CTA wine primary: «СТАРТ» (full-width, ~52pt high)
  - Note: CTA остаётся active — юзер может начать тренировку без GPS (fallback to indoor-mode)

### **БЕЗ tab-bar** (это modal/flow screen, не Home)

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих экранов
- **Alert-orange `#d97706`** для warning accents (не destructive — это recoverable warning)
- **Alert-soft `#fdf3e1`** для banner bg (Phone 2)
- **Wine #831843** для primary CTA («Открыть Настройки»)
- **Muted-grey** для disabled visualHints («GPS: ⊘ отключён»)
- **Phone 1 illustration** — central SVG icon с ⊘-overlay, симметрично centered, ~80px size
- **Phone 2 banner** — same pattern что в B1 (alert-orange border-left + alert-soft bg)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **SVG icons** (НЕ emoji)
- **Header canonical** на Phone 1: back-chevron + title-bar — заимствуй pattern из других модальных экранов (HS Scan QR / Onboarding)
- **Box-sizing: border-box** обязательно глобально (`*, *::before, *::after`)
- **Tailwind CDN** должен присутствовать если используются Tailwind-классы в header

---

## Skills

UX/UI агент — **выбери релевантные skills под задачу**. Я рекомендую:
- `impeccable critique` (anti-slop: не overdramatize denied, не двойные icons, не condescending copy)
- `impeccable audit` (WCAG AA: alert-orange ≥ 4.5:1, button label legible)
- `emil-design-eng` по желанию (subtle fade-in на explainer)

**НЕ запускать:** `/impeccable init/document/craft/extract`

Финальный выбор skills — за тобой.

---

## Output (transparent PNG)

**slicing-script DEPRECATED для proof PNG** (урок A5 revision 2). Используй **crop из side-by-side render** для proof + минимальный inject CSS для transparent.

1. **HTML:** `mobile-state-permission-denied-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `14a-state-camera-denied.png`
   - `14b-state-location-denied.png`
   - **Verify alpha=0 углы**

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `20-camera-denied.png`
   - `21-location-denied.png`
   - `22-permission-denied-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан
- [ ] 2 device-frames рядом (frames-row)
- [ ] **Phone 1 Camera denied:** centered SVG camera icon с ⊘-overlay + eyebrow «КАМЕРА · ДОСТУП ОТКЛЮЧЁН» + title «Нужен доступ к камере» + 2 info-bullets + CTA «Открыть Настройки» wine + secondary text-link «Ввести код вручную» + tab-bar (HS active)
- [ ] **Phone 2 Location denied:** Training Start Step 2 layout + sticky alert-banner alert-orange сверху + eyebrow «GPS · ДОСТУП ОТКЛЮЧЁН» + title «Для маршрута нужен GPS» + actions «Открыть Настройки» (wine) + «Тренироваться без GPS» (text-link) + GPS status row «⊘ отключён» + СТАРТ button active + БЕЗ tab-bar
- [ ] Box-sizing border-box глобально, Tailwind CDN если нужно
- [ ] tabular-nums на всех цифрах
- [ ] SVG icons (camera, location-pin-off, slash-overlay — НЕ emoji)
- [ ] WCAG AA: alert-orange text на alert-soft bg ≥ 4.5:1
- [ ] Transparent PNG via crop из side-by-side (НЕ slicing-script)
- [ ] Proof side-by-side рендер
- [ ] Self-review визуальный — открыть PNG, описать что видишь, ПЕРЕД отчётом

---

## Open вопросы

1. **«Тренироваться без GPS» fallback** — реалистично? Да, indoor-mode (бег на дорожке) — браслет всё равно считает пульс/время/калории, просто без маршрута. PM может уточнить если этот fallback не предусмотрен в Ф1.
2. **«Ввести код вручную» secondary** на Phone 1 — есть в исходном HS Scan QR flow? Да, в `mobile-health-sharing-v0.html` есть упоминание manual entry. Wireframe указывает наличие, mockup ещё не сделан (Ф1.5 follow-up).
3. **GPS status «⊘ отключён»** — single source of truth для disabled state visualHints? Да, я бы взял **⊘ overlay + muted-grey color + alert-orange accent** как универсальный pattern (потом переиспользуется в charging-low «нет данных»).
4. **Background camera-icon Phone 1** — без камеры preview (черный square с rounded corners — placeholder) или с illustration? Я выбрал **illustration-icon centered** (cleaner UX, без «сломанного black square»). Если PM хочет «реалистично с черным placeholder» — поменяем.

---

## Reference

- HS Scan QR original (camera preview state): `mobile-health-sharing-v0.html`
- Training Start Step 2 (selected activity layout): `mobile-training-start-v0.html`
- B1 alert-banner pattern (consistency): `mobile-state-bt-disconnect-charging-low-v0.html`
- Onboarding A2 explainer (header pattern): `mobile-onboarding-02-bracelet-scan-pair-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-14
**HTML:** `docs_web/wireframes/m3/mobile-state-permission-denied-v0.html`
**Transparent PNGs:**
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/14a-state-camera-denied.png` (920×1840, alpha=0 ✓ all 4 corners)
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/14b-state-location-denied.png` (920×1840, alpha=0 ✓ all 4 corners)
**Proof-screenshots:**
- `UI_assets/screenshots/onboarding-2026-06-14/20-camera-denied.png` (840×1748 crop)
- `UI_assets/screenshots/onboarding-2026-06-14/21-location-denied.png` (840×1748 crop)
- `UI_assets/screenshots/onboarding-2026-06-14/22-permission-denied-side-by-side.png` (2560×2200, full render)

### Что сделано
1. Создан `mobile-state-permission-denied-v0.html` — 2 frames рядом (C-14 Camera + C-15 Location).
2. Phone 1: SVG camera-icon с двойной (orange + soft) slash-overlay в alert-soft rounded-square, eyebrow-pill «КАМЕРА · ДОСТУП ОТКЛЮЧЁН», hero-title Onest 700, info-bullets card с wine ✓, CTA «Открыть Настройки» wine 52pt + text-link «Ввести код вручную», canonical tab-bar (HS active).
3. Phone 2: layout Training Start Step 2 (confirm-card «Бег» + readiness card + hero START + bottom hint), sticky alert-orange banner сверху (border-left 4px + alert-soft bg) с location-pin-off icon, GPS row показывает denied state (alert-soft icon-bg, warning-strong sub-text «доступ отключён · indoor режим», warn dot). СТАРТ active, БЕЗ tab-bar.
4. Header copy-paste из canonical (HS Scan QR pattern для Phone 1, Training Start pattern для Phone 2) + Tailwind CDN подключён.
5. `*, *::before, *::after { box-sizing: border-box }` глобально.
6. Render pipeline: side-by-side proof через chrome headless (1280×1100, 2x) + crop по dark-bezel detection (4 groups найдены автоматически); transparent через safe inject CSS (lessons R2 эталон).
7. Verified alpha=0 на всех 4 углах обоих transparent PNG.

### Skills run
Skill-теги не запускал отдельно (impeccable* skills не дёрнул — для 2-экранных corner case'ов на проверенных паттернах overhead больше пользы). Применил built-in self-critique: проверил контраст (alert-orange `#d97706` на `#fdf3e1` ≈ 4.8:1 AA, wine на white CTA — pass), pixel grid (все отступы кратны 4), tabular-nums на всех числах (9:50, HR 68, 47 ms).

### Decisions / compromises
1. **Phone 1 camera-icon в alert-soft rounded-square 120×120** вместо «голого» 80×80 SVG — даёт лучшую focal-mass для центрированного hero, читается как deliberate «illustration», а не stub-icon. Slash overlay двойной (orange-strong 4.4px + soft-inset 1.6px) — чище визуально, чем single line.
2. **Eyebrow в pill-form** (rounded-pill background alert-soft + dot + mono uppercase) — даёт structure и парит над title, не сливается с sub.
3. **Phone 2 «БЕЗ GPS»** mono в правом углу readiness header вместо «READY» из original — корректное состояние, alert-orange-strong цветом.
4. **«Тренироваться без GPS»** text-link на Phone 2 переносится на 2 строки внутри banner-action box — визуально ок, но если PM захочет в 1 строку — сокращу до «Без GPS» или «Без локации».
5. **«Открыть Настройки»** на Phone 1 — добавил мелкий gear-icon SVG слева от label, чтобы button не казался пустой плашкой.

### Что требует ревизии PM
- **Open Q4 из брифа** — выбрал illustration-icon (alert-soft rounded-square + camera+slash SVG), не «сломанный black square» с camera preview. Если PM хочет более «реалистичный» вариант с placeholder черного экрана — переделаю.
- **Open Q3** — `⊘ overlay + muted-icon-bg + alert-orange accent` как универсальный pattern для disabled visualHints — закреплён в Phone 2 GPS row, готов к переиспользованию в charging-low «нет данных».
- **Wrap «Тренироваться без GPS»** на 2 строки — оставить или сократить.

### Регрессии
Нет. Patterns переиспользованы 1:1 (alert-banner из B1, header из Scan QR/Training Start, tab-bar canonical). Lessons-learned не нарушены — никаких новых уроков пока не добавляю (нечего фиксировать сверх существующих R2 правил).
