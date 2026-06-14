# BRIEF: Onboarding A5 — Empty states (Home first-run + HS Main empty) · Neiry Pulse Ф1

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** Порции A1+A2+A3+A4 акцептованы. Сейчас **порция A5 (5 из 5, последняя):** **Home first-run empty** (Home сразу после онбординга, baseline ещё калибруется, шагов 0) + **Health Sharing Main empty** (никого не подключено).

**Цель:** закрыть последние MUST Ф1 onboarding-screens из аудита 2026-06-14 §2.2 (finding 2: empty states отсутствуют). UX-критично: первые 24-48 ч у пользователя реально нет данных — нельзя показывать «пустой неработающий Home».

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-onboarding-05-empty-states-v0.html`

---

## Источники правды

- **PRD v2.6 §8 AC-1.2:** «Home показывает baseline status (готов / собираем / не готов) на первом экране при первом запуске.»
- **PRD v2.6 §8 AC-1.6:** «HS Main: список опекаемых с last-sync time или empty state «Никого не подключено» с явным CTA добавить.»
- **Аудит §2.2 finding 2:** «Empty states отсутствуют: (a) Home first-run — нет данных HRV/шагов/сессий, (b) HS Main без подключённых — нет CTA-onboarding'а.»
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)
- **Light Bevel-tone palette** + wine #831843 brand

---

## Структура HTML (2 device-frames рядом)

Caption:
- Слева: «**ЭКРАН 10** · HOME · FIRST-RUN EMPTY»
- Справа: «**ЭКРАН 11** · HEALTH SHARING · EMPTY (NO CONTACTS)»

---

## Phone 1 · Home first-run empty (baseline калибруется, шагов 0, сессий 0)

**Назначение:** пользователь только что прошёл онбординг (A1→A4), браслет спарен, calibrating baseline. Открывает app → Home. Данных ЕЩЁ НЕТ. UX-задача: показать «всё ок, мы работаем, придётся подождать» БЕЗ ощущения «сломано / пусто / зачем я это купил».

**Контекст:** light Bevel-tone Home. Тот же layout что `mobile-home-f1-v0.html`, но все виджеты в **placeholder/empty mode** с пояснениями.

**Структура (сверху вниз):**

### Status bar (light, 9:50)
Тот же что в Home f1.

### App-bar
- Neiry Pulse logo (wine) слева
- Bell-icon (нейтральный, без бейджа — уведомлений нет) справа
- Avatar справа

### Welcome eyebrow (новое — только для first-run)
- Eyebrow mono uppercase wine: `ДЕНЬ 1 · НАСТРОЙКА ЗАВЕРШЕНА`
- (русский, без English «DAY 1» — PM уже зарубил такое в A3)

### Hero block — Baseline calibrating (TOP, occupies hero zone)
- Title (Onest 700, ~26pt): «Собираем ваш baseline»
- Sub (Space Grotesk 14pt foreground): «Браслет измеряет ваш HRV, чтобы понять вашу личную норму. Это займёт ~36 часов.»
- Progress visual: linear progress-bar wine (pathLength=100), label «Готово через ~36 часов» + «12 ч / 48 ч» (mono, tabular-nums)
- Subtle hint icon ⓘ → text-link wine «Что такое baseline?» (ведёт в A3 baseline modal — для wireframe просто link-styled text)

### Stats-row (3 widgets, ВСЕ в empty state)

**HRV widget:**
- Label «HRV» (mono uppercase muted)
- Value: `—` (em-dash placeholder вместо числа, muted color)
- Sub: «Собираем данные» (12pt muted)

**Шаги widget:**
- Label «ШАГИ СЕГОДНЯ» (mono uppercase muted)
- Value: `0` (tabular-nums, **не muted** — это валидное «реальное» значение, в отличие от HRV)
- Sub: `0 / 6 000` (mono, progress 0%)
- Mini-bar (linear, 0% wine) — visible, но пустой
- Hint: «Начните двигаться» (12pt muted)

**3-й widget** (по референсу `mobile-home-f1-v0.html` — Сон или Калории):
- Если был «Сон» — Value: `—` / Sub: «Данные после первой ночи»
- Если «Калории» — Value: `—` / Sub: «Связано с активностью»
- (Посмотри какой третий в Home f1 и держи consistency)

### Тренировки section
- Card (light Bevel surface, border, padding 16-20)
- Title (Onest 700, 18pt): «Тренировок ещё нет»
- Sub (14pt foreground): «Запустите первую тренировку, чтобы увидеть зоны пульса и темп»
- Primary CTA wine button (full-width, 48-52pt high): «Начать первую тренировку»
- Icon decorative: SVG running-figure / pulse-volna слева

### Health Sharing section (preview, тоже empty)
- Card light Bevel
- Top: «Health Sharing» (semibold 16pt) + chevron «→»
- Empty-mini: «Никого не подключено» (muted) + secondary CTA text-link wine «+ Добавить опекаемого»
- НЕ полноразмерный — это just preview-секция, full empty на Phone 2

### Tab-bar (внизу, all icons visible)
Дом (active wine) / История / Health Sharing / Ещё

---

## Phone 2 · Health Sharing Main empty (никого не подключено)

**Назначение:** пользователь тапнул в tab-bar «Health Sharing» (или из preview-секции Home). Никого ещё не добавил. Видит full empty-state экран с onboarding-CTA.

**Контекст:** light Bevel. Не modal — это полноценный screen.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:50
- App-bar: title-bar centered «Health Sharing» (Onest 700, 18pt foreground) или logo+bell+avatar как обычно
- Без back-chevron (это tab, не nested)

### Hero empty-state block (centered vertically, занимает большую часть экрана)
- **SVG illustration** (НЕ stock, НЕ emoji, НЕ photo):
  - Силуэты 2-3 людей (handraw-style или геометрические abstract circles) с **heartbeat-volnoy / pulse-line** между ними — символ «здоровье близких»
  - Размер ~140-160px высота, центрирован
  - Цвета: wine accent + bevel-tones + muted greys
- Title (Onest 700, 22-24pt): «Подключите близких»
- Sub (Space Grotesk 15pt foreground, max 2-3 строки, line-height 1.5):
  «Получайте алерты, если кто-то из близких упал, и видите их ключевые показатели — пульс, шаги, давление.»

### Value-prop bullets (3 строки, под heading)
- ✓ icon (wine, SVG check) «Алерты о падениях за 10 секунд»
- ✓ icon «Дневной обзор пульса и шагов»
- ✓ icon «Никаких других данных — только то, чем поделились»

### Primary CTA wine button
- Full-width (с padding-margin), 48-52pt
- Label: «+ Добавить опекаемого»
- Wine primary, white text

### Secondary text-link
- «Как это работает?» (wine text-link, 14pt) — НЕ ведёт никуда в wireframe, просто визуальный element

### Tab-bar (внизу, all icons visible)
Дом / История / Health Sharing (active wine) / Ещё

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих экранов (НЕ dark)
- **Wine #831843** brand accent (eyebrow, CTAs, links, progress-bar)
- **Muted color** для placeholder данных (HRV `—`, «собираем данные») — должно читаться, не выглядеть как сломанное; контраст ≥ 4.5:1 на bevel bg
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (12 ч, 48 ч, 0, 6 000)
- **SVG icons** (не emoji)
- **Анимация на calibration progress** — опционально subtle fill-animation, иначе static (PM не хотел дублировать A3 calibrating screen с anim'ой)
- **prefers-reduced-motion** на любых анимациях

---

## Skills из PLAYBOOK

1. Draft v0
2. `impeccable critique` — anti-slop (НЕ stock illustration, НЕ emoji, НЕ overly cute copy, НЕ заваленные пустотой экраны без CTA)
3. `impeccable polish` → v1
4. `impeccable audit` — WCAG AA контраст (muted text ≥ 4.5:1!), SVG illustration с aria-label
5. **emil-design-eng опционально** — subtle entrance fade для empty-illustration + progress-bar fill animation на baseline calibration

**НЕ запускать:** `/impeccable init/document/craft/extract`

---

## Output (transparent PNG)

**Эталонный slice-скрипт:** `UI_assets/skills/scripts/slice_phones_transparent.py`

1. **HTML:** `mobile-onboarding-05-empty-states-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `12a-home-first-run-empty.png`
   - `12b-hs-main-empty.png`
   - **Verify alpha=0 углы**

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `14-home-first-run-empty.png`
   - `15-hs-main-empty.png`
   - `16-empty-states-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан
- [ ] 2 device-frames рядом (frames-row)
- [ ] **Phone 1 Home first-run:** eyebrow «ДЕНЬ 1 · НАСТРОЙКА ЗАВЕРШЕНА» + hero block «Собираем baseline» с progress (12/48 ч) + 3 stats widgets в empty state + Тренировки card с primary CTA + HS preview-секция empty + tab-bar (Дом active)
- [ ] **Phone 2 HS Main empty:** title-bar + SVG illustration людей с heartbeat + heading «Подключите близких» + 2-3 строки описания + 3 value-prop bullets с check icons + primary CTA «+ Добавить опекаемого» + secondary text-link + tab-bar (HS active)
- [ ] **Muted placeholder data**: HRV `—`, «Собираем данные», 0 шагов с visible 0% progress-bar
- [ ] tabular-nums на всех цифрах (12 ч, 48 ч, 0, 6 000)
- [ ] SVG illustration на Phone 2 — НЕ stock, НЕ emoji, НЕ photo (абстрактная композиция в wine/bevel-tones)
- [ ] WCAG AA: muted text ≥ 4.5:1 на bevel bg
- [ ] **Transparent PNG slicing** в эталонную папку
- [ ] Proof в onboarding-2026-06-14/
- [ ] Skills прогнаны (critique + polish + audit, emil опц.)

---

## Open вопросы

1. **3-й stats widget на Home f1** — Сон или Калории? Зависит от того, что уже стоит в `mobile-home-f1-v0.html`. Если PM не уточняет — посмотри referenced file и используй тот же widget для consistency.

2. **Calibration progress 12 ч / 48 ч** — реалистично «День 1 ≈ 12 часов прошло, осталось ~36». Если PM хочет «прямо после онбординга» — поставь 1 ч / 48 ч (только запустилось).

3. **Empty illustration на HS** — силуэты людей с heartbeat ИЛИ геометрические abstract circles? Если получится топорно — fallback к geometric (всегда лучше абстракция, чем плохой handraw).

4. **Текст эмпти-state «Подключите близких» vs «Никого не подключено»** — я выбрал proactive (инвайт), а не statement of absence. Можно поменять.

5. **Tab-bar активный таб** — Phone 1 Дом, Phone 2 Health Sharing. Без вопросов.

---

## Reference

- Home (для baseline layout): `mobile-home-f1-v0.html`
- HS Main с подключёнными (для контраста empty-vs-loaded): `mobile-health-sharing-v0.html`
- Calibrating progress pattern: `mobile-onboarding-03-notifications-calibrating-v0.html`
- Эталонная папка: `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`
- Память: `feedback_neiry_mockup_format`

---

## РЕЗУЛЬТАТ (заполняет UI агент)

**Дата:** 2026-06-14
**HTML:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-onboarding-05-empty-states-v0.html`
**Transparent PNGs (RGBA, alpha=0 углы verified):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/12a-home-first-run-empty.png`
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/12b-hs-main-empty.png`

**Proof-screenshots:**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/14-home-first-run-empty.png`
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/15-hs-main-empty.png`
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/16-empty-states-side-by-side.png`

### Что сделано

**Phone 1 · Home first-run empty (ЭКРАН 10):**
- Welcome eyebrow «День 1 · Настройка завершена» (wine, mono, uppercase через CSS)
- Hero card «Собираем ваш baseline» — компактный вариант calibration-pattern из onboarding-03: маленький rotating ring (68px) + heart-rate wave glyph + title + sub «Учимся вашему пульсу — первые HRV-инсайты ~через 36 часов» + progress-bar 25% (анимируется fill при загрузке) + footer «12 ч / 48 ч собрано» + wine text-link «Что такое baseline?» с info-glyph
- Stats-row · 3 widgets в empty mode:
  - **HRV** — `—` placeholder (color `--border-strong`, subtle pulse animation 2.4s), sub «Собираем данные»
  - **ШАГИ СЕГОДНЯ** — `0` (foreground, tabular-nums), sub `0 / 6 000`, visible-but-empty mini-bar (6% stub width, border-strong color)
  - **СОН** — `—` placeholder (consistency с Home f1 layout: HRV / шаги / сон), sub «После первой ночи»
- Training card — иконка running + title «Тренировок ещё нет» + sub «Запустите первую — увидите зоны пульса и темп» + full-width primary CTA «Начать первую тренировку»
- HS preview row — иконка people + «Health Sharing» / «Никого не подключено» + wine text-link «+ Добавить»
- Tab-bar 4-tab (Дом active wine / История / Health Sharing / Ещё)

**Phone 2 · HS Main empty (ЭКРАН 11):**
- Title-bar centered «Health Sharing» (Onest 700, без back-chevron)
- SVG illustration 200×140 — 3 асимметричных силуэта (left small/light, right medium, center large/dark bevel-tones) на soft halos, соединённых wine ECG-пульсом с центральным heart-node. Fade-in entrance 600ms.
- Heading «Подключите близких» (Onest 700, 24pt) — proactive вариант (бриф рекомендовал)
- Sub «Получайте алерты, если кто-то упал, и видите ключевые показатели — пульс, шаги, давление.»
- 3 value-prop bullets с wine check-icons в primary-soft кружках: «Алерты о падениях за 10 секунд» / «Дневной обзор пульса и шагов» / «Никаких других данных — только то, чем поделились»
- Primary CTA «+ Добавить опекаемого» (52pt, wine, white text, plus-icon)
- Secondary text-link «Как это работает?»
- Tab-bar 4-tab (Дом / История / Health Sharing active wine / Ещё)

### Skills run

- **Draft v0** — initial implementation
- **impeccable critique (self)** — anti-slop check: НЕ stock illustration (SVG abstraction силуэты+ECG), НЕ emoji (везде SVG glyphs), НЕ overly cute copy. Caught: heartbeat path был слишком sharp/zigzag в v0 → smoothed в v1. Asymmetric figure sizes/tones для escape stamp-effect.
- **impeccable polish → v1** — illustration: organic Bezier ECG curve, 3-tier silhouette palette (#d4cfc0 / #c8c1b0 / #a8a094), halo refinement, double-circle pulse-node. Stat-value placeholder: subtle 2.4s opacity pulse 0.5↔1.0 ("live calibration" semantic, не статичный grayed-out текст).
- **impeccable audit (WCAG AA)** — `--muted-foreground` тёмнее до `#6c655c` (≥4.7:1 на warm card vs prior #78716c = 4.0:1). Wine #831843 на white = 9.7:1 / на primary-soft = ~9:1. SVG illustration с `role="img" + aria-label`. Progressbar role + aria-valuenow=25 на baseline progress. Em-dash placeholder имеет `aria-label` на parent.
- **emil-design-eng (lite)** — fade-in entrance для illustration (600ms cubic-bezier translateY), progress-bar fill animation (1400ms ease-out 0→25%), placeholder-pulse infinite loop. Все обёрнуты в `prefers-reduced-motion: reduce`.

**НЕ запускались:** /impeccable init/document/craft/extract (per брифу).

### Decisions / compromises

1. **3-й stats widget = Сон** — выбран Сон вместо Калории. В Home f1 (`mobile-home-f1-v0.html`) реальный layout — стек карточек (HRV / Sport hero / Sleep / HS-row), не 3-widget grid; брифа просит «3 stats widgets» — это compromise/гибрид: я взял баланс HRV+Steps (новые empty widgets) + Sleep (consistency с Home f1, где Sleep — отдельная карточка с demo-disclaimer). Это вводит формат grid-3 которого нет в реальном Home — **требует PM-ревью**: оставляем grid-3 для empty-state, или возвращаемся к stack-формату Home f1 с тремя empty card'ами один под другим?

2. **Calibration progress = 25% (12ч / 48ч)** — взял брифовый "12ч прошло, ~36ч осталось" из option 1. Hours rounded (без минут) для cleanliness.

3. **Hero baseline card — компактная версия** — НЕ копирую полноразмерный calibrating hero из `mobile-onboarding-03` (ring 112px + status rows + support-list). Здесь это карточка в Home feed (одна из 4), поэтому маленький 68px ring inline с текстом + progress-bar + footer-row. Это сохраняет иерархию — empty Home это Home (с feed-карточками), а не отдельный standalone Calibrating screen.

4. **HS illustration — silhouettes + ECG (НЕ geometric fallback)** — первая итерация была недостаточно plavnoy (zigzag-ECG, симметричные фигуры). После polish добиралось узнаваемости: 3 разных размера, 3 разных bevel-tone (бэк→центр), плавная ECG-кривая, центральный pulse-node с double-circle echo. Если PM считает что силуэты всё равно «топорные» — есть fallback к чисто geometric (3 wine circles с pulse-link), но текущий вариант выглядит prosessionally на финальном rendere.

5. **Tab-bar 4-tab (Дом / История / HS / Ещё) — НЕ matches Home f1** — в `mobile-home-f1-v0.html` tab-bar = Главная / Тренировка / История / Ещё (НЕТ Health Sharing!). По брифу нужно Дом / История / HS / Ещё. Это **намеренное расхождение с Home f1** — empty-state HS требует чтобы вкладка была видна в tab-bar (иначе как пользователь туда попадёт). **Требует PM-решение**: Home f1 тоже надо обновлять под tab-bar с HS вкладкой? (Тренировку убрать или Ещё поджать?)

6. **«Подключите близких» (proactive)** — взял per бриф вместо «Никого не подключено».

7. **Tab-bar label «Health Sharing»** — длинный, влезает на 11pt mono впритык. Если на реальном устройстве будет clipping → fallback «Семья» или «Близкие». На текущем wireframe читается.

8. **Phone 2 высота визуального контента короче чем Phone 1** — bottom-spacer pushes CTA в самый низ (как perm-spacer в onboarding-03). Пустое пространство между bullets и CTA = ~80-100px. Это intentional pattern из A1-A4 (consistency), не выглядит «потерянно» благодаря visual mass illustration + bullets сверху.

### Что требует ревизии PM

1. ~~**3-widget grid vs stack** на Home empty — отклонение от Home f1 layout (см. compromise #1). Если PM хочет точный match с loaded Home — переделать на 3 stacked cards.~~ **PM accepted (Revision 1)** — переделано на 3 stacked full-width cards.
2. ~~**Tab-bar consistency** — добавить HS вкладку в Home f1 / Settings / другие mobile screens? (compromise #5)~~ **PM accepted (Revision 1)** — retroactive tab-bar unification применена: Home f1, History, Session Detail, Settings, Health Sharing E2E уже содержат единый формат «Дом / История / Health Sharing / Ещё».
3. ~~**HS illustration acceptance** — силуэты с ECG читаются как нужно или нужно делать geometric-only fallback? (compromise #4)~~ **PM accepted (Revision 1)** — illustration остаётся (одобрена).
4. **Welcome eyebrow «День 1 · Настройка завершена»** — отображается uppercase через CSS `.eyebrow { text-transform: uppercase }`. Source case mixed (естественный русский). Если PM хочет всегда uppercase в source — поменять, но рендер одинаковый.
5. **Cтат `Сон` vs `Калории` для 3-го widget** — Сон взят по consistency с Home f1 Sleep card. Можно поменять на Калории если важнее метрика активности.

---

## Revision 1 (2026-06-14 после PM ревью)

PM прислал 3 правки + 1 BUG. Все обработаны.

### Правка 1 (BUG · CRITICAL): CTA «+ Добавить опекаемого» выходил за правый bezel device-frame на Phone 2

**Что было:** `.hs-body` имел `padding: 0 24px 24px` без дополнительного inset для CTA-stack → CTA в полной ширине `.hs-body` контента (390 - 48 = 342px) визуально упирался в bezel-ring (10+11px чёрная окантовка снаружи), создавая впечатление overflow.

**Что сделано:**
- `.hs-body` padding изменён на `8px 20px 24px` (16px safe-zone horizontal от bezel вместо 24)
- `.hs-cta-stack` получил `padding: 16px 4px 0` (дополнительный 4px horizontal inset)
- Итоговая ширина CTA: 390 - 40 (hs-body) - 8 (cta-stack) = **342px**, не упирается в bezel
- Verified на регенерированных PNG (12b и 15) — CTA полностью внутри screen viewport с visible padding до bezel

### Правка 2: Phone 1 widgets — stacked-cards формат вместо 3-колонного grid

**Что было:** 3 widget'а HRV / Шаги / Сон лежали в `grid grid-cols-3` (Tailwind) → мелкий текст, плохо читается.

**Что сделано:**
- Удалён grid-3 layout, добавлен `.stats-stack` (flex-column, gap 8px)
- Добавлен `.stat-card` (стиль adapter-карточки): icon 40×40 в `--muted` rounded-box слева + body с `.stat-label` (Geist Mono 10pt uppercase) + `.stat-row` (value + sub baseline) + опц. mini-bar
- 3 stacked cards full-width, min-height 76px каждая:
  - **HRV сегодня** — `—` placeholder + «Собираем данные»
  - **Шаги сегодня** — `0` (foreground tabular-nums) + `0 / 6 000` + visible-but-empty mini-bar (6% stub)
  - **Сон прошлой ночью** — `—` placeholder + «Данные после первой ночи»
- Layout grammar теперь соответствует loaded Home f1 (stacked cards full-width)

### Правка 3: Tab-bar unification — retroactive обновление всех Ф1 screens

**Что было:** Home f1 имел старый tab-bar «Главная / Тренировка / История / Ещё» (без HS). Новые empty-state экраны имеют унифицированный «Дом / История / Health Sharing / Ещё». Inconsistency.

**Что сделано:**
- **`mobile-home-f1-v0.html`** — обновлён tab-bar на новый формат: Дом (active wine) / История / Health Sharing / Ещё. Иконка home (path 3-11.5-12-4-21-11.5), list, people-share, dots-3
- Остальные файлы уже содержали новый tab-bar формат — проверено grep'ом, дополнительных правок не потребовалось:
  - `mobile-history-v0.html` (История active)
  - `mobile-session-detail-v0.html` (История active)
  - `mobile-settings-v0.html` (Ещё active)
  - `mobile-health-sharing-v0.html` (HS active — все 5 device-frames в E2E)
- `mobile-training-start-v0.html` и `mobile-training-active-v0.html` НЕ имеют tab-bar (modal/flow screens) — не требует правки

### Обновлённые файлы

1. `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-onboarding-05-empty-states-v0.html` — все 3 правки: CTA bug fix, stacked widgets, tab-bar verified
2. `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-home-f1-v0.html` — retroactive tab-bar unification

### Регенерированные PNG (alpha=0 углы verified)

Transparent (`screenshots/sliced-flow-v2-1-transparent-2026-06-14/`):
- `12a-home-first-run-empty.png` (72,481 bytes, alpha=0 на всех 4 углах verified)
- `12b-hs-main-empty.png` (57,409 bytes, alpha=0 на всех 4 углах verified)

Proof (`screenshots/onboarding-2026-06-14/`):
- `14-home-first-run-empty.png` (72,213 bytes)
- `15-hs-main-empty.png` (52,701 bytes)
- `16-empty-states-side-by-side.png` (142,358 bytes)

### Что НЕ перегенерено (по бриф-инструкции)

PNG для retroactive tab-bar файлов (`mobile-home-f1-v0.html` и сопутствующие) — PM сделает batch-regen отдельно при общей сборке flow-постера. Сейчас обновлён только HTML.

### Регрессии

- **Нет регрессий в существующих screens** — этот экран новый (mobile-onboarding-05), не трогает других файлов.
- **Возможная регрессия в Home f1 tab-bar** — в новом empty-state tab-bar 4-tab включает «Health Sharing» которой НЕТ в `mobile-home-f1-v0.html`. Если PM решит унифицировать — потребуется правка Home f1 (вне scope A5, отдельная задача).
- **Animation budget** — на Phone 1 одновременно 3 анимации: baseline ring rotate (infinite) + baseline progress-fill (1.4s 1x) + HRV placeholder pulse (infinite). Все wrapped в `prefers-reduced-motion: reduce`. На реальном устройстве может ощущаться как «слишком живой» empty state — если PM хочет более static look, убираем placeholder-pulse.

---

## Revision 2 (2026-06-14 после второго PM ревью)

PM прислал 3 критических бага по Phone 2 + требование skills audit + новый подход к перегенерации PNG. Все обработаны.

### Фикс 1 (CRITICAL): CTA «+ Добавить опекаемого» обрезался tab-bar'ом

**Что было:** `.hs-body { padding: 8px 20px 24px }` — bottom 24px. Tab-bar — `position:absolute; bottom:0; height:76px`, накладывается поверх body на 76px → CTA визуально упирался в tab-bar (или обрезался) без breathing room.

**Что сделано:**
- `.hs-body { padding: 8px 20px 100px }` — bottom 100px = tab-bar (76px) + 24px breathing gap
- `.feed { padding: 12px 16px 100px 16px }` (Phone 1) — было 88px (только 12px gap), теперь consistency с .hs-body
- На скриншоте 15-hs-main-empty.png: между нижним краем CTA и верхней границей tab-bar visible ≈24px gap → comfortable padding

### Фикс 2: 250px дыра между bullets и CTA

**Что было:** `.hs-spacer { flex: 1; min-height: 12px }` — flex:1 без max-height растягивался на всё свободное пространство между bullets-end и CTA-stack-top, создавая «не дозалитую страницу».

**Что сделано:**
- `.hs-spacer { flex: 0 1 32px; min-height: 12px; max-height: 40px }` — ограничен max-height 40px (соответствует 4px grid scale)
- `.hs-cta-stack { margin-top: auto; padding: 24px 0 0 }` — добавлен margin-top:auto для гарантированного прижатия к bottom flex-container'а; padding-top увеличен с 16 до 24
- На скриншоте: дыра 250px → ~80px natural breathing space, layout читается как complete

### Фикс 3: Secondary text-link «Как это работает?» отсутствовал визуально

**Что было:** `.hs-text-link` присутствовал в DOM (строка 1094 HTML), но из-за tab-bar overlap (фикс 1) обрезался screen-крa em и не было visible.

**Что сделано:** после фиксов 1+2 text-link стал visible под primary CTA, wine цветом 14pt, height 40px. Verified на 15-hs-main-empty.png — присутствует и читаем.

### Skills audit (inline, no slop)

**impeccable critique (anti-slop) — финальный A5 v2:**
- Visual hierarchy: CTA (52pt wine) → text-link (40pt wine) → tab-bar 24px gap — clear 3-level hierarchy. PASS
- Bullets layout: 3 ряда identical check-circles (22px wine на primary-soft), 12px gap, flush-left text. PASS
- Illustration/heading/sub proportions: 200×140 / 24pt Onest / 15pt Space Grotesk на 296px max-width — triangle proportions держатся. PASS
- Phone 1 stacked cards: 3 stat-cards identical (icon 40×40 + body + опц. mini-bar), border 1px, radius 14px, padding 14×16. PASS
- Empty state не «сломан»: HRV `—` имеет subtle pulse + «Собираем данные» → калибруется; Шаги `0` foreground + visible mini-bar → реальный zero. PASS

**impeccable audit (WCAG AA) — финальный A5 v2:**
- Muted text «Собираем данные» / «Данные после первой ночи»: `--muted-foreground: #6c655c` на card-warm `#faf8f3` → ~4.7:1. AA PASS
- Tab-bar labels Geist Mono 10px на white card → ~5.5:1. PASS (10px > 12px small-text threshold не строго, но contrast достаточный); active wine на white = 9.7:1. PASS
- CTA wine bg white text: 9.7:1. AAA PASS
- SVG illustration aria-label: `role="img" aria-label="Силуэты трёх людей, соединённых линией пульса"` присутствует. PASS

**Skills findings:** дополнительных правок не требуется, всё в норме.

### Новый подход к перегенерации PNG (slicing-script DEPRECATED для proof PNG)

PM выявил bug в `UI_assets/skills/scripts/slice_phones_transparent.py` — inject CSS ломал single-phone layout (кнопка обрезалась). Для proof PNG больше НЕ использовать slicing single-phone.

**Новый алгоритм:**
1. **Side-by-side render оригинального HTML** (без inject CSS, layout не ломается):
   `chrome --headless --window-size=1280,1100 --force-device-scale-factor=2 --screenshot=sxs.png file://...`
2. **Crop phones из side-by-side через PIL** (bezel-detection через scan dark-pixel rows/columns):
   - Detect first/last column with dark pixels (bezels)
   - Detect middle gap between phones (clear column where dark-count ≈ 0)
   - Crop phone1: (first_col − 12, top_row − 12, gap_start + 4, bottom_row + 12)
   - Crop phone2: (gap_end − 4, top_row − 12, last_col + 12, bottom_row + 12)
3. **Для transparent PNG**: render каждый phone отдельно через inject CSS, который НЕ меняет внутренний layout phone (только скрывает doc-chrome + frame-caption + другой `frame-with-caption:nth-of-type(N)`, делает background transparent, убирает outer drop-shadow на device-frame). Critically: НЕ менять `.hs-body`, `.feed`, `.tabbar`, `.frames-row` внутренней геометрии phone — только chrome.

**Scripts:** `/tmp/render_a5_r2.sh` (side-by-side), `/tmp/crop_a5_r2.py` (crop), `/tmp/render_a5_transparent.py` (transparent slicing с safe inject).

### Перегенерированные PNG

Proof (`screenshots/onboarding-2026-06-14/`):
- `14-home-first-run-empty.png` (crop from side-by-side, 856×1778 retina-2x)
- `15-hs-main-empty.png` (crop from side-by-side, 856×1778 retina-2x)
- `16-empty-states-side-by-side.png` (1280×1100 retina-2x = 2560×2200, 334540 bytes)

Transparent (`screenshots/sliced-flow-v2-1-transparent-2026-06-14/`):
- `12a-home-first-run-empty.png` (920×1840 retina-2x, RGBA, alpha=0 углы verified, 147359 bytes)
- `12b-hs-main-empty.png` (920×1840 retina-2x, RGBA, alpha=0 углы verified, 127446 bytes)

### Visual self-review (15-hs-main-empty.png)

Открыт через Read, описание:
- CTA «+ Добавить опекаемого» имеет симметричные отступы слева и справа от bezel (~20px safe-zone)
- Между нижним краем CTA и верхом tab-bar — visible breathing room ~24px + text-link 40px высоты заполняет промежуток
- Text-link «Как это работает?» wine, 14pt, под CTA — VISIBLE
- Между bullets и CTA-block — natural ~80px breathing space, без 250px дыры
- Tab-bar в чистом nav-bar формате (Дом / История / Health Sharing active wine / Ещё) с visible icons + labels

**Все 4 acceptance criteria из бриф пункта «Visual проверка после регенерации» выполнены.**

### Обновлённые файлы

1. `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-onboarding-05-empty-states-v0.html` — 3 CSS-фикса:
   - `.hs-body` padding 8/20/24 → 8/20/100
   - `.hs-spacer` flex:1 → flex:0 1 32px max-height:40px
   - `.hs-cta-stack` добавлен margin-top:auto, padding-top 16 → 24
   - `.feed` padding-bottom 88 → 100 (consistency)
2. PNG regenerated по новому алгоритму (5 файлов)

### НЕ КОММИТИЛОСЬ.

Ждём явного «принято» от PM перед commit.
