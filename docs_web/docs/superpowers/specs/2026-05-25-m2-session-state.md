# M2 UI Restyle — Session State (2026-05-26, Этап 2 в работе, режим согласования)

> **Назначение:** handoff-документ для восстановления контекста после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.
>
> **Если контекст потерян:** прочти этот файл целиком → `memory/MEMORY.md` + 9 ключевых memory-файлов (см. список) → план M2 UI Restyle → бриф Кирилла A1 → продолжай с раздела «⏭ Очередь работы».

---

## 🚨 СТАТУС НА МОМЕНТ ЭТОГО HANDOFF (2026-05-26, A5 только что внесён, ждёт приёмки PM)

**Этап 2 в работе, режим: согласование каждой правки PM перед внесением.**

PM ввёл новое правило: **«Перед тем как вносить каждую правку, согласовывай её со мной, чтобы не внести лишнего».**

**Что произошло в этой сессии (Этап 2):**
1. Изначально запустил implementer-агента в background (subagent-driven-development). PM сразу остановил с приказом перейти в режим согласования.
2. Откатил подпись «Сними браслет → получи отчёт» из футера (агент успел добавить до остановки), CSS-инфраструктуру оставил.
3. Согласовал и внёс **A2 калибровка 12 сек** → принято PM (после фикса размера текста: t-h1 → t-h2 + nowrap).
4. Согласовал **A3 drill-down CTA** → PM **переделал концепцию**: вместо drill-hint «Подробнее →» — **hover-glow на все 3 карточки (wine border + bg/4% + 3-слойный glow)** + клик ведёт на `kiosk-drilldown.html?id=kostya/alexey/guest`. **Принято PM.**
5. Согласовал и внёс **A5 BLE-индикатор** → ждёт визуальной проверки PM.

**Состояние kiosk-v2.html сейчас:**
- A2 калибровка ✅ внесена (HTML + dev-bar + JS)
- A3 hover-glow ✅ внесена (CSS + 3× data-href + JS click + a11y)
- A5 BLE-индикатор ✅ внесена (CSS + 3× ble-dot + 3× ble-overlay + dev-bar + JS cycle)
- A6 чистка футера ⚪ НЕ начата

**Состояние git:**
- Все правки **НЕ закоммичены** (uncommitted в `docs_web/wireframes/m2/kiosk-v2.html`)
- Финальный коммит Round 2 будет ПОСЛЕ приёмки A5 + согласования и внесения A6
- Также НЕ закоммичен этот handoff-файл (после auto-compact восстановления — закоммитить)

---

## ⏭ Очередь работы (что делать сразу после auto-compact)

### Шаг 1 — спросить PM: «Принимаешь A5 BLE-индикатор?»

**Что проверять в браузере (Cmd+R kiosk-v2.html):**
1. В каждой шапке карточки рядом с «Neiry.Pulse #N» — зелёный мигающий dot (`live-blink 1.4s`).
2. dev-bar: новая кнопка «BLE: connected» (после блока калибровки).
3. Клик → меняется на «BLE: lost» (жёлтый dot, без анимации) → клик → «BLE: disconnected» (серый dot opacity 0.5 + overlay поверх карточки + blur backdrop + спиннер + текст «Переподключаемся…») → клик → connected.
4. На disconnected: hover/click отключены (cursor default, нет glow).
5. В `idle` и `active-2` — гостевой dot скрыт (нет браслета пока).
6. Switch state кнопками: всё должно сохраняться.

### Шаг 2 — после OK на A5 → согласовать **A6 чистка футера**

Скоуп A6 (по брифу Round 2):
- **Удалить** блок справа в `<footer>` kiosk-v2.html: «Подробный отчёт по сессии · Сканируй QR → Telegram-бот» + SVG QR 120×120.
- В карточке гостя в `pending-claim` QR **ОСТАЁТСЯ** (внутри `.when-done`).
- Модалка `.qr-modal` с QR 240×240 **ОСТАЁТСЯ**.
- Освободившееся место — короткая подпись, например «Сними браслет → получи отчёт» (PM возможно поменяет формулировку, спросить).

**Перед внесением A6 — обязательно** показать PM детали (что именно удаляю + что вставляю на освободившееся место) и получить OK.

### Шаг 3 — финальный коммит и пуш Round 2

Из `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY`:
```bash
git add docs_web/wireframes/m2/kiosk-v2.html docs_web/docs/superpowers/specs/2026-05-25-m2-session-state.md
git commit -m "Применил Round 2 правок Kiosk v2: калибровка 12 сек, hover-glow на карточках, BLE-индикатор, чистка футера"
git push
```

После пуша — обновить handoff (этот файл) на «Round 2 закрыт» и приготовиться к Этапу 3 (Задача 5 — kiosk-drilldown.html с 3 фазами Bayevsky).

---

## ✅ Что СДЕЛАНО в kiosk-v2.html (uncommitted)

### A2 — Калибровка 12 сек

- **HTML (карточка гостя):** новый `<div class="when-calibrating">` со спиннером, текстом «Калибровка XX сек…», hidden hint «Чуть дольше, ловим baseline…».
- **dev-bar:** label «калибровка» + кнопка `data-action="calibrate-guest"` (disabled когда `body[data-state]≠active-3`) + кнопка-toggle `data-flag="slow-calibration"`.
- **JS:** IIFE `initCalibration` — счётчик 12→0 сек, при `slow-calibration=true` → 16→0 сек + сразу видна подпись «Чуть дольше…». `Calibrate Guest` setState-aware (enabled только в active-3).
- **CSS** уже был внесён до этой сессии (`.when-calibrating`, `.calib-spinner`, `[data-card-state=calibrating]` toggle).

### A3 — Hover-glow (переделано из drill-hint по приказу PM)

- **CSS:** новый блок `.card-anchor[data-href]:hover/focus-visible` — wine border + `bg: hsl(--primary)/0.04` + 3-слойный box-shadow (1px ring + 12px middle + 80px halo). В `body[data-state="idle"]` — отключён.
- **HTML:** все 3 `<article>` получили `data-href="./kiosk-drilldown.html?id=kostya|alexey|guest"`.
- **JS:** обработчик клика на `.card-anchor[data-href]` + `role="link"` + `tabindex="0"` + клавиатура (Enter/Space). В idle — клик игнорируется.
- **CSS блок `.drill-hint` УДАЛЁН** (его в предыдущей версии оставлял агент).
- **HTML drill-hint `<a>` элемент УДАЛЁН** (был в карточке гостя).
- Default `cardState='active'` в JS тоже удалён (был только для видимости drill-hint).

### A5 — BLE-индикатор

- **CSS** в основном был внесён до этой сессии (`.ble-dot`, `.ble-overlay`, состояния `[data-ble=connected/lost/disconnected]`). Этой сессией добавлено:
  - `body[data-state="idle/active-2"] [data-id="guest"] .ble-dot { display: none }`
  - `.card-anchor[data-ble="disconnected"][data-href]` — `cursor: default; pointer-events: none` + сброс hover-эффекта.
- **HTML headers (3 карточки):** `<span class="ble-dot" data-ble-dot aria-label="Связь активна"></span>` рядом с «Neiry.Pulse #N».
- **HTML articles (3 карточки):** `data-ble="connected"` атрибут + блок `<div class="ble-overlay" aria-hidden="true">` со спиннером и текстом «Переподключаемся…».
- **dev-bar:** label «BLE» + кнопка `data-action="cycle-ble"` с динамическим текстом «BLE: <phase>».
- **JS:** IIFE `initBleCycle` — циклит `connected → lost → disconnected → connected` для всех 3 карточек разом, обновляет `aria-label` у dots.

---

## 📋 Финальные решения PM (актуально, не менять)

| # | Тема | Решение PM |
|---|---|---|
| 1 | Метрика стресса на плазме | **NSI** (Neiry Stress Index). Зоны 0-39 НОРМА / 40-59 ПОВЫШЕН / 60-100 ВЫСОКИЙ. ↑=стресс↑ |
| 2 | Имя гостя | mobile name_input. В kiosk-v2 хардкод «Гость» |
| 3 | Калибровка | **12 сек**, расширение до 16 сек при недостатке семплов (флаг slow-calibration) |
| 4 | Тест Баевского | Только в drill-down (Задача 5, Этап 3) |
| 5 | BLE-индикатор | Dot в шапке. heartbeat 2 сек / lost 5 сек / disconnect 30 сек. В мокапе — циклит dev-bar кнопкой |
| 6 | QR на главном | В футере убрать. В `pending-claim` карточке остаётся. Модалка остаётся |
| 7 | Welcome-screen | Использовать active-2 |
| 8 | Dev-bar в продакшене | Оставить, PM сам уберёт через `?prod=1` |
| 9 | NSI формула | `NSI = 100 − (Current_BPM − Baseline_BPM) × 2`, clamp [0..100]. Baseline = mean BPM за 12 сек |
| 10 | Mobile pairing | Задача 7 в плане M2 UI Restyle |
| 11 | ТЗ Кириллу | Бриф A1, раздел 3.3 |
| 12 | **Drill-down CTA (A3 Round 2)** | **Hover-glow на все 3 карточки** (wine border + bg/4% + glow побольше). НЕ drill-hint «Подробнее →». Кликабельны все 3 → kiosk-drilldown.html?id=... |
| 13 | **Режим работы Этапа 2** | Каждая правка согласовывается с PM ДО внесения. НЕ запускать background-агентов |

---

## 📊 Статус задач плана M2 UI Restyle

| # | Задача | Статус | Артефакт | SHA |
|---|---|---|---|---|
| 1 | Калибровка эстетики | ✅ принято | `memory/project_neiry_ui_aesthetic.md` | — |
| 2 | BRIEF.md UX/UI | ✅ принято | `UI_assets/BRIEF.md` | bf1bf9e |
| 3 | UI Kit | ✅ принято | `docs_web/wireframes/m2/ui-kit.html` | bf1bf9e |
| 4 | Kiosk v2 | 🟡 **Round 2 в работе** (A2/A3/A5 внесены uncommitted, A6 не начат) | `docs_web/wireframes/m2/kiosk-v2.html` | uncommitted |
| 5 | Drill-down (3 фазы Bayevsky) | ⚪ pending (Этап 3 после Round 2 acceptance) | `docs_web/wireframes/m2/kiosk-drilldown.html` | — |
| 6 | Dashboard корпоратов | ⚪ pending | `docs_web/wireframes/m3/dashboard-corporate.html` | — |
| 7 | Mobile pairing + state machine | ⚪ pending | `docs_web/wireframes/m1/mobile-*.html` | — |
| 8 | Финальная индексация | ⚪ pending | `docs_web/index.html` | — |

---

## 🔗 GitPages URLs

- UI Kit: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/ui-kit.html
- Kiosk v2: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html
- Exhibition Flow: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/exhibition-flow.html
- Roadmap-дашборд R&D: https://s0101110110.github.io/neiry-pulse-m1-wireframes/research/brainstorms/assets/2026-05-22-pm-dashboard.html

---

## 🎨 Финальная эстетика (зафиксирована PM)

- **Шрифты:** Space Grotesk (UI) + Onest 700 (hero) + Geist Mono (data). Кириллица.
- **Палитра светофора:** success `#00E676` / warning `#FFB300` / destructive `#FF1744`.
- **Wine accent:** `#831843` (`var(--primary)`). Используется в hover-glow карточек.
- **База:** shadcn zinc/slate semantic CSS-переменные.
- **NSI-gauge:** Apple Rings 270° для kiosk + Tremor Radial 360° для drill-down. `pathLength=100`.
- **ECG-плашка:** параметрический P-QRS-T, окно ~5.1 сек.

---

## 🛡 Активные правила

1. **PM acceptance gate** — задача НЕ закрывается без явного «принято».
2. **Согласование Этапа 2** — каждая правка обсуждается с PM до внесения.
3. **HTML-first workflow** — HTML+Tailwind CDN → потом React.
4. **NDA-safe UI** — НЕТ: VITRO, VANTA, VIGOR, M1/M2/M3, Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #N», «Neiry Stress Index».
5. **Имена анкеров:** Костя + Алексей. НЕ Илья.
6. **На стенде 28-29.05:** Костя + Алексей. Никита и Кирилл — НЕ на стенде.
7. **Технические:** HTML5 + Tailwind CDN + inline SVG. Хардкод hex только `#831843`.
8. **НЕ обновляю исторические логи:** `knowledge-base/decisions/2026-05.md`, `knowledge-base/INBOX/raw/*`, `research/brainstorms/2026-05-22-task-package.md`.

---

## 📁 Ключевые memory-файлы

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_stress_index.md` — NSI
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты
- `memory/project_neiry_ui_stack.md` — стек
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_team_roles.md` — команда
- `memory/project_neiry_m2_artifacts.md` — карта файлов
- `memory/project_neiry_m2_kiosk_scenario.md` — сценарий стенда

---

## 🚨 Алгоритм восстановления (если auto-compact случился ПРЯМО СЕЙЧАС)

1. Прочитать **этот файл** целиком.
2. Прочитать `memory/MEMORY.md` + ключевые memory-файлы.
3. `git status` + `git log --oneline -5` — посмотреть локальные uncommitted и последние коммиты.
4. `git diff docs_web/wireframes/m2/kiosk-v2.html | head -200` — глянуть свежие правки.
5. Сказать PM:
   > «Контекст восстановлен. Этап 2 в работе:
   > • A2 калибровка ✅ внесена и принята PM (фикс t-h2 + nowrap)
   > • A3 hover-glow ✅ внесена и принята PM (переделано из drill-hint в hover-эффект на 3 карточки)
   > • A5 BLE-индикатор ✅ внесена, ждёт визуальной приёмки PM
   > • A6 чистка футера ⚪ не начата
   > • Всё uncommitted в `docs_web/wireframes/m2/kiosk-v2.html`
   > Продолжаем с приёмки A5?»

---

## 💬 Последняя реплика PM

> «Скоро произойдет авто-компакт. Обнови хенд-офф.»

(До этого: PM подтвердил все 3 уточнения по A5 → внёс A5 → теперь обновляю handoff.)

---

## 🎯 Что отвечать PM сразу после восстановления

> «Handoff обновлён. A2/A3/A5 внесены uncommitted в kiosk-v2.html. Жду приёмку A5 от тебя. Открыть файл в браузере?»
