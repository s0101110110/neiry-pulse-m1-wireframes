# Neiry Pulse · Design System — Hand-off & Playbook

**Версия:** v1.0.4 · **Дата:** 1 июля 2026 · **Статус:** Phase 1–4 завершены, ожидает PM acceptance + publish Team Library

Этот документ — комплексный hand-off для коллег и продуктовых менеджеров-solopreneur'ов, кто хочет повторить или расширить workflow.

---

## 0. TL;DR (для быстрого понимания)

- Design System Neiry Pulse существует одновременно в **коде** (`docs_web/bevel-clone/shared/`) и в **Figma** (cloud-файл со всеми Variables, Text/Effect Styles, 14 компонентами и одной демо-screen)
- Построена **AI-агентом (Claude Code + Figma MCP)** за один сеанс — не вручную дизайнером
- Один источник правды: `tokens.figma.json` ↔ Figma Variables, изменение в одном месте отражается в каждом подписчике
- Архитектурный паттерн — для роли **PM + on-demand designer**: AI готовит baseline, designer полирует только нужное

---

## 1. Контекст

- **Продукт:** Neiry Pulse — mobile-first wellness-приложение (трекер-браслет + Headband BCI). Фронт на React Native, дизайн-система прицельно на Figma + CSS-параллели для веба
- **Команда:** PM-solopreneur (без in-house дизайнера) + on-demand технический дизайнер/арт-директор
- **Бюджет на дизайн-tools:** Figma Professional ($12/editor/мес), Parallel AI ($10 одноразово на research)
- **Технологический стек DS:** Tokens Studio JSON format · CSS custom properties · Figma Variables · Figma Components с Variants · Pulse Mono (JetBrains Mono fallback) · Golos Text

---

## 2. Что построено (technical summary)

### 2.1 Локальный код (docs_web/bevel-clone/shared)

| Артефакт | Содержание |
|---|---|
| `tokens.css` | 73 CSS custom properties — runtime источник правды для веб-мокапов |
| `tokens.json` | Flat nested JSON для CSS/React импорта |
| `tokens.figma.json` | **Tokens Studio формат** с `{value, type}` обёрткой — для Figma sync |
| `components.css` | 14 `.bv-*` атомарных компонентов (BEM-like с modifiers) |
| `README.md` | DS-документация: usage, principles, tabs canon, versioning |
| `*.html` (cheatsheets) | Living-style guides: typography.html, colors.html, states.html, components-gallery.html |
| `figma-build-spec.md` | Build-инструкции для AI / fallback для manual rebuild (если был создан subagent'ом) |

### 2.2 Figma-файл

**URL:** https://www.figma.com/design/dfUahpollij3UUunPI4mG4
**План:** Professional (необходим для Team Library publish)
**Структура (3 страницы):**

1. **`1. Foundations`** — living style guide
   - 33 color swatches × 10 групп
   - 8 spacing-bars + 5 radius-карточек
   - 10 type specimens

2. **`2. Components`** — все 14 main components с variant-наборами
   | Категория | Компонент | Variants |
   |---|---|---|
   | Layout | bv-card · bv-row-divider | Type×4 / — |
   | Atomic | bv-capsule · bv-status-dot · bv-pill | Tone×3 / Tone×3 / — |
   | Nav | bv-nav-pill · bv-nav-item | — / State×2 |
   | Forms | bv-icon-square · bv-toggle | — / State×2 |
   | Type | bv-eyebrow · bv-section-heading · bv-row-label · bv-row-meta | Variant×2 / — / — / — |
   | Display | bv-metric-bento | — |

3. **`3. Screens`** — пример Home Etalon 375×812 собран из instances компонентов

### 2.3 Figma-объекты

- **3 Variable Collections:** Primitives · Spacing & Geometry · Typography
- **69 Variables** с правильными scopes (`FRAME_FILL`, `TEXT_FILL`, `GAP`, `CORNER_RADIUS` и т.д., НЕ `ALL_SCOPES`) + codeSyntax `var(--bv-*)`
- **10 Text Styles** (Display / Section / Body / Micro / Mono ramp)
- **4 Effect Styles** (Shadow/Card · Nav · Header · Dot)

### 2.4 Как сделано (стек инструментов)

| Инструмент | Роль |
|---|---|
| **Claude Code** (VSCode extension) | Главный AI-агент-исполнитель |
| **Figma MCP Server** (https://mcp.figma.com/mcp) | Bridge между AI и Figma (read + write через `use_figma`) |
| **context7 MCP** | Документация Figma Plugin API + skill discovery |
| **Parallel AI** | Deep research по Figma integration options |
| **Skills figma-use / figma-generate-library** | Структурированный workflow (Phase 0→1→2→3→4) |

**Команды установки в Claude Code (один раз):**

```bash
# Установить Figma MCP
claude mcp add --transport http figma https://mcp.figma.com/mcp

# Авторизоваться через OAuth (один раз)
claude mcp login figma
# → откроется браузер с Figma OAuth → разрешить доступ
```

---

## 3. Workflow-модель для PM + on-demand designer

### 3.1 Роли

| Кто | Делает | Не делает |
|---|---|---|
| **PM (Костя)** | Brief, scope, acceptance, общая координация, может править токены и Variables | Не пишет HTML/CSS, не строит компоненты руками |
| **AI-агент (Claude)** | HTML/CSS мокапы, Figma library generation через MCP, code↔design sync setup | Не принимает финальное продуктовое решение |
| **On-demand designer** | Полировка визуала, кастомные иконки, нестандартные screens, ревью pixel-perfection | Не строит baseline DS с нуля |
| **Kirill (dev)** | React Native implementation, pull tokens из `tokens.figma.json` | Не дизайнит UI |

### 3.2 Loop

```
1. PM описывает экран словами / в HTML-мокапе
       ↓
2. AI генерит HTML draft в docs_web/bevel-clone/ из bv-* компонентов
       ↓ ← PM ревьюит, итерации
3. AI пушит результат в Figma через use_figma (out of instances библиотеки)
       ↓
4. On-demand designer ревьюит в Figma, добавляет polish (только то что AI не смог)
       ↓
5. PM accept, designer publishes library update
       ↓
6. Kirill pull-ит обновлённые токены через Tokens Studio + GitHub sync
       ↓
7. Reactive Native UI обновляется
```

**Ключевая идея:** designer подключается **только на step 4**. Baseline и итерации делает AI с PM.

---

## 4. Tutorial: как воспроизвести этот workflow в другом проекте

### Step 0 — Подготовка

1. **Figma:** Professional plan ($12/editor/мес). Обязательно Full seat для библиотек.
2. **Claude Code** установлен (VSCode extension)
3. **Repo с CSS-tokens** + components.css в нужной структуре
4. **Tokens Studio JSON format** — конвертировать существующие tokens в `tokens.figma.json` (см. наш пример)

### Step 1 — Установка Figma MCP

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp login figma  # OAuth в браузере
```

После — рестартнуть Claude Code сессию, чтобы tools подгрузились.

### Step 2 — Запустить AI-агента с правильным контекстом

В Claude Code сессии:

```
Контекст: Build Figma library из существующих CSS-токенов и компонентов в [repo path].
Используй figma-use + figma-generate-library skills.

Phase 0: DISCOVERY — проинспектируй tokens.figma.json и components.css
Phase 1: FOUNDATIONS — создай Variable Collections, Text Styles, Effect Styles
Phase 2: FILE STRUCTURE — 3 страницы (Foundations / Components / Screens)
Phase 3: COMPONENTS — все компоненты с variants
Phase 4: пример screen из instances + publish hint
```

AI пройдёт все фазы автоматически с checkpoints после каждой.

### Step 3 — Publish Team Library (вручную в Figma)

После того как AI закончил:

1. Открой созданный Figma-файл
2. Main menu → **Libraries** (Cmd+Opt+O / Ctrl+Alt+O)
3. На карточке этого файла кликни **Publish**
4. Диалог покажет всё что будет опубликовано (69 vars + 14 components + 14 styles)
5. **Publish** → готово

Теперь любой другой Figma-файл может подписаться на эту library и получать обновления.

### Step 4 — Hand-off дизайнеру

Дай дизайнеру:
- Figma URL (с правами Editor)
- Этот HANDOFF документ
- Краткий контекст продукта + brand-guidelines

Designer работает в Figma как обычно — изменяет main components, добавляет polish, добавляет новые screens.

### Step 5 — Sync обратно в код

**Через Tokens Studio:**
1. Установи плагин **Tokens Studio for Figma** в Figma
2. Plugin → Settings → JSON tab → paste `tokens.figma.json`
3. Settings → Sync → GitHub → подключить repo
4. После — изменения в Figma Variables → авто-PR в `shared/tokens.figma.json`

**Через Code Connect** (для компонентов):
1. В коде создать `.figma.tsx` файлы рядом с React-компонентами
2. `npx @figma/code-connect publish --token=$FIGMA_TOKEN`
3. В Dev Mode дизайнер видит реальный код вместо auto-generated CSS

---

## 4a. Pipeline правок из Figma-комментариев

**Когда:** коллеги оставили комментарии в Pulse-file (или другом review-file), нужно применить правки к source и синхронизировать.

**Формат ввода PM → AI:**
- Figma URL с `node-id` (или короткое имя экрана типа `02a-training-start-step1`)
- Требование текстом ИЛИ прикреплённый screenshot с указаниями

**6-step pipeline:**

1. **Determine target** — по `docs_web/wireframes/m3/FIGMA-MAPPING.md` определяем HTML файл + frame
2. **HTML edit** — вносим правку в `docs_web/wireframes/m3/*-v0.html` (и в `-mvp-store.html` если существует)
3. **Preview** — headless Chrome screenshot → PM approve
4. **PNG reslice** — `python3 UI_assets/skills/scripts/slice_phones_transparent.py` → обновляет `ui_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/*.png`
5. **Figma upload** — `mcp__figma__upload_assets` с `nodeId`, POST PNG → image fill в Pulse-file rectangle заменяется
6. **Dashboard update** — в `docs_web/bevel-clone/tasks/figma-comments-dashboard.html`:
   - `data-status="open"` → `data-status="resolved"`
   - Добавить class `resolved` к article
   - Badge `🔴 OPEN` → `✅ DONE (DD.MM)`
   - Обновить статистику: Open −1, Done +1, соответствующий priority −1
   - Обновить чипы filters с counts
7. **ANALYZED.md sync** — в `knowledge-base/figma-comments-2026-07-01-pulse-wireframes-ANALYZED.md`: Статус → `✅ DONE (DD.MM.YYYY, commit XYZ)`
8. **Commit + push** — единый commit со всеми изменениями (`Задача #N · <краткое описание>`)

**Итог:** правка синхронизирована в **6 местах** — HTML source, PNG, Figma review-gallery, Dashboard, ANALYZED.md, git history.

**Время цикла:** 3-5 минут per задача (для Copy/Wording — Type A). Bigger правки (Type B/C) — 10-30 минут.

---

## 5. Варианты развития (Tracks)

PM может развивать в любую сторону самостоятельно до момента когда упрётся в технологию или фантазию.

### Track A — Полировка визуала (PM может сам через AI)

**Что:** Доделать визуальную плотность компонентов до prod-уровня.

- В Figma открыть main components на странице `2. Components`
- Через AI (`use_figma`): «Сделай Hero card как в `home-main-etalon.html` — внутри metric tiles + HRV-капсула»
- Или вручную в Figma: добавить иконки, контент, фоны
- Каждое изменение main component каскадирует на все instances

**Время:** часы (не дни). 

### Track B — Расширение screens (PM может сам через AI)

**Что:** Создать остальные экраны Pulse из существующих компонентов.

- Список целей: Training (start/active/end) · History · Settings (BT, Notifications, Privacy) · Health Monitor · Onboarding (8 шагов) · Health Sharing flow
- AI builds screens из instances → designer polishes → ready

**Время:** 1-2 часа per screen с AI vs 1-2 дня дизайнера с нуля.

### Track C — Иконки (требует designer)

**Что:** Создать 40+ иконок (battery, bluetooth, charge, profile, gear, etc.) как Figma Components.

- AI может создать placeholder-иконки (геометрические формы), но качество требует designer'а с illustrator skills
- Иконки добавляются как INSTANCE_SWAP в `bv-icon-square` и `bv-nav-item`
- Дизайнер делает SVG → импортирует в Figma как Components → publish

**Время:** 1-2 дня designer.

### Track D — Dark Mode (после Sleep-экрана) — PM с AI

**Что:** Добавить mode `Dark` в Color collection для Sleep-screen.

- AI: «Добавь mode Dark в Color collection, создай Dark-aliases для всех colors через `addMode + setValueForMode`»
- Каждый компонент автоматически работает в обоих modes (т.к. variables используют bindings)
- Designer проверяет contrast/легитимность Dark-цветов

**Время:** 2-3 часа с AI.

### Track E — Code Sync (требует Kirill + AI)

**Что:** Двусторонний sync Figma ↔ React Native код.

- Tokens Studio + GitHub sync для tokens
- Code Connect для components (`.figma.tsx` файлы) — пишет Kirill с AI помощью
- Style Dictionary V4 для конвертации tokens.json → Swift/Kotlin/Tailwind

**Время:** 1 неделя setup, потом auto.

### Track F — Component Library расширение

**Что:** Когда появятся новые UX-паттерны — добавлять как новые `bv-*` компоненты.

- Сначала в коде (`components.css`)
- Потом AI пушит в Figma как новый main component
- Designer ревьюит, polish
- Publish library update

**Когда подключать designer:** только если новый компонент требует кастомного визуала. Стандартные variations (size, state) AI делает сам.

### Track G — Motion (после Pro + Q3 2026)

**Что:** Анимации компонентов (загрузка, transitions, micro-interactions).

- Figma Motion (open beta, требует Professional+)
- AI может писать motion-tokens (duration, easing) как variables
- Designer записывает keyframes в Figma → AI экспортирует в React Native Reanimated

**Время:** 2-3 недели — но это уже отдельный subproject.

### Track H — Multi-brand support

**Что:** Если когда-то Neiry Pulse станет white-label SaaS — добавить brand-modes в Variables.

- Создать Mode `Default` + `Brand-X` + `Brand-Y` в Color collection
- Каждый brand имеет свой wine-equivalent
- Один screen работает для всех брендов через переключение mode

**Время:** дни — но только если будет нужно. YAGNI пока.

---

## 6. Product pipeline для Fast TTM

### Старая модель (without DS)

```
PM → brief (1 day)
   → designer создаёт wireframes (3 days)
   → designer создаёт high-fidelity (3 days)
   → designer создаёт прототип (1 day)
   → developer implements (5 days)
   = 13 дней per major feature
```

### Новая модель (с DS + AI)

```
PM → brief (1 day)
   → AI создаёт HTML мокап из bv-* (2 hours)
   → AI пушит в Figma (1 hour)
   → designer полирует pixel-perfect (4 hours, only what AI can't)
   → developer pulls tokens (auto via GitHub sync)
   → developer implements (2-3 days т.к. компоненты-instances уже есть)
   = 5-6 дней per major feature
```

**Acceleration: ×2-3.** Особенно эффект ощущается на 2-м и далее feature — DS уже зрелая, каждое следующее iteration ещё быстрее.

### Key TTM enablers

1. **Variables вместо хардкодов** — изменение `brand/wine` обновляет визуал всего продукта за секунды
2. **Components как Library** — новые screens строятся из drag-n-drop, не с нуля
3. **AI как baseline-builder** — designer работает только на 20% задач (polish), не на 100% (от brief до final)
4. **Tokens Studio GitHub sync** — нет ручного хэндоффа дизайнер→разработчик
5. **Code Connect** — Dev Mode показывает реальный код, разработчик не интерпретирует CSS
6. **Single source of truth** — `tokens.figma.json` живёт в Git, любой stakeholder видит историю

### Где скиллы подключаются

| Скилл | Когда |
|---|---|
| **Designer (visual)** | Polish, custom icons, branded illustrations, реалистичный контент в screens |
| **Designer (UX)** | Новые user flows, не покрытые существующими screens |
| **AI agent** | Baseline screens из known patterns, токены, документация, hand-off материалы |
| **Developer (React)** | Reactive Native implementation, fully isolated through Code Connect |
| **PM (you)** | Brief, scope, acceptance, выбор tracks из секции 5 |

### Где можно платно ускориться

- **Figma Make** — AI-генерация полных экранов из текста (Q4 2026, paid)
- **Figma Motion + Code Layers** — animation tokens + code on canvas (paid)
- **Tokens Studio Pro** — расширенные sync features, theming engine ($24/мес)
- **Parallel AI** — глубокий research для DS-decisions ($10/research)

---

## 7. Открытые риски и решения

| Риск | Решение |
|---|---|
| **MCP rate limits** — На Starter 6 calls/month, на Pro 200/day | Pro plan уже куплен. Хватит на 100+ итераций per day. |
| **Pulse Mono шрифт не доступен** | JetBrains Mono используется как fallback (см. `tokens.figma.json` font-stack). Когда appoint Pulse Mono — заменить везде один раз через Variable. |
| **Дизайнер изменит компонент несовместимо с кодом** | Publish acceptance gate: designer не пушит в Library без PM-acceptance. Tokens Studio GitHub auto-PR требует merge от code-owner. |
| **AI сделает «слегка не так»** | После каждой Phase — screenshot + visual review. AI пишет всё в use_figma calls которые **atomic** (failed = ничего не изменилось). |
| **Free plan лимит 3 страницы на файл** | Сейчас на Pro — unlimited. Если когда-то downgrade — все 3 страницы покрываются (Foundations / Components / Screens) с запасом. |
| **Lock-in в Figma** | tokens.figma.json в W3C-near формате (Tokens Studio compat). Можно мигрировать на Supernova/zeroheight без потери данных. |

---

## 8. Quick-start для нового коллеги

Если ты подключаешься к проекту впервые:

1. **Получи доступ** к Figma-файлу (https://www.figma.com/design/dfUahpollij3UUunPI4mG4) — попроси PM прислать invite на Editor seat
2. **Прочитай этот документ** + README в `docs_web/bevel-clone/shared/README.md`
3. **Посмотри Foundations** в Figma — пойми палитру и shape language за 10 минут
4. **Посмотри Components** — все 14 атомов с variants
5. **Если ты дизайнер:** работай только с main components на странице Components. Каждое изменение каскадирует на instances в Screens.
6. **Если ты developer:** изменения tokens приходят через GitHub PR от Tokens Studio. Компоненты можешь pull-ить через Code Connect когда он будет настроен.
7. **Если ты PM:** ты главный coordinator — пиши brief'ы, делай accept, выбирай tracks из секции 5.

---

## 9. Ссылки и артефакты

### В коде
- `docs_web/bevel-clone/shared/` — DS source-of-truth (tokens + components + docs)
- `docs_web/bevel-clone/home/` · `settings/` — рефакторенные screens на DS
- `docs_web/bevel-clone/index.html` — gallery всех DS-артефактов

### В Figma
- File: https://www.figma.com/design/dfUahpollij3UUunPI4mG4
- Team: STB (Professional plan)
- Owner: hello.solomono@gmail.com

### Документация
- DS README: `docs_web/bevel-clone/shared/README.md`
- Этот hand-off: `docs_web/bevel-clone/shared/HANDOFF.md`
- Spec: `docs_web/superpowers/specs/2026-06-29-bevel-clone-design-system-design.md`
- Implementation plan: `docs_web/superpowers/plans/2026-06-29-bevel-clone-design-system.md`

### GitPages (опубликовано)
- https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/bevel-clone/

### Внешние ресурсы
- Figma MCP Server docs: https://help.figma.com/hc/en-us/articles/32132100833559
- Tokens Studio for Figma: https://tokens.studio
- Code Connect docs: https://www.figma.com/code-connect-docs/
- Style Dictionary: https://amzn.github.io/style-dictionary/

---

**Hand-off owner:** Костя (PM)
**Last update:** 1 июля 2026
**Next milestone:** Publish Team Library + onboarding on-demand designer
