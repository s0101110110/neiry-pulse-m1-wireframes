# M2 UI Restyle — Session State (2026-05-25, обновлено 25.05 вечером)

> **Назначение:** handoff-документ для восстановления контекста после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.
>
> **Если контекст потерян:** прочти этот файл целиком → memory/MEMORY.md + 6 ключевых memory-файлов (см. список ниже) → план M2 UI Restyle → продолжай с раздела «⏭ Очередь работы — где остановились».

---

## 🎯 Где мы остановились (25.05.2026 вечер)

Round 1 правок PM по Kiosk v2 применён (commit `1d8b28b`). Затем PM в параллельном окне VS Code прошёлся с UI-дизайнером и улучшил `kiosk-v2.html` (type-scale, viewport-fit, ECG-генератор, accessibility). Я провёл **PM-аудит** и нашёл 10 пунктов — что забыли / что обсудить. PM прошёлся по всем 10, принял решения. **Согласован финальный план Этап 1 (документы) → Этап 2 (Round 2 правок Kiosk v2).** Перед стартом Этапа 1 — критическое уточнение: rename NCI→NSI касается **всех документов команды**, не только wireframe. PM подтвердил масштаб.

**На момент снапшота — не начали Этап 1.** Этот файл — снапшот всех решений.

---

## ⏭ Очередь работы — где остановились

### Этап 1 — документы (делать первым, без агента, сам)

**1.1. Глобальный rename NCI → NSI** во всех документах:
- `knowledge-base/briefs/2026-05-24-A1-kirill-bek-mobile.md` — раздел 3.1, 3.2, 6
- `memory/project_neiry_stress_index.md` — переписать: NSI = Fast UI metric (была путаница с NCI)
- `research/brainstorms/assets/2026-05-22-pm-dashboard.html` — упоминания NCI в задачах
- Проверка остальных M2 артефактов (grep по «NCI» в `docs_web/wireframes/m2/`)

**1.2. Расширить бриф Кирилла** — добавить новый раздел **3.3 «Mobile pairing → Plasma handoff»**:
- 3.3.1 Ввод имени гостя в mobile app (этап pairing flow)
- 3.3.2 Калибровка 12 сек: state-machine `pairing → name_input → calibrating → active → ended`
- 3.3.3 BLE connection lifecycle: heartbeat 2 сек, `connection_lost` после 5 сек timeout, `connection_restored` событие
- 3.3.4 WebSocket schema плазме: `pairing_started`, `name_submitted`, `calibration_started`, `calibration_done`, `connection_lost`, `connection_restored`, `bpm_tick`, `nsi_tick`, `session_ended`

**1.3. Обновить раздел 6 брифа Кирилла** (что подтвердить) — добавить пункты по 3.3.

**1.4. Добавить в roadmap-дашборд** (`research/brainstorms/assets/2026-05-22-pm-dashboard.html`) новые подзадачи Кирилла на 25-26.05 (вписать в существующую вёрстку): mobile pairing flow с именем, BLE heartbeat, WebSocket events.

**1.5. Обновить план M2 UI Restyle** (`docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md`):
- Задача 4 → подзадачи Round 2 (A2 калибровка, A3 drill-down CTA, A5 BLE-индикатор, A6 убрать QR из футера)
- Задача 5 (drill-down) → пункт «кнопка Тест Баевского внутри карточки гостя»
- Задача 7 (mobile pairing) → пункт «этап ввода имени перед сессией»

### Этап 2 — Round 2 правок Kiosk v2 (через implementer-агента в background)

**Скоуп Round 2:**
- **A2. Состояние «Калибровка 12 сек…»** — новое промежуточное состояние per-card через `data-card-state` на article. UI: спиннер + обратный отсчёт «Калибровка 12 сек…». Триггер: dev-bar добавить кнопку «Calibrate».
- **A3. Drill-down CTA** в карточке гостя — hint «Подробнее →» с hover-эффектом, клик → `kiosk-drilldown.html`.
- **A5. BLE-индикатор связи** — dot в шапке каждой карточки рядом с «Neiry.Pulse #N»: зелёный pulse = active, серый = lost. Триггер: dev-bar toggle.
- **A6. Убрать QR-блок из правой части футера.** В карточке гостя в `pending-claim` QR остаётся. Модалка остаётся. **Только футер чистим.**

**Скоуп НЕ Round 2 (отменено / перенесено):**
- ~~A1 rename NSI→NCI~~ **ОТМЕНЕНО** — остаёмся на NSI. PM прочитал переписку с Никитой, решил оставить NSI.
- A4 (кнопка Тест Баевского) — **только в drill-down**, не на главной плазме. Это Задача 5.
- A7 (имя гостя) — в мокапе хардкод «Гость» (нейтрально для скриншотов), механизм описан в ТЗ Кириллу.

### Этап 3 — после принятия Kiosk v2 PM

→ Задача 5 (kiosk-drilldown.html) с 3 фазами Bayevsky + кнопкой Теста Баевского.

---

## 📋 Финальные решения PM 25.05.2026 (вечер) — критично

| # | Тема | Решение PM |
|---|---|---|
| 1 | Метрика стресса на плазме | **NSI** (Neiry Stress Index). НЕ NCI. PM прочитал переписку с Никитой, решил остаться на NSI. Зоны: 0-39 НОРМА (success), 40-59 ПОВЫШЕН (warning), 60-100 ВЫСОКИЙ (destructive) |
| 2 | Имя гостя | Вводится в **mobile app при паринге**. После ввода → калибровка → данные на плазму. В мокапе Kiosk v2 хардкод «Гость» (для скриншотов нейтральнее) |
| 3 | Калибровка | **12 секунд**, новое промежуточное состояние. Mobile app шлёт `state: calibrating` → `state: active`. На UI — спиннер + обратный отсчёт |
| 4 | Тест Баевского | **Только в drill-down карточке гостя**, НЕ на главной плазме. Запускается опциональной кнопкой внутри drill-down |
| 5 | BLE-индикатор | Dot в шапке каждой карточки (рядом с «Neiry.Pulse #N»): зелёный pulse = active, серый = lost. Heartbeat 2 сек, timeout 5 сек |
| 6 | QR на главном экране | **В футере убрать** правый блок с QR + «Подробный отчёт по сессии». **В карточке гостя в pending-claim QR остаётся** (это финальный момент сессии). Модалка остаётся |
| 7 | Welcome-screen | Использовать существующее состояние `active-2` (Костя+Алексей активны, Гость в idle) — это уже работает как welcome |
| 8 | Dev-bar в продакшене | Оставить видимым, PM сам уберёт через `?prod=1` если надо |
| 9 | NSI = f(BPM) | Зафиксировать в ТЗ Кириллу: формула `100 − (Current_BPM − Baseline_BPM) × 2`, clamp [0..100] |
| 10 | Mobile pairing «агент» | **НЕ новый агент.** Это Задача 7 в плане M2 UI Restyle — её выполнит implementer-агент в свой черёд |
| 11 | ТЗ Кириллу | **НЕ создавать новый документ.** Расширить существующий бриф `knowledge-base/briefs/2026-05-24-A1-kirill-bek-mobile.md` новым разделом 3.3 |

---

## 📊 Статус задач плана M2 UI Restyle

| # | Задача | Статус | Артефакт | SHA |
|---|---|---|---|---|
| 1 | Калибровка эстетики (палитра/типографика/токены) | ✅ принято | `memory/project_neiry_ui_aesthetic.md` | — |
| 2 | BRIEF.md UX/UI Дизайнера | ✅ принято | `ui_assets/BRIEF.md` | ed14bea |
| 3 | UI Kit | ✅ принято | `docs_web/wireframes/m2/ui-kit.html` | e18bae3 → 8e1d254 → 8177629 → dbc2e37 |
| 4 | Kiosk v2 | 🟡 Round 1 принят, ждёт Round 2 | `docs_web/wireframes/m2/kiosk-v2.html` | 3f076f5 → 1bcb4c7 → 03c0f96 → 1d8b28b (round 1) → работа UI-дизайнера (uncommitted на момент снапшота) |
| 5 | Drill-down + 3 фазы Bayevsky + кнопка Теста | ⚪ pending | `docs_web/wireframes/m2/kiosk-drilldown.html` | — |
| 6 | Dashboard корпоратов (Neiry Unite v5) | ⚪ pending | `docs_web/wireframes/m3/dashboard-corporate.html` | — |
| 7 | Mobile pairing рестайл + этап ввода имени | ⚪ pending | `docs_web/wireframes/m1/mobile-*.html` (in-place) | — |
| 8 | Финальная индексация + push GitPages | ⚪ pending | `docs_web/index.html` | — |

---

## 🔗 GitPages URLs (для проверки в браузере)

- UI Kit: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/ui-kit.html
- Kiosk v2: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html

---

## 🎨 Финальная эстетика (зафиксирована PM 25.05.2026)

- **Шрифты:** Space Grotesk (UI 300-700) + Onest 700 (hero/display, tracking -0.04em) + Geist Mono (data). Все три с кириллицей.
- **Палитра светофора (Cyber-flat):** success `#00E676` (`151 100% 45%`), warning `#FFB300` (`42 100% 50%`), destructive `#FF1744` (`348 100% 54%`).
- **Wine accent:** `#831843` (`var(--primary)`).
- **База:** shadcn zinc/slate semantic CSS-переменные.
- **Темы:** тёмная для kiosk (плазма), светлая для админ-ноута (drill-down, dashboard).
- **NSI-gauge:** Apple Rings (270° arc) для kiosk + Tremor Radial (360° donut) для drill-down (паттерны в UI Kit).
- **ECG-визуализация под BPM:** параметрический P-QRS-T генератор (от UI-дизайнера 25.05), окно ~5.1 сек, цвет линии по BPM-зоне.

---

## 🛡 Активные правила (ИЗ ПАМЯТИ, критично)

1. **PM acceptance gate** (`feedback_neiry_pm_acceptance_gate.md`) — задача НЕ закрывается без явного «принято» от PM. Spec/code-review = техническая готовность, не замена принятия. Не двигаться к следующей задаче самовольно.
2. **HTML-first workflow** (`feedback_neiry_workflow_html_first.md`) — HTML+Tailwind CDN мокапы → передача Кириллу на React.
3. **NDA-safe UI** — НЕТ упоминаний: VITRO, VANTA, VIGOR, M1/M2/M3 (в видимом UI), Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #1», «Neiry Stress Index» (NSI).
4. **Имена анкеров на M2:** Костя (Project Lead) + Алексей (B2B Lead). НЕ Илья.
5. **На стенде 28-29.05:** только Костя + Алексей. Никита и Кирилл — НЕ на стенде.
6. **Технические правила:** HTML5 + Tailwind CDN + inline SVG. НЕТ React/Vue/jsx. НЕТ inline-стилей (`style="..."`) кроме SVG-параметров и swatch-плиток документации. НЕТ хардкода hex (только `#831843` wine). НЕТ внешних JS-зависимостей кроме Tailwind CDN + Google Fonts.
7. **Координация с параллельными агентами:** PM часто работает с UI-дизайнером в другом окне VS Code. Перед правкой `kiosk-v2.html` — `git status` + проверка что нет unstaged изменений. Если есть — закоммитить как «работа UI-дизайнера 25.05» до своих правок.

---

## 📁 Ключевые memory-файлы (читать после auto-compact)

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты/референсы
- `memory/project_neiry_ui_stack.md` — React-стек (shadcn + Tremor + кастом)
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_team_roles.md` — Костя/Алексей/Никита/Кирилл
- `memory/project_neiry_m2_artifacts.md` — карта файлов M2
- `memory/project_neiry_stress_index.md` — NSI Fast UI + Баевский Slow Backend (на момент снапшота требует rename NCI→NSI в самом memory-файле)
- `memory/project_neiry_m2_kiosk_scenario.md` — сценарий стенда (3 браслета, drill-down)

---

## 📝 Шаблон prompt для implementer-агента — Round 2 Kiosk v2

```
Ты — implementer-субагент для Neiry M2 UI Restyle, Round 2 правок Kiosk v2.

КОНТЕКСТ ПРОЕКТА:
- Файл: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-v2.html
- HTML+Tailwind CDN + inline SVG + vanilla JS мокап kiosk-плазмы 1920×1080 (тёмная тема).
- Token-first: semantic shadcn CSS-переменные, hex только #831843 (wine).
- Шрифты: Space Grotesk / Onest 700 / Geist Mono.
- Палитра: success `151 100% 45%`, warning `42 100% 50%`, destructive `348 100% 54%`.
- Имена анкеров: Костя (PL) + Алексей (B2B). НЕ Илья.
- NDA-stop: НЕТ VITRO/VANTA/VIGOR/M1/M2/M3 в UI.
- Состояния на body: data-state = idle / active-2 / active-3 / pending-claim.
- Метрика на плазме: NSI (Neiry Stress Index). НЕ NCI.
- NSI-gauge: pathLength=100, dasharray=100, dashoffset=100-NSI.
- Зоны NSI: 0-39 success НОРМА, 40-59 warning ПОВЫШЕН, 60-100 destructive ВЫСОКИЙ.

ПРАВКИ Round 2:

A2. Состояние «Калибровка 12 сек…» (per-card):
- Новый атрибут data-card-state на <article> = idle / calibrating / active / done
- В состоянии calibrating: показать спиннер + текст «Калибровка XX сек…» с обратным отсчётом
- Триггер для мокапа: dev-bar добавить кнопку «Calibrate Guest» — переключает карточку гостя в calibrating на 12 сек, потом active

A3. Drill-down CTA на карточке гостя:
- Hint «Подробнее →» в правом нижнем углу карточки с hover-эффектом (opacity transition)
- Клик: window.location.href = './kiosk-drilldown.html'
- Видимость: только когда у гостя data-card-state = active

A5. BLE-индикатор связи:
- Dot в шапке КАЖДОЙ карточки, рядом с «Neiry.Pulse #N»
- Состояния: connected = зелёный с live-blink анимацией, disconnected = серый (muted), opacity 0.5
- Триггер для мокапа: dev-bar добавить toggle «BLE Lost» — переключает все 3 карточки в disconnected

A6. Убрать QR-блок из правой части футера:
- Удалить блок справа: «Подробный отчёт по сессии · Сканируй QR → Telegram-бот» + SVG QR 120×120
- В карточке гостя в pending-claim QR ОСТАЁТСЯ
- Модалка с QR 240×240 ОСТАЁТСЯ
- Только футер чистим — высвобождается место для возможного будущего блока

НЕ ТРОГАТЬ:
- A1 (rename NSI→NCI) — отменено
- Тест Баевского — это для Задачи 5 (drill-down), не сейчас
- Имя гостя — оставить хардкод «Гость»
- ECG-генератор P-QRS-T, type-scale, viewport-fit — работа UI-дизайнера, не править

ШАГИ:
1. Прочитай файл целиком.
2. Применяй правки по одной (Edit tool). После каждой — Grep-чек.
3. Открой в браузере через `open` для визуальной проверки. Прокликай состояния через dev-bar + новые кнопки.
4. Коммит из /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY (.git в parent):
   cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY
   git add docs_web/wireframes/m2/kiosk-v2.html
   git commit -m "Применил Round 2 правок Kiosk v2: калибровка, BLE-индикатор, drill-down CTA, чистка футера"
   git push
5. Отчёт ≤200 слов: статус (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED), что сделано, SHA, GitPages URL, concerns.

GitPages URL: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html
```

---

## 🔄 Workflow напоминание (subagent-driven-development)

Per task:
1. PM даёт правки (скриншоты/тезисы)
2. Я формирую детальный prompt → запускаю **implementer** агента (background)
3. Имплементатор: код + commit + push + отчёт
4. Запускаю **spec-compliance reviewer** агента
5. Если FAIL → имплементатор фиксит → re-review
6. Если PASS → запускаю **code-quality reviewer**
7. Если NEEDS_FIXES → имплементатор фиксит → re-review
8. Если APPROVED → отчёт PM с GitPages URL + ОЖИДАНИЕ принятия (НЕ закрывать задачу)
9. PM «принято» → отмечаю чекбоксы плана → следующая задача

---

## 🚨 Если auto-compact случился прямо сейчас

1. Прочитать ЭТОТ файл (`docs_web/docs/superpowers/specs/2026-05-25-m2-session-state.md`) — целиком
2. Прочитать `memory/MEMORY.md` + 9 ключевых memory-файлов из списка выше
3. Прочитать план `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` (статус задач)
4. Прочитать `knowledge-base/briefs/2026-05-24-A1-kirill-bek-mobile.md` — статус задач Кирилла
5. Сделать `git log --oneline -20 && git status` — посмотреть актуальное состояние репо
6. Сказать PM: «Контекст восстановлен из handoff. Где остановились: [Этап 1 документов начат/не начат] / [Этап 2 Round 2 Kiosk v2 запущен/не запущен]. Готов продолжить.»

---

## 📌 Открытые риски снапшота

- На момент снапшота `kiosk-v2.html` имеет **unstaged изменения** от UI-дизайнера (работа в параллельном окне VS Code). Закоммичу их вместе со снапшотом сразу после Write этого файла, чтобы зафиксировать его работу в git history.
- Локальные коммиты `97189f0`, `df0a350` (мои session-state правки) ещё не запушены в origin — отправлю вместе со снапшотом.
- 2 локальных коммита от меня + работа UI-дизайнера = всё в одном пуше.