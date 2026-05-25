# M2 UI Restyle — UI Kit + 4 базовых экрана

> **Для исполнения:** План адаптирован под HTML-мокапы (не TDD-разработка). Каждая задача = создать/обновить файл → проверить в браузере → коммит → обновить этот план (отметить чекбокс) → обновить knowledge-base/PROJECT_STATE.md.

**Цель:** Подготовить визуально полные HTML-мокапы (Tailwind CDN) UI Kit и 4 ключевых экранов Neiry Pulse в эстетике shadcn/ui + Tremor, чтобы Кирилл смог собрать React-имплементацию 1:1.

**Архитектура:** Сначала калибровка эстетики (палитра + референсы) с PM → обновление брифа UX/UI Дизайнера → UI Kit как живой styleguide → 4 экрана поверх Kit-токенов → сверка с PM → GitPages.

**Tech Stack:** HTML5 + Tailwind CSS (CDN) + Manrope/Fraunces/JetBrains Mono шрифты + SVG для inline-иконок и графиков. Цель — токены и компоненты, согласованные со стеком React-проекта (shadcn/ui CSS-переменные, Tremor-эстетика дашборда).

**Скоп экранов:**
1. Демо-стенд kiosk на плазме (2 анкера + 1 гость)
2. Drill-down карточка гостя + 3 фазы Bayevsky test + результат
3. Дашборд корпоратов (Neiry Unite v5 — 4 KPI + 3 таба)
4. Приложение паринга — рестайл существующих M1 mobile-* экранов

---

### Задача 1: Калибровка эстетики с PM ✅ ЗАКРЫТА 25.05.2026

**Файлы:** нет (входной gate перед стартом дизайна).

- [x] **Шаг 1: Получить от PM ответы на 2 вопроса** ✅

PM подтвердил:
- **Палитра:** shadcn-defaults zinc/slate + wine accent **#831843** (наследие Neiry-айдентики)
- **Референсы:** Linear / Vercel / shadcn-defaults как baseline + Hume Band для био-визуализаций
- **Темы:** тёмная для плазмы 42", светлая для админ-ноута

- [x] **Шаг 2: Зафиксировать ответы в память** ✅

Создан `memory/project_neiry_ui_aesthetic.md` с финальной палитрой, accent, темами, референсами и типографикой. Добавлен пойнтер в `MEMORY.md`.

- [x] **Шаг 3: Обновить план** ✅

Чекбоксы Задачи 1 отмечены.

---

### Задача 2: Обновить BRIEF.md для UX/UI Дизайнера ✅ ЗАКРЫТА 25.05.2026

**Файлы:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/BRIEF.md`

- [x] **Шаг 1: Перезаписать BRIEF.md** ✅

Новый бриф «M2 UI Restyle: UI Kit + 4 экрана» с полным скоупом, эстетикой, путями файлов, NDA-правилами и форматом отчёта DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED.

- [x] **Шаг 2: Закоммитить** ✅

Закоммитили план в commit c510e9f. BRIEF.md догоняем отдельным коммитом (git case-mismatch с путём).

- [x] **Шаг 3: Обновить план** ✅

---

### Задача 3: UI Kit — живой styleguide ✅ ЗАКРЫТА 25.05.2026

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/ui-kit.html`

Готов в коммите `e18bae3` (создание), `8e1d254` (правки code-review). Spec PASS + code quality APPROVED.

- [x] **Шаг 1: Создать ui-kit.html**

Структура страницы:
1. **Tokens** — палитра (semantic CSS-переменные `--background`, `--foreground`, `--primary`, `--accent`, `--muted`, `--success`, `--warning`, `--destructive`), типографика (Manrope/Fraunces/JetBrains Mono с размерами), spacing-scale, радиусы, тени
2. **Base components** (shadcn-style) — Button (5 вариантов: primary, secondary, ghost, outline, destructive + sizes sm/md/lg), Card, Badge, Input, Select, Tabs, Dialog/Sheet, Tooltip, Avatar
3. **Биометрические виджеты** (кастом) — BPM-card (большое число + sparkline), NSI-gauge (полукруг-шкала со светофором 🟢🟡🔴, ↑ значение = ↑ стресс), Status-pill (NORMAL/ELEVATED/RECOVERY), RMSSD-индикатор с цветовой зоной, R-R sparkline (mini-chart), Heartbeat-pulse-animation
4. **Tremor-style виджеты для дашборда** — KPI-card (заголовок + большая цифра + delta + sparkline), BarList (top-N сотрудников), Progress-bar с цветовыми зонами

Каждый компонент с примером использования и кратким описанием «когда применять».

- [x] **Шаг 2: Проверить в браузере**

- [x] **Шаг 3: Закоммитить**

- [x] **Шаг 4: Обновить план + PROJECT_STATE**

- [ ] **Шаг 5: Чекпоинт с PM**

Показать PM ui-kit.html (локально + GitPages URL). Получить feedback. Если есть правки — внести и повторить Шаг 2-3.

---

### Задача 4: Kiosk restyle (2 анкера + 1 гость) — на ревью у PM

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-v2.html`

Технические шаги пройдены: `3f076f5` (создание) → `1bcb4c7` (QR fix) → `03c0f96` (NSI math + focus-ring). Spec PASS + Code Quality APPROVED. **Принятие PM ожидается.**

- [x] **Шаг 1: Создать kiosk-v2.html**

Layout (плазма 1920×1080, ландшафт):
- Header: лого Neiry + название «Live Demo» + dev-bar для переключения состояний (IDLE / ACTIVE_2 / ACTIVE_3 / PENDING_CLAIM)
- Main area: **3 карточки в ряд** (два анкера + слот гостя)
  - Каждая карточка: имя/роль (Костя/Алексей/Гость) + большой BPM + NSI-gauge + status-pill + R-R sparkline за 60 сек
  - Слот гостя в IDLE: «Надень браслет, чтобы начать» + анимация ожидания
- Footer: NSI-легенда (🟢 0–39 НОРМА / 🟡 40–59 ПОВЫШЕН / 🔴 60–100 ВЫСОКИЙ) + QR-код для TG-отчёта

Использовать токены и компоненты из ui-kit.html.

- [x] **Шаг 2: Реализовать 4 состояния через JS-switcher в dev-bar**
- [x] **Шаг 3: Fake live BPM анимация**
- [x] **Шаг 4: Проверить в браузере**
- [x] **Шаг 5: Закоммитить**
- [x] **Шаг 6: Обновить план + PROJECT_STATE**

- [ ] **Шаг 7: Round 2 правок Kiosk v2 после PM-ревью 25.05**

Правки, которые PM зафиксировал отдельным проходом:
- **A2 калибровка:** прогресс-бар калибровки строится на 12 сек (раньше шло 10–15). При недостатке семплов окно расширяется до 16 сек — добавить визуальный edge-case (текст «Чуть дольше, обнимаем данные…» поверх той же шкалы).
- **A3 drill-down CTA:** в карточке гостя на плазме появляется маленький CTA «Открыть карточку → админ-ноут» (визуальная отметка, что drill-down существует, но активируется со второго экрана). Без перехода в kiosk.html — только подпись.
- **A5 BLE-индикатор:** в карточке каждого участника статус-pill показывает BLE-уровень: 🟢 active (heartbeat ≤ 2 сек) / 🟡 lost (≥5 сек, окно не обнуляется) / 🔴 disconnect (≥30 сек, карточка blur + "Переподключаемся…"). Анимация плавная.
- **A6 убрать QR из футера:** футер плазмы без QR-кода. QR-код выезжает только в `PENDING_CLAIM` (модалка по центру). Освободившееся место в футере — короткая подпись «Сними браслет → получи отчёт» + дискретная анимация.

- [ ] **Шаг 8: Чекпоинт с PM**

---

### Задача 5: Drill-down карточка гостя + Bayevsky test

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-drilldown.html`

- [ ] **Шаг 1: Создать kiosk-drilldown.html**

Layout (админ-ноут, 1440×900, светлая тема — оговорено в брифе 24.05):
- Top bar: ← back to wall + «Гость #3 · 02:47» (timer от начала сессии)
- **Главный блок NSI** — большое число + NSI-gauge + caption «Уровень стресса (NSI · Neiry Stress Index, ↑ = стресс ↑)»
- **4 метрики 2×2** — BPM с sparkline / HRV-RMSSD (или «— нет данных») / SpO₂ / Шаги
- **60-сек график BPM** (line chart, SVG inline)
- **CTA «🧪 Запустить Тест Баевского (5 мин)»** — large primary button + caption «3 мин покоя + Stroop + дорожка»
- **Footer:** STOP SESSION → QR/PIN экран

- [ ] **Шаг 2: Добавить 3 фазы Bayevsky test (state-switcher)**

Состояния (переключаются по клику CTA + dev-bar):
- BAYEVSKY_PHASE_1 — «Покой 3 мин»: большой обратный таймер 03:00 → 00:00, инструкция «Стой неподвижно, дыши спокойно», прогресс-полоса
- BAYEVSKY_PHASE_2 — «Stroop 1 мин»: имитация теста (плашка цвета/слова), таймер 01:00, подпись «Это нормально, что стресс чуть подскочит — мозг работает»
- BAYEVSKY_PHASE_3 — «Беговая дорожка 1 мин»: «Перейди на дорожку, лёгкий бег», таймер 01:00
- BAYEVSKY_RESULT — таблица 3 фаз × значение ИН Баевского + общий вывод (цветовая зона)

**Формула Баевского (Slow, для TG-отчёта):** `ИН = AMo / (2·Mo·MxDMn)`, окно 3-5 мин.
**Двухступенчатый фильтр R-R:** медианный фильтр (отсечь ±20% от медианы) → перцентильный (отсечь 5/95%). Если в окне < 60% валидных R-R → выводить «недостаточно данных, продли фазу».
**CTA «Тест Баевского»** — опциональный, не запускается автоматически; кнопка large primary рядом с NSI-блоком.

- [ ] **Шаг 3: Проверить в браузере**

Открыть kiosk-drilldown.html. Прокликать всю цепочку: drill-down → CTA → фаза 1 → фаза 2 → фаза 3 → результат → back to wall.

- [ ] **Шаг 4: Закоммитить**

```bash
git add docs_web/wireframes/m2/kiosk-drilldown.html
git commit -m "Добавил drill-down карточку гостя + 3 фазы Bayevsky test + экран результата"
git push
```

- [ ] **Шаг 5: Обновить план + PROJECT_STATE + artifacts memory**

- [ ] **Шаг 6: Чекпоинт с PM**

---

### Задача 6: Дашборд корпоратов (Neiry Unite v5)

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3/dashboard-corporate.html` (создать папку m3/ если её нет)

- [ ] **Шаг 1: Создать папку m3/ и dashboard-corporate.html**

Layout (десктоп, 1440×900, светлая тема):
- **Top bar**: лого Neiry + название «Neiry Unite» + переключатель компании + аватар админа
- **3 таба в одной строке**: Спорт / Офис-команда / Драйверы-водители
- **KPI strip — 4 карточки** (Tremor-стиль): Recovery / Stress / Sleep / Burnout (БЕЗ Activity — решение R&D 22.05)
- **График динамики** (line chart 7/30/90 дней) — выбираемая метрика
- **BarList top-10** сотрудников по выбранной метрике
- **Drill-down side-panel** — карточка сотрудника со всеми метриками (включая Activity здесь)

- [ ] **Шаг 2: Реализовать переключатель табов**

Клик по табу → подгружает соответствующий dataset (mock JSON в JS). 3 разных pre-set данных под 3 сегмента.

- [ ] **Шаг 3: Проверить в браузере**

Открыть dashboard-corporate.html. Переключить все 3 таба. Убедиться: KPI обновляются, график перерисовывается, BarList сортируется.

- [ ] **Шаг 4: Закоммитить**

```bash
git add docs_web/wireframes/m3/dashboard-corporate.html
git commit -m "Добавил дашборд корпоратов Neiry Unite v5: 4 KPI + 3 таба + drill-down side-panel"
git push
```

- [ ] **Шаг 5: Обновить план + PROJECT_STATE + artifacts memory**

- [ ] **Шаг 6: Чекпоинт с PM**

---

### Задача 7: Mobile pairing — рестайл + state machine с handoff на плазму

**Файлы:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-splash.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-login.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-registration.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-ble-pairing.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-home.html`
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-name-input.html` (новый экран ввода имени гостя)
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-calibrating.html` (12-сек калибровка)

**State machine** (зафиксирована в брифе A1 раздел 3.3, 25.05):
`pairing → name_input → calibrating → active → ended`

- [ ] **Шаг 1: Применить новую палитру и компоненты UI Kit к 5 mobile-экранам**

In-place edit:
- Заменить старые цвета на CSS-переменные UI Kit
- Заменить кастомные кнопки на компоненты shadcn-стиля
- Применить новый BPM-card и status-pill из Kit на mobile-home

- [ ] **Шаг 1a: Создать mobile-name-input.html (новое состояние `name_input`)**

После BLE-паринга стенд-оператор передаёт телефон гостю; гость вводит имя в input «Как тебя зовут?» → primary-button «Начать». Имя уходит на плазму как `participant.display_name`. Шаг скиппится для анкеров (Костя/Алексей) — у них имя из БД.

- [ ] **Шаг 1b: Создать mobile-calibrating.html (новое состояние `calibrating`)**

12-сек обратный таймер + текст «Стой спокойно, ловим baseline пульс». На 13-й секунде если семплов < 60% → текст «Чуть дольше, ловим стабильный сигнал…», окно расширяется до 16 сек. По завершении → переход на `active` + handoff на плазму.

**BLE lifecycle (фоновая логика, отразить визуально):**
- heartbeat 2 сек (active state)
- lost timeout 5 сек (warning, окно сессии НЕ обнуляется)
- hard disconnect 30 сек (карточка на плазме blur + кнопка переподключения в mobile)

- [ ] **Шаг 2: Дополнительно — почистить дев-жаргон в mobile-hrv-sync.html и mobile-hrv-result.html**

Согласно старому брифу от 24.05:
- `HRV (readOriginData)` → `HRV · ночная синхронизация`
- `Синхронизация: день 0 · пакет 50 из 158` → `Загружаем данные за прошлую ночь...`
- `2230 HRV · RR/resRates: 169 знач.` → `RMSSD: 56 мс · ✓ норма`
- Добавить RMSSD-блок с цветовой зоной (<30 красный, 30-60 жёлтый, >60 зелёный)

- [ ] **Шаг 3: Проверить в браузере**

Открыть каждый из 5+2 экранов. Убедиться: палитра и компоненты выровнены с Kit, нет битых ссылок.

- [ ] **Шаг 4: Закоммитить**

```bash
git add docs_web/wireframes/m1/
git commit -m "Рестайл mobile-pairing M1 под новый UI Kit + чистка дев-жаргона HRV"
git push
```

- [ ] **Шаг 5: Обновить план + PROJECT_STATE**

- [ ] **Шаг 6: Чекпоинт с PM**

---

### Задача 8: Финальная сверка + landing

**Файлы:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/index.html`

- [ ] **Шаг 1: Обновить landing index.html**

Добавить новую секцию «UI Kit + рестайл M2» с карточками:
- UI Kit (ui-kit.html)
- Kiosk v2 (kiosk-v2.html)
- Drill-down (kiosk-drilldown.html)
- Dashboard корпоратов (dashboard-corporate.html)

- [ ] **Шаг 2: Закоммитить и запушить**

```bash
git add docs_web/index.html
git commit -m "Обновил landing: добавил секцию UI Kit + рестайл M2"
git push
```

- [ ] **Шаг 3: Финальная проверка GitPages**

Дождаться деплоя (1-2 мин). Открыть https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/ и пройти по всем новым ссылкам.

- [ ] **Шаг 4: Финальный отчёт PM**

Сводка: что готово, GitPages URL, что осталось open для стыковки 27.05.

- [ ] **Шаг 5: Обновить PROJECT_STATE.md + закоммитить knowledge-base**

Закрыть задачи UX/UI Дизайнера в PROJECT_STATE. Обновить статус агента → ⚫ Idle (готов к следующей задаче).

---

## Self-review

**Покрытие скоупа PM:**
- ✅ UI Kit компоненты — Задача 3
- ✅ Демо-стенд (2 анкера + 1 гость) — Задача 4
- ✅ Drill-down карточка гостя — Задача 5
- ✅ Дашборд корпоратов — Задача 6
- ✅ Приложение паринга (поверх M1) — Задача 7

**Зависимости:**
- Задача 1 (калибровка) блокирует Задачи 3-7 (без палитры и эстетики нельзя стартовать Kit)
- Задача 3 (UI Kit) блокирует Задачи 4-7 (экраны опираются на токены и компоненты Kit)
- Задачи 4, 5, 6, 7 могут идти последовательно (после Задачи 3)
- Задача 8 — финал, после всех

**Чекпоинты:** после каждой Задачи 3-7 — sync с PM перед началом следующей.
