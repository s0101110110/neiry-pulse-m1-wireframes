# HANDOFF — Kiosk Drill-down (Bayevsky test)

## Статус сессии 2026-05-27 — R6 локально (PM передаёт Кириллу, push потом)

🟡 **R6 применён ЛОКАЛЬНО — НЕ запушен.** PM отправляет файл Кириллу напрямую. После acceptance от Кирилла — push.

**Изменённый файл:** `docs_web/wireframes/m2/kiosk-drilldown.html`

### R6 правки (по фидбэку PM со скриншотом)

| # | Правка | Реализация |
|---|---|---|
| 1 | BPM hero преемственность с kiosk-v2 | Убрал сердечко, `flex items-baseline gap-3`, `font-display t-display` цифра + `font-data t-lead` BPM, под цифрой отдельная строка `<p>` с «● ПОДКЛЮЧЕН» (t-caption font-data). `.font-display { letter-spacing: -0.04em }`, `.t-display { line-height: 0.95 }` |
| 2 | Caption под кнопкой Тест по центру | Кнопки в `grid-cols-3 gap-x-4 gap-y-2`: ряд 1 = `СТОП` + `Тест (col-span-2)`, ряд 2 = `<div></div>` + `test-hint (col-span-2)`. Caption теперь ровно под кнопкой Тест, не растянут на всю ширину |
| 3 | Stress + IMU карточки одного размера и шрифтов | Activity card перестроен по структуре Stress: `relative w-56 h-56` контейнер, SVG 180×180 viewBox с concentric circles (r=72, r=52), waveform absolute top:46px, label «АКТИВНОСТЬ» absolute top:138px (=label Стресс), badge absolute bottom:4px через `.badge .status-*`. Добавлен `.status-idle` для off-state. `white-space: nowrap` в `.badge` (чтобы «НЕ НАДЕТ» не переносился) |

### Скриншоты R6 (proof, 1354×746)

Папка: `UI_assets/screenshots/kiosk-drilldown/r6-pm-3edits/`

- `dd-kostya-rest.png` — Покой, badge зелёный, тест enabled
- `dd-kostya-light.png` — Лёгкая, badge жёлтый, тест disabled
- `dd-kostya-motion.png` — Движение, badge красный
- `dd-kostya-off-v2.png` — Не надет, badge muted (status-idle), одной строкой
- `empty-guest.png` — empty-state, оба badge скрыты (opacity:0)

### Что НЕ менялось в R6
- 9 столбиков waveform (PM сказал «не перегенерировать, они хорошие»)
- IMU 4-статусная логика (rest/light/motion/off + dev-bar pills + `?imu=` URL-param)
- Все R5 фиксы

### Что ждёт push после Кирилла
- Коммит R6 с сообщением «R6: BPM hero паттерн kiosk-v2, caption-центр под Тест, Stress+IMU унификация (PM 3 правки)»
- Скриншоты `r6-pm-3edits/`

---

## R5 — ЗАКРЫТ полностью, запушен в main (`487f7c8`)

Все 5 системных проблем drilldown ↔ kiosk-v2 устранены:

| # | Проблема | Статус | Коммит |
|---|---|---|---|
| 1 | Bayevsky overflow в empty (`.main-content` height calc) | ✅ flex-1 min-h-0 + shrink-0 | `80ba982` |
| 2 | Type-scale 17+ размеров | ✅ 6 ступеней `--t-*` + `.t-widget` 7-я | `80ba982` + `487f7c8` |
| 3 | Хедер h-16 vs h-[86px] | ✅ shrink-0 h-[86px] px-10 + SVG-логотип neiry | `80ba982` |
| 4 | CSS-токены разъехались | ✅ `:root` копия 1:1 из kiosk-v2 | `80ba982` |
| 5 | `.font-hero` vs `.font-display` | ✅ replace_all | `80ba982` |

## GitHub Pages (текущий R5 финал = `487f7c8`)

https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-drilldown.html

State-params: `?id=kostya|alexey|guest&state=drilldown|phase-1|phase-2|phase-3|result|empty|claim`

## Скриншоты v6 (proof)

Папка: `UI_assets/screenshots/kiosk-drilldown/r5/` (28 файлов — 4 размера × 7 states)

**Ключевые:**
- `v6-1512x945-empty-guest.png` — proof фикса Проблемы 1 (Bayevsky плитка внутри stage)
- `v6-1920x1080-drilldown-kostya.png` — основной рабочий вид, палитра совпадает с kiosk-v2
- `v6-1920x1080-claim-kostya.png` — claim hero «Спасибо за участие» в t-h1 (72px)
- `v6-1920x1080-result-kostya.png` — иерархия ИН Σ → вердикт → фазы

## История коммитов

| Коммит | Содержание |
|---|---|
| **`487f7c8`** | **R5 финал** — Tailwind text-* → t-* (60+ замен), скриншоты v6 |
| `80ba982` | R5 чекпоинт — палитра, type-scale переменные, хедер, overflow-fix, font-hero → font-display |
| `b7f2ac1` | R4: dev-bar → floating pill (паттерн kiosk-v2), fitStage без вычитания |
| `1576f8d` | Merge feature/m2-kiosk-drilldown в main |
| `81f3e8f` | R3: viewport-fit canvas 1920×1080 + cancel-кнопки |
| `cf8b7ef` | R2: ECG нет сигнала, Stroop на планшете, НАГРУЗКА |
| `8331c21` | R1: UX-аудит, Sleep gauge, Bayevsky композиция, Result-модалка, Claim QR |

## Self-review checklist — пройден

- [x] Скрин 1512×945 empty — Bayevsky НЕ выходит за низ stage ✅
- [x] Скрин 1920×1080 drilldown — нет боковых пустот, нет вертикального overflow ✅
- [x] v6-drilldown-kostya vs kiosk-v2-active-3 — палитра совпадает (wine #831843, success зелёный, warning амбра) ✅
- [x] Хедер 86px высота, padding-x 40px, SVG-логотип neiry присутствует ✅
- [x] Все размеры шрифтов в t-* — в HTML нет text-3xl/5xl/7xl ✅
- [x] `font-hero` отсутствует в файле ✅

## Memory update

`project_neiry_kiosk_design_system.md` — добавлена §2.1 «Синхронизация между kiosk-экранами»:
- :root CSS-токены копируются 1:1 из kiosk-v2 (источник правды)
- Type-scale + helper-классы 1:1
- Font naming: .font-display / .font-data (.font-hero запрещён)
- Header pattern h-[86px] px-10 + SVG копируется 1:1
- Кастомные font-size CSS-классы должны использовать var(--t-*), не хардкод px
- Tailwind text-* запрещены в kiosk-контексте (только в служебных dev-bar pills)

## Что НЕ трогали в R5 (работает)

- Cancel-кнопки × в phase-1/2/3 (R3)
- Viewport-fit pattern + floating dev-bar (R3+R4)
- ECG, Stroop placeholder, НАГРУЗКА текст (R2)
- BPM hero, NSI gauge, Stress/Activity круги, Sleep gauge — структура
- State machine `body.state-X` через CSS
- Mock data + persona switcher

## Roadmap M2 — следующая задача после acceptance R5

Из `BRIEF.md`:
4. 🟡 Дашборд корпоратов `docs_web/wireframes/m3/dashboard-corporate.html`
5. 🟢 Mobile pairing рестайл `docs_web/wireframes/m1/mobile-*.html`

**Дедлайн:** 27.05.2026 стыковка офис, 28-29.05.2026 Startup Village.

## Технические известные (не R5-блокеры)

- ECG flat-line при BLE reconnect — minor degradation (через reload фиксится)
- Hit-target dev-bar pills на 67% zoom — pills 11px font, padding 4×10 (не Apple HIG 24×24, но dev-bar служебный)
- Bayevsky карточка результат (ИН 145) — fixed `t-h1` 72px, не имеет fallback при экстремально длинных значениях (4-значные ИН типа >999). Сейчас не критично (mock данные ≤320).
