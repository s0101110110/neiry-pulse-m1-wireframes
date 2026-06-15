# BRIEF: Corner cases B7 — HS edge cases (Scan failed + Role onboarding user B) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1-B6 приняты и закоммичены. **B7 — последняя порция (7 из 7) Ф1.5 corner cases.** Закроет полностью все corner-cases из аудита 14.06 §3.

**Цель:** закрыть Health Sharing edge cases:
- **HS Scan failed** (M-15) — QR недействителен или истёк → юзер видит explainer + retry
- **HS Role onboarding user B** (M-16) — при первом сканировании QR опекун видит роль «вы наблюдатель» с explainer что доступно

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-hs-edge-cases-v0.html`

---

## Источники правды

- **Аудит §2.2 finding 2:** «Health Sharing E2E не закрывает AC-1.10 на стороне получателя (user B). Нужен empty-state «вы только наблюдаете» + onboarding role»
- **Аудит M-15:** «HS Scan failed / camera denied — «Камера недоступна. Разреши в Настройках» / «Этот QR недействителен»»
- **Аудит M-16:** «HS Role onboarding (user B) — при первом сканировании → «Вы видите Сергея П. как тренер / опекун. Что вы видите: HRV, пульс, шаги, fall-alert»»
- **Reference:** `mobile-health-sharing-v0.html` (canonical HS flow + Scan QR layout)
- **B2 Camera denied pattern** (уже сделали): `mobile-state-permission-denied-v0.html` — НЕ дублируем, B7 это OTHER scan failures (QR invalid / expired / scan timeout)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 26** · HS SCAN QR · INVALID/EXPIRED»
- «**ЭКРАН 27** · HS ROLE · USER B ONBOARDING»

---

## Phone 1 · HS Scan QR с invalid/expired QR (HS Scan failed)

**Назначение:** юзер сканирует QR-код — camera работает, но **QR неверный** (истёкший / искажённый / не наш). Показать explainer + retry button. **Не** Camera denied (это B2).

**Контекст:** Scan QR layout (есть scanner frame с пунктирной рамкой) — но в центре scanner area показан **error overlay** с alert-orange tint.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:53
- App-bar: back-chevron «‹» + title «Сканировать QR» (centered)

### Scanner frame (top zone)
- Темно-серый camera-preview placeholder (mimics live camera)
- Centered scanner-rectangle dashed wine border (~240×240, rounded 16px)
- В центре rectangle — **alert-orange ⊘ icon SVG** (large ~64×64) + **«QR недействителен»** label под icon

### Error info-block (под scanner frame)
- Background: `#fdf3e1` alert-soft + border-left 4px `#d97706` alert-orange (consistency B1/B2/B3)
- Padding 16-20px
- Eyebrow (mono uppercase 11pt alert-orange): `QR · НЕ РАСПОЗНАН`
- Title (Onest 700 18pt): «Не удалось добавить опекаемого»
- Sub (Space Grotesk 13-14pt foreground, 2-3 строки):
  «Этот QR-код устарел или принадлежит другой системе. Попросите ещё раз сгенерировать код в Neiry Pulse.»

### Actions (2 buttons stacked под error)
- **«Попробовать ещё раз»** — wine primary CTA (48pt full-width, refresh-icon SVG)
- **«Ввести код вручную»** — text-link wine secondary (40pt, под CTA)

### Tab-bar
Дом / История / Health Sharing (active wine) / Ещё (canonical)

---

## Phone 2 · HS Role onboarding (user B видит роль наблюдателя)

**Назначение:** опекун (user B, например Сергей-сын для Папы) **впервые** сканирует QR от опекаемого. После Success — попадает на **Role onboarding screen** — explainer «Вы наблюдатель. Вот что вы видите». После него попадает в HS Main с подключённым подопечным.

**Контекст:** Full-screen modal/onboarding-style. После HS Success transitional → этот screen → HS Main.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:54
- App-bar: пустой левый + close-icon «×» top-right (skip, попадает в HS Main без explainer)

### Hero block (centered, top half)
- **SVG illustration** (НЕ stock, НЕ emoji):
  - Connection-illustration: 2 силуэта людей (один меньше, один больше) + соединительная line/heartbeat между ними (wine accent)
  - Размер ~120-140px высота, центрирован
- Eyebrow (mono uppercase wine 11pt): `ВЫ ПОДКЛЮЧИЛИСЬ`
- Title (Onest 700 22-24pt foreground): «Вы видите Папу»
- Sub (Space Grotesk 14pt foreground, line-height 1.5):
  «Папа поделился с вами своими ключевыми показателями здоровья. Вы — наблюдатель, не можете изменять его настройки.»

### «Что вы видите» section (центральная, info-list)
- Section title (semibold 13pt mono uppercase): `ЧТО ДОСТУПНО ВАМ`
- 4-5 строк с check-icons SVG (wine) + label:
  - ✓ Пульс сейчас и за день (HR, HRV)
  - ✓ Шаги и активность
  - ✓ Алерт о падении (за 10 секунд)
  - ✓ Качество сна
- 1 строка с ⊘-icon (muted) — что НЕ доступно:
  - ⊘ Личные сообщения и местоположение

### Privacy hint card (subtle)
- Soft Bevel surface, padding 12-16, border-radius 12
- Lock-icon SVG (small ~16, muted)
- Text (12pt muted): «Папа в любой момент может отключить доступ или скрыть конкретные метрики.»

### Primary CTA wine
- Full-width 48pt: «Понятно, перейти к Папе»
- Wine primary, white text, arrow-right SVG

### **БЕЗ tab-bar** (это onboarding-flow, не tab screen)

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих экранов
- **Alert-orange `#d97706`** для QR invalid error + ⊘ icon в scanner frame
- **Alert-soft `#fdf3e1`** для error info-block bg
- **Wine `#831843`** для primary CTAs, check-icons, accent в illustration
- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN** если нужно
- **Header canonical** — заимствуй из `mobile-health-sharing-v0.html` Scan QR layout (back-chevron + title + scanner-frame)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **SVG icons** (НЕ emoji): refresh, lock, check, ⊘ slash-circle, arrow-right, close, scan-rectangle

---

## Skills

UX/UI агент — выбирай сам. Рекомендую critique + audit. Особое внимание:
- Phone 1 error tone — НЕ обвинительный («ты сделал не так»), а helpful («это случается, давай попробуем ещё»)
- Phone 2 role copy — clear privacy boundaries, без condescending к user B

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 2-phone side-by-side.

1. **HTML:** `mobile-state-hs-edge-cases-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `19a-state-hs-scan-failed.png`
   - `19b-state-hs-role-onboarding.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `37-hs-scan-failed.png`
   - `38-hs-role-onboarding.png`
   - `39-hs-edge-cases-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames рядом
- [ ] **Phone 1 HS Scan failed:** scanner-frame layout + alert-orange ⊘ icon overlay в scanner area + error info-block («QR · НЕ РАСПОЗНАН» eyebrow + «Не удалось добавить опекаемого» title + sub) + wine CTA «Попробовать ещё раз» + text-link «Ввести код вручную» + tab-bar HS active
- [ ] **Phone 2 HS Role onboarding:** close × top-right + connection illustration + eyebrow «ВЫ ПОДКЛЮЧИЛИСЬ» + title «Вы видите Папу» + sub про роль наблюдателя + section «ЧТО ДОСТУПНО ВАМ» с 4-5 check-rows + 1 ⊘-row (что не доступно) + privacy hint card с lock-icon + wine CTA «Понятно, перейти к Папе» + БЕЗ tab-bar
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA: alert-orange ≥ 4.5:1, muted ≥ 4.5:1
- [ ] Transparent PNG via crop из side-by-side
- [ ] Self-review визуальный ПЕРЕД отчётом

---

## Open вопросы

1. **«Папу» vs «Сергея П.»** — я выбрал **«Папу»** (consistency с A4 Fall detection mockup где тоже Папа). Если PM хочет generic — «опекаемого». Альтернатива: real name «Сергея П.». Я бы оставил «Папа» — emotional + consistency.
2. **Illustration на Phone 2** — 2 силуэта + heartbeat line или геометрическая abstract? Я выбрал **силуэты + line** (semantic match с «вы видите Папу»). UX/UI агент решает финал.
3. **Privacy hint card** — нужен ли? Я считаю да — это важно для trust в первый момент. Если PM считает overkill — убираем.
4. **CTA «Понятно, перейти к Папе»** — может быть длинно. Альтернативы: «Перейти к Папе», «Открыть HS». Я бы оставил «Понятно, перейти к Папе» — добавляет user agency, не просто command.

---

## Reference

- HS Scan QR layout: `mobile-health-sharing-v0.html`
- B2 Camera denied (parallel pattern, НЕ дублируем): `mobile-state-permission-denied-v0.html`
- A4 Fall detection «Папа» naming: `mobile-onboarding-04-fall-detection-v0.html`
- A5 illustration approach: `mobile-onboarding-05-empty-states-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-hs-edge-cases-v0.html`
**Transparent PNGs:**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/19a-state-hs-scan-failed.png` (420×874, alpha=0 corners)
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/19b-state-hs-role-onboarding.png` (420×874, alpha=0 corners)

**Proof-screenshots:**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/37-hs-scan-failed.png`
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/38-hs-role-onboarding.png`
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/onboarding-2026-06-14/39-hs-edge-cases-side-by-side.png`

### Что сделано

**Phone 1 — HS Scan failed (QR invalid/expired):** App-bar back-chevron + title «Сканировать QR»; dim camera-view (canonical из HS Scan QR — radial gradient + noise + room silhouettes) scaled до height 330px (compact zone, освобождает место под error-block + CTA + tab-bar); dashed wine→alert-orange scanner frame 220×220 с 4 corner-brackets alert-orange `#d97706`; ⊘ slash-circle SVG 64×64 alert-orange + mono label «QR НЕДЕЙСТВИТЕЛЕН» внутри frame; error info-block alert-soft `#fdf3e1` bg + border-left 4px `#d97706` + eyebrow «QR · НЕ РАСПОЗНАН» + title «Не удалось добавить опекаемого» + sub про «устарел или принадлежит другой системе»; wine CTA «Попробовать ещё раз» + refresh-icon SVG; text-link wine «Ввести код вручную»; tab-bar HS active.

**Phone 2 — HS Role onboarding (user B):** Close × top-right (no back); illustration 2 силуэта + heartbeat-wine line (адаптация из A5: левый силуэт больше = Папа `#a8a094`, правый меньше = user B `#c8c1b0`, soft halos primary-soft + card-warm под фигурами, wine pulse-node с outer glow); eyebrow wine «ВЫ ПОДКЛЮЧИЛИСЬ»; title Onest 700 23pt «Вы видите Папу»; sub про роль наблюдателя; section label «ЧТО ДОСТУПНО ВАМ»; 4 ✓ rows wine check-pill (Пульс HR HRV / Шаги / Алерт о падении за 10s / Качество сна) + 1 ⊘ row muted (Личные сообщения и местоположение); privacy hint card warm bg + lock-icon SVG + muted text про «Папа может отключить доступ»; wine CTA full-width «Понятно, перейти к Папе» + arrow-right SVG; БЕЗ tab-bar (onboarding-flow).

### Skills run

Сама задача компактная — paint pattern уже зафиксирован B1–B6. Skills не запускал явно, но применил accumulated lessons:
- **L 2026-06-14 box-sizing + R2 hotfix** — `*, *::before, *::after { box-sizing: border-box }` глобально
- **L 2026-06-14 R2 tab-bar padding-bottom** — `.hs-failed-body padding-bottom: 100px` (76 tab + 24 gap)
- **L 2026-06-14 R2 flex spacer fix** — `margin-top: auto` на `.cta-stack` (НЕ flex-1 spacer)
- **L 2026-06-14 R2 slicing approach** — side-by-side render + PIL crop для proof + safe inject CSS для transparent (НЕ агрессивный inject)
- **L 2026-06-14 empty illustration 3 правила** — tonal asymmetry (3 уровня bevel: `#a8a094` → `#c8c1b0` → halos), size asymmetry (Папа крупнее на 1.3×), один wine accent (heartbeat-line + pulse-node)
- **L Alert-color hierarchy** — peak в scanner frame + error-block, в info-list muted для off-row, не «всё кричит»

### Decisions / compromises

1. **«Папа»** — оставил выбор PM (consistency с A4 Fall detection). НЕ generic «опекаемый».
2. **Illustration: 2 силуэта вместо 3** — A5 показывает 3 (HS empty value-prop), но для role-onboarding 1-to-1 connection нагляднее 2 силуэта (caregivee + observer). Heartbeat сохранён.
3. **Privacy hint card оставил** — за «yes» из open-вопросов; muted tone + warm bg чтобы не конкурировать с CTA.
4. **Scanner-zone не full-screen camera-view (как в HS Scan QR canonical)** — компактный 330px-блок, потому что под ним должен поместиться error-block + 2 CTAs + tab-bar. Decision trade-off: чуть менее «камерное» ощущение vs полный info-architecture без скролла. Pattern совпадает с B2 (camera denied тоже отказывается от full camera view).
5. **Dashed scanner frame alert-orange** (НЕ canonical wine solid corners) — explicit «error state» signal, не позволяет принять за обычное сканирование. Внутри corners — alert-orange (`#d97706`).
6. **CTA Phone 2 «Понятно, перейти к Папе»** оставил полный — добавляет user agency. Длина читается на 390px без переноса.

### Что требует ревизии PM

- **Tone Phone 1 «Не удалось добавить опекаемого»** — passive, не accusatory; «Этот QR-код устарел или принадлежит другой системе» — explainer что *возможно* случилось; «Попросите ещё раз сгенерировать код» — actionable, переводит в next-step. PM скажет ок?
- **Дизайн illustration role-onboarding** — fairly minimal по плотности (2 силуэта vs 3 в A5). Если PM хочет более «inviting» иллюстрацию или другой semantic — нужно правит.
- **«QR НЕДЕЙСТВИТЕЛЕН» label под slash-circle** — дублирование eyebrow в info-block («QR · НЕ РАСПОЗНАН»). Я оставил оба т.к. user сначала смотрит на frame (тут lable instant signal), потом читает explainer ниже. Если PM считает overkill — можно убрать в-frame label.
- **CTA Phone 2 нижний край близок к bezel** — ≈18px gap до home-indicator зоны (iOS safe). Acceptable, но если PM хочет breathing room — добавить `padding-bottom` на role-body.

### Регрессии

Нет. HTML не трогает существующие файлы.

### Self-review (выполнен)

Открыл `37-hs-scan-failed.png` и `38-hs-role-onboarding.png` через Read tool:
- Phone 1: status bar 9:53, app-bar with back + title; scanner zone dim с silhouettes; dashed orange frame с corners + ⊘ glyph + label; alert-soft error block; wine «Попробовать ещё раз» + refresh-icon; text-link «Ввести код вручную»; tab-bar HS active wine. **OK.**
- Phone 2: status bar 9:54, close × top-right; illustration 2 silhouettes + heartbeat wine + pulse-node; eyebrow wine «ВЫ ПОДКЛЮЧИЛИСЬ»; title «Вы видите Папу»; sub про роль; section label uppercase; 4 ✓ rows + 1 ⊘ row; privacy card warm + lock; wine CTA «Понятно, перейти к Папе» + arrow-right. БЕЗ tab-bar. **OK.**
- Transparent PNGs: corner alphas `[0, 0, 0, 0]` — verified.
