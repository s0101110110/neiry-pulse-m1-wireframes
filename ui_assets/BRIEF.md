# BRIEF: C4 — HRV first measurement celebration + Baseline ready transition · Neiry Pulse Ф1

**Дата:** 2026-06-16
**Заказчик:** PM (Костя)
**Контекст:** C3 закоммичено (`cdbdfd2`). Сейчас **C4** — две transitional screens после калибровки baseline (~48 ч после старта приложения): уведомление «Baseline готов» + celebration «Ваш первый HRV-замер».

**Цель:** закрыть emotional moment между калибровкой A3 (Baseline собирается ~36 ч) и регулярным мониторингом HRV detail (C1 Phone 2). Без celebration screen юзер не понимает что «закончилось — теперь можно полноценно использовать».

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-baseline-ready-first-hrv-v0.html`

---

## Источники правды

- **PRD v2.6 §8 AC-1.2:** «Home показывает baseline status (готов / собираем / не готов)»
- **AC-1.4 (контекст):** HRV отображается **только когда baseline ready**
- **Reference (existing):**
  - `mobile-onboarding-03-notifications-calibrating-v0.html` Phone 2 — Calibrating progress (что предшествует C4)
  - `mobile-onboarding-05-empty-states-v0.html` Phone 1 — Home empty (с placeholder baseline)
  - `mobile-state-end-of-session-bracelet-disconnect-v0.html` Phone 1 — End-of-session celebration pattern (confetti + hero)
  - `mobile-profile-hrv-detail-v0.html` Phone 2 — HRV detail (target screen после celebration)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 36** · BASELINE · READY NOTIFICATION»
- «**ЭКРАН 37** · HRV · FIRST MEASUREMENT REVEAL»

---

## Phone 1 · Baseline ready notification

**Назначение:** через ~36-48 ч после старта приложения (Day 2 утром) юзер открывает app → получает push «Baseline готов» → видит in-app celebration banner.

**Контекст:** light Bevel Home layout, но с **большим celebration banner сверху** замещающим обычный eyebrow + hero.

**Структура (сверху вниз):**

### Status bar + App-bar
- 9:48 / canonical Home app-bar (logo + bell + avatar КЛ)

### Big celebration card (top, 60-70% screen height)
- Full-width card light Bevel + wine soft bg `#fdf2f8` (warm)
- Padding 24-28px
- Border-radius 20
- **Subtle confetti SVG** в углах (6-8 wine particles)
- **Hero illustration center** — abstract «baseline ready» icon (concentric circles wine + center heart-pulse) ~80×80
- Eyebrow (mono uppercase wine 11pt): `ДЕНЬ 2 · УТРО`
- Title (Onest 700, 28-32pt foreground): «Ваш baseline готов!»
- Sub (Space Grotesk 15pt foreground, 2-3 строки):
  «Мы изучили вашу личную норму HRV за **36 часов**. Теперь будем показывать дельты — насколько вы сегодня отдохнули.»
- Stats inline (2 cells):
  - **СОБРАНО** «48 ч» (Onest 700 20pt + mono unit)
  - **ВАШ BASELINE** «47 ms» (Onest 700 20pt + mono unit)
- Primary CTA wine (full-width 48pt):
  - «Посмотреть первый замер» + arrow-right icon

### Home preview (под card, partial visible)
- Subtle peek of regular Home (HRV widget / Шаги / etc.) — dimmed slightly чтобы celebration был фокусом
- Tab-bar Дом active (canonical)

---

## Phone 2 · First HRV measurement reveal (celebration)

**Назначение:** юзер тапнул «Посмотреть первый замер» → попал на **dedicated reveal screen**. Видит свой первый HRV value с context.

**Структура:**

### Status bar + minimal app-bar
- 9:49 / close × top-right (skip → попадает в HRV detail C1 Phone 2)

### Hero block (centered, top zone)
- **Confetti SVG** (8 particles в углах, subtle fade-in 1.2s, wine + alert-orange + success-green mix)
- Eyebrow (mono uppercase wine 11pt): `ВАШ ПЕРВЫЙ ЗАМЕР`
- Hero number: **«52»** (Onest 700 128pt foreground, tabular-nums) + label «**ms**» (Space Grotesk 18pt muted, inline)
- Sub (Space Grotesk 14pt foreground): «Сегодня в 9:48»

### Context section (под hero)
- Card light Bevel, padding 16-20
- Title (semibold 14pt): «Что это значит»
- Sub (Space Grotesk 13pt foreground, 2-3 строки):
  «**52 ms** на **5 ms выше** вашего baseline (**47 ms**). Это хороший знак — нервная система отдохнула, готова к нагрузке.»
- Mini progress visual: horizontal scale from 30 ms (red-soft) → 47 ms (baseline marker) → 70 ms (green-soft) с **wine dot** at 52 (above baseline)

### Comparison section (под context)
- Section title (mono uppercase 11pt muted): `ВАШ ДИАПАЗОН`
- 3 stats inline (cards):
  - **ВЫ СЕЙЧАС** «52 ms» (wine, semibold)
  - **ВАШ BASELINE** «47 ms» (foreground)
  - **РАЗБРОС НОРМЫ** «±10%» (muted, mono)

### Actions row (bottom)
- Primary wine CTA: «Открыть HRV-экран» (full-width 48pt, arrow-right icon) → переходит в HRV detail (C1 Phone 2)
- Secondary text-link: «Понятно, спасибо» (wine 14pt, под CTA) → home

### **БЕЗ tab-bar** (modal-flow, transitional screen)

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих screens
- **Wine `#831843`** для primary actions / accent / hero number / baseline marker
- **Wine-soft `#fdf2f8`** для celebration card bg (Phone 1)
- **Success-green** для positive «выше baseline» indicator
- **Alert-orange** для negative «ниже baseline» (если delta negative, но в нашем case +5 ms — positive)
- **Subtle confetti** — 6-8 particles в углах, НЕ overdone (lesson B4 — серьёзные бегуны)
- **Box-sizing border-box** глобально
- **Tailwind CDN**
- **Header canonical:** Phone 1 — Home app-bar; Phone 2 — minimal с close ×
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (47, 48, 52, 36, ±10)
- **SVG icons** (НЕ emoji): heart-pulse, concentric-circles, arrow-right, close, confetti particles

---

## Skills

UX/UI агент — выбирай сам. Особое внимание к:
- Confetti не overdone (lesson B4)
- Hero number readable at arm's length (whoop principle)
- Compress padding превентивно (lessons C1/C2/C3)

`impeccable` если хочешь polish на celebration card hierarchy; `emil-design-eng` опц. для confetti animation timing.

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 2-phone side-by-side render.

1. **HTML:** `mobile-baseline-ready-first-hrv-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs:**
   - `23a-baseline-ready.png`
   - `23b-first-hrv-reveal.png`

3. **Proof:**
   - `51-baseline-ready.png`
   - `52-first-hrv-reveal.png`
   - `53-baseline-celebration-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames
- [ ] **Phone 1 Baseline ready:** Home app-bar + big celebration card (wine-soft bg + confetti + illustration + eyebrow «ДЕНЬ 2 · УТРО» + title «Ваш baseline готов!» + sub + 2 stats inline + CTA «Посмотреть первый замер») + Home preview под card + tab-bar Дом active
- [ ] **Phone 2 First HRV reveal:** close × + confetti + eyebrow «ВАШ ПЕРВЫЙ ЗАМЕР» + hero «52 ms» (Onest 128pt) + sub «Сегодня в 9:48» + context card «Что это значит» + mini progress scale 30-70 ms с baseline marker + comparison section (Вы сейчас / Ваш baseline / Разброс нормы) + actions wine «Открыть HRV-экран» + text-link «Понятно, спасибо» + БЕЗ tab-bar
- [ ] Confetti subtle (НЕ overdone)
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA contrast
- [ ] Transparent PNG via crop из side-by-side
- [ ] Self-review визуальный — открыть оба proof PNG

---

## Reference

- A3 Calibrating progress (предшествующий screen): `mobile-onboarding-03-notifications-calibrating-v0.html` Phone 2
- B4 End-of-session celebration (confetti pattern): `mobile-state-end-of-session-bracelet-disconnect-v0.html` Phone 1
- C1 HRV detail (post-celebration target): `mobile-profile-hrv-detail-v0.html` Phone 2

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-16
**HTML:** `docs_web/wireframes/m3/mobile-baseline-ready-first-hrv-v0.html` (1085 строк, файл существовал — провёл review-полировку)
**Transparent PNGs:**
- `screenshots/sliced-flow-v2-1-transparent-2026-06-14/23a-baseline-ready.png` (920×1840 @2x, RGBA, alpha=0 углы)
- `screenshots/sliced-flow-v2-1-transparent-2026-06-14/23b-first-hrv-reveal.png` (920×1840 @2x, RGBA, alpha=0 углы)

**Proof-screenshots:**
- `screenshots/onboarding-2026-06-14/51-baseline-ready.png` (860×1767 crop из SxS)
- `screenshots/onboarding-2026-06-14/52-first-hrv-reveal.png` (860×1767 crop из SxS)
- `screenshots/onboarding-2026-06-14/53-baseline-celebration-side-by-side.png` (2560×2200 @2x)

### Что сделано

**Phone 1 (Baseline ready notification):**
- Status bar 9:48 + Home canonical app-bar (Neiry Pulse logo wine pulse + bell + КЛ avatar)
- Celebration card: wine-soft bg `#fdf2f8`, padding 18×18, radius 20, subtle confetti 6 particles (wine + warning-orange staggered 200→500ms fade-in)
- Concentric circles + heart-pulse SVG icon 64×64 центрировано
- Eyebrow `ДЕНЬ 2 · УТРО` Geist Mono wine 10.5pt
- Title «Ваш baseline готов» Onest 700 26pt (без `!` — не cheesy)
- Sub 13.5pt с **bold** `36 часов`
- 2 stat cells «48 ч» / «47 ms» Onest 700 20pt, mono units
- Wine CTA «Посмотреть первый замер →» 46pt
- Home preview peek (opacity 0.4): HRV `—` placeholder + «ожидает первого замера», Шаги 1248
- Tab-bar canonical 4-tab (Дом active wine)

**Phone 2 (First HRV reveal):**
- Status bar 9:49 (+1 мин хронология после тапа CTA Phone 1)
- Minimal app-bar — только close × top-right (modal flow)
- Confetti 8 particles (wine + success-green + warning-orange) staggered 200→410ms fade-in
- Hero `52` Onest 700 **128pt** tabular-nums + `ms` 18pt mono inline
- Sub «Сегодня в 9:48»
- Context card «Что это значит» с inline-bold (52 ms / 5 ms выше / 47 ms)
- Mini scale 30→70 ms gradient (red-soft → green-soft) + baseline marker line (42.5%) + wine dot 16×16 with explanatory slide animation 600ms
- Comparison section `ВАШ ДИАПАЗОН` + 3 stat cells (Сейчас 52 ms wine / Baseline 47 ms / Норма ±10%)
- Wine CTA «Открыть HRV-экран →» + text-link «Понятно, спасибо»
- БЕЗ tab-bar (modal-flow)

### Skills run

**`impeccable` critique (вручную applied — skill не загружен в текущем cwd, использовал руководство):**
- Confetti не overdone (lesson B4 respected): 6+8 particles, max opacity 0.78-0.85, restrained sizes 4-7px
- Hero `52` 128pt — читается «at arm's length» (whoop principle confirmed на 860px render)
- Cards рестрейн: один accent (wine) per screen, contrast WCAG AA на body text
- **Найденный дефект:** Home preview HRV widget показывал `47 ms` (= baseline value) — семантически некорректно (это значение появится только после первого замера). **Fix:** заменил на `—` placeholder + sub «ожидает первого замера» (var(--border-strong)) — теперь preview честно отражает pre-reveal state

**`emil-design-eng` motion review:**
- Все transitions specify exact properties (`transform 160ms cubic-bezier(0.23, 1, 0.32, 1), background 160ms ease`) — не `all`
- Hero number entrance: NOT scale(0), а translateY(8px) + scale(0.96) → scale(1) — natural materialization
- Strong ease-out curve `cubic-bezier(0.23, 1, 0.32, 1)` на UI motion (не дефолтный ease-out)
- Confetti stagger 60ms apart (emil rule 30-80ms) — cascading, не uniform reflex
- Button `:active { transform: scale(0.97) }` присутствует
- `dot-slide` 600ms ease-in-out — explanatory motion (baseline → current), seen rare → can be longer
- `@media (prefers-reduced-motion: reduce)` cleanly disables motion (confetti remains visible opacity 0.78, dot static at 55%)

### Decisions / compromises

1. **Preview HRV peek = `—` placeholder, не `52`** — избегаем spoiler hero, корректна semantic «before first measurement reveal»
2. **Confetti subtle restraint** — 6 на Phone 1 (compact card), 8 на Phone 2 (full hero zone) — НЕ flood 20+ как cheesy SaaS celebration
3. **«Понятно, спасибо» text-link, не secondary button** — modal flow доминанта single primary action (Открыть HRV-экран)
4. **Mini scale 30-70 ms** — gradient red-soft → green-soft передаёт «низ = плохо, верх = хорошо» без verbose legend
5. **`px scaling factor=2`** в render — для retina-готовых PNG (более чёткое чтение на macOS Preview)
6. **HTML файл уже существовал** в репо (1085 строк) — не пересоздавал с нуля, провёл targeted polish + re-render

### Что требует ревизии PM

- **Hero number 128pt** — может быть «слишком крупный» для PM-видения. Easy revert to 112pt если нужно
- **Mini scale ширина** на Phone 2 — растянут на всю card. Можно сжать с side-padding если в визуальной композиции хочется уже
- **Text-link «Понятно, спасибо»** — может быть «Не сейчас» более нейтрально (без gratitude tone)

### Регрессии

- Нет. HTML файл уже существовал — изменения: только семантический fix preview HRV value (47 → `—` + объяснение). Все остальные элементы (confetti pattern, hero, scale, stats, CTAs) сохранены byte-for-byte.
