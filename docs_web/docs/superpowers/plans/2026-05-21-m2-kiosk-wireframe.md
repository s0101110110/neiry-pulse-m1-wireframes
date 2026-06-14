# M2 Kiosk Wireframe — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Создать HTML-wireframe Kiosk-экрана для демонстрации экосистемы Neiry Pulse на Startup Village. Один файл `wireframes/m2/kiosk.html` с тремя состояниями (`IDLE`, `ACTIVE`, `PENDING_CLAIM`), переключаемыми через служебный toggle.

**Architecture:** Один статический HTML-файл с Tailwind CSS через CDN. Состояния переключаются через классы на `<body>` (`state-idle`, `state-active`, `state-pending`). Видимость блоков управляется через CSS-правила вида `body:not(.state-active) .only-active { display: none; }`. Минимальный JS — toggle обработчик + setInterval для имитации live BPM.

**Tech Stack:** HTML5 · Tailwind CSS (CDN) · Google Fonts (Manrope, Fraunces, JetBrains Mono) · Vanilla JS (без фреймворков)

**Spec:** `docs/superpowers/specs/2026-05-21-m2-kiosk-wireframe-design.md`

**Срок:** 2 часа

---

## File Structure

```
wireframes/m2/
└── kiosk.html         # один HTML-файл, всё внутри
```

Все стили — через Tailwind utility classes + минимум кастомного CSS внутри `<style>`. Все скрипты — inline в `<script>` внизу `<body>`.

---

## Перед началом

Открыть в браузере `wireframes/m1/mobile-home.html` чтобы скопировать boilerplate (Google Fonts, Tailwind CDN, кастомные классы `.font-brand`, `.font-data`). Открыть spec `docs/superpowers/specs/2026-05-21-m2-kiosk-wireframe-design.md` — спецификация компоновки и текстов.

---

### Task 1: Создать скелет HTML + setup

**Files:**
- Create: `wireframes/m2/kiosk.html`

- [ ] **Step 1: Создать файл с базовым HTML-скелетом**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kiosk · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Manrope:wght@300;400;500;600;700;800&family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }

  /* State machine via body classes */
  body:not(.state-idle) .only-idle { display: none !important; }
  body:not(.state-active) .only-active { display: none !important; }
  body:not(.state-pending) .only-pending { display: none !important; }

  /* Heart pulse animation */
  @keyframes heart-pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.12); }
  }
  .animate-heart { animation: heart-pulse 1s ease-in-out infinite; }
</style>
</head>
<body class="state-active min-h-screen bg-[#0f0e0b] text-[#f7f6f1]">
  <!-- Сюда добавим toggle, header, main grid, modal -->
</body>
</html>
```

- [ ] **Step 2: Открыть файл в браузере**

Откройте `wireframes/m2/kiosk.html` напрямую в Chrome/Safari.
Ожидаемо: пустая чёрная страница (`#0f0e0b`). Без ошибок в DevTools console.

---

### Task 2: Добавить служебную toggle-панель состояний

**Files:**
- Modify: `wireframes/m2/kiosk.html` (внутри `<body>`, в самом верху)

- [ ] **Step 1: Добавить toggle-bar**

Сразу после открывающего `<body>`:

```html
<!-- DEV: State toggle (для согласования с командой, в продакшене удалить) -->
<div class="fixed top-2 left-1/2 -translate-x-1/2 z-50 flex gap-1 bg-[#1a1814] border border-[#2a2620] rounded-lg p-1">
  <button data-state="state-idle" class="state-btn px-3 py-1 text-xs font-semibold rounded text-[#7a766d] hover:text-[#f7f6f1] transition-colors">IDLE</button>
  <button data-state="state-active" class="state-btn px-3 py-1 text-xs font-semibold rounded text-[#7a766d] hover:text-[#f7f6f1] transition-colors">ACTIVE</button>
  <button data-state="state-pending" class="state-btn px-3 py-1 text-xs font-semibold rounded text-[#7a766d] hover:text-[#f7f6f1] transition-colors">PENDING_CLAIM</button>
</div>
```

- [ ] **Step 2: Добавить JS для переключения**

Перед закрывающим `</body>`:

```html
<script>
  const STATES = ['state-idle', 'state-active', 'state-pending'];
  const buttons = document.querySelectorAll('.state-btn');

  function setState(state) {
    STATES.forEach(s => document.body.classList.remove(s));
    document.body.classList.add(state);
    buttons.forEach(btn => {
      const isActive = btn.dataset.state === state;
      btn.classList.toggle('text-[#f7f6f1]', isActive);
      btn.classList.toggle('bg-[#831843]', isActive);
      btn.classList.toggle('text-[#7a766d]', !isActive);
    });
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => setState(btn.dataset.state));
  });

  // Init
  setState('state-active');
</script>
```

- [ ] **Step 3: Проверить в браузере**

Обновите страницу. Кликая на `IDLE / ACTIVE / PENDING_CLAIM` — класс на `<body>` должен меняться (проверить через DevTools → Elements). Активная кнопка подсвечена `#831843`.

- [ ] **Step 4: Commit**

```bash
git add wireframes/m2/kiosk.html
git commit -m "Добавил скелет M2 Kiosk wireframe с переключателем состояний"
```

---

### Task 3: Шапка (header)

**Files:**
- Modify: `wireframes/m2/kiosk.html`

- [ ] **Step 1: Добавить header после toggle-bar**

```html
<header class="h-20 px-8 border-b border-[#2a2620] flex items-center justify-between">
  <!-- Левая зона: лого -->
  <div class="font-brand text-[#f7f6f1] text-2xl">Neiry Pulse</div>

  <!-- Центральная зона: статус подключения -->
  <div class="flex items-center gap-2">
    <span class="w-2.5 h-2.5 rounded-full bg-[#166534] block"></span>
    <span class="text-[#f7f6f1] text-sm">Подключено · Neiry.Pulse #1</span>
  </div>

  <!-- Правая зона: dropdown + таймер -->
  <div class="flex items-center gap-4">
    <div class="flex items-center gap-1 px-3 py-1.5 bg-[#1a1814] border border-[#2a2620] rounded-lg text-sm text-[#f7f6f1]">
      <span>#1</span>
      <span class="text-[#7a766d]">▼</span>
    </div>
    <div class="font-data text-[#f7f6f1] text-lg">02:15</div>
  </div>
</header>
```

- [ ] **Step 2: Проверить в браузере**

В шапке слева — «Neiry Pulse» (Fraunces). По центру — зелёная точка + текст подключения. Справа — статичный dropdown `[▼ #1]` и таймер `02:15` (JetBrains Mono).

---

### Task 4: Layout главной зоны (две колонки 60/40)

**Files:**
- Modify: `wireframes/m2/kiosk.html`

- [ ] **Step 1: Добавить main с grid**

После `</header>`:

```html
<main class="grid grid-cols-[3fr_2fr] gap-6 p-8" style="min-height: calc(100vh - 5rem);">

  <!-- ЛЕВАЯ КОЛОНКА — LIVE -->
  <section class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-8 flex flex-col">
    <!-- Сюда добавим IDLE / ACTIVE / PENDING контент -->
    <div class="text-[#7a766d] text-sm">[LEFT COLUMN placeholder]</div>
  </section>

  <!-- ПРАВАЯ КОЛОНКА — FUTURE -->
  <aside class="flex flex-col gap-4">
    <!-- Сюда добавим плашку и 4 виджета -->
    <div class="text-[#7a766d] text-sm">[RIGHT COLUMN placeholder]</div>
  </aside>

</main>
```

- [ ] **Step 2: Проверить в браузере**

Под шапкой — две колонки. Левая шире (60%), правая уже (40%). Левая имеет border и фон `#1a1814`. Размер главной зоны заполняет высоту окна.

---

### Task 5: Левая колонка — состояние IDLE

**Files:**
- Modify: `wireframes/m2/kiosk.html` (внутри левой `<section>`, заменить placeholder)

- [ ] **Step 1: Добавить блок IDLE**

```html
<!-- IDLE state -->
<div class="only-idle flex-1 flex flex-col items-center justify-center text-center">
  <p class="text-[#7a766d] text-2xl mb-8">Подключите Neiry.Pulse и нажмите СТАРТ</p>
  <button class="px-12 py-4 bg-[#831843] text-[#f7f6f1] font-semibold text-lg rounded-xl hover:opacity-90 transition-opacity">
    СТАРТ
  </button>
</div>
```

- [ ] **Step 2: Проверить переключением на IDLE**

Кликнуть `IDLE` в toggle-bar. Левая колонка показывает текст «Подключите Neiry.Pulse и нажмите СТАРТ» по центру + большая кнопка `СТАРТ` (винно-красная). При переключении на ACTIVE — блок исчезает.

---

### Task 6: Левая колонка — состояние ACTIVE (BPM, график, Calmness, IMU, ЭКГ)

**Files:**
- Modify: `wireframes/m2/kiosk.html` (внутри левой `<section>`, после IDLE-блока)

- [ ] **Step 1: Добавить блок ACTIVE**

```html
<!-- ACTIVE state -->
<div class="only-active flex-1 flex flex-col gap-8">

  <!-- BPM -->
  <div class="flex items-center gap-6">
    <span class="text-5xl animate-heart" style="color: #831843;">♥</span>
    <div>
      <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-1">Сердечный ритм</p>
      <div class="flex items-baseline gap-3">
        <span id="bpm-value" class="font-data text-[#831843] text-[120px] leading-none">84</span>
        <span class="text-[#7a766d] text-lg">уд/мин</span>
      </div>
    </div>
  </div>

  <!-- BPM running graph -->
  <div class="bg-[#0f0e0b] border border-[#2a2620] rounded-xl p-4 h-32">
    <svg id="bpm-graph" viewBox="0 0 600 100" preserveAspectRatio="none" class="w-full h-full">
      <polyline id="bpm-line" fill="none" stroke="#831843" stroke-width="2"
                points="0,50 50,48 100,52 150,45 200,55 250,50 300,42 350,58 400,50 450,46 500,52 550,48 600,50" />
    </svg>
  </div>

  <!-- Stress / Calmness Score -->
  <div>
    <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-3">Stress / Calmness Score</p>
    <div class="relative h-6 rounded-full" style="background: linear-gradient(to right, #991b1b, #a16207, #166534);">
      <div class="absolute top-0 bottom-0 w-1 bg-[#f7f6f1] rounded" style="left: 68%; box-shadow: 0 0 8px rgba(247,246,241,0.6);"></div>
    </div>
    <div class="flex justify-between mt-2">
      <span class="text-[#7a766d] text-xs">СТРЕСС</span>
      <span class="text-[#7a766d] text-xs">СПОКОЙСТВИЕ</span>
    </div>
    <p class="font-data text-[#f7f6f1] text-base mt-3">68 · Спокойствие</p>
    <p class="text-[#7a766d] text-xs mt-1">Реал-тайм оценка вегетативного статуса</p>
  </div>

  <!-- IMU -->
  <div class="flex items-center gap-2">
    <span class="text-[#7a766d] text-xs uppercase tracking-widest">IMU:</span>
    <span class="w-2 h-2 rounded-full bg-[#166534]"></span>
    <span class="font-data text-[#f7f6f1] text-sm">Покой</span>
  </div>

  <!-- ECG button (disabled) + STOP button -->
  <div class="mt-auto flex gap-4 items-end">
    <button disabled class="flex-1 px-6 py-4 bg-[#1a1814] border border-[#2a2620] text-[#4a463e] text-sm font-semibold rounded-xl cursor-not-allowed flex items-center justify-center gap-2">
      <span>🔒</span>
      <span>ЭКГ-сканирование</span>
    </button>
    <button class="flex-1 px-6 py-4 bg-[#831843] text-[#f7f6f1] text-sm font-semibold rounded-xl hover:opacity-90 transition-opacity">
      СТОП
    </button>
  </div>

</div>
```

- [ ] **Step 2: Проверить в браузере**

Переключиться на `ACTIVE`. Должно быть видно:
- Большое сердце слева, пульсирует
- Цифра BPM `84` крупно (винно-красный)
- График пульса (статичная линия, оживим позже)
- Градиентный бар `СТРЕСС → СПОКОЙСТВИЕ`, ползунок справа (зелёная зона)
- `IMU: 🟢 Покой`
- Внизу: disabled кнопка `🔒 ЭКГ-сканирование` + accent кнопка `СТОП`

---

### Task 7: Левая колонка — состояние PENDING_CLAIM (карточка отчёта)

**Files:**
- Modify: `wireframes/m2/kiosk.html` (внутри левой `<section>`, после ACTIVE-блока)

- [ ] **Step 1: Добавить блок PENDING_CLAIM**

```html
<!-- PENDING_CLAIM state -->
<div class="only-pending flex-1 flex flex-col">
  <h2 class="text-[#f7f6f1] text-3xl font-bold text-center mb-8 tracking-wide">СЕССИЯ ЗАВЕРШЕНА</h2>

  <!-- Mini graph -->
  <div class="bg-[#0f0e0b] border border-[#2a2620] rounded-xl p-4 h-40 mb-8">
    <svg viewBox="0 0 600 120" preserveAspectRatio="none" class="w-full h-full">
      <polyline fill="none" stroke="#831843" stroke-width="2"
                points="0,80 30,75 60,70 90,68 120,65 150,55 180,40 210,30 240,25 270,20 300,18 330,22 360,30 390,40 420,55 450,65 480,72 510,75 540,78 570,80 600,82" />
    </svg>
  </div>

  <!-- Summary table -->
  <div class="bg-[#0f0e0b] border border-[#2a2620] rounded-xl p-6 mb-6 max-w-md mx-auto w-full">
    <div class="flex justify-between py-2 border-b border-[#2a2620]">
      <span class="text-[#7a766d]">Длительность</span>
      <span class="font-data text-[#f7f6f1]">04:32</span>
    </div>
    <div class="flex justify-between py-2 border-b border-[#2a2620]">
      <span class="text-[#7a766d]">Peak BPM</span>
      <span class="font-data text-[#831843]">92</span>
    </div>
    <div class="flex justify-between py-2">
      <span class="text-[#7a766d]">Средний Calmness</span>
      <span class="font-data text-[#f7f6f1]">68</span>
    </div>
  </div>

  <p class="text-[#7a766d] text-center text-sm mb-auto">Полный отчёт — в Telegram-боте</p>

  <!-- Reset button -->
  <div class="flex justify-end mt-6">
    <button class="px-6 py-3 bg-[#1e3a8a] text-[#f7f6f1] text-sm font-semibold rounded-xl hover:opacity-90 transition-opacity">
      СБРОСИТЬ
    </button>
  </div>
</div>
```

- [ ] **Step 2: Проверить в браузере**

Переключиться на `PENDING_CLAIM`. Левая колонка показывает:
- Заголовок `СЕССИЯ ЗАВЕРШЕНА` крупно
- Мини-график BPM (плавный пик в середине)
- Табличку с 3 числами
- Подзаголовок «Полный отчёт — в Telegram-боте»
- Кнопку `СБРОСИТЬ` справа внизу (синяя `#1e3a8a`)

- [ ] **Step 3: Commit**

```bash
git add wireframes/m2/kiosk.html
git commit -m "Собрал левую колонку M2 Kiosk: IDLE, ACTIVE и PENDING_CLAIM"
```

---

### Task 8: Правая колонка — плашка + 4 виджета

**Files:**
- Modify: `wireframes/m2/kiosk.html` (внутри `<aside>`, заменить placeholder)

- [ ] **Step 1: Добавить контент правой колонки**

```html
<!-- Header badge -->
<div class="bg-[#1a1814]/80 border border-[#2a2620] rounded-lg px-4 py-3 text-center">
  <span class="font-data text-[#7a766d] text-xs tracking-wider">
    ПРЕДИКТИВНАЯ АНАЛИТИКА · ТРЕБУЕТСЯ 14+ ДНЕЙ НОШЕНИЯ
  </span>
</div>

<!-- Widget 1: Neiry Readiness -->
<div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-6">
  <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-4">Neiry Readiness</p>
  <div class="flex items-center gap-6">
    <!-- Donut chart -->
    <svg width="100" height="100" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="40" fill="none" stroke="#2a2620" stroke-width="10" />
      <circle cx="50" cy="50" r="40" fill="none" stroke="#1e3a8a" stroke-width="10"
              stroke-dasharray="251.2" stroke-dashoffset="45" transform="rotate(-90 50 50)" stroke-linecap="round" />
      <text x="50" y="56" text-anchor="middle" font-family="JetBrains Mono" font-size="20" fill="#f7f6f1" font-weight="bold">82%</text>
    </svg>
    <div>
      <p class="text-[#f7f6f1] font-semibold mb-1">Индекс восстановления</p>
      <p class="text-[#7a766d] text-xs">На основе сна, HRV и активности за 14 дней</p>
    </div>
  </div>
</div>

<!-- Widget 2: Качество сна -->
<div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-6">
  <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-4">Качество сна</p>
  <div class="flex justify-between mb-3">
    <div class="text-center">
      <p class="font-data text-[#f7f6f1] text-2xl">21%</p>
      <p class="text-[#7a766d] text-xs mt-1">Deep</p>
    </div>
    <div class="text-center">
      <p class="font-data text-[#f7f6f1] text-2xl">24%</p>
      <p class="text-[#7a766d] text-xs mt-1">REM</p>
    </div>
    <div class="text-center">
      <p class="font-data text-[#f7f6f1] text-2xl">55%</p>
      <p class="text-[#7a766d] text-xs mt-1">Light</p>
    </div>
  </div>
  <!-- Stacked bar -->
  <div class="h-2 rounded-full overflow-hidden flex">
    <div class="bg-[#1e3a8a]" style="width: 21%;"></div>
    <div class="bg-[#831843]" style="width: 24%;"></div>
    <div class="bg-[#7a766d]" style="width: 55%;"></div>
  </div>
  <p class="text-[#7a766d] text-xs mt-3">Last night · 7ч 42мин</p>
</div>

<!-- Widget 3: Burnout Risk -->
<div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-6">
  <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-4">Burnout Risk</p>
  <p class="text-[#166534] text-2xl font-semibold mb-2">🟢 Низкий риск</p>
  <p class="text-[#7a766d] text-xs">Скользящее среднее стресса за 14 дней</p>
</div>

<!-- Widget 4: Drowsiness Predictor -->
<div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-6">
  <p class="text-[#7a766d] text-xs uppercase tracking-widest mb-4">Drowsiness Predictor</p>
  <p class="text-[#166534] text-2xl font-semibold mb-2">🟢 Активный режим</p>
  <p class="text-[#7a766d] text-xs">Алерт за 5–10 мин до микросна</p>
</div>
```

- [ ] **Step 2: Проверить в браузере**

В правой колонке видна плашка `ПРЕДИКТИВНАЯ АНАЛИТИКА...` + 4 виджета сверху вниз. Donut chart показывает 82%. Stacked bar в виджете сна — три цветных сегмента. Burnout Risk и Drowsiness — зелёные статусы.

- [ ] **Step 3: Переключить состояния** — правая колонка должна оставаться видимой во всех (IDLE, ACTIVE, PENDING).

---

### Task 9: QR-модалка (поверх PENDING_CLAIM)

**Files:**
- Modify: `wireframes/m2/kiosk.html` (после закрывающего `</main>`)

- [ ] **Step 1: Добавить модалку с overlay**

```html
<!-- QR Modal (only in PENDING_CLAIM) -->
<div id="qr-modal" class="only-pending fixed inset-0 z-40 flex items-center justify-center bg-black/60 backdrop-blur-sm">
  <div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-10 max-w-md w-full mx-4">
    <h3 class="text-[#f7f6f1] text-xl font-semibold text-center mb-6">📱 Заберите отчёт в Telegram</h3>

    <!-- QR placeholder (21x21 grid SVG) -->
    <div class="flex justify-center mb-6">
      <svg width="200" height="200" viewBox="0 0 21 21" class="bg-white rounded-lg p-2">
        <!-- Generated placeholder pattern (имитация QR через рандомный паттерн) -->
        <rect x="0" y="0" width="3" height="3" fill="black"/>
        <rect x="4" y="0" width="1" height="1" fill="black"/>
        <rect x="6" y="0" width="2" height="1" fill="black"/>
        <rect x="10" y="0" width="1" height="2" fill="black"/>
        <rect x="13" y="0" width="2" height="1" fill="black"/>
        <rect x="18" y="0" width="3" height="3" fill="black"/>

        <rect x="0" y="4" width="1" height="1" fill="black"/>
        <rect x="2" y="4" width="1" height="1" fill="black"/>
        <rect x="5" y="4" width="2" height="2" fill="black"/>
        <rect x="9" y="4" width="1" height="1" fill="black"/>
        <rect x="11" y="4" width="2" height="1" fill="black"/>
        <rect x="14" y="4" width="1" height="2" fill="black"/>
        <rect x="18" y="4" width="1" height="1" fill="black"/>
        <rect x="20" y="4" width="1" height="1" fill="black"/>

        <rect x="0" y="6" width="3" height="1" fill="black"/>
        <rect x="5" y="6" width="1" height="2" fill="black"/>
        <rect x="8" y="6" width="2" height="2" fill="black"/>
        <rect x="12" y="6" width="3" height="1" fill="black"/>
        <rect x="17" y="6" width="2" height="2" fill="black"/>

        <rect x="2" y="9" width="1" height="2" fill="black"/>
        <rect x="4" y="9" width="2" height="1" fill="black"/>
        <rect x="7" y="9" width="1" height="3" fill="black"/>
        <rect x="10" y="9" width="2" height="2" fill="black"/>
        <rect x="13" y="9" width="1" height="1" fill="black"/>
        <rect x="16" y="9" width="2" height="1" fill="black"/>
        <rect x="20" y="9" width="1" height="3" fill="black"/>

        <rect x="0" y="12" width="2" height="1" fill="black"/>
        <rect x="4" y="12" width="1" height="2" fill="black"/>
        <rect x="9" y="12" width="2" height="1" fill="black"/>
        <rect x="14" y="12" width="2" height="2" fill="black"/>
        <rect x="17" y="12" width="1" height="2" fill="black"/>

        <rect x="0" y="15" width="1" height="1" fill="black"/>
        <rect x="2" y="15" width="3" height="2" fill="black"/>
        <rect x="6" y="15" width="1" height="1" fill="black"/>
        <rect x="8" y="15" width="2" height="2" fill="black"/>
        <rect x="11" y="15" width="3" height="1" fill="black"/>
        <rect x="16" y="15" width="2" height="2" fill="black"/>
        <rect x="19" y="15" width="2" height="1" fill="black"/>

        <rect x="0" y="18" width="3" height="3" fill="black"/>
        <rect x="5" y="18" width="2" height="2" fill="black"/>
        <rect x="9" y="18" width="1" height="3" fill="black"/>
        <rect x="12" y="18" width="2" height="1" fill="black"/>
        <rect x="15" y="18" width="1" height="2" fill="black"/>
        <rect x="18" y="18" width="3" height="3" fill="black"/>
      </svg>
    </div>

    <p class="text-center text-[#831843] font-data text-4xl mb-4">PIN: 4815</p>
    <p class="text-center text-[#7a766d] text-sm mb-8">Отсканируйте код или введите PIN в @NeiryPulseBot</p>

    <div class="flex justify-end">
      <button id="modal-close" class="px-6 py-2 bg-[#1e3a8a] text-[#f7f6f1] text-sm font-semibold rounded-xl hover:opacity-90 transition-opacity">
        ЗАКРЫТЬ
      </button>
    </div>
  </div>
</div>
```

- [ ] **Step 2: Добавить обработчик закрытия в `<script>`**

В существующий `<script>` (после init) добавить:

```javascript
// QR modal close (visual only - re-opens when switching state)
const closeBtn = document.getElementById('modal-close');
const modal = document.getElementById('qr-modal');
if (closeBtn && modal) {
  closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });
}
```

- [ ] **Step 3: Проверить в браузере**

Переключиться на `PENDING_CLAIM`. Поверх левой колонки появляется модалка с заголовком, QR-картинкой (21×21 паттерн на белом фоне), `PIN: 4815` (крупно, винно-красный), подсказка про бота и кнопка `ЗАКРЫТЬ`. Клик `ЗАКРЫТЬ` — модалка скрывается. Переключение состояний → модалка снова появляется в PENDING.

---

### Task 10: Fake live BPM (анимация цифры)

**Files:**
- Modify: `wireframes/m2/kiosk.html` (в существующий `<script>`)

- [ ] **Step 1: Добавить setInterval для BPM**

В существующий `<script>` (после init):

```javascript
// Fake live BPM (only animates in active state)
const bpmEl = document.getElementById('bpm-value');
if (bpmEl) {
  setInterval(() => {
    if (!document.body.classList.contains('state-active')) return;
    const bpm = 76 + Math.floor(Math.random() * 17); // 76-92
    bpmEl.textContent = bpm;
  }, 1000);
}
```

- [ ] **Step 2: Проверить в браузере**

В `ACTIVE` цифра BPM меняется каждую секунду в диапазоне 76–92. Сердце пульсирует синхронно (CSS-анимация). При переключении на IDLE/PENDING — анимация цифры останавливается (т.к. ACTIVE-блок скрыт).

---

### Task 11: Финальная визуальная проверка всех состояний

- [ ] **Step 1: Открыть `wireframes/m2/kiosk.html` в Chrome**

Размер окна — full-screen или ≥1920×1080.

- [ ] **Step 2: Проверить IDLE**

Кликнуть кнопку `IDLE` в toggle-bar.

Ожидаемо:
- Шапка на месте (лого, статус подключения, dropdown, таймер)
- Левая колонка: «Подключите Neiry.Pulse и нажмите СТАРТ» + кнопка `СТАРТ`
- Правая колонка: плашка + 4 виджета (видна)
- Никаких сердец, графиков, QR

- [ ] **Step 3: Проверить ACTIVE**

Кликнуть кнопку `ACTIVE`.

Ожидаемо:
- Большое сердце пульсирует
- BPM меняется каждую секунду в пределах 76–92
- Градиентный бар Calmness виден с ползунком справа
- IMU: Покой
- ЭКГ-кнопка disabled с замком
- Кнопка СТОП
- Правая колонка видна
- Модалки нет

- [ ] **Step 4: Проверить PENDING_CLAIM**

Кликнуть кнопку `PENDING_CLAIM`.

Ожидаемо:
- Заголовок СЕССИЯ ЗАВЕРШЕНА
- Мини-график, табличка с числами, подзаголовок про Telegram, кнопка СБРОСИТЬ
- Поверх — модалка с QR, PIN: 4815, подсказкой, кнопкой ЗАКРЫТЬ
- Правая колонка видна за модалкой (через blur)

- [ ] **Step 5: Проверить, что нигде нет упоминаний VITRO / M1 / M2 / B2B-клиентов**

Открыть DevTools → Search (Ctrl+F / Cmd+F) и поискать в HTML: `VITRO`, `VANTA`, `VIGOR`, `M1`, `M2`, `M3`, `Сбер`, `Газпром`, `Райффайзенбанк`. Должно быть 0 совпадений.

- [ ] **Step 6: Финальный commit**

```bash
git add wireframes/m2/kiosk.html
git commit -m "Завершил M2 Kiosk wireframe: 3 состояния, fake live BPM, QR-модалка"
```

---

## Self-Review Checklist (после реализации)

- [ ] Все 3 состояния визуально различимы и переключаемы
- [ ] Левая колонка ACTIVE содержит: BPM крупно, график, Calmness bar с подписями СТРЕСС/СПОКОЙСТВИЕ, IMU, ЭКГ-кнопку disabled, кнопку СТОП
- [ ] Правая колонка содержит: плашку «ПРЕДИКТИВНАЯ АНАЛИТИКА...» + 4 виджета (Readiness donut 82%, Качество сна с stacked-bar, Burnout, Drowsiness)
- [ ] PENDING_CLAIM: левая = карточка отчёта, поверх = модалка QR с PIN: 4815 (B2-вариант)
- [ ] Палитра соответствует claude.md и спеке (фон `#0f0e0b`, accent `#831843` для live, `#1e3a8a` для dashboard-кнопок)
- [ ] Шрифты: Manrope (тексты), Fraunces (лого), JetBrains Mono (числа)
- [ ] Анимация сердца работает (CSS pulse 1s)
- [ ] Fake live BPM меняется в ACTIVE
- [ ] Нет упоминаний внутреннего нейминга (VITRO/VANTA/M1-3) и B2B-клиентов

---

## Что НЕ делать

- Не добавлять React/Vue/любые JS-фреймворки (только vanilla JS)
- Не добавлять реальные API-вызовы или WebSocket
- Не вёрстать переключение между N браслетами (всегда `Neiry.Pulse #1`)
- Не добавлять адаптивность под mobile (только desktop 1920×1080)
- Не использовать иконки/SVG из M1 (`Design/*.svg`), эти ассеты для мобильного

---

## После завершения

PM (главная сессия) откроет файл в браузере, проверит все 3 состояния, и решит:
- Если OK → отправить ссылку на GitHub Pages Кириллу и Паше для согласования
- Если нужны правки → новый BRIEF с правками
