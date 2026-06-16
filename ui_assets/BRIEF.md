# BRIEF: C3 — Sleep detail view + Sleep explainer modal · Neiry Pulse Ф1

**Дата:** 2026-06-16
**Заказчик:** PM (Костя)
**Контекст:** C2 закоммичено (`3b71c0a`). Сейчас **C3** — Sleep detail view (по аналогии с HRV detail, но для сна) + Sleep explainer modal.

**Цель:** закрыть Sleep tracking screens — параллельно HRV pattern, но с дисклеймером «демо-режим» (PRD v2.6 §3 Ф1 «Sleep — демо-режим с дисклеймером»).

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-sleep-detail-v0.html`

---

## Источники правды

- **PRD v2.6 §3 Ф1 (Скоуп):** «Sleep — демо-режим с дисклеймером»
- **PRD v2.6:** Sleep НЕ полноценный production-feature в Ф1 — это **demo для investor / pilot demo**. Должен быть **видимый дисклеймер** «Демо-режим. Реальное измерение сна — Ф2.»
- **Reference (existing):**
  - `mobile-profile-hrv-detail-v0.html` Phone 2 — HRV detail (canonical pattern для chart + insight + 3-metric strip)
  - `mobile-profile-hrv-detail-v0.html` Phone 3 — HRV explainer modal (canonical pattern для bottom-sheet explainer)
  - Whoop competitive: `knowledge-base/competitive-design/whoop.md` (Sleep phases visualization)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 34** · SLEEP · DETAIL VIEW»
- «**ЭКРАН 35** · SLEEP · EXPLAINER MODAL»

---

## Phone 1 · Sleep detail view (whoop-style, demo-mode)

**Назначение:** юзер тапнул Sleep widget на Home → попал в detail view. Видит quick stats прошлой ночи + chart 7 ночей + breakdown по фазам + явный дисклеймер demo-mode.

**Структура (сверху вниз):**

### Status bar + App-bar
- 9:55 / back-chevron «‹» + title «Сон» (centered) + ⓘ info-icon SVG top-right (tap → opens Phone 2 explainer modal)

### Demo-mode banner (top, прямо под app-bar)
- **Sticky info-banner** (alert-soft `#fdf3e1` bg + border-left 4px alert-orange `#d97706`)
- Padding 10-12px
- info-icon SVG (alert-orange ~16) + text (Space Grotesk 12pt foreground):
  «**Демо-режим.** Реальное измерение сна появится в обновлении.»
- (НЕ убираемый — info-only, без actions)

### Hero block (centered, top zone)
- Eyebrow (mono uppercase wine 11pt): `ПРОШЛАЯ НОЧЬ`
- Hero number: **«6 ч 42 мин»** (Onest 700 64-72pt foreground, tabular-nums)
- Sub-label: «**87%** качество сна» (semibold 14pt + wine background pill)
- Delta strip: «**+22 мин** к среднему за неделю» (mono 12pt success-green)

### Sleep phases breakdown (под hero)
- Section title (mono uppercase 11pt muted): `ФАЗЫ`
- **Horizontal stacked bar** (height ~40px, full-width, border-radius 8):
  - REM segment: ~20% width, primary wine
  - Light sleep: ~55% width, wine-soft
  - Deep sleep: ~25% width, wine-deep `#4c1f33`
- **Legend под bar** (3 cells inline):
  - 🔴 REM **1 ч 22 мин** (20%)
  - 🟣 Поверхностный **3 ч 41 мин** (55%)
  - 🟢 Глубокий **1 ч 39 мин** (25%)

### 7-night chart (whoop-style, мини)
- Container: light Bevel card, padding 16, border-radius 16
- Title row: `7 НОЧЕЙ` (mono uppercase 11pt muted)
- Chart area: height ~100px
- **Y-axis:** 3 ticks (~4ч / ~7ч / ~10ч)
- **X-axis:** 7 ticks (Пн / Вт / Ср / Чт / Пт / Сб / **Вс** today highlighted)
- **Bar chart:** 7 wine bars (опц., можно line с dots — на выбор UX/UI агента, pick simpler)
- **Today's bar/dot:** larger, wine-filled, с tooltip «6 ч 42 мин»

### Insight card (контекстная рекомендация)
- Card light Bevel + wine accent border-left 3px
- Icon: moon SVG (wine, 20×20)
- Title (semibold 14pt): «Хороший сон»
- Sub (Space Grotesk 13pt foreground, 2 строки):
  «Качественное восстановление. REM-фаза в норме. Можно повышенную нагрузку.»

### Bottom (text-link)
- «Узнать больше про сон» (wine text-link 14pt, ⓘ icon) → opens Phone 2 modal

### Tab-bar
Дом (active wine) / История / Health Sharing / Ещё — canonical

---

## Phone 2 · Sleep explainer modal-overlay (поверх Phone 1)

**Назначение:** юзер тапнул ⓘ icon в app-bar или text-link «Узнать больше про сон» — видит **bottom-sheet** с объяснением что такое sleep tracking, фазы, дисклеймер.

**Контекст:** Phone 1 visible сверху + semi-transparent overlay rgba(12, 10, 9, 0.45) + bottom-sheet card 75% screen.

**Структура:**

### Background (dimmed Phone 1)
- Phone 1 layout visible но dimmed

### Bottom-sheet (75% screen)
- Background: white card
- Border-top-radius 24px
- Padding 20-24px, padding-bottom 32
- Sheet handle на top (40×4px rounded, muted-grey)
- Close × top-right

### Header section
- Eyebrow (mono uppercase wine 11pt): `КАК ЭТО РАБОТАЕТ`
- Title (Onest 700 22pt foreground): «Как мы измеряем сон»

### Explainer body (2 параграфа)
- Para 1 (Space Grotesk 14pt foreground, line-height 1.5):
  «**В Ф1 это демо-режим.** Сейчас показываем средние значения из научных данных, чтобы вы понимали, как будет работать функция.»
- Para 2:
  «**С обновления** браслет начнёт измерять ваш реальный сон через motion-sensor + HRV. Фазы (REM / Поверхностный / Глубокий) определятся по комбинации HR + движения.»

### «Фазы сна» section (3 bullets)
Section title `ЧТО МЫ ИЗМЕРЯЕМ` (mono uppercase 11pt muted):
- 🔴 **REM** — фаза сновидений, восстановление мозга
- 🟣 **Поверхностный** — переход между фазами, лёгкое пробуждение
- 🟢 **Глубокий** — физическое восстановление, рост гормонов

### Divider thin border

### Disclaimer (повторение demo-mode)
- Sub (12pt muted, 2 строки):
  «**Не медицинский диагноз.** Если стабильно плохой сон — обратитесь к врачу. Полноценный sleep tracking — следующее обновление.»

### Primary CTA wine
- Full-width 48pt: «Понятно»
- Wine primary

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих screens
- **Wine `#831843`** для primary CTA / chart bars / quality pill / accent
- **Wine-soft** для Light sleep segment
- **Wine-deep `#4c1f33`** для Deep sleep segment (визуальная глубина → ассоциация с deep)
- **Alert-orange `#d97706`** для demo-mode banner accent
- **Alert-soft `#fdf3e1`** для banner bg
- **Success-green `#65a30d`** для positive delta (+22 мин)
- **Box-sizing border-box** глобально
- **Tailwind CDN** включён
- **Header canonical** back-chevron + title-bar
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (6 ч 42 мин, 87%, 1 ч 22 мин, +22 мин, 4ч/7ч/10ч)
- **SVG icons** (НЕ emoji): moon (crescent), info-circle, chevron-right, close, info-banner

---

## Skills

UX/UI агент — выбирай сам. Особое внимание к:
- Demo-mode banner НЕ слишком intrusive (subtle alert-orange, не destructive red)
- Sleep phases bar — proportions visualHints читаемы
- Compress padding превентивно (lessons C1 + C2)

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 2-phone side-by-side render.

1. **HTML:** `mobile-sleep-detail-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs:**
   - `22a-sleep-detail.png`
   - `22b-sleep-explainer-modal.png`

3. **Proof:**
   - `48-sleep-detail.png`
   - `49-sleep-explainer-modal.png`
   - `50-sleep-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames
- [ ] **Phone 1 Sleep detail:** back + «Сон» + ⓘ + demo-mode banner alert-orange + hero «6 ч 42 мин» + quality pill 87% + delta strip + sleep phases stacked bar + 3-cell legend (REM / Light / Deep) + 7-night chart + insight card + text-link + tab-bar
- [ ] **Phone 2 Sleep explainer modal:** Phone 1 dimmed + bottom-sheet 75% + eyebrow + title «Как мы измеряем сон» + 2 paragraphs + 3 фазы bullets + disclaimer demo-mode + wine CTA «Понятно»
- [ ] Demo-mode banner присутствует и читается чётко
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA contrast
- [ ] Transparent PNG via crop из 2-phone side-by-side
- [ ] Self-review визуальный — открыть оба proof PNG, проверить compactness

---

## Reference

- HRV detail pattern (для Sleep mirror): `mobile-profile-hrv-detail-v0.html` Phone 2
- HRV explainer modal pattern: `mobile-profile-hrv-detail-v0.html` Phone 3
- Demo-mode банер pattern: `mobile-state-bt-disconnect-charging-low-v0.html` B1 alert-orange
- Whoop sleep phases: `knowledge-base/competitive-design/whoop.md`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:**
**HTML:**
**Transparent PNGs:**
**Proof-screenshots:**

### Что сделано

### Skills run

### Decisions / compromises

### Что требует ревизии PM

### Регрессии
