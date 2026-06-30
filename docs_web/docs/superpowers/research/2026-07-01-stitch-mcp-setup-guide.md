# Google Stitch × MCP — Setup & Best-Practices Guide (для Neiry)

**Дата:** 2026-07-01 · **Источник:** parallel-cli deep research (`research run`, 58 цитат) + WebFetch официальных доков · **Сырьё:** `raw/stitch-deep-research-answer.md`
**Связано:** Anti-Generic Playbook (`UI_assets/anti-generic-playbook.md`, §Stitch-протокол)

> **TL;DR.** Stitch = ускоритель стадии Composition-first, не финальный инструмент. Его **главный рычаг против generic — файл `DESIGN.md`** (открытый формат, читают и Stitch, и Claude Code). Канонический MCP-пакет — **`@_davideast/stitch-mcp`** (David East, Google DevRel), НЕ `@google/stitch-mcp` (это ошибка сторонних гайдов). Связка против дрейфа: Figma MCP → DESIGN.md → Stitch MCP → код.

---

## 1. Канонический MCP-пакет (ВАЖНО)

Сторонние гайды называют разные пакеты (`stitch-mcp`, `@google/stitch-mcp`). **Документирован end-to-end только `@_davideast/stitch-mcp`** (David East, Google Cloud DevRel) — гайд `davideast.github.io/stitch-mcp/setup`. Используй его для новых установок.

~7 MCP-инструментов: `generate_screen_from_text`, `get_screen_code`, `get_screen_image`, `build_site`, `extract_design_context`, `list_projects`, `list_screens`.

## 2. Установка для Claude Code (рекомендуемый путь — init-wizard)

```bash
# 1. Запустить канонический мастер (9 шагов: клиент → транспорт → auth → scope → ping → doctor)
npx @_davideast/stitch-mcp init --client claude-code
```

**API-key режим (рекомендую для нас, проще):**
1. Войти на https://stitch.withgoogle.com (Google-аккаунт, владеющий ≥1 проектом).
2. Settings → **API Tokens** → **Generate New Token** → скопировать (хранить как приватный ключ).
3. ⚠️ Токен живёт **90 дней** — регенерировать перед запуском фичи, не словить cliff в середине.

Эквивалентный ручной конфиг (`~/.claude.json` user-scope или `.mcp.json` project-scope):
```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@_davideast/stitch-mcp", "proxy"],
      "env": {
        "STITCH_API_KEY": "your-token-here",
        "STITCH_PROJECT_ID": "your-project-id"
      }
    }
  }
}
```
или одной командой:
```bash
claude mcp add -e STITCH_API_KEY=your-token -e STITCH_PROJECT_ID=your-project -s user stitch -- npx -y @_davideast/stitch-mcp proxy
```

**OAuth-режим (альтернатива):** `init` ставит bundled gcloud SDK в `~/.stitch-mcp/` (отдельно от системного), сам гоняет `gcloud auth login` + `application-default login` + `gcloud beta services mcp enable stitch.googleapis.com`. Плюс — нет 90-дневного токена и нет ручного 1-часового refresh. Для нас API-key проще.

**Проверка:**
```bash
npx @_davideast/stitch-mcp doctor --verbose
```
Затем в Claude Code: «What tools do you have access to?» → должны быть `build_site`, `extract_design_context`, `generate_screen_from_text`, `get_screen_code`, `get_screen_image`, `list_projects`, `list_screens`.

**Типичные ошибки:** headless/SSH/WSL → скопировать OAuth URL в локальный браузер; `Server not found` → полный путь к `npx` (`/opt/homebrew/bin/npx`); `Authentication failed` → регенерировать токен (90 дней).

## 3. Парный сервер — Figma MCP (у нас подключён)

Официально Figma MCP — **OAuth remote** (`https://mcp.figma.com/mcp`), НЕ personal access token. Установка:
```bash
claude plugin install figma@claude-plugins-official      # предпочтительно
# или: claude mcp add --transport http figma https://mcp.figma.com/mcp
```

## 4. DESIGN.md — главный рычаг против generic ⭐

Открытый формат (Google открыл 2026-04-21). Плейн-маркдаун-манифест дизайн-системы: hex-цвета, типошкала, spacing, радиусы/тени, voice. **И Stitch, и Claude Code читают его.** Без DESIGN.md Stitch и даже Figma MCP дрейфуют к Material/iOS-дефолтам — это и есть источник generic.

**Наш план:** сделать `DESIGN.md` с токенами Neiry (cool-grey #F0F0F3, semantic colors, wine только brand-signal, Golos Text + Pulse Mono **только цифры**, контекстные радиусы 26/20/14, тени без бордеров) и положить в корень/`docs/`, закоммитить. Опц. усилить через генератор `designtoken.md` (CSS-vars + Tailwind + JSON-токены) — Stitch's нативный DESIGN.md всего ~30 строк, для плотных экранов нужен богаче.

## 5. Промпт-инжиниринг (официальные 4 правила)

| # | Правило | Cue |
|---|---|---|
| 1 | Выбрать «высоту» промпта осознанно (high-level исследует / detailed ограничивает) | «App for marathon runners to find races and training…» |
| 2 | Зафиксировать вайб прилагательными (пропагируются на все экраны) | «minimalist and focused», «vibrant and encouraging» |
| 3 | Якорить UI/UX-ключевыми существительными (Stitch парсит компонент-науны) | «navigation bar», «call-to-action button», «card layout» |
| 4 | **Одно крупное изменение за итерацию** (батч ломает цепочку наследования) | «primary CTA on the sign-up form» |

Итерационная петля: Seed → Steer (1 экран-правка) → Refine (1 компонент-правка) → Lock theme (1 промпт: primary+accent+font) → Image-pass.

## 6. Round-trip против дрейфа (3-сервер loop)

1. **Figma MCP** — прочитать живой дизайн-контекст: «Read the design system… return variables, components, Code Connect».
2. **Claude Code → DESIGN.md** — конвертировать Figma-переменные в DESIGN.md по нашей схеме.
3. **Stitch MCP** — генерить экраны: «read DESIGN.md and treat it as a HARD constraint, then screen-by-screen…».
4. **Figma MCP (write)** — вернуть фреймы в Figma с Auto Layout.
5. **Figma MCP** — сгенерить React по Code Connect mappings.
6. **Claude Code** — имплементировать из кодбейза.
7. **Loop for drift** — пере-прочитать DESIGN.md + Figma vars, diff против кода, поправить дрейфнувшие токены.

Механизм — «constraint stacking»: каждый промпт наследует DESIGN.md → прошлый экран → словарь Figma-компонентов. Без шага 1 Stitch отгружает pastel-Material, нарушающий бренд.

## 7. Лимиты и статус (на июнь 2026)

| Что | Значение |
|---|---|
| Free-квота | **550/мес** = 350 Standard (Gemini 2.5 Flash) + 200 Pro (Gemini 2.5 Pro). Старые гайды с «350» — до марта 2026. |
| API-токен | 90 дней TTL |
| Редактирование внутри Stitch | слабее Figma (Edit Text / Edit With AI) — доводка в Figma |
| Статус | Google **Labs** (procurement-риск). Платные тарифы — ожидаются **Q4 2026** (выход из Labs). |
| ⚠️ Июль 2026 | публичного апдейта НЕТ — не обещать команде июльский релиз. |

## 8. Вердикт для Neiry

**Подключать — да, но дисциплинированно.** Ценность Stitch = быстрые композиционные болванки на стадии Composition-first + MCP-мост в код. Условия (иначе generic): (1) **сделать брендовый DESIGN.md первым** — это решает 80% проблемы дрейфа; (2) только композиция, код доводим у себя; (3) taste-отбор вариантов; (4) round-trip через Figma MCP с re-grounding на DESIGN.md. Onboarding: день 1 — установка + прочесть Google prompt guide; день 2 — собрать наш DESIGN.md; день 3 — прогнать design-to-code на одном экране.

**Источники (топ):** `davideast.github.io/stitch-mcp/setup` · `stitch.withgoogle.com/docs/mcp/setup` · `blog.google/.../stitch-design-md` (DESIGN.md open-source) · `discuss.ai.google.dev/t/stitch-prompt-guide/83844` · полный список (58) — в `raw/stitch-deep-research-answer.md`.
