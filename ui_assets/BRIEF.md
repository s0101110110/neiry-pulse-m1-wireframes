# BRIEF: C1 — Profile edit + HRV detail + HRV explainer modal · Neiry Pulse Ф1

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** A1-A5 онбординг + B1-B7 corner cases + batch revision закоммичены и запушены (`085e23f`). PM выявил 2 missing screen-категории: Profile edit (нет mockup'а где юзер вводит личные данные) и HRV detail view (AC-1.4 требует «3 числа + график 30 дней + tap → объяснение»).

**Цель:** закрыть оба gap'а в одной порции **C1** (новая категория — НЕ corner cases). 3 device-frames:
- Phone 1: Profile edit (полный набор полей)
- Phone 2: HRV detail view (whoop-style 30-day chart)
- Phone 3: HRV explainer modal-overlay поверх Phone 2

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-profile-hrv-detail-v0.html`

---

## Источники правды

- **PRD v2.6 §8 AC-1.4:** «HRV экран: 3 числа (today / week avg / month avg) + график 30 дней + tap → объяснение» — MUST Ф1
- **Whoop competitive reference** (`knowledge-base/competitive-design/whoop.md`):
  - Hero metric ~70pt readable at arm's length
  - 30-day line chart + baseline horizontal line + daily dots
  - Progressive disclosure (overview → trends → deep data)
  - Whoop colors: dark BG + spring green accent. **Для Neiry: Light Bevel base + wine accent** (НЕ копируем dark wholesale)
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)
- **Reference (existing):**
  - `mobile-home-f1-v0.html` — Home с HRV widget (canonical header + tab-bar)
  - `mobile-settings-v0.html` — Settings (canonical entry point для Profile)
  - `mobile-onboarding-03-notifications-calibrating-v0.html` Phone 3 — Baseline modal (pattern для HRV explainer modal-overlay)

---

## Структура HTML (3 device-frames рядом)

Caption:
- «**ЭКРАН 28** · PROFILE · EDIT»
- «**ЭКРАН 29** · HRV · DETAIL VIEW»
- «**ЭКРАН 30** · HRV · EXPLAINER MODAL»

---

## Phone 1 · Profile edit (полный набор)

**Назначение:** юзер в Settings → Профиль → Редактировать. Видит form со всеми личными данными. Save → возврат в Settings.

**Контекст:** Light Bevel form-screen. Доступ через tab «Ещё» → раздел «Профиль» → edit.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:55
- App-bar: back-chevron «‹» + title «Профиль» (centered) + «Сохранить» text-link wine top-right

### Avatar block (top zone, centered)
- Circular avatar 96-100px (border-radius 50%, soft bevel-border)
- Placeholder/photo: muted-grey gradient circle с initials «КЛ» (Onest 700 28pt foreground)
- Под avatar: text-link wine 13pt «Изменить фото» (camera-icon SVG)

### Form fields (stacked, label-above-input pattern)
Каждое поле: label (mono uppercase 11pt muted) + input/value (Space Grotesk 16pt foreground), divider thin border-bottom

1. **Имя** — input «Костя Леонов»
2. **Email** — input «kostya@neiry.com» (muted-grey readonly indicator)
3. **Дата рождения** — date picker placeholder «12 марта 1989» (chevron «›» right indicating tap-to-edit)
4. **Пол** — segment control (3 options): «Мужской» selected wine / «Женский» / «Другое»
5. **Рост** — input numeric «178 см» (tabular-nums)
6. **Вес** — input numeric «76 кг» (tabular-nums)
7. **Цели** — chevron `›` right с preview «Шаги 6 000 · 4 тренировки/нед» (collapsed section, tap → expanded modal)

### Connected device section (под form)
- Section title (mono uppercase 11pt muted): `БРАСЛЕТ`
- Card: «VIGOR-XYZ123» (semibold) + sub «подключён · уровень заряда 87%» (mono 12pt muted, success-green dot) + chevron `›` (tap → device settings)

### Bottom (footer-area)
- Text-link destructive red «Удалить аккаунт» (14pt, под form, padding 24)

### Tab-bar
Дом / История / Health Sharing / Ещё (active wine) — canonical

---

## Phone 2 · HRV detail view (whoop-style 30-day chart)

**Назначение:** юзер тапнул HRV widget на Home → попал в detail view. Видит quick stats + 30-day chart + actionable advice.

**Контекст:** Light Bevel + wine accent. Inspired by Whoop, но adapted to Neiry palette.

**Структура (сверху вниз):**

### Status bar + App-bar
- Status bar 9:55
- App-bar: back-chevron «‹» + title «HRV» (centered) + ⓘ info-icon SVG top-right (tap → opens Phone 3 explainer modal)

### Hero block (centered, top zone)
- Eyebrow (mono uppercase wine 11pt): `СЕГОДНЯ · 9:48`
- Hero number: **«52»** (Onest 700 96pt foreground, tabular-nums) + label «**ms**» (Space Grotesk 16pt muted, inline)
- Delta strip ниже: 
  - «**+8%** к среднему за неделю» (mono 12pt, success-green wine `#831843` для positive)
  - «**+12%** к baseline» (mono 12pt, success-green)
  - Если delta negative — alert-orange

### 30-day line chart (whoop-style)
- Container: full-width card, padding 16-20, border-radius 16, Bevel-soft bg
- Title row: `30 ДНЕЙ` (mono uppercase 11pt muted) + right toggle pills «**30Д**» wine selected / «7Д» / «Год» (tap to switch range)
- Chart area: height ~140-160px
- **Y-axis:** 3 ticks (~30 / ~50 / ~70 ms, mono 10pt muted-foreground, right-aligned text)
- **X-axis:** 5 ticks (даты, mono 10pt muted, например «15.05 / 22.05 / 29.05 / 05.06 / 12.06»)
- **Line:** smooth wine line connecting 30 daily points
- **Baseline horizontal line:** dashed muted-grey at ~47 ms (label «baseline 47 ms» right side, 10pt mono muted)
- **Daily dots:** small wine circles на line (radius 3-4px), today's dot — larger wine-filled с ring (radius 6px) + tooltip-label «52 ms»
- **Area fill** под line: wine soft (rgba 4-5% opacity) — для visualHints volume

### 3-metric strip (под chart)
3 carded values inline (gap 8, equal width):
- **СЕГОДНЯ** `52` ms (semibold)
- **СРЕД. НЕДЕЛЯ** `48` ms (regular)
- **СРЕД. МЕСЯЦ** `45` ms (regular)
Каждая ячейка: card light Bevel, padding 12, border-radius 12, label mono 10pt muted + value Onest 700 24pt + unit mono 11pt muted

### Insight card (контекстная рекомендация)
- Card light Bevel + wine accent border-left 3px
- Icon: heart-pulse SVG (wine, 20×20)
- Title (semibold 14pt): «HRV выше нормы»
- Sub (Space Grotesk 13pt foreground, 2 строки):
  «Хорошая neuro-vegetative balance. Можно интенсивную тренировку или recovery-фокус.»

### Bottom (опц., text-link)
- «Узнать больше про HRV» (wine text-link 14pt, ⓘ icon) → opens Phone 3 modal

### Tab-bar
Дом (active wine) / История / Health Sharing / Ещё (canonical) — это nested screen из Home tab

---

## Phone 3 · HRV explainer modal-overlay (поверх Phone 2)

**Назначение:** юзер тапнул ⓘ icon в app-bar или text-link «Узнать больше про HRV» — видит **bottom-sheet** с объяснением что такое HRV, как читать дельты, зачем baseline.

**Контекст:** Phone 2 visible сверху (chart, hero, etc.) + semi-transparent overlay rgba(12, 10, 9, 0.45) + bottom-sheet card 70-75% screen снизу.

**Структура:**

### Background (dimmed Phone 2)
- Phone 2 layout visible но dimmed через overlay rgba 0.45

### Bottom-sheet (70-75% screen снизу)
- Background: white card
- Border-top-radius 24px
- Padding 20-24px, padding-bottom 32
- Sheet handle на top (40×4px rounded, muted-grey)
- Close × top-right (small, muted)
- Eyebrow (mono uppercase wine 11pt): `КАК ЭТО РАБОТАЕТ`
- Title (Onest 700 22pt foreground): «Что такое HRV?»

### Explainer body (2-3 параграфа)
- Para 1 (Space Grotesk 14pt foreground, line-height 1.5):
  «**HRV** (heart rate variability) — это вариабельность интервалов между ударами сердца, в миллисекундах. Чем выше — тем лучше нервная система отдохнула и готова к нагрузке.»
- Para 2:
  «Мы измеряем HRV каждое утро после пробуждения. Сравниваем с вашим личным baseline (среднее за 30 дней).»

### «Как читать график» bullets section (3 строки)
Под title section `КАК ЧИТАТЬ ГРАФИК` (mono uppercase 11pt muted):
- ▲ icon (success-green) «**+10% и выше** к baseline — отличное восстановление»
- ● icon (wine) «**±10%** к baseline — норма»
- ▼ icon (alert-orange) «**−10% и ниже** — стресс или недосып»

### Divider thin border

### Disclaimer
Sub-section (12pt muted, 2 строки):
«**Не медицинская диагностика.** HRV меняется от множества факторов: сон, тренировки, кофе, алкоголь, стресс. Если стабильно низкие значения — обратитесь к врачу.»

### Primary CTA wine
- Full-width 48pt: «Понятно»
- Wine primary, white text

---

## Дизайн-принципы

- **Light Bevel-tone** для всех 3 экранов
- **Wine `#831843`** для primary CTA / accent / hero number / daily dots / today marker
- **Success-green** (`#65a30d`) для positive delta (+8% к среднему) + ▲ icon
- **Alert-orange** (`#d97706`) для negative delta + ▼ icon
- **Muted-grey** для baseline dashed line + axis labels + secondary text
- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN**
- **Header canonical** — back-chevron + title-bar pattern (НЕ Home canonical с logo/bell/avatar — это nested screen)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на всех цифрах (52, 48, 45, 47, 178, 76, 87, 12.03.1989)
- **SVG icons** (НЕ emoji): heart-pulse, info-circle, chevron-right, camera, arrow-up-trend, arrow-down-trend, baseline-mark, close

---

## Skills

UX/UI агент — выбирай сам. Особое внимание:
- Chart proportions — высота / ширина / line-thickness / dot-size readable but not overcrowded
- Profile form readability — label/value contrast WCAG AA
- Modal explainer не overcrowded (2-3 параграфа max)

**НЕ запускать:** init/document/craft/extract.

---

## Output (transparent PNG)

**slicing-script DEPRECATED** — crop из 3-phone side-by-side render (window-size ~1900×1100).

1. **HTML:** `mobile-profile-hrv-detail-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `20a-profile-edit.png`
   - `20b-hrv-detail.png`
   - `20c-hrv-explainer-modal.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `40-profile-edit.png`
   - `41-hrv-detail.png`
   - `42-hrv-explainer-modal.png`
   - `43-profile-hrv-side-by-side.png` (3-phone wide)

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 3 device-frames рядом
- [ ] **Phone 1 Profile edit:** back + title «Профиль» + «Сохранить» top-right + avatar 96px + 7 form fields (Имя / Email / DOB / Пол / Рост / Вес / Цели chevron) + Connected braclet card + «Удалить аккаунт» text-link destructive внизу + tab-bar «Ещё» active
- [ ] **Phone 2 HRV detail:** back + «HRV» + ⓘ icon + hero «52 ms» (96pt) + delta strip (+8% wine / +12% baseline) + 30-day chart (range toggle / Y-axis / X-axis / smooth wine line / dashed baseline / daily dots / today highlight / area fill) + 3-metric strip (today/week/month) + insight card + tab-bar «Дом» active
- [ ] **Phone 3 HRV explainer:** Phone 2 dimmed + bottom-sheet 70-75% (sheet handle + close × + eyebrow + title «Что такое HRV?» + 2 paragraph explainer + 3 bullets «как читать» + disclaimer + wine CTA «Понятно»)
- [ ] Whoop-style line chart (30-day, line + baseline + dots + today highlight)
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA contrast на all
- [ ] Transparent PNG via crop из 3-phone side-by-side
- [ ] Self-review визуальный ПЕРЕД отчётом — открыть все 3 proof PNG

---

## Open вопросы

1. **Profile DOB display** — «12 марта 1989» (formatted) или «12.03.1989» (mono numeric)? Я выбрал **formatted** (humanizing), но если PM хочет consistent с mono цифрами — поменяем.
2. **Profile: добавить blood type / chronic illness?** Эти поля упоминались в PRD для Ф2 onboarding (вопросник). Сейчас НЕ добавляем — это будет в Ф2 detailed onboarding. Если PM хочет — добавить ниже Цели.
3. **HRV chart range toggle** — 30Д / 7Д / Год — какие три? Whoop использует 30D / 6M / 1Y. Я бы взял **30Д / 7Д / Год** (русифицированные сокращения, 30Д default).
4. **Insight card копи** — «HRV выше нормы» + сов «Хорошая neuro-vegetative balance» — может звучать слишком technically. Альтернатива: «Отличное восстановление» + «Хорошо отдохнули — можете тренироваться интенсивно». PM может уточнить.
5. **Connected braclet card на Profile** — действительно нужен здесь или в Settings? Я бы оставил здесь как preview (юзер видит сразу свой gear), full management в Settings.

---

## Reference

- Whoop HRV pattern: `knowledge-base/competitive-design/whoop.md` (30-day line chart + baseline + dots + progressive disclosure)
- Home f1 (canonical for HRV widget entry-point): `mobile-home-f1-v0.html`
- Settings (canonical Profile entry-point): `mobile-settings-v0.html`
- Baseline modal pattern (для HRV explainer): `mobile-onboarding-03-notifications-calibrating-v0.html` Phone 3

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `docs_web/wireframes/m3/mobile-profile-hrv-detail-v0.html` (3 device-frames в одном файле)
**Transparent PNGs:** `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/{20a-profile-edit, 20b-hrv-detail, 20c-hrv-explainer-modal}.png` (420×874, alpha=0 верифицирован)
**Proof-screenshots:** `UI_assets/screenshots/onboarding-2026-06-14/{40-profile-edit, 41-hrv-detail, 42-hrv-explainer-modal, 43-profile-hrv-side-by-side}.png`

### Что сделано
- **Phone 1 Profile edit:** App-bar nested (back ‹ + центрированный «Профиль» + wine «Сохранить»), avatar 96px с initials «КЛ» + camera-link «Изменить фото», 7 form-fields (Имя, Email readonly-tag, DOB chevron, Пол segment с wine «Мужской», Рост 178 см, Вес 76 кг, Цели chevron + preview), Bracelet card (VIGOR-XYZ123, success-green dot, заряд 87%), destructive «Удалить аккаунт» внизу, tab-bar «Ещё» active.
- **Phone 2 HRV detail:** Hero «52 ms» Onest 96pt + eyebrow «СЕГОДНЯ · 9:48» + delta strip («+8% к среднему» / «+12% к baseline»). 30-day SVG line chart с baseline 47ms dashed, area fill wine-soft, daily dots, today highlight (ring + filled + dark tooltip «52 ms»), range pills (7Д / 30Д wine active / Год), Y-axis 70/50/30, X-axis 5 dates. 3-metric strip (52/48/45 ms). Insight card с heart-pulse SVG и border-left wine. Tab «Дом» active.
- **Phone 3 HRV explainer modal:** Phone 2 dimmed (filter brightness 0.92 saturate 0.92) + dim-overlay rgba(12,10,9,0.45) + bottom-sheet (handle, close ×, eyebrow «КАК ЭТО РАБОТАЕТ», Onest title «Что такое HRV?», 2 параграфа с wine bold для HRV/baseline, 3 bullets ▲green/●wine/▼orange, disclaimer, wine CTA «Понятно»).

### Skills run
Skills из доступных явно не запускал — задача линейная (single-HTML + render). Использовал собственный rendering pipeline на базе lessons-learned (paired-bezel detection из B3 lessons + safe transparent CSS-inject из R2). Не использовал `init/document/craft/extract` (соблюдение правила).

### Decisions / compromises
- **DOB formatted («12 марта 1989»)** — humanizing, не mono-numeric. PM выбор из open-вопроса.
- **Range pills:** «7Д / 30Д / Год» (30Д default selected) — соответствие предпочтениям из брифа.
- **Insight copy:** «HRV выше нормы» + «Хорошо отдохнули — можно интенсивную тренировку или recovery-фокус» (более human-readable вариант из брифа, не «neuro-vegetative balance»).
- **Bracelet card на Profile** оставлен как preview — соответствует решению из open-вопроса.
- **Modal sheet** не fixed-height 70-75%, а grown-by-content (≈57% screen). Это даёт более компактный sheet с правильным reading rhythm, не пустое пространство. Если PM хочет fixed-75% — поменяем `max-height: 75%` + `padding-bottom` увеличим.
- **Dim overlay** покрывает body-scroll but не status/app-bar (R2 modal-stacking lesson: app-bar visible-but-dimmed). На Phone 3 это даёт визуальный context «вы в HRV экране, открыт modal», а не «full-screen takeover».
- **Today dot tooltip** — рисую как пиктограмма (dark rect + 52ms текст + pointer) внутри SVG, чтобы не выходить за viewBox. Проверено: рендерится корректно.

### Что требует ревизии PM
1. **Profile edit fold:** на 844px viewport «Удалить аккаунт» + Bracelet card требуют scroll. Если PM хочет всё одним кадром — сжать form padding (12→8px) или убрать «Цели» в Bracelet section.
2. **Insight card copy** — «recovery-фокус» содержит English-слово. Можно русифицировать в «лёгкая восстановительная тренировка» если PM требует full-Russian.
3. **Modal height 70-75% vs grown-by-content** — мой выбор content-grown даёт ~57%; если PM строго хочет 70-75%, поправим max-height fixed.
4. **Email readonly visual** — выбран pattern `kostya@neiry.com` + small READONLY mono-tag. Альтернатива — серый «not-allowed» cursor + lock-icon. PM подтверждает.
5. **Delta-strip иконки** — оба триangle вверх зелёные (positive). При negative delta переключатся на ▼ alert-orange — но текущий экран only positive states.

### Регрессии
Нет — новый файл, не трогал existing canonical. Tab-bar в обоих phones (1, 2) — byte-for-byte copy из Home f1 / Settings. Modal pattern — copy из onboarding-03 baseline-sheet.
