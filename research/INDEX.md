# R&D Knowledge Base — INDEX

_Последнее обновление: 2026-05-18_

## Метрики здоровья (metrics/)
- [Vitro Metrics Registry v0.2](metrics/vitro-metrics-registry.md) — полный реестр 58 метрик: Cardio, HRV, Blood, Activity, Sleep, Body, Workout, Safety, Female, Composite, Predictive
- [HRV / ВСР](metrics/hrv.md) — что это простыми словами, формула RMSSD, шкала 60-100/30-60/15-25/<15, окно 00:00-07:00, где считается в архитектуре Neiry
- [RHR / Пульс в покое](metrics/rhr.md) — что это, шкала 40-50/50-60/60-70/>80, окно 00:00-07:00, главный сигнал — изменение от baseline (Early Illness Alert)

## Брейнштормы (brainstorms/)
- [2026-05-18 — UI и метрики](brainstorms/2026-05-18-ui-i-metriki.md) — закрыты Блок A1 (Wow-сценарий M2: A+B4), A2 (layout плазмы L4), A3.0 (архивный HRV на стенде), A3 (Mobile UI = M1 wireframes), A4 (Neiry Unite = Никитин v4 как baseline + 3 локальные правки)
  - 🎨 **Прототип L4** (системо-образующий, для PM и питча): [`brainstorms/assets/2026-05-18-m2-plasma-layout-l4.html`](brainstorms/assets/2026-05-18-m2-plasma-layout-l4.html)

## Сырые источники (sources/)
- [metrics-audit-v0.1.txt](sources/metrics-audit-v0.1.txt) — **аудит 58 метрик от Никиты (16.05)** с trust-маркерами 🟢/🟡/🟠/🔴, 4 дилеммы, 6-слойная стратегия (Hardware→Edge→Mobile→Backend→ML→Presentation), сравнение Polar/Apple/Garmin, Q1 RR-intervals закрыт
- [supplier-questions-v1.txt](sources/supplier-questions-v1.txt) — 13 вопросов Veepoo (Q1 ✅, Q2-Q13 открыты, см. также `knowledge-base/supplier-questions/`)
- [nikita-vision.txt](sources/nikita-vision.txt) — общая рамка Никиты (Demo & MVP): 3 milestone, 2 Mode мобайл, 2 пресета дашборда, стек, In/Out scope, риски, roadmap по неделям
- [nikita-unite-v4-prototype.txt](sources/nikita-unite-v4-prototype.txt) — текст из HTML-прототипа Neiry Unite v4 (HR Dashboard для компаний)
- [levels-short.docx / levels-full.docx / levels-full.txt](sources/) — позиция техлида по 4 уровням метрик L1/L2/L3/L4, формулы Neiry Readiness, Stress Score, Burnout Risk, Drowsiness, blacklist метрик
- [kirill-architecture.txt](sources/kirill-architecture.txt) — архитектура Кирилла: Flutter + FastAPI + Celery + Redis + PostgreSQL + Yandex Cloud
- [ui-references/](sources/ui-references/) — скриншоты mobile-экранов: home screen, HRV view, HRV sync, HRV chart

## Железо (hardware/)
_(пусто — задача: разобрать спецификации Veepoo VE58 PRO)_

## SDK (sdk/)
_(пусто — задача: покурить HBandSDK)_

---

## Что исследовать в первую очередь
1. ~~**HBandSDK методы** — `readRRIntervalByDay`~~ ✅ закрыт в `metrics-audit-v0.1.txt`
2. **HRV (ВСР)** — формулы RMSSD, LF/HF, нормы по возрасту, проблема нулей у архивных данных. Теперь можем считать сами (Q1 закрыт)
3. **SpO2** — принцип работы оптики красного/ИК PPG, точность, почему «жрёт батарею»
4. **Композитные индексы** — Neiry Readiness, Stress Score: формулы из docx Кирилла и Product Sync
5. **Браслет Veepoo VE58 PRO** — спецификации, память (64 МБ), BLE-профиль 5.x
6. **6 архитектурных слоёв** из audit — где какие метрики считать (mobile vs backend vs ML)

## Активные задания (см. BRIEF.md)
- 2026-05-18 — Брейншторм UI и метрик для M2 стенда + Neiry Unite
