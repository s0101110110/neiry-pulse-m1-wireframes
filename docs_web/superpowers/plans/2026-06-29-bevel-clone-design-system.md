# Bevel-clone Design System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Вынести design tokens и atomic components из ETALON-экрана `home-main-etalon.html` в shared `_shared/` layer, отрефакторить existing screens чтобы они потребляли shared CSS, и собрать 4 live cheatsheets + README.

**Architecture:** Hybrid — живая DS в `docs_web/bevel-clone/_shared/` (`tokens.css` + `components.css` + 4 live HTML cheatsheets) + `DESIGN.md` как machine-readable mirror для Stitch. Screens подключают shared CSS через `<link>`. Никаких inline styles per-screen для shared компонентов.

**Tech Stack:** HTML5, CSS3 (CSS Custom Properties), JSON, Markdown. Шрифты Golos Text + Pulse Mono (local woff2). Никаких build-tools / npm в Mid scope.

**Spec:** `docs_web/superpowers/specs/2026-06-29-bevel-clone-design-system-design.md`

---

## File Structure (что создаётся/меняется)

### Создаётся

```
docs_web/bevel-clone/_shared/
├── tokens.css              # CSS-переменные (single runtime source)
├── tokens.json             # JSON mirror (для Stitch / Кирилл React)
├── components.css          # 14 атомарных .bv-* классов + модификаторы
├── colors.html             # live палитра + AA-матрица
├── typography.html         # live type-scale (Golos + Pulse Mono)
├── states.html             # 5 status states cheatsheet
├── components-gallery.html # каталог 14 компонентов (live)
└── README.md               # index + usage docs
```

### Модифицируется (refactor под shared CSS)

```
docs_web/DESIGN.md                                  # обновить под cool-gray v3 + новые tokens
docs_web/bevel-clone/home/home-main-etalon.html     # подключить tokens.css + components.css
docs_web/bevel-clone/home/home-health-monitor.html  # то же
docs_web/bevel-clone/settings/settings-bt-pairing.html       # то же
docs_web/bevel-clone/settings/settings-notifications.html    # то же
docs_web/bevel-clone/settings/settings-privacy.html          # то же
docs_web/bevel-clone/settings/settings-sub-screens-gallery.html  # iframe-only, не трогаем
docs_web/bevel-clone/index.html                              # обновить под наполнение
```

### НЕ трогать

- `docs_web/DESIGN-bevel-clone.html` (v2 baseline — остаётся как исторический референс)
- `docs_web/DESIGN-preview.html`
- `docs_web/DESIGN-explorations.html`
- `docs_web/font-pairs-comparison.html`
- `docs_web/wireframes/m2/ui-kit.html`
- `docs_web/fonts/pulse-mono/` (уже скопированы)
- `docs_web/bevel-clone/_shared/components-preview-DRAFT.html` (брайнсторм-артефакт)

---

## Workflow split

| Stage | Куда делегировать | Почему |
|---|---|---|
| 1 — Tokens extraction | **Второе окно UI_assets** (formal skills) | Designer's eye для именования + impeccable polish |
| 2a — tokens.json mirror | Subagent тут | Mechanical transformation |
| 2b — DESIGN.md update | **Второе окно UI_assets** | Stitch-критическая точность |
| 2c — colors.html | Subagent тут | Mechanical palette + AA |
| 3 — Components extraction | **Второе окно UI_assets** | impeccable polish/harden критичен |
| 4a — components-gallery.html | **Второе окно UI_assets** | typeset/polish |
| 4b — states.html | **Второе окно UI_assets** | colorize/harden |
| 4c — typography.html | **Второе окно UI_assets** | typeset формально |
| 5a — refactor home-main-etalon | Subagent тут | Mechanical refactor |
| 5b — refactor home-health-monitor | Subagent тут | Mechanical refactor |
| 5c — refactor settings × 3 | Subagent тут (или parallel × 3) | Mechanical refactor |
| 6 — README + validation | Тут | Финал |
| 7 — Figma sync | TBD (отдельная фаза) | После Stage 6 acceptance |

**PM-чекпоинты:** после Stages **1, 3, 4, 5, 6** (и 7 отдельно). Чекпоинты не блокируют parallel-работу — короткий screenshot review (1-2 мин).

---

# Stage 1 · Tokens extraction → `_shared/tokens.css`

**Цель:** Извлечь все CSS-vars из `home-main-etalon.html` в single source `_shared/tokens.css` с категоризацией и semver-header.

**Делегировать:** Второе окно UI_assets (formal skills: `impeccable polish/harden`).

### Task 1.1: Подготовить task brief для второго окна

**Files:**
- Read: `docs_web/bevel-clone/home/home-main-etalon.html` (lines 40-110 — секция TOKENS)

- [ ] **Step 1:** Открыть `home-main-etalon.html` локально, прочитать секцию `:root { … }` (с line 42 примерно — до конца блока TOKENS).
- [ ] **Step 2:** Скопировать в PM-чат полный текст brief'а (он ниже в Task 1.2).
- [ ] **Step 3:** Передать в чат UX-агента во втором окне.
- [ ] **Step 4:** Ждать report DONE от агента (скриншот + tokens.css path).

### Task 1.2: Task brief для UX-агента (второе окно)

Скопировать в чат UI_assets-сессии:

```
Файл-цель: создать /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css

Source: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-main-etalon.html (секция TOKENS, :root { ... } блок)

Задача:
1. Прочитать etalon полностью (особенно :root блок).
2. Создать tokens.css со следующей структурой:

   /*!
    * Neiry Pulse · Bevel-clone · tokens
    * v1.0.0 — 2026-06-29 — initial extraction from home-main-etalon
    * Source of truth для CSS-переменных. Все --bv-* префиксированы.
    */
   :root {
     /* ========= 1 · Brand & Accent ========= */
     /* Wine — единственный chromatic accent. Используется только в bottom nav active. */
     --bv-wine: ...;
     --bv-wine-tint: ...;     /* 8% wine для chip-bg */

     /* ========= 2 · Surface ========= */
     --bv-bg-screen: #F0F0F3;   /* cool-gray screen bg */
     --bv-bg-card: #FFFFFF;     /* card surface */
     /* ... */

     /* ========= 3 · Ink (text) ========= */
     --bv-ink: ...;
     --bv-ink-mute: ...;
     --bv-ink-dim: ...;
     --bv-ink-faded: ...;

     /* ========= 4 · Semantic colors ========= */
     /* Status semantics — НЕ chromatic accent, не используется в brand. */
     --bv-sem-norm: ...;          /* green fill */
     --bv-sem-norm-ink: ...;      /* green AA text variant */
     --bv-sem-warn: ...;          /* orange fill (Ниже/Выше) */
     --bv-sem-warn-ink: ...;      /* orange AA text */
     --bv-sem-high: ...;          /* red fill (Внимание/Critical) */
     --bv-sem-high-ink: ...;      /* red AA text */
     /* No-data: используем ink-faded */

     /* ========= 5 · Capsule colors ========= */
     /* Capsule track + fill colors. */
     --bv-capsule-track: ...;     /* empty/inactive */
     --bv-capsule-fill-norm: ...;
     --bv-capsule-fill-warn: ...;
     --bv-capsule-fill-high: ...;

     /* ========= 6 · Avatar ========= */
     --bv-avatar-bg: #D5E3F0;     /* light blue (Bevel real) */
     --bv-avatar-ink: #3A6FA0;

     /* ========= 7 · Border / hairline ========= */
     --bv-hairline: #E5E5EA;      /* cool-tone hairline для всех cards */

     /* ========= 8 · Shadows ========= */
     /* Использовать как одну переменную через box-shadow прямо. */
     --bv-shadow-card: 0 1px 3px rgba(22,22,32,.03), 0 6px 18px rgba(22,22,32,.04);
     --bv-shadow-nav: 0 4px 16px rgba(22,22,32,.08);
     --bv-shadow-header: 0 1px 2px rgba(22,22,32,.04);

     /* ========= 9 · Radii ========= */
     --bv-r-card: 20px;       /* HRV hero + 6 bento — единый */
     --bv-r-card-sm: 18px;
     --bv-r-pill: 999px;
     --bv-r-nav: 30px;        /* floating bottom nav */

     /* ========= 10 · Spacing (4px grid) ========= */
     --bv-sp-1: 4px;
     --bv-sp-2: 8px;
     --bv-sp-3: 12px;
     --bv-sp-4: 16px;
     --bv-sp-5: 20px;
     --bv-sp-6: 24px;
     --bv-sp-8: 32px;
     --bv-sp-section: 28px;   /* между секциями screen */

     /* ========= 11 · Typography families ========= */
     --bv-font-sans: 'Golos Text', system-ui, sans-serif;
     --bv-font-mono: 'Pulse Mono', 'JetBrains Mono', ui-monospace, monospace;

     /* ========= 12 · Typography sizes ========= */
     --bv-fs-display-hero: 60px;     /* HRV hero "47" — pre-size-reduction value */
     --bv-fs-section-h2: 28px;       /* "Монитор показателей" */
     --bv-fs-metric-bento: 28px;     /* bento mini-card цифры */
     --bv-fs-headline: 17px;         /* app-bar title */
     --bv-fs-label: 14px;            /* card labels */
     --bv-fs-body: 14px;
     --bv-fs-caption: 12px;
     --bv-fs-eyebrow: 11px;
     --bv-fs-tab-label: 10px;        /* bottom nav labels */
     --bv-fs-capsule-bounds: 11px;   /* 55/35 labels в HRV hero capsule */

     /* ========= 13 · Typography weights ========= */
     --bv-fw-regular: 400;
     --bv-fw-medium: 500;
     --bv-fw-semibold: 600;
     --bv-fw-bold: 700;

     /* ========= 14 · Typography rhythm ========= */
     --bv-lh-tight: 1;       /* для крупных цифр */
     --bv-lh-display: 1.1;
     --bv-lh-body: 1.5;
     --bv-ls-tight: -0.6px;  /* section header */
     --bv-ls-eyebrow: 0.6px; /* uppercase eyebrows */

     /* ========= 15 · Icon stroke ========= */
     --bv-icon-stroke: 1.7;  /* universal line-icon stroke-width */
   }

3. Извлечь РЕАЛЬНЫЕ значения из etalon, заполнить ВСЕ переменные выше. Если в etalon нет — оставить placeholder с TODO-комментарием для PM.
4. ВСЕ переменные с префиксом `--bv-`.
5. Категории комментариями обязательно.
6. Versioning header в начале.

Skills формально (применять последовательно):
- Skill impeccable args:"polish docs_web/bevel-clone/_shared/tokens.css" — финальная вылизка комментариев и порядка
- Skill impeccable args:"harden docs_web/bevel-clone/_shared/tokens.css" — проверка на edge cases (missing tokens, malformed values)

Возражения skill'ов — собрать в HTML-комментарии в конце файла (там где можно положить comment block без поломки CSS).

Self-review:
- [ ] Все 15 категорий покрыты значениями (не TODO)
- [ ] Префикс --bv-* везде
- [ ] Header semver есть
- [ ] Категории прокомментированы
- [ ] Никаких inline styles в файле кроме :root

НЕ КОММИТИТЬ. Вернуть путь к файлу + screenshot (открыть в браузере просто — это CSS, можно показать VSCode превью).
```

- [ ] **Step 1:** Скопировать blok выше в чат UX-агента
- [ ] **Step 2:** Ждать DONE report

### Task 1.3: PM checkpoint — review tokens.css

- [ ] **Step 1:** Открыть `_shared/tokens.css` в редакторе
- [ ] **Step 2:** Verify по чек-листу:
  - 15 категорий присутствуют
  - Все значения заполнены (нет TODO)
  - Naming consistent (все `--bv-*`)
  - Comments есть для каждой категории
- [ ] **Step 3:** PM acceptance — продолжаем или правки

### Task 1.4: Commit tokens.css

Run:
```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY
git add docs_web/bevel-clone/_shared/tokens.css
git commit -m "DS Stage 1: tokens.css extracted from home-main-etalon"
```
Expected: 1 file changed.

- [ ] **Step 1:** Run git add + commit
- [ ] **Step 2:** Verify with `git log --oneline -1`

---

# Stage 2 · Tokens mirror (parallel ×3)

**Цель:** Создать tokens.json (JSON mirror) + обновить DESIGN.md (Stitch-input) + colors.html (live палитра + AA).

**Параллельно:** 3 задачи независимы — можно запустить одновременно.

### Task 2A: tokens.json (mechanical mirror)

**Делегировать:** Subagent тут (general-purpose).

**Files:**
- Read: `docs_web/bevel-clone/_shared/tokens.css`
- Create: `docs_web/bevel-clone/_shared/tokens.json`

- [ ] **Step 1:** Dispatch subagent через Agent tool с prompt:

```
Прочитай /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css.

Создай /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.json со структурой:

{
  "$meta": {
    "name": "Neiry Pulse · Bevel-clone · tokens",
    "version": "1.0.0",
    "date": "2026-06-29",
    "source": "tokens.css mirror"
  },
  "brand": {
    "wine": "#831843",
    "wineTint": "rgba(131,24,67,0.08)"
  },
  "surface": {
    "bgScreen": "#F0F0F3",
    "bgCard": "#FFFFFF"
  },
  "ink": { ... },
  "semantic": { ... },
  "capsule": { ... },
  "avatar": { ... },
  "hairline": "#E5E5EA",
  "shadow": {
    "card": "0 1px 3px rgba(22,22,32,.03), 0 6px 18px rgba(22,22,32,.04)",
    "nav": "...",
    "header": "..."
  },
  "radius": { "card": 20, "cardSm": 18, "pill": 9999, "nav": 30 },
  "spacing": { "1": 4, "2": 8, ..., "section": 28 },
  "typography": {
    "families": { "sans": "...", "mono": "..." },
    "sizes": { "displayHero": 60, ... },
    "weights": { "regular": 400, ... },
    "rhythm": { "lhTight": 1, ... }
  },
  "iconStroke": 1.7
}

Категории и имена ключей соответствуют категориям в tokens.css. Извлекать ТОЛЬКО значения, никакой логики.

Self-verify: каждая переменная из tokens.css должна иметь соответствующий ключ в JSON. grep -c "^  --bv-" tokens.css должно равняться количеству leaf-keys в JSON.

НЕ коммитить. Доклад: DONE + path к файлу + count tokens matched.
```

- [ ] **Step 2:** Ждать DONE report.
- [ ] **Step 3:** Verify file existence: `ls docs_web/bevel-clone/_shared/tokens.json`.

### Task 2B: DESIGN.md update (UX-агент во втором окне)

**Делегировать:** Второе окно UI_assets (formal `impeccable harden`).

**Files:**
- Modify: `docs_web/DESIGN.md`
- Read: `docs_web/bevel-clone/_shared/tokens.css`

- [ ] **Step 1:** Скопировать в чат UX-агента второго окна:

```
Файл-цель: обновить /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/DESIGN.md
Source: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css

Задача:
1. Прочитать tokens.css (только что созданный)
2. Прочитать текущий DESIGN.md (он на старой палитре зачастую)
3. Синхронизировать DESIGN.md YAML frontmatter под значения из tokens.css:
   - colors: section — заменить hsl values на новые из tokens.css (cool-gray surface, semantic palette)
   - typography: фамилии Golos Text + Pulse Mono (заменить если есть Onest/Geist)
   - rounded: значения из tokens.css
   - spacing: значения из tokens.css
   - components: пройти по 14 bv-компонентам, заполнить если нет
4. Обновить markdown body (Overview / Colors / Typography / Layout / Components / Principles / Anti-patterns) — отразить cool-gray v3 + multi-semantic palette
5. **Замкнутые константы НЕ нарушать:** wine #831843 только в brand-anchor зоне, Golos+Pulse Mono only, light-first для mobile

Skill: 
- Skill impeccable args:"harden docs_web/DESIGN.md" — проверка на edge cases в YAML + парсимость для Stitch

Self-review:
- [ ] tokens.css ↔ DESIGN.md mirror — все category матчатся
- [ ] YAML frontmatter parsable (нет нарушений indentation)
- [ ] Markdown body отражает actual design (не устаревшие dark-only упоминания)

НЕ КОММИТИТЬ. Вернуть screenshot YAML frontmatter (первые ~150 строк).
```

- [ ] **Step 2:** Ждать DONE report.
- [ ] **Step 3:** Verify locally: open `docs_web/DESIGN.md`, проверить frontmatter.

### Task 2C: colors.html (palette + AA matrix)

**Делегировать:** Subagent тут.

**Files:**
- Create: `docs_web/bevel-clone/_shared/colors.html`
- Read: `docs_web/bevel-clone/_shared/tokens.css`

- [ ] **Step 1:** Dispatch subagent через Agent tool с prompt:

```
Создай /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/colors.html — live палитра + AA-контраст матрица.

Source: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css

Структура страницы:
1. Hero: "Bevel-clone colors — палитра + AA"
2. Секция 1 — Все цвета как swatches, grouped (Brand / Surface / Ink / Semantic / Capsule / Avatar / Hairline). Каждый swatch:
   - Цветной круг 60×60
   - Имя переменной (--bv-wine)
   - HEX / rgba value
   - Описание роли
3. Секция 2 — AA-контраст матрица. Таблица:
   - Rows: text colors (ink / ink-mute / sem-norm-ink / sem-warn-ink / sem-high-ink / wine)
   - Cols: background colors (bg-screen / bg-card / wine-tint / sem-norm chip / sem-warn chip / sem-high chip)
   - Cells: contrast ratio + ✅/⚠️/❌ (AAA = >7.0, AA = >4.5, FAIL = <4.5)
4. Секция 3 — Каждый "FAIL" highlighted с примечанием "не для текста, только icon / decorative"

Подключить tokens.css через <link rel="stylesheet" href="tokens.css"> чтобы values из переменных. Тексты + heading в Golos Text + Pulse Mono для hex кодов.

Light bg #F0F0F3, light cards #FFFFFF, шрифты из docs_web/fonts/pulse-mono/ через @font-face (тот же блок что в home-main-etalon.html — путь будет ../../fonts/pulse-mono/ ... wait, относительно _shared/ это будет ../../fonts/pulse-mono/).

Actually корректный path от _shared/colors.html к fonts: `../../fonts/pulse-mono/`. Verify the relative path работает.

Self-review:
- [ ] Все цвета из tokens.css представлены как swatches
- [ ] AA-матрица содержит 6×6 минимум cells, computed contrast
- [ ] FAIL cells явно помечены и объяснены

НЕ коммитить. Screenshot через Chrome headless в /tmp/colors-html-draft.png. Доклад: DONE + path + count swatches + count AA cells.
```

- [ ] **Step 2:** Ждать DONE report.
- [ ] **Step 3:** Open colors.html в браузере, sanity check.

### Task 2.D: Commit Stage 2 artefacts

Run:
```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY
git add docs_web/bevel-clone/_shared/tokens.json docs_web/bevel-clone/_shared/colors.html docs_web/DESIGN.md
git commit -m "DS Stage 2: tokens.json mirror + DESIGN.md sync + colors.html cheatsheet"
```

- [ ] **Step 1:** Run commit
- [ ] **Step 2:** `git log --oneline -1`

---

# Stage 3 · Components extraction → `_shared/components.css`

**Цель:** Извлечь 14 атомарных компонентов (с модификаторами) в `components.css`.

**Делегировать:** Второе окно UI_assets (formal `impeccable polish/harden`).

### Task 3.1: Brief для UX-агента второго окна

Скопировать в чат UI_assets-сессии:

```
Файл-цель: создать /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/components.css

Sources:
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css (используем переменные)
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-main-etalon.html (source styles)
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-health-monitor.html (для bento detail)
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/settings/settings-bt-pairing.html (для bv-row + bv-icon-square + bv-toggle)

Задача: создать components.css с 14 атомарными компонентами + модификаторами. Все стили должны использовать var(--bv-*) из tokens.css.

Версионинг header:
/*!
 * Neiry Pulse · Bevel-clone · components
 * v1.0.0 — 2026-06-29 — initial extraction
 * Зависит от: tokens.css
 */

Структура components.css (14 компонентов):

/* ========= GROUP A — Surface & Layout ========= */
.bv-screen { /* full screen wrapper */ }
.bv-card { /* base card: bg, hairline, radius, shadow */ }
.bv-card--hero { /* HRV hero variant: larger padding */ }
.bv-card--bento { /* mini bento variant: smaller padding/height */ }
.bv-section-header { /* H2 Golos 700 inline left */ }

/* ========= GROUP B — Chrome ========= */
.bv-app-bar { /* base header */ }
.bv-app-bar--pill { /* home-style: pill round + calendar + date + share + avatar */ }
.bv-app-bar--back { /* sub-screens: back-arrow + title + optional info */ }
.bv-nav-pill { /* bottom floating pill container */ }
.bv-nav-item { /* tab inside nav */ }
.bv-nav-item.is-active { /* wine icon + label + wine-tint chip bg */ }
.bv-avatar { /* circle 32x32 with initials */ }

/* ========= GROUP C — Health Monitor ========= */
.bv-capsule { /* base vertical pill indicator */ }
.bv-capsule--full { /* with bounds labels (55/35) — для HRV hero */ }
.bv-capsule--mini { /* compact — для bento */ }
.bv-capsule__track { /* internal: track element */ }
.bv-capsule__fill { /* internal: filled segment */ }
.bv-capsule__dot { /* internal: position indicator */ }
.bv-chip { /* base chip */ }
.bv-chip--status-low { /* green Норма */ }
.bv-chip--status-mid { /* orange Ниже/Выше */ }
.bv-chip--status-high { /* red Внимание */ }
.bv-chip--status-empty { /* grey Нет данных */ }
.bv-chip--delta-up { /* green ▲ +N% */ }
.bv-chip--delta-down { /* red ▼ -N% */ }
.bv-chip--badge { /* wine badge (например v 2.4) */ }

/* ========= GROUP D — Settings ========= */
.bv-row { /* settings list-row container */ }
.bv-icon-square { /* 32x32 tinted square */ }
.bv-icon-square--default { /* cool-gray bg */ }
.bv-icon-square--wine { /* 8% wine bg */ }
.bv-icon-square--danger { /* 10% red bg */ }
.bv-icon-square--success { /* 10% green bg */ }

/* ========= GROUP E — Controls ========= */
.bv-button { /* base button */ }
.bv-button--primary { /* wine fill, white text */ }
.bv-button--secondary { /* cool-gray fill */ }
.bv-button--ghost { /* transparent */ }
.bv-toggle { /* switch container */ }
.bv-toggle.is-on { /* wine track */ }
.bv-eyebrow { /* Pulse Mono 11px UPPERCASE label */ }

/* ========= Iconography convention ========= */
.bv-icon { stroke-width: var(--bv-icon-stroke); stroke-linecap: round; stroke-linejoin: round; fill: none; }

Skills формально (последовательно):
1. Skill impeccable args:"polish docs_web/bevel-clone/_shared/components.css"
2. Skill impeccable args:"harden docs_web/bevel-clone/_shared/components.css"
3. Skill impeccable args:"colorize docs_web/bevel-clone/_shared/components.css" — проверка что все color references через --bv-* tokens

Self-review:
- [ ] Все 14 атомарных + ~14 модификаторов покрыты
- [ ] Все hex/rgba заменены на var(--bv-*)
- [ ] Header semver есть
- [ ] Внутренние элементы (__track, __fill, __dot) с BEM-double-underscore
- [ ] Никаких hardcoded values (radius/padding/color) — всё через переменные
- [ ] prefers-reduced-motion: reduce поддерживается где есть animations

Возражения skill'ов — собрать в HTML-комментарии в конце CSS.

НЕ КОММИТИТЬ. Вернуть file path + screenshot редактора с верхней частью файла (header + group A).
```

- [ ] **Step 1:** Скопировать brief в чат UX-агента
- [ ] **Step 2:** Ждать DONE report

### Task 3.2: PM checkpoint — review components.css

- [ ] **Step 1:** Открыть `_shared/components.css`
- [ ] **Step 2:** Verify checklist:
  - 14 атомарных классов присутствуют
  - Все модификаторы (--hero, --bento, --mini, --full, etc.) есть
  - var(--bv-*) везде, нет hardcoded hex
  - Header semver есть
- [ ] **Step 3:** Sanity render: открыть home-main-etalon (он пока не использует shared CSS, но visually должен выглядеть так же)
- [ ] **Step 4:** PM acceptance — продолжаем или правки

### Task 3.3: Commit components.css

Run:
```bash
git add docs_web/bevel-clone/_shared/components.css
git commit -m "DS Stage 3: components.css extracted (14 bv-* atomic)"
```

- [ ] **Step 1:** Commit
- [ ] **Step 2:** `git log --oneline -1`

---

# Stage 4 · Live demonstrations (parallel ×3)

**Цель:** 3 live cheatsheets — components-gallery / states / typography.

**Делегировать:** Второе окно UI_assets (formal skills: typeset / colorize / polish / harden).

**Параллельно:** Можно запустить все 3 brief'а в один день (UX-агент работает над ними последовательно или в trio).

### Task 4A: components-gallery.html (финализировать из DRAFT)

**Files:**
- Modify: `docs_web/bevel-clone/_shared/components-preview-DRAFT.html` → `components-gallery.html` (переименовать + улучшить)
- Read: `docs_web/bevel-clone/_shared/tokens.css`, `components.css`

- [ ] **Step 1:** Brief в чат UX-агента:

```
Файл-цель: создать /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/components-gallery.html — финализировать из DRAFT-версии.

Source DRAFT: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/components-preview-DRAFT.html (уже создан, PM accepted его как scope-preview).

Задача:
1. Прочитать DRAFT и tokens.css + components.css
2. Создать новый файл components-gallery.html со следующими отличиями от DRAFT:
   - <link rel="stylesheet" href="tokens.css"> и <link rel="stylesheet" href="components.css"> подключены
   - Все компоненты в gallery используют РЕАЛЬНЫЕ классы из components.css (.bv-card, .bv-capsule, etc.), а не custom CSS для preview
   - Под каждым компонентом — code snippet (для копирования) с HTML и actual class names
   - Header: "Bevel-clone Components · v1.0.0 · 2026-06-29"
   - Footer: ссылки на tokens.css / components.css / states.html / typography.html / colors.html
3. Сохранить иерархию групп A-E (Surface / Chrome / Health Monitor / Settings / Controls)

Skills формально (последовательно):
1. Skill impeccable args:"typeset docs_web/bevel-clone/_shared/components-gallery.html"
2. Skill impeccable args:"polish docs_web/bevel-clone/_shared/components-gallery.html"

Self-review:
- [ ] Каждый компонент использует .bv-* классы (не inline styles)
- [ ] tokens.css + components.css подключены через <link>
- [ ] Code snippets под каждым компонентом
- [ ] Грубо: открыть в браузере → визуально матчится с DRAFT (новые классы рендерятся корректно)

НЕ КОММИТИТЬ. Screenshot /tmp/components-gallery-draft.png. Доклад: DONE + path + count components rendered.
```

- [ ] **Step 2:** Ждать DONE.

### Task 4B: states.html (5 status cheatsheet)

- [ ] **Step 1:** Brief в чат UX-агента:

```
Файл-цель: создать /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/states.html — 5 status states cheatsheet.

Sources:
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/components.css
- /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-health-monitor.html (reference для states examples)

Задача:
Создать live cheatsheet всех 5 status states. Структура:

1. Hero: "Status States Cheatsheet · 5 states"
2. Каждый state — отдельный section с:
   - Title (Норма / Ниже / Выше / Внимание / Нет данных)
   - Visual: bv-capsule--mini + bv-chip--status-* + bv-icon-square (если применимо)
   - When to use (1-2 предложения)
   - Color tokens used (table: --bv-sem-norm + --bv-sem-norm-ink + --bv-capsule-fill-norm)
   - Real-data example: метрика-карточка (bv-card--bento) с этим state в полной композиции

3. Capsule logic section:
   - Formula: position = (value - min) / (max - min)
   - Examples: HRV 65.4 ms in [60, 100] → position = 14%
   - When fill direction matters (Path B — invariant orientation, как мы решили)

4. Status combo matrix (когда какой state применяется): таблица "metric × normal range × current value → state".

Подключить tokens.css + components.css через <link>.

Skills формально:
1. Skill impeccable args:"colorize docs_web/bevel-clone/_shared/states.html" — strategic color в monochromatic
2. Skill impeccable args:"harden docs_web/bevel-clone/_shared/states.html" — edge cases (No-data, boundary values)

Self-review:
- [ ] 5 states покрыты с примерами
- [ ] Capsule formula задокументирована
- [ ] Status combo matrix даёт actionable guidance для разработчика

НЕ КОММИТИТЬ. Screenshot /tmp/states-html-draft.png.
```

- [ ] **Step 2:** Ждать DONE.

### Task 4C: typography.html (type-scale demo)

- [ ] **Step 1:** Brief в чат UX-агента:

```
Файл-цель: создать /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/typography.html — live type-scale demo.

Source: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/_shared/tokens.css

Задача:
Создать live type-scale страницу, демонстрирующую все --bv-fs-* размеры:
- display-hero (60px) — пример: "47" в Pulse Mono 500
- section-h2 (28px) — пример: "Монитор показателей" в Golos 700
- metric-bento (28px) — пример: "65.4 ms"
- headline (17px) — пример: "27 Июн 2026"
- label (14px) — пример: "HRV"
- body (14px) — пример: длинный параграф
- caption (12px) — пример: "Принято 28.06"
- eyebrow (11px) — пример: "HRV СЕГОДНЯ" Pulse Mono UPPERCASE
- tab-label (10px) — пример: "Дом / Тренировка"
- capsule-bounds (11px) — пример: "55 / 35"

Каждая ступень:
- Live sample реальным шрифтом
- Token name (--bv-fs-*)
- Размер / weight / line-height / letter-spacing
- Family (Golos Text / Pulse Mono)
- Where used (короткий список screen-имён)

Отдельная section:
- Mixed sample: цельный composition (header + hero + sub-body + small caption + numbers) показывающий иерархию рядом

Pulse Mono подключить через @font-face (относительный path ../../fonts/pulse-mono/...).

Skills формально:
1. Skill impeccable args:"typeset docs_web/bevel-clone/_shared/typography.html"
2. Skill impeccable args:"polish docs_web/bevel-clone/_shared/typography.html"

Self-review:
- [ ] Все 10 ступеней type-scale покрыты
- [ ] Каждая ступень с token name + sample + metadata
- [ ] Mixed composition демонстрирует иерархию

НЕ КОММИТИТЬ. Screenshot /tmp/typography-html-draft.png.
```

- [ ] **Step 2:** Ждать DONE.

### Task 4.D: PM checkpoint — 3 cheatsheets review

- [ ] **Step 1:** Открыть в браузере: components-gallery.html, states.html, typography.html, colors.html (последний из Stage 2)
- [ ] **Step 2:** Verify визуально + проверить что shared CSS правильно подключён в каждом
- [ ] **Step 3:** PM acceptance — все 4 cheatsheets ✅

### Task 4.E: Commit Stage 4

Run:
```bash
git add docs_web/bevel-clone/_shared/components-gallery.html \
        docs_web/bevel-clone/_shared/states.html \
        docs_web/bevel-clone/_shared/typography.html
git commit -m "DS Stage 4: 3 live cheatsheets (components-gallery + states + typography)"
```

- [ ] **Step 1:** Commit.

---

# Stage 5 · Screen refactor (parallel ×3)

**Цель:** Перевести existing screens на shared CSS. Visual regression PASS обязателен.

**Делегировать:** 3 subagent'а тут (parallel).

### Task 5A: refactor home-main-etalon.html

**Files:**
- Modify: `docs_web/bevel-clone/home/home-main-etalon.html`

- [ ] **Step 1:** Dispatch subagent с prompt:

```
Задача: рефакторить /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-main-etalon.html чтобы использовал shared CSS вместо собственных стилей.

Что делаем:
1. Прочитать tokens.css + components.css из _shared/ — увидеть какие переменные/классы доступны
2. В home-main-etalon.html:
   - Заменить inline :root { --... } блок (~lines 42-95) на <link rel="stylesheet" href="../_shared/tokens.css">
   - Заменить inline component CSS блоки (cards, capsules, badges, nav) на <link rel="stylesheet" href="../_shared/components.css">
   - В HTML body: заменить custom class names на .bv-* классы (например div.card-hero → div.bv-card.bv-card--hero)
   - Сохранить семантику разметки (структура секций не меняется)
3. Удалить весь inline CSS, который теперь покрыт shared — должно остаться только:
   - @font-face блок (Pulse Mono)
   - Глобальные resets если есть
   - Animations (@keyframes для breathing) если хочется оставить на этом screen-уровне
   - Page-level layout (max-width / margin auto для phone-mockup frame)

Visual regression check (обязательно):
- ДО refactor — открыть home-main-etalon.html в браузере, сделать screenshot /tmp/etalon-before-refactor.png
- ПОСЛЕ refactor — снова screenshot /tmp/etalon-after-refactor.png
- Сравнить ВИЗУАЛЬНО — должны быть identical (или максимально близко)
- Если есть отличия — описать ЧТО изменилось и почему

Self-review:
- [ ] inline tokens заменены на <link> к tokens.css
- [ ] inline component styles заменены на <link> к components.css
- [ ] HTML body использует .bv-* class names
- [ ] Visual regression PASS (или explained differences)

НЕ коммитить. Доклад: DONE + before/after screenshots + diff summary.
```

- [ ] **Step 2:** Ждать DONE.
- [ ] **Step 3:** Visual review screenshots.

### Task 5B: refactor home-health-monitor.html

- [ ] **Step 1:** Dispatch subagent с аналогичным prompt'ом, но для `home-health-monitor.html`. Полный prompt:

```
Задача: рефакторить /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/home/home-health-monitor.html на shared CSS.

Аналогично Task 5A:
1. Прочитать _shared/tokens.css + components.css
2. Заменить inline tokens + component styles на <link> к shared
3. HTML body использует .bv-* classes
4. Visual regression check: before/after screenshots /tmp/health-monitor-before-refactor.png / -after-

НЕ коммитить.
```

- [ ] **Step 2:** Ждать DONE.

### Task 5C: refactor settings × 3

- [ ] **Step 1:** Dispatch subagent с prompt:

```
Задача: рефакторить 3 файла в /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/bevel-clone/settings/ на shared CSS:
- settings-bt-pairing.html
- settings-notifications.html
- settings-privacy.html

Для каждого:
1. Прочитать _shared/tokens.css + components.css
2. Заменить inline tokens + component styles на <link>
3. HTML body на .bv-* classes (особенно: bv-row, bv-icon-square--*, bv-toggle, bv-app-bar--back)
4. Visual regression для каждого: before/after screenshots /tmp/settings-{name}-before/-after-.png

НЕ коммитить.

settings-sub-screens-gallery.html НЕ ТРОГАТЬ (это iframe-only file).
```

- [ ] **Step 2:** Ждать DONE.

### Task 5.D: PM checkpoint — visual regression review

- [ ] **Step 1:** Открыть все рефакторённые screens рядом со screenshots-before в браузере (или просмотреть screenshots side-by-side)
- [ ] **Step 2:** Verify нет visual regressions
- [ ] **Step 3:** PM acceptance ✅ либо запросить fixes

### Task 5.E: Commit Stage 5

Run:
```bash
git add docs_web/bevel-clone/home/home-main-etalon.html \
        docs_web/bevel-clone/home/home-health-monitor.html \
        docs_web/bevel-clone/settings/settings-bt-pairing.html \
        docs_web/bevel-clone/settings/settings-notifications.html \
        docs_web/bevel-clone/settings/settings-privacy.html
git commit -m "DS Stage 5: refactor 5 screens onto shared CSS (visual regression PASS)"
```

- [ ] **Step 1:** Commit.

---

# Stage 6 · Documentation + validation

### Task 6.1: README.md в _shared/

**Files:**
- Create: `docs_web/bevel-clone/_shared/README.md`

- [ ] **Step 1:** Создать README.md с содержанием:

```markdown
# Bevel-clone Design System · _shared

**Version:** 1.0.0
**Date:** 2026-06-29
**Source spec:** `docs_web/superpowers/specs/2026-06-29-bevel-clone-design-system-design.md`

## What's here

| File | Purpose | Audience |
|---|---|---|
| `tokens.css` | CSS-переменные (single runtime source) | Все screens, UX-агент |
| `tokens.json` | JSON mirror (для React / Tailwind / Stitch) | Кирилл, AI tools |
| `components.css` | 14 атомарных .bv-* классов | Все screens, UX-агент |
| `colors.html` | Live палитра + AA-матрица | PM, Кирилл a11y |
| `typography.html` | Live type-scale demo | PM, дизайнер samples |
| `states.html` | 5 status states cheatsheet | UX-агент |
| `components-gallery.html` | Каталог 14 компонентов (live) | UX-агент, Кирилл, PM |

## How to use

### Новый screen — UX-агент

В новом HTML файле подключи:
\`\`\`html
<link rel="stylesheet" href="../_shared/tokens.css">
<link rel="stylesheet" href="../_shared/components.css">
\`\`\`

Дальше используй `.bv-*` классы — не пиши custom стили для cards/capsules/buttons/etc.

### React (Кирилл)

Импорт tokens:
\`\`\`js
import tokens from './tokens.json';

const card = {
  background: tokens.surface.bgCard,
  borderRadius: tokens.radius.card,
  // ...
};
\`\`\`

Или CSS classes напрямую (если используешь className + .bv-card в bundle).

### AI / Stitch

Подавай `docs_web/DESIGN.md` — это YAML mirror tokens.css в Stitch-формате.

## Принципы

1. **bv-* prefix** — все классы и переменные с префиксом. Защита от Tailwind/shadcn конфликтов.
2. **No inline tokens** — если values runtime — `var(--bv-*)` через tokens.css. Никаких hardcoded hex/px в components.css или screens.
3. **Semantic colors only в content** — wine только в bottom nav active. Статусы — semantic (green/orange/red/grey).
4. **4px grid строго** — все spacing/sizing кратны 4.
5. **Visual regression** — изменение в shared должно проверяться на минимум одном screen перед commit.

## Versioning

См. header в каждом из tokens.css / tokens.json / components.css. Bump version при изменениях:
- patch (1.0.x) — visual tweak existing token value
- minor (1.x.0) — добавлен новый компонент / token
- major (x.0.0) — breaking change (rename / removal)

## Roadmap (post-Mid)

Wave 2 компоненты (когда появятся новые screens):
- bv-chart (HRV detail / Sleep trend)
- bv-modal-sheet (explainer modals)
- bv-input / bv-checkbox (Sign Up / Onboarding)
- bv-banner (Demo data warning)

После Mid:
- Phase 7 — Figma sync (Tokens Studio plugin)
- Wave 2 — React component library + Storybook (когда production React стартует)
```

- [ ] **Step 2:** Save file.

### Task 6.2: Final visual regression

- [ ] **Step 1:** Открыть в браузере подряд (например через `bevel-clone/index.html`):
  - home-main-etalon.html
  - home-health-monitor.html
  - settings-bt-pairing.html
  - settings-notifications.html
  - settings-privacy.html
  - components-gallery.html
  - states.html
  - typography.html
  - colors.html
- [ ] **Step 2:** Verify визуально что всё рендерится корректно (нет broken shared CSS links, нет 404 на fonts, нет CSS resolution issues)
- [ ] **Step 3:** PM acceptance ✅

### Task 6.3: Update index.html (bevel-clone gallery)

**Files:**
- Modify: `docs_web/bevel-clone/index.html`

- [ ] **Step 1:** Добавить в gallery новые карточки для `_shared/` cheatsheets:
  - colors.html
  - typography.html
  - states.html
  - components-gallery.html
  - README.md
- [ ] **Step 2:** Update счётчики (Принято / Дата сборки)
- [ ] **Step 3:** Save.

### Task 6.4: Commit + push Stage 6

Run:
```bash
git add docs_web/bevel-clone/_shared/README.md docs_web/bevel-clone/index.html
git commit -m "DS Stage 6: README.md + updated gallery + final validation"
git push origin main
```

- [ ] **Step 1:** Commit + push.
- [ ] **Step 2:** Verify на GitPages через 1-2 минуты.

### Task 6.5: PM final acceptance + share

- [ ] **Step 1:** Открыть https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/bevel-clone/ в браузере
- [ ] **Step 2:** PM проходит по всем 9 экранам/cheatsheets
- [ ] **Step 3:** PM acceptance — Mid DS ✅
- [ ] **Step 4:** Можно делиться ссылкой с Кириллом / Никитой

---

# Phase 7 · Figma sync (после Stage 6 acceptance)

**Цель:** Перенести tokens в Figma через Tokens Studio plugin.

**Делегировать:** Отдельная фаза, после Mid acceptance. Может быть PM выполнит сам или делегирует.

### Task 7.1: Установить Tokens Studio plugin

- [ ] **Step 1:** В Figma → Plugins → Browse → search "Tokens Studio" → install
- [ ] **Step 2:** Open plugin в любом Figma file (тестовом)

### Task 7.2: Import tokens.json в Tokens Studio

- [ ] **Step 1:** В Tokens Studio plugin → Settings → JSON tab → paste содержимое `docs_web/bevel-clone/_shared/tokens.json`
- [ ] **Step 2:** Plugin покажет parsed structure — verify все категории корректны
- [ ] **Step 3:** Apply tokens к selected layers в test-file → verify рендерятся правильные values

### Task 7.3: Configure GitHub sync (optional)

- [ ] **Step 1:** В Tokens Studio → Settings → Sync → GitHub → подключить s0101110110/neiry-pulse-m1-wireframes
- [ ] **Step 2:** Указать path `docs_web/bevel-clone/_shared/tokens.json`
- [ ] **Step 3:** Test pull — изменения из репо автоматически подхватываются в Figma

### Task 7.4: Документировать workflow

- [ ] **Step 1:** Дописать в `_shared/README.md` секцию "Figma sync (Phase 7)":
  - Plugin: Tokens Studio
  - Sync source: `tokens.json` в репо
  - Workflow: PM/дизайнер правит в Figma → push → tokens.json обновляется → screens автоматически отражают
- [ ] **Step 2:** Commit + push README update.

### Task 7.5: PM final Phase 7 acceptance

- [ ] **Step 1:** Демо: показать что Figma file использует те же tokens что и HTML screens
- [ ] **Step 2:** PM acceptance ✅

---

## Success criteria (overall)

После Stage 6:
- [ ] `_shared/` папка содержит 8 файлов (tokens.css + tokens.json + components.css + 4 cheatsheets + README)
- [ ] 5 existing screens рефакторены на shared CSS
- [ ] Visual regression PASS — все screens рендерятся идентично pre-refactor
- [ ] AA contrast PASS — все pairs в colors.html матрице
- [ ] Stitch parse PASS — DESIGN.md успешно импортируется в Stitch (test-fed)
- [ ] Token sync PASS — tokens.css ↔ tokens.json ↔ DESIGN.md mirror
- [ ] Pushed to GitPages — gallery accessible

После Phase 7:
- [ ] Tokens Studio в Figma sync с tokens.json
- [ ] README документирует Figma workflow
- [ ] PM/Никита могут редактировать tokens в Figma → автоматически в screens

---

## Spec self-review

After writing this plan, verified:
- [x] Все секции spec покрыты tasks (Architecture / Component scope / Build order / Validation / Open Q answered / Phase 7)
- [x] Нет placeholders — каждая task с exact file paths + exact commands + concrete content
- [x] Type consistency — class names (.bv-card, .bv-capsule__dot и т.д.) согласованы между stages
- [x] PM checkpoints обозначены (после 1, 3, 4, 5, 6)
- [x] Workflow split явно (formal-skills tasks → второе окно, mechanical → subagents здесь)
- [x] Self-verifiable — каждая task с self-review checklist

---

## Execution

Plan complete and saved to `docs_web/superpowers/plans/2026-06-29-bevel-clone-design-system.md`. Two execution options:

**1. Subagent-Driven (recommended)** — Я dispatch a fresh subagent per task, review между tasks, fast iteration. Для formal-skills tasks (Stages 1, 2b, 3, 4) — я генерирую paste-ready prompts для тебя → ты копируешь во второе окно UI_assets → возвращаешь report.

**2. Inline Execution** — Выполняем tasks в этой сессии последовательно с checkpoints для review. Для formal-skills tasks — тот же hand-off через второе окно.

**Какой подход?**
