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

### Задача 2: Обновить BRIEF.md для UX/UI Дизайнера

**Файлы:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/BRIEF.md`

- [ ] **Шаг 1: Перезаписать BRIEF.md**

Старый бриф (drill-down + Unite v4 + mobile-чистка от 24.05) → новый бриф «M2 UI Restyle: UI Kit + 4 экрана». Включить:
- Скоп Kit (токены + компоненты + био-виджеты)
- Скоп 4 экранов с путями файлов
- Эстетика из Задачи 1
- Запрет: не использовать React/Vue (только HTML + Tailwind CDN)
- Срок: 26.05 вечер (стыковка 27.05)

- [ ] **Шаг 2: Закоммитить**

```bash
git add UI_assets/BRIEF.md
git commit -m "Обновил бриф UX/UI: M2 UI Restyle (UI Kit + 4 экрана, shadcn-эстетика)"
```

- [ ] **Шаг 3: Обновить план**

Отметить чекбоксы Задачи 2.

---

### Задача 3: UI Kit — живой styleguide

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/ui-kit.html`

- [ ] **Шаг 1: Создать ui-kit.html**

Структура страницы:
1. **Tokens** — палитра (semantic CSS-переменные `--background`, `--foreground`, `--primary`, `--accent`, `--muted`, `--success`, `--warning`, `--destructive`), типографика (Manrope/Fraunces/JetBrains Mono с размерами), spacing-scale, радиусы, тени
2. **Base components** (shadcn-style) — Button (5 вариантов: primary, secondary, ghost, outline, destructive + sizes sm/md/lg), Card, Badge, Input, Select, Tabs, Dialog/Sheet, Tooltip, Avatar
3. **Биометрические виджеты** (кастом) — BPM-card (большое число + sparkline), NCI-gauge (полукруг-шкала со светофором 🟢🟡🔴), Status-pill (NORMAL/ELEVATED/RECOVERY), RMSSD-индикатор с цветовой зоной, R-R sparkline (mini-chart), Heartbeat-pulse-animation
4. **Tremor-style виджеты для дашборда** — KPI-card (заголовок + большая цифра + delta + sparkline), BarList (top-N сотрудников), Progress-bar с цветовыми зонами

Каждый компонент с примером использования и кратким описанием «когда применять».

- [ ] **Шаг 2: Проверить в браузере**

Открыть `file:///.../docs_web/wireframes/m2/ui-kit.html`. Проверить:
- Все компоненты рендерятся без ошибок
- Палитра консистентна
- Шрифты подгружаются (Manrope основной, JetBrains Mono для данных)
- Адаптивность 1280px и 1920px

- [ ] **Шаг 3: Закоммитить**

```bash
git add docs_web/wireframes/m2/ui-kit.html
git commit -m "Добавил UI Kit M2: токены + base-компоненты shadcn + био-виджеты + Tremor-стиль для дашборда"
git push
```

- [ ] **Шаг 4: Обновить план + PROJECT_STATE**

Отметить чекбоксы Задачи 3. Добавить ссылку на ui-kit.html в `knowledge-base/PROJECT_STATE.md` (раздел «Артефакты M2»).

- [ ] **Шаг 5: Чекпоинт с PM**

Показать PM ui-kit.html (локально + GitPages URL). Получить feedback. Если есть правки — внести и повторить Шаг 2-3.

---

### Задача 4: Kiosk restyle (2 анкера + 1 гость)

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-v2.html`

- [ ] **Шаг 1: Создать kiosk-v2.html**

Layout (плазма 1920×1080, ландшафт):
- Header: лого Neiry + название «Live Demo» + dev-bar для переключения состояний (IDLE / ACTIVE_2 / ACTIVE_3 / PENDING_CLAIM)
- Main area: **3 карточки в ряд** (два анкера + слот гостя)
  - Каждая карточка: имя/роль (Костя/Алексей/Гость) + большой BPM + NCI-gauge + status-pill + R-R sparkline за 60 сек
  - Слот гостя в IDLE: «Надень браслет, чтобы начать» + анимация ожидания
- Footer: NCI-легенда (🟢 ≤30 / 🟡 31-60 / 🔴 >60) + QR-код для TG-отчёта

Использовать токены и компоненты из ui-kit.html.

- [ ] **Шаг 2: Реализовать 4 состояния через JS-switcher в dev-bar**

IDLE (3 пустых слота) / ACTIVE_2 (2 анкера, гостя нет) / ACTIVE_3 (все 3 активны, fake live BPM) / PENDING_CLAIM (гость закончил → QR-модалка).

- [ ] **Шаг 3: Fake live BPM анимация**

`setInterval` на ±2 BPM каждые 1.5 сек для каждой карточки. Sparkline дорисовывает точки.

- [ ] **Шаг 4: Проверить в браузере**

Открыть kiosk-v2.html. Переключить все 4 состояния. Убедиться:
- BPM «дышит» в ACTIVE_3
- QR-модалка открывается в PENDING_CLAIM
- Нет горизонтального скролла на 1920×1080

- [ ] **Шаг 5: Закоммитить**

```bash
git add docs_web/wireframes/m2/kiosk-v2.html
git commit -m "Добавил kiosk v2: рестайл 2+1, новая эстетика shadcn + fake live BPM"
git push
```

- [ ] **Шаг 6: Обновить план + PROJECT_STATE**

Отметить чекбоксы. Обновить ссылку в PROJECT_STATE и project_neiry_m2_artifacts.md.

- [ ] **Шаг 7: Чекпоинт с PM**

---

### Задача 5: Drill-down карточка гостя + Bayevsky test

**Файлы:**
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m2/kiosk-drilldown.html`

- [ ] **Шаг 1: Создать kiosk-drilldown.html**

Layout (админ-ноут, 1440×900, светлая тема — оговорено в брифе 24.05):
- Top bar: ← back to wall + «Гость #3 · 02:47» (timer от начала сессии)
- **Главный блок NCI** — большое число + NCI-gauge + caption «Когнитивная нагрузка»
- **4 метрики 2×2** — BPM с sparkline / HRV-RMSSD (или «— нет данных») / SpO₂ / Шаги
- **60-сек график BPM** (line chart, SVG inline)
- **CTA «🧪 Запустить Тест Баевского (5 мин)»** — large primary button + caption «3 мин покоя + Stroop + дорожка»
- **Footer:** STOP SESSION → QR/PIN экран

- [ ] **Шаг 2: Добавить 3 фазы Bayevsky test (state-switcher)**

Состояния (переключаются по клику CTA + dev-bar):
- BAYEVSKY_PHASE_1 — «Покой 3 мин»: большой обратный таймер 03:00 → 00:00, инструкция «Стой неподвижно, дыши спокойно», прогресс-полоса
- BAYEVSKY_PHASE_2 — «Stroop 1 мин»: имитация теста (плашка цвета/слова), таймер 01:00
- BAYEVSKY_PHASE_3 — «Беговая дорожка 1 мин»: «Перейди на дорожку, лёгкий бег», таймер 01:00
- BAYEVSKY_RESULT — таблица 3 фаз × значение ИН Баевского + общий вывод (цветовая зона)

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

### Задача 7: Mobile pairing — рестайл

**Файлы:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-splash.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-login.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-registration.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-ble-pairing.html`
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m1/mobile-home.html`

- [ ] **Шаг 1: Применить новую палитру и компоненты UI Kit к 5 mobile-экранам**

In-place edit:
- Заменить старые цвета на CSS-переменные UI Kit
- Заменить кастомные кнопки на компоненты shadcn-стиля
- Применить новый BPM-card и status-pill из Kit на mobile-home

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
