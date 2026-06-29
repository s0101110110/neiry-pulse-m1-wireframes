# Bevel-clone Design System · `_shared/`

**Version:** 1.0.4 (29.06.2026)
**Scope:** Mid (M3 sprint) — mobile-only, light-mode primary
**Spec:** `docs_web/superpowers/specs/2026-06-29-bevel-clone-design-system-design.md`

---

## Что здесь

| Файл | Что | Audience |
|---|---|---|
| `tokens.css` | CSS-переменные — runtime source-of-truth (73 переменных, 15 категорий) | Все screens (через `<link>`), UX-агент |
| `tokens.json` | JSON mirror tokens.css | Кирилл React (import theme), Stitch, AI-tools |
| `components.css` | 14 атомарных `.bv-*` классов + 25 модификаторов + 8 BEM elements | Все screens (через `<link>`), UX-агент |
| `colors.html` | Live палитра + AA-контраст матрица 7×6 | PM-ревью, Кирилл a11y check |
| `typography.html` | Live type-scale (10 ступеней + mixed composition) | PM-ревью, дизайнер samples |
| `states.html` | 5 status-states cheatsheet + capsule formula + combo-matrix | UX-агент при сборке screens |
| `components-gallery.html` | Каталог 14 компонентов (live, с code snippets) | UX-агент, Кирилл, PM |
| `typography-rows-compare.html` | A vs B sub-text comparison (12px vs 10px) — для исторической справки | PM (archive) |
| `README.md` | Этот файл — index + usage | Onboarding |

---

## Как использовать

### Новый screen (UX-агент)

В HTML файле подключи:
```html
<link rel="stylesheet" href="../_shared/tokens.css">
<link rel="stylesheet" href="../_shared/components.css">
```

Дальше используй `.bv-*` классы — не пиши custom CSS для cards/capsules/buttons/etc. Все размеры/цвета/тени уже учтены.

**Пример:**
```html
<div class="bv-card bv-card--hero">
  <span class="bv-eyebrow">HRV сегодня</span>
  <div class="bv-metric-hero">47<span class="bv-metric-unit">ms</span></div>
</div>
```

### React (Кирилл)

Импорт tokens:
```js
import tokens from './tokens.json';

const cardStyle = {
  background: tokens.surface.bgCard,
  borderRadius: tokens.radius.card,        // 20
  border: `1px solid ${tokens.hairline.primary}`,
  boxShadow: tokens.shadow.card,
};
```

Или CSS classes напрямую (если используешь className + .bv-card в bundle).

### AI / Stitch

Скармливай `docs_web/DESIGN.md` — это YAML mirror tokens.css в Stitch-формате (с конвенцией `bv-*` без двойного dash для YAML парсимости).

---

## Принципы

1. **`bv-` prefix везде.** Защита от конфликтов с Tailwind / shadcn / utility-CSS.
2. **No inline tokens** — если value runtime, `var(--bv-*)` через `tokens.css`. Никаких hardcoded hex/px в screens.
3. **Wine — только в 8 зонах** (см. Wine Policy в DESIGN.md):
   - bottom nav-active
   - chip--badge
   - button--primary
   - toggle ON
   - app-bar--back (icons + tint)
   - button--ghost (text)
   - icon-square--wine
   - eyebrow--brand
   В content (status colors, metrics, capsule fills) wine **запрещён**.
4. **Semantic colors only в content** — green/orange/red/grey для status.
5. **4px grid строго** — все spacing/sizing кратны 2 или 4.
6. **Sub-screen nav-hide** — на settings/detail screens bottom nav-pill скрывается, остаётся только back-arrow.
7. **Visual regression check** — изменение в `_shared/` обязано тестироваться на минимум одном screen перед commit.

---

## Tabs канон (5)

Bottom nav на **Home screens** использует строго эти 5 tabs:

| # | Label | Icon |
|---|---|---|
| 1 | Дом | home outline / filled when active |
| 2 | Тренировка | activity / dumbbells |
| 3 | История | list / clock |
| 4 | Здоровье | heart |
| 5 | Ещё | dots |

Active state — wine **color** на icon + label (без chip-background).

На **sub-screens** (settings detail, modal sheets) bottom nav **скрыт**.

---

## Versioning

Header в `tokens.css` / `tokens.json` / `components.css`:
```
v1.0.4 — 2026-06-29 — PM patch (Stage 5 visual review)
```

Bump rules:
- **patch (1.0.x)** — visual tweak existing token value (например ink-dim AA-fix)
- **minor (1.x.0)** — добавлен новый компонент / token (например +bv-r-button)
- **major (x.0.0)** — breaking change (rename / removal класса или token)

Текущая история:
- v1.0.0 — initial extraction from home-main-etalon (29.06)
- v1.0.1 — ink-dim AA-fix, +toggle-track-off, section-h2 28→24
- v1.0.2 — +radius.button 14 + radius.icon 10
- v1.0.3 — +wine-hover, +ink-on-wine, +shadow-dot
- v1.0.4 — fs-label 14→12, fs-headline 17→16 (Option B sub-text 10px via inline на settings)

---

## A11y notes

- **Empty-state «Нет данных»** использует `--bv-ink-faded` (#B5B5BD, contrast 1.95:1 на белом — ниже WCAG 3:1 для большого текста). Это намеренно — empty-state должен быть subtle. Информация дублируется иконкой + пустой капсулой (double-encoded), что соответствует WCAG guidance.
- **`:focus-visible`** работает только если host элемент focusable (`<button>`, `tabindex=0`). DS-guidance: для `.bv-toggle` / `.bv-row` host должен быть `<button role="switch">` или `<div tabindex="0" role="button">`.
- Все semantic-цвета (norm/warn/high) проходят AA на cards и screens — см. `colors.html` матрицу.

---

## Roadmap (post-Mid)

### Wave 2 компоненты (когда появятся screens)
- `bv-chart` — HRV detail / Sleep trend chart
- `bv-modal-sheet` — HRV/Sleep explainer modals
- `bv-input` / `bv-checkbox` — Sign Up / Onboarding
- `bv-banner` — Demo data warning / Wellness disclaimer
- `bv-tabs` — sub-screen tabs (если понадобится)

### После Mid
- **Phase 7 — Figma sync** — Tokens Studio plugin import `tokens.json` → tokens доступны в Figma
- **Wave 2 — React component library** — когда стартует production React-development
- **Storybook** — опц., если Кирилл разработает live-каталог компонентов в React

### Backlog (low-priority)
- `bv-link` — для wine-цветных inline links (footer-ссылки, learn-more)
- `bv-toggle-track-on` — отдельный токен на случай если ON-track будет отличаться от `--bv-wine`
- `capsule__dot` fallback для IE/старого Safari (color-mix не поддерживается)
- `aria-hidden` blanket на 30+ декоративных SVG иконок

---

## Помощь

Источник истины для архитектурных вопросов — `docs_web/superpowers/specs/2026-06-29-bevel-clone-design-system-design.md`.

История изменений — `git log` по файлам `_shared/*`.

Эталон-implementation для новых screens — `docs_web/bevel-clone/home/home-main-etalon.html`.
