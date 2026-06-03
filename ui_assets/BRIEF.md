# BRIEF — UX/UI Дизайнер

## Статус
🔴 **Активное задание от PM от 2026-06-03 — BRIEF #1 из M2 Handover-пакета.**

R6/R8 drilldown уже запушены в main (cf0f1f1) — этот скоуп закрыт.

---

## Задача: создать `wireframes/m2/mobile-main.html`

Минимальный рестайл из `wireframes/m1/mobile-home.html` под выставочный пакет M2.

### Что нужно сделать
1. Скопировать `docs_web/wireframes/m1/mobile-home.html` → `docs_web/wireframes/m2/mobile-main.html`
2. Добавить блок **«Сегодня»**:
   - **BPM live** (большое число tabular-nums + точка-индикатор статуса)
   - **HRV today** (RMSSD, мс, маленькое число + точка)
   - **Шаги** (круговой прогресс или bar, число / 10 000)
3. Добавить **sparkline истории 24ч** под BPM (inline SVG, ~80px высота, neutral foreground, без заливки)
4. Привести типографику и палитру к **UI Kit M2** (`docs_web/wireframes/m2/ui-kit.html`):
   - Шрифт: тот, что выбран в UI Kit (Manrope или то, что уже стоит)
   - Применить t-* helper-классы (если в файле они уже есть после R5)
   - Семантические токены через CSS-переменные, не хардкод hex (кроме wine `#831843`)
   - **Tabular-nums** на BPM/HRV/шагах: `font-variant-numeric: tabular-nums`
5. Убрать devbar если есть (это финальный мокап, не state-switcher)

### Эстетика — те же правила, что R8
- Clinical, без похабщины: нет ярким заливкам, эмодзи, градиентам, glow, неону
- Цвет статуса — только в **маленьких индикаторах** (точка 8×8, полоска 4px слева, подчёркивание числа)
- Значение метрики — нейтральный foreground, цвет только на пограничной семантике
- Подписи статусов: «Норма / Снижена / Низкая» — subdued, без капса и !

### Что показать
- Применённый UI Kit (типографика, цвета, токены)
- Tabular-nums на цифрах (BPM, HRV, шаги выровнены по колонкам)
- Sparkline истории 24ч (плоский, без декора)

### Приёмка PM
- Открывается в Chrome mobile viewport (375×812)
- Видны: BPM live, HRV today, шаги, sparkline 24ч
- Нет devbar
- Tabular-nums применены
- Скриншот PM в чат **до** push

### Срок
до конца дня **2026-06-03**

### Способ работы
1. Создать файл, заскриншотить, отправить PM в чат **ДО коммита**
2. Дождаться «принято» от PM
3. Закоммитить (русское сообщение: «Добавил mobile-main.html: live BPM + HRV + шаги + sparkline 24ч»)
4. Push после OK PM

---

## Технические правила (НЕ нарушать)
- ✅ HTML5 + Tailwind CDN, inline SVG для sparkline
- ✅ Семантические CSS-переменные (не хардкод hex кроме wine)
- ❌ React/Vue/JS-фреймворки
- ❌ Inline-стили
- ❌ Эмодзи в UI, градиенты, glow, неон, яркие заливки карточек

## NDA-safe
В UI запрещено: VITRO/VANTA/VIGOR, M1/M2/M3, имена B2B-клиентов.

## После выполнения
Доложить PM: DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED.

**BRIEF #2 (рестайл `neiry_pulse_v5.html` под дашборд корпоратов)** придёт после acceptance этого BRIEF.
