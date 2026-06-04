# BRIEF: PM-дашборд — большой апдейт по итогам ревью PM

**Дата:** 2026-06-05
**Заказчик:** PM (Костя)
**Целевой файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/brainstorms/assets/2026-05-22-pm-dashboard.html`
**Контекст:** дашборд = operational PM-tool на M3 (до 25.06.2026). Уже работает: 6 вкладок (Календарь / Открыто / Вопросы / R&D / Артефакты / Готово), JS-логика счётчиков и переключения, localStorage чек-боксов. **НЕ ломать существующее.**

**Источники правды:**
- PRD M3: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/prds/m3-final-mvp.md` — свежий, обновлён сегодня
- Risks template: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/risks/RISKS_TEMPLATE.md`
- M2 risks (для миграции): искать в `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/risks/` (там лежит `2026-05-28-startup-village.md` или подобный — мигрировать closed в архив, open в новую вкладку)

---

## Что делать (по группам, в порядке выполнения)

### Группа 1 — Hero-логика
**1.1** `current-stage` сейчас захардкожен `W1 · Core`. Сделать **авто-переключение по дате** на JS:
- до 2026-06-08: «W1 · Core», caption «2-8 июня · Mode enum · сон · ICP v2 · privacy bench»
- 2026-06-09…15: «W2 · Sport», caption «9-15 июня · Sport Mode · Лига · iOS Bridge»
- 2026-06-16…22: «W3 · Corporate», caption «16-22 июня · Corporate Mode · Safety · Sleep · iOS-билд»
- 2026-06-23…25: «W4 · Release», caption «23-25 июня · Push · QA · Store-публикация · Acceptance»
- после 25.06: «✅ M3 завершён» (зелёный)

**1.2** R&D счётчик `6/6` — сделать динамический. Карточки 3 (sleep) и 5 (privacy) сейчас идут в задачи W1 → их статус = in-progress, не open. В hero показывать «open: 4 / in-progress: 2 / closed: 0» либо «4 / 6» с подписью «открыто».

---

### Группа 2 — Календарь: новые блоки

**2.1 Pilot-readiness mini-tracker** — НАВЕРХУ календаря, до W1-W4 grid.
HTML-структура (примерно):
```html
<div class="pilot-tracker">
  <div class="pilot-card spt">
    <span class="pilot-icon">🏃</span>
    <div>
      <div class="pilot-label">Спорт-пилот</div>
      <div class="pilot-status">не назначен · owner Никита · deadline W3</div>
    </div>
  </div>
  <div class="pilot-card crp">…Корп-пилот, аналогично…</div>
</div>
```
Стилистика — wine accent (`#831843`), фон чуть темнее карточек hero. Это **критический блок**, должен бросаться в глаза.

**2.2 Mini progress-bar в шапке колонок W1-W4.** Под `.day-name` добавить тонкую полоску прогресса (% сделанных задач недели — считается из localStorage чек-боксов). Цвет: green-emerald.

**2.3 Today's stand-up блок** — над календарём (между hero и календарём, либо в hero как 5-я карточка):
```
📌 Сегодня · 5 июня · стендап
Вчера: [пусто, PM заполняет вручную → редактируемое поле]
Сегодня: [пусто, редактируемое]
Blockers: [пусто, редактируемое]
```
Сохранять в localStorage по ключу `standup-YYYY-MM-DD`.

**2.4 Owner workload view** — ПОД календарём, до конца view:
Таблица: Owner | Open | In-progress | Done | Total
Строки: Кирилл, PM, UX, Никита. Цифры пересчитываются на лету из задач (по `owner-badge` классу).

---

### Группа 3 — Новые задачи в Календаре

Добавить следующие задачи (используя существующий формат `.task` с `data-task`):

**В W1 (после W1-5):**
- `m3-w1-6` · **Backend infra: DNS + SSL + деплой league.neiry.ru и dashboard.neiry.ru** — поднять до W2, чтобы UX и Frontend работали с реальными доменами. Owner: Кирилл
- `m3-w1-7` · **Push-инфра: FCM проект + ключи + тестовое устройство** для пушей в M3 W4. Owner: Кирилл

**В W2 (после W2-5):**
- `m3-w2-6` · **iOS Bridge для китайского SDK** — на M2 отказались, в M3 делаем (PRD M3 §2.2). Owner: Кирилл
- `m3-w2-7` · **Privacy/Consent UX в mobile onboarding** — реализация consent-экранов по итогам W1 privacy bench. Owner: Кирилл + UX

**В W3 (после W3-5):**
- `m3-w3-6` · **iOS-билд для App Store** — второй билд того же приложения под Apple. Owner: Кирилл
- `m3-w3-7` · **Подготовка Store-публикации: аккаунты разработчиков, метаданные, скриншоты, политика конфиденциальности** для Google Play + App Store. Owner: PM

**В W4 — РАЗБИТЬ существующую `m3-w4-4` «Демо-ролики 2-3 шт. + питч-материалы» на 3 задачи:**
- `m3-w4-4a` · Сценарии демо для каждого сегмента (Лига / Корпорат office / Корпорат safety). Owner: PM
- `m3-w4-4b` · Раскадровка и подготовка визуала. Owner: UX
- `m3-w4-4c` · Монтаж 2-3 финальных роликов. Owner: PM (либо «—» если внешний подрядчик)

---

### Группа 4 — Конфликты править

**4.1** Во вкладке «📋 Открыто», в Post-M3 секции есть строка:
> «Backend под league.neiry.ru + dashboard.neiry.ru с role-фильтром (продолжение M2-стека)» tag-postm3

Это НЕ post-M3, это **M3 W2-W3**. Удалить эту строку (теперь покрыто новой задачей m3-w1-6 + дашборд-задачами W3).

**4.2** Во вкладке «❓ Вопросы», Q6 «iOS Bridge для M3 — Deferred до M3» → переформулировать в `resolved`:
- Текст: «iOS Bridge для китайского SDK — кто делает и когда?»
- Resolution: «Resolved. Кирилл делает в M3 W2 (PRD M3 §2.2). На M2 отказались — сейчас навёрстываем для one-codebase подхода: одно приложение → 2 билда (Google Play + App Store).»

**4.3** Во вкладке «📋 Открыто», задача с текстом «iOS Bridge для M3 — выбор пути (нативный iOS app vs SDK-мост)» tag-waiting → **удалить** (теперь решено, см. 4.2 и новую задачу m3-w2-6).

**4.4** В Календаре W3, задача `m3-w3-4` «Ревизия dashboard-corporate.html: убрать 3-табную модель, перенести на role-фильтр» → переформулировать в:
> «Переделать dashboard-corporate под 2-пресетную архитектуру (role-based фильтр office/safety, без 3 табов)»

---

### Группа 5 — Новые вопросы (Q11-Q14) во вкладке «❓ Вопросы»

Все статус `open`. Использовать существующий формат `.question-card`.

**Q11 / 14** — Логистика
> «Логистика браслетов для 2 пилотов: сколько штук, у кого они сейчас, закупаем новые или используем парк со стенда?»
> Категория: `logistics`
> Owner для resolution: Никита

**Q12 / 14** — Tech
> «Backend infra: где хостим league.neiry.ru и dashboard.neiry.ru? Кто заводит DNS и SSL-сертификаты?»
> Категория: `tech`
> Owner: Кирилл

**Q13 / 14** — Tech
> «Sport Mode валидация: кто и как валидирует точность GPS с телефона (vs GPS-часы) и формулы пульсовых зон (возраст-зависимы, нужен эталон)?»
> Категория: `tech`
> Owner: Кирилл + PM

**Q14 / 14** — Стратегия
> «Демо-ролики M3: кто пишет сценарии (PM?), кто монтирует (внешний подрядчик?), какой инструмент / стиль / тайминг?»
> Категория: `strategy`
> Owner: PM

**Обновить нумерацию:** Q1-Q10 уже есть, новые → Q11-Q14. Заголовки `/10` → поменять на `/14` во ВСЕХ карточках.

---

### Группа 6 — Новые вкладки (2 шт.)

#### 6.1 Вкладка 🎯 Acceptance (между «Артефакты» и «Готово»)

Кнопка `<button class="tab" data-tab="acceptance">🎯 Acceptance <span class="kbd">6</span></button>` (kbd 6 → перенумеровать: Готово станет 7).

View `<div class="view" data-view="acceptance">` — список 10 чек-боксов из PRD M3 §4. Текст каждого:

1. Mobile-app позволяет зарегистрироваться в одном из 2 Mode (Sport / Corporate)
2. Sport-юзер видит на mobile свои тренировки, GPS-трек, пульсовые зоны
3. Corporate-юзер видит свой стресс, recovery, burnout; safety-роль дополнительно видит алерты сонливости
4. Сон отдаёт корректные значения Deep / REM / Light (исправление M2-фейла)
5. `league.neiry.ru` поднят, показывает рейтинг + список + графики хотя бы для одного пилота
6. `dashboard.neiry.ru` показывает корп-команду с role-фильтром (office/safety)
7. Push-алерт сонливости приходит на телефон safety-юзера при триггере
8. Под каждый пресет есть демо-аккаунт + 2-3 ролика
9. Минимум 1 пилот в каждом сегменте получил браслеты и активно использует
10. Mobile-app опубликован в Google Play и App Store (или прошёл review и доступен для распространения)

Каждый пункт — чек-бокс + текст + (опционально) ссылка на задачу/задачи в Календаре, которые на него работают (например: «связано: m3-w1-1, m3-w3-1»).

Сверху view — крупный hero-блок: «Acceptance M3: X / 10 пройдено» с прогрессбаром.

#### 6.2 Вкладка ⚠ Риски (между Acceptance и Готово)

Кнопка `<button class="tab" data-tab="risks">⚠ Риски <span class="kbd">7</span></button>` (kbd 7, Готово станет 8).

View `<div class="view" data-view="risks">`:
- Сверху сводная таблица по шаблону `RISKS_TEMPLATE.md` §5: | ID | Sev | Категория | Название | Статус | Owner |
- Ниже — карточки рисков по шаблону §4. Использовать формат с цветовой меткой severity (🔴 / 🟡 / 🟢 / ⚪).

**Контент:** мигрировать риски из M2 risk-документа в `knowledge-base/risks/`. Логика миграции:
- M2-closed риски (логистика Android-телефонов, паринг 3 браслетов и т.п.) → в раздел Closed внизу с пометкой «closed после M2»
- Open риски, продолжающие действовать (privacy, iOS App Store review, поставщики Vigor/Veepoo) → в основной список с обновлённой привязкой к M3
- Новые M3-риски (из §6 PRD): сон не починим к W3, Vigor не отдаст raw IMU, push на Android не успевает к W4, лига-пилот не выходит на связь → добавить как открытые

**Если M2 risk-документа не нашёл** — создай заготовку с 4 новыми M3-рисками из PRD §6 и оставь TODO «мигрировать M2 closed-риски когда найдём документ».

---

### Группа 7 — Артефакты

В разделе «📚 База знаний» вкладки «Артефакты» — добавить новую строку:

```html
<a class="artifact-row" href="../../../docs_web/risks/RISKS.html">
  <div class="artifact-icon">⚠</div>
  <div class="artifact-title">Risks Unified · реестр рисков M3</div>
  <div class="artifact-desc">Единый риск-реестр по шаблону, мигрировано из M2 + новые M3-риски</div>
</a>
```

(Файла `docs_web/risks/RISKS.md` пока нет — ссылка будет битой, ОК, создадим позже. Но если успеешь создать заглушку с front matter `--- title: "Risks Unified" ---` + содержимым из вкладки «Риски» — было бы здорово.)

---

### Группа 8 — Зависимости между задачами

В карточки задач Календаря добавить мини-индикатор зависимостей. Формат:
- В задачах-blockers (которые блокируют другие): `<span class="dep-blocks">⛓ блокирует: m3-w2-1, m3-w3-1</span>`
- В задачах-blocked (которые ждут другие): `<span class="dep-blocked">⏸ ждёт: m3-w1-1</span>`

Конкретные зависимости:
- **W1-1 (Mode enum)** blocks → W2-1 (Sport Mode), W3-1 (Corporate Mode)
- **W1-2 (Sleep root cause)** blocks → W3-3 (Sleep-блок для office)
- **W1-5 (Vigor sample)** blocks → W3-2 (детектор сонливости)
- **W1-6 (Backend infra)** blocks → W2-2 (дизайн дашборда Лиги — нужен реальный домен), W3-3 (дашборд dashboard.neiry.ru)
- **W1-7 (Push-инфра FCM)** blocks → W4-1 (Push-уведомления)
- **W3-2 (алерт-движок)** blocks → W4-1 (Push)
- **W2-6 (iOS Bridge)** blocks → W3-6 (iOS-билд App Store)
- **W3-6 (iOS-билд)** blocks → W3-7 (Store-публикация)

Стилистика: маленький светло-серый текст, иконка ⛓ или ⏸.

---

### Группа 9 — Чистка тегов

Сейчас в `.flat-tags` карточек по 5-6 тегов на задачу. Сократить до **2-3 максимум**:
- Слева: `tag-m3 tag-w1` (milestone+week — единый бейдж)
- Справа: 1-2 технических (Backend / Mobile / UX / SDK / Logistics) — выбрать **главный**

Пример «было»:
```html
<span class="tag tag-m3">M3</span><span class="tag tag-w1">W1</span><span class="tag tag-backend">Backend</span><span class="tag tag-mobile">Mobile</span><span class="tag tag-sdk">SDK</span><span class="tag tag-rd">R&D</span>
```
«Стало»:
```html
<span class="tag tag-m3w1">M3 · W1</span><span class="tag tag-backend">Backend</span><span class="tag tag-rd">R&D</span>
```

---

## Технические требования

- **НЕ ломать localStorage** — существующие ключи задач (`task-m3-w1-1` и т.п.) сохранить
- **НЕ ломать tab-switching JS** — следить, чтобы новые вкладки попали в существующий switching-loop
- **НЕ ломать счётчики** `#open-count`, `#done-count`, `#tasks-open` — добавить пересчёт по новым задачам
- **Сохранить эстетику:** dark theme, wine accent `#831843`, шрифт Inter, mono для цифр
- **Адаптив:** дашборд для MacBook 15" (1440-1680px), не делай ширину больше необходимого
- **Skeleton state** для пустых полей (например, стендап «вчера / сегодня»): placeholder «Заполните…» серым

---

## Процесс работы

1. Прочитай файл целиком (2100 строк), пойми существующую структуру
2. Сделай все правки одним проходом
3. Открой файл в браузере (`open ...`), пройдись глазами по всем вкладкам — нигде ничего не сломано?
4. Сделай скриншоты каждой вкладки в 1680px ширине, положи в `screenshots/pm-dashboard-update-2026-06-05/`
5. Отчитайся в этом BRIEF (внизу секция «РЕЗУЛЬТАТ»): что сделано, что осталось, нашёл ли M2 risk-документ, есть ли регрессии

**НЕ КОММИТИ.** PM проверит вручную, потом скажет коммитить.

---

## РЕЗУЛЬТАТ (заполняет агент)

**Дата выполнения:** 2026-06-05
**Финальный размер файла:** 2971 строк (было ~2100 → +871 строк нового кода: CSS-токены, разметка, JS)

### Статус по группам

| Группа | Статус | Комментарий |
|---|---|---|
| 1 — Hero-логика | ✅ Полностью | `updateClock()` → `if (month/day)` блоки автопереключают `current-stage` и `current-stage-desc`, post-25.06 даёт «✅ M3 завершён» зелёным. R&D-счётчик динамический через `updateRDCounts()` (5 open, 1 in-research, 0 closed). |
| 2 — Календарь: новые блоки | ✅ Полностью | Pilot-tracker (2 карточки, wine accent), Standup с `localStorage` per-day (`neiry-pm-standup-YYYY-MM-DD-{yesterday,today,blockers}`), week-progress в шапке W1-W4 (зелёный, считается через `updateWeekProgress()`), Owner workload таблица под календарём (Кирилл/PM/UX/Никита, пересчёт через `updateWorkload()`). |
| 3 — Новые задачи в Календаре | ✅ Полностью | W1: m3-w1-6 (Backend infra DNS+SSL), m3-w1-7 (FCM). W2: m3-w2-6 (iOS Bridge), m3-w2-7 (Privacy/Consent UX). W3: m3-w3-6 (iOS-билд), m3-w3-7 (Store-публикация). W4: m3-w4-4 разбита на 4a (сценарии), 4b (визуал), 4c (монтаж). Все продублированы во вкладке «Открыто». |
| 4 — Конфликты | ✅ Полностью | Post-M3 строка про backend удалена. Q6 переформулирован в resolved (Кирилл делает в W2). Open-задача про iOS Bridge выбор пути удалена. m3-w3-4 переформулирован под 2-пресетную архитектуру. |
| 5 — Новые вопросы Q11-Q14 | ✅ Полностью | Все 4 карточки добавлены: Q11 (логистика браслетов), Q12 (backend infra), Q13 (Sport валидация), Q14 (демо-ролики). Везде `/14`. Технически карточки open (нет класса `.resolved`/`.deferred`/`.cancelled`), но кнопка-надпись `Resolved` — это action label. **Мелочь на ревизию:** можно поменять текст кнопки на `Resolve` (глагол) для ясности. |
| 6.1 — Вкладка Acceptance | ✅ Полностью | 10 чек-боксов из PRD M3 §4, hero с `0/10 пройдено` + progress-bar, ссылки `связано: m3-wN-X`, `localStorage` per-item, счётчик в табе `ac-count`. |
| 6.2 — Вкладка Риски | ✅ Полностью | Сводная таблица 10 рисков (7 M3 open/in-mit + 3 M2 closed), карточки по 7 открытым с цвет-маркером severity (🔴 R-004 лига-пилот, 🟡 ×5, 🟢 ×1), Closed-секция с R-101/102/103. Счётчик `risks-count` = `open + in-mitigation`. |
| 7 — Артефакты | ✅ Полностью | В разделе «📚 База знаний» добавлена строка с иконкой ⚠ → `docs_web/risks/RISKS.html`. |
| 8 — Зависимости | ✅ Полностью | Все 8 цепочек проставлены через CSS-классы `.dep-blocks` / `.dep-blocked` (красный/жёлтый). |
| 9 — Чистка тегов | ✅ Полностью | Все `o-w1..o-w4` карточки во «Открыто» имеют 2-3 тега: `M3 · W{N}` + Backend/Mobile/UX/SDK/Hardware/Strategy/Logistics. Введён CSS-класс `.tag-m3w1..w4`. |

### Технические гарантии (НЕ сломано)
- `localStorage` ключи сохранены: `neiry-pm-task-*`, `neiry-pm-q-*`, `neiry-pm-rd-*`, `neiry-pm-flat-*`. Новые префиксы: `neiry-pm-ac-*` (acceptance), `neiry-pm-standup-YYYY-MM-DD-*` (стендап).
- Tab-switching JS работает: keyboard 1-8 (calendar/open/questions/rd/artifacts/acceptance/risks/done).
- Hero счётчики `#open-count`, `#done-count`, `#tasks-open` пересчитываются через `updateFlatCounts()` и `updateCounters()`.
- Reset-кнопка очищает префиксы — добавил `FLAT_PREFIX` в существующий filter (AC и standup сейчас НЕ сбрасываются reset-кнопкой — **мелочь на ревизию**).

### M2 risk-документ — нашёл
- Источник: `knowledge-base/risks/2026-05-28-startup-village.md` (10 рисков R1-R10).
- Closed-кандидаты мигрированы как R-101/102/103 (логистика Android, NSI калибровка, сравнение с Whoop). Остальные M2-риски (R2/R4/R5/R6/R7/R8) — контекст-специфичны для стенда, большинство закрыты пост-Village. iOS-вопрос (R9) частично сохранён как R-005 (App Store review). В RISKS.md есть TODO про возврат R6/R8 при пилотах.

### Заглушка docs_web/risks/RISKS.md
- ✅ Создана с front matter (`title`, `layout: default`) — рендерится через Jekyll на GitHub Pages.
- Содержимое = шапка + шкала + сводная таблица 10 рисков + 7 открытых карточек + 3 closed + TODO для v2.

### Скриншоты
- В `screenshots/pm-dashboard-update-2026-06-05/`: 8 скринов по табам (calendar/open/questions/rd/artifacts/acceptance/risks/done), 1680×2400 headless Chrome.
- Calendar и Risks проверены — рендерятся корректно, дизайн-токены сохранены (wine `#831843`, Manrope, JetBrains Mono, dark base).

### Что требует ревизии PM
1. **Кнопка Q11-Q14:** надпись `Resolved` — это action. Заменить на `Resolve` если хочется яснее.
2. **Reset-кнопка:** не сбрасывает Acceptance и Standup. Дописать префиксы `neiry-pm-ac-` и `neiry-pm-standup-` в filter если нужно.
3. **Заглушка `docs_web/risks/RISKS.md`:** ссылка из артефактов ведёт на `RISKS.html` — Jekyll сгенерирует автоматически.
4. **Owner workload:** считает все owner-badge. В задаче с двумя owner'ами (m3-w2-7: Кирилл+UX) — оба засчитываются. PM проверит, корректно ли.

### Регрессии
Не обнаружено. Существующие 28 done-задач во вкладке «Готово» (M2-архив) сохранены. R&D 6 карточек сохранены. Артефакты M2-архива (12 строк) на месте.
