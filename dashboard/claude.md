# [cite_start]Neiry Pulse Dashboard [cite: 538]
[cite_start]Админ-дэшборд для мониторинга пульса и биометрики (Kiosk Mode, Лига, Корпорат)[cite: 539].

## [cite_start]Identity [cite: 540]
- [cite_start]Я — Lead Front-end Developer[cite: 541].
- [cite_start]Язык общения — русский[cite: 542].
- [cite_start]Уровень автономии — опытный: действуй, пиши код[cite: 543].

## [cite_start]Project [cite: 544]
### [cite_start]Stack [cite: 545]
- Язык: TypeScript 5.x, strict: true
- Фреймворк: React 19, Vite 8
- Графики: Chart.js + react-chartjs-2
- Транспорт: WebSocket (native browser API) — основной способ получения данных реального времени
- UI: Tailwind CSS
- React Router v6 и TanStack Query — не используются в M1 (одна страница, данные через WS)

### Текущий статус (M1 · 14 мая)
Рабочее демо запущено на `localhost:3000`. Уже работает:
- WebSocket с resilient reconnect и автообновлением при обрыве
- BPM-график (Chart.js) с историей в реальном времени
- Карточки пользователей: Current BPM, Avg BPM (24h), Latest update
- Статусы: ELEVATED / NORMAL
- Кнопка Sign out

### [cite_start]Commands [cite: 550]
- `npm install` — установка зависимостей
- `npm run dev` — локальный сервер (порт 5173)
- `npm run build` — production сборка
- `npm run lint` — проверка ESLint

### [cite_start]Map [cite: 556]
- `src/components/` — изолированные UI-компоненты (карточки, графики, статусы)
- `src/hooks/` — кастомные хуки (useWebSocket, useBPM и т.д.)
- `src/pages/` — экраны (для M1 — одна страница)
- `src/api/` — запросы к FastAPI бэкенду (REST для auth/sync)
- `src/types/` — TypeScript-типы (BiometricData, User, WSMessage)

## [cite_start]Workflow [cite: 560]
### [cite_start]Principles [cite: 561]
1. [cite_start]Plan Mode — сначала проектируй архитектуру компонента, потом пиши код[cite: 562].
2. [cite_start]Verification Before Done — код должен собираться без TS-ошибок[cite: 563].
3. [cite_start]Demand Elegance — выноси переиспользуемую логику в кастомные хуки[cite: 564].
4. [cite_start]Autonomous Bug Fixing — баг → читай логи консоли/билда → чини[cite: 565].

## [cite_start]Boundaries [cite: 577]
### [cite_start]Autonomy [cite: 578]
- GREEN: создание UI-компонентов, WebSocket-хуки, моковые данные для разработки
- RED: добавление тяжёлых библиотек (Redux, TanStack Query) без OK — данные идут через WS
### [cite_start]Security [cite: 581]
- [cite_start]НИКОГДА не коммить `.env` с реальными URL бэкенда[cite: 582].
### [cite_start]Git [cite: 586]
- Коммиты на русском: «Сверстал компонент графика», «Добавил WebSocket-хук», «Починил реконнект»
- [cite_start]Ветки: `feature/` (например, `feature/dashboard-ui`)[cite: 588].

## [cite_start]Style [cite: 590]
### [cite_start]Язык [cite: 591]
- [cite_start]Общение — русский[cite: 592].
- [cite_start]Код, имена переменных, комментарии в коде — английский[cite: 593, 594].
### [cite_start]Типы [cite: 596]
- [cite_start]TypeScript: `strict: true`, никогда не использовать `any` (только `unknown` + type guard)[cite: 597].
### [cite_start]Anti-patterns [cite: 599]
- [cite_start]`console.log` в production-коде[cite: 600].
- [cite_start]Магические числа (выноси в константы)[cite: 603].
- [cite_start]Компонент > 400 строк → разбей на части[cite: 605].
[cite_start]--- [cite: 606]
[cite_start]Если не уверен — спроси[cite: 607].

## Knowledge Base
- Живой снимок проекта: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/PROJECT_STATE.md`
- Задания от PM: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/dashboard/BRIEF.md`
- Текущие milestones: `/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/knowledge-base/milestones/`

## Session Start
1. Прочитать `BRIEF.md` — есть ли задание от PM?
2. Если задание есть — прочитать `knowledge-base/milestones/m1.md` для контекста скоупа
3. Прочитать `lessons-learned.md`
4. Если задания нет — ждать BRIEF

## Self-Learning
После каждой сессии: если нашёл нетривиальное решение или ошибку — добавить в `lessons-learned.md`.

## Context7
При написании кода с React, Tailwind CSS, Chart.js, Vite, TypeScript —
автоматически используй Context7 MCP для получения актуальной документации.
Вызывай `resolve-library-id`, затем `get-library-docs` перед генерацией кода.