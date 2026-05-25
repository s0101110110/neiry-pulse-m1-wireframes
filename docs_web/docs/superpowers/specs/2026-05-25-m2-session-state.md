# M2 UI Restyle — Session State (2026-05-25, Этап 1 закрыт, переходим к Этапу 2)

> **Назначение:** handoff-документ для восстановления контекста после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.
>
> **Если контекст потерян:** прочти этот файл целиком → `memory/MEMORY.md` + 9 ключевых memory-файлов (см. список) → план M2 UI Restyle → бриф Кирилла A1 → продолжай с раздела «⏭ Очередь работы».

---

## 🚨 СТАТУС НА МОМЕНТ ЭТОГО HANDOFF (2026-05-25, после закрытия Этапа 1)

**Этап 1 M2 UI Restyle ЗАКРЫТ и ЗАПУШЕН.** PM сказал «обнови хенд-офф и идём на Этап 2» → готов диспатчить implementer-агента на Round 2 правок Kiosk v2 (A2 калибровка / A3 drill-down CTA / A5 BLE-индикатор / A6 убрать QR из футера).

**Последние коммиты:**
- `bf1bf9e` в NEIRY (docs_web + UI_assets + research) — запушен на `s0101110110/neiry-pulse-m1-wireframes`.
- `c351d28` в knowledge-base (локально, у этого репо нет remote).

**Working tree в docs_web после push:** только старые unstaged изменения (deleted dashboard-*.html, mobile-*.html, и т.д.) — НЕ моё, не трогать без приказа PM. Чистого нового нет.

---

## ✅ Что СДЕЛАНО в Этапе 1 (закоммичено и запушено)

### Memory-файлы (rename NCI → NSI + уточнения)

7 memory-файлов в `~/.claude/projects/-Users-solomono-Desktop-NOW---------NEIRY/memory/`:
1. `project_neiry_stress_index.md` — переписан под NSI Fast UI metric, зоны 0–39/40–59/60–100, калибровка 12 сек.
2. `MEMORY.md` — индекс обновлён.
3. `project_neiry_m2_kiosk_scenario.md` — NSI + 12 сек + имя гостя из mobile.
4. `project_neiry_ui_aesthetic.md` — NCI→NSI.
5. `project_neiry_ui_stack.md` — `NCIGauge` → `NSIGauge`.
6. `feedback_neiry_pitch_style.md` — питч-якоря: NSI.
7. `project_neiry_risks_strategy.md` — сценарный риск NSI ложно в красное.

### Бриф Кирилла A1

`knowledge-base/briefs/2026-05-24-A1-kirill-bek-mobile.md`:
- Новый блок «🔄 Update PM 25.05.2026» после TL;DR.
- Раздел 3.1 переписан под NSI: формула, warning-блок, зоны, калибровка 12 сек.
- Раздел 3.2 + раздел 5 первая строка — NCI→NSI.
- **Новый раздел 3.3 «Mobile pairing → Plasma handoff»**: 3.3.1 ввод имени гостя · 3.3.2 state machine 5 состояний · 3.3.3 BLE lifecycle (heartbeat 2/lost 5/disconnect 30) · 3.3.4 WebSocket-схема 11 событий + 2 команды.
- Раздел 6 (что подтвердить): 5 новых чекбоксов + дедлайны 27.05/28.05.

### knowledge-base (commit `c351d28`)

8 файлов:
- `PROJECT_STATE.md` — NCI→NSI + калибровка 12 сек + дата 2026-05-25 + блок «Свежие (25.05)».
- `briefs/A2-uxui-drilldown.md` — NSI 78 (🟡→🔴, цвет под новую семантику) + caption «Уровень стресса (NSI: ↑ = стресс ↑)».
- `briefs/A4-nikita-confirmation.md` — NCI→NSI.
- `briefs/A5-pitch-thesis-v0.1.md` — NCI→NSI + питч-фраза «концентрации → стресса в моменте».
- `risks/2026-05-25-m2-merged-for-nikita.md` — NCI→NSI + baseline 12 сек.
- `risks/2026-05-28-startup-village.md` — NCI→NSI + 12 сек.
- `milestones/m2.md` — NCI→NSI + зоны переписаны (🟢80-100 → 🟢0-39).
- `open-questions/index.md` — NCI→NSI + 12 сек.

### docs_web + UI_assets + research (commit `bf1bf9e`, push)

7 файлов:
- `docs_web/wireframes/m2/ui-kit.html` — NCI→NSI (~20 мест) + nsi-gauge id/class + caption «Уровень стресса (NSI · Neiry Stress Index, ↑ значение = ↑ стресс)» + зоны 0-39/40-59/60-100.
- `docs_web/index.html` — NCI→NSI (одна строка).
- `docs_web/wireframes/m2/exhibition-flow.html` — NCI→NSI (~14 мест) + питч-фраза + Stroop-комментарий + 5 точек калибровки 15→12 сек + BLE-блок с lifecycle (heartbeat 2 / lost 5 / disconnect 30).
- `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` — NCI→NSI + Шаг 7 «Round 2 правок Kiosk v2» (A2/A3/A5/A6) в задачу 4 + расширение задачи 5 (формула Баевского, двухступенчатый фильтр R-R) + расширение задачи 7 (mobile name_input + calibrating + state machine).
- `docs_web/docs/superpowers/specs/2026-05-25-m2-session-state.md` — этот файл.
- `UI_assets/BRIEF.md` — NCI→NSI (3 места).
- `research/brainstorms/assets/2026-05-22-pm-dashboard.html` — NCI→NSI + блок «Mobile pairing + handoff на плазму (бриф A1 §3.3)» (5 подзадач Кириллу: k6 name_input · k7 state machine · k8 калибровка 12 сек · k9 BLE lifecycle · k10 WebSocket-схема).

---

## ⏭ Очередь работы — Этап 2 (Round 2 правок Kiosk v2)

**Скоуп Round 2** (через implementer-агента в background):

| # | Правка | Описание |
|---|---|---|
| A2 | Состояние «Калибровка 12 сек…» | Новый атрибут `data-card-state` на `<article>` = idle/calibrating/active/done. В состоянии calibrating: спиннер + текст «Калибровка XX сек…» с обратным отсчётом. Триггер: dev-bar добавить кнопку «Calibrate Guest» — переключает карточку гостя в calibrating на 12 сек, потом active. Edge-case: если семплов < 60% → текст «Чуть дольше, ловим baseline…», окно расширяется до 16 сек. |
| A3 | Drill-down CTA на карточке гостя | Hint «Подробнее →» в правом нижнем углу карточки с hover-эффектом (opacity transition). Клик: `window.location.href = './kiosk-drilldown.html'`. Видимость: только когда у гостя `data-card-state=active`. |
| A5 | BLE-индикатор связи | Dot в шапке КАЖДОЙ карточки рядом с «Neiry.Pulse #N». Состояния: connected (зелёный live-blink, heartbeat ≤2 сек) / lost (жёлтый, ≥5 сек, окно сессии НЕ обнуляется) / disconnected (серый opacity 0.5, ≥30 сек, blur на карточке + «Переподключаемся…»). Триггер: dev-bar добавить toggle «BLE Lost». |
| A6 | Убрать QR-блок из футера | Удалить блок справа в футере: «Подробный отчёт по сессии · Сканируй QR → Telegram-бот» + SVG QR 120×120. В карточке гостя в `pending-claim` QR ОСТАЁТСЯ. Модалка с QR 240×240 ОСТАЁТСЯ. Освободившееся место — короткая подпись «Сними браслет → получи отчёт» + дискретная анимация. |

**Скоуп НЕ Round 2 (отменено / перенесено):**
- ~~A1 rename NSI→NCI~~ **ОТМЕНЕНО** — остаёмся на NSI.
- A4 кнопка Тест Баевского — **только в drill-down** (Задача 5, Этап 3).
- A7 имя гостя — в мокапе хардкод «Гость» (нейтрально для скриншотов).

---

## 📋 Финальные решения PM 25.05.2026 — критично (не менять)

| # | Тема | Решение PM |
|---|---|---|
| 1 | Метрика стресса на плазме | **NSI** (Neiry Stress Index). Зоны: 0-39 НОРМА / 40-59 ПОВЫШЕН / 60-100 ВЫСОКИЙ. Семантика: ↑ = стресс ↑ |
| 2 | Имя гостя | Вводится в mobile app при паринге → state `name_input`. На kiosk-v2 мокапе хардкод «Гость» |
| 3 | Калибровка | **12 секунд**, новое промежуточное состояние. Расширение до 16 сек при недостатке семплов |
| 4 | Тест Баевского | Только в drill-down карточке гостя, опциональная кнопка |
| 5 | BLE-индикатор | Dot в шапке каждой карточки. heartbeat 2 сек / lost 5 сек / disconnect 30 сек |
| 6 | QR на главном экране | В футере убрать. В карточке гостя `pending-claim` остаётся. Модалка остаётся |
| 7 | Welcome-screen | Использовать существующее `active-2` (Костя+Алексей активны, Гость в idle) |
| 8 | Dev-bar в продакшене | Оставить видимым, PM сам уберёт через `?prod=1` |
| 9 | NSI формула | `NSI = 100 − (Current_BPM − Baseline_BPM) × 2`, clamp [0..100]. Baseline = mean BPM за 12 сек калибровки |
| 10 | Mobile pairing | Не новый агент, Задача 7 в плане M2 UI Restyle |
| 11 | ТЗ Кириллу | Не новый документ — расширен бриф A1 (раздел 3.3) |

---

## 📊 Статус задач плана M2 UI Restyle

| # | Задача | Статус | Артефакт | SHA |
|---|---|---|---|---|
| 1 | Калибровка эстетики | ✅ принято | `memory/project_neiry_ui_aesthetic.md` | — |
| 2 | BRIEF.md UX/UI Дизайнера | ✅ принято | `UI_assets/BRIEF.md` | ed14bea + bf1bf9e (NSI rename) |
| 3 | UI Kit | ✅ принято (NSI rename done) | `docs_web/wireframes/m2/ui-kit.html` | dbc2e37 + bf1bf9e |
| 4 | Kiosk v2 | 🟡 Round 1 принят, **Round 2 — Этап 2 СЕЙЧАС** | `docs_web/wireframes/m2/kiosk-v2.html` | 1d8b28b + работа UI-дизайнера (3703975) |
| 5 | Drill-down (3 фазы Bayevsky) | ⚪ pending (Этап 3 после Round 2) | `docs_web/wireframes/m2/kiosk-drilldown.html` | — |
| 6 | Dashboard корпоратов | ⚪ pending | `docs_web/wireframes/m3/dashboard-corporate.html` | — |
| 7 | Mobile pairing + state machine | ⚪ pending | `docs_web/wireframes/m1/mobile-*.html` + новые `mobile-name-input.html` / `mobile-calibrating.html` | — |
| 8 | Финальная индексация | ⚪ pending | `docs_web/index.html` | — |

---

## 🔗 GitPages URLs

- UI Kit: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/ui-kit.html
- Kiosk v2: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html
- Exhibition Flow: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/exhibition-flow.html
- Roadmap-дашборд R&D: https://s0101110110.github.io/neiry-pulse-m1-wireframes/research/brainstorms/assets/2026-05-22-pm-dashboard.html

---

## 🎨 Финальная эстетика (зафиксирована PM 25.05.2026)

- **Шрифты:** Space Grotesk (UI 300-700) + Onest 700 (hero/display, tracking -0.04em) + Geist Mono (data). Кириллица.
- **Палитра светофора (Cyber-flat):** success `#00E676` (`151 100% 45%`), warning `#FFB300` (`42 100% 50%`), destructive `#FF1744` (`348 100% 54%`).
- **Wine accent:** `#831843` (`var(--primary)`).
- **База:** shadcn zinc/slate semantic CSS-переменные.
- **Темы:** тёмная для kiosk, светлая для админ-ноута.
- **NSI-gauge:** Apple Rings (270° arc) для kiosk + Tremor Radial (360° donut) для drill-down. `pathLength=100`, dasharray=100, dashoffset=100-NSI.
- **ECG-визуализация под BPM:** параметрический P-QRS-T генератор, окно ~5.1 сек.

---

## 🛡 Активные правила (ИЗ ПАМЯТИ, критично)

1. **PM acceptance gate** — задача НЕ закрывается без явного «принято» от PM.
2. **HTML-first workflow** — HTML+Tailwind CDN мокапы → передача Кириллу на React.
3. **NDA-safe UI** — НЕТ: VITRO, VANTA, VIGOR, M1/M2/M3 (в UI), Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #N», «Neiry Stress Index» (NSI).
4. **Имена анкеров на M2:** Костя + Алексей. НЕ Илья.
5. **На стенде 28-29.05:** только Костя + Алексей. Никита и Кирилл — НЕ на стенде.
6. **Технические правила:** HTML5 + Tailwind CDN + inline SVG. НЕТ React/Vue/jsx. НЕТ inline-стилей (кроме SVG-параметров и swatch-плиток). Хардкод hex только `#831843`.
7. **Координация с параллельными агентами:** PM часто работает с UI-дизайнером в другом окне VS Code. Перед правкой `kiosk-v2.html` — `git status` + проверка unstaged.
8. **НЕ обновляю исторические логи:** `knowledge-base/decisions/2026-05.md`, `knowledge-base/INBOX/raw/*`, `research/brainstorms/2026-05-22-task-package.md` — NCI там остаётся как есть.

---

## 📁 Ключевые memory-файлы (читать после auto-compact)

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_stress_index.md` — NSI Fast UI + Баевский Slow Backend
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты/референсы
- `memory/project_neiry_ui_stack.md` — стек
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_team_roles.md` — Костя/Алексей/Никита/Кирилл
- `memory/project_neiry_m2_artifacts.md` — карта файлов M2
- `memory/project_neiry_m2_kiosk_scenario.md` — сценарий стенда

---

## 📝 Шаблон prompt для implementer-агента — Round 2 Kiosk v2 (Этап 2 СЕЙЧАС)

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
- В состоянии calibrating: спиннер + текст «Калибровка XX сек…» с обратным отсчётом
- Триггер: dev-bar добавить кнопку «Calibrate Guest» — переключает карточку гостя в calibrating на 12 сек, потом active
- Edge-case: если на 13-й сек семплов < 60% → текст «Чуть дольше, ловим baseline…», окно расширяется до 16 сек

A3. Drill-down CTA на карточке гостя:
- Hint «Подробнее →» в правом нижнем углу карточки с hover-эффектом (opacity transition)
- Клик: window.location.href = './kiosk-drilldown.html'
- Видимость: только когда у гостя data-card-state = active

A5. BLE-индикатор связи:
- Dot в шапке КАЖДОЙ карточки, рядом с «Neiry.Pulse #N»
- Состояния: connected (зелёный live-blink, heartbeat ≤2 сек) / lost (жёлтый, ≥5 сек, окно не обнуляется) / disconnected (серый opacity 0.5, ≥30 сек, blur на карточке + «Переподключаемся…»)
- Триггер: dev-bar добавить toggle «BLE Lost» — переключает все 3 карточки

A6. Убрать QR-блок из правой части футера:
- Удалить блок справа: «Подробный отчёт по сессии · Сканируй QR → Telegram-бот» + SVG QR 120×120
- В карточке гостя в pending-claim QR ОСТАЁТСЯ
- Модалка с QR 240×240 ОСТАЁТСЯ
- Освободившееся место — короткая подпись «Сними браслет → получи отчёт»

НЕ ТРОГАТЬ:
- A1 (rename NSI→NCI) — отменено
- Тест Баевского — это для Задачи 5 (drill-down, Этап 3)
- Имя гостя — хардкод «Гость»
- ECG-генератор P-QRS-T, type-scale, viewport-fit — работа UI-дизайнера

ШАГИ:
1. Прочитай файл целиком.
2. Применяй правки по одной (Edit). После каждой — Grep-чек.
3. open для визуальной проверки. Прокликай состояния через dev-bar.
4. Коммит из /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY:
   git add docs_web/wireframes/m2/kiosk-v2.html
   git commit -m "Применил Round 2 правок Kiosk v2: калибровка, BLE-индикатор, drill-down CTA, чистка футера"
   git push
5. Отчёт ≤200 слов: статус (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED), что сделано, SHA, GitPages URL.

GitPages URL: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html
```

---

## 🚨 Если auto-compact случился прямо сейчас — алгоритм восстановления

1. Прочитать **ЭТОТ файл** (`docs_web/docs/superpowers/specs/2026-05-25-m2-session-state.md`) — целиком.
2. Прочитать `memory/MEMORY.md` + 9 ключевых memory-файлов из списка выше.
3. Прочитать план `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` (статус задач + Шаг 7 Round 2 правок в задаче 4).
4. Прочитать обновлённый бриф Кирилла `knowledge-base/briefs/2026-05-24-A1-kirill-bek-mobile.md` — там новый раздел 3.3.
5. `git status` + `git log --oneline -5` — посмотреть локальные uncommitted и последние коммиты.
6. Сказать PM: «Контекст восстановлен. Этап 1 закрыт (commit bf1bf9e в NEIRY push, c351d28 в knowledge-base локально). Этап 2 — Round 2 правок Kiosk v2 (A2 калибровка / A3 drill-down CTA / A5 BLE-индикатор / A6 убрать QR из футера). Готов диспатчить implementer-агента — шаблон prompt в session-state. Подтверждаешь?»

---

## 💬 Последняя реплика PM

> «Обнови хенд-офф и идем дальше на этап 2.»

(Перед этим Этап 1 был закрыт — два коммита `bf1bf9e` (push) + `c351d28` (knowledge-base локально), 16+ файлов переписаны.)

---

## 🎯 Что отвечать PM сразу после восстановления

> «Handoff обновлён, Этап 1 закрыт (commit bf1bf9e в NEIRY запушен, c351d28 в knowledge-base локально). Готов к Этапу 2 — Round 2 правок Kiosk v2 (A2 калибровка / A3 drill-down CTA / A5 BLE-индикатор / A6 убрать QR из футера). Диспатчу implementer-агента?»
