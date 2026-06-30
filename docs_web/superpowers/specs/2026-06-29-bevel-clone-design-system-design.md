# Bevel-clone Design System — Mid Scope (M3 sprint)

**Status:** Draft for PM review
**Date:** 2026-06-29
**Brainstorm session:** 2026-06-29 (single-session)
**Author:** PM (Константин) × Claude (UX-orchestrator)
**Scope:** Mid (M3 sprint, 5-7 рабочих дней)

---

## Context

После 5+ итераций Bevel-clone (Home / HRV / Settings) + утверждённого ЭТАЛОНА (`docs_web/bevel-clone/home/home-main-etalon.html`) — у проекта есть рабочий визуальный язык, но НЕТ систематизированной design system. Каждый screen дублирует CSS-tokens, имена классов разные, изменение radius в одном месте не отражается в других.

**Цель этой работы:** вынести design tokens, atomic components и patterns в shared layer, который служит одновременно:
- UX-агенту (быстрая сборка новых screens из готовых классов)
- Кириллу-разработчику (production React imports от единого источника)
- Google Stitch / AI tools (machine-readable DESIGN.md mirror)
- PM/Никите (self-service ревью без агента)

**Решающие constraints:**
- Не ломать existing screens (visual regression PASS обязателен)
- Не вводить новые dependencies (no Storybook, no React build, no Stitch CLI в Mid)
- Сохранить замкнутые константы: Golos Text + Pulse Mono, wine `#831843` brand-anchor, cool-gray `#F0F0F3` palette, 4px grid

---

## Decisions log

| # | Question | Answer |
|---|---|---|
| 1 | Audience | Все 4 (UX-agent + Кирилл + Stitch + PM) |
| 2 | Pace | Mid в M3 sprint (1 месяц) |
| 3 | Approach | Hybrid — `bevel-clone/shared/` живой DS + `DESIGN.md` зеркало для AI |
| 4 | Auto code gen | Не в Mid. Ручной sync tokens.css ↔ tokens.json. Auto-gen Wave 2 |
| 5 | Versioning | Semver в header comment файлов. CHANGELOG.md когда будет breaking change |
| 6 | Figma sync | Phase 7 — последняя фаза скоупа |
| 7 | Storybook | Не в Mid. `components-gallery.html` выполняет 80% той же роли |
| 8 | React component library | Не в Mid. `tokens.json` + `components.css` достаточно для Кирилла |

---

## 1 · Architecture

### Folder structure

```
docs_web/bevel-clone/shared/         ← новая папка-source для DS (single location)
├── tokens.css                        ← CSS-переменные (runtime source-of-truth)
├── tokens.json                       ← same в JSON (для Stitch / Tailwind / Кирилл React)
├── components.css                    ← атомарные стили (.bv-card, .bv-capsule, …)
├── colors.html                       ← live палитра + AA-контраст матрица
├── typography.html                   ← live type-scale (Golos + Pulse Mono samples)
├── states.html                       ← 5 status-states cheatsheet (Норма/Ниже/Выше/Внимание/Нет данных)
├── components-gallery.html           ← каталог всех 14 компонентов (live)
└── README.md                         ← index + usage docs (для UX-агента / Кирилла / PM)

docs_web/DESIGN.md                    ← обновляется как machine-readable mirror tokens.css (Stitch input)
docs_web/bevel-clone/{home,hrv,settings,…}/*.html
                                      ← все screens подключают tokens.css + components.css через <link>
                                         НИКАКИХ inline styles per-screen для shared компонентов

docs_web/fonts/pulse-mono/            ← локальные Pulse Mono font files (уже скопировано 29.06)
```

### File responsibilities

| Файл | Source-of-truth для | Кто использует |
|---|---|---|
| `tokens.css` | Все CSS-переменные runtime (colors / spacing / radii / shadows / typography) | Все screens (через `<link>`), UX-агент при правках |
| `tokens.json` | Same values в JSON | Кирилл React (импорт values), Stitch, Tailwind config |
| `components.css` | Атомарные классы `.bv-*` | Все screens (через `<link>`), UX-агент при сборке screens |
| `DESIGN.md` | High-level YAML spec mirror | Stitch / Claude / другие AI |
| `colors.html` | Live палитра + AA-матрица | PM-ревью, Кирилл a11y check |
| `typography.html` | Live type-scale demo | PM-ревью, дизайнер samples |
| `states.html` | 5 status-states matrix | UX-агент при сборке screens с status |
| `components-gallery.html` | Live каталог всех 14 компонентов | UX-агент, Кирилл (RSVP), PM |
| `README.md` | Usage instructions + index | Onboarding для нового разработчика / агента |

### Naming convention

- Все классы компонентов: префикс `bv-` (Bevel-clone). Защищает от Tailwind / shadcn / utility-CSS конфликтов.
- BEM-style модификаторы: `bv-card--hero`, `bv-capsule--mini`, `bv-button--primary`
- States: `.is-active`, `.is-disabled`, `.has-data`, `.empty`
- CSS-переменные: `--bv-radius-card`, `--bv-shadow-card`, `--bv-color-wine` (тоже с `bv-` префиксом для уникальности)

### Versioning

- Header comment в каждом из `tokens.css` / `tokens.json` / `components.css`:
  ```css
  /*!
   * Neiry Pulse · Bevel-clone · tokens
   * v1.0.0 — 2026-06-29 — initial extraction from home-main-etalon
   */
  ```
- Major version bump = breaking change (rename класса, удаление token).
- Minor = new addition (новый компонент в Wave 2).
- Patch = visual tweak (изменение значения существующего token).

---

## 2 · Component scope (первая волна, 14 атомарных)

### Group A — Surface & Layout (3)

| Класс | Назначение | Модификаторы |
|---|---|---|
| `bv-screen` | Полный wrapper экрана (cool-gray bg, mobile container) | — |
| `bv-card` | Базовая карточка (white bg, hairline, soft shadow, radius 20) | `--hero` (HRV), `--bento` (mini) |
| `bv-section-header` | Inline left H2 (Golos 700 22-28px) | — |

### Group B — Chrome (4)

| Класс | Назначение | Модификаторы |
|---|---|---|
| `bv-app-bar` | Top header | `--pill` (home), `--back` (sub-screens) |
| `bv-nav-pill` | Bottom floating pill | — |
| `bv-nav-item` | Tab в bottom nav (5 шт: Дом / Тренировка / История / Здоровье / Ещё) | `.is-active` (wine + chip bg) |
| `bv-avatar` | Круг 32×32 с инициалами (КЛ blue) | — |

### Group C — Health Monitor (2)

| Класс | Назначение | Модификаторы |
|---|---|---|
| `bv-capsule` | Вертикальная pill-индикатор статуса | `--full` (с bounds), `--mini` (compact) |
| `bv-chip` | Цветной chip | `--status-low/mid/high/critical/empty`, `--delta-up/down`, `--badge-wine` |

### Group D — Settings rows (2)

| Класс | Назначение | Модификаторы |
|---|---|---|
| `bv-row` | Settings list-row container | — |
| `bv-icon-square` | 32×32 tinted квадрат с line-icon | `--default`, `--wine`, `--danger`, `--success` |

### Group E — Controls (3)

| Класс | Назначение | Модификаторы |
|---|---|---|
| `bv-button` | Кнопка | `--primary` (wine), `--secondary`, `--ghost` |
| `bv-toggle` | Switch | `.is-on` (wine track) |
| `bv-eyebrow` | Pulse Mono 11px UPPERCASE label | — |

### Iconography convention (не компонент, правило)

- Все line-SVG: `stroke-width: 1.7px`, `stroke-linecap: round`, `stroke-linejoin: round`, `fill: none`, `stroke: currentColor`
- Размеры: 16 / 18 / 20 / 24px (4px grid)

### Wave 2 (НЕ сейчас, упоминаем для горизонта)

- `bv-chart` — нужен для HRV detail / Sleep
- `bv-modal-sheet` — HRV/Sleep explainer
- `bv-input` / `bv-checkbox` — Sign Up / Onboarding
- `bv-banner` — Demo data warning
- `bv-tabs` — sub-screen tabs

---

## 3 · Build order (6 stages + Phase 7)

### Dependencies

```
tokens.css ──► components.css ──► все cheatsheets + screen refactor
   │
   ├──► tokens.json (auto-mirror)
   ├──► DESIGN.md (update)
   └──► colors.html (только tokens, не нужны components)
```

### Stage table

| # | Stage | Содержание | Время | Parallel | Где делегировать |
|---|---|---|---|---|---|
| **1** | Tokens extraction | Извлечь CSS-vars из `home-main-etalon.html` в `shared/tokens.css`. Документировать каждый token. | 1 день | НЕТ | Второе окно UI_assets (formal skills) |
| **2** | Tokens mirror (×3) | (a) `tokens.json` — JSON mirror. (b) `DESIGN.md` — обновить под cool-gray v3 + Pulse Mono + новые tokens. (c) `colors.html` — палитра + AA матрица. | 1 день | ДА (3 agents) | (a)+(c) тут (мех.), (b) во втором окне |
| **3** | Components extraction | Извлечь все `.bv-*` стили в `shared/components.css`. Атомарные + модификаторы. | 1 день | НЕТ | Второе окно (formal `impeccable polish/harden`) |
| **4** | Live demonstrations (×3) | (a) `components-gallery.html` — финализировать. (b) `states.html` — 5 status cheatsheet. (c) `typography.html` — type-scale demo. | 1.5 дня | ДА (3 agents) | Все три во втором окне (formal `typeset/colorize`) |
| **5** | Screen refactor (×3) | Перевести existing screens на shared CSS: (a) `home-main-etalon`. (b) `home-health-monitor`. (c) `settings/{bt-pairing,notifications,privacy}`. Visual regression check. | 1.5 дня | ДА (3 agents) | Тут (механ. refactor, parallel subagents) |
| **6** | Documentation + validation | (a) `README.md` — index + usage. (b) Final visual regression. (c) Push to GitPages. | 0.5-1 день | НЕТ | Тут |
| **7** | Figma sync | Перенос tokens в Figma plugin (Figma Tokens / Tokens Studio). PM/Никита получают тот же source-of-truth в Figma. | 1-2 дня | НЕТ | Отдельная фаза, после Stage 6 acceptance |

### PM-чекпоинты

- **После Stage 1** → показываю `tokens.css` (наполнение, имена, нет ли пропусков)
- **После Stage 3** → показываю `components.css` + verify ETALON ещё рендерится корректно через shared
- **После Stage 4** → показываю 3 cheatsheets (самые PM-readable артефакты)
- **После Stage 5** → visual regression report — все existing screens рендерятся идентично pre-refactor
- **Stage 6** → финальный acceptance + push
- **Stage 7** → Figma sync acceptance (отдельно)

Чекпоинты — короткие screenshot reviews (1-2 мин), не блокируют другие parallel-работы.

### Workflow split

**Второе окно UI_assets (formal skills доступны):** Stages 1, 2(b), 3, 4 — там где нужна designer's eye + impeccable typeset/colorize/polish/harden.

**Тут (subagents, методология вручную):** Stages 2(a), 2(c), 5, 6 — где нужен parallel + mechanical extraction/refactor.

---

## 4 · Validation + risks + open questions

### Success criteria

| Критерий | Проверка |
|---|---|
| Visual regression | Все рефакторённые screens рендерятся идентично pre-refactor (side-by-side compare) |
| Component coverage | Каждый visual pattern в screens покрыт классом из `components.css` |
| AA contrast PASS | `colors.html` матрица — все text/bg пары 4.5:1+ (normal) / 3:1+ (large) |
| Stitch parse PASS | `DESIGN.md` импортируется в Stitch (test-fed одного нового screen) |
| Кирилл usability | Кирилл берёт `bv-card-hero` HTML+CSS, адаптирует в React за 30 мин |
| UX-agent usability | При новой screen-task агент использует `bv-*` классы, не изобретает свои |
| Token sync PASS | tokens.css ↔ tokens.json ↔ DESIGN.md mirror друг друга |

### Risks + mitigations

| Риск | Вероятность | Митигация |
|---|---|---|
| Token drift между tokens.css / tokens.json / DESIGN.md | Средняя | Validation checklist в Stage 6 |
| Refactor ломает existing screens | Средняя | После каждого рефактора — open в браузере, side-by-side compare |
| `components.css` разрастается до 2000+ строк | Низкая | Подразделить на `components/{card,capsule,…}.css` post-Mid |
| PM-чекпоинты задерживают на 1+ день | Средняя | Делать checkpoints parallel с другими agents в работе |
| Skill objections overload PM | Средняя | Aggregate возражения в один doc в конце Stages 4-5 |
| Stitch не понимает наш DESIGN.md | Низкая | Test-parse в Stage 2 (early validation) |
| Кирилл захочет другие имена классов | Низкая | Префикс `bv-` защищает от конфликта Tailwind/shadcn |
| Figma sync несовместим с нашими токенами | Низкая | Phase 7 — после основного scope, не блокирует Mid |

### Open questions — все answered

| # | Question | Answer |
|---|---|---|
| 1 | Auto code generation pipeline | Не в Mid. Ручной sync. Wave 2 — рассмотреть `design.md export tailwind` |
| 2 | Versioning model | Semver в header comment. CHANGELOG.md когда breaking change |
| 3 | DesignSync / Figma sync | **Phase 7** — последняя фаза скоупа (после Stage 6) |
| 4 | React component library | Не в Mid. `tokens.json` + `components.css` достаточно. Кирилл импортит tokens.json для React theme |
| 5 | Storybook | Не в Mid. `components-gallery.html` выполняет 80% той же роли. Кирилл может развернуть позже для production React |

### Out of scope (для Mid)

- ❌ React component library (.tsx files)
- ❌ Storybook
- ❌ Auto-generated Tailwind config
- ❌ Dark mode (Sleep section post-MVP)
- ❌ Animation library (motion specs остаются inline на screens)
- ❌ Documentation site (README.md в `shared/` достаточно)
- ❌ Wave 2 компоненты (`bv-chart`, `bv-modal-sheet`, `bv-input`, `bv-banner`, `bv-tabs`)

---

## 5 · Acceptance & next steps

После одобрения PM этого spec:

1. **Invoke `writing-plans` skill** — детальный implementation plan с шагами под каждый Stage
2. **Execution** — следовать плану по stages с PM-чекпоинтами
3. **Финал** — commit + push to GitPages

Каждый stage завершается screenshot + PM acceptance до перехода к следующему.

---

## Appendix · Source artefacts (что вошло в анализ)

- `docs_web/bevel-clone/home/home-main-etalon.html` (ETALON, 29.06) — главный источник tokens и patterns
- `docs_web/bevel-clone/home/home-health-monitor.html` (Health Monitor с states)
- `docs_web/bevel-clone/settings/{bt-pairing,notifications,privacy}.html` (Settings sub-screens)
- `docs_web/DESIGN.md` (current high-level YAML spec)
- `docs_web/DESIGN-bevel-clone.html` (v2 baseline с HRV detail)
- Memory: `project_neiry_bevel_clone_v3`, `project_neiry_bevel_clone_header_footer_canon`, `project_neiry_typography_system`, `project_neiry_pulse_mono_font`, `project_neiry_ds_wave1_approved`
