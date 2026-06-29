---
version: v1.0.3
name: Neiry-Pulse-bevel-clone-design-system
description: "Neiry Pulse — мобильное приложение био-мониторинга (Android + iOS, 390×844). Дизайн-направление — Bevel-clone v3: прохладно-серый surface (#F0F0F3) + белые карточки на мягких тенях, мультисемантическая палитра (green/orange/red severity), light-mode primary. Wine #831843 — единственный хроматический акцент (бренд-якорь), живёт в bottom-nav active + chip-badge. Типографика: Golos Text (заголовки + UI/body) + Pulse Mono (все числа и табличные данные). Сетка 4px. Этот файл — YAML-зеркало docs_web/bevel-clone/_shared/tokens.css (--bv-* → bv-*) для Stitch / AI-tools. Dark Mode отложен на Sleep-раздел."

# ============================================================
# COLORS — зеркало tokens.css :root (--bv-* → bv-*)
# Все hex в кавычках (YAML: # = комментарий вне кавычек).
# ============================================================
colors:
  # Brand & Accent — wine = единственный chromatic accent
  bv-wine: "#831843"
  bv-wine-tint: "#F7E3EC"           # ≈8% wine — bg nav-active и chip-bg
  bv-wine-hover: "#6E0F37"          # darken wine — :hover button--primary (v1.0.3)
  bv-ink-on-wine: "#FFFFFF"         # текст на wine-фоне (v1.0.3)
  # Surface — cool-gray v3
  bv-bg-screen: "#F0F0F3"           # экран
  bv-bg-card: "#FFFFFF"             # карточки / pills
  bv-bg-subtle: "#E8E8EE"           # разделители, empty-chip bg
  # Ink (text)
  bv-ink: "#1B1B21"
  bv-ink-mute: "#62626C"            # вторичный (AA на белом)
  bv-ink-dim: "#6C6C76"             # третичный — AA на всех bg (≥4.5:1, PM patch v1.0.1)
  bv-ink-faded: "#B5B5BD"           # «Нет данных»
  bv-ink-soft: "#9C9CA8"            # range-cap (55/35)
  # Semantic — severity (fill / AA-ink / chip-bg)
  bv-sem-norm: "#1DA049"
  bv-sem-norm-ink: "#117A38"
  bv-sem-norm-bg: "#E5F7EE"
  bv-sem-warn: "#F2752B"
  bv-sem-warn-ink: "#C2511A"
  bv-sem-warn-bg: "#FBE9DA"
  bv-sem-high: "#E11D48"
  bv-sem-high-ink: "#C20D2E"
  bv-sem-high-bg: "#FBDDE3"
  # Capsule — track + fill per status
  bv-capsule-track: "#EAEAEF"
  bv-capsule-track-norm: "#D6F0E2"
  bv-capsule-track-warn: "#F8DEC8"
  bv-capsule-track-high: "#F4C7D0"
  bv-capsule-fill-norm: "#1DA049"
  bv-capsule-fill-warn: "#F2752B"
  bv-capsule-fill-high: "#E11D48"
  # Avatar — light blue (НЕ wine)
  bv-avatar-bg: "#D5E3F0"
  bv-avatar-ink: "#3A6FA0"
  # Border / hairline
  bv-hairline: "#E5E5EA"
  bv-hairline-2: "#EEEEF2"
  bv-toggle-track-off: "#D5D5DD"    # OFF-track bv-toggle (cool v3, PM patch v1.0.1)

# ============================================================
# SHADOWS — мягкие cool-tone (Bevel-DNA: глубина тенью, не бордером)
# ============================================================
shadows:
  bv-shadow-card: "0 1px 3px rgba(22,22,32,.03), 0 6px 18px rgba(22,22,32,.04)"
  bv-shadow-nav: "0 4px 16px rgba(22,22,32,.08)"
  bv-shadow-header: "0 1px 2px rgba(22,22,32,.04)"
  bv-shadow-dot: "0 1px 2px rgba(22,22,32,.18)"   # capsule dot-lift (v1.0.3)

# ============================================================
# TYPOGRAPHY — Golos Text + Pulse Mono only
# ============================================================
typography:
  families:
    sans: "'Golos Text', system-ui, -apple-system, sans-serif"
    mono: "'Pulse Mono', 'JetBrains Mono', ui-monospace, 'SFMono-Regular', monospace"
  sizes:
    display-hero: 60px         # HRV hero число
    section-h2: 24px           # «Монитор показателей» (PM choice из 22/24/28, v1.0.1)
    metric-bento: 28px         # цифра в bento-карточке
    headline: 17px             # app-bar-title
    label: 14px                # mcard-label
    body: 14px
    caption: 12px
    eyebrow: 11px
    tab-label: 10px            # nav tab
    capsule-bounds: 11px       # range-cap 55/35
  weights:
    regular: 400
    medium: 500
    semibold: 600
    bold: 700
    extrabold: 800             # Golos 800 — hero/display
  rhythm:
    lh-tight: 1                # метрики / hero
    lh-display: 1.1            # заголовки
    lh-body: 1.5               # body / проза
    ls-tight: "-0.6px"         # section-header / display
    ls-eyebrow: "0.6px"        # eyebrow / brand uppercase

# ============================================================
# ROUNDED — радиусы (зеркало tokens.css §9)
# ============================================================
rounded:
  bv-r-card: 20px              # ОДНО значение для HRV hero И bento
  bv-r-pill: 999px
  bv-r-nav: 30px              # footer floating pill
  bv-r-button: 14px           # CTA buttons (tokens.css v1.0.2)
  bv-r-icon: 10px             # bv-icon-square (tokens.css v1.0.2)

# ============================================================
# SPACING — 4px grid (зеркало tokens.css §10)
# ============================================================
spacing:
  bv-sp-1: 4px
  bv-sp-2: 8px
  bv-sp-3: 12px
  bv-sp-4: 16px
  bv-sp-5: 20px
  bv-sp-6: 24px
  bv-sp-8: 32px
  bv-sp-section: 28px         # section-head padding

# ============================================================
# ICON
# ============================================================
icon:
  bv-icon-stroke: 1.7         # единый stroke для line-иконок

# ============================================================
# COMPONENTS — первая волна DS (bv-* классы)
# ============================================================
components:
  bv-screen:
    backgroundColor: "{colors.bv-bg-screen}"
    note: "cool-gray wrapper, light-mode primary"
  bv-card:
    backgroundColor: "{colors.bv-bg-card}"
    border: "1px solid {colors.bv-hairline}"
    rounded: "{rounded.bv-r-card}"
    shadow: "{shadows.bv-shadow-card}"
    variants: "--hero (pad 20–22) · --base (pad 14) · --bento (pad 13, min-h 122)"
  bv-section-header:
    typography: "section-h2 24 / Golos 700 / ls -0.6"
    textColor: "{colors.bv-ink}"
  bv-app-bar:
    rounded: "{rounded.bv-r-pill}"
    shadow: "{shadows.bv-shadow-header}"
    variants: "--pill (home: glass, нейтральные иконки, avatar blue) · --back (settings: wine-tint pill + wine иконки — canon chrome)"
  bv-nav-pill:
    backgroundColor: "{colors.bv-bg-card}"   # solid white (mirror эталона, не glass)
    border: "1px solid {colors.bv-hairline}"
    rounded: "{rounded.bv-r-nav}"
    shadow: "{shadows.bv-shadow-nav}"
  bv-nav-item:
    default: "{colors.bv-ink-dim}"
    is-active: "color {colors.bv-wine} + bg {colors.bv-wine-tint}"   # WINE spot #1
  bv-avatar:
    backgroundColor: "{colors.bv-avatar-bg}"
    textColor: "{colors.bv-avatar-ink}"
    typography: "mono 12 / 600"
  bv-capsule:
    track: "{colors.bv-capsule-track}"
    fills: "norm {colors.bv-capsule-fill-norm} · warn {colors.bv-capsule-fill-warn} · high {colors.bv-capsule-fill-high}"
    variants: "--full (bounds-caps, 120px) · --mini (92px, 4 состояния)"
  bv-chip:
    variants: "--status (sem-*-bg + sem-*-ink, 5 состояний) · --delta (up green / down red, mono) · --badge (wine-tint bg + wine ink, subtle)"   # WINE zone #2 (badge)
  bv-row:
    minHeight: 56px
    padding: "14px 16px"
    border: "1px solid {colors.bv-hairline}"
    trail: "toggle / chevron / badge"
  bv-icon-square:
    size: 32px
    rounded: "{rounded.bv-r-icon}"
    tints: "default {colors.bv-bg-subtle} · wine 8% · danger 10% red · success 10% green"
  bv-button:
    rounded: "{rounded.bv-r-button}"
    variants: "--primary (solid {colors.bv-wine}) · --secondary (card + hairline) · --ghost (wine text)"
  bv-toggle:
    size: "38×22"
    on: "{colors.bv-wine} track"
    off: "{colors.bv-toggle-track-off} (#D5D5DD cool-muted)"
  bv-eyebrow:
    typography: "mono 11 UPPERCASE / ls 0.6"
    textColor: "{colors.bv-ink-mute}"
    variants: "--brand (color {colors.bv-wine}, weight 600) — для catalog headers и brand-chrome"
---

## Overview

Neiry Pulse — **мобильное приложение био-мониторинга** (Android + iOS, 390×844). Дизайн-направление — **Bevel-clone v3**: прохладно-серое полотно, белые карточки на мягких тенях, мультисемантическая палитра, light-mode по умолчанию. Эстетический референс — Bevel Health (premium, calm, glassmorphic chrome), но с нашими шрифтами и wine-якорем.

**Scope: mobile-only** (PM-confirm 29.06). Kiosk и dashboard — archived в M2-эпоху; если понадобятся позже, заводятся отдельным DESIGN-файлом, не смешиваются с этим mobile DS.

**Source-of-truth для CSS:** `docs_web/bevel-clone/_shared/tokens.css` (CSS-переменные `--bv-*`) + `components.css` (компонентные классы, _shared). Этот DESIGN.md — их **YAML-зеркало** для Stitch / AI-tools: значения совпадают 1:1, ключи `bv-*` соответствуют `--bv-*`. Эталонные экраны: `bevel-clone/home/home-main-etalon.html`, `home/home-health-monitor.html`, `hrv/hrv-detail.html`, `settings/*`.

**Ключевые принципы:**
- **Cool-gray light-first.** Полотно `{colors.bv-bg-screen}` (#F0F0F3, прохладный нейтрал — НЕ тёплый крем), карточки `{colors.bv-bg-card}` (#FFFFFF) на мягких тенях. Dark Mode отложен на Sleep-раздел (вводится override-слоем, не правкой токенов).
- **Wine — единственный хроматический акцент.** Бренд-якорь `{colors.bv-wine}` (#831843). Не подлежит замене.
- **Мультисемантика несёт смысл.** Данные/статусы/severity окрашены семантикой (green норма · orange выход за норму · red critical · grey нет данных), не одним акцентом.
- **Две гарнитуры.** Golos Text (текст + заголовки) + Pulse Mono (все числа и табличные данные). Иерархию несёт вес, не смена семейства.
- **Сетка 4px строго.** Все отступы кратны 4. Никаких 18 / 22 / 30px.

## Colors

> Source-of-truth: `_shared/tokens.css`. Палитра принята PM 26–29.06 (cool-gray v3 + multi-semantic), memory `project_neiry_bevel_clone_v3`.

### Brand & Accent
- **Wine** (`{colors.bv-wine}` #831843) — единственный chromatic accent. Solid wine появляется только в действ./бренд-зонах (см. Principles · правило wine).
- **Wine-tint** (`{colors.bv-wine-tint}` #F7E3EC) — ≈8% wine на белом: bg для nav-active и chip-bg.

### Wine Policy (8 зон)

Wine — brand-anchor **только** для action/chrome. Solid/tint wine разрешён ровно в 8 зонах (PM-canon 29.06, расширено v1.0.3 на ghost + icon-square--wine; +eyebrow--brand — components.css patch 29.06):

1. **bottom nav-active** (`bv-nav-item.is-active`) — wine текст + wine-tint bg.
2. **chip--badge** (`bv-chip--badge`) — wine-tint bg + wine ink (subtle indicator, не CTA).
3. **button--primary** (`bv-button--primary`) — solid wine + ink-on-wine текст.
4. **toggle ON** (`bv-toggle.is-on`) — wine track + knob.
5. **app-bar--back** (`bv-app-bar--back`) — wine иконки + wine-tint bg (chrome canon).
6. **button--ghost** (`bv-button--ghost`) — wine текст (tertiary action).
7. **icon-square--wine** (`bv-icon-square--wine`) — 8% wine tint + wine иконка (brand/account row).
8. **eyebrow--brand** (`bv-eyebrow--brand`) — wine текст + weight 600 (catalog headers / brand-chrome). Default `bv-eyebrow` = ink-mute 500 (in-content), wine НЕ применяется.

В **content** (metrics, status colors, capsule fills, charts) wine **ЗАПРЕЩЁН** — только semantic colors.

### Surface (cool-gray, light-first)
- **Screen** (`{colors.bv-bg-screen}` #F0F0F3) — главное полотно.
- **Card** (`{colors.bv-bg-card}` #FFFFFF) — карточки, pills, app-bar.
- **Subtle** (`{colors.bv-bg-subtle}` #E8E8EE) — разделители секций, фон empty-chip.

### Ink (text)
- **Ink** (`{colors.bv-ink}` #1B1B21) — основной текст и метрики.
- **Ink-mute** (`{colors.bv-ink-mute}` #62626C) — вторичный, AA на белом.
- **Ink-dim** (`{colors.bv-ink-dim}` #6C6C76) — третичный; AA на всех bg (≥4.5:1, patch v1.0.1).
- **Ink-faded** (`{colors.bv-ink-faded}` #B5B5BD) — «Нет данных».
- **Ink-soft** (`{colors.bv-ink-soft}` #9C9CA8) — range-cap (55/35).

### Semantic (severity)
Каждый статус несёт тройку: **fill** (графика/иконка), **ink** (AA-текст на белом ≥4.5:1), **bg** (chip-фон).
- **Норма** — `{colors.bv-sem-norm}` #1DA049 / ink #117A38 / bg #E5F7EE (green).
- **Выход за норму** (выше/ниже) — `{colors.bv-sem-warn}` #F2752B / ink #C2511A / bg #FBE9DA (orange).
- **Critical / Внимание** — `{colors.bv-sem-high}` #E11D48 / ink #C20D2E / bg #FBDDE3 (red).
- **Нет данных** — нейтральный grey (`{colors.bv-bg-subtle}` / `{colors.bv-ink-faded}`).

### Capsule (позиция в коридоре нормы)
- **Track** базовый `{colors.bv-capsule-track}` #EAEAEF; per-status треки norm #D6F0E2 / warn #F8DEC8 / high #F4C7D0.
- **Fill** norm #1DA049 / warn #F2752B / high #E11D48.

### Avatar / Hairline
- **Avatar** bg `{colors.bv-avatar-bg}` #D5E3F0 / ink #3A6FA0 — мягкий голубой (как у Bevel), **НЕ wine**.
- **Hairline** `{colors.bv-hairline}` #E5E5EA (cards/pills/nav), `{colors.bv-hairline-2}` #EEEEF2 (тонкая внутренняя). **Toggle-off** `{colors.bv-toggle-track-off}` #D5D5DD — OFF-track bv-toggle.

## Typography

### Families
- **Golos Text** — единая sans для display и UI: hero/headlines (600–800) и body/buttons/labels (400–500). Иерархия несётся весом. Fallback: system-ui → -apple-system.
- **Pulse Mono** — **обязательно** для всех чисел (BPM, мс HRV, NSI, минуты) И табличных/тайм-серийных списков целиком (время, значения, метки строк). `font-feature-settings: 'tnum' 1` всегда. Pulse Mono = JetBrains Mono с плоским нулём; локальные woff2 в `docs_web/fonts/pulse-mono/`.

### Hierarchy

| Token | Size | Use |
|---|---|---|
| `{typography.sizes.display-hero}` | 60px | HRV hero число (Golos 800 / mono) |
| `{typography.sizes.section-h2}` | 24px | «Монитор показателей» (Golos 700, ls -0.6) |
| `{typography.sizes.metric-bento}` | 28px | Цифра в bento-карточке (Pulse Mono) |
| `{typography.sizes.headline}` | 17px | app-bar-title (Golos 700) |
| `{typography.sizes.label}` | 14px | mcard-label (Golos 500) |
| `{typography.sizes.body}` | 14px | Body-текст (Golos 400) |
| `{typography.sizes.caption}` | 12px | Подписи, единицы |
| `{typography.sizes.eyebrow}` | 11px | Eyebrow (Pulse Mono UPPERCASE, ls 0.6) |
| `{typography.sizes.tab-label}` | 10px | Подпись таба nav |
| `{typography.sizes.capsule-bounds}` | 11px | range-cap 55/35 (Pulse Mono) |

**Weights:** 400 / 500 / 600 / 700 / 800. **Rhythm:** lh-tight 1 (метрики), lh-display 1.1 (заголовки), lh-body 1.5 (проза); ls-tight -0.6px (display), ls-eyebrow 0.6px (eyebrow).

## Layout

### Spacing (4px grid)
- **Base:** 4px. Все отступы кратны 4 — никаких 18 / 22 / 30px.
- **Tokens:** 1=4 · 2=8 · 3=12 · 4=16 · 5=20 · 6=24 · 8=32 · section=28 (padding section-head).
- **Mobile-screen:** 16px горизонтальный padding, gap между карточками ~10–16px (bento), 28px над section-head.

### Radii
- `{rounded.bv-r-card}` 20px — единый радиус карточек (HRV hero И bento). `{rounded.bv-r-pill}` 999px — pills/капсулы. `{rounded.bv-r-nav}` 30px — floating nav pill.
- `{rounded.bv-r-button}` 14px — CTA buttons. `{rounded.bv-r-icon}` 10px — icon-square (оба в tokens.css v1.0.2).

### Depth
Глубина — **мягкими тенями** (Bevel-DNA), не жирными бордерами: `{shadows.bv-shadow-card}` на карточках, `{shadows.bv-shadow-nav}` на floating nav, `{shadows.bv-shadow-header}` на header pill. Hairline 1px — тонкая граница, не основной разделитель.

## Components

Первая волна DS — 14 атомарных `bv-*` (scope утверждён PM 29.06, memory `project_neiry_ds_wave1_approved`). Превью: `_shared/components-preview-DRAFT.html`.

### Surface & Layout
- `bv-screen` — cool-gray wrapper полотна.
- `bv-card` (+ `--hero` / `--base` / `--bento`) — белая карточка, hairline-2, r20, shadow-card.
- `bv-section-header` — Golos 700, 24px, ls -0.6.

### Chrome (навигация)
- `bv-app-bar--pill` (home — glass, нейтральные иконки, avatar blue) / `bv-app-bar--back` (settings — wine-tint pill + wine иконки, **canon chrome**, memory `bevel-clone-header-pill-footer-floating-nav-brand-anchor`).
- `bv-nav-pill` — floating solid-white 5-tab (shadow-nav); `bv-nav-item.is-active` — **wine + wine-tint bg** (главный wine-якорь).
- `bv-avatar` — голубой, инициалы Pulse Mono.

### Health Monitor (данные)
- `bv-capsule--full` / `--mini` — вертикальная капсула «позиция в коридоре», fill снизу + dot, semantic per status.
- `bv-chip--status` (5 состояний, sem-bg + sem-ink) / `--delta` (up green / down red, mono) / `--badge` (**solid wine**).

### Settings
- `bv-row` — list-row 56px (toggle / chevron / badge).
- `bv-icon-square` — 32px r10, 4 тинта (default / wine 8% / danger 10% / success 10%).

### Controls
- `bv-button--primary` (solid wine) / `--secondary` (card + hairline) / `--ghost` (wine text).
- `bv-toggle` — 38×22, ON = wine track, OFF = `{colors.bv-toggle-track-off}` #D5D5DD.
- `bv-eyebrow` — Pulse Mono 11px UPPERCASE, ink-mute 500 (default). Вариант `--brand` — wine + weight 600 (catalog headers / chrome).

## Principles

1. **Wine — единственный chromatic accent.** Brand-anchor ровно для **7 action/chrome зон** (см. Wine Policy): nav-active · chip--badge · button--primary · toggle ON · app-bar--back · button--ghost · icon-square--wine. В **content** (metrics, status, capsule fills, charts) wine **запрещён** — только semantic colors.
2. **Мультисемантика обязательна на данных.** Severity несёт цвет (green/orange/red/grey) + иконку/текст (не только цвет — a11y). Все `-ink` варианты AA ≥4.5:1 на белом.
3. **Light-first.** Primary surface — cool-gray #F0F0F3. Dark Mode отложен на Sleep (override-слой).
4. **Tabular nums везде на живых метриках.** Pulse Mono + `'tnum' 1` — пульс не «прыгает» при 78→79.
5. **Глубина тенью, не бордером.** Soft shadows (Bevel-DNA); hairline 1px только как тонкая граница.
6. **4px grid строго.** Арифметика пикселей проверяется (memory `feedback_neiry_design_iteration_workflow`).
7. **Source-of-truth — tokens.css.** Этот DESIGN.md — зеркало. Правки значений идут в tokens.css, затем синхронизируются сюда. Skills — подсказка, не закон.
8. **PM acceptance gate.** Любой визуал идёт через preview → «принято» → commit. Не пушим до OK PM.

## Anti-patterns

- ❌ Wine в content data (metrics / status colors / capsule fills / charts). Wine — только в 7 action/chrome зонах (см. Wine Policy).
- ❌ Тёплый крем / sand / warm-neutral surface (это Whoop/Oura, не Bevel). Только cool-gray.
- ❌ Dark Mode сейчас (до Sleep-раздела).
- ❌ Onest / Space Grotesk / Geist Mono — заменены на Golos Text + Pulse Mono.
- ❌ Single-accent на всех данных — теряется мгновенная читаемость severity.
- ❌ Inline-styles (`<div style="...">`) — только классы / CSS-переменные.
- ❌ Жирные decorative shadows / gradients ради «премиума» — soft shadow делает работу.
- ❌ 18 / 22 / 30px отступы — только 4px-grid.

## Version & Source-of-Truth

- `version: v1.0.3` — зеркало `tokens.css` v1.0.3 (73 переменных). v1.0.1: ink-dim AA-fix · toggle-track-off · section-h2 24px. v1.0.2: +r-button 14 · +r-icon 10. v1.0.3: +wine-hover · +ink-on-wine · +shadow-dot; Wine Policy → 7 зон; chip--badge → wine-tint; nav-pill → solid. Stage 1 commit a958cc0.
- **Source-of-truth CSS:** `docs_web/bevel-clone/_shared/tokens.css` (+ `components.css` — Stage 3).
- **Эталоны:** `bevel-clone/home/home-main-etalon.html` (главный), `home-health-monitor.html`, `hrv/hrv-detail.html`, `settings/*`.
- **Memory якоря:** `project_neiry_bevel_clone_v3`, `project_neiry_typography_system`, `project_neiry_pulse_mono_font`, `bevel-clone-header-pill-footer-floating-nav-brand-anchor`, `project_neiry_ds_wave1_approved`.
- Изменения значений — только в tokens.css, затем sync сюда. UI-агент читает, не правит произвольно.

<!-- ============================================================
     ВОЗРАЖЕНИЯ SKILL'ОВ (impeccable harden) — на разбор PM
     ============================================================

     1. ✅ RESOLVED (PM 29.06) — SCOPE WINE расширен до канон-списка 5 зон: nav-active ·
        chip--badge · button--primary · toggle ON · app-bar--back. В content wine запрещён.
        Зафиксировано: раздел «Wine Policy» + Principle #1 + Anti-patterns.

     2. ✅ RESOLVED (PM 29.06) — SCOPE DOC подтверждён mobile-only. Kiosk/dashboard archived
        в M2-эпоху (отдельный DESIGN-файл при необходимости). Зафиксировано в Overview · Scope.

     3. ✅ RESOLVED (v1.0.2) — RADII: --bv-r-button 14px + --bv-r-icon 10px добавлены в
        tokens.css §9, зеркалятся в YAML rounded; компоненты ссылаются на токены, не литералы.
        NB: bv-icon-square size resolved → 32px (PM decision 29.06, исправлено перед commit).

     4. ✅ RESOLVED (v1.0.1) — TOGGLE-OFF токенизирован: --bv-toggle-track-off #D5D5DD добавлен
        в tokens.css §7. Также v1.0.1: ink-dim AA-fix (#8E8E97 → #6C6C76) и section-h2 = 24px (PM choice).

     5. AVATAR DRIFT — tokens/DESIGN канон #D5E3F0/#3A6FA0; экраны home/settings пока
        #B5DAF1/#0A4C7A. Привести экраны в Stage 5 refactor (уже зафиксировано в tokens.css).

     6. YAML-КЛЮЧИ — префикс --bv-* в YAML недопустим (строка на «--» ломает парсер как
        sequence). Зеркалю как bv-* (без двойного дефиса) + все hex и отрицательные значения
        в кавычках. Mapping 1:1 однозначен, парсимость для Stitch сохранена.
     ============================================================ -->
