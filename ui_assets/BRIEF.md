# BRIEF: C2 — Settings detail screens (BT pairing + Notifications + Privacy) · Neiry Pulse Ф1

**Дата:** 2026-06-16
**Заказчик:** PM (Костя)
**Контекст:** C1 закрыт (Profile + HRV detail). PM выявил оставшиеся missing screens в Settings — детальные sub-экраны, недоступные из base Settings. Сейчас **порция C2 (1 из 4)** — 3 Settings detail-экрана.

**Цель:** закрыть Settings management gaps:
- **BT pairing edit** — управление подключёнными браслетами (replace/remove/add)
- **Notifications detail** — toggles per type (HRV insight / training / fall-alert / sleep / weekly summary)
- **Privacy controls** — data sharing visibility, export/delete account, HS audit log

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-settings-detail-v0.html`

---

## Источники правды

- **PRD v2.6 §8 AC-1.2:** «Settings: подключение/отключение браслета, управление уведомлениями, privacy»
- **Reference (existing):**
  - `mobile-settings-v0.html` — base Settings (entry-point)
  - `mobile-onboarding-02-bracelet-scan-pair-v0.html` — для BT pairing entry pattern
  - `mobile-onboarding-03-notifications-calibrating-v0.html` Phone 1 — Notifications permission

---

## Структура HTML (3 device-frames рядом)

Caption:
- «**ЭКРАН 31** · SETTINGS · BT PAIRING»
- «**ЭКРАН 32** · SETTINGS · NOTIFICATIONS»
- «**ЭКРАН 33** · SETTINGS · PRIVACY»

---

## Phone 1 · BT pairing edit

**Назначение:** управление подключёнными браслетами. Юзер: тап Settings → раздел «Браслет» → видит свои спаренные устройства с детальной информацией, может add/replace/remove.

**Структура:**

### Status bar + App-bar
- 9:55 / back-chevron «‹» + title «Браслет» (centered)

### Connected braclet section
- Section title (mono uppercase 11pt muted): `ПОДКЛЮЧЁН`
- **Big card** (light Bevel, padding 16-20, border-radius 16):
  - Top row: braclet icon SVG (48×48, wine bg-soft circle) + name «VIGOR-XYZ123» (Onest 700 18pt) + success-green dot + sub «подключён»
  - Stats grid 3-col (mono 11pt muted labels + 14pt values):
    - **ЗАРЯД** 87% (success-green if >50% / alert-orange if <30%)
    - **FIRMWARE** 2.1.4
    - **ПОСЛ. SYNC** 9:52
  - Action row (2 buttons inline):
    - **«Переподключить»** — wine small button
    - **«Отключить»** — text-link destructive

### Other devices section
- Section title: `ДРУГИЕ УСТРОЙСТВА`
- 2 list-rows (light Bevel cards, compact):
  - «VANTA-ABC456 · последний раз 12.05.2026» (muted-grey, не active)
  - chevron `›` правая (tap → connect)

### Add new section (CTA)
- Card-style row с **+ icon SVG**: «Добавить новый браслет» (semibold 15pt foreground) + chevron
- Wine accent on hover

### Tab-bar
Ещё active wine (canonical)

---

## Phone 2 · Notifications detail

**Назначение:** управление **per-type notifications**. Юзер видит все типы уведомлений, может toggle on/off каждый.

**Структура:**

### Status bar + App-bar
- 9:55 / back-chevron + title «Уведомления»

### Master toggle (top)
- Row (light Bevel, padding 16):
  - Bell-icon SVG + label «**Уведомления Neiry Pulse**» (Onest 700 16pt)
  - Right: large toggle (ON, wine bg)
- Sub-hint: «Получать любые уведомления» (12pt muted)

### Notifications grouping (под master)
Section title (mono uppercase 11pt muted): `ТИПЫ УВЕДОМЛЕНИЙ`

5 rows (каждая: icon-32 + label + sub + toggle):
1. **❤️ HRV-инсайт** — sub «Каждое утро в 9:00» — toggle ON
2. **🏃 Напоминания о тренировке** — sub «За 30 мин до запланированной» — toggle ON
3. **⚠️ Алерт о падении** — sub «Опекунам, при детекции» — toggle ON (нельзя выключить если есть HS)
4. **🌙 Анализ сна** — sub «По утрам после > 4 ч сна» — toggle ON
5. **📊 Еженедельная сводка** — sub «По понедельникам в 10:00» — toggle OFF

### Quiet hours section
Section title: `НЕ БЕСПОКОИТЬ`
- Row: «**Тихие часы**» + sub «22:00 — 07:00» + chevron `›` (tap → edit hours)
- Row: «**Выходные**» + sub «Только критичные (fall-alert)» + toggle ON

### Tab-bar Ещё active

---

## Phone 3 · Privacy controls

**Назначение:** управление приватностью данных. Health Sharing audit, data export, account delete.

**Структура:**

### Status bar + App-bar
- 9:55 / back-chevron + title «Приватность»

### Data sharing section
Section title: `КОМУ ВЫ ПОКАЗЫВАЕТЕ ДАННЫЕ`

- Row: avatar circle (Мама) + «Мама» + sub «HRV, шаги, fall-alert · с 12.05» + chevron `›` (tap → edit access)
- Row: avatar (Папа) + «Папа» + sub «Все метрики · с 03.06» + chevron
- Bottom: **Wine text-link** «+ Подключить нового» (16pt, semibold)

### Privacy details section
Section title: `ВАШИ ДАННЫЕ`

3 rows (icon-24 + label + sub muted + chevron):
- **📥 Скачать данные** — sub «JSON со всеми метриками за всё время»
- **📤 Удалить данные** — sub «Очистить всю историю, оставить аккаунт»
- **🚪 Удалить аккаунт** — destructive red, sub «Безвозвратно, всё стирается»

### Legal section (bottom)
Section title: `ЮРИДИЧЕСКОЕ`

- Row: «**Политика конфиденциальности**» + chevron
- Row: «**Условия использования**» + chevron
- Row: «**Согласие на обработку**» + sub «Версия 2.6 · принято 14.06.2026» + chevron

### Tab-bar Ещё active

---

## Дизайн-принципы

- **Light Bevel-tone** для всех 3 screens
- **Wine `#831843`** для primary actions, accent, master toggle ON
- **Destructive red `#b91c1c`** для «Удалить аккаунт» / «Удалить данные»
- **Success-green `#65a30d`** для active dot, success battery indicator
- **Alert-orange `#d97706`** для low battery (<30%) warning
- **Toggle UI:** rounded-pill style (iOS native), 51×31 size, white knob, wine bg for ON, muted-grey для OFF
- **Box-sizing border-box** глобально (`*, *::before, *::after`)
- **Tailwind CDN**
- **Header canonical** — back-chevron + title-bar pattern (nested screens)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (87, 9:52, 22:00, 12.05)
- **SVG icons** (НЕ emoji): bracelet, bell, heart, running, fall-alert-triangle, moon, chart, download, trash, door, document, chevron, plus

---

## Skills

UX/UI агент — выбирай сам. Особое внимание к toggle accessibility (aria-checked) + section hierarchy не overcrowded.

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 3-phone side-by-side render.

1. **HTML:** `mobile-settings-detail-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `21a-settings-bt-pairing.png`
   - `21b-settings-notifications.png`
   - `21c-settings-privacy.png`

3. **Proof в `screenshots/onboarding-2026-06-14/`:**
   - `44-settings-bt-pairing.png`
   - `45-settings-notifications.png`
   - `46-settings-privacy.png`
   - `47-settings-detail-side-by-side.png` (3-phone wide)

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 3 device-frames
- [ ] **Phone 1 BT pairing:** title «Браслет» + Connected card (VIGOR-XYZ123 + 3-col stats + actions) + Other devices (2 inactive cards) + «Добавить новый браслет» CTA + tab-bar
- [ ] **Phone 2 Notifications:** title «Уведомления» + Master toggle + 5 per-type rows с toggles + Quiet hours section (Тихие часы + Выходные) + tab-bar
- [ ] **Phone 3 Privacy:** title «Приватность» + Data sharing rows (Мама + Папа + Подключить нового) + Privacy details (Скачать / Удалить данные / Удалить аккаунт destructive) + Legal section + tab-bar
- [ ] Toggle UI iOS-style (51×31, wine ON)
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA contrast
- [ ] Transparent PNG via crop из 3-phone side-by-side
- [ ] Self-review визуальный ПЕРЕД отчётом — открой все 3 proof PNG, **проверь что не обрезано** (compress если нужно как в C1 fix)

---

## Open вопросы

1. **Master toggle для всех уведомлений** — должен ли disable fall-alert? Я бы оставил **отдельный override** для fall-alert (safety-критично) — даже при master OFF, fall-alert остаётся. Можно с дисклеймером.
2. **Quiet hours для fall-alert** — игнорируем? Да — fall-alert всегда проходит независимо от quiet hours (safety override).
3. **Battery low warning на BT pairing screen** — добавить alert-orange visualHints если заряд <30%? Я бы добавил (consistency с B1 Charging-low banner).
4. **Privacy: «Удалить данные» vs «Удалить аккаунт»** — разница может быть неочевидной. Я выбрал sub-text explainer для каждой. PM может уточнить или схлопнуть в один пункт.

---

## Reference

- Settings base: `mobile-settings-v0.html`
- HS connections (для Privacy data sharing): `mobile-health-sharing-v0.html`
- A3 Notifications permission pattern: `mobile-onboarding-03-notifications-calibrating-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:**
**HTML:**
**Transparent PNGs:**
**Proof-screenshots:**

### Что сделано

### Skills run

### Decisions / compromises

### Что требует ревизии PM

### Регрессии
