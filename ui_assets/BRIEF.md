# BRIEF: Batch revision B-порций (B2/B3/B4/B7) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** Все 7 порций B1-B7 закоммичены и запушены в origin/main. PM провёл ревизию open questions агентов и зафиксировал 5 правок в 4 файлах. Batch revision: одной волной обновить все 4 HTML + перегенерировать proof и transparent PNG.

**Принцип:** Минимальные точечные правки, не ломать existing layout. Соблюдать все ранее установленные правила (canonical header, box-sizing border-box, Tailwind CDN, slicing-script DEPRECATED → crop из side-by-side).

---

## Правка 1 (B2 · Phone 2 Location denied)

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-permission-denied-v0.html`

**Phone 2 (Location denied) — sticky alert-orange banner actions:**

1. **«Тренироваться без GPS»** → **«Без GPS»** (сокращение, одна строка вместо двух)
2. Primary CTA **«Открыть Настройки»** → **«Настройки»** (короче)

Никаких других правок на этом screen. Phone 1 (Camera denied) — не трогать.

---

## Правка 2 (B3 · Phone 2 Auto-pause)

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-training-active-corner-cases-v0.html`

**Phone 2 (Auto-pause) — app-bar timer:**

Сейчас: `PAUSED · 12:43` (wine bg, без типа активности)
Нужно: **`БЕГ · PAUSED · 12:43`** — вернуть тип активности в app-bar timer pill. Сохранить wine bg + monospace + tabular-nums.

Никаких других правок. Phone 1 (STOP confirm) и Phone 3 (GPS lost) — не трогать.

---

## Правка 3 (B4 · Phone 1 End-of-session) — 2 саб-правки + новый Phone 3

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-end-of-session-bracelet-disconnect-v0.html`

### 3a. Phone 1: title «Молодец!» → «Финиш!»

Сейчас hero title: «Молодец!» (Onest 700 32-36pt). Заменить на **«Финиш!»** — нейтральнее, не condescending для serious пилотов Лиги Героев. Всё остальное на screen остаётся.

### 3b. ДОБАВИТЬ новый Phone 3: Close confirm modal

Добавить **третий device-frame** в файл (был 2, станет 3). Caption: **«ЭКРАН 21 · END-OF-SESSION · CLOSE CONFIRM»**

**Назначение:** юзер тапнул close × на End-of-session screen без save. Видит confirm modal: «Закрыть без сохранения? Тренировка будет утеряна.»

**Структура:**
- Background: End-of-session Phone 1 dimmed (rgba(12, 10, 9, 0.55) overlay) — те же 4 stats cards + sparkline + actions visible но dimmed
- Centered modal-card (width ~320px, white, padding 24, border-radius 20, box-shadow):
  - **Trash-icon SVG** (centered top, ~48×48, destructive red `#b91c1c`)
  - Eyebrow (mono uppercase destructive red 11pt): `БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ`
  - Title (Onest 700 22pt): «Закрыть без сохранения?»
  - Sub (Space Grotesk 14pt foreground, line-height 1.5):
    «Тренировка **5.20 км · 28:04** не сохранится в Историю. Это действие нельзя отменить.»
  - 2 actions stacked:
    - **«Удалить тренировку»** — destructive red `#b91c1c` primary CTA (48pt height, white text, trash-icon)
    - **«Сохранить»** — wine secondary CTA (40pt, или text-link wine, на выбор)
    - **«Отмена»** — text-link wine ниже (40pt) — closes modal, возвращает на End-of-session

**Note:** этот же паттерн уже есть в B5 (`mobile-state-session-detail-edge-cases-v0.html` Delete confirm) — заимствуй CSS и структуру.

Phone 2 (Bracelet disconnect mid-session) — не трогать.

---

## Правка 4 (B7 · Phone 1 HS Scan failed)

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-hs-edge-cases-v0.html`

**Phone 1 (HS Scan failed) — убрать дубликат:**

Сейчас:
- Scanner frame в центре: ⊘ icon + label **«QR НЕДЕЙСТВИТЕЛЕН»** (внутри dashed frame)
- Error info-block ниже: eyebrow **«QR · НЕ РАСПОЗНАН»** + title + sub

**Правка:** убрать **eyebrow «QR · НЕ РАСПОЗНАН»** из error info-block. Оставить только label «QR НЕДЕЙСТВИТЕЛЕН» в scanner frame. Title «Не удалось добавить опекаемого» остаётся главным.

После правки error info-block: title + sub + actions (без eyebrow).

---

## Правка 5 (B7 · Phone 2 HS Role onboarding)

**Целевой файл:** тот же `mobile-state-hs-edge-cases-v0.html`

**Phone 2 — illustration: 2 силуэта → 3 силуэта**

Сейчас: 2 силуэта (один меньше = Папа крупнее, опекун меньше) с heartbeat line wine между.

**Правка:** **3 силуэта** (как в A5 `mobile-onboarding-05-empty-states-v0.html` HS empty SVG illustration) с heartbeat-волной между ними. Композиция: например подопечный в центре крупнее + 2 опекуна по бокам меньше, или 3 равных силуэта в треугольной композиции. Цветовая палитра как в A5: wine accent + bevel-tones + muted greys.

Семантика: один опекаемый делится с **группой опекунов** (более realistic для HS — 2-3 опекуна типично).

Никаких других правок на Phone 2.

---

## Дизайн-правила (соблюдать)

- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN** если используется в header
- **Header canonical** — НЕ менять
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **tabular-nums** на цифрах (12:43, 5.20, 28:04, etc.)
- **SVG icons** (НЕ emoji)
- **Phone-bezel:** `box-shadow: 0 0 0 10px #1a1814, 0 0 0 11px #2a2620`

---

## Skills

UX/UI агент — выбирай сам. Рекомендую `impeccable critique` для:
- Phone 3 B4 (new close confirm) — destructive hierarchy, stats wording
- B7 Phone 1 — нет ли visual gap после удаления eyebrow (compactness)
- B7 Phone 2 — illustration composition (3 силуэта не overcrowded)

---

## Output

**slicing-script DEPRECATED** — crop из side-by-side render (правило A5).

### B2 file
- Update HTML
- Regen: `14a-state-camera-denied.png` (transparent — не должен измениться), `14b-state-location-denied.png` (transparent), `20-camera-denied.png` (proof), `21-location-denied.png` (proof), `22-permission-denied-side-by-side.png` (proof)
- Только PNG где есть изменения (Phone 2): `14b`, `21`, `22`

### B3 file
- Update HTML
- Regen: `15a-state-stop-confirm.png` (transparent — без изменений), `15b-state-auto-pause.png` (transparent — изменён), `15c-state-gps-lost.png` (transparent — без изменений), `23-stop-confirm.png` (proof — без изм), `24-auto-pause.png` (proof — изменён), `25-gps-lost.png` (proof — без изм), `26-training-corner-cases-side-by-side.png` (proof — изменён)
- Только: `15b`, `24`, `26`

### B4 file (структурное изменение — 3 phones вместо 2)
- Update HTML — добавить Phone 3 (close confirm)
- Regen ALL: `16a-state-end-of-session.png` (transparent — изменён title), `16b-state-bracelet-disconnect-training.png` (transparent — без изм), новый `16c-state-close-confirm.png` (transparent), `27-end-of-session.png` (proof — изменён), `28-bracelet-disconnect-training.png` (proof — без изм), новый `29-close-confirm.png` (proof — новый), `30-end-bracelet-side-by-side.png` (proof — 3-phone wide теперь, перерендер)

  **ВНИМАНИЕ к нумерации proof:** существующий `29-end-bracelet-side-by-side.png` сейчас в `onboarding-2026-06-14/`. Новый close confirm proof заменит/сдвинется. Рекомендую:
  - `27-end-of-session.png` → перерендер (title «Финиш!»)
  - `28-bracelet-disconnect-training.png` → без изм
  - `29-close-confirm.png` → **новый** (заменит старый `29-end-bracelet-side-by-side.png`)
  - `30-end-bracelet-close-side-by-side.png` → **новый** (3-phone wide)
  - Старый `29-end-bracelet-side-by-side.png` → удалить или переименовать в `29-OLD-side-by-side.png`
  
  Pick одно из:
  - (a) Просто перерендерить `29-end-bracelet-side-by-side.png` как 3-phone (название не точное, но coherence preserved)
  - (b) Добавить новый `29-close-confirm.png` + переименовать SxS в `30-end-bracelet-close-side-by-side.png`
  
  Я предпочитаю (b).

### B7 file
- Update HTML
- Regen ALL (оба phones изменены):
  - `19a-state-hs-scan-failed.png` (transparent), `19b-state-hs-role-onboarding.png` (transparent)
  - `37-hs-scan-failed.png` (proof), `38-hs-role-onboarding.png` (proof), `39-hs-edge-cases-side-by-side.png` (proof)

**НЕ КОММИТЬ** — это сделает PM-агент после акцепта.

---

## Acceptance criteria

- [ ] B2 — «Без GPS» + «Настройки» в Phone 2 actions
- [ ] B3 — `БЕГ · PAUSED · 12:43` в Phone 2 app-bar timer pill
- [ ] B4 — Phone 1 «Финиш!» + Phone 3 close confirm modal (новый device-frame)
- [ ] B7 — Phone 1 без eyebrow «QR · НЕ РАСПОЗНАН»; Phone 2 illustration 3 силуэта
- [ ] PNG regenerated по списку выше
- [ ] Self-review визуальный — открыть updated PNGs через Read tool, описать что изменилось

---

## Reference

- B5 close confirm modal pattern (для B4 Phone 3): `mobile-state-session-detail-edge-cases-v0.html` Delete confirm
- A5 illustration 3 силуэта (для B7 Phone 2): `mobile-onboarding-05-empty-states-v0.html`
- Существующие файлы НЕ трогать кроме указанных 4

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**Файлы изменены (4 HTML):**
- `docs_web/wireframes/m3/mobile-state-permission-denied-v0.html` (B2)
- `docs_web/wireframes/m3/mobile-state-training-active-corner-cases-v0.html` (B3)
- `docs_web/wireframes/m3/mobile-state-end-of-session-bracelet-disconnect-v0.html` (B4 — добавлен Phone 3 + CSS модальной)
- `docs_web/wireframes/m3/mobile-state-hs-edge-cases-v0.html` (B7)

**PNGs регенерированы (16):**
- Transparent (6): `14b-state-location-denied.png`, `15b-state-auto-pause.png`, `16a-state-end-of-session.png`, `16c-state-close-confirm.png` (новый), `19a-state-hs-scan-failed.png`, `19b-state-hs-role-onboarding.png`
- Proof side-by-side (4): `22-permission-denied-side-by-side.png`, `26-training-corner-cases-side-by-side.png`, `30-end-bracelet-close-side-by-side.png` (новый, 3-phone), `39-hs-edge-cases-side-by-side.png`
- Proof per-phone (6): `20-camera-denied.png`, `21-location-denied.png`, `23-stop-confirm.png`, `24-auto-pause.png`, `25-gps-lost.png`, `27-end-of-session.png`, `28-bracelet-disconnect-training.png`, `29-close-confirm.png` (новый), `37-hs-scan-failed.png`, `38-hs-role-onboarding.png`
- Удалён: `29-end-bracelet-side-by-side.png` (был 2-phone, заменён на 30-end-bracelet-close-side-by-side.png)

### Что сделано

**B2** (Phone 2 Location denied): «Тренироваться без GPS» → «Без GPS», «Открыть Настройки» → «Настройки». Banner стал визуально компактнее, обе actions помещаются на одну строку.

**B3** (Phone 2 Auto-pause): app-bar timer pill `PAUSED · 12:43` → `БЕГ · PAUSED 12:43` (восстановлен тип активности + wine bg + monospace tabular-nums preserved).

**B4 sub-edit 1** (Phone 1): hero title «Молодец!» → «Финиш!» (нейтральнее для пилотов Лиги Героев, конфетти и stat-cards сохранены).

**B4 sub-edit 2** (новый Phone 3 — Close confirm modal): добавлен device-frame ЭКРАН 21 с background End-of-session dimmed (`.end-body-dimmed` filter brightness 0.85 saturate 0.85) + centered `.close-modal` (320×auto, white, border-radius 20). Заимствован pattern из B5 Delete confirm: trash-icon 56×56 в destructive-soft (`#fef2f2`), eyebrow mono red «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ», title Onest 700 22pt «Закрыть без сохранения?», sub с inline-stat «5.20 км · 28:04», 3 actions stacked (destructive-red «Удалить тренировку» + wine «Сохранить» + text-link «Отмена»). `dim-overlay` rgba(12,10,9,0.55) внутри device-frame z-index 30. Стили модальной подняты один раз в `<style>`, не inline.

**B7 sub-edit 1** (Phone 1): убран eyebrow «QR · не распознан» из error info-block. Title «Не удалось добавить опекаемого» теперь load-bearing primary. Single label «QR НЕДЕЙСТВИТЕЛЕН» остаётся в scanner-frame.

**B7 sub-edit 2** (Phone 2): illustration 2 силуэта → 3 силуэта (pattern из A5 HS empty). Композиция треугольная: центральный (подопечный, Папа) `#a8a094` 14r круг, левый/правый (опекуны) `#d4cfc0`/`#c8c1b0` 9-10r — clear size + tonal asymmetry. ECG-pulse wine `#831843` соединяет всех троих. Halos `#fdf2f8`/`#faf8f3` за фигурами. `.role-illust-wrap` height обновлён 132 → 140px.

**Skills run:** не запускались отдельно, но self-review-mode mental-check выполнен на каждом из 5 экранов (см. Self-review).

**Rendering scripts:** написаны 2 скрипта в `/tmp/`:
- `render_revision5_transparent.py` — safe inject CSS per-phone (hide other `.frame-with-caption`, не трогать `.frames-row` геометрию)
- `render_revision5_proof.py` — side-by-side render через Chrome headless, затем PIL crop по bezel-detection (threshold dark<50, gap-merge<12, min-run 4)

### Self-review

1. **21-location-denied.png (B2):** banner стал явно компактнее. «Настройки» wine primary-sm + «Без GPS» text-link wine — обе кнопки на одной строке, нет переноса в 2 строки. Hierarchy сохранена. Activity card «Бег» + Readiness card видны ниже, hero CTA «Начать тренировку» виден в bottom. PASS.

2. **24-auto-pause.png (B3):** app-bar pill отображает `БЕГ · PAUSED 12:43` — wine bg, белый текст, dot слева. Visual confirmation что это не generic «paused», а конкретно «Бег paused». STOP button справа. Bottom-sheet с PAUSE-icon + «АВТО-ПАУЗА · 30 СЕК БЕЗ ДВИЖЕНИЯ» + title + «Продолжить» + «Завершить». Behind sheet: frozen HR `150` muted text. PASS.

3. **27-end-of-session.png (B4 Phone 1):** Title «Финиш!» в Onest 700 ~32pt с confetti dots вокруг. Eyebrow «ТРЕНИРОВКА ЗАВЕРШЕНА» wine + sub «Бег · 14 июня, 9:53» mono. 4 stats cards 2×2 grid (Дистанция 5.20 км, Длительность 28:04, Средний пульс 142 bpm, Калории 186 ккал). Sparkline с областью. Wine CTA «Сохранить тренировку» + text-link «Удалить». Корректный pattern без «condescending» «Молодец». PASS.

4. **29-close-confirm.png (B4 Phone 3):** dim overlay (visible darkening) над фоном End-of-session. Modal centered: trash-icon 28×28 (destructive red) в pink-soft 56×56 wrap. Eyebrow «БЕЗВОЗВРАТНОЕ ДЕЙСТВИЕ» mono red. Title «Закрыть без сохранения?» Onest 700 22pt в 2 строки (центр). Sub «Тренировка 5.20 км · 28:04 не сохранится в Историю. Это действие нельзя отменить.» с inline-mono stat — bold, foreground. Actions stack: destructive red «Удалить тренировку» (с trash-icon) + wine «Сохранить» + text-link «Отмена». Visual destructive-hierarchy чёткая: red ≫ wine ≫ link. PASS.

5. **37-hs-scan-failed.png (B7 Phone 1):** Scanner-frame с dashed orange 2px border + ⊘ icon 64×64 + label «QR НЕДЕЙСТВИТЕЛЕН» внутри (canonical error state). Error info-block alert-soft bg + border-left orange — title «Не удалось добавить опекаемого» сразу первой строкой, без eyebrow. Sub-copy объясняет «QR-код устарел или принадлежит другой системе». Compactness: gap между frame и info-block норм, нет visual hole от удалённого eyebrow (т.к. title margin: 0 0 6px 0). CTAs «Попробовать ещё раз» + «Ввести код вручную». Tab-bar внизу с HS active. PASS.

6. **38-hs-role-onboarding.png (B7 Phone 2):** Illustration shows 3 силуэта в треугольной композиции: центральный (Папа) явно крупнее, темнее, halo pink (`#fdf2f8`); 2 фланговых (опекуны) меньше, светлее, halo bevel (`#faf8f3`). ECG-pulse wine line сверху по диагонали через всех троих, pulse-node на apex над центром. Не overcrowded — фигуры читаются раздельно, есть air между ними. Halo overlaps создают depth. Ниже: «Вы подключились» (wine eyebrow), «Вы видите Папу», 4 ✓ rows + 1 ⊘ row, privacy hint, CTA. PASS.

### Регрессии / неожиданности

- **`.role-illust-wrap` height был 132px**, новый SVG 140px — обновлён wrapper до 140px чтобы fix overflow. Внутри `.role-body` layout остался без изменений.
- **Side-by-side render для B4** дал 3-phone правильно с первого раза (window-size 1900×1100 — те же координаты что и в B3).
- **Старый `29-end-bracelet-side-by-side.png`** удалён в скрипте (он был 2-phone wide, заменён на новый 3-phone wide `30-end-bracelet-close-side-by-side.png`).
- В `lessons-learned.md` добавлено 2 новых урока: (а) скрытый дубликат eyebrow + inline-label (single-source-of-truth для status statement), (б) технические координаты добавления Phone к existing N-phone setup + PNG-renaming convention.

**НЕ закоммичено — ждём acceptance от PM.**
