# M2 UI Restyle — Session State (2026-05-26, Этап 2 закрыт, готовимся к Этапу 3)

> **Назначение:** handoff-документ для восстановления контекста после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.
>
> **Если контекст потерян:** прочти этот файл целиком → `memory/MEMORY.md` + 9 ключевых memory-файлов (см. список) → план M2 UI Restyle → продолжай с раздела «⏭ Очередь работы».

---

## 🚨 СТАТУС НА МОМЕНТ ЭТОГО HANDOFF (2026-05-26, Round 2 закрыт)

**Этап 2 закрыт. Готовимся к Этапу 3 — Задача 5 (Drill-down + 3 фазы Bayevsky test).**

**Round 2 правок Kiosk v2 — все 4 пункта внесены, закоммичены, запушены:**
- ✅ A2 калибровка 12 сек (с расширением до 16 сек по slow-флагу)
- ✅ A3 hover-glow на 3 карточки (вместо drill-hint «Подробнее →» — переделано по приказу PM)
- ✅ A5 BLE-индикатор (data-ble: connected/lost/disconnected с overlay)
- ✅ A6 чистка футера (dev-bar сдвинут на left:62% для пространства легенды)

**Финальный коммит Round 2: `1226e0b`** — pushed to origin/main.

**Задача 4 (Kiosk v2) → ✅ ПРИНЯТО PM** (последняя реплика PM по приёмке: «да»).

---

## ⏭ Очередь работы (что делать сразу после auto-compact)

### Шаг 1 — выдать PM бриф на Этап 3 (Задача 5 — kiosk-drilldown.html)

PM попросил дословно: **«Сделай хэндов, а после этого сделай компакт чата, и после этого дай мне бриф.»**

После выполнения /compact (это делает сам PM, я не могу) — выдать бриф следующего содержания:

**Артефакт:** `docs_web/wireframes/m2/kiosk-drilldown.html` (новый файл)

**Куда сейчас ведут клики:** все 3 карточки в kiosk-v2 имеют `data-href="./kiosk-drilldown.html?id={kostya|alexey|guest}"`. JS читает query-параметр `id` и подставляет имя/avatar/baseline в шапку.

**Layout (админ-ноут, 1440×900, ОТДЕЛЬНАЯ светлая тема — не плазма):**
- **Top bar:** ← back to wall (ссылка на kiosk-v2.html) + «Гость #3 · 02:47» (timer от начала сессии)
- **Главный блок NSI:** большое число (Onest 700) + NSI-gauge Tremor Radial 360° (отличается от Apple Rings 270° на плазме) + caption «Уровень стресса (NSI · Neiry Stress Index, ↑ = стресс ↑)»
- **4 метрики 2×2:** BPM с sparkline / HRV-RMSSD (или «— нет данных») / SpO₂ / Шаги
- **60-сек график BPM** (line chart, SVG inline)
- **CTA «🧪 Запустить Тест Баевского (5 мин)»:** large primary button + caption «3 мин покоя + Stroop + дорожка»
- **Footer:** STOP SESSION → QR/PIN экран

**3 фазы Bayevsky test (state-switcher через dev-bar):**
- **BAYEVSKY_PHASE_1 — «Покой 3 мин»:** большой обратный таймер 03:00 → 00:00, инструкция «Стой неподвижно, дыши спокойно», прогресс-полоса
- **BAYEVSKY_PHASE_2 — «Stroop 1 мин»:** имитация теста (плашка цвета/слова), таймер 01:00, подпись «Это нормально, что стресс чуть подскочит — мозг работает»
- **BAYEVSKY_PHASE_3 — «Беговая дорожка 1 мин»:** «Перейди на дорожку, лёгкий бег», таймер 01:00
- **BAYEVSKY_RESULT:** таблица 3 фаз × значение ИН Баевского + общий вывод (цветовая зона)

**Формула Баевского (Slow, для TG-отчёта):** `ИН = AMo / (2·Mo·MxDMn)`, окно 3-5 мин.

**Двухступенчатый фильтр R-R:** медианный (отсечь ±20% от медианы) → перцентильный (5/95%). Если в окне < 60% валидных R-R → выводить «недостаточно данных, продли фазу».

**Принципы:**
- Стек — тот же что в kiosk-v2: HTML + Tailwind CDN + shadcn semantic CSS-переменные + inline SVG + vanilla JS.
- Шрифты те же: Space Grotesk + Onest 700 + Geist Mono.
- Палитра светофора: success/warning/destructive HSL-токены.
- CTA «Тест Баевского» — опциональный, не запускается автоматически.
- Кнопка «← back to wall» — `<a href="./kiosk-v2.html">`.
- dev-bar внизу: state-switcher для 5 состояний (drilldown / phase-1 / phase-2 / phase-3 / result).
- NDA-safe: «Neiry.Pulse #N», «Neiry Stress Index». БЕЗ M1/M2/M3, VITRO, B2B-клиентов.

**Режим работы:** как в Round 2 — каждый блок согласовываю с PM ДО внесения. НЕ запускать background-агентов.

### Шаг 2 — ждать решений PM по уточняющим вопросам и согласовывать каждый блок drilldown

---

## ✅ Что СДЕЛАНО в Round 2 (commit 1226e0b)

### A2 — Калибровка 12 сек
- **HTML (карточка гостя):** новый `<div class="when-calibrating">` со спиннером, текстом «Калибровка XX сек…» (t-h2 + nowrap), hidden hint «Чуть дольше, ловим baseline…».
- **dev-bar:** label «калибровка» + кнопка `data-action="calibrate-guest"` (disabled когда `body[data-state]≠active-3`) + кнопка-toggle `data-flag="slow-calibration"`.
- **JS:** IIFE `initCalibration` — счётчик 12→0 сек, при `slow-calibration=true` → 16→0 сек + сразу видна подпись «Чуть дольше…». `Calibrate Guest` setState-aware (enabled только в active-3).
- **CSS:** `.when-calibrating`, `.calib-spinner`, `[data-card-state=calibrating]` toggle.

### A3 — Hover-glow (переделано из drill-hint по приказу PM)
- **CSS:** `.card-anchor[data-href]:hover/focus-visible` — wine border + `bg: hsl(--primary)/0.04` + 3-слойный box-shadow (1px ring + 12px middle + 80px halo). В `body[data-state="idle"]` — отключён.
- **HTML:** все 3 `<article>` получили `data-href="./kiosk-drilldown.html?id=kostya|alexey|guest"`.
- **JS:** обработчик клика на `.card-anchor[data-href]` + `role="link"` + `tabindex="0"` + клавиатура (Enter/Space). В idle — клик игнорируется.

### A5 — BLE-индикатор
- **CSS:** `.ble-status-dot` реагирует на `[data-ble]` родителя — connected (зелёный live-blink), lost (жёлтый без анимации), disconnected (серый opacity 0.5). Текст рядом тоже меняет цвет на warning при lost/disconnected.
- **HTML:** существующая строка «● ПОДКЛЮЧЕН» под BPM переписана на `<span class="ble-status-dot"></span><span class="ble-status-text">Подключен</span>`.
- **HTML overlay:** в каждой `<article>` добавлен `.ble-overlay` со спиннером и текстом «Переподключаемся…» (показывается на `data-ble=disconnected`).
- **CSS:** `[data-ble="disconnected"][data-href]` — `cursor: default; pointer-events: none` + сброс hover-эффекта.
- **dev-bar:** label «BLE» + кнопка `data-action="cycle-ble"` с динамическим текстом «BLE: <phase>».
- **JS:** IIFE `initBleCycle` — циклит `connected → lost → disconnected → connected` для всех 3 карточек разом, меняет текст «Подключен / Нет связи / Отключено».

### A6 — Чистка футера
- QR-блок справа в `<footer>` был удалён до Round 2 (коммит 3703975).
- Round 2: dev-bar сдвинут на `left: 62%` (было `50%`) — освобождает пространство под легенду стрессовых зон.

---

## 📋 Финальные решения PM (актуально, не менять)

| # | Тема | Решение PM |
|---|---|---|
| 1 | Метрика стресса на плазме | **NSI** (Neiry Stress Index). Зоны 0-39 НОРМА / 40-59 ПОВЫШЕН / 60-100 ВЫСОКИЙ. ↑=стресс↑ |
| 2 | Имя гостя | mobile name_input. В kiosk-v2 хардкод «Гость» |
| 3 | Калибровка | **12 сек**, расширение до 16 сек при недостатке семплов (флаг slow-calibration) |
| 4 | Тест Баевского | Только в drill-down (Задача 5, Этап 3), опциональный CTA |
| 5 | BLE-индикатор | Dot под BPM (не в шапке!). heartbeat 2 сек / lost 5 сек / disconnect 30 сек. В мокапе — циклит dev-bar кнопкой |
| 6 | QR на главном | В футере убрать. В `pending-claim` карточке остаётся. Модалка остаётся |
| 7 | Welcome-screen | Использовать active-2 |
| 8 | Dev-bar в продакшене | Оставить, PM сам уберёт через `?prod=1` |
| 9 | NSI формула | `NSI = 100 − (Current_BPM − Baseline_BPM) × 2`, clamp [0..100]. Baseline = mean BPM за 12 сек |
| 10 | Mobile pairing | Задача 7 в плане M2 UI Restyle |
| 11 | ТЗ Кириллу | Бриф A1, раздел 3.3 |
| 12 | Drill-down CTA (A3 Round 2) | Hover-glow на все 3 карточки (wine border + bg/4% + glow). Кликабельны все 3 → kiosk-drilldown.html?id=... |
| 13 | Режим работы Этапа 2+ | Каждая правка согласовывается с PM ДО внесения. НЕ запускать background-агентов |
| 14 | Drilldown тема | Светлая (админ-ноут 1440×900). На плазме — тёмная |
| 15 | Drilldown NSI-gauge | Tremor Radial 360° (отличается от Apple Rings 270° на плазме) |

---

## 📊 Статус задач плана M2 UI Restyle

| # | Задача | Статус | Артефакт | SHA |
|---|---|---|---|---|
| 1 | Калибровка эстетики | ✅ принято | `memory/project_neiry_ui_aesthetic.md` | — |
| 2 | BRIEF.md UX/UI | ✅ принято | `UI_assets/BRIEF.md` | bf1bf9e |
| 3 | UI Kit | ✅ принято | `docs_web/wireframes/m2/ui-kit.html` | bf1bf9e |
| 4 | Kiosk v2 | ✅ **принято** (Round 2 закрыт) | `docs_web/wireframes/m2/kiosk-v2.html` | **1226e0b** |
| 5 | Drill-down (3 фазы Bayevsky) | 🔴 **СЛЕДУЮЩАЯ** (Этап 3) | `docs_web/wireframes/m2/kiosk-drilldown.html` | — |
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

- **Шрифты:** Space Grotesk (UI) + Onest 700 (hero, letter-spacing −0.02em) + Geist Mono (data). Кириллица.
- **Палитра светофора:** success `151 100% 45%` / warning `42 100% 50%` / destructive `348 100% 54%` (HSL-токены).
- **Wine accent:** `#831843` (`var(--primary)`). Используется в hover-glow карточек.
- **База:** shadcn zinc/slate semantic CSS-переменные.
- **NSI-gauge:** Apple Rings 270° для kiosk + Tremor Radial 360° для drill-down. `pathLength=100`.
- **ECG-плашка:** параметрический P-QRS-T, окно ~5.1 сек.

---

## 🛡 Активные правила

1. **PM acceptance gate** — задача НЕ закрывается без явного «принято».
2. **Согласование с PM** — каждая правка обсуждается с PM до внесения. Действует с Round 2 Kiosk v2 и продолжает действовать на drilldown.
3. **HTML-first workflow** — HTML+Tailwind CDN → потом React.
4. **NDA-safe UI** — НЕТ: VITRO, VANTA, VIGOR, M1/M2/M3, Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #N», «Neiry Stress Index».
5. **Имена анкеров:** Костя + Алексей. НЕ Илья.
6. **На стенде 28-29.05:** Костя + Алексей. Никита и Кирилл — НЕ на стенде.
7. **Технические:** HTML5 + Tailwind CDN + inline SVG. Хардкод hex только `#831843`.
8. **НЕ обновляю исторические логи:** `knowledge-base/decisions/2026-05.md`, `knowledge-base/INBOX/raw/*`, `research/brainstorms/2026-05-22-task-package.md`.

---

## 📁 Ключевые memory-файлы

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_stress_index.md` — NSI + Баевский + двухступенчатый R-R фильтр
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты
- `memory/project_neiry_ui_stack.md` — стек
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_team_roles.md` — команда
- `memory/project_neiry_m2_artifacts.md` — карта файлов
- `memory/project_neiry_m2_kiosk_scenario.md` — сценарий стенда
- `memory/project_neiry_kiosk_design_system.md` — type-scale, токены, layout-правила

---

## 🚨 Алгоритм восстановления (если auto-compact случился ПРЯМО СЕЙЧАС)

1. Прочитать **этот файл** целиком.
2. Прочитать `memory/MEMORY.md` + ключевые memory-файлы.
3. `git status` + `git log --oneline -5` — последние коммиты, проверить что `1226e0b` на месте.
4. Если PM уже сделал /compact → выдать ему **бриф на Задачу 5** из раздела «⏭ Очередь работы → Шаг 1».
5. Если PM ещё не сделал /compact → напомнить ему и подождать.
6. Сказать PM:
   > «Контекст восстановлен. Round 2 Kiosk v2 закрыт (commit 1226e0b, принято). Готов выдать бриф на Задачу 5 (kiosk-drilldown.html + 3 фазы Bayevsky test). Поехали?»

---

## 💬 Последняя реплика PM

> «Сделай хэндов, а после этого сделай компакт чата, и после этого дай мне бриф.»

(До этого: «да» — принял Round 2 и дал команду коммитить.)

---

## 🎯 Что отвечать PM сразу после восстановления

> «Handoff обновлён и запушен. Round 2 Kiosk v2 закрыт коммитом 1226e0b. Я не могу сам вызвать /compact — это slash-команда. Когда сделаешь /compact, скажи мне и я выдам бриф на Задачу 5 (drilldown + Bayevsky).»
