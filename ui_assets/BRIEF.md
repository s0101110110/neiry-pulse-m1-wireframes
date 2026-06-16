# BRIEF: C5 — Role onboarding user A (Делюсь / Со мной делятся) · Neiry Pulse Ф1

**Дата:** 2026-06-16
**Заказчик:** PM (Костя)
**Контекст:** C4 закоммичено (`82143ba`). Сейчас **C5** — финальная порция. Two-way Health Sharing role explainer: симметричная картина (Я делюсь данными vs Со мной делятся), которой не было в B7 (где user B видит только свою observer-роль).

**Цель:** закрыть Health Sharing role-asymmetry gap. User A (опекаемый = подопечный) **тоже** должен видеть свою роль чётко — кто видит его данные + что они видят. Это NOT B7 — там был только user B (observer onboarding). Здесь — два aspects одного user A: «делюсь» + «со мной делятся».

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-hs-role-user-a-v0.html`

---

## Источники правды

- **PRD v2.6 §8 AC-1.10:** «Health Sharing v1 — QR-pairing тренер/опекун, two-way visibility»
- **Аудит §2.2 finding 2 (продолжение):** «User B role onboarding закрыт B7. User A — sharer-перспектива — НЕ показана. Юзер не понимает что **его метрики видны** + симметрично может видеть metricsfriends.»
- **Reference (existing):**
  - `mobile-health-sharing-v0.html` — HS Main с loaded contacts
  - `mobile-state-hs-edge-cases-v0.html` Phone 2 — B7 user B role onboarding (parallel pattern)
  - `mobile-settings-detail-v0.html` Phone 3 (C2) — Privacy controls (доступ из profile)

---

## Структура HTML (2 device-frames рядом)

Caption:
- «**ЭКРАН 38** · HS ROLE · USER A SHARING»
- «**ЭКРАН 39** · HS ROLE · TWO-WAY DASHBOARD»

---

## Phone 1 · User A sharing role («Я делюсь»)

**Назначение:** опекаемый (Костя) впервые увидел, кто видит его данные. Settings → Privacy → tap «Кому я делюсь» → видит full screen с list + role explainer.

**Структура (сверху вниз):**

### Status bar + App-bar
- 9:55 / back-chevron «‹» + title «Кому я делюсь» (centered) + ⓘ info-icon (tap → explainer modal)

### Hero block (centered, top zone, без heavy hero)
- Eyebrow (mono uppercase wine 11pt): `ВЫ ПОДЕЛИЛИСЬ С 2 ЛЮДЬМИ`
- Title (Onest 700 22-24pt foreground): «Ваши близкие видят»
- Sub (Space Grotesk 14pt foreground, 2 строки):
  «Мама и Папа подключены как опекуны. Они получают алерты о падениях и видят дневные показатели.»

### Connected receivers list (2 cards)
**Card 1 — Мама:**
- Avatar circle 48px (initials «М» или photo)
- Right info: name «Мама» (semibold 16pt) + sub mono «подключено 12.05 · видит HRV, пульс, шаги, fall-alert» (12pt muted)
- Chevron `›` right
- Light Bevel surface, padding 14, border-radius 14

**Card 2 — Папа:**
- Avatar 48px (initials «П»)
- name «Папа» + sub mono «подключено 03.06 · видит ВСЁ»
- Chevron `›`
- Special wine accent border-left 3px (full-access marker)

### Default access section (под cards)
- Section title (mono uppercase 11pt muted): `ПО УМОЛЧАНИЮ ВИДНО`
- 4 строки с ✓ icons (wine):
  - ✓ Пульс и HRV
  - ✓ Шаги и активность
  - ✓ Алерт о падении (за 10 секунд)
  - ✓ Качество сна
- 1 строка с ⊘ icon (muted):
  - ⊘ Личные сообщения, местоположение

### Quick controls (bottom, 2 cards inline)
- **«Пауза доступа»** — wine outlined button (48pt, half-width) — temporary suspend all sharing
- **«Удалить всех»** — text-link destructive (half-width) — кnuclear option

### Tab-bar
Дом / История / Health Sharing (active wine) / Ещё — canonical

---

## Phone 2 · Two-way dashboard view (Я ↔ Со мной)

**Назначение:** symmetric HS dashboard — юзер видит **обе свои роли одновременно**: кому он делится (вверху) + кто делится с ним (внизу).

**Структура (сверху вниз):**

### Status bar + App-bar
- 9:55 / canonical Home app-bar (logo + bell + avatar КЛ)

### Title block
- Eyebrow (mono uppercase wine 11pt): `HEALTH SHARING`
- Title (Onest 700 22pt): «Ваша сеть здоровья»
- Sub (Space Grotesk 13pt muted): «2 + 1 = 3 человека связаны с вами»

### Section 1: Я делюсь с... (top half)
- Section header (mono uppercase 11pt wine): `Я ДЕЛЮСЬ С ↗`
- Sub-title (12pt muted): «Они видят мои показатели»
- 2 compact rows (avatar 36px + name + last-seen mono):
  - Avatar «М» + «Мама» + «активна 14:32»
  - Avatar «П» + «Папа» + «активен 15:18»
- Text-link «+ Добавить ещё» (wine, semibold 13pt, под list)

### Divider (subtle wine border)

### Section 2: Со мной делятся... (bottom half)
- Section header (mono uppercase 11pt wine): `СО МНОЙ ДЕЛЯТСЯ ↙`
- Sub-title (12pt muted): «Их показатели — для меня»
- 1 compact row:
  - Avatar «Б» + «Бабушка» + sub «вчера 22:15 · HRV ↓» (alert-orange small)
  - Chevron `›` (tap → opens HS Detail-view — мониторинг бабушки)
- Text-link «+ Принять приглашение» (wine 13pt, под list — если есть pending invite, иначе hidden)

### Quick action card (bottom)
- Light Bevel card + wine accent border-left 3px
- Icon: shield-check SVG (wine, 24×24)
- Title (semibold 14pt): «Вы под защитой»
- Sub (13pt muted):
  «Если упадёте — Мама и Папа получат алерт за 10 секунд. Если упадёт Бабушка — вы тоже узнаете.»

### Tab-bar
HS active wine (canonical)

---

## Дизайн-принципы

- **Light Bevel-tone** для обоих screens
- **Wine `#831843`** для primary CTA / accent / section headers
- **Wine outlined buttons** для secondary actions («Пауза доступа»)
- **Destructive red** для «Удалить всех»
- **Alert-orange** для warning indicators (бабушка HRV ↓)
- **Success-green** для positive states (active recently)
- **Box-sizing border-box** глобально
- **Tailwind CDN**
- **Header canonical:** Phone 1 — back-chevron + title-bar (nested); Phone 2 — Home canonical app-bar
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на цифрах (2, 1, 14:32, 15:18, 22:15)
- **SVG icons** (НЕ emoji): check, slash-circle, chevron-right, arrow-up-right (Я делюсь), arrow-down-left (Со мной делятся), shield-check, info-circle, plus

---

## Skills

UX/UI агент — запусти **`impeccable` critique** для two-way symmetry hierarchy (Section 1 vs Section 2 баланс) + **`emil-design-eng`** для arrow-direction visual cues (↗ vs ↙).

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 2-phone side-by-side render.

1. **HTML:** `mobile-hs-role-user-a-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs:**
   - `24a-hs-role-user-a-sharing.png`
   - `24b-hs-two-way-dashboard.png`

3. **Proof:**
   - `54-hs-role-user-a-sharing.png`
   - `55-hs-two-way-dashboard.png`
   - `56-hs-role-user-a-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 2 device-frames
- [ ] **Phone 1 «Я делюсь»:** back + «Кому я делюсь» + ⓘ + eyebrow «ВЫ ПОДЕЛИЛИСЬ С 2 ЛЮДЬМИ» + title «Ваши близкие видят» + sub + 2 receiver cards (Мама HRV/пульс/шаги/fall + Папа ВСЁ с wine border-left) + section «ПО УМОЛЧАНИЮ ВИДНО» (4 ✓ + 1 ⊘) + quick controls (Пауза доступа outlined + Удалить всех destructive text-link) + tab-bar HS active
- [ ] **Phone 2 Two-way dashboard:** Home canonical app-bar + eyebrow «HEALTH SHARING» + title «Ваша сеть здоровья» + sub «2 + 1 = 3 человека» + section «Я ДЕЛЮСЬ С ↗» (2 rows + Добавить ещё) + divider + section «СО МНОЙ ДЕЛЯТСЯ ↙» (1 row Бабушка с alert-orange HRV ↓) + quick action card «Вы под защитой» + tab-bar HS active
- [ ] Two-way symmetry visualHints (↗ vs ↙ arrows)
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA contrast
- [ ] Transparent PNG via crop из side-by-side
- [ ] Self-review визуальный

---

## Reference

- B7 user B onboarding (parallel): `mobile-state-hs-edge-cases-v0.html` Phone 2
- HS Main loaded: `mobile-health-sharing-v0.html`
- C2 Privacy controls (entry point): `mobile-settings-detail-v0.html` Phone 3
- A4 Fall detection в-app banner (cross-reference safety story): `mobile-onboarding-04-fall-detection-v0.html` Phone 2

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-16
**HTML:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-hs-role-user-a-v0.html` (1018 строк, 2 device-frames в одном файле)
**Transparent PNGs:**
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/24a-hs-role-user-a-sharing.png` (460×920, RGBA alpha=0 corners)
- `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/24b-hs-two-way-dashboard.png` (460×920, RGBA alpha=0)
**Proof-screenshots:**
- `UI_assets/screenshots/onboarding-2026-06-14/54-hs-role-user-a-sharing.png` (456×910)
- `UI_assets/screenshots/onboarding-2026-06-14/55-hs-two-way-dashboard.png` (456×910)
- `UI_assets/screenshots/onboarding-2026-06-14/56-hs-role-user-a-side-by-side.png` (902×910)

### Что сделано

Создан 2-phone HTML файл C5 — HS role user A sharing perspective + two-way dashboard.

**Phone 1 «Кому я делюсь»:** back+title+info app-bar, hero (eyebrow «ВЫ ПОДЕЛИЛИСЬ С 2 ЛЮДЬМИ» + title «Ваши близкие видят» + sub про Маму и Папу), 2 receiver-cards (Мама стандартная + Папа с full-access marker через full wine border + wine avatar + «ПОЛНЫЙ» wine pill — БЕЗ side-stripe), section «ПО УМОЛЧАНИЮ ВИДНО» (4 wine ✓ + 1 muted ⊘), quick-controls (Пауза доступа wine outline + Удалить всех destructive red text-link compact subordinate), tab-bar HS active.

**Phone 2 «Ваша сеть здоровья»:** Home canonical app-bar (Neiry Pulse logo + bell + КЛ), hero (eyebrow «HEALTH SHARING» + title + «2 + 1 = 3 человека связаны с вами»), Section 1 «Я ДЕЛЮСЬ С ↗» с wine pill arrow backplate + 2 person-rows (Мама/Папа с green status-dot + mono timestamp) + «+ Добавить ещё» link, clean divider, Section 2 «СО МНОЙ ДЕЛЯТСЯ ↙» с parallel wine pill backplate + 1 row (Бабушка с orange status-dot + alert-orange «вчера 22:15 · HRV ↓»), protect-card «Вы под защитой» (wine icon backplate + soft-wine bg + thin wine border, БЕЗ side-stripe), tab-bar HS active.

### Skills run

- **impeccable critique (self-applied):** обнаружил P0 violation — 2x side-stripe `border-left: 3px solid wine` (на Папа card и protect-card). Это absolute ban из reference. Заменил: на Папа — full wine border + wine avatar + «ПОЛНЫЙ» pill; на protect-card — wine icon backplate (32×32 wine bg) + soft-wine gradient + 1px wine-soft border. Identity сохранён без stripe-anti-pattern. Также: «Удалить всех» переделан в visually subordinate text-link (flex:0, auto width, underline-on-hover) — semantic clarity (primary action wins over nuclear).
- **emil-design-eng (self-applied):** для arrow direction symmetry — wine pill backplate 22×22 round под ↗ и ↙, parallel shape только rotation иконки. Receiver-card hover micro-interaction (chevron translateX +2px + bg lighten). Add-link gap-expand on hover (6→10px ease-out-quart, prefers-reduced-motion respected). Clean symmetric divider (убран асимметричный left-wine overlay).

### Decisions / compromises

1. **Side-stripe → full wine treatment.** Impeccable ban триггернулся 2 раза. Replaced both — без потери семантики «full access» и «вы защищены», даже улучшено: на Папа card теперь явный visual marker «ПОЛНЫЙ» pill вместо subtle stripe.
2. **Section 2 содержит только 1 row (Бабушка)** — мог бы добавить второй placeholder row, но это было бы fake-data. Symmetry достигнута через parallel structure (eyebrow + arrow backplate + sub-title + person-row), а не через row-count. Honest content > forced symmetry.
3. **«Полный» pill mono uppercase 9.5pt** — компактный wine badge справа от receiver-info, не конкурирует с chevron. Альтернатива (расширить sub «видит ВСЁ») приводила к 2-line wrap — pill чище.
4. **Quick-controls row distribution:** Пауза flex:1 + Удалить flex:0 auto. Это subverts симметричный grid но правильно семантически — destructive не должен быть равноправен с safe action.

### Что требует ревизии PM

- Текст «ПОЛНЫЙ» pill на Phone 1 — альтернативы: «ВСЁ», «MAX», «PRO». Выбрал «ПОЛНЫЙ» как русский + не маркетинговый.
- «+ Добавить ещё» в Section 1 (выше divider) — PRD ничего не говорит про invite-pending state в Section 2, поэтому secondary text-link там не добавлен. Если PM захочет — добавим «+ Принять приглашение» под Бабушкой conditional.
- HRV ↓ inline arrow в Бабушка row — мелкий 9×9px, читается как «снизился». Альтернатива: word «снизился» (длинно) или badge orange (визуально heavy). Сейчас compact mono row.

### Регрессии

Нет. Tab-bar canonical 1:1 с B7/HS Main. App-bar Phone 2 byte-for-byte скопирован с mobile-home-f1 (включая Tailwind-классы — Tailwind CDN в head). Шрифты Space Grotesk / Onest / Geist Mono — все 3 подключены. Tabular-nums на 12.05, 03.06, 14:32, 15:18, 22:15, 10, 2, 1, 3. SVG icons (НЕ emoji): back-chevron, info-circle, check, slash-circle, chevron-right, plus, arrow-up-right ↗, arrow-down-left ↙, shield-check, pause-bars, down-arrow для HRV. Padding-bottom 100px на обоих scroll-containers (lesson R2 tab-bar overlap).
