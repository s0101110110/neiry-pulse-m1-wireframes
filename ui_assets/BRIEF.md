# UX TASK BRIEF — Обновить DESIGN-preview.html под новые токены

**Дата:** 2026-06-16
**От:** PM (Константин)
**Приоритет:** ВЫСОКИЙ — следующий шаг разблокирован после выбора шрифта Никитой

---

## Контекст — три стратегических сдвига

1. **Mobile = light-mode primary** (требование Никиты). Dark остаётся, но опциональный toggle. Kiosk + dashboard остаются dark-first.
2. **Шрифтовая пара утверждена Никитой:** **Golos Text + JetBrains Mono** (заменяет старые Onest + Space Grotesk + Geist Mono).
3. **Whoop+Bevel synthesis принят PM — вариант D:** точечная пересадка, всё в одном `DESIGN.md`. Overlay-файл НЕ делаем.

**Текущая задача:** обновить только `docs_web/DESIGN-preview.html`. `DESIGN.md` НЕ трогаем — это следующая задача после acceptance preview.

---

## Файл для правки

**Единственный файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/DESIGN-preview.html`

Текущая версия: dark-first, Onest+Space Grotesk+Geist Mono. Нужно переписать под новые токены и добавить 4 мобильных HTML-мокапа реальных экранов.

---

## 5 решений PM (источник истины)

### 1. Surface map
| Поверхность | Tone | Donor lean | Mode |
|---|---|---|---|
| Kiosk (1920×1080) | hardcore-data | Whoop ~90% | **Dark** |
| Dashboard (1440+) | плотный профи | Whoop 60% / Bevel 40% | **Dark** |
| Mobile Home | wellness-companion | Bevel 70% / Whoop 30% | **Light** |
| Mobile Detail | data-rich дружелюбный | 50/50 | **Light** |

### 2. Glassmorphic
- Применяется на **mobile home hero card** + **ВСЕ modal sheets** (HRV explainer, Sleep explainer, любые modals).
- НЕ применяется на dashboard / kiosk / обычных карточках mobile.

### 3. Recovery-ring
- **Одинарное кольцо.** Outer ring = NSI semantic ramp (green/yellow/red). Внутреннего HR-zone кольца НЕТ.

### 4. Customizable cards
- Пост-MVP. **НЕ добавляем** сейчас.

### 5. Архитектура
- Variant D — всё в одном `DESIGN.md`, без overlay-файла. Donor-компоненты пометить HTML-комментарием `<!-- from Whoop -->` или `<!-- from Bevel -->`.

---

## Что нужно сделать в DESIGN-preview.html

### A. Hero и token chips
- Hero на light cream/off-white bg (например `#FAFAF7`), не dark.
- Подзаголовок: «light-mode primary для mobile, dark для kiosk + dashboard».
- Token chips: **Golos Text · JetBrains Mono · wine #831843 · 4px grid · light-first mobile**.

### B. Палитра
- Добавить light-mode surfaces (`background-light: #FFFFFF`, `card-light: #FAFAF7`, `border-light: #E8E4DE`, `ink-light: #1A1815`, `ink-mute-light: #6B6660`).
- Сохранить dark-mode параллельно (для kiosk + dashboard).
- **Bio-палитра на light bg — проверить контраст AA**. Success `#00E676` на белом не проходит — затемнить до `#00A653`. Warning `#FFB300` на белом тоже слабо — затемнить до `#E89500`. Destructive `#FF1744` → `#D1003C`.
- HRV cyan на light — поставить `#0288A8` для контраста.
- Wine `#831843` — оставить, на белом контраст 9.3:1 (AA passed).

### C. Типографика
- Обновить hierarchy table под Golos + JetBrains Mono:
  - `display-kiosk` 180px / Golos 700 / -6px (kiosk hero)
  - `metric-xl` 128px / JetBrains 500 / -3px tnum (kiosk metric)
  - `metric-lg` 64px / JetBrains 500 / -1.5px tnum (mobile hero metric)
  - `metric-md` 32px / JetBrains 500 tnum (KPI)
  - `display-xl` 56px / Golos 700 / -1.5px (mobile hero text)
  - `display-lg` 40px / Golos 600 / -1px
  - `headline` 24px / Golos 600
  - `body` 14-15px / Golos 400
  - `caption` 12px / Golos 400
  - `eyebrow` 11px / JetBrains 500 / +0.6px UPPERCASE
  - `button` 14px / Golos 500
- Каждый sample показать живым шрифтом через Google Fonts CDN.
- Убрать упоминания Onest, Space Grotesk, Geist Mono.

### D. Spacing — без изменений
4px base сохраняется.

### E. Components на light bg
- Кнопки: wine remains wine, текст белый (контраст OK).
- Badges: low/mid/high — пересчитать контраст на белом фоне.
- Cards: белые с 1px hairline-border (`#E8E4DE`), не dark.
- ECG-плашка: light bg, mint `#00A653` stroke.

### F. **Главное — секция «На реальных экранах»**

Вставить новый `<section>` с **4 phone-mockups**:

| # | Reference screen | Surface | Что демонстрирует |
|---|---|---|---|
| 1 | `01-home.png` | Mobile Home (light) | **Glass hero card** (HRV 47ms + +12% к вчера + body), workout card (Сегодня лёгкий бег + sparkline + CTA «Начать тренировку»), warning row, sleep row, bottom nav |
| 2 | `20b-hrv-detail.png` | Mobile Detail (light) | Large hero metric «52» ms + 2 deltas, 30-day chart с baseline-line, 3 stat cards (52/48/45 ms), insight card «HRV выше нормы» с wine border, learn-more link |
| 3 | `20c-hrv-explainer-modal.png` | Modal sheet (**glassmorphic**) | Modal с frosted-glass поверх dimmed HRV detail. «КАК ЭТО РАБОТАЕТ» eyebrow + X close, «Что такое HRV?» heading, body с wine highlights, bullets ▲●▼, disclaimer, «Понятно» wine button |
| 4 | `03a-training-active-page1-zones.png` | Mobile Active (Whoop-leaning) | Live workout HR-zones screen — показывает Whoop heritage даже на mobile light-mode. Текущий BPM крупно, текущая зона (Z2/Z3/Z4), таймер, кнопка stop |

**Технические требования к мокапам:**

- Это **HTML-мокапы, не embed PNG**. Шрифты применяются через cascade.
- Phone bezel: `#1A1815`, border-radius 32-36px, padding 6-8px.
- Screen внутри: light bg `#FFFFFF` или `#FAFAF7`, border-radius 26-30px.
- Status bar mock (9:41 / notch / signal-wifi-battery).
- Bottom nav: Дом / История / Sharing / Ещё (Дом active с wine).
- **Glass effect** (для home hero + modal):
  ```css
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.5);
  ```
- Все живые метрики (47, 52, 78 bpm и т.д.) — `font-family: 'JetBrains Mono'; font-variant-numeric: tabular-nums;`.
- Все остальные текста — `font-family: 'Golos Text'`.

**Готовый референс по phone-мокам** можешь подсмотреть в `docs_web/font-pairs-comparison.html` — там полноценные `.phone` + `.s-statusbar` + `.s-card` классы. Заимствуй / адаптируй стили оттуда под light-bg.

### G. Principles
- 1. «Wine — единственный chromatic accent» — без изменений
- 2. «Tabular nums на живых метриках» — без изменений
- 3. «Hairline-borders, не shadows» — без изменений (на light bg тем более — никаких heavy shadows)
- 4. «4px grid» — без изменений
- 5. **Переписать:** «**Light-first для mobile, dark для kiosk + dashboard**. Wine остаётся wine в обеих темах.»
- 6. **Новый:** «**Glassmorphic — только mobile home hero + ВСЕ modal sheets**. Dashboard и kiosk — flat surfaces.»
- 7. Skills — без изменений
- 8. Mobile = Android + iOS — без изменений

### H. Anti-patterns — обновить
- Добавить: «❌ Применять glassmorphic вне home hero и modals — размывает медицинскую серьёзность».
- Удалить: устаревшее про Geist Mono / Onest, заменить на Golos / JetBrains Mono.

---

## Защищённые элементы — НЕ трогать

- ❌ Wine `#831843` — НЕ менять.
- ❌ 4px base grid.
- ❌ Семантика bio-палитры (HEX могут чуть подвинуться для AA на light, но роли те же).
- ❌ Файл `docs_web/DESIGN.md` — отдельная задача.
- ❌ Файл `docs_web/font-pairs-comparison.html` — закрыт.
- ❌ Файл `wireframes/m2/ui-kit.html` — отдельная задача.
- ❌ Memory или global rules.

---

## Контрольный список (self-review до DONE)

- [ ] Все цвета на light bg проходят WCAG AA (4.5:1 для body, 3:1 для large text)
- [ ] `font-variant-numeric: tabular-nums` на ВСЕХ живых метриках (47, 52, 78, 7ч 42м и т.д.)
- [ ] Glass effect ТОЛЬКО на mobile home hero + modal sheets (больше нигде)
- [ ] Recovery-ring если рендеришь — одинарный outer NSI semantic ramp
- [ ] Все отступы кратны 4 (никаких 18/22/30px)
- [ ] НЕ добавлен второй chromatic accent помимо wine
- [ ] НЕ добавлены customizable cards / drag-handles
- [ ] Все 4 phone-мокапа рендерятся как HTML с применёнными через cascade Golos + JetBrains Mono
- [ ] Donor-компоненты помечены `<!-- from Whoop -->` или `<!-- from Bevel -->`
- [ ] Бренд «Neiry Pulse» в hero
- [ ] Light bg — `#FAFAF7` или `#FFFFFF` (не cream, не warm-cream)

---

## Skills (опционально, по необходимости)

После того как собрал draft DESIGN-preview.html:
- `Skill impeccable args:"critique docs_web/DESIGN-preview.html"` — UX-критика, иерархия, ясность
- `Skill impeccable args:"audit docs_web/DESIGN-preview.html"` — технический (a11y, контраст, responsive)
- `Skill impeccable args:"harden docs_web/DESIGN-preview.html"` — edge cases (overflow, i18n)

**Хард-баны (НЕ использовать):**
- ❌ `init`, `document`, `craft`, `extract`, `live`, `pin`, `overdrive` — перепишут DS
- ❌ `Skill impeccable` без аргумента — подтянет 87KB SKILL.md (token waste)
- ❌ `emil-design-eng` — это статика, не моушн

**Принимать советы skill критически:**
- Если skill советует убрать tnum, поменять wine, добавить gradient, сделать «warmer palette», заменить шрифты — **игнорировать**, пометить `REJECTED_BY_AGENT` в докладе.

---

## Ожидаемый выход (формат доклада)

1. Обновлённый файл `docs_web/DESIGN-preview.html`
2. **Screenshot страницы в чат PM** (один или несколько)
3. Доклад в одном из форматов:
   - `DONE — готово, всё по спеке, ждём acceptance`
   - `DONE_WITH_CONCERNS — готово, но: [список]`
   - `NEEDS_CONTEXT — заблокирован вопросом: [конкретные вопросы]`
   - `BLOCKED — невозможно из-за: [причина]`
4. **НЕ коммитить** до явного «принято» от PM (memory `feedback_neiry_preview_before_push.md`)

---

## Дедлайн

Не критичный, но желательно сегодня — Никита ждёт следующий артефакт на ревью.
