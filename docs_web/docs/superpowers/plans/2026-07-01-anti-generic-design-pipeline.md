# Anti-Generic Design Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **NB — это research/synthesis-план, не код.** TDD-шаги «failing test» заменены на
> **verify-шаги по содержимому артефакта** (artifact contains X). Каждая задача
> производит markdown-артефакт. Коммиты — после каждой задачи.

**Goal:** Провести diagnostic-first research по внешним дизайн-скиллам (taste, UX UI Pro Max), Stitch и нашему арсеналу, и синтезировать исполнимый Anti-Generic Design Pipeline, заземлённый на 4 пункта критики команды.

**Architecture:** Diagnostic (Поток 0) → barrier → 6 параллельных research-потоков (A–F) → adversarial-верификация находок → синтез 2 артефактов (research-отчёт + pipeline-playbook). Под ultracode исполняется как Workflow: фазы Diagnose → Research → Verify → Synthesize → Handoff.

**Tech Stack:** WebFetch, WebSearch, Parallel CLI (`~/.local/bin/parallel-cli`), Agent tool (general-purpose / Explore / UX-агент), Figma MCP (подключён), скиллы `impeccable`/`deep-research`.

**Спека:** `docs_web/docs/superpowers/specs/2026-07-01-anti-generic-design-pipeline-design.md`

**Выходные директории:**
- Промежуточные артефакты потоков: `docs_web/docs/superpowers/research/`
- Финальный research-отчёт: `docs_web/docs/superpowers/research/2026-07-01-anti-generic-research-report.md`
- Pipeline-playbook (читает UX-агент): `UI_assets/anti-generic-playbook.md`

---

## Workflow-маппинг (ultracode execution)

| Фаза Workflow | Задачи | Тип |
|---|---|---|
| Diagnose | Task 0 | один агент (UX-агент / impeccable), barrier |
| Research | Tasks A, B, C, D, E, F | parallel (6 агентов) |
| Verify | Task G | parallel adversarial по находкам |
| Synthesize | Tasks H, I | sequential (дирижёр) |
| Handoff | Task J | дирижёр + PM acceptance |

Структурированный вывод каждого research-агента — через JSON-schema (StructuredOutput),
чтобы синтез не парсил прозу.

---

## File Structure

| Файл | Ответственность |
|---|---|
| `research/00-diagnostic.md` | Таблица failure modes нашего bevel-clone vs 4 критики, с evidence |
| `research/A-external-skills.md` | taste + UX UI Pro Max: методология, цена, доступность, verdict |
| `research/B-arsenal-matrix.md` | Матрица «7 наших скиллов × симптом» + invocation args |
| `research/C-broad-sweep.md` | Кандидаты-скиллы/инструменты + методология анти-generic |
| `research/D-bevel-ds.md` | Bevel DS/UI-кит + что делает Bevel рукотворным |
| `research/E-references.md` | Паттерны/токены из референсов, которые наш клон растерял |
| `research/F-stitch-figma.md` | Stitch × Figma MCP: прикладной сценарий + verdict |
| `research/G-verification.md` | Adversarial-верификация verdict'ов и ключевых утверждений |
| `research/2026-07-01-anti-generic-research-report.md` | Сводный research-отчёт (deliverable 1) |
| `UI_assets/anti-generic-playbook.md` | 6-стадийный пайплайн со скиллами+args (deliverable 2) |

---

## Task 0: Диагностика (Поток 0) — teardown bevel-clone vs Bevel

**Owner:** UX-агент (визуальная критика — PM-role-boundary) или скилл `impeccable critique`.

**Files:**
- Read: `docs_web/bevel-clone/index.html`, `docs_web/bevel-clone/home/home-main-etalon.html`
- Read (эталон): `UI_assets/screenshots/references/*.png` (14 шт.)
- Create: `docs_web/docs/superpowers/research/00-diagnostic.md`

- [ ] **Step 1: Загрузить вход** — открыть оба HTML и все 14 PNG-референсов Bevel.

- [ ] **Step 2: Построить failure-mode таблицу** с колонками: `Критика | Где в нашем коде (file:line) | Как у Bevel (ref-файл) | Серьёзность (1-3)`. Заполнить все 4 строки критики (типовые компоненты / композиция / wine / рукотворность), каждую — минимум 2 конкретных evidence-пункта с привязкой к file:line и к референсу.

- [ ] **Step 3: Зафиксировать «anti-generic чеклист»** — 8-12 конкретных правил, выведенных из дельты «наш клон vs Bevel» (напр. «бордеры карточек 1px solid вместо мягкой тени», «радиус 8px стоковый vs 14px Bevel»).

- [ ] **Step 4: Verify** — файл `00-diagnostic.md` существует, содержит все 4 строки критики, каждая с ≥2 evidence, и чеклист из ≥8 правил. Команда проверки:

```bash
test -f docs_web/docs/superpowers/research/00-diagnostic.md && grep -c "file:line\|home-main\|index.html" docs_web/docs/superpowers/research/00-diagnostic.md
```
Expected: файл есть, ≥4 ссылок на наш код.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/00-diagnostic.md
git commit -m "Поток 0: диагностика bevel-clone vs Bevel — failure modes + anti-generic чеклист"
```

---

## Task A: Внешние скиллы — taste + UX UI Pro Max

**Owner:** research-агент (general-purpose) + Parallel CLI. **Schema:** да.

**Files:**
- Create: `docs_web/docs/superpowers/research/A-external-skills.md`

- [ ] **Step 1: Фетч первоисточников**

```bash
# через WebFetch (в агенте): https://www.tasteskill.dev/ и https://ui-ux-pro-max-skill.com/
~/.local/bin/parallel-cli fetch "https://www.tasteskill.dev/"
~/.local/bin/parallel-cli fetch "https://ui-ux-pro-max-skill.com/"
```

- [ ] **Step 2: Research методологии и отзывов**

```bash
~/.local/bin/parallel-cli research "What is the 'taste' skill (tasteskill.dev) for AI design — methodology, what it actually does, price, how distributed, reviews"
~/.local/bin/parallel-cli research "UX UI Pro Max skill (ui-ux-pro-max-skill.com) — methodology, principles, price, format, reviews, how it avoids generic AI UI"
```

- [ ] **Step 3: Записать структурированный разбор** — для каждого скилла: `Что это | Методология (принципы/чек-листы/подход) | Цена | Доступность/формат | Чем закрывает наши симптомы | Verdict (брать/не брать/почему)`.

- [ ] **Step 4: Verify** — оба скилла покрыты, у каждого есть Verdict и цена (или явное «цена не найдена»). Команда:

```bash
grep -c "Verdict\|verdict" docs_web/docs/superpowers/research/A-external-skills.md
```
Expected: ≥2.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/A-external-skills.md
git commit -m "Поток A: research taste + UX UI Pro Max — методология + verdict"
```

---

## Task B: Аудит нашего арсенала — матрица скилл × симптом

**Owner:** дирижёр (инлайн — чтение документации).

**Files:**
- Read: `UI_assets/.agents/skills/{high-end-visual-design,emil-design-eng,minimalist-ui,redesign-existing-projects,imagegen-frontend-mobile,app-store-screenshots}/SKILL.md`, `UI_assets/.claude/skills/impeccable/SKILL.md`
- Create: `docs_web/docs/superpowers/research/B-arsenal-matrix.md`

- [ ] **Step 1: Прочитать все 7 SKILL.md** — для каждого извлечь: назначение, когда вызывать, ключевые аргументы/режимы, что на выходе.

- [ ] **Step 2: Построить матрицу** строки = 7 скиллов, колонки = 4 симптома критики (типовые компоненты / композиция / wine / рукотворность). В ячейке — «как этот скилл лечит этот симптом» или «—».

- [ ] **Step 3: Колонка «invocation»** — для каждого скилла точный пример вызова (имя + args), как его дёргать на стадии пайплайна.

- [ ] **Step 4: Verify** — матрица 7×4 заполнена, у каждого скилла есть invocation-пример. Команда:

```bash
grep -c "high-end-visual-design\|emil-design-eng\|minimalist-ui\|redesign-existing\|imagegen-frontend\|app-store-screenshots\|impeccable" docs_web/docs/superpowers/research/B-arsenal-matrix.md
```
Expected: ≥7.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/B-arsenal-matrix.md
git commit -m "Поток B: матрица наших 7 скиллов × симптом критики + invocation"
```

---

## Task C: Broad sweep — ещё более сильные скиллы + методология анти-generic

**Owner:** research-агент (general-purpose) + Parallel CLI. **Schema:** да.

**Files:**
- Create: `docs_web/docs/superpowers/research/C-broad-sweep.md`

- [ ] **Step 1: Поиск кандидатов**

```bash
~/.local/bin/parallel-cli research "Best Claude Code / AI agent skills for high-end UI design in 2026 — beyond taste and UX UI Pro Max. Skills that make AI-generated UI look hand-crafted not generic"
~/.local/bin/parallel-cli findall "AI design skill that produces non-generic hand-crafted UI"
```

- [ ] **Step 2: Поиск методологии оркестрации**

```bash
~/.local/bin/parallel-cli research "How to orchestrate multiple AI design skills in a pipeline to avoid the generic AI look — staging, critique loops, taste gates, reference-driven design"
```

- [ ] **Step 3: Записать** — таблица кандидатов `Инструмент/скилл | Что даёт | Доступность | Стоит ли пробовать` (≥5 кандидатов) + раздел «Методология анти-generic» (ключевые приёмы со ссылками-источниками).

- [ ] **Step 4: Verify** — ≥5 кандидатов, раздел методологии присутствует, источники указаны. Команда:

```bash
grep -c "http" docs_web/docs/superpowers/research/C-broad-sweep.md
```
Expected: ≥5 ссылок-источников.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/C-broad-sweep.md
git commit -m "Поток C: broad sweep — кандидаты-скиллы + методология анти-generic"
```

---

## Task D: Bevel Design System / UI-кит

**Owner:** research-агент (general-purpose) + Parallel CLI + анализ референсов. **Schema:** да.

**Files:**
- Read: `UI_assets/screenshots/references/*.png` (14 шт.)
- Create: `docs_web/docs/superpowers/research/D-bevel-ds.md`

- [ ] **Step 1: Поиск официального DS**

```bash
~/.local/bin/parallel-cli research "Bevel app (HRV / sleep / readiness tracker) design system, UI kit, typography, color palette, design language — official or community teardown"
~/.local/bin/parallel-cli findall "Bevel health app design system / UI kit"
```

- [ ] **Step 2: Анализ 14 референсов** — извлечь по 4 осям: типографика (шрифты/веса/трекинг), сетка/композиция (отступы, ритм, плотность), цвет (палитра, акценты, как используют), детали (тени/бордеры/радиусы/иконки/«рукотворность»).

- [ ] **Step 3: Записать** — раздел «Что делает Bevel рукотворным» по 4 осям + извлечённые токены (hex, радиусы, шрифты) где видно из скринов.

- [ ] **Step 4: Verify** — все 4 оси покрыты, есть ссылка на конкретные ref-файлы. Команда:

```bash
grep -ci "типограф\|сетк\|цвет\|деталь\|bevel-home\|bevel-HRV\|bevel-sleep" docs_web/docs/superpowers/research/D-bevel-ds.md
```
Expected: ≥4.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/D-bevel-ds.md
git commit -m "Поток D: Bevel DS/UI-кит + разбор что делает Bevel рукотворным"
```

---

## Task E: Разбор референсов — что наш клон растерял

**Owner:** UX-агент (визуальный разбор) или `impeccable`. **Schema:** да.

**Files:**
- Read: `UI_assets/screenshots/references/*.png`, `docs_web/bevel-clone/index.html`, `docs_web/bevel-clone/home/home-main-etalon.html`
- Create: `docs_web/docs/superpowers/research/E-references.md`

- [ ] **Step 1: Side-by-side** — сопоставить наш home-экран с `bevel-home-real.png` / `bevel-home screen primary.png`.

- [ ] **Step 2: Список потерь** — ≥5 переиспользуемых паттернов/токенов Bevel, которые наш клон потерял или огрубил (с указанием: что у Bevel → что у нас → как вернуть).

- [ ] **Step 3: Verify** — ≥5 потерь, каждая в формате «Bevel → наш клон → fix». Команда:

```bash
grep -c "→\|->" docs_web/docs/superpowers/research/E-references.md
```
Expected: ≥5.

- [ ] **Step 4: Commit**

```bash
git add docs_web/docs/superpowers/research/E-references.md
git commit -m "Поток E: разбор референсов — паттерны Bevel, потерянные в нашем клоне"
```

---

## Task F: Stitch × Figma MCP — прикладной сценарий

**Owner:** research-агент (general-purpose) + Parallel CLI. **Schema:** да.

**Files:**
- Create: `docs_web/docs/superpowers/research/F-stitch-figma.md`

- [ ] **Step 1: Фетч + research Stitch**

```bash
~/.local/bin/parallel-cli fetch "https://stitch.withgoogle.com"
~/.local/bin/parallel-cli research "Google Stitch (stitch.withgoogle.com) — what it does, input/output, Figma export, how it fits a design-to-code workflow, limitations, pricing"
```

- [ ] **Step 2: Спроектировать интеграцию** — где Stitch встаёт в наш пайплайн (между PM-брифом и UX-агентом, стадия Composition-first), связка `Stitch → Figma (MCP подключён) → код`, как избежать generic-генерата (taste-отбор вариантов).

- [ ] **Step 3: Записать** — раздел «Прикладной сценарий» (пошагово: вход → Stitch → Figma MCP → UX-агент) + Verdict «усиливает/мешает/при каких условиях».

- [ ] **Step 4: Verify** — есть пошаговый сценарий с участием Figma MCP + Verdict. Команда:

```bash
grep -ci "figma\|stitch\|verdict" docs_web/docs/superpowers/research/F-stitch-figma.md
```
Expected: ≥3.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/F-stitch-figma.md
git commit -m "Поток F: Stitch × Figma MCP — прикладной сценарий + verdict"
```

---

## Task G: Adversarial-верификация находок

**Owner:** parallel skeptic-агенты (по одному на verdict). **Schema:** да.

**Files:**
- Read: `research/A-external-skills.md`, `research/C-broad-sweep.md`, `research/D-bevel-ds.md`, `research/F-stitch-figma.md`
- Create: `docs_web/docs/superpowers/research/G-verification.md`

- [ ] **Step 1: Собрать verdict'ы** — извлечь все verdict-утверждения (брать/не брать taste, UX UI Pro Max, Stitch; «Bevel рукотворен потому что X»; кандидаты из C).

- [ ] **Step 2: Refute-проход** — на каждый verdict отдельный скептик-агент с промптом «попробуй опровергнуть; default = опровергнуто, если фактов мало». Выживает verdict, если опровергнуть не удалось.

- [ ] **Step 3: Записать** — таблица `Утверждение | Refute-попытка | Выжило? | Confidence (low/med/high)`.

- [ ] **Step 4: Verify** — каждый verdict из A/C/D/F имеет строку с confidence. Команда:

```bash
grep -ci "confidence\|выжило\|опроверг" docs_web/docs/superpowers/research/G-verification.md
```
Expected: ≥3.

- [ ] **Step 5: Commit**

```bash
git add docs_web/docs/superpowers/research/G-verification.md
git commit -m "Поток G: adversarial-верификация verdict'ов research"
```

---

## Task H: Синтез — Research-отчёт (deliverable 1)

**Owner:** дирижёр.

**Files:**
- Read: `research/00-diagnostic.md`, `research/A..G`
- Create: `docs_web/docs/superpowers/research/2026-07-01-anti-generic-research-report.md`

- [ ] **Step 1: Свести** все потоки в единый отчёт: Executive summary → Диагностика (4 симптома) → Внешние скиллы (verdict) → Наш арсенал (матрица) → Broad sweep → Bevel DS → Stitch → Confidence-сводка из G.

- [ ] **Step 2: Раздел «Verdict-таблица»** — taste / UX UI Pro Max / Stitch: брать/не брать, цена, confidence.

- [ ] **Step 3: Verify (spec coverage)** — отчёт покрывает G1 (методология+verdict внешних), G2 (broad sweep), и питает G3. Команда:

```bash
grep -ci "taste\|UX UI Pro Max\|stitch\|verdict\|матриц" docs_web/docs/superpowers/research/2026-07-01-anti-generic-research-report.md
```
Expected: ≥5.

- [ ] **Step 4: Commit**

```bash
git add docs_web/docs/superpowers/research/2026-07-01-anti-generic-research-report.md
git commit -m "Синтез: Anti-Generic research-отчёт (deliverable 1)"
```

---

## Task I: Синтез — Anti-Generic Playbook (deliverable 2)

**Owner:** дирижёр.

**Files:**
- Read: research-отчёт (Task H) + `00-diagnostic.md` + `B-arsenal-matrix.md`
- Create: `UI_assets/anti-generic-playbook.md`

- [ ] **Step 1: Заполнить 6 стадий** пайплайна (из спеки, раздел 4) конкретикой: на каждой стадии — точный скилл + аргументы вызова + что на входе/выходе + какой симптом из диагностики закрывает.

- [ ] **Step 2: Раздел «Роли»** — PM / UX-агент / дирижёр: кто что делает на каждой стадии.

- [ ] **Step 3: Раздел «Anti-generic gate»** — критерии прохождения стадии 5 (скоринг против Bevel-рефов, чек-лист из Task 0), условие петли назад.

- [ ] **Step 4: Verify (spec coverage)** — каждая из 6 стадий имеет скилл+args; каждый из 4 симптомов критики имеет контрмеру; роли определены. Команда:

```bash
grep -ci "Стадия\|стадия\|скилл\|роль\|gate" UI_assets/anti-generic-playbook.md
```
Expected: ≥6 (стадии) + наличие ролей и gate.

- [ ] **Step 5: Commit**

```bash
git add UI_assets/anti-generic-playbook.md
git commit -m "Синтез: Anti-Generic Playbook — исполнимый пайплайн со скиллами+args (deliverable 2)"
```

---

## Task J: Handoff + PM acceptance

**Owner:** дирижёр + PM.

- [ ] **Step 1: Показать PM** оба deliverable'а с прямыми путями (visual-path rule): research-отчёт + playbook.

- [ ] **Step 2: Дать verdict-сводку** по 3 внешним инструментам (брать/не брать) одним абзацем.

- [ ] **Step 3: Обозначить следующий шаг** — фаза G4 (flagship proof-экран по пайплайну) запускается отдельно после acceptance.

- [ ] **Step 4: Дождаться явного «принято»** от PM (PM acceptance gate). НЕ закрывать задачу без него.

- [ ] **Step 5: Обновить** `knowledge-base/PROJECT_STATE.md` + memory после acceptance.

---

## Self-Review (выполнено при написании плана)

- **Spec coverage:** G1 → Task A+H; G2 → Task C+H; G3 → Task I; диагностика (4 симптома) → Task 0 → питает I; референсы → Task D+E; Stitch×Figma → Task F; verdict'ы → верифицированы Task G. G4 (proof) — явно отложен в спеке, не в этом плане. ✅
- **Placeholder scan:** конкретные пути, команды Parallel CLI, verify-команды в каждой задаче. ✅
- **Type consistency:** имена артефактов (`00-diagnostic.md`, `A..G`, report, playbook) consistent между File Structure, задачами и Task H/I. ✅
