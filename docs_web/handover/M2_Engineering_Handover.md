# M2 Engineering Handover — пакет приёмки

**Дата:** 2026-06-04
**Этап:** M2 (Startup Village 28-29.05.2026)
**Адресат:** Никита (CCO, Neiry Pulse)
**PM:** Константин Двугрошев · c.dvugroshev@gmail.com

---

## Пакет артефактов

| # | Артефакт | Путь в репозитории | GitPages URL |
|---|---|---|---|
| 1 | Dashboard корпоратов (рестайл v5 → wine palette + UI Kit M2) | [`wireframes/m3/dashboard-corporate.html`](../wireframes/m3/dashboard-corporate.html) | https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m3/dashboard-corporate.html |
| 2 | Mobile main (live BPM + HRV + шаги + sparkline 24ч) | [`wireframes/m2/mobile-main.html`](../wireframes/m2/mobile-main.html) | https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/mobile-main.html |
| 3 | Спецификация HRV + Steps (формулы, источники, пороги) | [`specs/metrics-hrv-steps-m2.md`](../specs/metrics-hrv-steps-m2.md) | — (Markdown) |
| 4 | Demo Script «Спортсмен» (5-мин сценарий + fallback) | [`demo/Demo_Script_M2_Athlete.md`](../demo/Demo_Script_M2_Athlete.md) | — (Markdown) |
| 5 | UX-test post-mortem (фактура со стенда 28-29.05) | [`reports/post-village-2026-05.html`](../reports/post-village-2026-05.html) | https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/reports/post-village-2026-05.html |
| 6 | M2 Pitch onepager (для печати в PDF / инвесторов) | [`pitch/M2_Pitch_Onepager.html`](../pitch/M2_Pitch_Onepager.html) | https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/pitch/M2_Pitch_Onepager.html |
| 7 | Drill-down карточка гостя (test Баевского, 5 стресс-аватаров) | [`wireframes/m2/kiosk-drilldown.html`](../wireframes/m2/kiosk-drilldown.html) | https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-drilldown.html |

---

## Критерии приёмки

| Артефакт | Критерий |
|---|---|
| HRV+Steps spec | Markdown 1 стр: формулы + источник + пороги + визуализация |
| Demo Script | Читается вслух за 5 мин, есть fallback на отказ устройства/гостя |
| Pitch onepager | Открывается в Chrome 1920×1080, печатается в PDF без обрезок |
| UX post-mortem | Минимум 3 факта «что зашло» + 2 факта «что косячило» |
| mobile-main | BPM live + sparkline истории, без devbar, tabular-nums |
| dashboard-corporate | 3 mode-кнопки (CORP/SPORT/SAFETY), drill-down side-panel, без хардкод hex кроме wine |
| kiosk-drilldown | 5 стресс-аватаров Баевского, кнопка теста, без эмодзи в UI |

---

## Скоуп backend (Кирилл)

Эндпоинты, упомянутые в `specs/metrics-hrv-steps-m2.md`, — задача Кирилла, не входят в пакет PM-handover:
- `POST /v1/metrics/hrv/calculate`
- `GET /v1/metrics/steps/daily`
- Veepoo SDK интеграция: `readRRIntervalByDay`, `readDailyStepByDay`

---

## Out of scope (явно НЕ в пакете)

- Полный M3-дашборд (только рестайл v5 как baseline)
- iOS (решение 20.05 — Android only)
- Figma-макеты (наш формат — HTML+Tailwind, согласовано)
- Юридическая сверка договора по буквам

---

## Контакт

Все вопросы по пакету: **Константин Двугрошев · c.dvugroshev@gmail.com**
