---
title: "Письмо Никите · M2-приёмка + PRD M3 walkthrough"
---

**Дата:** 2026-06-05
**Кому:** Никита (CCO)
**Тема:** M2-приёмка + обновлённый PRD M3 после walkthrough
**Статус:** draft, ожидает отправки

---

Никита, привет.

Закрыл M2-цикл и обновил PRD M3 по итогам walkthrough'а. Делюсь пакетом — посмотри когда будет минут 30-40.

## 🎯 M2 · приёмка (всё закоммичено, рендерится на Pages)

1. **Engineering Handover** — что Кирилл унёс с Village, какой код в продакшене
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/handover/M2_Engineering_Handover.html

2. **Demo Script (Athlete)** — сценарий стенда, fallback'и, что НЕ говорим
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/demo/Demo_Script_M2_Athlete.html

3. **Metrics Spec (HRV/Steps)** — формулы, эндпоинты, пороги для UI
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/specs/metrics-hrv-steps-m2.html

4. **Post-Village отчёт** — что не сработало, что унесли в M3
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/reports/post-village-2026-05.html

5. **Kiosk drill-down (финал R8)** — карточка персонажа с тестом Баевского
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-drilldown.html

6. **Mobile main (M2-обновлённый)** — основа для расширения под Sport/Corporate Mode
   https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/mobile-main.html

## 🚀 M3 · что обновилось сегодня

**PRD M3 (source of truth, после walkthrough):**
https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/prds/m3-final-mvp.html

Ключевые изменения после прохода по 8 секциям:
- Sport-активности: +плавание, +кроссфит
- White-label lite (лого+цвет+домен) для **обоих** пресетов — Лига и Корпорат
- Push: FCM+APNS, обе платформы в W4
- Acceptance: 10 → 11 критериев (+ white-label lite)
- Out-of-scope расширен: multi-role, двойной аккаунт, B2C, tVNS/Recovery — явно похоронено
- +5 новых рисков (R-104..R-108): перегрузка Кирилла, App Store review, юрист, white-label, noser'ы

**PM-дашборд (управление M3-разработкой):**
https://s0101110110.github.io/neiry-pulse-m1-wireframes/research/brainstorms/assets/2026-05-22-pm-dashboard.html

36 задач по неделям W1-W4, R&D-бэклог, риск-реестр, acceptance criteria, today's standup. Сегодня добавил 7 новых задач из walkthrough'а.

**Реестр рисков:**
https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/risks/RISKS.html

## ❓ Где нужно твоё участие

1. **Пилоты W2-W3** — нужны подтверждения по спорт-пилоту и корп-пилоту, без этого AC-5 и AC-9 проваливаются (R-004)
2. **Юрист для privacy policy** — нужен в W1, иначе App Store review блокируется (R-106)
3. **Vigor raw IMU/PPG sample** — sample к W2, иначе сонливость на BPM-derivatives (R-002)
4. **PRD review** — пройдись по §1-§8 и скажи если что добавить/поправить

Готов созвониться в любое время на этой неделе.

— Костя
