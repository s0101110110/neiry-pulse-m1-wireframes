# BRIEF — UX/UI Дизайнер

## Статус
🔴 **Активное задание от PM от 2026-06-04 — BRIEF #2 из M2 Handover-пакета.**

BRIEF #1 (mobile-main.html) — ✅ принят PM, закоммичен (5d706d7).

---

## Задача: рестайл дашборда корпоратов

**Источник:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/INBOX/external/.processed/neiry_pulse_v5.html` — это файл Никиты (CCO), который он сам собрал для выставки. **НЕ переписывать с нуля.** Рестайл in-place поверх его структуры (sidebar, mode switcher, drill-down side-panel, Chart.js остаются).

**Куда сохранять:** `docs_web/wireframes/m3/dashboard-corporate.html` (создать папку `m3/`).

---

## Что сделать

### P0 — обязательно

1. **Шрифт.** Сама выбери современный бесплатный UI-шрифт 2026 (требования: бесплатно для коммерции, кириллица, хороший number-set с моноширинным режимом). Используй skill `emil-design-eng`. Inter в v5 убрать.
2. **Типографика — 6 ступеней.** Сейчас в файле ~12 разных px-размеров. Свести к шкале `t-display / t-h1 / t-h2 / t-body / t-caption / t-micro` (как в `ui-kit.html`). Это значит: каждый текст в файле принадлежит одной из 6 категорий, размеры захардкожены в CSS-переменных, не в hex по месту.
3. **Tabular-nums на всех цифрах.** BPM, метрики, шаги, HRV, проценты, времена — `font-variant-numeric: tabular-nums` (или `font-feature-settings: 'tnum'`). Простыми словами: цифры одной ширины, колонки чисел не «прыгают» при изменении.
4. **Палитра.** Заменить teal `#0F766E` → wine `#831843` как primary. Свои CSS-vars Никиты → semantic shadcn-токены: `--background`, `--foreground`, `--primary`, `--muted`, `--muted-foreground`, `--card`, `--card-foreground`, `--border`, `--accent`, `--destructive`. Хардкод hex запрещён везде, кроме `--primary`.
5. **SAFETY mode — добавить данные.** Сейчас этот таб пустой. Добавь 5 водителей/операторов с метриками: fatigue (усталость), reaction time (реакция, мс), microsleep events (количество). Структура карточек как у CORP/SPORT-табов.
6. **Сохранить:** 3-mode logic (CORP/SPORT/SAFETY), Chart.js, sidebar навигацию, drill-down side-panel — это работающая логика Никиты, не ломаем.

### P1 — если время

- Расшифровка метрик в UI: «re» → «Восстановление», «st» → «Стресс», единицы (мс, шагов/день, %).
- NSI-семантика **clinical, без похабщины**:
  - НЕТ ярким заливкам фона карточек (никаких `#ECFDF5`/`#FFFBEB`/`#FEF2F2`)
  - НЕТ эмодзи, градиентам, glow, неону
  - Цвет статуса — только в маленьких индикаторах: точка 8×8, полоска 4px слева, подчёркивание числа
  - Значение метрики — нейтральный foreground, цвет только на пограничной семантике
  - Палитра приглушённая, clinical (Linear / Hume Band), не насыщенная Material
  - Текст статуса «Норма / Повышен / Высокий» — ровным subdued, без капса и `!`

### P2 — отложить в M3 (НЕ делать сейчас)

- Архетипы (3 типа на mode)
- Sparkline в drill-down
- Structural cleanup (.blink/backdrop-filter/inline-styles)

---

## Эстетика — те же правила, что R8 kiosk

- Clinical, без эмодзи и яркого декора
- Wine accent `#831843` — только на критических элементах (primary CTA, активное состояние)
- Тонкая работа с серой шкалой, не цветными заливками

---

## Технические правила (НЕ нарушать)
- ✅ HTML5 + Tailwind CDN (уже есть в v5) + Chart.js (уже есть)
- ✅ Семантические CSS-переменные через `:root { --... }`
- ❌ React/Vue
- ❌ Inline-стили (`<div style="...">`) — переноси в `<style>` блок или Tailwind-классы
- ❌ Эмодзи, градиенты, glow, неон в UI

## NDA-safe
В UI запрещено: VITRO/VANTA/VIGOR, M1/M2/M3, имена B2B-клиентов. Имена сотрудников в v5 — оставить (они не B2B-клиенты, это персонажи).

---

## Способ работы (как с R8 и BRIEF #1)

1. Сделать файл, заскриншотить ключевые состояния (CORP / SPORT / SAFETY + drill-down открыт)
2. Отправить PM в чат **ДО коммита**
3. Дождаться «принято» от PM
4. Закоммитить на `feature/m2-handover` с русским сообщением: «Добавил dashboard-corporate.html: рестайл v5 → wine + UI Kit M2»
5. Push после OK PM (или PM сам сделает финальный мерж в main)

## После выполнения
Доложить PM: DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED.

## Приёмка PM
- 3 mode-кнопки переключаются (CORP/SPORT/SAFETY)
- drill-down side-panel открывается
- SAFETY-таб содержит 5 водителей с fatigue/reaction/microsleep
- Нет хардкод hex кроме `--primary: #831843`
- Tabular-nums применены на цифрах
- Без эмодзи, ярких заливок, градиентов

**Срок:** до конца дня 2026-06-04.
