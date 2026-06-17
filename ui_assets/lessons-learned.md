# Lessons Learned — UX/UI Дизайнер

_Читать перед началом каждой сессии._

## Шаблон записи

```
## ГГГГ-ММ-ДД — [Краткое описание]
Проблема: что пошло не так
Правило: что делать по-другому
```

## 2026-05-16 — Всегда использовать палитру из claude.md
Проблема: при создании нового экрана можно случайно использовать стандартные цвета вместо палитры Neiry.
Правило: перед любой вёрсткой открыть таблицу цветов в `claude.md` и скопировать HEX-коды.

## 2026-05-25 — M2 использует НОВЫЙ дизайн-токенный стек (НЕ M1 палитра из claude.md)
Проблема: `claude.md` UI агента содержит палитру M1 (`#0f0e0b` / `#1a1814` / etc.) и пометку «не отклоняться». Для M2 этот hex-набор устарел — мы перешли на shadcn semantic tokens.
Правило для M2+ задач (Kiosk v2, drilldown, UI Kit, dashboard, mobile-restyle):
- **Single source of truth по токенам:** `docs_web/wireframes/m2/ui-kit.html` — открыть в браузере перед стартом
- **Использовать:** semantic CSS-переменные shadcn (`--background` / `--foreground` / `--card` / `--primary` / `--muted` / `--border` / `--success` / `--warning` / `--destructive`)
- **Hex напрямую только** для wine accent `#831843` (Neiry brand)
- **Шрифты M2:** Space Grotesk (UI) + Onest 700 letter-spacing -0.02em (hero-числа) + Geist Mono (data, session-ID, метки)
- **M1 палитра в `claude.md`** = legacy, использовать ТОЛЬКО для in-place правок старых mobile-* экранов M1

## 2026-05-25 — pathLength=100 для всех SVG-gauge (точная математика процентов)
Проблема: на NCI-gauge в Kiosk v2 stroke-dasharray не совпадал с целевым процентом из-за вычисления окружности по `2πr`.
Правило: на всех `<circle>` и `<path>` для gauge-визуализаций ставить `pathLength="100"`. Тогда `stroke-dasharray="42 100"` = ровно 42%, без вычислений радиуса.

## 2026-05-25 — Все числовые данные через `font-variant-numeric: tabular-nums`
Проблема: при анимации BPM/NSI числа «прыгают» по горизонтали — пропорциональные цифры разной ширины.
Правило: на каждом блоке с live-числом (BPM hero, NSI hero, таймеры, ИН Баевского) добавлять `font-variant-numeric: tabular-nums`. Числа стоят на месте при смене значения.

## 2026-05-25 — Dev-bar = плашка СНИЗУ на всю ширину (НЕ сверху)
Проблема: легко перепутать dev-bar с верхним header'ом — потерять полезную высоту экрана.
Правило: dev-bar всегда снизу, на всю ширину, полупрозрачная плашка `bg-card/80 backdrop-blur-sm border-t border-border`. Состав: state-pills + back-кнопка слева + STATE-индикатор справа. Референс структуры: `docs_web/wireframes/m2/kiosk-v2.html`.

## 2026-05-25 — Proof-screenshot обязателен перед DONE
Проблема: легко отправить «готово» по тому, что код собран, без проверки в браузере. Потом всплывает overflow, кривые шрифты, сломанные SVG.
Правило: перед `DONE / DONE_WITH_CONCERNS`:
1. Открыть файл в Chrome на 1920×1080 (или DevTools toolbar)
2. Прогнать **все** state-pills из dev-bar — каждое состояние визуально не сломано
3. Сделать скриншоты ключевых состояний
4. Арифметически проверить размеры viewBox / pixel-grid (кратно 4px)
5. **Перечислить непроверенное** в отчёте если что-то не успел

## 2026-05-25 — PM acceptance gate (задача НЕ закрывается без явного «принято»)
Проблема: писал «готово» на основе спецификации/code-review — а PM ещё не проверил визуально.
Правило: после реализации:
1. Запушить ветку с коммитом
2. Дать PM ссылку GitPages (деплоится 1-2 мин)
3. Доложить в формате `DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED` + перечислить что проверено и что НЕ проверено
4. **Ждать явного «принято» от PM** — НЕ начинать следующую задачу
5. spec-review и code-review ≠ acceptance — это технические проверки, финальное решение всегда за PM

## 2026-05-25 — Отступы и размеры кратны 4px
Проблема: «на глаз» поставленные padding/margin (например, 18px, 22px) ломают визуальный ритм.
Правило: все отступы и размеры — кратны 4px (Tailwind spacing scale: 4/8/12/16/20/24/32/40/48/64/80). Если нужно 22px — поставь 24px и проверь, не сломалось ли.

## 2026-05-27 — Source-of-truth для kiosk-палитры = kiosk-v2.html (R5 lessons)
Проблема: при создании drilldown-экрана в R1 я скопировал «похожую» shadcn-палитру вместо точной копии из kiosk-v2 — токены `--card`, `--primary`, `--success`, `--warning` разъехались по lightness/hue на 2-5 пунктов. По отдельности микро, вместе создают «прыжок» при переходе kiosk-v2 → drilldown на одной плазме.
Правило: для всех kiosk-уровней (kiosk-v2, kiosk-drilldown, future m3/dashboard-corporate) единый источник правды = `docs_web/wireframes/m2/kiosk-v2.html`. Перед стартом kiosk-задачи копировать 1:1: блок `:root` (палитра + type-scale переменные `--t-*`) + helper-классы `.t-*` + header pattern `shrink-0 h-[86px] px-10` с SVG-логотипом neiry. НЕ переписывать «по памяти», НЕ адаптировать «чуть-чуть для своего экрана».

## 2026-05-27 — main overflow в kiosk = flex-1 min-h-0, не height calc (R5 lessons)
Проблема: в drilldown я задал `.main-content { height: calc(1080px - 64px) }` с magic-числом высоты header. При смене header на 86px main всё ещё рассчитывал высоту от 64px — empty-state Bayevsky плитка выходила за низ stage на 1512×945.
Правило: внутри `#kiosk-stage` все секции используют flex-семантику: header/banner = `shrink-0`, main = `flex-1 min-h-0 overflow-hidden`. Никаких `height: calc(VIEWPORT - HEADER_HEIGHT)` — height пересчитается автоматически при смене размеров header. min-h-0 обязателен (без него flex-child игнорирует overflow children).

## 2026-06-14 — Phone-mockups PM-у только в transparent PNG (незыблемое правило)
Проблема: на двух итерациях flow-плаката композитный PNG (несколько phones в одном файле) показывал «слипшиеся» экраны без чётких границ. Также PNG с light-фоном создавал двойную карточку (card-in-card) при размещении на bevel-tone плакате — критическое замечание `impeccable critique`.
Правило (zero-tolerance): когда PM просит phone-mockups для плаката/презентации/документа — **каждый экран = отдельный transparent PNG (RGBA с alpha=0 углами)**, содержащий ТОЛЬКО phone-bezel + интерфейс. Никакой подложки, никакого page-chrome (page-title / .page-sub / frame-caption), никакого outer drop-shadow.

**Эталонный скрипт slicing** (Python markup-parsing — НЕ JS-injection): `/tmp/slice_phones_transparent.py`. Алгоритм:
1. Найти все `<div class="frame-with-caption">` или `<div class="frame-wrap">` blocks через regex+brace-tracking (поддержка вложенных div).
2. Surgically удалить все блоки кроме target_idx — html переменная с одним оставшимся frame.
3. CSS-injection перед `</head>`:
   - `html, body { background: transparent !important; }`
   - `.page-title, .page-sub, .frame-caption, body > h1/h2/p/header, .footer, .meta-bar { display: none !important; }`
   - `.frames-row, .frames-strip { display: flex; justify-content: center; width: 460px; height: 920px; padding: 0; overflow: visible; scroll-snap-type: none !important; }`
   - `.device-frame { box-shadow: 0 0 0 10px #1a1814, 0 0 0 11px #2a2620 !important; }` — keep ONLY bezel rings, REMOVE outer drop-shadow.
4. Headless Chrome: `--default-background-color=00000000 --window-size=460,920 --screenshot=out.png file://...html`.
5. Verify alpha: Python PIL `img.getpixel((0,0)) == (0,0,0,0)`.

**Эталонная папка качества:** `UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/` — 14 phones из Ф1.

**Anti-patterns (НЕ делать):**
- ❌ Composite-PNG нескольких phones в одном файле (слипание блоков на плакате)
- ❌ White card-wrapper в plakat вокруг phone (card-in-card → critique flag)
- ❌ Outer drop-shadow на bezel в самом PNG (компонуется на стороне layout если нужна)
- ❌ Видимые .page-sub / .page-title / footer-meta в screenshot'е

## 2026-06-14 — Fall detection A4 (хронология + dark-glass contrast)

### Проблема 1 — Хронологический баг status-bar
При создании flow «push на lock screen → opened in-app» легко поставить одно и то же время в status-bar обоих phones (9:42 / 9:42) при тексте «3 минуты назад» в in-app alert. Это **внутренняя нестыковка хронологии** — критику ловит на раз.

**Правило:** для любого многоэкранного flow с относительными метками («3 минуты назад», «N секунд назад») — status-bar следующего экрана = status-bar предыдущего + delta. Push @ 9:42 → opened in 3 min → status-bar 9:45 + sub-text «3 минуты назад». Каждое относительное время — это **constraint на следующий status-bar**.

### Проблема 2 — Wine `#831843` НЕ работает на dark glass push card
Pure wine `#831843` на `rgba(40, 40, 42, 0.78)` имеет contrast < 4.5:1 — не проходит AA для text. Использовать pure wine в push-action нельзя.

**Правило:** для action labels на dark frosted glass (iOS lock-screen pattern) — wine-tinted-light `#f9a8c5` (~7.5:1, AA+ для small text). Сохраняет «winenes» бренда, читается на любой dark backdrop. **Любой brand color на dark glass нужно ВСЕГДА проверять contrast** — не предполагать что «бренд = можно».

### Проблема 3 — Alert-color overload (color fatigue)
В alert-banner с destructive-red фоном + warning-orange stat values + warning-orange mini-row HRV icon + warning-orange HRV value создаётся «всё кричит одним цветом» — eye теряет hierarchy. Critique flag: «multiple severity peaks on one screen».

**Правило color-coding hierarchy (зафиксировать):**
1. **Один severity peak per screen** — топ-level severity (e.g. destructive red в banner-eyebrow + title + CTA + border).
2. **Intermediate metrics** в alert-orange `#d97706` — только в **values**, иконки и labels оставляем muted.
3. **Positive states (success green)** — точечно, маленькими dots, не блок цвета. На alert-screen зелёный — это «оазис спокойствия», должен быть minimal.
4. Если на одном экране 3+ alert-color чанков (red title + orange stat + orange row + orange value), последовательно депрессировать второстепенные: row-icon → muted, stat-icon → muted, оставить цвет только в самом значении.

### Проблема 4 — Lock-screen flat vs gradient depth
Pure `#1c1c1e` flat фон на lock-screen выглядит плоско, ненатурально для iOS 17+ depth-aware backgrounds.

**Правило:** для lock-screen mockup — лёгкий radial-gradient от верх-центра `#2a2a2e` → `#1c1c1e` → углы `#131315`. Это симулирует iOS depth без необходимости photo-blur placeholder. **Без depth — лочный экран читается как «выключенный»**, а нам нужен «лочный включённый с push».

## 2026-06-14 — iOS notification stack: порядок по ВРЕМЕНИ, не по priority
Проблема: при моделировании множественных уведомлений на iOS lock-screen легко поставить «важное» (Neiry Pulse alert о падении) сверху, а второстепенное (missed call) — снизу, по subjective priority дизайнера. Это **неверно** — iOS складывает notifications по chronological order, не по app-priority.

**Правило:** native iOS lock-screen stack:
- **Сверху** — более старое (earlier timestamp). Внизу — самое недавнее (recent).
- Если в Ф1 при детекции падения произошли два события (GBand «звонок из коробки» 9:41 → push Neiry Pulse 9:42), на lock-screen:
  - `[ Telephone · Папа · 9:41 ]` — выше (старше)
  - `[ Neiry Pulse · alert · 9:42 ]` — ниже (новее, ближе к нижнему краю экрана)
- App-priority НЕ перетасовывает порядок — `severity ≠ visual position`. Если хочется приоритезировать визуально — это делается через **expanded preview** (расширенная карточка для самого приоритетного notification), но stack-order остаётся хронологическим.

**Следствие для frosted-bg consistency:** оба cards используют ТОТ ЖЕ frosted bg `rgba(40,40,42,0.78)` — не выделять «важное» отдельным цветом. iOS-native pattern = единый glass effect, разница в семантике передаётся icon-color (зелёный telephone vs wine Neiry icon) и payload (Title + body), не background.

**Следствие для GBand integration:** на любом mockup Ф1 fall-event-flow на стороне опекуна сначала показываем missed call (GBand direct call — PRD v2.6 §3 / R-017 alt), потом push с деталями. Без missed call card flow читается неполно — опекун не понимает, что «звонок из коробки» вообще был.

## 2026-06-14 — Empty states A5: «calibrating» Home empty ≠ standalone Calibrating screen

Проблема: при делегировании Home first-run empty естественно скопировать большой calibration hero (112px rotating ring + status rows + support-list) из `mobile-onboarding-03-notifications-calibrating-v0.html`. Это даёт ощущение «отдельный standalone calibrating screen», а не Home в feed-формате.

**Правило:** Home empty — это **по-прежнему Home** с feed-карточками, не standalone calibrating screen. Calibration hero должен быть **одной из card'ов в feed**, не whole-screen. Конкретные параметры:
- **Ring 68px** (НЕ 112px standalone) — inline с текстом, slimmer presence
- **Layout row-style** (ring слева + текст справа), НЕ centered column
- **БЕЗ status rows про «батарея 87% / собрано 14ч 32м»** — это бэк-данные standalone screen
- **БЕЗ support-list (3 tips «носите 24/7 / спите с ним»)** — это уже было в onboarding-03, не дублируем
- **С progress-bar + footer «12 ч / 48 ч собрано» + text-link** — компактно, для signature калибровки
- Под этой card идут другие feed-cards (stats-row, training, HS preview) — Home продолжается, не обрывается

Иначе экран читается как «Calibrating Mode replaced Home», а нам нужно «Home работает, но без данных пока».

## 2026-06-14 — Empty SVG illustration: 3 правила против stock-feel

Проблема: empty-state illustration легко скатывается в stock-look (символический человечек + heart-emoji) или в overly-cute geometric (3 circles + smile). Bevel-tone palette даёт мало hex'ов для tonal variation, поэтому illustration выходит «mono-color stamp».

**Правило для SVG empty illustrations (bevel + wine):**
1. **Tonal asymmetry** — никогда не делать все объекты одного цвета. Для bevel: разносить figures по 3 уровням opacity/tone (`#d4cfc0` → `#c8c1b0` → `#a8a094` для background → mid → foreground). Это создаёт depth без 3D-rendering.
2. **Size asymmetry** — центральная фигура заметно больше (×1.4-1.6) чем фланговые. Симметрия одинаковых фигур = «штамп».
3. **Wine accent ровно один** — pulse-node / connection-line / glyph, не размазывать wine по нескольким элементам. Один accent = focal point; два accent'a → конкурируют, теряют semantic load.

**Анти-pattern:** ECG-path с zigzag-углами без curve (тип ломаной): выглядит «sharp/cartoon». Использовать cubic-Bezier или mix straight + curve для organic feel.

**Aria:** SVG illustration в empty-state обязательно `role="img" + aria-label="осмысленное описание"` — screen-reader user поймёт что показано вместо «image».

## 2026-06-14 — Stat-widget em-dash placeholder: «calibrating» vs «broken»

Проблема: em-dash `—` placeholder в stat-widget без visual cue считывается как «сломано» / «no data ever» / «device offline». На empty Home это критично — пользователь только что купил продукт, любая неоднозначность = «зачем я заплатил».

**Правило:** для em-dash placeholder, когда данные **ещё калибруются** (НЕ permanently missing):
- Color: `var(--border-strong)` (не полный grey, не полный foreground — visually quiet but not «failed»)
- **Subtle infinite opacity pulse** 2.4s ease-in-out (0.5 ↔ 1.0) — signals «system is alive, data is coming». Wrap в `prefers-reduced-motion: reduce`.
- Обязательный `.stat-sub` под em-dash объясняющий **когда** появятся данные: «Собираем данные», «После первой ночи», «через 24 часа». Без этого пользователь не знает таймайн.
- Для **валидного нуля** (шаги: пользователь буквально не двигался) — НЕ placeholder color, foreground 100%, без pulse animation. 0 шагов = реальное «0», а не «—».

Различие placeholder vs valid-zero load-bearing для UX: первое говорит «мы калибруемся», второе говорит «ваш результат сегодня».

## 2026-06-14 (Revision 1) — Empty state widget layout = mirror of loaded layout

Проблема: первая итерация empty Home f1 положила 3 widget'а (HRV / Шаги / Сон) в `grid grid-cols-3`. В реальном loaded Home f1 widget'ы стоят stacked full-width одна под другой. PM сразу заметил inconsistency: «empty layout отличается от loaded → grid даёт мелкий текст, плохо читается».

**Правило:** **empty state widget layout НИКОГДА не должен отличаться от loaded-варианта.** Если в loaded используются stacked-cards, в empty тоже stacked (только value заменён на placeholder контент: `—` + «Собираем данные»). Если loaded — 2-колонный, empty 2-колонный. Если grid — grid.

Почему: пользователь, который сегодня видит empty, завтра увидит loaded. Если layout прыгает (grid → stack), это разрыв ментальной модели и UX-шок «приложение перестроилось без меня».

Mechanical check: открыть loaded-варианты feed-карточек, выписать grammar (stack/grid/dimensions/padding), точно повторить в empty с заменой только value-content. НЕ изобретать новый layout для empty.

## 2026-06-14 (Revision 2) — Tab-bar требует явный padding-bottom на body выше его

Проблема: при `position: absolute; bottom: 0; height: 76px` tab-bar накладывается поверх content-area внутри device-frame. Если внутренний body (`.hs-body` / `.feed` / любой scroll-container) имеет `padding-bottom < 76 + comfort_gap`, нижний контент (CTA, последняя card, footer-link) визуально упирается в tab-bar или обрезается.

**Правило:** для ЛЮБОГО scroll-container внутри device-frame с tab-bar (position:absolute):
- `padding-bottom: 100px` (= tab-bar height 76px + 24px breathing gap)
- НЕ полагаться на `flex-spacer` или `padding-bottom: 24px` — это не учитывает tab-bar overlap
- Если меняется tab-bar height — обновить ВСЕ scroll-container padding-bottom одновременно (mechanical: grep по `padding.*bottom` или `padding: .* .* (Xpx)` где X < tab-bar.height + 24)

Mechanical check: открыть screenshot, измерить расстояние bottom-edge последнего CTA до top-edge tab-bar. Должно быть ≥ 16px (минимум для touch target separation). Если меньше — фикс padding-bottom.

## 2026-06-14 (Revision 2) — Flex spacer без max-height = «дыра» в empty state

Проблема: `flex: 1; min-height: 12px` без `max-height` на промежуточном spacer'е растягивается на ВСЁ свободное пространство в flex-column container'е. В empty state, где content (illustration + heading + sub + bullets) занимает только ~50% screen height, spacer создаёт 200-300px «дыру» между bullets и CTA — выглядит как «не дозалитая страница».

**Правило для flex-spacer'ов в empty/sparse layouts:**
- `flex: 0 1 32px; min-height: 12px; max-height: 40px` — ограниченный spacer, не растягивающийся бесконечно
- ИЛИ удалить spacer и использовать `margin-top: auto` на CTA-block — flex-magic прижмёт CTA к bottom без визуального вакуума
- Лучше второй вариант (margin-top:auto) — он более идиоматичен для flex и не вводит дополнительный DOM-node

Visual heuristic: если в empty state между content-mass и action-CTA visible gap > 120px (на 844px screen) — что-то с layout. Либо content слишком short и нужно добавить mid-element, либо spacer/flex-distribution ломается.

## 2026-06-14 (Revision 2) — Slicing-script с inject CSS ломает single-phone layout

Проблема: `UI_assets/skills/scripts/slice_phones_transparent.py` для transparent PNG делал агрессивный inject CSS, который менял `.frames-row` display/dimensions и затрагивал внутреннюю геометрию `.hs-body` / `.device-frame`. Это **ломало visual layout** одиночного phone — CTA выезжал за bezel или обрезался tab-bar'ом, хотя в side-by-side render тот же HTML рендерился корректно.

**Правило:** для **proof PNG** (визуальное подтверждение для PM на flow-overview) — НЕ использовать slicing single-phone через layout-breaking inject CSS. Вместо этого:
1. **Side-by-side render оригинального HTML** через chrome --headless --window-size=1280,1100 — layout не ломается, всё рендерится как в браузере
2. **Crop из side-by-side через PIL** — detect bezel columns/rows по dark-pixel scan, crop phone1 и phone2 в отдельные PNG
3. Этот подход даёт ground-truth для визуального ревью

Для **transparent PNG** (для composition на плакате/презентации) можно продолжать использовать inject CSS, НО:
- НЕ менять `.hs-body`, `.feed`, `.tabbar`, `.frames-row` внутренней геометрии
- Менять ТОЛЬКО outer chrome (background transparent, .page-title display:none, frame-caption display:none, hide N-th frame-with-caption)
- НЕ менять box-shadow device-frame radically (можно убрать outer drop-shadow, оставить bezel rings)

**Anti-pattern:** inject `.frames-row { width: 460px; height: 920px; padding: 0; overflow: visible; scroll-snap-type: none !important }` — это ломает реальный layout, особенно если `.frames-row` влияет на inner flex-distribution.

Эталонный safe inject (Revision 2):
```html
<style>
html, body { background: transparent !important; }
.page-chrome { background: transparent !important; padding: 0 !important; min-height: auto !important; gap: 0 !important; }
.page-title, .frame-caption { display: none !important; }
.frames-row { display: flex !important; gap: 0 !important; padding: 16px !important; justify-content: flex-start !important; }
.frame-with-caption:nth-of-type(2) { display: none !important; }  /* hide other phone */
.frame-with-caption { gap: 0 !important; }
.device-frame { box-shadow: 0 0 0 10px #1a1814, 0 0 0 11px #2a2620 !important; }  /* keep ONLY bezel rings */
</style>
```

**Scripts:** `/tmp/render_a5_transparent.py` — эталонный safe transparent slicing. `/tmp/crop_a5_r2.py` — эталонный proof PNG crop из side-by-side.

## 2026-06-14 (Revision 1) — Tab-bar = single source of truth, retroactive фиксы обязательны

Проблема: новые экраны (Health Sharing E2E + Empty States) ввели 4-tab bar «Дом / История / Health Sharing / Ещё». Старый `mobile-home-f1-v0.html` (Ф1 baseline) до сих пор имел 4-tab «Главная / Тренировка / История / Ещё» — БЕЗ HS вкладки. Получалась inconsistency: пользователь на Home не видел HS-tab, потом на HS-screen видел tab-bar с HS active, на других screens обратно tab-bar разный.

**Правило:** tab-bar — **single source of truth для ВСЕХ Ф1 screens**. Когда вводится новый tab (как HS появился позже Home f1):
1. Найти ВСЕ screens с tab-bar grep'ом `class="tabbar"` или `nav .*tab`
2. Обновить tab-bar блок в каждом файле (footer/bottom-nav) одновременно с новой фичей — НЕ откладывать
3. Сохранить визуальную грамматику: те же иконки SVG, те же label'ы, те же size, тот же active-state wine
4. **Не трогать логику screens** — менять ТОЛЬКО tab-bar block, остальное оставлять как есть
5. Если есть «modal/flow» screens без tab-bar (training-start, training-active, onboarding 01-04) — это OK, не добавлять им tab-bar

Retroactive cleanup НЕ опционален — каждая inconsistency в tab-bar = сломанная навигация в восприятии пользователя.

В этой итерации обновлён `mobile-home-f1-v0.html` (последний файл без HS-tab). Остальные Ф1 mobile файлы уже унифицированы.

## 2026-06-15 — Alert-banner stacking pattern: stale-data state требует cascade muted

Проблема: при BT-disconnect banner естественно muted'ить только HRV-card (метрика «о которой banner»), а Шаги/Сон оставить foreground. Это логически неверно — шагомер тоже на браслете, значит при disconnect все live-метрики с браслета заморожены. Sleep — единственный «исторический» виджет (вчерашняя ночь, уже синхронизировано).

**Правило для stale-state cascade на disconnect-banner экранах:**
1. **Выявить источник live-данных каждого виджета** — что приходит с браслета прямо сейчас (HRV, Шаги, Heart Rate, Activity Zones), что уже синхронизировано как история (Sleep прошлой ночи, последние workouts).
2. **Все live-source виджеты идут в `is-stale`** state: muted value (`var(--border-strong)` weight 500), muted progress bar, sub-метка «до HH:MM» в alert-orange-strong (`#b45309`), card-bg warm (`var(--card-warm)`).
3. **Исторические виджеты остаются foreground** — Sleep вчерашней ночи валидно даже если браслет ушёл сейчас.
4. **Stale-marker (clock 16px top-right)** — только на head-метрике, к которой банер референяит. На остальных stale-cards достаточно muted-value + warm-bg. Два clock-маркера = visual clutter.
5. **Stale-strip над cards** (orange dot + uppercase mono «ПОСЛЕДНИЕ ДАННЫЕ · 9:48 (2 МИН НАЗАД)») — explicit timestamp boundary между «alive» и «frozen» зоной feed.

Иначе пользователь видит «HRV сломан, остальное норм» — а в реальности всё, что live с браслета, заморожено. Frosen-data UX-cue должен быть консистентным.

## 2026-06-15 — Snooze pattern для charging-low: «Напомнить через N ч» вместо dismiss

Проблема: на charging-low warning естественно дать secondary CTA «Скрыть» / «Понятно». Это permanent dismiss — banner исчезает, пользователь забыл, ночью браслет разрядился, утром нет HRV → upset.

**Правило для non-critical reminder banners (charging-low, app-update available, sync-pending):**
1. Primary CTA — actionable («Как зарядить?» / «Обновить» / «Синхронизировать»).
2. Secondary CTA — `snooze` с конкретным интервалом («Напомнить через 1 ч»), НЕ permanent dismiss («Скрыть» / «Игнорировать»).
3. Время snooze — context-aware: для charging «1 ч» = мягко, для critical «15 мин» = настойчиво.
4. Permanent dismiss разрешён ТОЛЬКО для информационных banners (notifications-onboarding-tip), где non-action consequence близка к нулю.

UX-следствие: snooze сохраняет состояние «надо что-то сделать» в сознании пользователя без раздражения. Permanent dismiss = «я обещаю не показать опять» — продукт не должен давать такого обещания для metric-affecting состояний.

## 2026-06-15 — Frozen-state visualHints: cascade muted на ВСЕХ live-source compontents

Проблема: при auto-pause естественно muted'ить только hero-метрику (HR 156 в Phone 2) — но Zone chip, meta-cells (км/мин-км/ккал), zones-strip остаются foreground. Это разлад: «HR заморожен, но зоны живые?» — пользователь не понимает state model.

**Правило для frozen overlays (auto-pause, manual pause):**
1. **Все live-source children идут в `is-frozen`** state одновременно: hero number (`var(--border-strong)`), zone chip (тот же tone), meta-cells .v values muted.
2. **Zones-strip** также cascade: bg остаётся `var(--zone-inactive)`, active cell становится `var(--border-strong)` вместо `var(--primary)`. Это сохраняет zone-visual hierarchy (Z3 ещё «active») но без яркого wine.
3. **Eyebrow label обновляется**: «Пульс» → «Пульс · заморожен» — explicit textual cue для screen-readers + visual reinforcement.
4. **Анимация stop**: hr-pulse animation: none на is-frozen, иначе цвет muted, но scale всё ещё качает — confusing.

GPS lost — частный случай (только distance frozen, HR alive). Тут cascade применяется selectively: bottom-strip distance muted + PAUSED tag, pace muted («last» tag), HR live wine. Zones-strip остаётся foreground (HR-zones продолжают апдейтиться).

Mechanical check: выписать список «что приходит с браслета прямо сейчас» (HR, zones, активность) vs «что заморожено» (distance/pace/cals при pause; distance при GPS lost). Все frozen-source — `is-frozen`. Все alive-source — foreground.

## 2026-06-15 — Modal overlay stacking inside device-frame (z-index hierarchy)

Проблема: при создании overlay (dim-overlay, bottom-sheet) внутри `.page-content` который сам `flex: 1; overflow: hidden`, overlay'и могут (а) обрезаться по `.page-content` границе, не покрывая app-bar + zones-strip, или (б) выезжать за device-frame если положить их absolute в `.device-frame` напрямую.

**Правило stacking для overlays внутри device-frame:**
1. **Dim overlay (modal STOP):** позиционируется внутри `.page-content` с `position: absolute; inset: 0; z-index: 30`. Это покрывает ровно page content area (между app-bar и zones-strip) — app-bar и zones-strip остаются seen-but-disabled. Логично: STOP confirm живёт «над» текущей страницей, app-bar остаётся как контекст.
2. **Bottom-sheet (Auto-pause):** аналогично внутри `.page-content`, `position: absolute; left/right/bottom: 0; z-index: 25`. Sheet поднимается из низа page-content, не закрывая app-bar и не выезжая за zones-strip (которая sticks внизу).
3. **Banner (GPS lost):** flex-child между `.app-bar-active` и `.pagination`, не overlay. Sticky-feel за счёт `flex-shrink: 0` и `border-bottom: 1px solid warning-border`.

Mechanical check: после render каждого overlay открыть screenshot:
- Status bar visible вверху?
- App-bar visible (тёмная плашка app-bar-active)?
- Overlay/sheet НЕ выходит за device-frame border-radius 44px?
- Zones-strip visible (для overlay'ев которые сидят в page-content, иначе hidden)?

Если overlay должен покрыть app-bar (полноэкранный takeover) — тогда `position: absolute` относительно `.device-frame` с `z-index: 50` (выше device-notch). Но это redesign pattern, не «overlay над страницей».

## 2026-06-15 — 3-phone side-by-side render — coordinates для crop из 1900×1100

Проблема: при side-by-side render 3 phones (window-size 1900×1100) bezel-detection через простой `dark_col_mask` склеивает все 3 phones в один column-range, потому что outer drop-shadow + close gap (frames-row gap: 48px) даёт continuous dark pixels между phones.

**Правило crop'а для 3+ phone side-by-side:**
1. **Threshold dark должен быть строгий** (`<50`, не `<70`) — иначе drop-shadow считается bezel.
2. **Gap-merge должен быть малым** (`<12px`, не `<40px`) — крупный merge склеит phones.
3. **Если всё равно склеилось** (один widerange > 600px), применить **split_if_needed**: внутри range искать low-density column-gaps (>=14 consecutive non-dark) и резать по midpoints.
4. **Padding 18-24px** вокруг bezel — иначе drop-shadow обрезается.

Эталонный скрипт: `/tmp/crop_b3_phones.py` (3-phone) — работает на render 1900×1100, каждый phone ~412×866 + padding. Detected phones get crop'нуты в 448×902 файлы.

Coordinates 3-phone-side-by-side render (1900×1100, padding 16):
- Phone 1: x ~306-717
- Phone 2: x ~744-1155
- Phone 3: x ~1182-1593
- Y range: 96-961 (включая device-notch)

Этот ground-truth можно переиспользовать для будущих 3-phone сетов.

## 2026-06-14 (Revision 2 hotfix) — Header = single source of truth между empty и loaded variants

Проблема: при создании empty-state экрана `mobile-onboarding-05-empty-states-v0.html` я **пересоздал app-bar markup с нуля**, копируя только видимую часть DOM из `mobile-home-f1-v0.html` (logo SVG + button'ы), НО **забыл подключить `<script src="https://cdn.tailwindcss.com"></script>`** в `<head>`. Markup app-bar использует Tailwind-классы (`flex items-center gap-2`, `w-9 h-9`, `rounded-full`, `bg-stone-200`, `hover:bg-stone-100`) — без runtime'а они мёртвые. Результат: logo не центровался вертикально (flexbox не работал), icon-buttons выглядели как «коробки с border» (нет round + размер + bg). PM это поймал на финальном ревью A5.

**Правило:** для любой empty/loading/error variant существующего экрана header **= byte-for-byte копия canonical**, включая runtime-зависимости (Tailwind CDN, иконочные библиотеки, шрифты). Чеклист при создании variant'а:

1. **Открыть canonical** (`mobile-home-f1-v0.html` для Home variants, `mobile-history-v0.html` для History variants и т.д.) — это source of truth
2. **Скопировать весь `<head>`** новому файлу (Tailwind CDN, `<link>` шрифтов, `<link>` иконок) — НЕ только относящиеся к header'у строки, потому что header может зависеть от любой из них через классы Tailwind
3. **Скопировать app-bar блок целиком** — каждый класс, каждый aria-label, каждый inline-style. Не «перепечатывать», а буквально copy-paste
4. **Проверка** в браузере: открыть variant и canonical рядом на одинаковой ширине, сравнить header pixel-perfect (или хотя бы скриншоты overlay'нуть)
5. Если canonical обновился (новый avatar style, иной icon-bell) — синхронизировать ВСЕ variants одновременно (как Tab-bar single source of truth)

**Альтернатива:** если Tailwind не нужен в variant'е (только кастомный CSS) — дублировать все эффективные стили app-bar в `<style>` (`.app-bar > div { display:flex; align-items:center; gap:8px }`, `.icon-btn { width:36px; height:36px; border-radius:50%; ... }`). Но это удваивает работу — проще подключить Tailwind CDN.

Урок шире: **никогда не пересоздавай повторно используемый блок с нуля. Копируй markup + runtime + CSS из canonical**. Это применимо к header'у, tab-bar'у, dev-bar'у, card'ам с типовой структурой.

## 2026-06-15 — Глиф `·` в Onest font fallback'ится на emoji в Chrome (B4 end-of-session)

Проблема: в hero-sub строке «Бег · 14 июня, 9:53» character `·` (U+00B7 MIDDLE DOT) внутри `<span>` без explicit font-family наследует `font-family: 'Onest', sans-serif` (от родителя .end-hero-sub). Onest не содержит глиф для U+00B7 → Chrome fallback'ит на Apple Color Emoji font → рендерится как пустой grey balloon-like glyph 14×14px. Critique-flag.

**Правило для middot separator в multilingual headlines:**
1. **Всегда оборачивать `·` в `<span class="dot">` с explicit `font-family: 'Space Grotesk', sans-serif` или `'Geist Mono'`** — оба фонта содержат U+00B7 корректно.
2. **Size — explicit (10-14px) + `color: var(--border-strong)` или muted-foreground** — middot никогда не претендует на семантику, это только разделитель.
3. **Альтернатива:** использовать обычный `bullet •` (U+2022) с тем же подходом — но у `•` ниже частотность в русскоязычных subs, придётся объяснять глаз.
4. **Mechanical check:** после render открыть screenshot, найти middot-separator в headline. Если выглядит как балон, эмодзи, толстая точка или вертикальная палочка — точно font-fallback. Если subtle middot между словами на baseline — OK.

**Anti-pattern:** наследовать font-family от Onest hero parent — почти любой Onest mockup с separator middot будет страдать от emoji-fallback в Chrome. Это **системный** баг pre-existing в Onest font file, не локальный.

Применимо ко всем future mockups с inline middot: home meta-bar, history-row meta, settings-row meta, training session-meta.

## 2026-06-15 — Frozen HR ≠ Frozen Zones (bracelet vs auto-pause)

Проблема: В B3 (auto-pause) все live-source данные frozen — HR + zones + meta + zone-chip. В B4 (bracelet disconnect) только HR-source данных frozen — GPS/time/cals продолжают писаться. Naive cascade «всё frozen» неверен — он коммуницирует «тренировка на паузе», а юзер не понимает почему он продолжает бежать а UI «остановился».

**Правило: cascade frozen зависит от data source, не от event severity:**
1. **Bracelet disconnect (HR-source потерян, GPS работает):**
   - Frozen: HR-value, Z-zones chip (live zone = HR-based), zones-strip active cell
   - Live: км (GPS), pace (GPS-derived), cals (time+motion-derived), timer
   - Banner messaging: «Пульс не обновляется. Время, дистанция и калории продолжают писаться» — explicit user-mental-model alignment
2. **GPS lost (location потерян, HR работает):**
   - Frozen: км (GPS), pace, last-known-marker на карте
   - Live: HR, zones, time, cals (time-based estimate)
   - Banner: «Пульс и время продолжают записываться. Дистанция временно на паузе» (B3 GPS lost canonical)
3. **Auto-pause (юзер не движется, всё на паузе):**
   - Frozen: ALL — HR, км, pace, zones, cals
   - Live: только timer (но он показывает elapsed, не active duration)
4. **Manual pause:**
   - Same as auto-pause

Mechanical check: открыть source canonical training-active, выписать список widgets, для каждого определить data source (GPS/HR/time/motion-sensor). Bracelet disconnect = только HR widgets frozen. GPS lost = только GPS widgets frozen. Pause = все widgets frozen.

## 2026-06-15 — Dim overlay strength = function of severity (destructive vs transient)

Проблема: при моделировании двух overlay'ев (Delete confirm + Sharing in progress) над одним и тем же Session Detail base, естественно поставить одинаковый dim-уровень для consistency. Это смазывает семантику — пользователь не различает «warning, обрати внимание» от «processing, подожди».

**Правило для dim-overlay strength внутри device-frame:**
1. **Destructive confirm** (delete, irreversible action, stop training): `rgba(12, 10, 9, 0.55)` — strong dim. Background читается, но focus полностью на modal. Это «вы должны принять решение прежде чем продолжать».
2. **Transient processing** (sharing, syncing, uploading): `rgba(12, 10, 9, 0.40)` — softer dim. Background more visible — communicates «временное состояние, не warning». Это «подождите, идёт работа».
3. **Critical alert** (battery 5%, fall detected confirm): `rgba(12, 10, 9, 0.65)` — strongest dim. Modal должен быть единственным объектом внимания.
4. **Informational sheet** (auto-pause, GPS lost banner): нет dim — bottom-sheet или banner без overlay. Это «информация о текущем состоянии», не interrupt.

Mechanical check: открыть два mockup'а рядом (Delete + Sharing в одной задаче). Если оба dim-уровня выглядят одинаково — что-то не так в семантике. Should be visibly different intensity (одна заметно темнее).

## 2026-06-15 — Spinner pattern consistency across product (rotating arc, not 3-dot wave)

Проблема: при добавлении нового loading-state легко взять «более премиум» spinner pattern (3-dot wave, pulsing rings, custom SVG morph). Это вносит motion-vocabulary fragmentation: onboarding-calibrating использует rotating ring, sharing-in-progress 3-dot wave, future syncing — pulsing dots. Каждый spinner ощущается как «другая часть приложения».

**Правило для spinner pattern в Neiry Pulse:**
1. **Canonical spinner = rotating arc circle** с `stroke-dasharray="70 30" pathLength=100` rotating 1.1s linear infinite. Wine `#831843` stroke на white card / wine background.
2. **Size scale (4 уровня):** hero 40-48px (sharing card, full-screen loader), mini 14-16px (inline-row progress-step), micro 10-12px (button-loading, inline status).
3. **НЕ вводить альтернативные patterns** (3-dot wave, pulsing rings, skeleton-shimmer) кроме как для skeleton-content loader (плейсхолдеры карточек). Skeleton — другой semantic class, не spinner.
4. **Spinner всегда соответствует canonical animation** — никаких кастом-кейв-функций для отдельных экранов.
5. **`prefers-reduced-motion`** обязателен: animation: none + статичный visible arc.

Альтернативные patterns можно рассмотреть только для дизайн-системы целиком (R&D-decision), не per-screen.

## 2026-06-15 — Progress steps в loading-state: 3 states max + explicit visual hierarchy

Проблема: 4+ progress-steps в loading-card перегружают modal vertically — пользователь читает list, не processing-status. Visual hierarchy без чётких state-markers (done/in-progress/pending) превращает steps в plain bullet-list — теряется sense of progression.

**Правило для mini progress-steps в loading-overlay:**
1. **Maximum 3 шага** в visible state. Если процесс реально длиннее — collapse в «несколько следующих» или показывать через progress-bar percentage, не enumerate.
2. **3 explicit states с разными visual cues:**
   - **DONE:** wine check-icon 16×16 (с outline-circle opacity 0.32) + foreground text (no muted)
   - **IN-PROGRESS:** mini rotating spinner 14×14 wine + foreground text + `aria-current="step"`
   - **PENDING:** muted dot 6×6 (`var(--border-strong)`) + muted-foreground text
3. **Spacing 10px gap** между rows, vertical separator (`border-top: 1px solid var(--border)` + padding-top: 14px) отделяет от sub-copy. Это даёт смысловое разделение «вы здесь читаете, ниже — реальный прогресс».
4. **Иконки aligned by center, fixed width** (icon column 18px) — text-column flex:1. Никаких jagged left edges.
5. **Font: Geist Mono 12pt letter-spacing 0.02em** — даёт ощущение system-status, не human-text. Согласуется с timestamp / device-status mono-pattern.

Mechanical check: если кнопка «Отмена» появляется в loading-card — она ВСЕГДА bottom (после progress-steps), text-link wine, не destructive. User должен иметь option escape, но не encouraged.

## 2026-06-15 — Scanner-frame error state: dashed + alert-orange ≠ canonical wine solid

Проблема: для HS Scan QR canonical layout — solid wine corner-brackets `#831843` + scan-target-glow soft wine. При создании error state (QR invalid/expired) первый импульс — оставить canonical frame и положить error icon сверху. Это смешивает active-scanning visual language с error visual language — пользователь secs не считывает «что-то пошло не так».

**Правило для scanner error states:**
1. **Frame border переключается** на `2px dashed` от solid 4px solid — dashed визуально читается как «нестабильное / прерванное».
2. **Цвет corners + dashed border** переключается на alert-orange `#d97706` (не wine). Wine = active brand action; alert-orange = degraded/failed state.
3. **Glow box-shadow** меняется на alert-orange tint (`rgba(217, 119, 6, 0.22)` 40px blur + 1px alpha-18 ring) — сохраняем «attention pull» паттерна, но семантически переключаем.
4. **Внутри frame** — alert-orange ⊘ slash-circle SVG 64×64 (consistency с B2 camera denied iconography) + mono label «<СУЩНОСТЬ> НЕДЕЙСТВИТЕЛЕН» 11pt warning-soft-foreground.
5. **Camera-view background — dim, compact** (не full-screen). Scanner zone сжимается до ~330px чтобы под ней поместились error info-block (alert-soft) + 2 CTAs + tab-bar. Full camera-view нужен для «active scan», для error state он отнимает место без semantic add.

Anti-pattern: оставить scanner-frame wine + наложить orange icon — это сосуществование двух brand semantics на одном элементе, создаёт когнитивный диссонанс.

## 2026-06-15 — Role-onboarding privacy boundary copy: имя + что НЕ доступно + agency

Проблема: при создании screen «вы наблюдатель» естественно написать "Вы можете просматривать данные Папы" — нейтрально и неинформативно. Это не объясняет границу роли и оставляет пользователя в неопределённости «а что если я нажму другую кнопку?». В первом контакте с asymmetric-permission продуктом это вызывает hesitation.

**Правило для role-onboarding copy при первом подключении:**
1. **Имя** (real person, не «опекаемый») в title — «Вы видите Папу» создаёт эмоциональную связь, а не процедурную («Подключение установлено»).
2. **Explicit «вы — наблюдатель»** в sub — отрицание агентности должно быть прямым, не размытым. «Вы не можете изменять его настройки» в одной строке с ролью.
3. **Что доступно (4 ✓ rows)** — concrete metrics (HR/HRV, Шаги, Алерт о падении 10s, Сон). Generic «здоровье» не работает.
4. **Что НЕ доступно (1 ⊘ row, muted)** — обязательно. Без явного «что я НЕ вижу» пользователь будет thinking «возможно вижу всё?». Concrete: «Личные сообщения и местоположение». Muted icon + muted text — visually downgraded, но not hidden.
5. **Privacy hint card** про subject agency («Папа в любой момент может отключить») — снимает паранойю с обеих сторон: caregiver не может «следить» в полном смысле, caregivee сохраняет контроль.
6. **CTA с agency**: «Понятно, перейти к Папе» — «Понятно» = пользователь подтверждает, что прочитал; «к Папе» = explicit next destination, не «Готово / Продолжить» (где?).

Mechanical check: open role-onboarding screen, прочитать вслух 3 секунды — должен сложиться понятный mental model «я вижу X, не вижу Y, он управляет». Если читается «всё равно непонятно что доступно» — переписать concrete rows.

## 2026-06-15 (Revision 5) — Скрытый дубликат eyebrow: scanner-label + info-block-eyebrow

Проблема: при моделировании error state HS Scan QR canonical pattern (B7 Phone 1) случайно ставлю **два mono-eyebrow** для одной семантики: «QR НЕДЕЙСТВИТЕЛЕН» внутри scanner-frame (большой, prominent, alert-orange) + «QR · НЕ РАСПОЗНАН» в error info-block ниже (small, mono, warning-strong). Это **double-labelling** одного и того же события — eye сначала читает scanner-label, потом дублирующий eyebrow, теряет immediacy «что title говорит мне».

**Правило:** в любом screen с inline-status-label (scanner-frame label, badge на icon, pill в hero) **не дублировать тот же statement в eyebrow info-block'а ниже**. Eyebrow info-block резервируется ТОЛЬКО для добавочной семантики («время события», «severity», «sub-category»). Если eyebrow info-block повторяет inline-label — удалить, title станет load-bearing primary.

Mechanical check: для каждого alert-screen открыть screenshot, прочитать labels сверху вниз. Если два mono-eyebrow подряд говорят примерно то же самое — один лишний.

## 2026-06-15 — Whoop-style 30-day line chart: SVG-only (no JS) с inline path-data

Проблема: при создании HRV detail view естественно подумать про charting library (recharts / chart.js / d3) — но это вводит JS-runtime, lifecycle complexity и dependency. Для wireframe-mockup это overkill: график статичный, данные mock, нужна только pixel-perfect визуальная подача whoop-style.

**Правило для chart mockups в wireframes:**
1. **SVG inline path-data** через preserveAspectRatio="none", все координаты вычислены математически (values → y через `(max-val)/(max-min) * plotHeight + topY`). Пишется один раз в HTML, никаких runtime-вычислений.
2. **Структура слоёв (z-order):** grid-lines → baseline dashed → area fill → line → dots (regular) → today-dot ring + filled + tooltip. SVG draw-order = z-order, так что порядок в DOM критичен.
3. **viewBox 360×160 + preserveAspectRatio="none"** — chart растягивается на любую card width не ломаясь. Плотность 30 точек размещается step ~11.03px по x.
4. **Daily dots: r=2 для обычных, r=3.5 + r=6 ring для today** — даёт subtle hierarchy без overcrowd.
5. **Tooltip как SVG-shape (rect + text + pointer triangle)**, не HTML-overlay — остаётся внутри chart viewBox, не требует absolute positioning.
6. **Baseline label inline в SVG** через `<text>` с text-anchor="end" справа от dashed line — не пытаемся использовать legend block.
7. **Y-axis labels: 3 ticks max** — top/middle/bottom. Больше = noise для 160px высоты chart.

Anti-pattern: chartlib JS + ResizeObserver + state hook для wireframe «потому что в production будет recharts». Mockup ≠ component; статичный SVG = ground truth для дизайнерского ревью.

## 2026-06-15 — Profile edit form pattern: label-above-value vs label-horizontal

Проблема: 7 form fields на 844px screen с tab-bar требуют compact pattern. Если делать каждое поле header + input как в desktop forms (label сверху 20pt + input ниже 24pt + 8px gap + 16px row gap), на mobile получается 60-80px per row × 7 = 420-560px только form — без avatar block + bracelet card + destructive link.

**Правило для mobile-Profile (или любой compact-edit form):**
1. **Mixed pattern** — поля с inline-edit (Имя, Email, Пол segment) используют label-above-value vertical layout (44-56px высота row). Поля с tap-to-open picker (DOB, Рост, Вес, Цели) используют label+value-stacked-left + chevron-right horizontal layout (60-72px высота). Это даёт visual rhythm и signals «можно тапнуть → откроется picker» без явных кнопок.
2. **Segment control для пола** — 3 опции на одной строке, 32-36px высота. Wine background для selected, beige muted-bg для inactive. Inline с form-rows (внутри form-section), не отдельная card.
3. **Sections с border-bottom на rows + section-gap 12-16px между группами** — даёт subtle visual grouping без выноса каждой section в отдельную card. Group 1: identity (Имя/Email). Group 2: demographic (DOB/Пол). Group 3: physical+goals (Рост/Вес/Цели).
4. **Avatar block top на белой surface (var(--card)) с border-bottom** — отделяет identity area от form area через subtle surface contrast, не через border-thick.
5. **Destructive link «Удалить аккаунт»** — отдельная button center-aligned 14px wine красный, без icon. НЕ внутри form-section (это не form-field, это destructive action). Отступ 24px сверху от bracelet card.
6. **Readonly visual indicator (Email)** — small uppercase READONLY mono-tag в muted-bg + muted-foreground текст самой value. Не disabled-state input chrome (на mockup это не имеет смысла — нет input chrome вообще).

Mechanical check: подсчитать row-heights × N + section-gaps × M = должно влезть в body-scroll height (≈688px на 844-44-48-76). Если не влезает — допустимо что bracelet card + destructive link уходят под fold (scroll required). Это OK pattern для mobile Profile (юзер ожидает scroll на edit-form).

## 2026-06-15 — Bottom-sheet modal: max-height grown-by-content vs fixed 70-75%

Проблема: брифы часто требуют «bottom-sheet 70-75% screen» как fixed-height — но если content реально занимает 50-60%, то sheet с fixed 75% выглядит как «дыра» внизу (большая зона padding-bottom). Если content требует 80%, fixed 75% обрезает контент.

**Правило для bottom-sheet modal в mobile-mockups:**
1. **Default: max-height: 75%; height: auto** — sheet растёт по content, ограничен сверху до 75% screen чтобы не превратиться в full-screen takeover.
2. **padding-top 14px + padding-bottom 26-32px** — даёт comfortable touch-target gap для CTA + breathing room под sheet-handle.
3. **Если content overflows (long bullets, large illustration)** — внутри sheet `overflow-y: auto` на body section + sheet-handle и close-× остаются sticky на top.
4. **Eyebrow + title + body + bullets + disclaimer + CTA** — стандартный stack для explainer modal. Между секциями 12-18px vertical gap или `border-top: 1px solid var(--border)` + padding-top 12px для смыслового разделения.
5. **Wine CTA full-width 48px bottom** — single primary action; secondary action (если есть) — text-link выше CTA, НЕ outline-button рядом (mobile sheet ≠ desktop dialog с двумя buttons).

Anti-pattern: фиксировать `height: 75%` без `auto` fallback — на грани screen size получаются артефакты или обрезанный CTA.

## 2026-06-16 — C4 Celebration: preview peek НЕ должен spoiler-ить hero ревью на следующем экране

Проблема: на Phone 1 (Baseline ready notification) под celebration card положен dimmed Home preview peek (opacity 0.4) с widget'ами HRV / Шаги. Естественно скопировать loaded-state values из canonical Home — но если HRV preview покажет конкретное value (например `47 ms`), это либо (а) **дублирует** baseline value из stat-cell наверху и читается как ошибка («почему два раза 47?»), либо (б) **spoiler-ит** first HRV measurement value (52), который раскрывается ТОЛЬКО на Phone 2.

Семантически: на момент Baseline ready (Day 2 утром, через 36-48 ч калибровки) первый замер HRV ещё НЕ сделан — user нажимает CTA «Посмотреть первый замер» именно чтобы получить его. Следовательно preview HRV widget в этот момент = pre-reveal state, и должен показывать placeholder.

**Правило для preview peek под celebration card:**
1. **Placeholder pattern для HRV widget pre-reveal:** `—` (em-dash) в `var(--border-strong)` weight 500 + sub-label «ожидает первого замера» в muted-foreground. Это same pattern что и empty Home (A5 lesson 2026-06-14) — calibrating placeholder, не «broken».
2. **Real values только для метрик, которые валидны на этот момент:** Шаги (1 248) — валидно, юзер двигался эти 36 ч. Sleep, если есть — валидно (вчерашняя ночь). HR resting — валидно (не зависит от baseline).
3. **HRV / Stress Index / любые baseline-dependent метрики** — placeholder до первого замера. Только Phone 2 (reveal) раскрывает их.
4. Не дублировать значение из stat-cell наверху celebration card в preview — это inconsistency прокидывает «47» дважды (1 раз как baseline label, 1 раз как «сегодня»), читатель не различает контексты.

Mechanical check: для любого celebration-screen с preview peek — пройти список widget'ов и для каждого ответить «эта метрика существует на этот момент времени flow'а?» Если ответ «нет» / «именно её мы будем показывать на следующем экране» — placeholder.

## 2026-06-16 — Side-stripe «full-access marker» — impeccable absolute ban, alternatives

Проблема: естественный паттерн для «special / full / VIP» card — добавить `border-left: 3px solid wine` как accent. На C5 я сделал это дважды: на receiver-card Папа (full-access) и на protect-card «Вы под защитой». Это **impeccable absolute ban**: «Side-stripe borders. border-left greater than 1px as a colored accent on cards, list items, callouts, or alerts. Never intentional.» AI-grammar tell, появляется в 50%+ генераций.

**Правило для маркировки «special status» на card:**
1. **Full border (1.5px solid brand)** вместо stripe — clear, contained, не выбивается на левую кромку.
2. **Tinted background gradient** (например `linear-gradient(180deg, primary-soft 0%, card-warm 100%)`) — subtle wine identity без stripe.
3. **Avatar / icon recolor** на brand wine — переносит accent в content, не на chrome.
4. **Compact pill / badge** справа (`Geist Mono uppercase 9.5pt + wine bg + white fg + rounded-full`) — explicit semantic marker.
5. **Combining 2-4 совмещает identity без cliché.** Например: full wine border + wine avatar + «ПОЛНЫЙ» pill = «Папа full access» readable, no stripe.

Anti-pattern: оставлять `border-left: 3px wine` «потому что quick и visible» — это AI shortcut который impeccable critique поймает первым же проходом. Любой card с special-status треатуется через **full border + content recolor**, не через side-stripe.

Применимо ко всем будущим cards: featured / pinned / premium / full-access / alert / urgent — никаких side-stripes.

## 2026-06-16 — Two-way symmetry через parallel structure, не через равное количество элементов

Проблема: при моделировании two-way dashboard (Я делюсь vs Со мной делятся) первый импульс — поставить равное количество rows в обоих секциях для visual balance. Но в реальной user A story 2 sharers + 1 sharer-to-me — данные асимметричны.

**Правило для two-way / bidirectional UI dashboards:**
1. **Symmetry достигается через parallel structure**, не через равный content:
   - Те же section-header eyebrow в том же шрифте/размере/цвете
   - Те же decorative anchors (например wine pill backplate под direction arrows)
   - Те же sub-title fonts
   - Те же row-card patterns
2. **Direction arrows как visual differentiator** — ↗ (outgoing) vs ↙ (incoming) внутри одинаковых backplates. Reading rhythm: «label + arrow → list». Mirrored geometry даёт subconscious read «это другая сторона того же».
3. **Honest data > forced symmetry.** Если sharers != receivers, не fake-добавлять placeholder rows. Структурная параллельность достаточна. Spaces между секциями + protect-card pushed к bottom (margin-top: auto) утилизирует свободное место.
4. **Divider должен быть symmetric** — никаких асимметричных wine-overlay только-слева. Clean 1px border = единственный честный divider между bidirectional zones.
5. **Color cue:** outgoing data = brand wine (вы инициируете), incoming alerts (Бабушка HRV ↓) = alert-orange (warning peak, single severity per screen).

Mechanical check: сложить screenshot пополам по divider — обе половины должны иметь идентичную structural grammar (header height, arrow shape, sub-title position), отличие только в content density и arrow rotation.

## 2026-06-15 (Revision 5) — 3 phones в одном файле: добавление Phone к existing 2-phone setup

Проблема: добавляя Phone 3 (close confirm modal) к существующему 2-phone файлу B4 (end-of-session + bracelet disconnect), естественно скопировать Phone 1 markup целиком как background для overlay. Это дублирует 100+ строк HTML — рискованно для maintenance и нарушает single-source-of-truth.

**Правило для добавления Phone N к existing N-1 layout:**
1. **Поднять modal-styles один раз** в `<style>` (НЕ inline в Phone 3) — `.dim-overlay`, `.close-modal`, `.btn-destructive-full`, etc.
2. **Phone 3 markup** = упрощённая копия Phone 1 (нужный context для overlay) + `aria-hidden="true"` + `tabindex="-1"` на интерактивных элементах + `.end-body-dimmed` class (filter: brightness 0.85 saturate 0.85) для visual dim cue. Без `position: absolute` overlay — modal встроен в DOM phone'а.
3. **Proof-render координаты** для 3-phone side-by-side: window-size 1900×1100, phones at x ~306-717 / 744-1155 / 1182-1593 (ground-truth из B3). Reuse.
4. **Backwards-compat нумерация PNG:** при добавлении 3-го экрана к 2-экранному файлу, side-by-side PNG переименовывается (например, `29-end-bracelet-side-by-side.png` → удалить, новое `30-end-bracelet-close-side-by-side.png` для 3-phone). Новый proof Phone 3 = `29-close-confirm.png`. PM-выбор (b) из brief: rename SxS, add proof.

Mechanical check: после ренда proof PNG'ов посчитать визуально количество phones в side-by-side. Должно совпадать с числом `.frame-with-caption` в HTML (`grep -c "frame-with-caption" file.html`).

## 2026-06-17 — Cross-file persona consistency: HTML-правки ≠ proof-PNG; всегда re-render всех затронутых артефактов
Проблема: при batch revision canonical persona (Костя Леонов / VIGOR-XYZ123 / HS receivers ИП Тренер + М67 Мама / observer Папа) HTML 4 файлов был корректно обновлён, но C5 PNGs (24a/24b transparent + 54/55/56 proof) остались stale с прошлой генерацией (old persona «М Мама / П Папа / Бабушка»). При cross-file sync задаче handoff между агентами легко пропустить часть PNG.

**Правило для batch persona/data sync:**
1. **Compare mtime:** `stat -f "%Sm" file.html file.png` — если HTML newer чем PNG, PNG stale, требует re-render. Не доверять brief'у «PNG регенерированы ✓» — verify вручную.
2. **Open proof PNG через Read tool ОБЯЗАТЕЛЬНО** перед закрытием задачи — даже если предыдущий step сказал «done». Глазами проверить, что текстовые элементы (имена, цифры, аватары) соответствуют HTML.
3. **Map HTML → PNG явно:** для каждого изменённого HTML файла перечислить все производные PNG (transparent + proof + side-by-side) и убедиться что mtime каждого PNG > mtime HTML.
4. **Anti-pattern:** «brief сказал C5 done, значит done». Brief — это план, не источник истины. Источник истины = `Read` tool на PNG + visual diff.

## 2026-06-17 — Hybrid entry-point pattern (inline + chevron) для главного Settings экрана
Проблема: на canonical Settings экране нужно одновременно (a) дать быстрый доступ к самым частым настройкам (3 toggle уведомлений + 2 HS receiver toggles), (b) обеспечить точку входа в детальные настройки (BT pairing, Notifications, Privacy, Sleep). Чистый inline = негде хранить advanced. Чистый chevron-list = 5 тапов до простого toggle.

**Правило hybrid pattern для entry-point screens:**
1. **Critical primary actions = inline** (toggle на самой карточке). Пример: 3 toggle уведомлений, 2 HS receiver toggles на canonical Settings.
2. **Detail/advanced access = chevron** на той же section. Варианты:
   - **Wine text-link в header section** (`Все настройки ›`) — для secondary entry, не загромождает основной layout. Пример: «УВЕДОМЛЕНИЯ» header правее = `Все настройки ›` link → C2 Phone 2 Notifications detail.
   - **«+ Управление»** wine link внизу section — для HS типа entry. Tap → C5 Phone 1 sharer detail.
   - **Chevron на header card** (user card, Sleep card) — entry в isolated detail (Profile edit, Sleep detail).
3. **Anchor card БЕЗ chevron** — текущее состояние ресурса (Braclet «подключён 87%»). Tap опционально ведёт на detail, но visual cue = info-card, не nav.
4. **Section «ПРИВАТНОСТЬ»** как новая = single chevron-row (icon shield + label + chevron) — для редких но важных flow (download data / delete account). Не inline.

Mechanical check: на entry-point Settings должны быть ровно 3 типа entries: inline-toggle, hybrid-section (inline + secondary chevron), pure-chevron. Если 4+ типов — UX усложняется, refactor.

## 2026-06-17 — Settings: добавление новой section требует pre-emptive compress audit (cumulative micro-padding wins)

Проблема: при добавлении новой section «ПРИВАТНОСТЬ» в canonical Settings (5 sections итого: Уведомления / HS / Данные и Sleep / Приватность / Прочее) контент overflow'нул 844px viewport. Privacy section была формально в HTML, но визуально не показывалась — обрезана tab-bar'ом. Аналог проблемы C1 Profile edit где compress padding'ом починили похожий overflow.

**Правило для list-heavy entry-point Settings (5+ sections):**

1. **Pre-emptive compress audit ДО добавления новой section.** Считать total content height: app-bar (~48) + status (~44) + sum(section heights) + tab-bar (~88). Если ≥ 844 — compress сначала, потом добавляй section.

2. **Cumulative micro-padding budget** (validated на 5-section Settings 390×844, все 8 acceptance elements visible):
   - `.toggle-row` / `.entry-row` / `.action-row`: padding `7-8px 12px` (НЕ 12-14px). gap `10px` (НЕ 12px).
   - `.section`: padding `8px 16px 0` (НЕ 16px top).
   - `.section-header` margin-bottom: `6px` (НЕ 8-12px).
   - `.device-card` / `.profile-inline`: padding `8-10px` (НЕ 12-14px). Avatar/icon `32-36px` (НЕ 40px).
   - `.manage-link`: `8px 12px`. `.destructive-row`: `10px 14px` (если есть).
   - `.row-sub` / `.device-meta` / `.profile-email` margin-top: `1-2px` (НЕ 4px).

3. **Sections priority ladder** для Settings list — что обязано быть above-fold-no-scroll vs ниже:
   - **Above viewport (must visible):** App-bar, User card, Anchor card (Braclet), main toggles section (Уведомления), HS section, primary entry-rows (Sleep + Privacy).
   - **Below viewport (scroll required, OK):** Калибровка / Поддержка / О приложении / destructive Выйти.
   - Visual scroll-affordance: section «ПРОЧЕЕ» peek снизу tab-bar — даёт намёк что есть ещё контент. Эстетически работает.

4. **Mechanical post-render check:** обязательно открыть proof PNG через Read tool и подтвердить acceptance checklist visible. Если row залезает под tab-bar даже на 4-6px — overflow ещё есть, нужен round 2 compress (snap `padding: 8px → 7px` ещё на 1px на самой длинной group of rows). Это окупается.

5. **Anti-pattern:** добавлять новую section и сразу регенерить PNG без compress audit. На list-heavy экранах с 5+ sections это всегда даёт overflow — micro-paddings × 30+ rows накапливаются в крупные суммы (60-80px). Compress ДО добавления, не после.

## 2026-06-17 — Targeted regen subset transparent PNGs (не trigger full batch)

Когда нужно обновить 2 из 5 frames в multi-frame HTML (e.g. `mobile-health-sharing-v0.html` имеет 5 `.frame-wrap` блоков), запускать `slice_phones_transparent.py` целиком — wasteful (рендерит все 14+ PNG, дублирует Onboarding + Training + Settings + Home, тратит 60-90 сек на headless Chrome).

**Правило targeted regen:**

1. **Reuse production logic** — copy/paste `HIDE_CHROME_CSS`, `find_div_blocks`, `slice_clean`, `shoot_transparent` из canonical `slice_phones_transparent.py` в одноразовый `/tmp/regen-<file>-<frames>.py`. Не модифицируй production script.

2. **Specify только нужные frame indexes:** для HS (5 frames) frame 0 = main, frame 1 = generate-qr, frame 2 = scan-qr, frame 3 = success, frame 4 = detail. Если правки только в 0 + 4, рендерим только их (2 вызова `slice_clean` + `shoot_transparent`).

3. **Output paths должны overwrite канонические DEST PNG** напрямую (`sliced-flow-v2-1-transparent-2026-06-14/`), а не временные. Иначе PM получит non-updated PNG в acceptance.

4. **Verify byte size после регена** — если новый PNG ≪ старого (например, 12KB вместо 56KB) — render упал silently. Проверь `os.path.getsize()` в `print()` после `shoot_transparent`.

5. **Anti-pattern:** регенерить full batch script "на всякий случай". Все 5 frames overwrite одновременно, и если в одной из НЕ-целевых frame случайно был WIP коммит (но не для PM ревью) — он попадёт в acceptance под видом "согласованной правки". Subset rebuild — explicit and safe.

6. **Mechanical post-render:** Read tool на оба PNG → visual confirm swap (avatar глиф, name, palette) → enumerate acceptance checklist в BRIEF РЕЗУЛЬТАТ section. Headless render иногда подменяет шрифт fallback'ом если Onest/Geist Mono cdn не успел загрузиться — visual check ловит это.

## 2026-06-17 — Persona swap в alert-tier context: avatar palette consistency rule

Контекст: при swap «Мама · 67 лет» (alert HRV receiver) → «Папа» (alert HRV receiver) в HS Main + Detail, нужно было решить — оставить ли `avatar-warning` palette на новой персоне или переключить на default wine.

**Правило для persona swap в alert-state row/header:**

1. **Alert state палитра привязана к state, не к персоне.** `avatar-warning` (warning-soft bg `#fdf3e1` + warning-strong text `#b45309`) визуально маркирует «HRV в зоне alert», не «эта конкретная персона opaque». Если новая персона тоже alert (Папа HRV 38 ms ↓) — palette остаётся `avatar-warning`. Если бы Папа был в normal state — switch на default wine.

2. **Глиф avatar (initials) ≠ palette.** «П» (1 char) vs «МА» (2 char) — оба umещаются в 32-40px circle с `letter-spacing: 0.02em` без overflow. Кол-во char не диктует palette.

3. **Visual cohesion check:** в Detail-view header avatar `avatar-warning` соседствует с alert-orange HRV ms hero number (`var(--warning)` `#d97706`) + alert-orange banner + sparkline warning tint. Все warning-tier elements в одной цветовой семье — это intentional unified language, а не coincidence. Persona swap должен сохранить эту цепочку.

4. **Cross-frame consistency:** если персона маркирована `avatar-warning` в HS Main row, она должна быть `avatar-warning` и в Detail header. Switching palette между frames для same person — breaks visual identity.

5. **Anti-pattern:** «новая персона = новый avatar bg». Особенно опасно когда BRIEF говорит «wine bg для П» без указания state — wine на alert HRV row создаст visual conflict с alert-orange dot/text справа. State diktiruet palette, not BRIEF text alone — проверяй state у row перед применением.
