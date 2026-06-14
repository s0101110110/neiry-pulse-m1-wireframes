# PLAYBOOK — Работа с дизайн-skill'ами

**Для UI-агента.** Читай этот файл, когда PM поставил задачу с указанием skill'а или со словами «прогони критику / аудит / polish / animate / harden». Если задача чисто по вёрстке без skill'ов — игнорируй этот файл, работай по `claude.md`.

**Установлены три skill'а** (см. `INSTALL-SKILLS.md`):
- `emil-design-eng` — моушн, easings, micro-interactions
- `impeccable` v3.5.0 — критика / аудит / polish готовых экранов (27 reference-команд)
- `redesign-existing-projects` — перерисовка существующего блока без потери ДНК

---

## 1. Матрица решения «какой skill на какую фазу»

| Фаза работы | Дашборд (продукт, плотность) | Мобайл (бренд, touch, моушн) |
|---|---|---|
| Аудит перед правкой | `impeccable critique` | `impeccable critique` |
| План UX/IA (без кода) | Plan Mode + Brainstorm — без skill | то же |
| Перерисовать блок in-place | `redesign-existing-projects` | `redesign-existing-projects` |
| Микро-анимации (модалка, gauge, tap-feedback) | `emil-design-eng` | `emil-design-eng` ⭐ |
| Технический аудит (a11y, контраст, responsive) | `impeccable audit` ⭐ | `impeccable audit` |
| «Бледно, добавь жизни» | `impeccable bolder` | `impeccable bolder` |
| «Перегружено, успокой» | `impeccable quieter` ⭐ | редко |
| Edge cases (overflow, i18n, empty/error) | `impeccable harden` ⭐ | `impeccable harden` |
| Финальная вычистка перед коммитом | `impeccable polish` | `impeccable polish` |

⭐ — самый частый кейс в этой вертикали.

---

## 2. Как PM формулирует бриф со skill'ом

Базовый шаблон:

```
Файл: <путь>
Цель: <что хотим получить>
Skill: <skill + аргументы>
Не трогать: <список защищённых элементов>
Ожидаемый выход: <screenshot / список / правки in-place>
```

### Готовые шаблоны для дашборда

**A. Перерисовать KPI-strip Спорт-таба**
> Файл: `docs_web/wireframes/m3/dashboard-corporate.html`. Цель: KPI-strip выглядит как стандартный SaaS-шаблон, нужно отличить от Office-таба. Skill: `Skill redesign-existing-projects args:"KPI-strip Спорт-таба"`. Не трогать токены, шрифты, остальные секции. Ожидаю: вариант + screenshot before/after, ждать acceptance.

**B. Аудит drill-down side-panel**
> Файл: `dashboard-corporate.html`, state `panel-open` через dev-bar. Skill: `Skill impeccable args:"audit side-panel drill-down"`. Интересуют: контраст текста на хедере, focus-states inputs, overflow ФИО, читаемость sparkline на 1440. Ожидаю: список находок, без правок файла.

**C. Уменьшить визуальный шум Driver-таба**
> Driver-таб перегружен — 6 виджетов. Skill: `Skill impeccable args:"quieter Driver-таб"`. Не убирать данные, только иерархия / spacing / цвета. Ожидаю: правки in-place + before/after screenshot.

**D. Edge cases**
> Skill: `Skill impeccable args:"harden dashboard-corporate.html"`. Цель: найти места: ФИО 40 символов, empty state, NSI=null, ошибки сети. Ожидаю: список + предложения, без коммитов.

### Готовые шаблоны для мобайла

**A. Анимация BPM-карточки**
> Файл: `wireframes/m1/mobile-home.html`. BPM-цифра статична — нужен плавный переход 72→78. Skill: `Skill emil-design-eng args:"BPM transition, длительность, easing, как избежать дёргания tabular-nums"`. Ожидаю: конкретный CSS + объяснение, не правки файла.

**B. Tap-feedback всех CTA в pairing**
> Файл: `mobile-ble-pairing.html`. Кнопки без `:active` feedback. Skill: `Skill emil-design-eng args:"tap feedback primary/secondary CTA + icon-button, scale(0.97), 160ms ease-out"`. Ожидаю: правки in-place + screenshot.

**C. Рестайл экрана регистрации на M2-токены**
> Файл: `mobile-registration.html` — старая M1 палитра. Skill: `Skill redesign-existing-projects args:"переезд на M2 semantic tokens (Space Grotesk + shadcn dark + wine #831843), сохранить input-структуру"`. Wine — единственный hex, остальное переменные.

**D. Аудит touch-таргетов и моушна**
> Skill: `Skill impeccable args:"audit mobile-*.html"`. Touch-target ≥44×44, reduced-motion media-query, контраст placeholder, читаемость на 390px. Ожидаю: список по экранам.

---

## 3. Универсальные правила

1. **Один skill на одну задачу.** Не комбинируй emil + impeccable в одном проходе. Сначала `critique` → дай PM посмотреть → потом `polish`.
2. **Skill = подсказка, не закон.** Если skill советует убрать wine accent / поменять шрифт — игнорируй. Источник истины: `wireframes/m2/ui-kit.html`.
3. **PM acceptance gate.** UI-агент не закрывает задачу сам. Формат доклада: `DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED`.
4. **Preview перед commit/push.** Screenshot в чат → ждёшь «принято» → только потом git.
5. **Не коммить `.claude/skills/`** в репо `docs_web` — лежат в `UI_assets/.claude/skills/` под отдельным `.gitignore`.

---

## 4. Что НЕ вызывать (хард-баны)

- ❌ `Skill impeccable args:"init"` — перепишет PRODUCT.md/DESIGN.md
- ❌ `Skill impeccable args:"document"` — перегенерит ui-kit
- ❌ `Skill impeccable args:"craft"` — полный rebuild компонентов
- ❌ `Skill impeccable args:"extract"` — вытащит лишнее в DS
- ❌ `Skill impeccable` без аргумента — подтянет 87 KB SKILL.md
- ❌ Skill на чужой ветке без явного указания PM
- ❌ Менять CSS-переменные `--background` / `--primary` / шрифты M2 даже по совету skill'а

---

## 5. Cheatsheet команд impeccable

Доступные через `Skill impeccable args:"<command> [target]"`:

| Команда | Когда |
|---|---|
| `critique <path>` | UX-ревью: иерархия, ясность, эмоциональный отклик |
| `audit <path>` | Технический: a11y, perf, responsive, контраст |
| `polish <path>` | Финальный пас перед коммитом, выравнивание по DS |
| `bolder <path>` | Усилить бледное |
| `quieter <path>` | Приглушить перегруженное |
| `distill <path>` | Снять лишнее, оголить суть |
| `harden <path>` | Errors / i18n / overflow / edge cases |
| `onboard <path>` | First-run, empty states, активация |
| `animate <path>` | Покажет где добавить моушн (без правок) |
| `colorize <path>` | Стратегический цвет в монохромный UI |
| `typeset <path>` | Шрифты, иерархия, размеры |
| `layout <path>` | Сетка, spacing, ритм |
| `delight <path>` | Моменты радости (точечно) |
| `clarify <path>` | Улучшить непонятный UX-копи |
| `adapt <path>` | Адаптация под устройство |
| `optimize <path>` | Performance |

**Запрещены:** `init`, `document`, `craft`, `extract`, `live`, `pin`, `overdrive`.

---

## 6. Когда skill вернул bullshit

Skill — это generic-правила, обученные на лендингах. Они **часто** конфликтуют с продуктовой спецификой Neiry (медицинские интерфейсы, плотный дашборд, kiosk на 1.5m). Признаки bullshit:

- Советует убрать tabular-nums («слишком техно»)
- Хочет добавить gradient / soft shadows ради «премиума»
- Просит сократить плотность данных в дашборде
- Предлагает «более тёплую» палитру (cream/sand) — это AI-default 2026
- Хочет поменять Geist Mono на Inter

**Реакция:** игнорировать, в докладе пометить `REJECTED_BY_AGENT: <причина>`. PM сам решает спорные случаи.

---

## 7. Обновление PLAYBOOK

Если PM добавил новый skill или новые правила — он сам обновит этот файл. Агент **не правит** PLAYBOOK самостоятельно.
