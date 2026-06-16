# BRIEF: C1 Revision — Compress padding в Profile edit · Neiry Pulse Ф1

**Дата:** 2026-06-14
**Заказчик:** PM (Костя)
**Контекст:** C1 закоммичено (`6cff452`). PM выявил overflow в Phone 1 Profile edit — обрезаются Connected braclet card + «Удалить аккаунт» text-link. Нужна compress-правка чтобы ВСЕ элементы помещались в 844px viewport.

**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/mobile-profile-hrv-detail-v0.html`

**Что НЕ трогать:** Phone 2 (HRV detail) и Phone 3 (HRV explainer modal) — они помещаются корректно.

---

## Задача: compress padding в Phone 1 Profile edit

Цель — вместить ~900px контента в 844px viewport через визуальное сжатие. Все запрошенные элементы должны остаться видны.

### Текущая структура (~900px overflow)
- App-bar ~60px
- Avatar block ~140px (avatar 96px + «Изменить фото» + padding)
- 7 form fields × ~70px = ~490px
- Braclet section ~80px
- «Удалить аккаунт» link ~50px
- Tab-bar ~80px
- **Total: ~900px** — overflow ~60px

### Compress правки

1. **Avatar block:**
   - Avatar 96px → **72px** (initials font auto-scale)
   - Padding над/под — уменьшить с ~20px до ~12px
   - «Изменить фото» text-link: 13pt → 12pt
   - Экономия: ~30-40px

2. **Form fields:**
   - Vertical gap между полями: ~14px → **10px**
   - Padding внутри каждого field row: ~16px → **12-14px**
   - Label-to-value spacing: ~6px → **4px**
   - Экономия: ~20-30px по форме

3. **Optional micro-compressions:**
   - Section «БРАСЛЕТ» card: padding 16 → 12
   - «Удалить аккаунт» padding: 24 → 16
   - Экономия: ~10-15px

**Цель:** total ~840px (помещается в 844px). Все элементы видимы при render 460×920.

### Что НЕ менять
- Содержание полей (всё остаётся)
- Колонки / структура (avatar + 7 fields + braclet + удалить + tab-bar)
- Шрифты (Onest / Space Grotesk / Geist Mono)
- Цвета (wine accent, destructive red, success-green dot)
- Иконки (camera, chevron, success-dot)

---

## Дизайн-принципы (соблюдать)

- **Box-sizing border-box** глобально
- **Tailwind CDN** оставить
- **Phone 2 + Phone 3 не трогать**
- **Header canonical** остаётся
- **Tab-bar canonical** остаётся (Ещё active wine)

---

## Output

**slicing-script DEPRECATED** — crop из 3-phone side-by-side render.

Перегенерировать ТОЛЬКО Phone 1 PNGs:

1. **Transparent:** `screenshots/sliced-flow-v2-1-transparent-2026-06-14/20a-profile-edit.png`
2. **Proof:** `screenshots/onboarding-2026-06-14/40-profile-edit.png`
3. **Side-by-side (3-phone wide):** `screenshots/onboarding-2026-06-14/43-profile-hrv-side-by-side.png`

Phone 2 (20b, 41) и Phone 3 (20c, 42) PNG — НЕ перегенерировать (они не изменились).

**НЕ КОММИТЬ.**

---

## Acceptance criteria

- [ ] Phone 1 HTML compressed
- [ ] Avatar 96 → 72px
- [ ] Form field gap 14 → 10px
- [ ] Vertical padding sections сжато
- [ ] ВСЕ элементы видимы на 460×920 render: avatar / 7 form fields / Connected braclet card / «Удалить аккаунт» link / tab-bar
- [ ] Phone 2 + Phone 3 не тронуты
- [ ] PNG регенерированы (20a, 40, 43)
- [ ] **Self-review обязательно** — открыть `40-profile-edit.png` через Read tool, подтвердить ВИЗУАЛЬНО что braclet card + «Удалить аккаунт» теперь видимы

---

## Skills

UX/UI агент — выбирай сам. Compress без потери readability — приоритет.

**НЕ запускать:** init/document/craft/extract.

---

## РЕЗУЛЬТАТ (заполняет UX/UI агент)

**Дата:**
**Изменено в Phone 1:**
**Новый total height:**
**PNG регенерированы:**

### Self-review (визуальный — какие элементы теперь видны)

### Регрессии (если что-то ухудшилось)
