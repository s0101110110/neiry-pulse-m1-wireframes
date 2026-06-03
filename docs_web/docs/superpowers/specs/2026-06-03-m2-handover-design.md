# M2 Handover — Дизайн оперативной сдачи

**Дата:** 2026-06-03
**Контекст:** Этап M2 (Startup Village 28-29.05.2026) прошёл. Дедлайны договора (18-24.05) истекли. Нужно собрать пакет артефактов для сдачи Никите ретроспективно — как «материалы, по которым прошла демонстрация».

**Приёмка:** Никита, внутренняя. Формулировки гибкие. НЕ юридическая сверка по буквам.

**Срок:** 1-1.5 рабочих дня (2026-06-03 — 2026-06-04).

---

## 1. Карта артефактов: договор → файл → исполнитель

| # | Пункт договора | Артефакт (путь) | Исполнитель | Стартовый статус |
|---|---|---|---|---|
| 1 | Web-Dashboard (live + история, навигация) | `wireframes/m3/dashboard-corporate.html` — рестайл `INBOX/external/neiry_pulse_v5.html` под нашу DS | UX/UI агент | 🟡 baseline v5 от Никиты |
| 2 | Mobile main (live + история, Material+кастом) | `wireframes/m2/mobile-main.html` — минимальный рестайл из `m1/mobile-home.html` | UX/UI агент | ⚪ создать |
| 3 | Спецификация HRV + Steps (формула, источник, пороги, визуализация) | `docs_web/specs/metrics-hrv-steps-m2.md` | PM | ⚪ создать |
| 4 | Demo_Script «Спортсмен» + питч-материалы | `docs_web/demo/Demo_Script_M2_Athlete.md` + `docs_web/pitch/M2_Pitch_Onepager.html` | PM | ⚪ создать |
| 5 | UX-test report (post-mortem 28-29.05) | `docs_web/reports/ux-test-m2-athlete.md` | PM (требует фактуру со стенда от Кости) | ⚪ создать |
| + | R6 drilldown push в main | `wireframes/m2/kiosk-drilldown.html` | UX/UI агент | 🟢 готово локально |
| + | Engineering Handover index | `docs_web/handover/M2_Engineering_Handover.md` | PM | ⚪ создать |

**Принципиальные решения:**
- `neiry_pulse_v5.html` НЕ переписываем с нуля — рестайл in-place поверх Никитиной структуры (sidebar, mode switcher, drill-down side-panel сохраняются).
- `mobile-main.html` создаётся в `m2/`, а не in-place в `m1/` — M1 остаётся зафиксированным как baseline.
- Все 7 артефактов = единый handover-пакет (документ #7 = индекс ко всем).
- В UI запрещены: VITRO/VANTA/VIGOR, M1/M2/M3, имена B2B-клиентов (см. NDA-правила UX/UI агента).

---

## 2. Workstream split (параллельные треки)

### Трек PM (эта сессия, ~5-6 часов)

1. **HRV + Steps spec** (~1ч) — `docs_web/specs/metrics-hrv-steps-m2.md`
   - Формулы: RMSSD, SDNN из R-R Veepoo SDK; Steps через `readDailyStepByDay`
   - Источники: SDK calls + backend агрегация
   - Пороги: HRV зоны (low/normal/high), Steps daily target
   - Визуализация: где живёт в dashboard и mobile

2. **Demo_Script_M2_Athlete.md** (~2ч) — `docs_web/demo/`
   - Структура: цель / персона / сценарий (3-5 мин) / wow-моменты / fallback
   - Сборка из: `milestones/m2.md`, `briefs/2026-05-24-A5-pitch-thesis-v0.1.md`, фактов прогона

3. **M2_Pitch_Onepager.html** (~1ч) — `docs_web/pitch/`
   - Одноэкранник для инвесторов, готов для печати в PDF
   - На базе ui-kit.html токенов: problem / solution / traction / ask

4. **UX-test post-mortem** (~1.5ч) — `docs_web/reports/ux-test-m2-athlete.md`
   - **Блокер:** требует фактуры стенда от PM (фото/видео/заметки)
   - Структура: что показывали / что зашло / что косячило / устранено on-the-fly / TODO для M3

5. **Engineering Handover index** (~30 мин) — `docs_web/handover/M2_Engineering_Handover.md`
   - Список 7 артефактов + GitPages URL + acceptance-критерии + контакт PM

### Трек UX/UI агент (отдельная сессия, 2 BRIEF-итерации)

**BRIEF #1 (немедленно):**
1. Push R6 drilldown (готов локально, ~15 мин)
2. Создать `wireframes/m2/mobile-main.html` — взять `m1/mobile-home.html`, добавить live-график BPM + history sparkline (24ч), причесать под UI Kit M2 (Manrope/JetBrains/wine accent)
3. Скриншоты + DONE PM

**BRIEF #2 (после acceptance #1):**
1. Анализ `INBOX/external/neiry_pulse_v5.html`
2. Создать `wireframes/m3/dashboard-corporate.html` — рестайл v5 под нашу DS:
   - Inter → Manrope + JetBrains Mono для данных
   - Teal #0F766E → wine #831843 акцент
   - Свои CSS-vars → semantic shadcn-токены (--background, --primary, --muted...)
   - Линеаризация по Linear/Vercel discipline
   - Сохранить 3-mode logic (CORP/SPORT/SAFETY) и Chart.js
3. Скриншоты + DONE PM

---

## 3. Acceptance-критерии по артефактам

| Артефакт | Критерий приёмки PM |
|---|---|
| HRV+Steps spec | 1 стр Markdown, есть формулы + источник + пороги + визуализация. Никита может процитировать пороги. |
| Demo_Script | Можно прочитать вслух за 5 мин, есть fallback на отказ устройства/гостя. |
| Pitch onepager | Открывается в Chrome 1920×1080, печатается в PDF без обрезок. |
| UX post-mortem | Минимум 3 факта со стенда (что зашло), 2 факта (что косячило). |
| Handover index | Все 7 ссылок рабочие (relative paths + GitPages URL). |
| mobile-main.html | Виден BPM live, виден sparkline истории, нет devbar. Применены t-* классы. |
| dashboard-corporate.html | 3 mode-кнопки переключаются, drill-down side-panel открывается, нет хардкод hex кроме --primary. |
| R6 drilldown push | Коммит в main, GitPages обновлён, R6-скриншоты в репо. |

---

## 4. Точки синхронизации

- **Чекпоинт 1** (вечер 2026-06-03): бумага PM (1-3) готова, агент BRIEF#1 в работе.
- **Чекпоинт 2** (утро 2026-06-04): UX-report и Handover (4-5) готовы; даю агенту BRIEF#2.
- **Чекпоинт 3** (вечер 2026-06-04): полный пакет → PM-acceptance каждого артефакта → push в main → отправка Никите.

---

## 5. Риски и зависимости

| Риск | Митигация |
|---|---|
| Нет фактуры со стенда → UX-report = фикция | Спросить Костю сегодня; fallback — отчёт «соответствие макетов реализованному ПО» |
| Агент застрянет на рестайле v5 (337 строк чужого кода) | BRIEF #2 содержит чёткий список замен (Inter→Manrope, teal→wine); если зависнет — режу скоуп до «токены + типографика» без структурных правок |
| Стиль `dashboard-corporate` разъедется с `mobile-main` | PM acceptance gate после каждого BRIEF: сверка скриншотов; никакого commit/push до OK |
| Никита захочет PDF-версию питча | Onepager верстается print-ready изначально (A4 portrait, @media print) |
| INBOX-файл v5 потеряется | Сразу после взятия в работу — move в `INBOX/external/.processed/neiry_pulse_v5.html` |

---

## Out of scope (явно НЕ делаем)

- Полный M3-дашборд (только рестайл v5 как baseline для M2-сдачи).
- iOS-приложение (решение 20.05 — Android only).
- Figma-макеты (наш формат — HTML+Tailwind, согласовано).
- Юридическая сверка договора по буквам (приёмка Никиты, гибкая).
- Backend-имплементация эндпоинтов из спеки (это скоуп Кирилла).
