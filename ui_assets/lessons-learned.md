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
