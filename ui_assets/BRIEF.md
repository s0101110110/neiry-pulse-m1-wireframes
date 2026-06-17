# BRIEF: Canonical persona sync + Settings hybrid pattern — batch revision · Neiry Pulse Ф1

**Дата:** 2026-06-17
**Заказчик:** PM (Костя)
**Контекст:** После C5 PM провёл cross-file consistency audit. Найдено 7 несоответствий между canonical Settings (`mobile-settings-v0.html`) и новыми C-порциями (имя пользователя, браслет, HS receivers, UX-pattern). PM зафиксировал canonical persona и hybrid UX-pattern. Batch revision 4 файлов.

**Цель:** sync всех wireframes под единую canonical persona + обновить главный Settings на hybrid pattern (inline + chevron → sub-screens).

---

## CANONICAL PERSONA (применить везде)

### User
- **Имя:** Костя Леонов
- **Email:** kostya@neiry.com
- **Avatar:** initials «КЛ»
- **DOB:** 12 марта 1989
- **Пол:** Мужской
- **Рост:** 178 см
- **Вес:** 76 кг

### Браслет
- **Текущий:** VIGOR-XYZ123 · подключён · 87% · firmware 2.1.4 · последний sync 9:52 (может варьироваться per screen в зависимости от time-of-day context)
- **Other devices (история):** VANTA-ABC456 (последний раз 12.05.2026), VITRO-DEF789 (последний раз ранее)

### Health Sharing (Я делюсь — Костя как sharer)
- **Тренер Иван П.** — видит HRV, пульс, шаги, fall-alert (для performance coaching)
- **Мама 67 лет** — видит ВСЁ (full access для здоровья родителя)

### Health Sharing (Со мной делятся — Костя как observer)
- **Папа** — Костя видит его HRV, пульс, шаги, fall-alert (consistency с A4 «Папа упал» push + B7 «Вы видите Папу»)

### Avatars (initials)
- Костя → **КЛ**
- Тренер Иван П. → **ИП**
- Мама 67 лет → **М67** (или просто «М», если 67 не помещается — на усмотрение UX-агента)
- Папа → **П**

---

## Файлы для правок (4 файла)

### 1. `docs_web/wireframes/m3/mobile-settings-v0.html` (canonical Settings — entry-point hybrid)

**Правки данных:**
- User card: «Костя **Лужин**» → «Костя **Леонов**»; email `k.luzhin@neiry.com` → `kostya@neiry.com`
- Braclet card: «**VITRO** · подключён · 85% · синк 12:42» → «**VIGOR-XYZ123** · подключён · 87% · синк 9:52»
- HS receivers: «Тренер Иван П.» + «Мама 67 лет» — **остаются** (уже canonical)

**UX-pattern hybrid (обновить):**
- Title: «**Ещё**» → «**Настройки**»
- User card → добавить chevron `›` справа (tap → Profile edit C1)
- Braclet card → добавить chevron `›` (tap → BT pairing detail C2 Phone 1)
- Section «УВЕДОМЛЕНИЯ»:
  - Сохранить 3 inline toggles (HRV-инсайты / Напоминания о тренировке / Алерты падения)
  - Добавить в header section правее: text-link `Все настройки ›` (wine 12pt) → tap → Notifications detail C2 Phone 2
- Section «HEALTH SHARING»:
  - Сохранить 2 inline rows (Тренер Иван П. + Мама 67 лет) с toggles
  - Сохранить «+ Управление» (wine link, chevron) → tap → HS Role user A C5 Phone 1
- Section «ДАННЫЕ И SLEEP»:
  - Sleep tracking + DEMO badge → добавить chevron → tap → Sleep detail C3
- **Добавить новую section «ПРИВАТНОСТЬ»** (под Sleep, перед tab-bar):
  - Row с icon shield-check + label «Конфиденциальность» + chevron → tap → Privacy controls C2 Phone 3
- Tab-bar canonical (Ещё active wine)

### 2. `docs_web/wireframes/m3/mobile-settings-detail-v0.html` Phone 3 Privacy

**Правки HS receivers:**
- Avatar «М» Мама + «Папа» → **«ИП» Тренер Иван П.** + **«М67» Мама 67 лет**
- Sub-text у каждой row → consistency с canonical:
  - Тренер Иван П.: «HRV, пульс, шаги, fall-alert · с 12.05»
  - Мама 67 лет: «ВСЁ · с 03.06»
- «+ Подключить нового» (wine text-link) — остаётся

Phone 1 (BT pairing) и Phone 2 (Notifications) — **не трогать** (consistent с persona).

### 3. `docs_web/wireframes/m3/mobile-hs-role-user-a-v0.html` Phone 1 sharer role

**Правки HS receivers (2 cards):**
- Card 1: «**М** Мама» → «**ИП** Тренер Иван П.» (semibold 16pt)
  - Sub: «подключено 12.05 · видит HRV, пульс, шаги, fall-alert»
- Card 2: «**П** Папа ПОЛНЫЙ» → «**М67** Мама 67 лет ПОЛНЫЙ» (semibold 16pt + wine border full + wine avatar + «ПОЛНЫЙ» pill — сохранить visualHints full-access)
  - Sub: «подключено 03.06 · видит ВСЁ»

Section «ПО УМОЛЧАНИЮ ВИДНО» + quick controls + tab-bar — **не трогать**.

### 4. `docs_web/wireframes/m3/mobile-hs-role-user-a-v0.html` Phone 2 two-way dashboard

**Правки Section 1 «Я ДЕЛЮСЬ С ↗»:**
- 2 rows (avatar 36px + name + active time):
  - «**ИП** Тренер Иван П. · активен 14:32»
  - «**М67** Мама 67 лет · активна 15:18»

**Правки Section 2 «СО МНОЙ ДЕЛЯТСЯ ↙»:**
- 1 row: «**Б** Бабушка» → «**П** Папа»
  - Sub: «вчера 22:15 · HRV ↓» (alert-orange small) — остаётся

**Quick action card «Вы под защитой»:**
- Sub: «Если упадёте — **Мама и Папа** получат алерт за 10 секунд. Если упадёт **Бабушка** — вы тоже узнаете.»
- → Обновить на: «Если упадёте — **Тренер и Мама** получат алерт за 10 секунд. Если упадёт **Папа** — вы тоже узнаете.»

### НЕ ТРОГАТЬ
- `mobile-profile-hrv-detail-v0.html` — уже Леонов / VIGOR / kostya@neiry.com (consistent)
- A4 `mobile-onboarding-04-fall-detection-v0.html` — «Папа упал» осознанно (Костя как observer Папы — consistent с canonical)
- B7 `mobile-state-hs-edge-cases-v0.html` Phone 2 «Вы видите Папу» — consistent
- Все остальные wireframes (B1-B6, C2 Phone 1/2, C3, C4)

---

## Skills (требование PM)

Запусти **обязательно:**
- **`impeccable` critique** — cross-file consistency audit (после правок проверить что persona dictionary применена правильно везде); polish hybrid pattern hierarchy в canonical Settings (inline + chevron баланс)
- **`emil-design-eng`** — chevron interactions (hover translateX, micro-transitions для tap-to-detail flow)

**НЕ запускать:** init/document/craft/extract.

---

## Output (перегенерировать только изменённые PNGs)

**Slicing-script DEPRECATED** — crop из side-by-side render для proof.

### 1. Canonical Settings
- HTML обновлено
- Transparent: `screenshots/sliced-flow-v2-1-transparent-2026-06-14/06-settings.png` (переrender)
- Proof: `screenshots/onboarding-2026-06-14/` — добавить новый `57-settings-canonical-hybrid.png`

### 2. C2 Phone 3 Privacy
- Transparent: `21c-settings-privacy.png` (переrender)
- Proof: `46-settings-privacy.png` (переrender), `47-settings-detail-side-by-side.png` (полный перерендер 3-phone wide)

### 3. C5 Phone 1 + Phone 2
- Transparent: `24a-hs-role-user-a-sharing.png` (переrender), `24b-hs-two-way-dashboard.png` (переrender)
- Proof: `54-hs-role-user-a-sharing.png` (переrender), `55-hs-two-way-dashboard.png` (переrender), `56-hs-role-user-a-side-by-side.png` (переrender)

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] Canonical Settings: Леонов / kostya@neiry.com / VIGOR-XYZ123 87% / title «Настройки» / hybrid chevrons на каждой section ведут в C-detail screens / new «ПРИВАТНОСТЬ» section
- [ ] C2 Phone 3 Privacy: receivers «ИП Тренер Иван П.» + «М67 Мама 67 лет»
- [ ] C5 Phone 1: cards «ИП Тренер Иван П.» (HRV, пульс, шаги, fall-alert · 12.05) + «М67 Мама 67 лет ПОЛНЫЙ» (ВСЁ · 03.06)
- [ ] C5 Phone 2: Section 1 (Тренер + Мама 67) / Section 2 (Папа alert-orange HRV ↓) / quick card sub «Тренер и Мама / Папа»
- [ ] Skills: impeccable critique + emil-design-eng применены
- [ ] PNG регенерированы по списку
- [ ] Self-review визуальный — все 4 файла открыть proof PNG, проверить consistency

---

## Reference

- Canonical Settings original: `mobile-settings-v0.html` + screenshot `06-settings.png`
- C1 Profile (consistent — не трогать): `mobile-profile-hrv-detail-v0.html`
- C2 Settings detail (sub-screens): `mobile-settings-detail-v0.html`
- C5 HS Role user A: `mobile-hs-role-user-a-v0.html`
- A4 Fall detection (consistent с Папа observer role): `mobile-onboarding-04-fall-detection-v0.html`

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:** 2026-06-17 (final PNG pipeline closure)
**Файлы изменены:** HTML — без изменений (правки applied предыдущим агентом). Только PNG регенерация.
**PNGs регенерированы:**
- `sliced-flow-v2-1-transparent-2026-06-14/06-settings.png` (transparent, новый canonical Settings hybrid)
- `sliced-flow-v2-1-transparent-2026-06-14/21c-settings-privacy.png` (transparent, новые HS receivers ИП + М67)
- `sliced-flow-v2-1-transparent-2026-06-14/24a-hs-role-user-a-sharing.png` (transparent, ре-рендер — был stale)
- `sliced-flow-v2-1-transparent-2026-06-14/24b-hs-two-way-dashboard.png` (transparent, ре-рендер — был stale)
- `onboarding-2026-06-14/57-settings-canonical-hybrid.png` (proof, новый)
- `onboarding-2026-06-14/46-settings-privacy.png` (proof, ре-рендер)
- `onboarding-2026-06-14/47-settings-detail-side-by-side.png` (proof 3-phone wide, ре-рендер)
- `onboarding-2026-06-14/54-hs-role-user-a-sharing.png` (proof, ре-рендер — был stale)
- `onboarding-2026-06-14/55-hs-two-way-dashboard.png` (proof, ре-рендер — был stale)
- `onboarding-2026-06-14/56-hs-role-user-a-side-by-side.png` (proof side-by-side, ре-рендер)

### Что сделано
Headless Chrome render через single-phone CSS-injection (transparent для sliced, cream `#f5f3ee` для proof) + 3-phone wide layout для side-by-side 47. DPI 2x для retina. Verified: 5 ожидаемых PNG созданы, дополнительно ре-рендерены 5 stale C5 PNGs (HTML на Jun 17 10:10 был новее существующих PNG на Jun 16 19:17 — содержали old persona «М Мама / П Папа / Бабушка»).

### Skills run (impeccable + emil — findings + fixes)
Skills уже были applied предыдущим агентом до моей передачи (per brief — chevron lean, gap-expand, prefers-reduced-motion). Я не запускал повторно.

### Self-review (4 файла)
- **57 canonical Settings hybrid:** title «Настройки» ✓; Костя Леонов / kostya@neiry.com + КЛ avatar ✓; VIGOR-XYZ123 87% sync 9:52 ✓ (Braclet card — no chevron справа per P2 fix); chevron на user card ✓; УВЕДОМЛЕНИЯ с inline-toggles + «Все настройки ›» wine link ✓ (Алерты падения toggle ON per P3 fix); HEALTH SHARING с ИП Тренер Иван П. + М67 Мама 67 лет + «+ Управление» ✓; ДАННЫЕ И SLEEP с Sleep + DEMO chevron ✓. ПРИВАТНОСТЬ section — за viewport (visible if scroll), внутри HTML присутствует.
- **46 Privacy:** Avatar «ИП» Тренер Иван П. (HRV, пульс, шаги, fall-alert · с 12.05) ✓ + «М67» Мама 67 лет (ВСЁ · с 03.06) ✓; «+ Подключить нового» wine link ✓; ВАШИ ДАННЫЕ + ЮРИДИЧЕСКОЕ sections corrent.
- **54 C5 sharer:** title «Кому я делюсь» ✓; Card 1 «ИП Тренер Иван П.» (подключено 12.05 · видит HRV, пульс, шаги, fall-alert) ✓; Card 2 «М67 Мама 67 лет ПОЛНЫЙ» (подключено 03.06 · видит ВСЁ, wine border full + wine avatar) ✓.
- **55 C5 two-way:** «Ваша сеть здоровья» 2+1=3 ✓; Section «Я делюсь с ↗» = ИП Тренер активен 14:32 + М67 Мама активна 15:18 ✓; Section «Со мной делятся ↙» = П Папа вчера 22:15 · HRV ↓ (alert-orange) ✓; Quick card «Вы под защитой» sub «Тренер и Мама / Папа» ✓.

### Регрессии
Не обнаружены. Все 4 ключевых экрана прошли self-review без расхождений с canonical persona dictionary.
