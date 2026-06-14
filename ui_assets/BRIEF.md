# BRIEF: Corner cases B1 — BT-disconnect + Charging-low banners · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** Онбординг A1-A5 закрыт и закоммичен (`59d4718`). Сейчас **порция B1 (1 из 5-7) Ф1.5 corner cases:** **BT-disconnect banner** (браслет отключился) + **Charging-low banner** (заряд браслета ≤15%). Оба — глобальные banner-паттерны поверх Home, переиспользуются на других экранах.

**Цель:** закрыть **C-16 (BT disabled / disconnect)** и **battery-low warnings** из аудита 14.06 §3 — оба MUST Ф1. Без них в пилотах 22.06 пользователь не понимает почему виджеты «замерли» / куда делись данные.

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-bt-disconnect-charging-low-v0.html`

---

## Источники правды

- **Аудит §3 C-16:** «Bluetooth disabled на телефоне — Home / Onboarding / Settings — MUST Ф1»
- **Аудит §2.5 finding 4:** «Все banner-states (sync-failed, BT-disconnect, charging-low) отсутствуют — без них юзер видит «замершие» данные и не понимает что происходит»
- **PRD v2.6 §8 AC-1.2:** «Home показывает baseline status (готов / собираем / не готов) на первом экране»
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)
- **Light Bevel-tone palette** + wine #831843 brand
- **Alert hierarchy** (из A4 Fall detection): destructive red `#b91c1c` для critical, alert-orange `#d97706` для warning, wine `#831843` для primary action

---

## Структура HTML (2 device-frames рядом)

Caption:
- Слева: «**ЭКРАН 12** · HOME · BT-DISCONNECT BANNER»
- Справа: «**ЭКРАН 13** · HOME · CHARGING-LOW BANNER»

---

## Phone 1 · Home с BT-disconnect banner (браслет отключился)

**Назначение:** пользователь открывает Home, видит что **браслет отключён** (Bluetooth disabled или out of range, или браслет разряжен и выключился). Виджеты «замирают» на последних данных. Поверх Home — **sticky-top banner** alert-orange с CTA «Переподключить».

**Контекст:** light Bevel-tone Home. Берём layout как в `mobile-home-f1-v0.html`, но:
- Виджеты показывают **last-known values** с timestamp («последние данные: 2 мин назад»)
- Над виджетами — **sticky alert-banner**
- Tab-bar не меняется (Дом active)

**Структура (сверху вниз):**

### Status bar + App-bar
Тот же что в Home f1 (canonical header).

### Sticky alert-banner (сверху, под app-bar, full-width)
- Background: `#fdf3e1` (alert-soft warm)
- Border-left: 4px `#d97706` (alert-orange)
- Padding 12-16px
- Top row:
  - **Alert-icon SVG** (warning triangle, alert-orange `#d97706`)
  - Eyebrow (mono uppercase 11pt alert-orange): `БРАСЛЕТ ОТКЛЮЧЁН`
  - Right: timestamp `2 мин назад` (mono 11pt muted)
- Title (Onest 700, 16-18pt foreground): «Не вижу ваш браслет»
- Sub (Space Grotesk 13pt foreground, 2 строки max):
  «Возможно, вышли из зоны Bluetooth или браслет разрядился. Данные временно не обновляются.»
- Actions row (2 buttons inline):
  - **«Переподключить»** — primary wine button (small, ~36pt high, padding 12 16)
  - **«Что делать?»** — text-link wine secondary

### Stale data row (после banner — намёк что данные старые)
- Subtle horizontal text-strip: `ПОСЛЕДНИЕ ДАННЫЕ · 9:48 (2 МИН НАЗАД)` (mono uppercase 10pt muted-foreground)
- Над stats — небольшой пояснительный текст

### Stats widgets (3 stacked, как в Home f1 / A5 empty stacked-cards)
- **HRV widget:** Value `58 ms` (tabular-nums, **muted** color — «замороженное» значение) + sub «последний замер 9:48»
- **Шаги widget:** Value `3 420` (mono tabular-nums, foreground) + sub `3 420 / 6 000` + mini-bar 57% wine
- **Сон widget:** Value `6 ч 42 мин` + sub «прошлой ночью»
- На HRV — subtle visual indicator что данные «заморожены» (например, тонкий border alert-orange или иконка часов справа)

### Тренировки / Health Sharing sections
Скрыть/упростить — это не главное на этом экране (focus = banner).

### Tab-bar
Дом active wine / История / Health Sharing / Ещё (canonical)

---

## Phone 2 · Home с Charging-low banner (заряд браслета ≤15%)

**Назначение:** браслет подключён и работает, но заряд **≤15%** — скоро разрядится. Показать **soft warning banner** с CTA «Как зарядить?» / «Напомнить позже». Виджеты НЕ замирают (данные актуальны).

**Контекст:** light Bevel-tone Home, всё работает, но warning сверху.

**Структура (сверху вниз):**

### Status bar + App-bar
Canonical header.

### Sticky charging-low banner
- Background: `#fdf3e1` (alert-soft warm, тот же что BT-disconnect для consistency)
- Border-left: 4px `#d97706` (alert-orange)
- Padding 12-16px
- Top row:
  - **Battery-low icon SVG** (battery с маленькой полоской, alert-orange)
  - Eyebrow (mono uppercase 11pt alert-orange): `ЗАРЯД БРАСЛЕТА · 12%`
  - Right: visual mini-battery indicator (SVG, ~24×12px, 12% fill alert-orange)
- Title (Onest 700, 16-18pt foreground): «Браслет скоро разрядится»
- Sub (Space Grotesk 13pt foreground, 2 строки):
  «Заряда хватит примерно на 4 часа. Поставьте на зарядку, чтобы не пропустить ночное измерение HRV.»
- Actions row (2 buttons inline):
  - **«Как зарядить?»** — primary wine button (small)
  - **«Напомнить через 1 ч»** — text-link wine secondary

### Stats widgets (3 stacked, **полностью работают**, не заморожены)
- **HRV widget:** Value `52 ms` (tabular-nums, foreground) + sub «обновлено сейчас» + heartbeat-volna icon
- **Шаги widget:** Value `4 856` / `6 000` + mini-bar 81%
- **Сон widget:** `6 ч 42 мин` + sub «прошлой ночью»

### Тренировки / Health Sharing sections
Полноценные (как в Home f1), но visualHints не критичны.

### Tab-bar
Canonical (Дом active).

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих экранов
- **Alert-orange `#d97706`** для warning banner accents (НЕ destructive red — это warning, не critical)
- **Alert-soft `#fdf3e1`** для banner bg (warm tint, не яркий)
- **Wine #831843** для primary action buttons («Переподключить», «Как зарядить?»)
- **Stale data state на Phone 1**: HRV value muted color, subtle alert-orange border-left или icon-часов на widget — visual cue что данные «заморожены»
- **Charging-low на Phone 2**: данные актуальные, но banner предупреждает
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (58 ms, 3 420, 12%, 4 ч)
- **SVG icons** (НЕ emoji) — warning triangle, battery, clock
- **Header** — обязательно canonical из Home f1 (logo центрован, icon-buttons clean) — **НЕ повторяй баг A5 revision 1**
- **Tab-bar** — canonical (Дом / История / Health Sharing / Ещё)
- **Box-sizing: border-box** обязательно глобально (`*, *::before, *::after { box-sizing: border-box; }`) — урок из A5 revision 2

---

## Skills из PLAYBOOK

1. Draft v0
2. `impeccable critique` — anti-slop (не overdramatize warning, не двойные icons, banner должен быть scannable за 1 секунду)
3. `impeccable polish` → v1
4. `impeccable audit` — WCAG AA контраст (alert-orange на alert-soft bg ≥ 4.5:1!), aria-live="polite" на banner для screen readers
5. **emil-design-eng** опционально — subtle slide-down entrance для banner (240ms ease-out), pulse-glow на battery icon Phone 2

**НЕ запускать:** `/impeccable init/document/craft/extract`

---

## Output (transparent PNG)

**НЕ используй slicing-script** для proof PNG — урок из A5 revision 2. **Crop из side-by-side render** правильный подход:

```python
chrome --headless --window-size=1280,1100 --screenshot=sxs.png file://...
# Crop phones:
from PIL import Image
img = Image.open("sxs.png")
phone1 = img.crop((200, 70, 660, 970))
phone2 = img.crop((620, 70, 1080, 970))
```

Для transparent PNG — минимальный inject (только transparent bg, не layout-rewrite):
```python
INJECT = """<style>html, body { background: transparent !important; }
.doc-title, .page-title, .page-sub, body > h1, body > h2, body > p, body > header { display: none !important; }</style></head>"""
```

1. **HTML:** `mobile-state-bt-disconnect-charging-low-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `13a-state-bt-disconnect.png`
   - `13b-state-charging-low.png`
   - **Verify alpha=0 углы**

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/` (или создать новую папку `corner-cases-2026-06-14/`):
   - `17-bt-disconnect.png`
   - `18-charging-low.png`
   - `19-bt-disconnect-charging-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан
- [ ] 2 device-frames рядом (frames-row)
- [ ] **Phone 1 BT-disconnect:** sticky alert-banner alert-orange сверху + stale data hint + замороженные HRV в muted цвете + actions «Переподключить» (wine) / «Что делать?»
- [ ] **Phone 2 Charging-low:** sticky alert-banner alert-orange сверху + мини-battery visual + actions «Как зарядить?» (wine) / «Напомнить через 1 ч»
- [ ] Header canonical (logo центрован, icon-buttons clean) — НЕ повторить баг A5
- [ ] Box-sizing border-box глобально — НЕ повторить баг A5 revision 1
- [ ] tabular-nums на всех цифрах
- [ ] SVG icons (warning triangle, battery, clock — НЕ emoji)
- [ ] WCAG AA: alert-orange text на alert-soft bg ≥ 4.5:1
- [ ] **Transparent PNG crop из side-by-side** (НЕ slicing-script)
- [ ] Proof side-by-side рендер
- [ ] Skills прогнаны (critique + polish + audit, emil опц.)
- [ ] Self-review визуальный — открыть PNG, описать что видишь, перед отчётом

---

## Open вопросы

1. **«Замороженные» HRV на Phone 1** — насколько визуально подчеркнуть что данные старые? Я бы добавил тонкий left-border alert-orange на HRV-card + iconchasov справа, и value в muted-цвете. Альтернативу — overlay-mask с opacity 0.6.

2. **Battery indicator на Phone 2** — выбрать % значение: 15%, 12%, 10%? Я взял **12%** — визуально достаточно тревожно (под 15% threshold для warning, но ещё не critical 5%).

3. **Charging-low CTA «Как зарядить?»** — ведёт куда? Я бы оставил wireframe placeholder — в final UI это modal/sheet с гайдом по зарядке. Но на mockup просто button styled.

4. **«Напомнить через 1 ч»** vs «Скрыть» как secondary — я взял «Напомнить» (snooze pattern, не dismiss). Опытнее UX, чем permanent dismiss.

5. **BT-disconnect timestamp «2 мин назад»** — реалистично, но если PM хочет более dramatic — «12 мин назад» (HRV «совсем замёрз»). Я бы взял 2 мин (свежее, действие имеет смысл).

---

## Reference

- Home loaded layout (для baseline + canonical header / tab-bar): `mobile-home-f1-v0.html`
- Empty Home (для stacked-cards pattern): `mobile-onboarding-05-empty-states-v0.html`
- Alert-banner pattern (alert-soft + border-left): `mobile-onboarding-04-fall-detection-v0.html` Phone 2 (in-app banner)
- Память: `feedback_neiry_mockup_format`, lessons-learned уроки A5 (slicing-script deprecated, box-sizing border-box, header source of truth)

---

## РЕЗУЛЬТАТ (заполняет UI агент)

**Дата:** 2026-06-15
**HTML:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-bt-disconnect-charging-low-v0.html`
**Transparent PNGs:**
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/13a-state-bt-disconnect.png` (920×1840, alpha=0)
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/13b-state-charging-low.png` (920×1840, alpha=0)

**Proof-screenshots:**
- `UI_assets/screenshots/onboarding-2026-06-14/17-bt-disconnect.png` (840×1748)
- `UI_assets/screenshots/onboarding-2026-06-14/18-charging-low.png` (840×1748)
- `UI_assets/screenshots/onboarding-2026-06-14/19-bt-disconnect-charging-side-by-side.png` (2560×2200)

### Что сделано

- 2 device-frames в одном HTML — каноничный Home layout f1 (header byte-for-byte: logo+КЛ-avatar, bell, tab-bar Дом/История/HS/Ещё).
- **Phone 1 BT-disconnect:** alert-banner alert-orange (warm bg #fdf3e1 + border-left 4px #d97706) с warning-triangle SVG, eyebrow «БРАСЛЕТ ОТКЛЮЧЁН», timestamp «2 мин назад», title «Не вижу ваш браслет» (Onest 700), CTA «Переподключить» (wine) + «Что делать?» (text-link). Stale-data strip с orange dot. HRV (58 ms) и Шаги (3 420) — muted value + grey progress + clock-marker top-right. Sleep — actual (вчерашняя ночь не зависит от текущего соединения).
- **Phone 2 Charging-low:** alert-banner с battery-icon SVG + pulse-glow animation, eyebrow «ЗАРЯД БРАСЛЕТА · 12%», справа mini-battery 12% fill, title «Браслет скоро разрядится», CTA «Как зарядить?» (wine) + «Напомнить через 1 ч» (snooze). Виджеты живые (52 ms / 4 856 / 6 ч 42 м, wine progress 81%).
- Box-sizing border-box глобально (`*, *::before, *::after`). Tailwind CDN подключён (header полагается на Tailwind utility-классы).
- tabular-nums на всех цифрах. Geist Mono на labels/metrics, Onest 700 на title, Space Grotesk UI.
- `aria-live="polite"`, `role="alert"`, `aria-labelledby` на banners. WCAG: alert-orange-strong `#b45309` на soft bg `#fdf3e1` ≥ 4.5:1 (используем strong tint для eyebrow/timestamp).
- Slide-down 240ms ease-out на banner entrance + battery icon pulse-glow 1.8s; обёрнуто в `prefers-reduced-motion: reduce`.

### Skills run

- В сессии прогнал inline critique + polish (anti-slop + 4px grid + tabular-nums + SVG-only) и audit на head (WCAG strong-tint + aria-live + role=alert + reduced-motion). Дополнительный pulse-glow на battery (emil-style) уже встроен в первый pass.
- НЕ запускал init/document/craft/extract по правилу брифа.

### Decisions / compromises

1. **Шаги тоже muted на Phone 1** — шагомер live-данные с браслета, значит при disconnect шаги тоже «замёрзшие». Только Sleep (вчерашняя ночь) остаётся foreground — это уже синхронизированная история.
2. **Stale-marker только на HRV-card** (top-right clock 16px) — на Шагах достаточно muted value + grey bar; два clock-маркера = visual clutter.
3. **Banner CTA «text-wine»** (НЕ btn-outline) — secondary action легче, не конкурирует с primary. Соответствует pattern из A4 Fall detection.
4. **Phone 2 banner — НЕ destructive pulse-ring** (как A4 fall), а более мягкий battery-pulse — warning, не critical. Только battery icon glow, не вся banner.
5. **Time on Phone 1 = 9:50** (banner says «2 мин назад», disconnect @ 9:48) — chronology constraint выполнен (lesson 2026-06-14 хронология).
6. **На Phone 1 HRV value не «—», а 58 ms muted** — мы видим last-known данные, это не отсутствие. Em-dash был бы про calibrating empty (другой кейс).

### Что требует ревизии PM

- Текст secondary action «Напомнить через 1 ч» — мог бы быть короче («Через 1 ч»). Сохранил длинный для ясности — на узком banner упирается в правый край, но визуально читается. Если будет лучше — сократить.
- Sleep-card на BT-disconnect остаётся не-muted (логично) — но визуально создаёт контраст с двумя muted-cards выше. Если PM хочет — можно слегка обозначить muted-выше / live-ниже разделителем (но это уже gilding).

### Регрессии

Нет. Header / tab-bar / spacing полностью копируют canonical Home f1, никакие другие файлы не затронуты.
