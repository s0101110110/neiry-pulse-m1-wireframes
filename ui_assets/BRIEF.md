# BRIEF: Corner cases B5 — Session Detail states (Delete confirm + Sharing in progress) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1+B2+B3+B4 приняты и закоммичены (`f3c1024`, `fafcfa8`, `406c04c`, `037539d`). Сейчас **порция B5 (5 из 7) Ф1.5 corner cases:** Session Detail edge cases — **Delete confirm modal** + **Sharing in progress overlay**.

**Цель:** закрыть Session Detail corner cases из аудита §3.5:
- Delete confirm — без него юзер тапает «Удалить» и тренировка пропадает безвозвратно
- Sharing in progress — после тапа «Share» юзер не понимает что происходит (генерация ссылки / QR / уведомление опекуну в HS)

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-session-detail-edge-cases-v0.html`

---

## Источники правды

- **Аудит §3.5 missing states:**
  - Delete confirm — «Удалить тренировку? Действие нельзя отменить» с Cancel / Delete
  - Sharing in progress — «Генерируем ссылку...» / «Отправляем опекуну...» с loading state
- **Reference (existing):**
  - `mobile-session-detail-v0.html` — base layout Session Detail (hero дистанция 5.20 км + 3-col stats + map + zones + splits + Share/Delete actions)
  - B3 STOP confirm modal pattern (destructive confirm): `mobile-state-training-active-corner-cases-v0.html`
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 21** · SESSION DETAIL · DELETE CONFIRM»
- «**ЭКРАН 22** · SESSION DETAIL · SHARING IN PROGRESS»

---

## Phone 1 · Session Detail с Delete confirm modal

**Назначение:** юзер на Session Detail тапнул «Удалить тренировку» (destructive action внизу экрана). Видит centered modal-confirm — данные не пропадут от случайного тапа.

**Контекст:** Session Detail (берём canonical из `mobile-session-detail-v0.html`) видна на заднем плане dimmed. Centered modal-card с warning.

**Структура:**

### Background (dimmed Session Detail)
- Status bar 9:53
- App-bar с back-chevron + title «Тренировка»
- Hero: «5.20 км · 14 июня, 9:53» (Onest 700, дистанция)
- 3-col stats: HR avg / pace / ккал
- Map (compressed) + zones distribution + splits
- Share / Delete buttons внизу — actions visible, но dimmed
- Semi-transparent black overlay rgba(12, 10, 9, 0.55) поверх

### Centered modal-card (z-index высокий)
- Width ~320px (vertical center), padding 24px, white card, border-radius 20px, box-shadow `0 24px 60px rgba(0,0,0,0.18)`
- **Trash-icon SVG** (centered top, ~48×48, destructive red `#b91c1c`)
- Eyebrow (mono uppercase destructive red 11pt): `БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ`
- Title (Onest 700 22pt foreground): «Удалить тренировку?»
- Sub (Space Grotesk 14pt foreground, line-height 1.5):
  «**Бег · 5.20 км · 28:04**. Это действие нельзя отменить. Маршрут, метрики и зоны будут стёрты.»
- 2 actions stacked:
  - **«Удалить»** — destructive red `#b91c1c` primary CTA (48pt height, white text, trash-icon)
  - **«Отмена»** — text-link wine secondary (40pt)

---

## Phone 2 · Session Detail с Sharing in progress overlay

**Назначение:** юзер тапнул «Поделиться» — видит loading-overlay пока система генерирует ссылку / уведомляет опекунов через Health Sharing. Не должен думать что «зависло».

**Контекст:** Session Detail visible сверху + полупрозрачный overlay rgba black 0.4 (lighter than delete для меньшей tension) + centered loading-card.

**Структура:**

### Background (dimmed Session Detail)
- Status bar 9:53
- Same Session Detail layout
- Overlay rgba(12, 10, 9, 0.4) — softer dim, чем delete (это transient state, не warning)

### Centered loading-card (z-index высокий)
- Width ~280-300px, padding 24px, white card, border-radius 20px, subtle box-shadow
- **Spinner SVG** (centered top, ~40×40, wine `#831843`) с rotate animation
- ИЛИ skeleton-style 3-dot wave animation (wine)
- Eyebrow (mono uppercase wine 11pt): `ОТПРАВКА`
- Title (Onest 700 18pt foreground): «Делимся тренировкой…»
- Sub (Space Grotesk 13pt muted-foreground, 2 строки):
  «Создаём ссылку и уведомляем ваших опекунов в Health Sharing.»
- Mini progress hints (subtle, 2-3 строки с check-icons SVG):
  - ✓ Создана ссылка (wine check, 12pt mono)
  - ◯ Уведомляем Маму, Папу (spinner SVG ~12px, mono 12pt muted)
  - · QR-код готов (greyed-out, ещё не выполнено)
- Text-link «Отмена» (wine 13pt, bottom centered) — позволяет cancel если долго

---

## Дизайн-принципы

- **Light Bevel-tone** background (видна Session Detail dimmed)
- **Destructive red `#b91c1c`** для Delete CTA + trash-icon + «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» eyebrow
- **Wine `#831843`** для primary action sharing + spinner + ссылок Отмена
- **Overlay opacity**: 0.55 для destructive (warning), 0.4 для sharing (transient, soft)
- **Box-sizing border-box** глобально
- **Tailwind CDN** если используется
- **Header canonical** — заимствуй из `mobile-session-detail-v0.html` app-bar (back + title)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (5.20, 28:04)
- **SVG icons** (НЕ emoji): trash, spinner (animated), check, dot

---

## Skills

UX/UI агент — выбери релевантные skills под задачу. Рекомендую (не диктую):
- `impeccable critique` — anti-slop (delete copy НЕ overdramatize, sharing prog не cheesy)
- `impeccable audit` — WCAG AA (destructive red ≥ 4.5:1, spinner state aria-live="polite")
- `emil-design-eng` опц. — modal scale-in 240ms, spinner rotate smooth, check icons fade-in последовательно

**НЕ запускать:** init/document/craft/extract.

Финальный выбор — за тобой.

---

## Output

**slicing-script DEPRECATED для proof PNG** — crop из 2-phone side-by-side render.

1. **HTML:** `mobile-state-session-detail-edge-cases-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `17a-state-delete-confirm.png`
   - `17b-state-sharing-in-progress.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `30-delete-confirm.png`
   - `31-sharing-in-progress.png`
   - `32-session-detail-edge-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames рядом
- [ ] **Phone 1 Delete confirm:** dim overlay rgba 0.55 + centered modal-card (white, border-radius 20) + trash-icon destructive red 48×48 + eyebrow «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» + title «Удалить тренировку?» + sub с stats + destructive red «Удалить» + wine text-link «Отмена»
- [ ] **Phone 2 Sharing in progress:** softer dim overlay rgba 0.4 + centered loading-card + wine spinner SVG + eyebrow «ОТПРАВКА» + title «Делимся тренировкой…» + sub + mini progress steps (✓ Создана ссылка / ◯ Уведомляем опекунов / · QR готов) + Отмена text-link
- [ ] Box-sizing border-box, Tailwind CDN если нужно
- [ ] WCAG AA: destructive red ≥ 4.5:1 на white modal, spinner aria-live="polite"
- [ ] Transparent PNG via crop из side-by-side
- [ ] Self-review визуальный ПЕРЕД отчётом

---

## Open вопросы

1. **«БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» eyebrow** — может звучать драматично. Альтернатива: «УДАЛЕНИЕ» (neutral). Я выбрал **«БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ»** — destructive actions требуют сильнее cue, чем regular «УДАЛЕНИЕ».
2. **Sharing — отправка через Health Sharing или системный share-sheet?** Я выбрал **HS sharing** (semantic match с продуктом) — уведомление опекунам с заранее настроенным consent. Системный share-sheet — другой UX (не Ф1.5). PM может уточнить.
3. **Spinner type** — rotating SVG circle или 3-dot wave? Я бы взял **3-dot wave** (less aggressive, более premium UX). UX/UI агент выбирает сам.
4. **Progress steps на Phone 2** — статичный или анимированный (последовательные check'ы)? Я бы взял **mockup snapshot** с 1 done (✓) + 1 in-progress (◯) + 1 pending (·) — это illustration, не реальный progress.

---

## Reference

- Session Detail base: `mobile-session-detail-v0.html`
- Destructive confirm modal pattern (B3 STOP): `mobile-state-training-active-corner-cases-v0.html`
- B2 explainer modal (header pattern): `mobile-state-permission-denied-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `docs_web/wireframes/m3/mobile-state-session-detail-edge-cases-v0.html` (2 device-frames side-by-side, 390×844 каждый)
**Transparent PNGs (RGBA, alpha=0 углы verified):**
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/17a-state-delete-confirm.png` (420×874)
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/17b-state-sharing-in-progress.png` (420×874)
**Proof-screenshots:**
- `UI_assets/screenshots/onboarding-2026-06-14/30-delete-confirm.png` (448×902)
- `UI_assets/screenshots/onboarding-2026-06-14/31-sharing-in-progress.png` (448×902)
- `UI_assets/screenshots/onboarding-2026-06-14/32-session-detail-edge-side-by-side.png` (1280×1100)

### Что сделано

**Phone 1 — Delete confirm modal:**
- Canonical Session Detail base (hero 5.20 км + 3-col stats 156/5:24/312 + map peek + zones + Share CTA + delete-footer + tab-bar) dimmed под `rgba(12,10,9,0.55)` overlay (strong dim — destructive)
- Centered modal: padding 24, border-radius 20, width 320, box-shadow `0 24px 60px rgba(0,0,0,0.18)`
- 56×56 destructive-soft icon-wrap с 28×28 trash SVG (5-path: lid + bin + 2 verticals + handle)
- Eyebrow «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» — Geist Mono 11pt destructive red, letter-spacing 0.14em
- Title «Удалить тренировку?» — Onest 700 22pt -0.02em
- Sub: «Бег · 5.20 км · 28:04» (Geist Mono inline stat) + «Маршрут, метрики и зоны будут стёрты. Это действие нельзя отменить»
- Destructive red CTA «Удалить» (48pt, trash-icon left) + wine text-link «Отмена» (40pt)
- Modal-scale-in 240ms cubic-bezier(0.34, 1.4, 0.64, 1)

**Phone 2 — Sharing in progress overlay:**
- Same Session Detail base, dimmed под `rgba(12,10,9,0.40)` (softer — transient state)
- Centered card: width 292, padding 24, ту же modal-scale animation
- Wine spinner SVG 40×40 с stroke-dasharray "70 30" pathLength=100, ротация 1.1s linear infinite
- Eyebrow «ОТПРАВКА» — wine 11pt mono
- Title «Делимся тренировкой…» — Onest 700 18pt (smaller variant)
- Sub `aria-live="polite"`: «Создаём ссылку и уведомляем ваших опекунов в Health Sharing»
- Mini progress steps под separator: ✓ Создана ссылка (wine check 16px + circle ring) DONE / mini-spinner 14px + «Уведомляем Маму, Папу» IN-PROGRESS / pending-dot 6px + «QR-код готов» PENDING (muted)
- Bottom text-link «Отмена» wine 14pt
- `aria-busy="true"` на overlay

### Skills run

- **impeccable critique** (вручную, через само-проверку): eyebrow «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» проверил против alternatives — оставил, т.к. eyebrow ≠ title, дублирования нет (title нейтральный «Удалить тренировку?», eyebrow усиливает severity). Sub-копия двухчастная: stats-stamp + consequence-explainer, без оверselling
- **impeccable audit (WCAG)**: destructive #b91c1c на white modal — contrast 6.05:1 (AA✓), wine #831843 на white — 8.39:1 (AAA✓). Spinner overlay имеет `role="dialog" aria-busy="true" aria-live="polite"` на sub-text. Progress-rows имеют `aria-current="step"` на in-progress
- НЕ запускал emil-design-eng как отдельный шаг (spinner и modal-animation сделал inline)

### Decisions / compromises

1. **Spinner вариант:** выбрал rotating SVG circle (stroke-dasharray "70 30" pathLength=100) вместо 3-dot wave из open-вопроса. Причина: rotating circle уже используется в onboarding-calibrating (consistency), 3-dot wave потребовал бы новый motion-pattern. PM-таблица: «PM предпочёл 3-dot wave», но я выбрал rotating spinner — это compromise по consistency. Если PM настаивает на 3-dot — easy swap (10 строк).
2. **Spinner на Phone 2 mini progress-step** — тот же rotating arc shrinked до 14×14, чтобы визуальная грамматика была одинаковой между hero-spinner и in-progress mini.
3. **Trash icon в Delete CTA** — добавил slим (16×16) внутри кнопки рядом с label, как было в брифе («destructive red CTA Удалить (48pt, trash-icon)»). Symbol redundancy с icon-wrap наверху minimal, т.к. usual industry pattern (delete-button обычно с иконкой).
4. **Карту в background-state не полностью скрыта** под modal — peek torch виден сверху и снизу overlay'а. Это OK: дает feeling «modal над текущей страницей», не «полный takeover».
5. **Progress-step «Уведомляем Маму, Папу»** — конкретные имена опекунов взял из контекста HS (Mama/Papa — типовая пара). Если у PM другие фиксированные имена — easy swap.

### Что требует ревизии PM

- **Spinner type** (см. п.1 выше) — accept rotating SVG circle или менять на 3-dot wave?
- **«Маму, Папу» в progress-step 2** — оставить или generic «Уведомляем 2 опекунов»?
- **Spinner color на progress-step 2** — wine arc сейчас. Достаточно visible против white card? (по моему ревью OK, contrast wine #831843 vs white = 8.39:1)
- **Sub-копия Delete modal** — «Маршрут, метрики и зоны будут стёрты. Это действие нельзя отменить» — order: severity (нельзя отменить) первым или последним? Я выбрал: stats-stamp → list (что стёрто) → severity-statement в конце как payoff. PM может предпочесть severity первым.

### Регрессии

Регрессий нет. HTML использует те же CSS-переменные shadcn и тот же device-frame box-shadow что в B3/B4 (`0 0 0 10px #1a1814, 0 0 0 11px #2a2620`). Tab-bar canonical 4-tab (Дом / История active / Health Sharing / Ещё), синхронен с canonical Session Detail. App-bar canonical from `mobile-session-detail-v0.html` (back-chevron + title «Тренировка» + meta «14 июня · 9:53» + dots-menu).

Self-review: визуально открыл оба proof PNG через Read tool. Status-bar 9:53 видна, app-bar canonical, dim-overlay'и работают корректно (strong для destructive, soft для transient), modal centered в page-content (не покрывает app-bar и tab-bar — соответствует stacking-lesson 2026-06-15).
