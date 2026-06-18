# UX TASK BRIEF — 3 exploration-варианта мобильного дизайна (одинаковый Home экран в 3 направлениях)

**Дата:** 2026-06-18
**От:** PM (Константин)
**Приоритет:** СРЕДНИЙ — exploration, не финальный артефакт. Цель — дать PM визуально выбрать направление для следующего витка.

---

## Контекст

`DESIGN-preview.html` принят PM и закоммичен (commit 0436a9f). PM считает что текущий дизайн **выглядит скучно** и просит развернуть **3 трендовых направления** редизайна на одном и том же экране (Home), чтобы наглядно сравнить.

Это **только sketches** — не production, не overlay в `DESIGN.md`. Просто визуальное предложение, на основе которого PM выберет, в каком направлении двигаться дальше.

---

## Файл вывода

**Новый файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/DESIGN-explorations.html`

НЕ трогать существующие: `DESIGN.md`, `DESIGN-preview.html`, `font-pairs-comparison.html`, `ui-kit.html`.

---

## Что рендерим

**3 phone-мокапа одного и того же экрана (Home, светлая тема, основан на `01-home.png`)** — рядом в одном ряду. Каждый мокап подписан буквой варианта (B / C / D) + одно-предложение описание.

Базовый контент во всех трёх (чтобы сравнение было apples-to-apples):
- Status bar 9:41
- App header «Pulse» + bell + avatar КЛ
- HRV-секция: 47 ms + «+12% к вчера» + body «Вы набираете форму…»
- Workout-секция: «Сегодня лёгкий бег» + sparkline + CTA «Начать тренировку» + ghost «Подробнее»
- Sleep row: «Сон прошлой ночью» + 7ч 42м + 22%/15%/63%
- Bottom nav: Дом / История / Sharing / Ещё

Контент тот же, **визуальная подача — разная** под каждый вариант.

---

## ЗАМКНУТЫЕ КОНСТАНТЫ (НЕ ТРОГАТЬ ни в одном варианте)

- ❌ **Шрифты:** только Golos Text + JetBrains Mono. **Никаких новых шрифтов**, никакого serif, никакого italic accent от других семейств. Italic в JetBrains/Golos — можно, новые family — НЕЛЬЗЯ.
- ❌ **Wine `#831843`** — единственный chromatic accent во всех 3 вариантах.
- ❌ **Light-mode primary** для всех 3 мокапов.
- ❌ **4px grid base.**
- ❌ Bio-палитра (low/mid/high) — те же HEX из AA-safe набора (`#00A653` / `#E89500` / `#D1003C`).

Эти константы — фундамент. Варианты исследуют ДРУГИЕ оси: моушн, размерность, плотность.

---

## ВАРИАНТЫ — направления

### Вариант B — «Bio-Spatial / Kinetic»

**Идея:** живой интерфейс. Данные дышат, карточки имеют глубину, ощущение мониторинга жизни.

**Конкретные приёмы:**
- **Pulse-breathing анимация** на hero HRV-метрике (47 ms): `@keyframes` ~4s loop, `transform: scale(1) ↔ scale(1.015)`, ease-in-out infinite. Subtle, не отвлекает.
- **Depth на карточках:** многослойная тень — `box-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 8px 24px rgba(131,24,67,0.06);` + inset highlight сверху `inset 0 1px 0 rgba(255,255,255,0.9)`.
- **Ambient color zone:** общий фон мокапа имеет очень тонкий gradient — `linear-gradient(180deg, #FAFAF7 0%, #FFF8FA 100%)` (микро-розовый снизу) или равноценный по тонкости.
- **Depth-ring для NSI:** SVG-кольцо с `radialGradient` или `linearGradient` (mint → light-mint) вместо solid stroke. Эффект «3D».
- **Apple Watch-like overlapping rings** на home — три rings (HRV / Sleep / Activity), перекрывающиеся, единый виджет. Уникальная Neiry-фишка.
- **ECG-pulse в фоне** hero-карточки — micro-анимация sin-волны 1px stroke в `opacity: 0.08`, едва видна, ощущается как «прибор живой».
- **Tactile button-press**: на `:active` кнопке `transform: scale(0.97)` 160ms ease-out (можно реализовать через :active в CSS).

**Чувство:** живой, премиальный, медицинский с пульсом.

### Вариант C — «Bold Expressive» (Apple Vision / Numi-inspired)

**Идея:** одна метрика — главная. Всё остальное даётся минималистично, шепотом. Огромная типографика, generous breathing room.

**Конкретные приёмы:**
- **HUGE hero metric:** `47` рендерится **96-128px** (на 280px ширине phone) JetBrains Mono 500/600. `ms` маленьким (12-14px) рядом.
- **Heavy display headlines:** Golos Text **weight 800-900**, letter-spacing -3 to -4px. «Сегодня лёгкий бег» становится **40-48px**, не 17px.
- **Generous whitespace:** между секциями 32-48px (не 8-12px). Карточки воздушны.
- **Cut content for breathing room:** возможно убрать warning row или sleep row, чтобы hero получил **половину экрана**. Радикальная редакция.
- **One-screen-one-message:** доминантная иерархия. Глаз сразу падает на HRV-метрику, остальное — peripheral.
- **Minimal chrome:** без borders на карточках. Только тонкие dividers (1px на 8% opacity).
- **Mono для метрик + Golos для всего остального** — контраст резкий: всё либо «слова» (Golos), либо «числа» (Mono).

**Чувство:** премиум-fashion, Apple Vision Pro, журнальная обложка.

### Вариант D — «Brutalist Precision» (counter-Bevel)

**Идея:** инженерная честность. Hyper-density, JetBrains Mono **всюду**, sharp edges, без украшений. Чувство — медицинский прибор / терминал.

**Конкретные приёмы:**
- **JetBrains Mono ВЕЗДЕ:** body, headings, captions, brand. Только числа и текст — единый mono голос.
- **Sharp corners:** `border-radius: 0` или максимум `2px`. Никаких 12-16px rounded.
- **Hard 1px-1.5px borders:** карточки = прямоугольники с `border: 1px solid #1A1815` (почти чёрный).
- **Higher density:** показать БОЛЬШЕ данных. Например, развернуть HRV-метрику с дельтами, статистикой, временем измерения. Не «47 ms», а «47 ms · 2026-06-18 09:48 · Δ +5 vs avg · base 42».
- **Terminal-style separators:** `===` / `---` / `// ` иногда между блоками для эстетики «прибор».
- **Color: только wine + black + white**, минимум warmth. Bio-палитра ужесточена.
- **Grid lines visible:** subtle 1px lines на разделах.
- **Uppercase labels:** все labels (HRV СЕГОДНЯ, ГОТОВЫ ТРЕНИРОВАТЬСЯ, СОН) — uppercase с tracking +0.6-0.8px.

**Чувство:** медицинский прибор, инженерная честность, hyper-precision.

---

## Технические требования

- 3 phone-мокапа в одном ряду (или 1×3 column на узком экране), внутри `<section>` страницы.
- Phone bezel: `#1A1815`, border-radius 32-36px (в **варианте D** — снизить до 12px, чтобы матчить brutalist).
- Каждый мокап = ширина ~300-340px, высота ~600-680px.
- Подпись над каждым мокапом: буква варианта (большая) + одно-предложение описание.
- Под мокапами — короткая 2-3 строки таблица: что меняется по сравнению с baseline DESIGN-preview.html (типографика / motion / density / chrome).
- Hero страницы: «3 направления редизайна — выбираем тон» + контекст что это exploration.

---

## Контрольный список

- [ ] Шрифты только Golos Text + JetBrains Mono (grep verify — ни Source Serif, ни Newsreader, ни Inter, ни Manrope)
- [ ] Wine `#831843` — единственный chromatic accent (grep verify hex codes)
- [ ] Все 3 мокапа на light bg (не dark)
- [ ] 4px grid соблюдён в B и C; в D — допустимо нарушать ради brutalist (специально пометить в комментарии CSS)
- [ ] `font-variant-numeric: tabular-nums` на живых метриках
- [ ] Pulse-breathing анимация в варианте B видна (но subtle, не раздражает)
- [ ] Huge hero metric в варианте C (≥96px)
- [ ] Mono `font-family` на body в варианте D (grep `font-family.*JetBrains` в variant-d секции)
- [ ] Не сломаны существующие файлы DESIGN-preview.html / DESIGN.md / ui-kit.html / font-pairs-comparison.html

---

## Skills (рекомендую использовать)

- **`Skill redesign-existing-projects`** — основной для всех 3 вариантов. Цель: перерисовать тот же блок (Home) в трёх разных направлениях БЕЗ потери ДНК (wine, Golos+JetBrains, light-bg, 4px grid в B/C).
- **`Skill emil-design-eng`** — для варианта B (моушн: pulse-breathing, ambient-bg gradient, depth-rings, tactile button-press). Запрос: длительности, easings, как избежать дёргания tabular-nums при scale animation.
- **`Skill impeccable polish docs_web/DESIGN-explorations.html`** — финальный pass перед докладом, если останется время.

**Хард-баны:** `init`, `document`, `craft`, `extract`, `live`, `pin`, `overdrive`. `impeccable` без аргумента — НЕ вызывать.

**Если skill советует:**
- Поменять wine — игнорировать (REJECTED_BY_AGENT)
- Добавить serif/новый шрифт — игнорировать
- Сделать dark-mode — игнорировать
- Использовать «warmer palette» — игнорировать

---

## Ожидаемый выход

1. Новый файл `docs_web/DESIGN-explorations.html` (НЕ trogaть DESIGN-preview.html)
2. Screenshot в чат PM
3. Доклад:
   - `DONE` / `DONE_WITH_CONCERNS` / `NEEDS_CONTEXT` / `BLOCKED`
   - Какие skills вызывал и для чего
   - REJECTED_BY_AGENT — если skill советовал ерунду
4. **НЕ КОММИТИТЬ** до явного «принято» от PM

---

## Дедлайн

Не критичный. Желательно сегодня.

---

## Что PM сделает после получения

Посмотрит 3 варианта. Выберет 1 (или комбо из 2). После выбора — следующая задача: применить выбранное направление ко всем 4 экранам из DESIGN-preview.html. **Это уже отдельная задача**, не для этого брифа.
