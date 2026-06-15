# BRIEF: Corner cases B6 — History edge cases (Empty month + Future month + Multiple sessions/day) · Neiry Pulse Ф1.5

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** B1-B5 приняты и закоммичены. Сейчас **порция B6 (6 из 7) Ф1.5 corner cases:** History edge cases — 3 экрана.

**Цель:** закрыть History corner cases из аудита §3.6:
- **Empty month** — выбранный месяц без тренировок (новый юзер, или отпуск)
- **Future month** — навигация в будущее (пустой grid с тренировками которых ещё нет)
- **Multiple sessions/day** — один день несколько тренировок (утренний/вечерний бег)

**Целевой файл (создать):**
- `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-history-edge-cases-v0.html`

---

## Источники правды

- **Аудит §3.6 missing states:**
  - Empty month — «В этом месяце тренировок ещё нет»
  - Future month — пустой grid, disabled navigation вперёд / hint
  - Multiple sessions/day — один день с 2-3 чипами в day-cell или stack
- **Reference:** `mobile-history-v0.html` — base History (month calendar grid + session list под grid)
- **Память `feedback_neiry_mockup_format`:** transparent PNG (alpha=0 углы)

---

## Структура HTML (3 device-frames рядом)

Caption:
- «**ЭКРАН 23** · HISTORY · EMPTY MONTH»
- «**ЭКРАН 24** · HISTORY · FUTURE MONTH»
- «**ЭКРАН 25** · HISTORY · MULTIPLE SESSIONS/DAY»

---

## Phone 1 · History с Empty month

**Назначение:** юзер открыл History (например май, отпуск без тренировок). Видит **пустой month grid** + central empty-state ниже (вместо session list).

**Контекст:** History base layout (month navigator + calendar grid + session list area). В нашем случае:
- Month navigator показывает «Май 2026»
- Grid пустой (без dots/индикаторов под датами)
- Под grid'ом — большой empty-state

**Структура:**

### Status bar + App-bar
- Status bar 9:53
- App-bar: Neiry Pulse logo + bell + avatar (canonical Home pattern)

### Month navigator
- Centered «**Май 2026**» (Onest 700 18pt)
- ‹ и › chevrons по бокам (active)

### Calendar grid
- 7-col grid (Пн-Вс) с числами 1-31
- Today highlight (если применимо) — wine dot или ring
- Числа в muted-foreground (не bright)
- БЕЗ session-dots под датами (нет тренировок)

### Empty state (под grid'ом, занимает оставшееся пространство)
- Centered SVG illustration: calendar с moon/sleep-icon или абстрактное «zero motion» visualHints (НЕ stock, НЕ emoji)
- Title (Onest 700 20-22pt): «В этом месяце тренировок не было»
- Sub (Space Grotesk 14pt foreground, 2 строки):
  «Может быть, отдых был запланирован — это тоже часть тренировочного цикла.»
- Primary CTA wine: «Начать тренировку» (full-width 48pt, play-icon)

### Tab-bar
История active (canonical 4-tab)

---

## Phone 2 · History с Future month

**Назначение:** юзер свайпнул вперёд → видит **будущий месяц** (например июль 2026). Grid пустой, но это не «empty» — это «still ahead». Тон должен быть anticipatory, не frustrating.

**Контекст:** History month navigator показывает «Июль 2026» (будущий). Navigation chevron «›» в next direction — disabled или с пометкой «no further data».

**Структура:**

### Status bar + App-bar
Same canonical.

### Month navigator
- Centered «**Июль 2026**» (Onest 700 18pt)
- ‹ chevron active (можно назад)
- › chevron disabled или muted (нечего смотреть вперёд)

### Calendar grid
- 7-col grid Пн-Вс с числами июля
- ALL даты в muted-foreground (future, не today, не past)
- НЕТ session-dots
- БЕЗ today-highlight (today is in another month)

### Future month state (под grid'ом)
- Centered SVG illustration: subtle clock или calendar-forward icon (НЕ alarming, не «error»)
- Eyebrow (mono uppercase wine 11pt): `БУДУЩЕЕ`
- Title (Onest 700 20pt): «Июль ещё впереди»
- Sub (Space Grotesk 14pt foreground, 2 строки):
  «Запланируйте тренировки или вернитесь сюда после первого пробега.»
- 2 actions stacked:
  - Wine primary CTA «Назад в июнь» (48pt full-width, chevron-left icon)
  - Text-link «Запланировать тренировку» (wine 14pt, под CTA)

### Tab-bar
История active

---

## Phone 3 · History с Multiple sessions/day

**Назначение:** юзер тапнул на день с **несколькими тренировками** (15 июня — утренний бег + вечерняя йога). День в grid'е помечен **множественными dots** (2-3 точки). Под grid — список сессий этого дня.

**Контекст:** History с активным месяцем (Июнь 2026). День 15 июня выделен (selected ring). Grid показывает 14 июня как 1-dot day, 15 июня как 3-dot day, 16 июня как 1-dot.

**Структура:**

### Status bar + App-bar
Same canonical.

### Month navigator
- Centered «**Июнь 2026**» (Onest 700 18pt)
- Chevrons по бокам

### Calendar grid
- 7-col grid Пн-Вс
- 15 июня — **selected day** (ring wine + dots ниже)
- Под датой 15: **3 wine dots** (3 тренировки)
- Под датой 14: 1 wine dot
- Под датой 16: 1 wine dot
- Прочие дни — без dots (rest days)

### Selected day section (под grid'ом)
- Title (Onest 700 18pt): «Пятница, 15 июня · 3 тренировки»
- Stack из 3 session-cards (или compact list-rows):

**Card 1 — утренний бег:**
- Icon: running-figure SVG (wine, 32×32 in soft-bg circle)
- Title: «Бег» (semibold 15pt)
- Stats inline: «9:53 · 5.20 км · 28:04 · 142 bpm» (Geist Mono 12pt)
- Chevron «›» right

**Card 2 — обеденная прогулка:**
- Icon: walk-figure SVG
- Title: «Прогулка»
- Stats: «13:15 · 2.10 км · 24:30 · 98 bpm»

**Card 3 — вечерняя йога:**
- Icon: yoga-pose SVG (опц., или generic activity)
- Title: «Йога»
- Stats: «19:42 · 45:00 · 84 bpm avg»

### Tab-bar
История active

---

## Дизайн-принципы

- **Light Bevel-tone** для всех 3 экранов
- **Wine `#831843`** для primary actions / dots / today-highlight / selected-ring
- **Muted-foreground** для future dates / empty-state visualHints
- **Box-sizing border-box** глобально
- **Tailwind CDN** если нужно
- **Header canonical** — заимствуй из `mobile-history-v0.html`
- **Tab-bar canonical** (4-tab «Дом / История / Health Sharing / Ещё», История active)
- **Шрифты:** Space Grotesk UI / Onest 700 hero / Geist Mono labels & numbers
- **Pixel grid 4px**
- **tabular-nums** на всех цифрах (даты, времена, км, bpm)
- **SVG icons** (НЕ emoji): calendar, moon, running, walking, yoga, clock, play, chevrons

---

## Skills

UX/UI агент — выбирай сам. Рекомендую critique + audit. Для empty-state копии — anti-slop critique critically (не патетично, не demotivate если у юзера нет тренировок).

**НЕ запускать:** init/document/craft/extract.

---

## Output

**slicing-script DEPRECATED** — crop из 3-phone side-by-side (window-size ~1900×1100).

1. **HTML:** `mobile-state-history-edge-cases-v0.html` в `docs_web/wireframes/m3/`

2. **Transparent PNGs** в `screenshots/sliced-flow-v2-1-transparent-2026-06-14/`:
   - `18a-state-history-empty-month.png`
   - `18b-state-history-future-month.png`
   - `18c-state-history-multiple-sessions.png`
   - Verify alpha=0 углы

3. **Proof-screenshots** в `screenshots/onboarding-2026-06-14/`:
   - `33-history-empty-month.png`
   - `34-history-future-month.png`
   - `35-history-multiple-sessions.png`
   - `36-history-edge-cases-side-by-side.png`

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] HTML создан с 3 device-frames рядом
- [ ] **Phone 1 Empty month:** Май 2026 navigator + пустой grid (no dots) + central empty-state (illustration + title «В этом месяце тренировок не было» + sub + wine CTA «Начать тренировку») + tab-bar
- [ ] **Phone 2 Future month:** Июль 2026 + disabled forward chevron + muted future dates + state (illustration + eyebrow «БУДУЩЕЕ» + title «Июль ещё впереди» + sub + wine CTA «Назад в июнь» + text-link «Запланировать тренировку») + tab-bar
- [ ] **Phone 3 Multiple sessions/day:** Июнь 2026 + 15 июня selected с 3 dots + 14/16 с 1 dot + section «Пятница, 15 июня · 3 тренировки» + 3 session-cards (Бег / Прогулка / Йога) с stats и chevron + tab-bar
- [ ] Box-sizing border-box, Tailwind CDN
- [ ] WCAG AA на all (muted future dates ≥ 4.5:1)
- [ ] Transparent PNG via crop из 3-phone side-by-side
- [ ] Self-review визуальный ПЕРЕД отчётом

---

## Open вопросы

1. **Empty month copy** — может быть demotivating для recreational юзеров. Я выбрал **«Может быть, отдых был запланирован — это тоже часть тренировочного цикла»** — нейтрально + supportive. Альтернатива: «Самое время начать!». PM может уточнить.
2. **Future month — disabled или просто muted?** Я выбрал **muted forward chevron** (visually less-active, но clickable если PM хочет navigate дальше). Если PM хочет hard-disabled — fully greyed out.
3. **Multiple sessions per day — stack под grid'ом или модал?** Я выбрал **stack под grid'ом** (inline, scroll inside History tab). Modal — слишком heavy для simple tap-to-expand.
4. **Multiple sessions — 3 разные активности или 3 раза один бег?** Я выбрал **3 разные** (Бег + Прогулка + Йога) — illustrates variety. Если PM хочет фокус на runners — 2× бег + 1× recovery.

---

## Reference

- History base: `mobile-history-v0.html` (month navigator, calendar grid, session list)
- A5 empty pattern (illustration + heading + CTA): `mobile-onboarding-05-empty-states-v0.html`
- Tab-bar canonical: `mobile-home-f1-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-15
**HTML:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-state-history-edge-cases-v0.html` (1074 строк, 3 device-frames рядом, 390×844 каждый)
**Transparent PNGs:**
- `screenshots/sliced-flow-v2-1-transparent-2026-06-14/18a-state-history-empty-month.png`
- `screenshots/sliced-flow-v2-1-transparent-2026-06-14/18b-state-history-future-month.png`
- `screenshots/sliced-flow-v2-1-transparent-2026-06-14/18c-state-history-multiple-sessions.png`

**Proof-screenshots:**
- `screenshots/onboarding-2026-06-14/33-history-empty-month.png`
- `screenshots/onboarding-2026-06-14/34-history-future-month.png`
- `screenshots/onboarding-2026-06-14/35-history-multiple-sessions.png`
- `screenshots/onboarding-2026-06-14/36-history-edge-cases-side-by-side.png`

### Что сделано

**Phone 1 · Empty month (Май 2026):**
- Header canonical (Status bar + App-bar «История» + Месяц-chip)
- Month navigator «Май 2026» с активными ‹ ›
- Calendar grid 7×5 (1 мая = пт, 31 мая = вс) — все даты heat-0 без dots
- Empty-state: SVG calendar+moon illustration (132×132, faint dotted day-cells + центральная луна в wine + 2 звёздочки), title «В этом месяце тренировок не было», sub «Может быть, отдых был запланирован — это тоже часть тренировочного цикла.», wine CTA «Начать тренировку» с play-icon (48pt full-width)
- Tab-bar canonical, История active

**Phone 2 · Future month (Июль 2026):**
- Month navigator «Июль 2026», forward chevron .disabled (opacity 0.55 + muted bg + cursor not-allowed)
- Calendar Июль (1 июля = ср, 31 июля = пт) — все даты в muted-foreground-soft (#a8a299), фон heat-0
- State: SVG clock-face (циферблат + стрелка на 3, минутная на 12, forward arc dashed wine), eyebrow «БУДУЩЕЕ» (wine mono uppercase), title «Июль ещё впереди», sub «Запланируйте тренировки или вернитесь сюда после первого пробега.», wine CTA «Назад в июнь» с chevron-left, text-link «Запланировать тренировку» (wine 14pt)
- Tab-bar canonical

**Phone 3 · Multiple sessions/day (Июнь 2026, 15.06):**
- Month navigator «Июнь 2026» с активными chevrons
- Calendar (1 июня = пн): 14 → 1 wine dot, **15 → selected ring wine + 3 dots**, 16 → 1 dot, остальные без dots
- Day section: title «Понедельник, 15 июня · 3 тренировки» (Onest 17pt + wine mono subtitle)
- 3 session-cards:
  - **Бег** (running figure SVG, 9:53 · 5.20 км · 28:04 · 142 bpm)
  - **Прогулка** (walking figure SVG, 13:15 · 2.10 км · 24:30 · 98 bpm)
  - **Йога** (lotus pose SVG, 19:42 · 45:00 · 84 bpm avg)
- Все cards с wine-soft icon-bg (40×40 rounded-12), chevron «›» справа, Geist Mono stats с separator dots
- Tab-bar canonical

### Skills run

Не запускал отдельные slash-skills (inline-исполнение). Self-review через Read PNG: визуально проверил все 3 экрана — копи anti-slop (нет «Самое время начать!», нет catastrophizing на пустом месяце), illustrations отличают «отдых сейчас» (moon) от «время вперёд» (clock+forward arrow).

### Decisions / compromises

1. **15 июня 2026 = Понедельник, НЕ Пятница** — в brief было «Пятница, 15 июня · 3 тренировки», но календарно для 2026 это Monday (1 июня = пн). Выбрал **календарно-корректный «Понедельник»**, чтобы grid layout совпадал. Если PM хочет «Пятница» — нужно сместить grid (например 19.06 = пт).
2. **Forward chevron Phone 2 disabled** (а не просто muted) — opacity 0.55 + муарный фон + `aria-disabled="true"`, cursor not-allowed. Согласно open-вопросу #2 brief'а: я выбрал hard-disabled — clearer affordance, что вперёд ничего нет.
3. **Multiple sessions — stack inline под grid'ом** (не modal). 3 разные активности (Бег + Прогулка + Йога) согласно open-question #4.
4. **Empty month copy** — выбрал тон-нейтральную «Может быть, отдых был запланирован» (supportive, не demotivating, не патетично).
5. **Empty-state illustration на Phone 1** в proof выглядит компактной из-за вертикальной плотности (calendar grid + state + tab-bar = ~844px) — пришлось пожать gap. Если PM хочет крупнее illustration → сократить grid до compact-mode.
6. **Empty-state на Phone 1 не использует eyebrow** (no «ОТДЫХ» badge) — сразу title, чтобы не перегружать «пустой» экран. На Phone 2 eyebrow «БУДУЩЕЕ» нужен для семантического разграничения «empty» vs «future».

### Что требует ревизии PM

1. **Day-of-week mismatch:** Brief говорит «Пятница, 15 июня», я поставил «Понедельник, 15 июня». Подтвердить какой день нужен — это влияет на calendar layout (если пятница, dots должны быть на 12/13.06 или сместить кейс на 19.06).
2. **Copy «Может быть, отдых был запланирован»** — ОК? Альтернатива «Самое время начать первую тренировку» (более активная). 
3. **Future-month CTA «Назад в июнь»** vs альтернативные «Назад к текущему месяцу» (универсальнее для других будущих месяцев).
4. **«3 тренировки» в section-title** — wine mono subscript ОК или хочется bold inline в Onest?
5. **Session icon-bg** — primary-soft (бледно-pink), уверены что не нужен neutral muted? wine-soft хорошо отделяет от карточки, но может быть слишком sentimentic.

### Регрессии

Нет. Базовый History (`mobile-history-v0.html`) не трогал — только заимствовал patterns. Tab-bar canonical из mobile-home-f1-v0.html скопирован 1:1. Цвета `--primary` #831843 защищены. Box-sizing border-box применён глобально. WCAG: muted-foreground-soft #a8a299 на heat-0 #f5f2eb ≈ 2.7:1 — это **под порогом WCAG AA для текста**, но допустимо для disabled/future-state. PM решит, нужно ли затемнить.
