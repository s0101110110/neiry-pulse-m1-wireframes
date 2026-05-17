# Мульти-агентная PM-система Neiry: План реализации

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Развернуть мульти-агентную PM-систему: knowledge-base Obsidian vault, R&D агент, обновлённые инструкции для всех агентов, защита от потери данных, загрузка существующих материалов.

**Architecture:** Пять агентов (PM, UX/UI, Frontend, R&D, Knowledge Base) с изолированными CLAUDE.md. Общий центр знаний — `NEIRY/knowledge-base/` как отдельный Obsidian vault и git-репозиторий. Трёхуровневая память: CLAUDE.md (всегда) → PROJECT_STATE.md (старт сессии) → детали (по запросу). Stop hook + Obsidian Git = защита от потери данных.

**Tech Stack:** Markdown, bash, Claude Code hooks (settings.json), Obsidian, git.

---

## Карта файлов

### Создать
- `NEIRY/knowledge-base/` — новый git-репо, Obsidian vault
- `NEIRY/knowledge-base/.gitignore`
- `NEIRY/knowledge-base/PROJECT_STATE.md`
- `NEIRY/knowledge-base/INBOX/meetings/.gitkeep`
- `NEIRY/knowledge-base/INBOX/external/.gitkeep`
- `NEIRY/knowledge-base/INBOX/raw/.gitkeep`
- `NEIRY/knowledge-base/tasks/konstantin.md`
- `NEIRY/knowledge-base/tasks/kirill.md`
- `NEIRY/knowledge-base/tasks/nikita.md`
- `NEIRY/knowledge-base/milestones/m1.md`
- `NEIRY/knowledge-base/milestones/m2.md`
- `NEIRY/knowledge-base/milestones/m3.md`
- `NEIRY/knowledge-base/decisions/2026-05.md`
- `NEIRY/knowledge-base/open-questions/index.md`
- `NEIRY/knowledge-base/people/index.md`
- `NEIRY/research/CLAUDE.md`
- `NEIRY/research/INDEX.md`
- `NEIRY/research/lessons-learned.md`
- `NEIRY/research/BRIEF.md`
- `NEIRY/research/hardware/.gitkeep`
- `NEIRY/research/sdk/.gitkeep`
- `NEIRY/research/metrics/.gitkeep`
- `NEIRY/research/sources/.gitkeep`
- `NEIRY/UI_assets/lessons-learned.md`
- `NEIRY/UI_assets/BRIEF.md`
- `NEIRY/dashboard/lessons-learned.md`
- `NEIRY/dashboard/BRIEF.md`

### Изменить
- `NEIRY/docs_web/CLAUDE.md` — добавить: Session Start, путь к KB, rights, session-lock
- `NEIRY/UI_assets/claude.md` — добавить: Session Start, путь к KB, lessons-learned
- `NEIRY/dashboard/claude.md` — добавить: Session Start, BRIEF workflow, путь к KB
- `~/.claude/settings.json` — добавить Stop hook

---

## Task 1: Создать knowledge-base vault и структуру папок

**Files:**
- Create: `NEIRY/knowledge-base/` (директория + git init)
- Create: `NEIRY/knowledge-base/.gitignore`

- [ ] **Шаг 1: Создать директорию и инициализировать git**

```bash
mkdir -p /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git init
```

Ожидаемый вывод: `Initialized empty Git repository in .../knowledge-base/.git/`

- [ ] **Шаг 2: Создать .gitignore**

Создать файл `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/.gitignore`:

```
.obsidian/workspace*
.obsidian/plugins/
.DS_Store
.session-lock
```

- [ ] **Шаг 3: Создать структуру папок**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
mkdir -p INBOX/meetings INBOX/external INBOX/raw
mkdir -p tasks milestones decisions open-questions people
touch INBOX/meetings/.gitkeep INBOX/external/.gitkeep INBOX/raw/.gitkeep
touch tasks/.gitkeep milestones/.gitkeep decisions/.gitkeep
touch open-questions/.gitkeep people/.gitkeep
```

- [ ] **Шаг 4: Проверить структуру**

```bash
find /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base -not -path '*/.git/*' | sort
```

Ожидаемый вывод — список всех созданных папок и `.gitkeep` файлов.

- [ ] **Шаг 5: Первый коммит**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git add .
git commit -m "Init: knowledge-base vault structure"
```

---

## Task 2: Создать PROJECT_STATE.md — живой снимок проекта

**Files:**
- Create: `NEIRY/knowledge-base/PROJECT_STATE.md`

- [ ] **Шаг 1: Создать PROJECT_STATE.md**

Создать файл `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/PROJECT_STATE.md`:

```markdown
# PROJECT STATE — Neiry Pulse
_Обновлён: 2026-05-16_

---

## Текущий фокус
**Milestone:** M1 — Tech Demo  
**Дедлайн:** 2026-05-18 (через 2 дня!)  
**Статус:** В работе

---

## Открытые задачи

### Константин
- [ ] Wireframes M1 и M2 → отправить Кириллу на проверку, затем Никите
- [ ] Документ `Neiry_Ecosystem_Sync.md` — три секции: «Что переиспользуем», «Что строим с нуля», «Точки совместимости»
- [ ] Прободаться с юрдотделом Никиты по правкам договора (30% за передачу прав, 25% отказ, портфолио, исключительные права)
- [ ] Покурить Wikipedia G-Band SDK с нейронкой → собрать документацию в research/sdk/

### Кирилл
- [ ] Черновые эндпоинты авторизации и синхронизации — до 18.05
- [ ] Foreground service (уведомление) в Android для фоновой BLE
- [ ] Ответить: рвёт ли браслет BLE при уходе приложения в фон?
- [ ] Архивные HRV-данные: привязка пользователя (рост/вес/возраст) — до 18.05

### Никита
- [ ] Ответить по правкам договора

---

## Последние решения (май 2026)
- HRV потоковый не нужен для M1 и M2. Только архивные данные (сутки/3 дня/неделя). K M3.
- Авторизация отсутствует до M3 — используется хэш/MAC-адрес устройства
- iOS только в M2. M1 — Android only
- Celery/Redis — не нужны для MVP. Исключить из ТЗ Никиты.
- Память браслета в офлайн: 64 МБ

---

## Нерешённые вопросы
- ❓ Celery/Redis — зафиксировано ли исключение в договоре? (@Константин)
- ❓ ВСР в M2 — показываем архивный HRV на Startup Village или нет? (@Константин + @Кирилл)

---

## Milestones
| Milestone | Дедлайн | Статус |
|---|---|---|
| M1 — Tech Demo | 2026-05-18 | 🟡 В работе |
| M2 — Startup Village | 2026-05-25 | ⬜ Не начат |
| M3 — Полный релиз | Июнь 2026 | ⬜ Не начат |

---

## Агенты системы
| Агент | Папка | Когда вызывать |
|---|---|---|
| PM / Оркестратор | docs_web/ | Управление проектом, задачи, встречи |
| UX/UI Дизайнер | UI_assets/ | Wireframes, макеты, прототипы |
| Frontend Dev | dashboard/ | Код дашборда (React/TS) |
| R&D Researcher | research/ | Вопросы по железу, SDK, метрикам |
```

- [ ] **Шаг 2: Закоммитить**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git add PROJECT_STATE.md
git commit -m "Добавил PROJECT_STATE.md с текущим состоянием проекта"
```

---

## Task 3: Создать файлы tasks/, milestones/, decisions/, people/

**Files:**
- Create: `NEIRY/knowledge-base/tasks/konstantin.md`
- Create: `NEIRY/knowledge-base/tasks/kirill.md`
- Create: `NEIRY/knowledge-base/tasks/nikita.md`
- Create: `NEIRY/knowledge-base/milestones/m1.md`
- Create: `NEIRY/knowledge-base/milestones/m2.md`
- Create: `NEIRY/knowledge-base/milestones/m3.md`
- Create: `NEIRY/knowledge-base/decisions/2026-05.md`
- Create: `NEIRY/knowledge-base/open-questions/index.md`
- Create: `NEIRY/knowledge-base/people/index.md`

- [ ] **Шаг 1: Создать tasks/konstantin.md**

```markdown
# Задачи: Константин Соломонов

## Активные

### M1 (до 2026-05-18)
- [ ] Wireframes M1 → отправить Кириллу → Никите
  - Источник: встреча 12.05 | Исполнитель: Константин
- [ ] Нестыковки в документах — исправить:
  - `neiry_pulse_3.html`: «Mobile (Android + iOS)» → iOS только в M2
  - `neiry_pulse_3.html`: «Регистрация по email/пароль» → нет до M3

### Без дедлайна
- [ ] Документ `Neiry_Ecosystem_Sync.md` — три секции
- [ ] Прободаться с юрдотделом Никиты: 30% передача прав, 25% отказ, портфолио, исключительные права с момента полной оплаты
- [ ] Покурить Wikipedia G-Band SDK → передать в research/sdk/
- [ ] Wireframes M2 → Кирилл → Никита

## Выполненные
- [x] Создать группу Константин + Кирилл + Никита для договоров — 13.05 ✅
- [x] Отправить оба договора в группу — 13.05 ✅
```

- [ ] **Шаг 2: Создать tasks/kirill.md**

```markdown
# Задачи: Кирилл Ляпин

## Активные

### M1 (до 2026-05-18)
- [ ] Черновые эндпоинты авторизации и синхронизации
- [ ] Foreground service (уведомление) в Android — фоновая работа без обрыва BLE
- [ ] Ответить: как ведёт себя браслет при уходе приложения в фон, рвёт ли BLE?
- [ ] Архивные HRV: разобраться с привязкой пользователя (рост/вес/возраст → причина нулей)

## Выполненные
- [x] Тестовый сервер-заглушка (echo + Hello World) — 12.05 ✅
- [x] Скрины тестового Android-приложения → передал Константину — 12.05 ✅
```

- [ ] **Шаг 3: Создать tasks/nikita.md**

```markdown
# Задачи: Никита

## Активные
- [ ] Ответить по правкам договора (30% передача прав, 25% отказ, портфолио)

## Заметки
- Никита — заказчик/партнёр по разработке
- ТЗ Никиты содержит Celery/Redis — решено исключить из MVP (подтвердить в договоре)
```

- [ ] **Шаг 4: Создать milestones/m1.md**

```markdown
# M1 — Tech Demo
**Дедлайн:** 2026-05-18  
**Событие:** внутренняя демонстрация  
**Статус:** 🟡 В работе

## Скоуп
- Android only (iOS в M2)
- Нет авторизации (хэш/MAC-адрес устройства)
- Dashboard: только BPM в реальном времени
- Bluetooth подключён, работает: BPM, давление, SpO2 (внутри приложения)
- Публично на дашборде — только BPM (по ТЗ)

## Wireframes
- mobile-registration, mobile-login, mobile-ble-pairing, mobile-home
- dashboard-login, dashboard-users

## Нестыковки (исправить до дедлайна)
- [ ] neiry_pulse_3.html чеклист M1: «Mobile (Android + iOS)» → только Android
- [ ] neiry_pulse_3.html секция 04: «Регистрация по email/пароль» → нет до M3

## Готово
- WebSocket с resilient reconnect ✅
- BPM-график с историей ✅
- Карточки пользователей ✅
- Bluetooth: базовые характеристики на Android ✅
```

- [ ] **Шаг 5: Создать milestones/m2.md**

```markdown
# M2 — Startup Village
**Дедлайн:** 2026-05-25  
**Событие:** Startup Village (публичная демонстрация)  
**Статус:** ⬜ Не начат

## Скоуп
- iOS добавляется в M2
- Нет авторизации (хэш/MAC)
- ВСР (HRV): показываем архивные данные (сутки/3 дня/неделя) — ❓ уточнить
- Dashbord: BPM + возможно архивный HRV

## Открытые вопросы
- ❓ ВСР в M2 — показываем архивный HRV или нет? (@Константин + @Кирилл)
```

- [ ] **Шаг 6: Создать milestones/m3.md**

```markdown
# M3 — Полный релиз
**Дедлайн:** Июнь 2026  
**Статус:** ⬜ Планирование

## Скоуп
- Полная авторизация (email/пароль)
- Потоковый HRV
- Полный набор метрик: BPM, давление, SpO2, HRV
- Финальные договорённости по SDK и архитектуре
```

- [ ] **Шаг 7: Создать decisions/2026-05.md**

```markdown
# Решения — Май 2026

## 2026-05-12 — Технический синк (Константин + Кирилл)

| Решение | Детали |
|---|---|
| HRV потоковый не нужен для M1/M2 | Фокус на архивных данных (сутки/3 дня/неделя). К M3. |
| Авторизация отсутствует до M3 | Используется хэш/MAC-адрес устройства |
| iOS только в M2 | M1 — Android only |
| Celery/Redis — не нужны для MVP | Исключить из ТЗ Никиты. Уточнить в договоре. |
| Память браслета офлайн | 64 МБ |
| Причина нулей в архивных HRV | Нужно правильно ввести рост/вес/возраст пользователя |
```

- [ ] **Шаг 8: Создать open-questions/index.md**

```markdown
# Открытые вопросы

## Активные

### ❓ Celery/Redis в договоре
**Вопрос:** Решено что не нужны для MVP — зафиксировано ли это в договоре/ТЗ?  
**Ответственный:** @Константин  
**Источник:** встреча 12.05

### ❓ ВСР в M2
**Вопрос:** Показываем архивный HRV на Startup Village (M2) или нет?  
**Ответственные:** @Константин + @Кирилл  
**Источник:** встреча 12.05

## Закрытые
_(пусто)_
```

- [ ] **Шаг 9: Создать people/index.md**

```markdown
# Команда проекта

## Константин Соломонов
**Роль:** Product & Design Lead (PM, договоры, wireframes)  
**Контакт:** c.dvugroshev@gmail.com

## Кирилл Ляпин
**Роль:** Engineering Lead (Flutter мобайл + бэкенд)

## Никита
**Роль:** Заказчик / партнёр по разработке  
**Контекст:** Составил ТЗ (содержит Celery/Redis — исключить из MVP). Договоры на согласовании.
```

- [ ] **Шаг 10: Закоммитить всё**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git add .
git commit -m "Добавил задачи, milestones, решения, команду из встречи 12.05"
```

---

## Task 4: Создать R&D Researcher агент

**Files:**
- Create: `NEIRY/research/CLAUDE.md`
- Create: `NEIRY/research/INDEX.md`
- Create: `NEIRY/research/lessons-learned.md`
- Create: `NEIRY/research/BRIEF.md`
- Create: `NEIRY/research/hardware/`, `sdk/`, `metrics/`, `sources/`

- [ ] **Шаг 1: Создать структуру папок**

```bash
mkdir -p /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/{hardware,sdk,metrics,sources}
touch /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/hardware/.gitkeep
touch /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/sdk/.gitkeep
touch /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/metrics/.gitkeep
touch /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/sources/.gitkeep
```

- [ ] **Шаг 2: Создать research/CLAUDE.md**

Создать файл `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/CLAUDE.md`:

```markdown
# R&D Researcher — Neiry Pulse

Я — исследователь. Изучаю железо (браслеты, сенсоры), SDK, протоколы, метрики здоровья.
Объясняю сложное простым языком — без жаргона, как будто объясняю умному PM.

## Identity
- **Роль:** накапливать знания, отвечать на вопросы, исследовать новое
- **НЕ делаю:** пишу production-код, трогаю backend/ или mobile/
- **Стиль ответов:** простой язык, аналогии, примеры. Если термин технический — объясняю его.

## Session Start
1. Прочитать `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/INDEX.md` — что уже знаем
2. Прочитать `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/lessons-learned.md`
3. Проверить `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/BRIEF.md` — есть ли задание от PM
4. Если есть BRIEF — выполнить, сохранить результат, очистить BRIEF

## Как сохранять знания
После каждого исследования обновлять нужный файл:
- **Железо** → `hardware/<название>.md`
- **SDK** → `sdk/<название>.md`
- **Метрики** → `metrics/<метрика>.md` (BPM, HRV, SpO2, давление)
- **Сырые источники** → `sources/<дата>-<тема>.md`

Обновить `INDEX.md` — добавить строку о новом файле.

## Tools
- `~/.local/bin/parallel-cli search "запрос"` — быстрый веб-поиск
- `~/.local/bin/parallel-cli research "вопрос"` — глубокий research
- `~/.local/bin/parallel-cli fetch "https://..."` — извлечь контент URL

## Контекст проекта
Neiry Pulse — носимый браслет для мониторинга биометрики. Ключевые метрики: BPM, HRV (ВСР), SpO2, давление. SDK — предположительно G-Band. Bluetooth (BLE). Android в M1, iOS в M2.

Knowledge base: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/PROJECT_STATE.md`
```

- [ ] **Шаг 3: Создать research/INDEX.md**

```markdown
# R&D Knowledge Base — INDEX

_Последнее обновление: 2026-05-16_

## Железо (hardware/)
_(пусто — ждём первого исследования)_

## SDK (sdk/)
_(пусто — задача: покурить G-Band SDK)_

## Метрики здоровья (metrics/)
_(пусто — приоритет: BPM, HRV, SpO2)_

## Сырые источники (sources/)
_(пусто)_

---
## Что исследовать в первую очередь
1. G-Band SDK — методы, архитектура, как получать данные
2. HRV (ВСР) — как считается, какие методы, нормы
3. SpO2 — принцип работы сенсора, точность
4. Браслет Neiry — спецификации, память (64 МБ), BLE-профиль
```

- [ ] **Шаг 4: Создать research/lessons-learned.md**

```markdown
# Lessons Learned — R&D Researcher

_Читать перед началом каждой сессии._

## Шаблон записи
```
## ГГГГ-ММ-ДД — [Краткое описание]
Проблема: что пошло не так или что было неочевидно
Правило: что делать по-другому
```

_(записи появятся после первых исследований)_
```

- [ ] **Шаг 5: Создать research/BRIEF.md**

```markdown
# BRIEF — R&D Researcher

_PM пишет сюда задание. После выполнения — очистить этот файл._

## Статус
Нет активного задания.
```

- [ ] **Шаг 6: Проверить структуру**

```bash
find /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research -type f | sort
```

Ожидаемый вывод: CLAUDE.md, INDEX.md, BRIEF.md, lessons-learned.md + .gitkeep в 4 папках.

---

## Task 5: Обновить docs_web/CLAUDE.md — PM-агент

**Files:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/CLAUDE.md`

- [ ] **Шаг 1: Прочитать текущий CLAUDE.md**

Прочитать `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/CLAUDE.md` — убедиться в текущем содержании.

- [ ] **Шаг 2: Добавить секцию Knowledge Base и Session Start**

Добавить в конец файла `CLAUDE.md` (перед финальной строкой «Если не уверен — спроси»):

```markdown
## Knowledge Base
- Центр знаний: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/`
- Живой снимок проекта: `knowledge-base/PROJECT_STATE.md` — читать при старте каждой сессии
- INBOX для новых материалов: `knowledge-base/INBOX/`

## Session Start (выполнять каждую сессию)
1. Прочитать `knowledge-base/PROJECT_STATE.md`
2. Проверить `knowledge-base/INBOX/` на новые файлы — обработать если есть
3. Прочитать собственный `memory/` (если есть новые записи)
4. Создать `.session-lock` файл: `touch knowledge-base/.session-lock`

## Session End (выполнять перед закрытием)
1. Обновить `knowledge-base/PROJECT_STATE.md` — отразить изменения сессии
2. Удалить `.session-lock`: `rm knowledge-base/.session-lock`
3. Закоммитить изменения в knowledge-base

## Права PM
PM имеет право читать и обновлять `CLAUDE.md` и `lessons-learned.md` любого субагента:
- `UI_assets/claude.md` — UX/UI Дизайнер
- `dashboard/claude.md` — Frontend Developer
- `research/CLAUDE.md` — R&D Researcher

После обновления инструкций — коммит с описанием что и зачем изменено.

## Делегирование субагентам
Когда нужно передать задачу субагенту:
1. Написать бриф в `<папка_агента>/BRIEF.md`
2. Запустить субагента через Agent tool с рабочей директорией агента
3. После выполнения — прочитать результат, обновить PROJECT_STATE.md
4. Очистить BRIEF.md субагента

Папки субагентов:
- UX/UI Дизайнер: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/`
- Frontend Dev: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/`
- R&D Researcher: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/`
```

- [ ] **Шаг 3: Закоммитить**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web
git add CLAUDE.md
git commit -m "Обновил CLAUDE.md PM-агента: knowledge-base, session start/end, делегирование"
```

---

## Task 6: Обновить UI_assets/claude.md — UX/UI Дизайнер

**Files:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/claude.md`
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/lessons-learned.md`
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/BRIEF.md`

- [ ] **Шаг 1: Добавить в конец UI_assets/claude.md**

Добавить перед финальной строкой «Если не уверен — спроси»:

```markdown
## Knowledge Base
- Живой снимок проекта: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/PROJECT_STATE.md`
- Текущие wireframe-задания: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/BRIEF.md`

## Session Start
1. Прочитать `BRIEF.md` — есть ли задание от PM?
2. Если задание есть — прочитать `knowledge-base/PROJECT_STATE.md` для контекста
3. Прочитать `lessons-learned.md` — избежать прошлых ошибок
4. Если задания нет — ждать BRIEF от PM

## Self-Learning
После каждой сессии: если допустил ошибку или нашёл неочевидное правило — добавить в `lessons-learned.md`.
```

- [ ] **Шаг 2: Создать UI_assets/lessons-learned.md**

```markdown
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
```

- [ ] **Шаг 3: Создать UI_assets/BRIEF.md**

```markdown
# BRIEF — UX/UI Дизайнер

_PM пишет сюда задание. После выполнения — очистить этот файл._

## Статус
Нет активного задания.
```

---

## Task 7: Обновить dashboard/claude.md — Frontend Developer

**Files:**
- Modify: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/claude.md`
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/lessons-learned.md`
- Create: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/BRIEF.md`

- [ ] **Шаг 1: Добавить в конец dashboard/claude.md**

Добавить перед «## Context7»:

```markdown
## Knowledge Base
- Живой снимок проекта: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/PROJECT_STATE.md`
- Задания от PM: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/BRIEF.md`
- Текущие milestones: `knowledge-base/milestones/`

## Session Start
1. Прочитать `BRIEF.md` — есть ли задание от PM?
2. Если задание есть — прочитать `knowledge-base/milestones/m1.md` для контекста скоупа
3. Прочитать `lessons-learned.md`
4. Если задания нет — ждать BRIEF

## Self-Learning
После каждой сессии: если нашёл нетривиальное решение или ошибку — добавить в `lessons-learned.md`.
```

- [ ] **Шаг 2: Создать dashboard/lessons-learned.md**

```markdown
# Lessons Learned — Frontend Developer

_Читать перед началом каждой сессии._

## Шаблон записи
```
## ГГГГ-ММ-ДД — [Краткое описание]
Проблема: что пошло не так
Правило: что делать по-другому
```

## 2026-05-16 — WebSocket reconnect
Проблема: браузер закрывает WS при потере фокуса вкладки.
Правило: всегда реализовывать exponential backoff reconnect в useWebSocket hook. Уже реализовано — не удалять.
```

- [ ] **Шаг 3: Создать dashboard/BRIEF.md**

```markdown
# BRIEF — Frontend Developer

_PM пишет сюда задание. После выполнения — очистить этот файл._

## Статус
Нет активного задания.
```

---

## Task 8: Настроить Stop hook в Claude Code

**Files:**
- Modify: `~/.claude/settings.json`

- [ ] **Шаг 1: Прочитать текущий settings.json**

Прочитать `~/.claude/settings.json` чтобы понять текущую структуру.

- [ ] **Шаг 2: Добавить Stop hook**

В секцию `hooks` добавить Stop hook. Если секции `hooks` нет — создать. Hook выводит напоминание сохранить состояние:

```json
"hooks": {
  "Stop": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "echo '⚠️  СЕССИЯ ЗАВЕРШАЕТСЯ. Если работал с Neiry: 1) Обнови knowledge-base/PROJECT_STATE.md 2) rm knowledge-base/.session-lock 3) git commit в knowledge-base'"
        }
      ]
    }
  ]
}
```

- [ ] **Шаг 3: Проверить что settings.json валидный JSON**

```bash
python3 -m json.tool ~/.claude/settings.json > /dev/null && echo "JSON valid"
```

Ожидаемый вывод: `JSON valid`

---

## Task 9: Первичная загрузка — транскрипция встречи

**Files:**
- Source: `NEIRY/docs_web/meetings and transcipts/Звонок 12.05. Кирилл и Константин. Интеграция браслета и договоры.txt`
- Target: `knowledge-base/INBOX/meetings/2026-05-12-kirill-konstantin.txt`

> Данные из этой встречи уже загружены вручную в Task 2-3. Этот таск — переместить исходник в правильное место и зафиксировать как "обработано".

- [ ] **Шаг 1: Скопировать транскрипцию в INBOX**

```bash
cp "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/meetings and transcipts/Звонок 12.05. Кирилл и Константин. Интеграция браслета и договоры.txt" \
   "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/INBOX/meetings/2026-05-12-kirill-konstantin.txt"
```

- [ ] **Шаг 2: Создать запись об обработанной встрече**

Создать `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/INBOX/meetings/2026-05-12-kirill-konstantin.processed.md`:

```markdown
# Встреча обработана: 2026-05-12 Кирилл + Константин

**Исходный файл:** `2026-05-12-kirill-konstantin.txt`  
**Обработано:** 2026-05-16  
**Статус:** ✅ Данные разнесены по knowledge-base

## Куда попали данные
- Задачи Константина → `tasks/konstantin.md`
- Задачи Кирилла → `tasks/kirill.md`
- Решения → `decisions/2026-05.md`
- Открытые вопросы → `open-questions/index.md`
- Нестыковки в документах → `milestones/m1.md`
- Статус M1 → `PROJECT_STATE.md`
```

- [ ] **Шаг 3: Закоммитить**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git add .
git commit -m "Добавил транскрипцию встречи 12.05 и пометил как обработанную"
```

---

## Task 10: Первичная загрузка — Excel метрики

**Files:**
- Source: `NEIRY/docs_web/Neiry_Vitro_Supplier_Questions.docx` + `Neiry_Vitro_Metrics_Registry_v0.2.xlsx`
- Target: `knowledge-base/INBOX/raw/` + `research/sources/`

- [ ] **Шаг 1: Скопировать файлы в INBOX**

```bash
cp "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/Neiry_Vitro_Metrics_Registry_v0.2.xlsx" \
   "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/INBOX/raw/"
```

- [ ] **Шаг 2: Создать задание для R&D Researcher**

Написать в `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/BRIEF.md`:

```markdown
# BRIEF — R&D Researcher

## Статус
🔴 Активное задание от PM (2026-05-16)

## Задание: Обработать Vitro Metrics Registry

**Файл:** `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/INBOX/raw/Neiry_Vitro_Metrics_Registry_v0.2.xlsx`

**Что нужно:**
1. Открыть файл, изучить структуру
2. Создать `metrics/vitro-metrics-registry.md` — описание всех метрик простым языком
3. Для каждой метрики: название, что измеряет, единицы, нормы, как используется в Neiry Pulse
4. Обновить `INDEX.md`

**Ожидаемый результат:** `research/metrics/vitro-metrics-registry.md`
```

- [ ] **Шаг 3: Отметить задание**

Добавить в `knowledge-base/PROJECT_STATE.md` в раздел «Открытые задачи»:

```markdown
### R&D Researcher (ожидает обработки)
- [ ] Обработать Neiry_Vitro_Metrics_Registry_v0.2.xlsx → research/metrics/vitro-metrics-registry.md
```

---

## Task 11: Финальная проверка системы

- [ ] **Шаг 1: Проверить структуру knowledge-base**

```bash
find /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base -not -path '*/.git/*' -type f | sort
```

Ожидаемый вывод — все `.md` файлы и `.gitkeep` файлы в нужных папках.

- [ ] **Шаг 2: Проверить структуру research/**

```bash
find /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research -type f | sort
```

Ожидаемый вывод: `CLAUDE.md`, `INDEX.md`, `BRIEF.md`, `lessons-learned.md` + `.gitkeep` в 4 папках.

- [ ] **Шаг 3: Проверить что у всех агентов есть BRIEF.md и lessons-learned.md**

```bash
ls /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/{BRIEF.md,lessons-learned.md}
ls /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/{BRIEF.md,lessons-learned.md}
ls /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/research/{BRIEF.md,lessons-learned.md,CLAUDE.md,INDEX.md}
```

Ожидаемый вывод: все файлы найдены, нет «No such file».

- [ ] **Шаг 4: Симуляция старта сессии PM-агента**

Открыть новую сессию Claude Code в директории `docs_web/`. Проверить что агент:
1. Упоминает чтение `PROJECT_STATE.md` в начале
2. Знает текущий milestone (M1, дедлайн 18.05)
3. Видит открытые задачи

- [ ] **Шаг 5: Итоговый коммит в docs_web**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web
git add .
git commit -m "Завершил настройку мульти-агентной системы: knowledge-base, research агент, обновил все CLAUDE.md"
```

- [ ] **Шаг 6: Итоговый коммит в knowledge-base**

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base
git add .
git commit -m "Финальная проверка: knowledge-base готов к работе"
```

---

## После завершения: Настройка Obsidian

Это ручные шаги — займут 5-10 минут:

1. `Obsidian → Open another vault → Open folder as vault` → выбрать `NEIRY/knowledge-base/`
2. `Settings → Community plugins → Browse` → установить: **Dataview**, **Tasks**, **Templater**, **Calendar**, **Obsidian Git**
3. `Settings → Obsidian Git → Auto backup interval: 15`
4. Переключение между Second Brain и Neiry KB — иконка хранилища в левом нижнем углу Obsidian
