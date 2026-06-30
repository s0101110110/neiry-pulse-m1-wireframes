# Anti-Generic Design Playbook — Neiry Pulse / bevel-clone

> **Назначение:** исполнимый пайплайн, который системно производит «рукотворный», не-generic UI.
> Заземлён на 4 пункта критики команды (01.07.2026). Каждая стадия закрывает конкретный симптом,
> имеет владельца-роль и точный скилл с аргументами.
> **Источник:** `docs_web/docs/superpowers/research/2026-07-01-anti-generic-research-report.md`
> **Читать UX/UI-агенту перед любой дизайн-задачей bevel-clone.**

---

## 0. Рекомендуемый стек скиллов (установить / импортировать)

| Слой | Скилл | Действие | Зачем |
|---|---|---|---|
| Baseline | **frontend-design** (Anthropic, official) | установить `/plugin install frontend-design` | банит generic-шрифты/градиенты на уровне постановки. Первый слой под всё. |
| Каркас вкуса | **taste-skill** (Leonxlnx) | **импортировать SKILL.md-правила** сюда, не ставить слепо | диалы VARIANCE/DENSITY, «no 3 equal cards», Brief Inference. Override: разрешить 3+ радиуса. |
| Цвет | **oklch-skill** | установить | wine #831843 → перцептивная шкала без «мути» HSL. |
| Финишный deslop | **interface-design** (Dammyjay93) | `npx skills add Dammyjay93/interface-design` | `design-deslop` — срез AI-tells перед каждым показом PM. |
| Кандидат на ядро | **ui-craft** (educlopez) | испытать на 1 экране | детерминированные гейты (score/lint), durable brief/tokens. |
| Наш арсенал | `redesign-existing-projects`, `impeccable`, `high-end-visual-design` | уже есть — **вызывать системно** | лучший фит под существующий код + AI-slop-test + variance. |
| Вторичный QA | **UX UI Pro Max** | держать reasoning-таблицу как pre-flight | accessibility/touch/charts. НЕ лекарство от generic. |

**Принцип-фундамент (из методологии):** **Reference-grounding превыше prose.** Никогда «сделай премиально» — всегда скриншот реального референса (Bevel из `screenshots/references/`) → конкретные токены и правила.

---

## 1. Стадия Intent & Taste-target · владелец: PM + дирижёр · лечит: вход (гасит generic)

- PM пишет бриф в `UI_assets/BRIEF.md` (что за экран, цель, защищённые элементы).
- **frontend-design:** зафиксировать 4 решения ДО пикселей — purpose / tone / constraints / **differentiation**.
- **taste-skill Brief Inference:** one-line read «page kind / audience / vibe».
- **Выбрать taste-target** — конкретный Bevel-реф из `screenshots/references/` как эталон композиции.
- Выставить диалы под тип экрана: home/hero = `VARIANCE 8`; settings/таблицы = `VARIANCE 4 + DENSITY 7`.

## 2. Стадия Composition-first · владелец: UX-агент · лечит: «нарушена композиция»

- **`/shape` (ASCII-wireframe ДО кода)** или эскиз — ломает дефолтную центрированную сетку до первого div.
- Заложить **ритм плотности** (по Bevel): доминантный блок → **prose insight-пауза** → плотная сетка. Запретить «hero → сразу 6 близнецов».
- `Skill high-end-visual-design` через BRIEF: Variance Mandate + Asymmetrical Bento (одна featured-ячейка span-2 + мелкие).
- **Опционально Stitch** (только если нужен быстрый старт композиции): сгенерить 4-6 вариантов → §Stitch-протокол ниже.
- Заголовки секций — **однострочные** (убрать ручной `<br/>` L557), eyebrow uppercase +0.6px трекинг.

## 3. Стадия Bespoke components · владелец: UX-агент · лечит: «типовые компоненты»

- `Skill redesign-existing-projects args:"audit and fix bevel-clone/home/home-main-etalon.html + shared/components.css + tokens.css"` — Scan→Diagnose→Fix по нашему стеку.
- **Построить ≥3 не-капсульных viz-примитива** в `components.css` (главный фикс симптома #1):
  - `.bv-ring-gauge` — SVG-кольцо r=44, stroke 8, gradient-дуга, hue от semantic-токена;
  - `.bv-sparkline` — polyline + полупрозрачная normal-range полоса `color-mix(--bv-sem-norm 12%)`;
  - `.bv-battery-bar` — горизонтальные дискретные палочки 3×16px с порогом.
- **Правило:** запретить рендер одного индикатора подряд >2 раз на экране.
- `Skill high-end-visual-design` Double-Bezel для глубины. Перевести HRV hero с вертикальной капсулы на ring-gauge/area-sparkline.

## 4. Стадия Color & hand-crafted detail · владелец: UX-агент · лечит: «поганый wine» + «не рукотворный»

- **Wine:** `oklch-skill` → wine #831843 в перцептивную шкалу. **Вынести из chrome** (см. §Канон). `redesign` color-audit: один accent, saturation <80%.
- **Цвет — в данные:** chrome ахроматичен (#F0F0F4/#FFF/near-black, **чёрные** active/CTA), хроматика только в метриках/графиках. 1 тёплая + 1 холодная семантическая шкала + sleep-индиго.
- **Границы → тени:** убрать `border 1px #E5E5EA` с карт на светлом фоне → диффузная 2-слойная тень `0 1px 2px rgba(22,22,32,.04), 0 8px 24px rgba(22,22,32,.06)`.
- **Контекстные радиусы** (вместо одного 20px): `--bv-r-card-lg 26px` (hero/ring/insight) · `--bv-r-card 20px` (bento) · `--bv-r-card-sm 14px` (вложенные/timeline) · pill 999px (чипы/табы).
- **Рукотворность:** легализовать **градиенты** в дугах колец и иконках; добавить **`.bv-insight-card`** (emoji + headline + 2-3 строки прозы, напр. «Спокойный день — нервная система отдыхала»); **фирменная сигнатура** — persistent bottom-bar «Спросить Pulse» с blob-аватаром над nav; объёмные градиентные статус-иконки вместо плоского lucide stroke 1.7.

## 5. Стадия Anti-generic gate · владелец: UX-агент / критик · лечит: ловит generic ДО глаз PM

- `Skill impeccable args:"critique <path>"` — **AI slop test**: если можно сказать «AI made that» → провал. Возвращает P0/P1 бэклог.
- `Skill interface-design:design-deslop` — diff-scoped срез AI-tells (generic-токены, дефолтная типографика, identical cards, missing states).
- **Скоринг против диагностики:** прогнать по 12-пунктовому anti-generic чеклисту (§ниже) + side-by-side с выбранным Bevel-рефом.
- **Условие петли:** если ≥2 пункта чеклиста проваливаются — назад на стадию 3/4. Не показывать PM, пока gate не пройден.

## 6. Стадия Proof & acceptance · владелец: дирижёр + PM

- (Опц.) UX UI Pro Max pre-flight: accessibility 4.5:1 / touch 44px / tabular-figures.
- Транспарентный proof PNG (правило mockup-format) **side-by-side с Bevel-рефом**.
- Показать PM с **прямым путём последней строкой** (правило visual-path).
- **PM acceptance gate:** задача НЕ закрыта без явного «принято».

---

## Anti-generic чеклист (12 правил — прогонять на стадии 5)

1. Запретить единый radius — ≥3 контекстных (26/20/14 + pill).
2. ≥3 не-капсульных viz-примитива (ring/sparkline/stacked-bar). Один индикатор ≤2 раз подряд.
3. Убрать 1px hairline с карт на светлом фоне → диффузная тень без обводки.
4. Wine вне chrome — active/CTA нейтрально-тёмные.
5. Цвет живёт в данных — chrome ахроматичен, 1 тёплая + 1 холодная шкала, без 4-й бордовой hue.
6. Иерархия плотности: доминанта → prose-пауза → сетка. Не hero→6 близнецов.
7. Фирменный элемент (persistent «Спросить Pulse» / голос продукта).
8. Иконки с характером — объёмные/градиентные для статусов, не дефолтный lucide.
9. Трекинг: заголовки однострочные, uppercase eyebrow +0.6px (без ручного `<br/>`).
10. Асимметрия в bento — одна featured + мелкие, не 6 идентичных 122px.
11. Легализовать мягкие градиенты (дуги колец, статус-иконки). 0 градиентов = плоско.
12. Dark Sleep — слоистый navy с цветными REM/Core/Deep, не механический инверс.

## Bevel-токены (эталон, confidence HIGH)

```
Фон app:        #F0F0F4 / #F2F2F5 (cool-grey)   Карта: #FFFFFF
Текст:          #0A0A0A / #111   Вторичный/юнит: #9AA0A6
Active/CTA:     #000000 (НЕ wine)
Strain/тёплый:  #FFB020 → #FFC400      High/коралл: #FF6B5C / #FF5A4D
Recovery/лайм:  #7ED321 → #5FB100      Low-stress:  #34C0A0
Sleep/REM:      #4F6BFF → #9AA8FF      Trend-сигнал: #FF8A3D
Тень карты:     0 8px 24px rgba(0,0,0,.06), БЕЗ border
Радиусы:        pill 24-28 · карта 20-24 · CTA 32 · иконка-таблетка 16-18
Eyebrow:        uppercase tracking +0.6px
Dark Sleep:     фон #0E1320/#141A2D, карта #1B2236
Шрифт:          единый grotesque, числа тем же шрифтом extra-bold (Bevel БЕЗ отдельного mono)
```

## 6 потерь клона → фиксы (из Потока E, полностью в research/raw/E.json)

1. **Viz-словарь** (1 примитив ×7) → построить ring/sparkline/battery-bar.
2. **Wine в chrome** → `.bv-nav-item.is-active` color `--bv-ink`, не wine.
3. **Hairline-бордеры** → `border: none` + диффузная тень.
4. **Единый радиус 20px** → 3 контекстных.
5. **Hero→6 близнецов** → ритм доминанта→insight-проза→сетка.
6. **Нет сигнатуры/градиентов** → «Спросить Pulse» bar + градиенты + emoji-проза.

## ⚠️ Канон под вопрос (решение PM — см. отчёт §7)

- **Wine в chrome** → research рекомендует вынести (противоречит memory `project_neiry_bevel_clone_header_footer_canon`). **Ждёт решения PM.**
- **Pulse Mono для чисел** → Bevel намеренно без mono. Мягкая точка для обсуждения, не мандат.

## Stitch-протокол (если используется на стадии 2)

1. UX-агент → Stitch-промпт с **явными якорями** (cool-grey #F0F0F3, semantic в контенте, wine только brand-anchor, Golos Text + Pulse Mono).
2. Генерация 4-6 вариантов (Experimental/Gemini-Pro, можно подложить транспарентный реф).
3. **TASTE-отбор** по 4 симптомам → оставить 1-2. Stitch-вариант = болванка, не финал.
4. Мост: ZIP-экспорт → плагин **html.to.design** (НЕ нативный Paste-to-Figma — отваливается на Gemini-Pro).
5. **Figma-детокс через MCP:** `get_design_context` → `use_figma` пересобрать на наших bv-компонентах → `search_design_system`/`get_variable_defs` сверить токены → убрать wine из контента.
6. **Код Stitch выбрасываем** — берём только композицию. Код рождается из вычищенного Figma.

## Роли

| Стадия | PM | UX-агент | Дирижёр |
|---|---|---|---|
| 1 Intent | бриф, выбор taste-target | — | формулировка, taste-target |
| 2-4 Build | — | вся генерация/компоненты/цвет/детали | брифинг скиллов |
| 5 Gate | — | прогон critique-скиллов | enforcement gate |
| 6 Proof | **acceptance** | proof PNG | сборка, показ с путём |
