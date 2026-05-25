# M2 UI Restyle — Session State (2026-05-25)

> **Назначение:** handoff-документ для восстановления контекста после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.

## Текущая ситуация (одним абзацем)

Идёт исполнение плана `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` (8 задач) в режиме subagent-driven-development. Задачи 1-3 закрыты и приняты PM. **Задача 4 (Kiosk v2) технически готова, на ревью у PM — ждём список правок (PM сказал «вижу огромное количество логических и технических ошибок»).** Задачи 5-8 pending.

## Статус задач

| # | Задача | Статус | Артефакт | SHA |
|---|---|---|---|---|
| 1 | Калибровка эстетики (палитра/типографика/токены) | ✅ принято | `memory/project_neiry_ui_aesthetic.md` | — |
| 2 | BRIEF.md UX/UI Дизайнера | ✅ принято | `ui_assets/BRIEF.md` | ed14bea |
| 3 | UI Kit | ✅ принято | `docs_web/wireframes/m2/ui-kit.html` | e18bae3 → 8e1d254 → 8177629 → dbc2e37 |
| 4 | Kiosk v2 | 🟡 на ревью PM (правки ждём) | `docs_web/wireframes/m2/kiosk-v2.html` | 3f076f5 → 1bcb4c7 → 03c0f96 |
| 5 | Drill-down + 3 фазы Bayevsky | ⚪ pending | `docs_web/wireframes/m2/kiosk-drilldown.html` | — |
| 6 | Dashboard корпоратов (Neiry Unite v5) | ⚪ pending | `docs_web/wireframes/m3/dashboard-corporate.html` | — |
| 7 | Mobile pairing рестайл | ⚪ pending | `docs_web/wireframes/m1/mobile-*.html` (in-place) | — |
| 8 | Финальная индексация + push GitPages | ⚪ pending | `docs_web/index.html` | — |

## GitPages URLs (для проверки в браузере)

- UI Kit: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/ui-kit.html
- Kiosk v2: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html

## Финальная эстетика (зафиксирована PM 25.05.2026)

- **Шрифты:** Space Grotesk (UI 300-700) + Onest 700 (hero/display, tracking -0.04em) + Geist Mono (data). Все три с кириллицей.
- **Палитра светофора (Cyber-flat):** success `#00E676` (`151 100% 45%`), warning `#FFB300` (`42 100% 50%`), destructive `#FF1744` (`348 100% 54%`).
- **Wine accent:** `#831843` (`var(--primary)`).
- **База:** shadcn zinc/slate semantic CSS-переменные.
- **Темы:** тёмная для kiosk (плазма), светлая для админ-ноута (drill-down, dashboard).
- **NCI-gauge:** два варианта в UI Kit — Apple Rings (270° arc) для kiosk + Tremor Radial (360° donut) для drill-down.

## Активные правила (ИЗ ПАМЯТИ, критично)

1. **PM acceptance gate** (`feedback_neiry_pm_acceptance_gate.md`) — задача НЕ закрывается без явного «принято» от PM. Spec/code-review = техническая готовность, не замена принятия. Не двигаться к следующей задаче самовольно.
2. **HTML-first workflow** (`feedback_neiry_workflow_html_first.md`) — HTML+Tailwind CDN мокапы → передача Кириллу на React.
3. **NDA-safe UI** — НЕТ упоминаний: VITRO, VANTA, VIGOR, M1/M2/M3 (в видимом UI), Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #1», «Neiry Stress Score».
4. **Имена анкеров на M2:** Костя (Project Lead) + Алексей (B2B Lead). НЕ Илья.
5. **На стенде 28-29.05:** только Костя + Алексей. Никита и Кирилл — НЕ на стенде.
6. **Технические правила:** HTML5 + Tailwind CDN + inline SVG. НЕТ React/Vue/jsx. НЕТ inline-стилей (`style="..."`) кроме SVG-параметров и swatch-плиток документации. НЕТ хардкода hex (только #831843 wine). НЕТ внешних JS-зависимостей кроме Tailwind CDN + Google Fonts.

## Открытые вопросы / ждём от PM

- **Правки по Kiosk v2** — список логических и технических ошибок (PM пришлёт скриншотами + тезисами).
- После применения правок → повторный ревью PM → принятие → старт Задачи 5.

## ⏸ Очередь правок после параллельного UI-дизайнера (НЕ применять сейчас)

**Контекст:** PM параллельно работает с UI-дизайнером в другом окне VS Code над тем же файлом `kiosk-v2.html`. Любые мои правки сейчас создадут конфликт. **Жду явного сигнала PM «UI-дизайнер закончил, можешь править»** — только после этого выполнять.

**Правка #1 (от 25.05, после round 1):** Заменить декоративный R-R sparkline → BPM sparkline за 60 секунд.

- **Почему:** R-R sparkline я добавил сам в commit `3f076f5` без фиксации в спеке. Сейчас это статичный декоративный SVG-зигзаг, не отражающий реальную математику NSI. PM решил: BPM-график понятнее для зрителя.
- **Где:** Все 3 карточки персонажей в `wireframes/m2/kiosk-v2.html`. Sparkline стоит под BPM (между BPM и NSI-gauge).
- **Что делать:**
  - Лейбл: `R-R 60S` → `BPM · 60 сек` (русский)
  - Заменить статичный SVG-path с зигзагом на динамический буфер из 30-60 точек (одна точка ≈ 1-2 сек × 60 сек окно)
  - Подключить к существующему `tickBPM` setInterval JS-функции: каждые 1500ms добавлять текущее BPM значение в буфер, удалять самое старое, перерисовывать polyline
  - Цвет линии: по BPM (мы показываем BPM, а не NSI). Зоны для цвета — уточнить у PM перед имплементацией. Предварительная гипотеза: ≤ 60 → success (resting), 60-100 → foreground/нейтральный (норма), 100-140 → warning (повышенный), > 140 → destructive (высокий).
  - В футере легенды убрать упоминание `RMSSD + R-R distribution · обновление каждые 5 сек` (это тоже моё добавление от commit 3f076f5)
- **Технический риск:** при «живом» обновлении polyline через JS — добавить ограничение на DOM-операции (не пересоздавать SVG, только обновлять `points` атрибут). Префер: фиксированная координатная сетка + сдвиг массива точек.
- **Не трогать:** анимацию BPM числа, NSI gauge, верхнюю градиентную шкалу, состояния data-state.

**Когда PM скажет «можно править»:**
1. `cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY && git pull` (взять изменения UI-дизайнера)
2. Сформировать prompt по шаблону → запустить implementer-агента в background
3. Стандартный цикл: implementer → spec-review → code-quality → ожидание PM acceptance

## Workflow напоминание (subagent-driven-development)

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

## Шаблон prompt для implementer-агента (вставлять при правках)

```
Ты — implementer-субагент для Neiry M2 UI Restyle.

КОНТЕКСТ:
- Файл: /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-v2.html
- Это HTML+Tailwind CDN+inline SVG+vanilla JS мокап kiosk-плазмы 1920×1080 (тёмная тема).
- Token-first: semantic shadcn CSS-переменные, hex только #831843 (wine).
- Шрифты: Space Grotesk / Onest 700 / Geist Mono.
- Палитра: success `151 100% 45%`, warning `42 100% 50%`, destructive `348 100% 54%`.
- Имена анкеров: Костя (PL) + Алексей (B2B). НЕ Илья.
- NDA-stop: НЕТ VITRO/VANTA/VIGOR/M1/M2/M3 в UI.
- Состояния: data-state на body = idle / active-2 / active-3 / pending-claim.
- NCI-gauge: pathLength=100, dasharray=100, dashoffset=100-NCI.

ПРАВКИ ОТ PM:
[вставить список тезисов/скриншоты-описание]

ШАГИ:
1. Прочитай файл целиком.
2. Применяй правки по одной (Edit tool). После каждой — короткий Grep-чек.
3. Открой файл в браузере для визуальной проверки.
4. Коммит из /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY (.git в parent):
   git add docs_web/wireframes/m2/kiosk-v2.html && git commit -m "..." && git push
5. Отчёт ≤200 слов: статус (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED), что сделано, SHA, concerns.
```

## Ключевые memory-файлы (читать после auto-compact)

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты/референсы
- `memory/project_neiry_ui_stack.md` — React-стек (shadcn + Tremor + кастом)
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_team_roles.md` — Костя/Алексей/Никита/Кирилл
- `memory/project_neiry_m2_artifacts.md` — карта файлов M2

## Если auto-compact случился прямо сейчас

1. Прочитать ЭТОТ файл (`docs_web/docs/superpowers/specs/2026-05-25-m2-session-state.md`)
2. Прочитать `memory/MEMORY.md` + 6 ключевых memory-файлов из списка выше
3. Прочитать план `docs_web/docs/superpowers/plans/2026-05-25-m2-ui-restyle.md` (статус задач)
4. Спросить PM: «восстановил контекст M2 после compact, готов принимать правки по Kiosk v2»
