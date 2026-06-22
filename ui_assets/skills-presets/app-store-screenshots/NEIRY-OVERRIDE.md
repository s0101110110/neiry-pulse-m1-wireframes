# NEIRY-OVERRIDE — Project-specific defaults для app-store-screenshots

**Версия:** 2026-06-20
**Назначение:** этот override применяется КАЖДЫЙ раз, когда скилл `app-store-screenshots` запускается в репозитории Neiry Pulse. Он перетирает дефолтные шрифты/темы шаблона нашими токенами.

Файл живёт внутри установленного скилла, рядом с `SKILL.md`. Если скилл будет обновлён (`npx skills update`), этот файл может быть перезатёрт — в таком случае восстанови его из канонической копии в репо: `UI_assets/skills-presets/app-store-screenshots/NEIRY-OVERRIDE.md`.

---

## Hard rules (обязательны до Step 1 Q&A)

Когда агент видит триггер «app store screenshots / play store / phone mockup» и работает в директории Neiry Pulse:

1. **Не задавай Step 1 Q5 (Style direction).** Стиль уже определён: `neiry-pulse` (см. ниже).
2. **Не предлагай named deep-spec styles** из `style-prompts/` (Rubberhose, K-Beauty, Skeuomorphic и т. д.) — они для других проектов.
3. **Не задавай Q11 (Brand colors / font).** Брендовые токены задокументированы здесь.
4. **Не задавай Q9 (Localized screenshots).** На M3 — только `ru`. Английский откладывается до пост-M4.
5. **Не запускай мульти-локаль вообще** — даже если шаблон поддерживает массив `locales`, оставь `["ru"]`.

## Brand tokens (single source of truth)

### Шрифты (утверждены Никитой 17.06.2026)

- **UI / body / headings:** `Golos Text` (weights `400`, `500`, `600`, `700`) — Google Fonts
- **Mono / labels / numbers / eyebrow:** `JetBrains Mono` (weights `400`, `500`, `600`, `700`) — Google Fonts
- **Запрещены fallback'ы:** Inter, SF Pro, Space Grotesk, Geist Mono, Onest. Если Google Fonts недоступен — system-ui, не подменять на схожий гротеск.

### Цвета (semantic tokens M3, light theme is default)

| Token | HEX | HSL (для tailwind) | Назначение |
|---|---|---|---|
| `--background` | `#f7f5ef` | `42 33% 95%` | основной фон |
| `--foreground` | `#0c0a09` | `24 10% 4%` | основной текст |
| `--card` | `#ffffff` | `0 0% 100%` | фон карточек |
| `--card-warm` | `#faf8f3` | `42 33% 97%` | тёплый вариант карточки |
| `--muted` | `#f1ede4` | `42 26% 92%` | muted-плашки |
| `--muted-foreground` | `#78716c` | `25 5% 45%` | secondary текст |
| `--border` | `#e8e4d8` | `42 23% 88%` | базовая граница |
| `--border-strong` | `#d4cfc0` | `42 17% 79%` | strong-граница |
| `--primary` | `#831843` | `336 70% 31%` | **wine — PROTECTED, единственный accent** |
| `--primary-foreground` | `#ffffff` | `0 0% 100%` | текст на wine |
| `--primary-soft` | `#fdf2f8` | `327 73% 97%` | wine-tinted фон |
| `--success` | `#65a30d` | `84 84% 35%` | OK-состояния |
| `--warning` | `#d97706` | `28 92% 44%` | предупреждения |
| `--destructive` | `#b91c1c` | `0 74% 42%` | критические |

**Защищённые элементы:**
- Wine `#831843` — единственный accent. Никаких градиентов, никаких побочных accent-цветов.
- Фон `#f7f5ef` — Bevel-tone, не белый, не серый.
- Нет shadcn neutral palette по умолчанию (`zinc`/`slate` для бэкграунда — НЕТ).

## Neiry-preset (готовое наполнение для scaffold)

После шага `cp -R <SKILL_DIR>/template/. <PROJECT>/` агент **обязан** применить три patch-файла. Они лежат в репо по пути:

```
UI_assets/skills-presets/app-store-screenshots/
├── globals.css       → копируется в src/app/globals.css
├── layout.tsx        → копируется в src/app/layout.tsx
└── constants-patch.ts → инструкция, какие строки заменить в src/lib/constants.ts
```

### Применение (после `cp template/. ./`)

```bash
PRESET_DIR="/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/skills-presets/app-store-screenshots"
cp "$PRESET_DIR/globals.css" src/app/globals.css
cp "$PRESET_DIR/layout.tsx" src/app/layout.tsx
# constants.ts: см. инструкцию в constants-patch.ts (там diff-блок) — добавить тему "neiry-pulse" в THEMES, перевести DEFAULT_THEME_ID на "neiry-pulse"
```

После этих трёх правок:
- `next/font/google` импорт переключается с `Inter` на `Golos_Text` + `JetBrains_Mono`
- CSS-переменные в globals.css перепишутся на Neiry-tokens (light theme, dark откладываем)
- Тема `neiry-pulse` появится в editor toolbar как single preset, дефолт

## Project state seed

Когда (опционально, Step 2.5) скилл генерирует `app-store-screenshots.json`:

```json
{
  "schemaVersion": 2,
  "appName": "Neiry Pulse",
  "themeId": "neiry-pulse",
  "connectedCanvas": true,
  "locale": "ru",
  "locales": ["ru"],
  "device": "iphone"
}
```

`tagline` / `headlines` — пусть PM напишет копию в editor, не угадывай.

## Что НЕ переписываем

- `mockup.png` (iPhone bezel) — оставляем дефолтный из скилла. У нас собственные device frames внутри wireframes, но для store-скриншотов идёт нативный Apple-bezel из скилла, это правильно.
- `tailwind.config.ts` — использует CSS-переменные через `hsl(var(--*))`, перетирать не нужно. Переменные меняются в `globals.css`.
- Логика export (html-to-image), canvas dimensions, EXPORT_SIZES — не трогаем.

## Если скилл обновится

После `npx skills update app-store-screenshots`:
1. Проверить, что `NEIRY-OVERRIDE.md` всё ещё на месте; если нет — восстановить из `UI_assets/skills-presets/app-store-screenshots/NEIRY-OVERRIDE.md`.
2. Сравнить новый `template/src/lib/constants.ts` с patched-версией в preset — если структура `THEMES` изменилась, переписать `constants-patch.ts`.
3. Сравнить `template/src/app/layout.tsx` и `globals.css` с preset-копиями — обновить preset, если шаблон сильно перерисован.

PM решает, переходить ли на новую версию.

## Gap (важно для PM)

Скилл работает как **Next.js scaffold-генератор** + **interactive browser editor**. Финальный PNG-экспорт делается человеком через UI editor'а кликом по «Export bundle». Это значит:

- Полностью headless / CLI-only генерация скриншотов **невозможна** без дополнительной автоматизации (Playwright/Puppeteer click-через-UI или собственный server-side renderer html-to-image).
- Для регулярной CI-генерации (например, перед каждым релизом в стор) нужно либо человек-в-петле, либо доп. инфраструктура.

Это документировано как открытый вопрос в `PLAYBOOK.md` секция «App Store / Google Play screenshots».
