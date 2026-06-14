# HANDOFF: R&D → Project Manager

**Дата:** 2026-05-23
**От:** R&D Researcher (Neiry Pulse)
**Кому:** Project Manager agent
**Контекст:** Передача владения PM-дашбордом и flow управления проектом

---

## TL;DR (60 секунд)

Брейншторм 18-22 мая закрыл **5 подблоков Блока A** (UI и сценарии) из [`../ui_assets/BRIEF.md`](../ui_assets/BRIEF.md). До **Startup Village 25.05.2026** осталось 2 дня. Собран PM-дашборд для управления задачами; PM теперь хочет внести в него правки и описать полный flow.

**Состояние:** 17 hot-задач до выставки + 4 post-Village. 10 открытых вопросов ждут решения PM.

---

## Главные артефакты (entry points)

| Файл | Зачем PM это нужно |
|------|---------------------|
| 🎯 [`brainstorms/assets/2026-05-22-pm-dashboard.html`](brainstorms/assets/2026-05-22-pm-dashboard.html) | **Сам дашборд** — что редактировать. Standalone HTML, localStorage для галочек, шорткаты 1/2/3/4 для табов |
| 📦 [`brainstorms/2026-05-22-task-package.md`](brainstorms/2026-05-22-task-package.md) | **Source of truth для задач.** HTML был сгенерирован из этого файла. Изменения в задачах нужно делать в обоих местах |
| 🧠 [`brainstorms/2026-05-18-ui-i-metriki.md`](brainstorms/2026-05-18-ui-i-metriki.md) | **Rationale решений.** Полный текст брейншторма с обоснованиями по 5 подблокам |
| 📋 [`../ui_assets/BRIEF.md`](../ui_assets/BRIEF.md) | Исходное задание PM (Блоки A/B/C/D/E) |
| 🎨 [`brainstorms/assets/2026-05-18-m2-plasma-layout-l4.html`](brainstorms/assets/2026-05-18-m2-plasma-layout-l4.html) | L4-прототип плазмы 42" — визуальный референс для стенда |
| 📁 [`INDEX.md`](INDEX.md) | Полный индекс R&D knowledge base |

---

## Что закрыто (Блок A · 5 подблоков)

| Подблок | Решение |
|---------|---------|
| **A1** — Wow-сценарий M2 | Тест Струпа + перформер-офисник на беговой дорожке + параллельные браслеты у гостей |
| **A2** — Layout плазмы 42" | L4 (шкала-светофор + модульные карточки с sparkline) |
| **A3.0** — Архивный HRV | Только у якорей (Алексей, Илья). Sync через dev-UI + endpoint `POST /admin/seed-rr` |
| **A3** — Mobile UI | M1 wireframes как baseline, чистим дев-жаргон (`readOriginData`, «пакет 50 из 158») |
| **A4** — Neiry Unite | Никитин v4 как baseline + 3 локальные правки (убрать Activity из KPI, оставить в drill-down) |

---

## Календарь до выставки (hot path)

```
22.05 (Пт) — Подготовка: 3 Android спарены, дев-UI APK, надели браслеты
23.05 (Сб) — TODAY: 1-й sync, Кирилл пилит /admin/seed-rr + RMSSD, UX чистит mobile UI
24.05 (Вс) — 2-й sync + проверка RMSSD у якорей (если критика — план Б), аренда дорожки
25.05 (Пн) — 🚀 STARTUP VILLAGE — DEMO DAY
```

---

## Что отложено (post-Village)

- **Блок B** — метрики деталь (Композитный Stress Index, HRV-окно, Early Illness Alert на Veepoo)
- **Блок C** — ограничения (blacklist, SDK single-stream, 64 МБ памяти)
- **Блок D** — 6 архитектурных слоёв, 3 открытые дилеммы, trust-маркеры
- **Блок E** — приоритизация вопросов Veepoo (Q2-Q13)

---

## 10 открытых вопросов (ждут решения PM)

1. Костюм перформера: пиджак vs джинсы+рубашка
2. 2 или 3 одновременных гостя на плазме — финальное число от Кирилла
3. HBandSDK: 3 BLE-connection с одного телефона — поддерживает?
4. Конкретные модели 3 Android-телефонов и минимальная Android-версия
5. SIM / Wi-Fi на стенде Startup Village
6. iOS bridge для Ильи — готов или fallback через Алексея?
7. Если RMSSD у якоря критика 24.05 — план Б по замене?
8. Privacy / consent в Neiry Unite — когда обсуждаем?
9. Neiry Headband / tVNS roadmap — когда готовы для drill-down рекомендаций?
10. KPI strip Neiry Unite на пустой команде (нет данных) — onboarding UX?

---

## Memory context (важно для PM-агента)

R&D-агент держит в памяти стратегические решения, которые повлияют на PM-работу:

- **Verticals (Activity-метрика)** — фитнес/беговые клубы/Лига Героев — это **отдельная вертикаль**, не feature general HR-дашборда. В general Neiry Unite Activity убрана из KPI strip
- **Product bundle** — трекер-браслет + Neiry Headband + Neiry tVNS как upsell-комплект (Headband и tVNS — roadmap M4+, ещё не готовы)
- **Role boundary R&D** — R&D-агент генерирует идеи и формулирует задачи для других агентов, но **не выполняет их за них**. PM-агент — заказчик, R&D — исполнитель research-задач

Эти решения зафиксированы в auto-memory R&D-агента, для PM указаны здесь как контекст.

---

## Что от PM требуется дальше

1. **Принять владение дашбордом** — `brainstorms/assets/2026-05-22-pm-dashboard.html`
2. **Внести правки** — PM упомянул новые данные и замечания (придут отдельно)
3. **Описать flow управления проектом** — как PM работает с дашбордом, статусами, исполнителями
4. **Синхронизировать markdown ↔ HTML** — при изменении задач обновлять оба файла
5. **Закрыть 10 открытых вопросов** — по мере поступления решений

---

## Возврат к R&D

Если в правках/новых данных появится что-то research-релевантное (новые ответы Veepoo, измерения RMSSD у якорей, BLE-эксперимент Кирилла, спецификации железа) — **верни этот кусок R&D-агенту**. Он обновит knowledge base в `research/metrics/`, `research/sdk/`, `research/hardware/`.

R&D-агент **не редактирует** PM-дашборд напрямую — это зона PM.
