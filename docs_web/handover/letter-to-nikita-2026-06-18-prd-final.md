# Письмо Никите · PRD v2.6 финализирован

**Дата:** 2026-06-18
**От:** Константин Соломонов (PM)
**Для:** Никита (CCO)
**Документ:** `~/Desktop/Pulse-PRD-v2.6-final-2026-06-18.docx`

---

## Привет, Никита!

PRD v2.6 финализирован. Прикладываю docx с TOC для твоей stakeholder-перепроверки.

Документ зафиксирован в репо: [`docs_web/prds/m3-final-mvp-v2-6.md`](https://github.com/s0101110110/neiry-pulse-m1-wireframes/blob/main/docs_web/prds/m3-final-mvp-v2-6.md) (последний коммит `7df6a9f`).

---

## Что изменилось после твоего акцепта 12.06

### 1. Pulse rebrand (17.06)
Согласовано — приложение называется **Pulse** (а не «Neiry Pulse»). Применено globally: app-bar, splash hero, push notifications, store metadata. Исключение — «Neiry-браслет» (бренд устройства).

### 2. Шрифтовая пара — твой выбор (17.06)
**Golos Text** (UI sans) + **JetBrains Mono** (numbers / labels). Заменяют Onest / Space Grotesk / Geist Mono. Применено во всех 33 wireframes. Правило: «mono для NUMBERS, sans для WORDS».

### 3. Tab-bar 4→5 (17.06)
Дом / Тренировка / История / **Здоровье** / Ещё. «Health Sharing» переименовано в «Здоровье» (русский UI). В MVP store v1 активны только Дом + Ещё, остальные — placeholder «В разработке».

### 4. Anglicisms cleanup (17.06)
Интерфейс **строго на русском**: READY→ГОТОВО, DEMO→ДЕМО, PAUSED→ПАУЗА, STOP→СТОП, baseline→«личная норма», Sleep tracking→«Анализ сна». Исключения: HRV, ms, bpm, Z1-Z5 (медицинские/спортивные обозначения), Bluetooth, QR.

### 5. MVP store submission scope (17.06)
**Согласовано с тобой + Кирилл:** для первой версии store submission реализуем **минимальный scope из 4 разделов**:
- Онбординг (8 экранов)
- Главный экран (Home loaded)
- HRV flow (4 экрана: Baseline ready → First reveal → HRV detail → HRV explainer)
- Настройки (6 экранов: Settings + Profile + BT pairing + Notifications + Privacy + **Калибровка браслета**)

**Итого 19 экранов в MVP v1.**

### 6. Отложено в v2 — после store v1 approval
HTML wireframes готовы, но НЕ подключаем для store v1:
- Health Sharing v1 (QR-pairing + observer flow)
- Training (Start / Active / End-of-session)
- История
- Fall detection (push + in-app banner)
- Все corner cases (BT-disconnect / Auto-pause / GPS lost / etc.)

После v1 approval (≈ 27.06) — открываем v2 с этими feature. Зафиксировано как **§9.1 PRD v2.6**.

---

## Что добавлено в PRD v2.6

### §9.1 Отложено в v2 — новая subsection
Зафиксирована scope cut с явным списком отложенных feature + указанием что HTML уже готов (Кирилл имеет zip).

### R-020 в RISKS.md (v3.1)
Новый риск 🟡 **Backend baseline pipeline + Калибровка re-trigger** (owner: Кирилл).

**Что:** Frontend Калибровка screen готова (17.06), но backend infrastructure для baseline pipeline неясна:
1. Первая калибровка (~36-48 ч сбор HRV данных + формирование personal baseline)
2. Push notification «Личная норма готова» triggers через scheduled job
3. **Re-trigger endpoint** для Settings → Калибровка браслета (сброс старой нормы + новый сбор)

**Митигация по фазам:**
- К **19.06**: baseline pipeline + ready trigger (без re-trigger — отложить)
- К **22.06 pilots**: re-trigger endpoint обязательно (UI обещает что работает)
- Резерв: fallback на системные значения личной нормы (как Sleep demo-режим)

---

## Документы для review

| Файл | Где |
|---|---|
| **PRD v2.6 (docx с TOC)** | `~/Desktop/Pulse-PRD-v2.6-final-2026-06-18.docx` |
| PRD v2.6 (markdown, источник) | `docs_web/prds/m3-final-mvp-v2-6.md` |
| RISKS v3.1 (markdown) | `docs_web/risks/RISKS.md` |
| Handover doc Кириллу | `knowledge-base/briefs/2026-06-18-kirill-mvp-store-handover.md` |
| Все HTML wireframes (33 экрана) | `docs_web/wireframes/m3/` + GitPages URL |

---

## Timeline до pilots

| Дата | Что |
|---|---|
| **19.06.2026 пт** | Ф1 release · финальный bundle Android + iOS готов к store submission |
| **22.06.2026 пн** | Pilots start (Райф / Лига / внутренний beta) |
| **30.06.2026** | Ф2 release · v2 wireframes подключаем feature-by-feature |

---

## Что нужно от тебя

1. **Acceptance PRD v2.6 final** — что зафиксированный scope cut в §9.1 ОК
2. **Acceptance R-020** — что Кирилл owner и митигация-фазы логичны
3. **Опционально:** отправить docx в инвесторам / стейкхолдерам как референс актуального scope

Дай знать после прочтения. Если хочешь обсудить детали — звоним.

Константин Соломонов

---

## P.S.

Все HTML мокапы переданы Кириллу в zip 17.06 + GitPages URL для актуальной версии. Handover doc с пошаговым flow (19 экранов с указанием файлов) — `knowledge-base/briefs/2026-06-18-kirill-mvp-store-handover.md`.
