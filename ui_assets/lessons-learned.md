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
