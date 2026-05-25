# BRIEF — UX/UI Дизайнер

## Статус
🔴 Активное задание от PM от 2026-05-25 (предыдущий брифинг 2026-05-24 — закрыт, скоуп заменён)

## Задача — M2 UI Restyle: UI Kit + 4 базовых экрана

Полный рестайл дизайн-системы Neiry Pulse под выставку Startup Village (28-29.05.2026). Готовим **визуально полные HTML-мокапы**, которые потом Кирилл соберёт на React 1:1.

### Скоуп (порядок исполнения)

1. 🔴 **UI Kit** (`docs_web/wireframes/m2/ui-kit.html`) — живой styleguide: токены + базовые компоненты + био-виджеты + Tremor-стиль для дашборда
2. 🔴 **Kiosk v2** (`docs_web/wireframes/m2/kiosk-v2.html`) — рестайл плазмы: 2 анкера + 1 гость, 4 состояния
3. 🔴 **Drill-down карточка гостя** (`docs_web/wireframes/m2/kiosk-drilldown.html`) — карточка + 3 фазы Bayevsky test + экран результата
4. 🟡 **Дашборд корпоратов** (`docs_web/wireframes/m3/dashboard-corporate.html`) — Neiry Unite v5: 4 KPI + 3 таба (Спорт/Офис/Драйверы) + drill-down side-panel
5. 🟢 **Mobile pairing рестайл** (in-place edit `docs_web/wireframes/m1/mobile-*.html`) — переключить на новый UI Kit + почистить дев-жаргон HRV

## Срок
**До 2026-05-26 вечера** (чтобы на стыковке 27.05 wireframes уже были в репо).

## Эстетика — финал PM 25.05.2026

### Стек React-имплементации (для понимания целевой компонентной модели)
- **Foundation:** shadcn/ui (Radix Primitives + Tailwind) — base-компоненты
- **Дашборд:** Tremor — KPI strip, sparklines, BarList
- **Кастом:** биометрические виджеты на shadcn-базе (BPM-card, NCI-gauge, status-pill)
- **Точечно:** Aceternity для 1-2 wow-эффектов на kiosk (НЕ применять на дашборде)

### Палитра — shadcn-defaults (zinc/slate) + Neiry wine accent
Использовать semantic CSS-переменные shadcn, **НЕ хардкодить hex** (кроме wine):
- `--background` / `--foreground` / `--card` / `--card-foreground`
- `--muted` / `--muted-foreground` / `--border` / `--input` / `--ring`
- `--popover` / `--secondary` / `--destructive`
- `--primary` = **#831843** (wine, Neiry brand accent)

### Темы
- **Тёмная** — для kiosk на плазме 42" (далёкая дистанция, высокий контраст, крупная типографика)
- **Светлая** — для админ-ноута (drill-down, dashboard корпоратов)
- Обе темы — варианты zinc/slate

### Семантика статусов
- success / норма → `--chart-2` (зелёный)
- warning / каскад → `--chart-4` (амбра)
- danger / звоночек → `--destructive` (красный)

### Типографика
- **Manrope** — основной UI sans-serif
- **Fraunces** — brand-italic («Pulse», hero-числовые)
- **JetBrains Mono** — для данных (BPM, NCI, цифры, временные метки)

### Референсы — визуальная школа
- **Linear / Vercel / shadcn-defaults** — baseline всех экранов: плотная типографика, дисциплина spacing, hover-states, минимум декора, отличная читаемость
- **Hume Band** (humehealth.com/pages/hume-band) — для био-визуализаций (NCI-gauge, BPM-card, recovery-индикаторы): премиум-clinic-вайб

НЕ референсы: Whoop (спортивный), Oura (мягкие), Apple Health (декоративные градиенты).

## Куда сохранять результаты

| Артефакт | Путь |
|---|---|
| UI Kit | `docs_web/wireframes/m2/ui-kit.html` |
| Kiosk v2 | `docs_web/wireframes/m2/kiosk-v2.html` |
| Drill-down + Bayevsky | `docs_web/wireframes/m2/kiosk-drilldown.html` |
| Dashboard корпоратов | `docs_web/wireframes/m3/dashboard-corporate.html` (создать папку m3/) |
| Mobile рестайл | in-place edit `docs_web/wireframes/m1/mobile-*.html` |

## Способ исполнения

Запускаешься субагентом по плану `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md`. Каждая задача из плана = отдельный запуск. Между задачами PM делает чекпоинт.

## Технические правила (НЕ нарушать)

- ✅ HTML5 + Tailwind CSS (CDN), inline SVG для графиков и иконок
- ✅ Семантические токены через CSS-переменные (не хардкод hex)
- ✅ Адаптивность 1280 / 1440 / 1920
- ❌ React / Vue / любой JS-фреймворк — это вайрфреймы (RED в claude.md)
- ❌ Inline-стили (`<div style="...">`)
- ❌ Внешние JS-зависимости кроме Tailwind CDN и Google Fonts
- ✅ Простой vanilla JS только для state-switcher (dev-bar переключение состояний) и fake live BPM анимации

## Критические напоминания (NDA-safe)

В UI **запрещено** упоминать:
- VITRO / VANTA / VIGOR (внутренний нейминг устройств)
- M1 / M2 / M3 (внутренние milestone)
- Сбер / Райффайзенбанк / Газпром (B2B-клиенты)

Использовать: `Neiry.Pulse #1`, `Neiry Stress / Calmness Score`, без B2B-привязок в виджетах.

## После каждой задачи

1. Открыть результат в Chrome, проверить состояния
2. Закоммитить с русскоязычным сообщением вида «Добавил UI Kit M2: ...»
3. Git push (GitPages деплоится 1-2 мин)
4. Доложить PM в формате DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED
5. PM делает чекпоинт перед следующей задачей

## Главные документы (читать перед стартом)

- **План:** `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` — пошаговый план с layouts
- **Эстетика (память):** `~/.claude/projects/-Users-solomono-Desktop-NOW---------NEIRY/memory/project_neiry_ui_aesthetic.md`
- **Стек (память):** `~/.claude/projects/-Users-solomono-Desktop-NOW---------NEIRY/memory/project_neiry_ui_stack.md`
- **Состояние проекта:** `knowledge-base/PROJECT_STATE.md`
- **Текущий kiosk (для эстетической преемственности):** `docs_web/wireframes/m2/kiosk.html`
- **Exhibition flow (для понимания сценария):** `docs_web/wireframes/m2/exhibition-flow.html`
