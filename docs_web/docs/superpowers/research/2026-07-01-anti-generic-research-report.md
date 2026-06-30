# Anti-Generic Research — Отчёт

**Дата:** 2026-07-01 · **Метод:** diagnostic-first multi-agent Workflow (15 агентов, ~676K токенов, adversarial-верификация) · **Спрос PM:** опровергнуть критику команды через реальный level-up
**Сырые данные:** `raw/{diag,A,B,C,D,E,F,verification}.json`

---

## 0. TL;DR — главное

1. **Критика команды частично СПРАВЕДЛИВА — и это хорошая новость.** Диагностика подтвердила все 4 пункта конкретными ссылками на наш код. Но причина не «Claude генерит generic», а наши **закреплённые в каноне решения**, которые буквально программируют generic-look (один радиус на всё, hairline-бордеры, wine в навигации, один data-viz примитив ×7, нулевые градиенты). Это значит — **чинится сменой правил, а не сменой инструмента.**

2. **«У нас все крутые скиллы» — верно, но неполно.** Наш арсенал силён (`impeccable`, `redesign-existing-projects`, `high-end-visual-design` прямо бьют по нашим симптомам), но в текущем пайплайне **не вызывается системно**. Плюс есть бесплатные внешние усиления, которых у нас нет.

3. **Verdict по запрошенным скиллам:**
   - **taste** → **БРАТЬ** (методологию импортировать, не устанавливать слепо). Бесплатный MIT.
   - **UX UI Pro Max** → брать **только как вторичный QA/accessibility-слой**, НЕ как лекарство от generic (лечит не те симптомы; premium на паузе, цена скрыта).
   - **Stitch** → **усиливает ПРИ УСЛОВИЯХ** (только композиция-болванка, код выбрасываем, обязательный taste-отбор + Figma-детокс).

4. **Найдено 4 внешних усиления сильнее запрошенных:** Anthropic `frontend-design` (официальный, must-have baseline), `interface-design` (финишный deslop-пасс), `oklch-skill` (точно под боль wine), `ui-craft` (детерминированные гейты — кандидат на ядро).

5. **✅ Два канона — решено PM (01.07):** (а) **wine ВЫНЕСЕН из chrome** (согласовано) — отменяет прежний header/footer-canon; (б) **Pulse Mono ОСТАЁТСЯ — только для цифр**, всё остальное Golos Text (см. §7).

---

## 1. Диагностика — критика подтверждена нашим же кодом

Диагностик-агент открыл `bevel-clone/home/home-main-etalon.html` + `index.html` и сверил с 6 реальными скринами Bevel. Все 4 пункта подтверждены.

| Критика | Severity | Корень проблемы (наш код) | Как у Bevel |
|---|---|---|---|
| **Типовые компоненты** | 🔴 3 | Единственный data-viz примитив `.bv-capsule` (components.css L161-203) отрендерен **7 раз подряд** (hero + 6 bento). Мы изобрели вертикальный термометр, которого у Bevel нет, и размножили. | 5+ разных примитивов: ring-gauge, радиальный циферблат, battery-bar, area-sparkline, stacked severity-bars. |
| **Нарушена композиция** | 🟠 2 | Bento 2×3 из 6 ячеек одинакового веса (122px, padding 14px). Нет доминанты, нет паузы. Заголовок сломан ручным `<br/>` (L557) — сам код в objections-таблице признаёт «недо-вёрстка». | F-композиция с убыванием веса: доминантный ring-блок → prose insight-карта («🔋 Slow and steady energy») → плотная сетка. |
| **Поганый wine #831843** | 🟠 2 | Wine закрашивает **chrome**: активный nav-таб (L739-743), header eyebrow (L452). На cool-grey #F0F0F3 это 4-я несогласованная hue-семья поверх green/orange/red. | Chrome **ахроматичен**: активный таб чёрный, CTA чёрный. Цвет только семантический и **живёт в данных**. Бордового нет нигде. |
| **Не рукотворный** | 🔴 3 | Тотальная униформность: один radius 20px (tokens.css L70 «ОДНО значение»), один border 1px, один shadow, один icon-stroke 1.7. **0 градиентов.** Нет фирменной сигнатуры. objections-таблица системно отклоняет художественные советы скиллов «в пользу канона». | AI-ghost + «Ask Bevel anything» на каждом экране, градиентные дуги колец, area-fill, emoji в insight, объёмные градиентные иконки. У каждого экрана «изюминка». |

**Anti-generic чеклист (12 правил)** — выведен из дельты «наш клон vs Bevel», полный список в `raw/diag.json` и в Playbook. Ключевые: запретить единый радиус; добавить ≥3 не-капсульных viz-примитива; убрать hairline-бордеры (тень вместо обводки); вынести wine из chrome; цвет — только в данных; ритм плотности; фирменная сигнатура; иконки с характером; легализовать градиенты.

---

## 2. Verdict-таблица (с confidence из adversarial-верификации)

| Инструмент | Verdict | Цена/доступ | Confidence | Примечание |
|---|---|---|---|---|
| **taste-skill** (Leonxlnx) | ✅ **БРАТЬ** — методологический каркас №1 | Free, MIT · `npx skills add Leonxlnx/taste-skill` | — | Импортировать SKILL.md-правила в `UI_assets`, НЕ ставить слепо. Override: разрешить 3+ радиуса (его one-radius догма противоречит нашему фиксу). |
| **UX UI Pro Max** (nextlevelbuilder) | ✅ **Установить open-source ядро** как вторичный QA/a11y-слой (не лекарство) | Free MIT, v2.10.0 (29.06.26) · ядро полностью открыто · `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill` → `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill` | medium | Ядро открыто (67 стилей, 161 палитра, 99 UX-guidelines, 25 charts, 161 reasoning-rules). Лечит accessibility/touch/charts — НЕ вкус/душу. Premium (бренд-ассеты) — отдельно, можно игнорировать. |
| **Google Stitch** | 🟡 **Усиливает при условиях** | Free (Labs, ~400/день) · платно ожидается Q4 2026 | medium | Только композиция-болванка; код выбрасываем; обязателен taste-отбор + Figma-детокс. Без условий — производит generic. |
| **Anthropic frontend-design** | ✅ **МАСТХЭВ baseline** | Free, official · 277k+ установок · `/plugin install frontend-design` | **high** | Банит generic-шрифты/градиенты на уровне постановки. Один недостаточен для плотных product-экранов. |
| **interface-design** (Dammyjay93) | ✅ Финишный deslop-пасс | Free · 5.2k⭐ · `npx skills add Dammyjay93/interface-design` | medium | `design-deslop` — diff-scoped срез AI-tells. Гонять перед каждым показом PM. |
| **oklch-skill** | ✅ Точно под боль wine | Free | (часть методологии, high) | Wine #831843 → перцептивная шкала 50-900 без «мути» HSL mid-tones. |
| **ui-craft** (educlopez) | 🟢 **Кандидат на ядро** — испытать | Free · `npx skills add educlopez/ui-craft` | medium (superlative «лучший» оспорен) | Детерминированные гейты (UICraftScore 0-100, tokens_lint), durable brief/tokens против дрейфа бренда. Технически реален; «сильнее всех» — не доказано, испытать. |

---

## 3. Внешние скиллы — детально (Поток A)

### taste-skill — БРАТЬ
- **Что:** open-source «anti-slop» SKILL.md-фреймворк. Цель один-в-один наша: не дать агенту сгенерить generic.
- **Методология (почему силён):** 3 числовых диала `DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY` (1-10); **Brief Inference** (читает «page kind / audience / vibe» до генерации — лекарство от «не рукотворного»); **Anti-Default 5 Tells** (бан AI-purple градиентов, бан Inter по дефолту, **ЗАПРЕТ трёх равных карточек** ← прямо наш симптом); Layout Discipline (3 одинаковых лэйаута подряд = fail); Hard Pre-Flight (66 пунктов).
- **Оговорка:** требует ОДИН радиус и ОДИН accent на проект — **противоречит** нашему фиксу «3+ контекстных радиуса». Берём философию, игнорим one-radius.

### UX UI Pro Max — вторичный QA
- **Что:** searchable база (50+ стилей, 161 палитра, 99 UX-guidelines, 25 типов графиков, 161 reasoning-rule). По сути — справочник корректности/accessibility, не вкуса.
- **Методология:** priority-rules 1→10 (Accessibility → Touch → Performance → Style → Layout → Typography → Animation → Forms → Nav → Charts).
- **Почему не лекарство:** симптомы 2 (композиция) и 4 (рукотворность) почти не закрывает — нет диалов вариативности, нет «no equal cards», нет brief-inference. Premium фактически недоступен (продажи на паузе).

---

## 4. Broad sweep — методология анти-generic (Поток C)

11 принципов оркестрации (полностью в `raw/C.json`), ключевые:

1. **Reference-grounding превыше prose** — не «сделай премиально», а скриншот реального референса (Linear/Vercel/Hume/Bevel) → конкретные токены и правила. Параграф оставляет модели свободу свалиться в дефолт; картинка+токен — нет. **Фикс №1 против всех 4 симптомов.**
2. **Слоёный стек «дешёвое первым»:** frontend-design (банит generic) → durable DESIGN.md+tokens в репо → визуальный референс-anchor → screenshot-loop.
3. **`/shape` (ASCII-wireframe ДО кода)** ломает дефолтную центрированную композицию (симптом #2) до первого div.
4. **Durable-артефакты против дрейфа бренда** — brief.md + tokens живут в репо, перезагружаются каждую сессию. Связать с нашим `tokens.figma.json`.
5. **Двухфазный анти-slop:** генерит один скилл, deslop делает ДРУГОЙ (генератор ≠ ревьюер в одном проходе).
6. **Цвет только в OKLCH** — wine → перцептивная шкала, а не ручной HSL (мутит mid-tones).
7. **Multi-perspective критика** (design-reviewer + a11y-auditor + persona-walkthrough параллельно) — фиксировать НАПРЯЖЕНИЯ, не консенсус.
8. **Scored gates** (UICraftScore / Nielsen) — «кажется generic» → измеримый порог в acceptance-bar.
9. **Tunable dials под тип экрана** — лендинг high-variance, settings/таблицы low-variance+high-density.
10. **Living keep/reject библиотека** с причинами → в наш `lessons-learned.md`.
11. **Hybrid hand-off** — AI генерит скелет, человек добавляет душу (edge/empty/error/loading states — главный tell «не рукотворного»).

---

## 5. Bevel DS — что делает его рукотворным (Поток D, confidence HIGH)

**Типографика:** один гротеск-санс на весь UI (SF Pro-подобный). Hero-числа extra-bold крупные («80.3 ms» ~40-56px), **единица серым тонким рядом**. Секц-заголовки однострочные 22-24px bold БЕЗ uppercase. Eyebrow — единственное место uppercase+трекинг. **Числа НЕ выделены отдельным mono** — крупность и вес делают работу.

**Композиция:** вертикальный ритм с иерархией плотности (не равномерная сетка): дата → статус-пилюли → **доминантный triple-ring** → **prose insight-пауза** → Stress&Energy → battery-bar → bento. Поля ~16-20px, gap между секциями ~28-36px, внутри ~12px.

**Цвет:** chrome **полностью ахроматичен** (#F0F0F4 фон, #FFF карты, near-black текст, **чёрные** active/CTA). Цвет только семантический в данных: тёплая шкала (orange→yellow), коралл/красный (high), зелёный/лайм (recovery), индиго→лаванда (sleep). **1 тёплая + 1 холодная шкала + sleep-индиго. Wine отсутствует.**

**5 техник рукотворности:** (1) богатый viz-словарь (neumorphic ring с градиентной дугой, радиальный циферблат, rainbow line-chart, area-sparkline с normal-range, stacked severity-bars, range-слайдеры); (2) градиенты в дугах и иконках; (3) **фирменная сигнатура** (AI-ghost blob + «Ask Bevel anything» на каждом экране + контекстные мини-пилюли); (4) объёмные градиентные статус-иконки в squircle-таблетках с glow; (5) **варьируемые радиусы и тени без обводок** (карты на диффузной тени `0 8px 24px rgba(0,0,0,.06)`, pill ~24-28px, карта ~20-24px, CTA ~32px).

**Извлечённые токены** → перенесены в Playbook §«Bevel-токены».

---

## 6. Что наш клон растерял (Поток E) + Матрица арсенала (Поток B)

**6 потерь** (формат Bevel → наш клон → fix), полностью в `raw/E.json`. Каждая = прямой actionable-фикс в `components.css`/`tokens.css`. Сведены в Playbook.

**Наш арсенал × симптом** (полностью в `raw/B.json`):
- **`impeccable`** — сильнейший по «не рукотворный»: «AI slop test» (если можно сказать «AI made that» → провал), absolute ban на identical card grids + hero-metric template. Вызов: `Skill impeccable args:"critique <path>"` → `args:"polish <path>"`.
- **`redesign-existing-projects`** — **лучший фит под наш кейс** (существующий код, Scan→Diagnose→Fix). Прямые аудиты: «generic card look → remove border», «more than one accent → pick one, desaturate <80%», «uniform border-radius → vary». Вызов: `Skill redesign-existing-projects args:"audit and fix <files>"`.
- **`high-end-visual-design`** — Variance Mandate, Double-Bezel, ABSOLUTE ZERO banned defaults (1px gray borders, harsh shadows, thick Lucide). Через UX-агента в BRIEF.md.
- **`minimalist-ui`** — двойственный: даёт asymmetric bento, НО «no gradients/shadows» **усугубляет** «не рукотворный». Брать выборочно (типографика+asymmetry), не целиком.
- **`imagegen-frontend-mobile`** — диагностика на стадии концепта + генерация premium-референса.
- **`app-store-screenshots`** — для маркетинга, не in-app.

---

## 7. ✅ Канон — решения PM (01.07.2026, мандат «canon revisable»)

1. **Wine ВЫНЕСЕН из chrome (СОГЛАСОВАНО).** Активный nav-таб / header-eyebrow / CTA → нейтрально-тёмные `--bv-ink`. Wine #831843 остаётся **только** как редкий brand-signal (splash / onboarding / лого). Chrome ахроматичен, цвет живёт в данных. **Отменяет** прежний `project_neiry_bevel_clone_header_footer_canon` (wine-tint pill как brand-anchor) — память обновлена.
2. **Pulse Mono ОСТАЁТСЯ — ТОЛЬКО для цифр (решение PM).** Все числа (значения, время, проценты, ID) — Pulse Mono; **всё остальное Golos Text**, включая единицы измерения, метки строк, заголовки таблиц, body. Сознательная дивергенция от Bevel (он без mono) — наш фирменный приём. **Уточняет** `project_neiry_typography_system`: раньше mono покрывал табличные блоки целиком, теперь — строго цифры.

---

## 8. Confidence-сводка (adversarial-верификация, Поток G)

- **HIGH:** Bevel handcrafted 5 техник; Bevel типографика; frontend-design = официальный must-have baseline. (Скептики проверили против реальных скринов и первоисточников — подтвердилось.)
- **MEDIUM, выжило:** Stitch усиливает-при-условиях (мартовский MCP-апдейт DS-проблему НЕ решил); interface-design design-deslop.
- **MEDIUM, оспорено:** ui-craft «сильнее всех / лучшее ядро» (тех-дифференциал реален, но superlative не доказан → испытать, не короновать); UX UI Pro Max «QA-роль» (скептик сузил пользу ещё больше).
- **1 верификатор упал** (StructuredOutput retry cap) — не критично, остальные 7 валидны.

---

## 9. Что дальше

Этот отчёт питает **Anti-Generic Playbook** (`UI_assets/anti-generic-playbook.md`) — исполнимый 6-стадийный пайплайн. После acceptance PM — фаза **G4: flagship proof-экран** по пайплайну (отдельный запуск).
