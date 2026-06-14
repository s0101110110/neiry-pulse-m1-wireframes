# INSTALL-SKILLS — Установка дизайн-skills для UI-агента

**Версия:** 2026-06-01 · **Автор:** PM (Дирижёр) · **Статус:** ждёт согласования PM перед выполнением

---

## Цель

Дать UI-агенту три внешних skill'а, которые повышают качество frontend-вывода (моушн, anti-slop, taste), **не ломая** существующую дизайн-систему Neiry Pulse M2.

**Главное условие:** никакого `init` / `document` / `craft` / `extract` — эти команды переписывают артефакты. Используем только режимы аудита и polish'а.

---

## Что ставим (whitelist)

| Skill | Источник | Зачем | Размер |
|---|---|---|---|
| `emil-design-eng` | `emilkowalski/skill` | Моушн-фреймворк, easings, durations, spring-физика, button :active, popover origin, tooltip skip-delay | ~27 KB |
| `impeccable` (частично) | `pbakaus/impeccable` | Anti-AI-slop rules, 7 reference-доменов (typography/color/motion/spatial/interaction/responsive/ux-writing), команды polish/critique/audit | ~150 KB (загружается on-demand) |
| `redesign-existing-projects` | `Leonxlnx/taste-skill` | Audit-then-fix для итераций по существующему UI | ~30 KB |

**Что НЕ ставим:**
- Дефолт `taste-skill` (`design-taste-frontend`) — он явно не для дашбордов, переключит на лендинг-режим.
- `taste-skill-v1`, `gpt-tasteskill`, `brutalist-skill`, `soft-skill`, `stitch-skill`, `output-skill`, `minimalist-skill` — лишние варианты, дубль логики или конфликт эстетики.
- Image-generation skills (`imagegen-frontend-web/mobile`, `brandkit`) — пока не нужны, при появлении задач на мудборд поставим отдельно.

---

## Token Economy (правила экономии)

1. **Skills загружаются on-demand** через Skill tool — пока не вызываешь, в контексте их нет.
2. **Не вызывай `impeccable craft`** — он подгружает большой reference + 4–6 файлов. Используй точечные команды: `polish`, `critique`, `audit`, `animate`, `harden`, `quieter`, `bolder`, `distill`.
3. **Не запускай два skill'а подряд на одной задаче** — выбери один по типу задачи (см. матрицу ниже).
4. **emil-design-eng** маленький, можно вызывать часто.

### Матрица выбора skill по задаче

| Задача | Какой skill |
|---|---|
| Анимация модалки / drill-down / gauge / button feedback | `emil-design-eng` |
| Проверка готового экрана на anti-slop тэги (gradient text, card-in-card, eyebrow на секцию) | `impeccable critique` |
| Технический аудит (a11y, контраст, responsive) | `impeccable audit` |
| Финальная вычистка перед коммитом | `impeccable polish` |
| Усилить «бледную» область | `impeccable bolder` |
| Приглушить перегруженный экран | `impeccable quieter` |
| Edge cases (overflow, i18n, error states) | `impeccable harden` |
| Перерисовать существующий kiosk-блок без потери ДНК | `redesign-existing-projects` |

---

## Хард-баны (RED)

- ❌ **Не вызывай `/impeccable init`** — создаёт `PRODUCT.md` + `DESIGN.md` в корне репо. У нас уже есть память `kiosk-design-system` и `wireframes/m2/ui-kit.html` как source of truth.
- ❌ **Не вызывай `/impeccable document`** — генерирует DESIGN.md по коду, может затереть наш `ui-kit.html`.
- ❌ **Не вызывай `/impeccable craft`** — полный end-to-end build, перепишет компоненты. Только если PM явно сказал «делай через craft».
- ❌ **Не вызывай `/impeccable extract`** — может вытащить «компоненты» в design system, который у нас уже зафиксирован.
- ❌ **Не предлагай менять токены** (`--background`, `--primary` = `#831843`, шрифты Space Grotesk / Onest / Geist Mono) — это утверждённая палитра M2.
- ❌ **Не меняй wine accent** `#831843` — это brand-якорь Neiry, защищён памятью `project_neiry_ui_aesthetic`.
- ❌ **Не применяй skill-правила «всегда» — только когда PM поставил задачу через тот же skill.** Если PM пишет «улучши drilldown» без указания skill — спроси какой использовать.

---

## Установка (только после "ОК" от PM)

### Шаг 1 — emil-design-eng (минимальный риск)

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets
npx skills add https://github.com/emilkowalski/skill
```

Проверка: должен появиться `.claude/skills/emil-design-eng/SKILL.md`. PM проверяет ls + reads SKILL.md frontmatter.

### Шаг 2 — impeccable через CLI (среднее воздействие)

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets
npx impeccable skills install
```

CLI сам определит harness (Claude Code) и положит в `.claude/skills/impeccable/`. Проверка: PM делает `ls .claude/skills/impeccable/` и читает первые 50 строк `SKILL.md` — убедиться, что не запускался setup-скрипт `context.mjs` (он бы потребовал PRODUCT.md).

**После установки:** PM делает ручную проверку — попросить агента `/impeccable critique wireframes/m2/kiosk.html` на одном экране, посмотреть, что вывод адекватный, не ломает ничего.

### Шаг 3 — только redesign-skill из taste-skill (точечная установка)

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets
npx skills add https://github.com/Leonxlnx/taste-skill --skill "redesign-existing-projects"
```

**Не использовать** `npx skills add https://github.com/Leonxlnx/taste-skill` без `--skill` — он притянет все 10+ вариантов.

---

## Smoke-test после установки

Агент должен последовательно:

1. `ls .claude/skills/` — показать список (должно быть 3 папки: `emil-design-eng`, `impeccable`, `redesign-existing-projects`).
2. Сделать `Skill emil-design-eng` без аргументов — посмотреть, что выдаётся вводное сообщение про animations.dev (это его «здравствуй»-сообщение, нормально).
3. На одном экране (PM укажет каком) попробовать `Skill impeccable args: "critique <путь>"` — короткий аудит-вывод, без правок файлов.
4. Доложить PM: `DONE / DONE_WITH_CONCERNS / BLOCKED` + что именно skill'ы видят в проекте.

PM проверяет вывод и даёт acceptance. Только после acceptance — skill'ы становятся доступны для боевых задач.

---

## PM Acceptance Gate (двойная проверка)

После каждой установки (шаг 1, 2, 3):
- ❗ **Не переходить к следующему шагу без явного «ОК» PM.**
- ❗ **Не вызывать skill'ы на боевые артефакты** (kiosk.html, drilldown, ui-kit) до завершения всех 3 шагов и acceptance.
- ❗ **Никаких коммитов в этой ветке без PM** — `.claude/skills/*` добавится в gitignore проверочной командой (см. ниже).

### Gitignore-проверка

После шага 2 убедиться, что `.claude/skills/` не попадает в коммиты основного репо `docs_web`:

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets
cat .gitignore | grep -E "\.claude|skills" || echo "Добавить .claude/skills/ в .gitignore"
```

---

## После acceptance — обновление claude.md

PM сам внесёт правки в `UI_assets/claude.md`, добавив раздел «Skills» с whitelist команд и RED-блоком. Агент не правит свой claude.md.

---

## Если что-то пошло не так

**Откат:** удалить установленные skill'ы.

```bash
cd /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets
rm -rf .claude/skills/emil-design-eng
rm -rf .claude/skills/impeccable
rm -rf .claude/skills/redesign-existing-projects
```

После отката — доложить PM что именно сломалось (ошибка установки, конфликт с существующими файлами, неожиданное поведение).

---

## Не делать

- Не запускать установку без явного «ОК» PM на каждый шаг.
- Не применять skill-правила к артефактам без поручения PM.
- Не править свой `claude.md` — это делает PM.
- Не коммитить `.claude/skills/` в репо `docs_web`.
- Не задавать вопросы по содержимому skill'ов — там сотни правил, читаем по требованию задачи, а не превентивно.
