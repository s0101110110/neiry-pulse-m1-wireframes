---
version: alpha
name: Neiry-Pulse-design-analysis
description: "Neiry Pulse — экосистема носимых биосенсоров (браслет + recovery-устройства) с тремя поверхностями: kiosk (выставочный стенд 1.5–2м, full-screen 1920×1080), corporate dashboard (плотный продуктовый интерфейс на 1440+), мобильное приложение (390×844, Android+iOS). Визуальный код — shadcn dark zinc/slate как baseline с единственным хроматическим акцентом wine `#831843`. Эстетический эталон — Linear / Vercel по продуктовой плотности и Hume Band по био-виджетам. Типографика: Space Grotesk (UI sans), Onest (display), Geist Mono (tabular numerics для пульса, HRV, NSI). Сетка 4px. Цвета хранятся как HSL-токены shadcn, тёмная тема — primary surface, light — паритетная альтернатива."

colors:
  primary: "hsl(336 76% 33%)"
  primary-hover: "hsl(336 76% 28%)"
  primary-dark: "hsl(336 76% 45%)"
  primary-dark-hover: "hsl(336 76% 52%)"
  primary-foreground: "hsl(0 0% 98%)"
  background-light: "hsl(0 0% 100%)"
  background-dark: "hsl(240 10% 3.9%)"
  foreground-light: "hsl(240 10% 3.9%)"
  foreground-dark: "hsl(0 0% 98%)"
  card-light: "hsl(0 0% 100%)"
  card-dark: "hsl(240 10% 6%)"
  muted-light: "hsl(240 4.8% 95.9%)"
  muted-dark: "hsl(240 3.7% 15.9%)"
  muted-foreground-light: "hsl(240 3.8% 46.1%)"
  muted-foreground-dark: "hsl(240 5% 64.9%)"
  border-light: "hsl(240 5.9% 90%)"
  border-dark: "hsl(240 3.7% 15.9%)"
  ring: "hsl(336 76% 33%)"
  destructive: "hsl(348 100% 54%)"
  success: "hsl(151 100% 45%)"
  warning: "hsl(42 100% 50%)"
  bio-pulse: "hsl(336 76% 45%)"
  bio-hrv: "hsl(195 90% 55%)"
  bio-stress-low: "hsl(151 100% 45%)"
  bio-stress-mid: "hsl(42 100% 50%)"
  bio-stress-high: "hsl(348 100% 54%)"
  ecg-trace: "hsl(151 100% 55%)"

typography:
  display-kiosk:
    fontFamily: "Onest, Space Grotesk, system-ui, sans-serif"
    fontSize: 180px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -6px
    fontFeatureSettings: "'tnum' 1"
  metric-xl:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 128px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -3px
    fontFeatureSettings: "'tnum' 1"
  metric-lg:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -1.5px
    fontFeatureSettings: "'tnum' 1"
  metric-md:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
    fontFeatureSettings: "'tnum' 1"
  display-xl:
    fontFamily: "Onest, Space Grotesk, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1.8px
  display-lg:
    fontFamily: "Onest, Space Grotesk, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  headline:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.4px
  card-title:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  body:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  eyebrow:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  button:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px

spacing:
  px: 1px
  0_5: 2px
  1: 4px
  2: 8px
  3: 12px
  4: 16px
  5: 20px
  6: 24px
  8: 32px
  10: 40px
  12: 48px
  16: 64px
  20: 80px
  24: 96px
  section: 120px

components:
  kiosk-metric-card:
    backgroundColor: "{colors.card-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.metric-xl}"
    rounded: "{rounded.xl}"
    padding: 48px
    border: "1px solid {colors.border-dark}"
  dashboard-kpi-card:
    backgroundColor: "{colors.card-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.metric-md}"
    rounded: "{rounded.lg}"
    padding: 20px
    border: "1px solid {colors.border-dark}"
  data-table-row:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    borderBottom: "1px solid {colors.border-dark}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-foreground}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
  button-primary-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.primary-foreground}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
  button-secondary:
    backgroundColor: "{colors.muted-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted-foreground-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
  text-input:
    backgroundColor: "{colors.card-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "10px 12px"
    border: "1px solid {colors.border-dark}"
  status-badge-low:
    backgroundColor: "hsl(151 100% 45% / 0.15)"
    textColor: "{colors.bio-stress-low}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: "2px 10px"
  status-badge-mid:
    backgroundColor: "hsl(42 100% 50% / 0.15)"
    textColor: "{colors.bio-stress-mid}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: "2px 10px"
  status-badge-high:
    backgroundColor: "hsl(348 100% 54% / 0.15)"
    textColor: "{colors.bio-stress-high}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: "2px 10px"
  gauge-ring:
    strokeWidth: 12px
    backgroundColor: "{colors.muted-dark}"
    strokeColor: "{colors.bio-pulse}"
    rounded: "{rounded.pill}"
  ecg-strip:
    backgroundColor: "{colors.card-dark}"
    strokeColor: "{colors.ecg-trace}"
    strokeWidth: 2px
    rounded: "{rounded.lg}"
    padding: 16px
  sparkline:
    strokeWidth: 1.5px
    strokeColor: "{colors.bio-pulse}"
    fillOpacity: 0.1
  top-nav:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.body-sm}"
    height: 56px
    borderBottom: "1px solid {colors.border-dark}"
  side-panel-drilldown:
    backgroundColor: "{colors.card-dark}"
    textColor: "{colors.foreground-dark}"
    rounded: "{rounded.lg}"
    padding: 24px
    border: "1px solid {colors.border-dark}"
    width: 480px
  tab-default:
    backgroundColor: transparent
    textColor: "{colors.muted-foreground-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "8px 14px"
  tab-selected:
    backgroundColor: "{colors.muted-dark}"
    textColor: "{colors.foreground-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "8px 14px"
---

## Overview

Neiry Pulse — это **продуктовая био-система**, а не маркетинговый лендинг. Поверхностей три, эстетический код единый:

1. **Kiosk** (выставочный стенд, 1920×1080, читается с 1.5–2м) — крупные tabular-цифры пульса/HRV/NSI, layered SVG-gauge, ECG-плашка с fake live-данными синусоидой. Источник истины: `wireframes/m2/kiosk.html` + `project_neiry_kiosk_design_system` memory.
2. **Dashboard** (B2B corporate, 1440+, плотный продукт) — три таба (Спорт / Офис / Драйверы-водители), KPI-strip, таблица сотрудников с sparkline-микро-графиками, drill-down side-panel с тестом Баевского. Эстетический baseline — Linear / Vercel: dark canvas, hairline borders, ноль декоративных градиентов.
3. **Mobile** (Android + iOS, 390×844) — браслет-пэйринг, BPM-карточка, HRV-форма, результат, синхронизация. iOS публикация подтверждена post-M2 (см. memory `project_neiry_ios_post_m2`).

**Единственный хроматический акцент** — `{colors.primary}` (wine `#831843`). Это бренд-якорь Neiry, **не подлежит замене** ни по совету skill'а, ни по моде на тёплые палитры 2026. На тёмном фоне используется `{colors.primary-dark}` (35%→45% lightness) для контрастности.

**Bio-палитра** — четыре служебных hue для биометрики: `{colors.bio-pulse}` (пульс/HR, тот же wine), `{colors.bio-hrv}` (HRV, cyan), `{colors.bio-stress-low/mid/high}` (NSI mint→amber→red). Цвета привязаны к семантике, не к декору.

**Типографика** — три family: **Space Grotesk** (UI body/buttons), **Onest** (display/headlines), **Geist Mono** (любые числа с tabular-nums — пульс не должен прыгать при смене 78→79).

**Сетка** — 4px base, 24px gutter в карточках, 48px в kiosk-блоках. Spacing-токены кратны 4.

**Key Characteristics:**
- Dark-first интерфейс. Light-тема существует, но primary surface — `{colors.background-dark}`.
- Wine как единственный chromatic accent. Никаких вторых акцентных hue ради «премиума».
- Tabular numerics на всех биометриках (Geist Mono + `font-feature-settings: 'tnum' 1`).
- Layered SVG-gauge с outer-ring (стресс) + inner-ring (HR-zone) — фирменный био-виджет.
- ECG-плашка с псевдо-live-данными — fake sin-волна для визуального витализма стенда.
- Hairline-borders (1px `{colors.border-dark}`), нулевые decorative shadows. Иерархия через surface ladder.
- 4px grid строго. Отступы кратны 4. Никаких 18px / 22px / 30px.

## Colors

> Источники истины: `wireframes/m2/ui-kit.html` (canonical CSS-переменные), memory `project_neiry_ui_aesthetic`, `project_neiry_kiosk_design_system`.

### Brand & Accent
- **Wine Primary** (`{colors.primary}` `hsl(336 76% 33%)` / `#831843`) — единственный chromatic accent. CTA, focus rings, фокусные элементы. **НЕ менять.**
- **Wine Primary Dark** (`{colors.primary-dark}` `hsl(336 76% 45%)`) — wine на тёмном фоне (повышенная lightness для контраста).
- **Wine Hover** (`{colors.primary-hover}` / `{colors.primary-dark-hover}`) — hover-state в light / dark темах.

### Surface (Dark — primary)
- **Background** (`{colors.background-dark}` `hsl(240 10% 3.9%)`) — главное полотно. На нём всё.
- **Card** (`{colors.card-dark}` `hsl(240 10% 6%)`) — поднятые поверхности: KPI-карточки, side-panel, kiosk-блоки.
- **Muted** (`{colors.muted-dark}` `hsl(240 3.7% 15.9%)`) — фон вторичных кнопок, выбранных табов.
- **Border** (`{colors.border-dark}` `hsl(240 3.7% 15.9%)`) — все hairline-разделители. 1px, не 2px.

### Surface (Light — паритет)
- Те же роли (`{colors.background-light}` / `{colors.card-light}` / `{colors.muted-light}` / `{colors.border-light}`).
- Wine остаётся `#831843` без сдвига lightness.

### Text
- **Foreground** (`{colors.foreground-dark}` `hsl(0 0% 98%)`) — основной текст и метрики на тёмном фоне.
- **Muted Foreground** (`{colors.muted-foreground-dark}` `hsl(240 5% 64.9%)`) — вторичные подписи, лейблы осей, единицы (BPM, мс).

### Semantic
- **Destructive** (`{colors.destructive}` `#FF1744`) — критические алерты, ошибки, NSI High.
- **Success** (`{colors.success}` `#00E676`) — нормальные значения, NSI Low.
- **Warning** (`{colors.warning}` `#FFB300`) — пограничные значения, NSI Mid.

### Bio (служебная палитра биометрик)
- `{colors.bio-pulse}` — пульс / HR. Тот же wine для семантической связки бренда и главной метрики.
- `{colors.bio-hrv}` — HRV. Cyan `hsl(195 90% 55%)`.
- `{colors.bio-stress-low/mid/high}` — NSI ladder. Мapped на semantic success/warning/destructive.
- `{colors.ecg-trace}` — линия ЭКГ на kiosk-плашке. Mint `hsl(151 100% 55%)` для визуального витализма.

## Typography

### Font Families
- **Onest** — display family. Headlines kiosk и dashboard hero. Fallback: Space Grotesk → system-ui.
- **Space Grotesk** — UI body, buttons, labels. Fallback: system-ui → -apple-system.
- **Geist Mono** — **обязательно** для всех числовых метрик (BPM, мс HRV, NSI score, минуты). `font-feature-settings: 'tnum' 1, 'lnum' 1` всегда.

### Hierarchy

| Token | Size | Weight | LH | Tracking | Use |
|---|---|---|---|---|---|
| `{typography.display-kiosk}` | 180px | 600 | 1.0 | -6px | Kiosk большая метрика (BPM на стенде) |
| `{typography.metric-xl}` | 128px | 500 | 1.0 | -3px | Kiosk вторичная метрика (HRV) |
| `{typography.metric-lg}` | 64px | 500 | 1.0 | -1.5px | Drill-down side-panel главная цифра |
| `{typography.metric-md}` | 32px | 500 | 1.1 | -0.5px | Dashboard KPI-card цифра |
| `{typography.display-xl}` | 56px | 600 | 1.1 | -1.8px | Hero headline (mobile splash) |
| `{typography.display-lg}` | 40px | 600 | 1.15 | -1px | Section opener |
| `{typography.headline}` | 24px | 600 | 1.25 | -0.4px | Dashboard tab title, mobile screen heading |
| `{typography.card-title}` | 18px | 500 | 1.3 | -0.2px | KPI-card label, mobile-form label |
| `{typography.body}` | 14px | 400 | 1.5 | 0 | Default body, table cells |
| `{typography.body-sm}` | 13px | 400 | 1.45 | 0 | Dense table rows, footer columns |
| `{typography.caption}` | 12px | 400 | 1.4 | 0.1px | Captions, axis labels, units |
| `{typography.eyebrow}` | 11px | 500 | 1.3 | 0.6px | Section eyebrow, mono uppercase |
| `{typography.button}` | 14px | 500 | 1.2 | 0 | All button labels |

### Principles
- **Tabular nums везде, где цифра обновляется в реальном времени.** Иначе BPM 78→79 «прыгает».
- **Negative tracking растёт с размером.** -6px на kiosk-180px ≈ 3.3% от size.
- **Eyebrow — это единственный mono в маркетинговой иерархии.** Остальной mono — внутри метрик.
- **Onest и Space Grotesk — один голос.** Семья переключается тихо.

## Layout

### Spacing System
- **Base unit:** 4px. Все отступы кратны 4 — никаких 18px / 22px / 30px.
- **Tokens (frontmatter):** `1`=4px, `2`=8px, `3`=12px, `4`=16px, `5`=20px, `6`=24px, `8`=32px, `10`=40px, `12`=48px, `16`=64px, `20`=80px, `24`=96px, `section`=120px.
- **Kiosk-блок:** 48px внутренний padding, 64px между блоками.
- **Dashboard KPI-card:** 20px padding, 16px gutter в strip.
- **Side-panel:** 24px padding, 480px ширина.
- **Mobile-screen:** 16px горизонтальный padding, 24px между секциями.

### Grid & Container
- **Kiosk:** viewport-fit 1920×1080. 12-column grid, 24px gutter, 48px outer padding.
- **Dashboard:** max-content 1440px, 12-column, 16px gutter. KPI-strip — 4-up на desktop, 2-up на tablet.
- **Mobile:** 390×844 baseline, единый column с 16px margins.

### Whitespace Philosophy
Тёмное полотно **и есть** whitespace. Секции отделяются подъёмом на `{colors.card-dark}` (surface ladder), не белыми гэпами. Гэп внутри карточки — `{spacing.6}` (24px), между секциями kiosk — `{spacing.16}` (64px), между секциями dashboard — `{spacing.12}` (48px).

## Components

### Kiosk (Stand)
- `kiosk-metric-card` — крупная метрика с layered SVG-gauge, ECG-плашкой, status-badge. Padding 48px, border 1px hairline.
- `gauge-ring` — двойное кольцо (outer = NSI, inner = HR-zone), stroke 12px.
- `ecg-strip` — fake sin-волна, mint stroke, 2px. Запрос: визуальная живость без реальных данных.
- State machine: `empty` (нет браслета) → `live` (данные идут) → `drilldown` (тест Баевского).

### Dashboard (Corporate)
- `dashboard-kpi-card` — четыре в строке, цифра + дельта + sparkline.
- `data-table-row` — 12px×16px padding, hairline borderBottom, hover bg `{colors.muted-dark}`.
- `side-panel-drilldown` — 480px right slide-in, сотрудник profile + тест Баевского.
- `tab-default` / `tab-selected` — три таба (Спорт / Офис / Драйверы).
- `status-badge-low/mid/high` — NSI status pills, контраст 4.5:1 минимум.
- `sparkline` — 1.5px stroke, 0.1 fillOpacity, без осей.

### Mobile (App)
- `button-primary-dark` — на wine background, белый текст. CTA в pairing/login.
- `text-input` — card bg, hairline border, focus ring wine.
- `kiosk-metric-card` адаптация для BPM-карточки (180px → 96px на 390px ширине).

### Shared
- `button-primary` / `button-secondary` / `button-ghost` — три кнопочные роли, без четвёртой.
- `top-nav` — 56px height, hairline borderBottom.

## Principles

1. **Wine — единственный chromatic accent.** Никаких вторых брендовых hue. Bio-палитра — служебная, не декоративная.
2. **Tabular nums обязательны** на всех живых метриках. `font-feature-settings: 'tnum' 1` на Geist Mono.
3. **Hairline-borders, не shadows.** Иерархия через surface ladder (`background` → `card` → `muted`).
4. **4px grid строго.** Дизайн-агент проверяет арифметику пикселей через viewBox-math (см. memory `feedback_neiry_design_iteration_workflow`).
5. **Skills — подсказка, не закон.** Если skill советует тёплую палитру / убрать tnum / поменять шрифт — игнорировать. Источник истины: этот файл + `wireframes/m2/ui-kit.html`.
6. **PM acceptance gate.** Любая правка визуала идёт через preview → ждём «принято» → потом commit. Никогда не пушим до явного OK PM.
7. **Dark-first, light — паритет.** Wine остаётся wine в обеих темах. Surface ladder параллельна.
8. **Mobile = Android + iOS.** При компонентных решениях учитывать HIG (action sheets, back-gesture) где конфликтует с Material.

## Anti-patterns

- ❌ Inline-styles (`<div style="...">`) — только Tailwind / CSS-переменные.
- ❌ Менять `--primary` / шрифты M2 даже «временно для эксперимента».
- ❌ Добавлять gradients ради «премиума». Surface ladder делает работу.
- ❌ Сокращать плотность данных в dashboard в угоду «дыхания» — это медицинский интерфейс, не лендинг.
- ❌ Заменять Geist Mono на Inter в метриках. Цифры будут прыгать.
- ❌ Использовать `impeccable init / document / craft / extract` без явного OK PM — затрёт DESIGN.md.
- ❌ Превентивный вызов skill'ов «на всякий случай» — экономия токенов.

## Notes on Substitutes

- Onest и Space Grotesk — open-source, Google Fonts. Geist Mono — Vercel, open-source.
- На системах без шрифтов fallback `system-ui` → `-apple-system` приемлем, но **метрики обязательно** в mono-fallback (`ui-monospace`).

## Version & Source-of-Truth

- `version: alpha` — первая итерация. После acceptance PM статус → `stable`.
- **Source-of-truth для CSS:** `wireframes/m2/ui-kit.html`. Этот DESIGN.md синхронизируется с ним.
- **Memory якоря:** `project_neiry_ui_aesthetic`, `project_neiry_ui_stack`, `project_neiry_kiosk_design_system`, `feedback_neiry_design_iteration_workflow`.
- Изменения вносятся только PM. UI-агент читает, не правит.
