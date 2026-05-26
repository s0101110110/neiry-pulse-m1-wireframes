# Kiosk Drilldown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Собрать визуально полный HTML-мокап `kiosk-drilldown.html` — внутренняя страница карточки гостя/якоря для админ-ноута на M2 Startup Village, со всеми 7 состояниями (empty / drilldown / phase-1/2/3 / result / claim), Bayevsky-модалкой и mock-данными по 3 персонажам.

**Architecture:** Один файл `docs_web/wireframes/m2/kiosk-drilldown.html` с inline `<style>` (CSS-токены shadcn + анимации) и inline `<script>` (vanilla JS для state-machine, mock-data switcher, live BPM, ECG scroll, Bayevsky-таймеры). State-машина = body-class (`state-drilldown` / `state-phase-1` / ... / `state-claim` / `state-empty`), элементы показываются/скрываются через `body.state-X .element { display: ... }`. URL-параметры `?id=kostya|alexey|guest&session=active` определяют initial state и mock-data set.

**Tech Stack:** HTML5, Tailwind CSS (CDN), Google Fonts (Space Grotesk + Onest + Geist Mono), inline SVG для всех графиков/gauge/иконок, vanilla JavaScript. Никаких внешних JS-зависимостей кроме Tailwind CDN и Google Fonts.

**Spec:** `docs_web/docs/superpowers/specs/2026-05-26-m2-kiosk-drilldown-design.md` — единый источник всех решений по дизайну, mock-данным, шкалам.

**Verification approach:** Для wireframe нет unit-тестов. После каждой задачи: открыть файл в Chrome на 1920×1080 (или DevTools toolbar) → проверить визуально → сделать proof-screenshot → закоммитить. Финальная проверка — пройти все 17 пунктов acceptance criteria из §15 спеки.

---

## File Structure

Единственный файл (создаётся в Task 1, изменяется во всех остальных):

```
docs_web/wireframes/m2/kiosk-drilldown.html
```

Внутренняя структура файла:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <!-- meta, Tailwind CDN, Google Fonts -->
  <style>
    /* CSS-переменные shadcn (--background, --foreground, --primary, etc.) */
    /* Семейство шрифтов */
    /* state-классы (body.state-X .element { display }) */
    /* Кейфреймы анимаций (pulse, ecg-scroll) */
  </style>
</head>
<body class="state-drilldown">

  <!-- Top-bar (§4) -->
  <header>...</header>

  <!-- Empty-state баннер (§9.1) — visible только при body.state-empty -->
  <div id="empty-banner">...</div>

  <!-- Main 2-column layout (§5, §6) -->
  <main>
    <section id="live-column">
      <!-- BPM hero, ECG, 2 круга, 2 кнопки -->
    </section>
    <section id="predictive-column">
      <!-- Recovery, Sleep, Burnout, Drowsy, Bayevsky -->
    </section>
  </main>

  <!-- Bayevsky modal overlay (§7) — visible при state-phase-1/2/3/result -->
  <div id="bayevsky-modal">
    <div id="phase-1-content">...</div>
    <div id="phase-2-content">...</div>
    <div id="phase-3-content">...</div>
    <div id="result-content">...</div>
  </div>

  <!-- Claim state (§8) — full-screen при body.state-claim -->
  <div id="claim-screen">...</div>

  <!-- Dev-bar (§10) — всегда снизу -->
  <footer id="dev-bar">...</footer>

  <script>
    /* MOCK_DATA по 3 персонажам */
    /* URL params parsing */
    /* state machine (setState fn) */
    /* fake live BPM (sin-волна) */
    /* ECG SVG scroll */
    /* dev-bar pill handlers */
    /* Bayevsky timers */
    /* session-timer (02:47 ticker) */
  </script>
</body>
</html>
```

---

## Tasks

### Task 1: HTML-скелет + CSS-токены + top-bar

**Files:**
- Create: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §2 (стек), §3 (сетка), §4 (top-bar)

- [ ] **Step 1: Создать файл с базовым HTML-скелетом**

Создать `docs_web/wireframes/m2/kiosk-drilldown.html` с содержимым:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1920, initial-scale=1">
  <title>Neiry Pulse · Kiosk Drilldown</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Onest:wght@700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      /* shadcn dark theme — zinc/slate base */
      --background: 240 10% 4%;
      --foreground: 0 0% 98%;
      --card: 240 6% 10%;
      --card-foreground: 0 0% 98%;
      --muted: 240 4% 16%;
      --muted-foreground: 240 5% 65%;
      --border: 240 4% 20%;
      --primary: 333 76% 30%; /* wine #831843 */
      --primary-foreground: 0 0% 100%;
      --success: 151 100% 45%;
      --warning: 42 100% 50%;
      --destructive: 348 100% 54%;
      --chart-2: 151 100% 45%;
      --chart-4: 42 100% 50%;
    }
    body {
      font-family: 'Space Grotesk', sans-serif;
      background: hsl(var(--background));
      color: hsl(var(--foreground));
      -webkit-font-smoothing: antialiased;
    }
    .font-hero { font-family: 'Onest', sans-serif; font-weight: 700; letter-spacing: -0.02em; }
    .font-data { font-family: 'Geist Mono', monospace; }
    .tnum { font-variant-numeric: tabular-nums; }
  </style>
</head>
<body class="state-drilldown min-h-screen overflow-hidden">

  <!-- Top-bar — §4 -->
  <header class="h-16 px-8 flex items-center justify-between border-b" style="border-color: hsl(var(--border));">
    <div class="flex items-center gap-3">
      <span class="text-xl font-medium">neiry <span class="font-hero italic" style="color: hsl(var(--primary));">Pulse</span></span>
      <span style="color: hsl(var(--muted-foreground));">·</span>
      <span class="font-data tnum text-sm" style="color: hsl(var(--muted-foreground));" id="session-id-label">sess_7K2M9</span>
    </div>
    <div class="font-data tnum text-lg" id="session-timer">02:47</div>
  </header>

  <!-- Main layout — placeholder, заполнится в следующих задачах -->
  <main class="px-8 py-8 flex gap-6" style="height: calc(100vh - 64px - 80px);">
    <section id="live-column" class="flex-1 flex flex-col gap-6">
      <!-- LIVE column (Task 2-5) -->
    </section>
    <section id="predictive-column" class="flex-1 flex flex-col gap-4">
      <!-- PREDICTIVE column (Task 6-8) -->
    </section>
  </main>

  <!-- Dev-bar — placeholder, заполнится в Task 9 -->
  <footer id="dev-bar" class="h-20 fixed bottom-0 left-0 right-0 backdrop-blur-sm border-t" style="background: hsl(var(--card) / 0.8); border-color: hsl(var(--border));"></footer>

  <script>
    /* Session timer tick — §4 */
    let sessionSeconds = 167; // 02:47 starting
    setInterval(() => {
      sessionSeconds++;
      const m = String(Math.floor(sessionSeconds / 60)).padStart(2, '0');
      const s = String(sessionSeconds % 60).padStart(2, '0');
      document.getElementById('session-timer').textContent = `${m}:${s}`;
    }, 1000);
  </script>
</body>
</html>
```

- [ ] **Step 2: Verify visually**

Открыть `docs_web/wireframes/m2/kiosk-drilldown.html` в Chrome.

Expected:
- Тёмный фон (zinc-900-ish)
- Сверху горизонтальная полоса 64px с надписью `neiry Pulse · sess_7K2M9` слева, `02:47` (тикает!) справа
- Снизу пустая полоса 80px (dev-bar placeholder)
- Между ними — пустое пространство (тут потом заполнится 2 колонки)
- Никаких JS-ошибок в DevTools console

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил скелет kiosk-drilldown.html + CSS-токены + top-bar с тикающим таймером"
```

---

### Task 2: BPM hero — левая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html` (внутри `<section id="live-column">`)

**Spec ref:** §5.1, §5.5 (микро-чипы)

- [ ] **Step 1: Вставить HTML BPM hero блока**

В `<section id="live-column">` добавить **первым** ребёнком:

```html
      <div class="rounded-2xl p-8 flex flex-col items-center justify-center" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border));">
        <div class="flex items-end gap-4">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor" style="color: hsl(var(--primary));">
            <path d="M12 21s-7-4.5-9.5-9C.5 8.5 3 4 7 4c2 0 3.5 1 5 3 1.5-2 3-3 5-3 4 0 6.5 4.5 4.5 8-2.5 4.5-9.5 9-9.5 9z"/>
          </svg>
          <div class="font-hero tnum leading-none" id="bpm-value" style="font-size: 160px;">82</div>
          <div class="font-data text-xl pb-6" style="color: hsl(var(--muted-foreground));">BPM</div>
        </div>
        <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 rounded-full font-data text-sm uppercase tracking-wide" id="bpm-status-chip" style="background: hsl(var(--muted) / 0.5);">
          <span class="w-2 h-2 rounded-full" style="background: hsl(var(--success));"></span>
          <span>Подключен</span>
        </div>
      </div>
```

- [ ] **Step 2: Добавить fake live BPM анимацию**

В `<script>` после session-timer кода добавить:

```javascript
    /* Fake live BPM — sin-волна около базового значения */
    let bpmBase = 82;
    let bpmTick = 0;
    setInterval(() => {
      bpmTick++;
      const variation = Math.sin(bpmTick / 3) * 2;
      const value = Math.round(bpmBase + variation);
      document.getElementById('bpm-value').textContent = value;
    }, 800);

    /* BPM pulse breathing animation via CSS — добавим класс */
```

В `<style>` добавить keyframe:

```css
    @keyframes bpm-breathe {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.02); }
    }
    #bpm-value { animation: bpm-breathe 1s ease-in-out infinite; transform-origin: center; }
```

- [ ] **Step 3: Verify visually**

Open in Chrome. Expected:
- В левой колонке сверху — карточка с большим числом `82` (~160px), иконка сердца ♥ слева, `BPM` справа
- Под числом — небольшой чип с зелёной точкой и `Подключен`
- Число «дышит» (плавный scale 1.0 → 1.02) и слегка меняется (80-84) каждые 0.8 сек
- Никакого «прыжка» цифр (tabular-nums работает)

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил BPM hero в drilldown: число 160px + breathing-анимация + fake live"
```

---

### Task 3: ECG plashka — левая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §5.2

- [ ] **Step 1: Вставить SVG ECG-плашки**

В `<section id="live-column">` **сразу после** BPM-блока (Task 2) добавить:

```html
      <div class="rounded-2xl p-4 relative overflow-hidden" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); height: 140px;">
        <div class="absolute top-2 left-4 font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">ECG</div>
        <svg class="w-full h-full" viewBox="0 0 884 108" preserveAspectRatio="none" id="ecg-svg">
          <g id="ecg-pattern" stroke="currentColor" stroke-width="2" fill="none" style="color: hsl(var(--success));">
            <!-- 2 sibling patterns для бесшовного scroll -->
            <path id="ecg-path-1" d="M 0 54 L 50 54 L 60 50 L 65 54 L 70 30 L 75 80 L 80 54 L 90 54 L 100 48 L 110 54 L 160 54 L 170 50 L 175 54 L 180 30 L 185 80 L 190 54 L 200 54 L 210 48 L 220 54 L 270 54 L 280 50 L 285 54 L 290 30 L 295 80 L 300 54 L 310 54 L 320 48 L 330 54 L 380 54 L 390 50 L 395 54 L 400 30 L 405 80 L 410 54 L 420 54 L 430 48 L 440 54 L 490 54 L 500 50 L 505 54 L 510 30 L 515 80 L 520 54 L 530 54 L 540 48 L 550 54 L 600 54 L 610 50 L 615 54 L 620 30 L 625 80 L 630 54 L 640 54 L 650 48 L 660 54 L 710 54 L 720 50 L 725 54 L 730 30 L 735 80 L 740 54 L 750 54 L 760 48 L 770 54 L 820 54 L 830 50 L 835 54 L 840 30 L 845 80 L 850 54 L 860 54 L 870 48 L 884 54"/>
            <path id="ecg-path-2" d="M 0 54 L 50 54 L 60 50 L 65 54 L 70 30 L 75 80 L 80 54 L 90 54 L 100 48 L 110 54 L 160 54 L 170 50 L 175 54 L 180 30 L 185 80 L 190 54 L 200 54 L 210 48 L 220 54 L 270 54 L 280 50 L 285 54 L 290 30 L 295 80 L 300 54 L 310 54 L 320 48 L 330 54 L 380 54 L 390 50 L 395 54 L 400 30 L 405 80 L 410 54 L 420 54 L 430 48 L 440 54 L 490 54 L 500 50 L 505 54 L 510 30 L 515 80 L 520 54 L 530 54 L 540 48 L 550 54 L 600 54 L 610 50 L 615 54 L 620 30 L 625 80 L 630 54 L 640 54 L 650 48 L 660 54 L 710 54 L 720 50 L 725 54 L 730 30 L 735 80 L 740 54 L 750 54 L 760 48 L 770 54 L 820 54 L 830 50 L 835 54 L 840 30 L 845 80 L 850 54 L 860 54 L 870 48 L 884 54" transform="translate(884, 0)"/>
          </g>
        </svg>
      </div>
```

- [ ] **Step 2: Добавить scroll-анимацию ECG**

В `<style>` добавить:

```css
    @keyframes ecg-scroll {
      from { transform: translateX(0); }
      to { transform: translateX(-884px); }
    }
    #ecg-pattern { animation: ecg-scroll 6s linear infinite; }
```

- [ ] **Step 3: Verify visually**

Open in Chrome. Expected:
- Под BPM-блоком — rounded-плашка высотой 140px с зелёной волной ECG (PQRST-комплексы)
- Волна плавно «уезжает» влево с скоростью ~150px/сек, бесшовно (нет skip'ов между patterns)
- Слева сверху — мелкая подпись `ECG`

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил ECG-плашку с PQRST-узором + scroll-анимация"
```

---

### Task 4: Stress + IMU круги — левая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §5.3, §5.5

- [ ] **Step 1: Вставить блок с 2 кругами**

В `<section id="live-column">` **сразу после** ECG-блока (Task 3) добавить:

```html
      <div class="grid grid-cols-2 gap-6">
        <!-- Stress круг — без gauge-заливки, цвет светофора в чипе -->
        <div class="rounded-2xl p-6 flex flex-col items-center justify-center" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border));">
          <div class="relative" style="width: 240px; height: 240px;">
            <svg class="w-full h-full" viewBox="0 0 240 240">
              <circle cx="120" cy="120" r="116" stroke="hsl(var(--border))" stroke-width="2" fill="none"/>
            </svg>
            <div class="absolute inset-0 flex flex-col items-center justify-center">
              <div class="font-hero tnum leading-none" id="stress-value" style="font-size: 88px;">41</div>
              <div class="text-sm mt-2" style="color: hsl(var(--muted-foreground));">стресс</div>
            </div>
          </div>
          <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 rounded-full font-data text-sm uppercase tracking-wide" id="stress-chip" style="background: hsl(var(--muted) / 0.5);">
            <span class="w-2 h-2 rounded-full" style="background: hsl(var(--warning));"></span>
            <span>Повышен</span>
          </div>
        </div>

        <!-- IMU круг — концентрические декоративные кольца -->
        <div class="rounded-2xl p-6 flex flex-col items-center justify-center" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border));">
          <div class="relative" style="width: 240px; height: 240px;">
            <svg class="w-full h-full" viewBox="0 0 240 240">
              <circle cx="120" cy="120" r="116" stroke="hsl(var(--border))" stroke-width="1.5" fill="none" opacity="0.9"/>
              <circle cx="120" cy="120" r="94" stroke="hsl(var(--border))" stroke-width="1" fill="none" opacity="0.7"/>
              <circle cx="120" cy="120" r="72" stroke="hsl(var(--border))" stroke-width="1" fill="none" opacity="0.5"/>
              <circle cx="120" cy="120" r="50" stroke="hsl(var(--border))" stroke-width="1" fill="none" opacity="0.3"/>
              <circle cx="120" cy="120" r="28" stroke="hsl(var(--border))" stroke-width="1" fill="none" opacity="0.2"/>
            </svg>
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="text-xl" style="color: hsl(var(--foreground));">IMU</div>
            </div>
          </div>
          <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 rounded-full font-data text-sm uppercase tracking-wide" id="imu-chip" style="background: hsl(var(--muted) / 0.5);">
            <span class="w-2 h-2 rounded-full" style="background: hsl(var(--success));"></span>
            <span>Покой</span>
          </div>
        </div>
      </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome. Expected:
- Под ECG — ряд из 2 круглых карточек 50/50
- Слева: круг с числом `41` в центре, подпись `стресс`, под кругом чип `● Повышен` (амбра)
- Справа: круг с концентрическими кольцами (5 шт.), в центре подпись `IMU`, под кругом чип `● Покой` (зелёный)
- Оба круга 240×240px, идентичный padding

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Stress и IMU круги в левую колонку drilldown"
```

---

### Task 5: Кнопки СТОП + ТЕСТ — левая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §5.4

- [ ] **Step 1: Вставить ряд из 2 кнопок**

В `<section id="live-column">` **последним** ребёнком (после кругов из Task 4):

```html
      <div class="grid grid-cols-2 gap-4">
        <button id="btn-stop" class="h-16 rounded-xl font-medium text-lg transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">
          СТОП
        </button>
        <button id="btn-test" class="h-16 rounded-xl font-medium text-lg transition flex items-center justify-center gap-2" style="background: #831843; color: white;" onmouseover="this.style.background='#9a1d50'" onmouseout="this.style.background='#831843'">
          <span>▶</span><span>ТЕСТ</span>
        </button>
      </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome. Expected:
- Под кругами — ряд из 2 кнопок одинаковой высоты (64px)
- Слева: `СТОП` — ghost (transparent + border)
- Справа: `▶ ТЕСТ` — wine fill, белый текст
- Hover: СТОП — border светлеет, ТЕСТ — фон чуть светлее

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил кнопки СТОП (ghost) и ТЕСТ (primary wine) в drilldown"
```

---

### Task 6: Recovery + Burnout + Drowsy виджеты — правая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §6.1, §6.3, §6.4

- [ ] **Step 1: Создать reusable-структуру и вставить 3 виджета**

В `<section id="predictive-column">` добавить (ВНИМАНИЕ: Sleep идёт между Recovery и Burnout в финальной сетке 2×2, но в этой задаче добавляем только 3 — Sleep будет в Task 7):

```html
      <div class="grid grid-cols-2 gap-4" id="predictive-grid-top">
        <!-- Recovery -->
        <div class="rounded-2xl p-6 flex flex-col justify-between" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 240px;">
          <div class="flex items-start justify-between">
            <div class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Recovery</div>
            <div class="font-hero tnum leading-none" id="recovery-value" style="font-size: 56px;">78%</div>
          </div>
          <div>
            <div class="h-3 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
              <div class="h-full rounded-full" id="recovery-bar" style="width: 78%; background: hsl(var(--success));"></div>
            </div>
            <div class="mt-4 flex items-center gap-2 text-base" id="recovery-caption">
              <span>🟢</span><span>Хорошее восстановление</span>
            </div>
          </div>
        </div>

        <!-- Placeholder для Sleep — заполнится в Task 7 -->
        <div id="sleep-card-placeholder" class="rounded-2xl p-6" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 240px;"></div>

        <!-- Burnout -->
        <div class="rounded-2xl p-6 flex flex-col justify-between" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 240px;">
          <div class="flex items-start justify-between">
            <div class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Burnout</div>
            <div class="font-hero tnum leading-none" id="burnout-value" style="font-size: 56px;">12%</div>
          </div>
          <div>
            <div class="h-3 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
              <div class="h-full rounded-full" id="burnout-bar" style="width: 12%; background: hsl(var(--success));"></div>
            </div>
            <div class="mt-4 flex items-center gap-2 text-base" id="burnout-caption">
              <span>🟢</span><span>Низкий риск</span>
            </div>
          </div>
        </div>

        <!-- Drowsy -->
        <div class="rounded-2xl p-6 flex flex-col justify-between" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 240px;">
          <div class="flex items-start justify-between">
            <div class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Drowsy</div>
            <div class="font-hero tnum leading-none" id="drowsy-value" style="font-size: 56px;">18%</div>
          </div>
          <div>
            <div class="h-3 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
              <div class="h-full rounded-full" id="drowsy-bar" style="width: 18%; background: hsl(var(--success));"></div>
            </div>
            <div class="mt-4 flex items-center gap-2 text-base" id="drowsy-caption">
              <span>🟢</span><span>Бодрость</span>
            </div>
          </div>
        </div>
      </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome. Expected:
- Правая колонка содержит сетку 2×2
- Слева-сверху: Recovery с числом `78%` и зелёным прогресс-баром, caption «🟢 Хорошее восстановление»
- Справа-сверху: пустая карточка (placeholder для Sleep)
- Слева-снизу: Burnout `12%` зелёный, «🟢 Низкий риск»
- Справа-снизу: Drowsy `18%` зелёный, «🟢 Бодрость»

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Recovery/Burnout/Drowsy виджеты в правую колонку drilldown"
```

---

### Task 7: Sleep gauge — правая колонка

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §6.2

- [ ] **Step 1: Заменить Sleep placeholder на реальную карточку с концентрическими кольцами**

Заменить блок `<div id="sleep-card-placeholder" ...></div>` на:

```html
        <!-- Sleep с концентрическими кольцами -->
        <div class="rounded-2xl p-6 flex flex-col justify-between" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 240px;">
          <div class="flex items-start justify-between">
            <div class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Sleep</div>
            <div class="font-hero tnum leading-none" id="sleep-value" style="font-size: 44px;">7ч&nbsp;12м</div>
          </div>
          <div class="flex items-center gap-6">
            <svg width="140" height="140" viewBox="0 0 140 140" id="sleep-gauge">
              <!-- Незаполненные круги под cada кольцом -->
              <circle cx="70" cy="70" r="60" stroke="hsl(var(--muted) / 0.3)" stroke-width="6" fill="none"/>
              <circle cx="70" cy="70" r="48" stroke="hsl(var(--muted) / 0.3)" stroke-width="6" fill="none"/>
              <circle cx="70" cy="70" r="36" stroke="hsl(var(--muted) / 0.3)" stroke-width="6" fill="none"/>
              <!-- Заполненные дуги (pathLength=100 для % math) -->
              <circle cx="70" cy="70" r="60" stroke="hsl(var(--primary))" stroke-width="6" fill="none" pathLength="100" stroke-dasharray="22 100" stroke-dashoffset="0" transform="rotate(-90 70 70)" stroke-linecap="round"/>
              <circle cx="70" cy="70" r="48" stroke="hsl(var(--chart-2))" stroke-width="6" fill="none" pathLength="100" stroke-dasharray="28 100" stroke-dashoffset="0" transform="rotate(-90 70 70)" stroke-linecap="round"/>
              <circle cx="70" cy="70" r="36" stroke="hsl(var(--chart-4))" stroke-width="6" fill="none" pathLength="100" stroke-dasharray="50 100" stroke-dashoffset="0" transform="rotate(-90 70 70)" stroke-linecap="round"/>
            </svg>
            <div class="flex flex-col gap-2 text-xs font-data uppercase tracking-wide" style="color: hsl(var(--muted-foreground));">
              <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full" style="background: hsl(var(--primary));"></span>Deep 22%</div>
              <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full" style="background: hsl(var(--chart-2));"></span>REM 28%</div>
              <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full" style="background: hsl(var(--chart-4));"></span>Light 50%</div>
            </div>
          </div>
          <div class="flex items-center gap-2 text-base" id="sleep-caption">
            <span>🟢</span><span>Норма</span>
          </div>
        </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome. Expected:
- Карточка Sleep на месте placeholder'a
- Сверху: `Sleep` (label) слева, `7ч 12м` (число) справа
- В центре: 3 концентрических кольца (внешнее wine, среднее зелёное, внутреннее амбра) с разными заполнениями (22%, 28%, 50%)
- Справа от gauge: легенда `Deep 22% / REM 28% / Light 50%`
- Снизу: caption «🟢 Норма»

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Sleep gauge с концентрическими кольцами (Deep/REM/Light)"
```

---

### Task 8: Bayevsky Results блок — empty + done состояния

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §6.5

- [ ] **Step 1: Добавить Bayevsky-блок (оба варианта) под сеткой 2×2**

В `<section id="predictive-column">` **после** `<div id="predictive-grid-top">` (закрывающий тег которого был в Task 6/7) добавить:

```html
      <!-- Bayevsky Results — оба варианта в одном контейнере, переключаются по data-bayevsky -->
      <div class="rounded-2xl p-6 flex-1 flex flex-col items-center justify-center cursor-pointer transition hover:border-foreground" id="bayevsky-card" style="background: hsl(var(--card)); border: 1px solid hsl(var(--border)); min-height: 200px;" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">
        <!-- Empty state (до прохождения) -->
        <div id="bayevsky-empty" class="text-center">
          <div class="text-5xl mb-3">🧪</div>
          <div class="font-medium text-xl mb-2" style="color: hsl(var(--foreground));">ТЕСТ НЕ ПРОЙДЕН</div>
          <div class="text-base" style="color: hsl(var(--muted-foreground));">Запусти ниже ↓</div>
        </div>

        <!-- Done state (после прохождения) — скрыт по умолчанию -->
        <div id="bayevsky-done" class="hidden text-center w-full">
          <div class="font-data text-xs uppercase tracking-wider mb-3" style="color: hsl(var(--muted-foreground));">Bayevsky · ИН <span id="bayevsky-summary-in">145</span></div>
          <div class="font-medium text-2xl mb-2" id="bayevsky-verdict" style="color: hsl(var(--success));">🟢 Реактивность нормальная</div>
          <div class="text-sm" style="color: hsl(var(--muted-foreground));">Клик для деталей →</div>
        </div>
      </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome. Expected:
- Под сеткой 2×2 — широкая карточка с empty-state: иконка 🧪, заголовок `ТЕСТ НЕ ПРОЙДЕН`, caption `Запусти ниже ↓`
- Карточка кликабельна (cursor-pointer)
- Hover: рамка карточки светлеет
- Done-state (`#bayevsky-done`) пока скрыт (`.hidden`)

- [ ] **Step 3: Временно показать done-state для визуальной проверки**

В DevTools console:
```javascript
document.getElementById('bayevsky-empty').classList.add('hidden');
document.getElementById('bayevsky-done').classList.remove('hidden');
```

Expected: На месте empty появляется done-state: `Bayevsky · ИН 145` сверху, `🟢 Реактивность нормальная` (зелёный) в центре, `Клик для деталей →` снизу.

Вернуть в empty-state:
```javascript
document.getElementById('bayevsky-done').classList.add('hidden');
document.getElementById('bayevsky-empty').classList.remove('hidden');
```

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Bayevsky Results блок с empty/done состояниями"
```

---

### Task 9: Dev-bar + state-классы (CSS state machine)

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §10, §11

- [ ] **Step 1: Заполнить dev-bar (заменить пустой placeholder из Task 1)**

Заменить `<footer id="dev-bar" class="...">"</footer>` на:

```html
  <footer id="dev-bar" class="h-20 fixed bottom-0 left-0 right-0 backdrop-blur-sm border-t flex items-center gap-6 px-8" style="background: hsl(var(--card) / 0.8); border-color: hsl(var(--border)); z-index: 40;">
    <button id="back-to-wall" class="px-4 py-2 rounded-lg text-sm transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">
      ← на стену
    </button>
    <div class="flex items-center gap-3">
      <span class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Сценарий</span>
      <div class="flex items-center gap-2" id="state-pills">
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="empty">Empty</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm active" data-state="drilldown">Drilldown</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="phase-1">Phase-1</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="phase-2">Phase-2</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="phase-3">Phase-3</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="result">Result</button>
        <button class="state-pill px-3 py-1.5 rounded-full text-sm" data-state="claim">Claim</button>
      </div>
    </div>
    <div class="ml-auto font-data text-sm uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">
      STATE: <span id="state-indicator" style="color: hsl(var(--foreground));">drilldown</span>
    </div>
  </footer>
```

- [ ] **Step 2: Добавить CSS для pills и state-классов**

В `<style>` добавить:

```css
    .state-pill {
      background: hsl(var(--muted) / 0.5);
      color: hsl(var(--foreground));
      transition: background 0.15s;
    }
    .state-pill:hover { background: hsl(var(--muted)); }
    .state-pill.active {
      background: #831843;
      color: white;
    }

    /* State-классы — управляют видимостью элементов */
    /* По умолчанию все state-зависимые элементы скрыты, показываются по body.state-X */
    #bayevsky-modal, #claim-screen, #empty-banner { display: none; }

    body.state-phase-1 #bayevsky-modal,
    body.state-phase-2 #bayevsky-modal,
    body.state-phase-3 #bayevsky-modal,
    body.state-result #bayevsky-modal { display: flex; }

    body.state-claim #claim-screen { display: flex; }
    body.state-claim main,
    body.state-claim #empty-banner { display: none; }

    body.state-empty #empty-banner { display: flex; }
```

- [ ] **Step 3: Добавить JS state-switcher**

В `<script>` добавить (после bpm-кода):

```javascript
    /* State machine — переключение body-класса */
    const STATES = ['empty', 'drilldown', 'phase-1', 'phase-2', 'phase-3', 'result', 'claim'];
    function setState(newState) {
      STATES.forEach(s => document.body.classList.remove(`state-${s}`));
      document.body.classList.add(`state-${newState}`);
      document.getElementById('state-indicator').textContent = newState;
      document.querySelectorAll('.state-pill').forEach(p => {
        p.classList.toggle('active', p.dataset.state === newState);
      });
    }

    /* Bind dev-bar pills */
    document.querySelectorAll('.state-pill').forEach(p => {
      p.addEventListener('click', () => setState(p.dataset.state));
    });

    /* Back-to-wall */
    document.getElementById('back-to-wall').addEventListener('click', () => {
      window.location.href = 'kiosk-v2.html';
    });
```

- [ ] **Step 4: Verify visually**

Open in Chrome.

Expected:
- Dev-bar внизу содержит: `← на стену` слева, `Сценарий` + 7 pills в центре, `STATE: drilldown` справа
- Активная pill `Drilldown` подсвечена wine-цветом
- Клик по pill `Empty` — индикатор справа меняется на `empty`, pill становится активной
- Других визуальных изменений пока нет (state-зависимые элементы пока не созданы — будут в следующих задачах)
- Клик по `← на стену` — переход на `kiosk-v2.html` (404 ок если файл рядом нет — поведение корректно)

- [ ] **Step 5: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил dev-bar с 7 state-pills + state-machine на body-классах"
```

---

### Task 10: URL params + mock-switcher 3 персонажей

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §12, §13

- [ ] **Step 1: Добавить MOCK_DATA объект и функцию `applyPersona`**

В `<script>` добавить ДО state-machine кода:

```javascript
    /* Mock-данные по 3 персонажам — §13 */
    const MOCK_DATA = {
      kostya: {
        bpm: 82,
        ecgColor: 'hsl(var(--success))',
        stress: 41, stressLabel: 'Норма', stressColor: 'hsl(var(--success))',
        imuLabel: 'Покой', imuColor: 'hsl(var(--success))',
        recovery: 78, recoveryCap: '🟢 Хорошее восстановление', recoveryColor: 'hsl(var(--success))',
        sleep: '7ч 12м', sleepCap: '🟢 Норма', sleepDeep: 22, sleepRem: 28, sleepLight: 50,
        burnout: 12, burnoutCap: '🟢 Низкий риск', burnoutColor: 'hsl(var(--success))',
        drowsy: 18, drowsyCap: '🟢 Бодрость', drowsyColor: 'hsl(var(--success))',
        bayevsky: { done: true, in: 145, verdict: '🟢 Реактивность нормальная', color: 'hsl(var(--success))', phases: [{label:'ПОКОЙ', in:64, icon:'🟢', cap:'норма'},{label:'STROOP', in:145, icon:'🟢', cap:'норма'},{label:'ХОДЬБА', in:230, icon:'🟡', cap:'повышен.'}] }
      },
      alexey: {
        bpm: 90,
        ecgColor: 'hsl(var(--warning))',
        stress: 63, stressLabel: 'Высокий', stressColor: 'hsl(var(--destructive))',
        imuLabel: 'Покой', imuColor: 'hsl(var(--success))',
        recovery: 35, recoveryCap: '🟡 Частичное восстановление', recoveryColor: 'hsl(var(--warning))',
        sleep: '5ч 40м', sleepCap: '🟡 Граница нормы', sleepDeep: 14, sleepRem: 20, sleepLight: 66,
        burnout: 52, burnoutCap: '🔴 Высокий риск выгорания', burnoutColor: 'hsl(var(--destructive))',
        drowsy: 35, drowsyCap: '🟡 Лёгкая сонливость', drowsyColor: 'hsl(var(--warning))',
        bayevsky: { done: true, in: 320, verdict: '🟡 Повышенная реактивность', color: 'hsl(var(--warning))', phases: [{label:'ПОКОЙ', in:105, icon:'🟢', cap:'норма'},{label:'STROOP', in:320, icon:'🟡', cap:'повышен.'},{label:'ХОДЬБА', in:420, icon:'🟡', cap:'повышен.'}] }
      },
      guest: {
        bpm: 100,
        ecgColor: 'hsl(var(--primary))',
        stress: 50, stressLabel: 'Повышен', stressColor: 'hsl(var(--warning))',
        imuLabel: 'Покой', imuColor: 'hsl(var(--success))',
        recovery: null, recoveryCap: 'нет данных',
        sleep: null, sleepCap: 'нет данных',
        burnout: null, burnoutCap: 'нет данных',
        drowsy: null, drowsyCap: 'нет данных',
        bayevsky: { done: false }
      }
    };

    function applyPersona(personaKey) {
      const d = MOCK_DATA[personaKey] || MOCK_DATA.guest;
      bpmBase = d.bpm;
      document.getElementById('bpm-value').textContent = d.bpm;
      document.getElementById('ecg-pattern').style.color = d.ecgColor;

      document.getElementById('stress-value').textContent = d.stress;
      const stressChip = document.getElementById('stress-chip');
      stressChip.children[0].style.background = d.stressColor;
      stressChip.children[1].textContent = d.stressLabel;

      const imuChip = document.getElementById('imu-chip');
      imuChip.children[0].style.background = d.imuColor;
      imuChip.children[1].textContent = d.imuLabel;

      /* Recovery / Burnout / Drowsy — числа + bars + captions; null = «нет данных» */
      ['recovery', 'burnout', 'drowsy'].forEach(metric => {
        const val = d[metric];
        const valueEl = document.getElementById(`${metric}-value`);
        const barEl = document.getElementById(`${metric}-bar`);
        const capEl = document.getElementById(`${metric}-caption`);
        if (val === null) {
          valueEl.textContent = '—';
          barEl.style.width = '0%';
          capEl.innerHTML = `<span style="color: hsl(var(--muted-foreground));">${d[metric+'Cap']}</span>`;
        } else {
          valueEl.textContent = `${val}%`;
          barEl.style.width = `${val}%`;
          barEl.style.background = d[`${metric}Color`];
          capEl.innerHTML = d[`${metric}Cap`].replace(/^(🟢|🟡|🔴)\s*/, '<span>$1</span><span class="ml-2">') + '</span>';
        }
      });

      /* Sleep */
      const sleepVal = document.getElementById('sleep-value');
      const sleepCap = document.getElementById('sleep-caption');
      if (d.sleep === null) {
        sleepVal.textContent = '— ч — м';
        sleepCap.innerHTML = `<span style="color: hsl(var(--muted-foreground));">${d.sleepCap}</span>`;
        document.querySelectorAll('#sleep-gauge circle[pathLength]').forEach(c => c.style.opacity = '0.2');
      } else {
        sleepVal.innerHTML = d.sleep.replace(' ', '&nbsp;');
        sleepCap.innerHTML = d.sleepCap.replace(/^(🟢|🟡|🔴)\s*/, '<span>$1</span><span class="ml-2">') + '</span>';
        const gaugeCircles = document.querySelectorAll('#sleep-gauge circle[pathLength]');
        gaugeCircles[0].setAttribute('stroke-dasharray', `${d.sleepDeep} 100`);
        gaugeCircles[1].setAttribute('stroke-dasharray', `${d.sleepRem} 100`);
        gaugeCircles[2].setAttribute('stroke-dasharray', `${d.sleepLight} 100`);
        gaugeCircles.forEach(c => c.style.opacity = '1');
      }

      /* Bayevsky */
      if (d.bayevsky.done) {
        document.getElementById('bayevsky-empty').classList.add('hidden');
        document.getElementById('bayevsky-done').classList.remove('hidden');
        document.getElementById('bayevsky-summary-in').textContent = d.bayevsky.in;
        const verdictEl = document.getElementById('bayevsky-verdict');
        verdictEl.textContent = d.bayevsky.verdict;
        verdictEl.style.color = d.bayevsky.color;
      } else {
        document.getElementById('bayevsky-empty').classList.remove('hidden');
        document.getElementById('bayevsky-done').classList.add('hidden');
      }
    }

    /* URL params parsing */
    const urlParams = new URLSearchParams(window.location.search);
    const initialPersona = urlParams.get('id') || 'guest';
    const initialState = urlParams.get('session') === 'active' ? 'drilldown' : 'empty';
    applyPersona(initialPersona);
    setState(initialState);
```

- [ ] **Step 2: Добавить persona-switcher в dev-bar (опциональный — для удобства тестирования всех 3 в браузере)**

Вставить в dev-bar **перед** «STATE:» (т.е. перед `<div class="ml-auto ...">`):

```html
    <div class="flex items-center gap-3">
      <span class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Persona</span>
      <div class="flex items-center gap-2" id="persona-pills">
        <button class="persona-pill state-pill px-3 py-1.5 rounded-full text-sm" data-persona="kostya">Костя</button>
        <button class="persona-pill state-pill px-3 py-1.5 rounded-full text-sm" data-persona="alexey">Алексей</button>
        <button class="persona-pill state-pill px-3 py-1.5 rounded-full text-sm active" data-persona="guest">Гость</button>
      </div>
    </div>
```

В `<script>` после state-pill bindings добавить:

```javascript
    document.querySelectorAll('.persona-pill').forEach(p => {
      p.addEventListener('click', () => {
        document.querySelectorAll('.persona-pill').forEach(x => x.classList.remove('active'));
        p.classList.add('active');
        applyPersona(p.dataset.persona);
      });
    });

    /* Mark initial persona active */
    document.querySelector(`.persona-pill[data-persona="${initialPersona}"]`)?.classList.add('active');
    /* Уберём active с дефолтной guest-pill если URL передал другую */
    if (initialPersona !== 'guest') {
      document.querySelector('.persona-pill[data-persona="guest"]')?.classList.remove('active');
    }
```

- [ ] **Step 3: Verify visually**

Open in Chrome:
- `kiosk-drilldown.html` — должен открыться в state=empty с персоной Гость
- `kiosk-drilldown.html?id=kostya&session=active` — должен открыться в state=drilldown с данными Кости: BPM 82, NSI 41 Норма (зелёный чип), Recovery 78%, Sleep 7ч 12м, Burnout 12%, Drowsy 18%, Bayevsky-блок показывает done «🟢 Реактивность нормальная · ИН 145»
- `kiosk-drilldown.html?id=alexey&session=active` — данные Алексея: BPM 90, NSI 63 Высокий (красный), Recovery 35%, Sleep 5ч 40м, Burnout 52%, Drowsy 35%, Bayevsky «🟡 Повышенная реактивность · ИН 320»
- `kiosk-drilldown.html?id=guest&session=active` — данные Гостя: BPM 100, NSI 50 Повышен (амбра), Predictive все 4 виджета `—` / `нет данных`, Bayevsky empty-state «🧪 ТЕСТ НЕ ПРОЙДЕН»
- В dev-bar появилась группа `Persona [Костя] [Алексей] [Гость]` — клик переключает данные не перезагружая страницу

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил mock-данные 3 персонажей + URL params + persona-switcher в dev-bar"
```

---

### Task 11: Bayevsky modal overlay base + open/close JS

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §7.1

- [ ] **Step 1: Вставить контейнер модалки**

**Перед** `<footer id="dev-bar">` добавить:

```html
  <!-- Bayevsky modal overlay — §7 — visible при body.state-phase-1/2/3/result -->
  <div id="bayevsky-modal" class="fixed inset-0 items-center justify-center" style="z-index: 50; background: hsl(var(--background) / 0.7); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);">
    <div class="rounded-2xl shadow-2xl relative" style="width: 960px; height: 680px; background: hsl(var(--card)); border: 1px solid hsl(var(--border)); padding: 32px;">
      <!-- Phase-1 content — visible при body.state-phase-1 -->
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-1">
        <!-- заполнится в Task 12 -->
      </div>
      <!-- Phase-2 content -->
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-2">
        <!-- заполнится в Task 13 -->
      </div>
      <!-- Phase-3 content -->
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-3">
        <!-- заполнится в Task 12 (структура та же что Phase-1) -->
      </div>
      <!-- Result content -->
      <div class="phase-content w-full h-full flex flex-col" data-phase="result">
        <!-- заполнится в Task 14 -->
      </div>
    </div>
  </div>
```

- [ ] **Step 2: Добавить CSS для переключения phase-content**

В `<style>` добавить:

```css
    .phase-content { display: none; }
    body.state-phase-1 .phase-content[data-phase="phase-1"],
    body.state-phase-2 .phase-content[data-phase="phase-2"],
    body.state-phase-3 .phase-content[data-phase="phase-3"],
    body.state-result .phase-content[data-phase="result"] {
      display: flex;
    }
```

- [ ] **Step 3: Привязать кнопку «ТЕСТ» к открытию модалки**

В `<script>` после persona-pill bindings:

```javascript
    /* Кнопка ТЕСТ — открывает phase-1 */
    document.getElementById('btn-test').addEventListener('click', () => {
      setState('phase-1');
    });

    /* Bayevsky card клик — открывает result-модалку (если тест пройден) */
    document.getElementById('bayevsky-card').addEventListener('click', () => {
      const persona = document.querySelector('.persona-pill.active')?.dataset.persona || 'guest';
      if (MOCK_DATA[persona].bayevsky.done) {
        setState('result');
      }
    });
```

- [ ] **Step 4: Verify visually**

Open `kiosk-drilldown.html?id=kostya&session=active`:
- Клик ТЕСТ — drilldown размывается под backdrop blur 12px, появляется пустая модалка 960×680px по центру (содержимое появится в следующих задачах)
- Клик state-pill `Drilldown` в dev-bar — модалка исчезает, drilldown возвращается
- Клик state-pill `Result` — модалка появляется снова (пустая, контент в Task 14)
- Клик по `Bayevsky · ИН 145` карточке (когда done) — открывает result-модалку
- Клик по empty Bayevsky-карточке у Гостя — ничего не происходит (нет данных)

- [ ] **Step 5: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Bayevsky modal overlay base + open/close через state-pills и кнопку ТЕСТ"
```

---

### Task 12: Phase-1 (Покой) и Phase-3 (Быстрая ходьба)

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §7.2, §7.4

- [ ] **Step 1: Заполнить Phase-1 контент**

Заменить `<div class="phase-content ... data-phase="phase-1">` блок на:

```html
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-1">
        <div class="font-data text-sm uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Фаза 1 из 3</div>
        <div class="flex-1 flex flex-col items-center justify-center">
          <div class="font-hero tnum leading-none" id="phase-1-timer" style="font-size: 220px;">02:47</div>
          <div class="font-medium text-5xl mt-4">ПОКОЙ</div>
          <div class="text-xl mt-2" style="color: hsl(var(--muted-foreground));">Стой неподвижно, дыши спокойно</div>
        </div>
        <div class="h-2 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
          <div class="h-full rounded-full transition-all" id="phase-1-progress" style="width: 33%; background: #831843;"></div>
        </div>
      </div>
```

- [ ] **Step 2: Заполнить Phase-3 контент (структурно идентичен Phase-1, разное содержимое)**

Заменить `<div class="phase-content ... data-phase="phase-3">` блок на:

```html
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-3">
        <div class="font-data text-sm uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Фаза 3 из 3</div>
        <div class="flex-1 flex flex-col items-center justify-center">
          <div class="font-hero tnum leading-none" id="phase-3-timer" style="font-size: 220px;">00:54</div>
          <div class="font-medium text-5xl mt-4">БЫСТРАЯ ХОДЬБА</div>
          <div class="text-xl mt-2 text-center" style="color: hsl(var(--muted-foreground));">Быстро пройдитесь в течение 1 минуты,<br>чтобы поднять пульс</div>
        </div>
        <div class="h-2 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
          <div class="h-full rounded-full transition-all" id="phase-3-progress" style="width: 46%; background: #831843;"></div>
        </div>
      </div>
```

- [ ] **Step 3: Verify visually**

Open `kiosk-drilldown.html?id=kostya&session=active`:
- Клик state-pill `Phase-1` — модалка показывает большой таймер `02:47` (220px), под ним `ПОКОЙ` (48px) + caption «Стой неподвижно, дыши спокойно». Внизу прогресс-бар на 33%.
- Клик state-pill `Phase-3` — модалка показывает `00:54`, `БЫСТРАЯ ХОДЬБА`, caption про быструю ходьбу, прогресс-бар на 46%.

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил содержимое Phase-1 (Покой) и Phase-3 (Быстрая ходьба) модалок"
```

---

### Task 13: Phase-2 (Stroop)

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §7.3

- [ ] **Step 1: Заполнить Phase-2 контент**

Заменить `<div class="phase-content ... data-phase="phase-2">` блок на:

```html
      <div class="phase-content w-full h-full flex flex-col" data-phase="phase-2">
        <div class="flex items-center justify-between">
          <div class="font-data text-sm uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">Фаза 2 из 3</div>
          <div class="font-data tnum text-2xl" style="color: hsl(var(--foreground));">00:42</div>
        </div>
        <div class="flex-1 flex items-center justify-center">
          <div class="font-medium leading-none" style="font-size: 120px; color: hsl(var(--success));">КРАСНЫЙ</div>
        </div>
        <div class="grid grid-cols-4 gap-4 mb-6">
          <button class="h-14 rounded-xl text-lg font-medium transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">КРАСНЫЙ</button>
          <button class="h-14 rounded-xl text-lg font-medium transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">ЗЕЛЁНЫЙ</button>
          <button class="h-14 rounded-xl text-lg font-medium transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">СИНИЙ</button>
          <button class="h-14 rounded-xl text-lg font-medium transition" style="background: transparent; border: 1px solid hsl(var(--border)); color: hsl(var(--foreground));" onmouseover="this.style.borderColor='hsl(var(--foreground))'" onmouseout="this.style.borderColor='hsl(var(--border))'">ЖЁЛТЫЙ</button>
        </div>
        <div class="h-2 rounded-full overflow-hidden" style="background: hsl(var(--muted));">
          <div class="h-full rounded-full" style="width: 72%; background: #831843;"></div>
        </div>
      </div>
```

- [ ] **Step 2: Verify visually**

Open in Chrome, переключить на `Phase-2`:
- В шапке модалки: слева `Фаза 2 из 3`, справа `00:42`
- В центре: слово `КРАСНЫЙ` крупным шрифтом (120px), цвет — зелёный (success-цвет, классический Stroop эффект «слово ≠ цвет»)
- Под центром: 4 ghost-кнопки в ряд: `КРАСНЫЙ` / `ЗЕЛЁНЫЙ` / `СИНИЙ` / `ЖЁЛТЫЙ`
- Внизу: прогресс-бар на 72%
- Клик по кнопкам — заглушка (не делаем рабочую механику)

- [ ] **Step 3: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил содержимое Phase-2 (Stroop) модалки с 4 кнопками-вариантами"
```

---

### Task 14: Result-модалка + закрытие → drilldown с заполненным Bayevsky

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §7.5, §6.5.2

- [ ] **Step 1: Заполнить Result-контент**

Заменить `<div class="phase-content ... data-phase="result">` блок на:

```html
      <div class="phase-content w-full h-full flex flex-col" data-phase="result">
        <div class="flex items-center justify-between mb-4">
          <div class="font-medium text-2xl">Результат теста Баевского</div>
          <button id="result-close" class="w-10 h-10 rounded-full flex items-center justify-center text-xl transition" style="background: transparent; color: hsl(var(--muted-foreground));" onmouseover="this.style.background='hsl(var(--muted))'" onmouseout="this.style.background='transparent'">×</button>
        </div>
        <div class="grid grid-cols-3 gap-6" id="result-phases">
          <!-- 3 фазовые плашки — заполняются JS-функцией updateResult() -->
        </div>
        <div class="flex-1 flex flex-col items-center justify-center">
          <div class="font-data text-sm uppercase tracking-wider mb-2" style="color: hsl(var(--muted-foreground));">Индекс напряжения Σ</div>
          <div class="font-hero tnum leading-none" id="result-in-sum" style="font-size: 120px; color: hsl(var(--success));">145</div>
        </div>
        <div class="text-center">
          <div class="font-medium text-2xl uppercase" id="result-verdict" style="color: hsl(var(--success));">🟢 Реактивность нормальная</div>
          <div class="text-base mt-2" style="color: hsl(var(--foreground));">Здоровая адаптация ВНС к нагрузкам</div>
        </div>
      </div>
```

- [ ] **Step 2: Добавить функцию `updateResult()`**

В `<script>` после `applyPersona`:

```javascript
    function updateResult() {
      const persona = document.querySelector('.persona-pill.active')?.dataset.persona || 'guest';
      const data = MOCK_DATA[persona].bayevsky;
      if (!data.done) return;
      const phasesContainer = document.getElementById('result-phases');
      phasesContainer.innerHTML = data.phases.map(p => `
        <div class="rounded-xl p-4 flex flex-col items-center" style="background: hsl(var(--muted) / 0.3); border: 1px solid hsl(var(--border));">
          <div class="font-data text-xs uppercase tracking-wider" style="color: hsl(var(--muted-foreground));">${p.label}</div>
          <div class="font-hero tnum leading-none my-2" style="font-size: 64px; color: ${p.icon === '🟢' ? 'hsl(var(--success))' : 'hsl(var(--warning))'};">${p.in}</div>
          <div class="text-2xl">${p.icon}</div>
          <div class="text-sm" style="color: ${p.icon === '🟢' ? 'hsl(var(--success))' : 'hsl(var(--warning))'};">${p.cap}</div>
        </div>
      `).join('');
      document.getElementById('result-in-sum').textContent = data.in;
      document.getElementById('result-in-sum').style.color = data.color;
      document.getElementById('result-verdict').textContent = data.verdict;
      document.getElementById('result-verdict').style.color = data.color;
    }

    /* Запускать updateResult() при входе в state=result */
    const _setState = setState;
    setState = function(newState) {
      _setState(newState);
      if (newState === 'result') updateResult();
    };

    /* Close-X — возврат в drilldown с заполненным Bayevsky */
    document.getElementById('result-close').addEventListener('click', () => {
      /* После теста — отметить Bayevsky как пройденный для текущей персоны */
      const persona = document.querySelector('.persona-pill.active')?.dataset.persona || 'guest';
      if (!MOCK_DATA[persona].bayevsky.done) {
        /* Для guest симулируем «прошёл тест прямо сейчас» — даём ему mock-результат как у Кости */
        MOCK_DATA[persona].bayevsky = MOCK_DATA.kostya.bayevsky;
        applyPersona(persona);
      }
      setState('drilldown');
    });
```

- [ ] **Step 3: Verify visually**

Open `kiosk-drilldown.html?id=kostya&session=active`:
- Клик state-pill `Result` — модалка показывает: заголовок `Результат теста Баевского` + close-X справа; 3 плашки в ряд: ПОКОЙ 64 🟢 норма / STROOP 145 🟢 норма / ХОДЬБА 230 🟡 повышен.; в центре `Индекс напряжения Σ` + большое `145` зелёное; снизу `🟢 РЕАКТИВНОСТЬ НОРМАЛЬНАЯ` + описание.
- Переключить персону на Алексея → state=result: ПОКОЙ 105 🟢 / STROOP 320 🟡 / ХОДЬБА 420 🟡, ИН Σ 320 (амбра), вердикт «🟡 Повышенная реактивность».
- Клик × — модалка закрывается, drilldown возвращается, Bayevsky-карточка справа показывает заполненный summary.

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил Result-модалку с 3 фазовыми плашками + close-X → drilldown с заполн. Bayevsky"
```

---

### Task 15: Claim state — полноэкранный QR + кнопка Готово

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §8

- [ ] **Step 1: Вставить claim-экран**

**Перед** `<footer id="dev-bar">` (рядом с `#bayevsky-modal`) добавить:

```html
  <!-- Claim state — §8 — visible при body.state-claim, скрывает main -->
  <div id="claim-screen" class="fixed inset-0 flex-col items-center justify-center" style="z-index: 30; background: hsl(var(--background));">
    <div class="absolute top-8 left-0 right-0 text-center">
      <span class="text-2xl font-medium">Сессия завершена · </span><span class="font-data tnum text-2xl" style="color: hsl(var(--muted-foreground));">sess_7K2M9</span>
    </div>
    <!-- Placeholder QR (SVG pattern, без реальной генерации) -->
    <div class="p-6 rounded-2xl" style="background: white; border: 1px solid hsl(var(--border));">
      <svg width="400" height="400" viewBox="0 0 100 100" style="display: block;">
        <!-- Простой checker-pattern как заглушка QR -->
        <rect x="0" y="0" width="100" height="100" fill="white"/>
        <g fill="black">
          <!-- Уголки-маркеры QR -->
          <rect x="2" y="2" width="20" height="20"/>
          <rect x="5" y="5" width="14" height="14" fill="white"/>
          <rect x="8" y="8" width="8" height="8" fill="black"/>
          <rect x="78" y="2" width="20" height="20"/>
          <rect x="81" y="5" width="14" height="14" fill="white"/>
          <rect x="84" y="8" width="8" height="8" fill="black"/>
          <rect x="2" y="78" width="20" height="20"/>
          <rect x="5" y="81" width="14" height="14" fill="white"/>
          <rect x="8" y="84" width="8" height="8" fill="black"/>
          <!-- Pseudo-random data cells -->
          <rect x="26" y="2" width="4" height="4"/>
          <rect x="34" y="6" width="4" height="4"/>
          <rect x="42" y="2" width="4" height="4"/>
          <rect x="50" y="10" width="4" height="4"/>
          <rect x="58" y="2" width="4" height="4"/>
          <rect x="66" y="6" width="4" height="4"/>
          <rect x="2" y="26" width="4" height="4"/>
          <rect x="14" y="30" width="4" height="4"/>
          <rect x="26" y="26" width="4" height="4"/>
          <rect x="34" y="34" width="4" height="4"/>
          <rect x="42" y="26" width="4" height="4"/>
          <rect x="50" y="34" width="4" height="4"/>
          <rect x="58" y="42" width="4" height="4"/>
          <rect x="66" y="34" width="4" height="4"/>
          <rect x="78" y="30" width="4" height="4"/>
          <rect x="90" y="26" width="4" height="4"/>
          <rect x="6" y="50" width="4" height="4"/>
          <rect x="18" y="58" width="4" height="4"/>
          <rect x="30" y="50" width="4" height="4"/>
          <rect x="42" y="58" width="4" height="4"/>
          <rect x="54" y="50" width="4" height="4"/>
          <rect x="66" y="58" width="4" height="4"/>
          <rect x="78" y="50" width="4" height="4"/>
          <rect x="90" y="58" width="4" height="4"/>
          <rect x="30" y="78" width="4" height="4"/>
          <rect x="42" y="86" width="4" height="4"/>
          <rect x="54" y="78" width="4" height="4"/>
          <rect x="66" y="86" width="4" height="4"/>
          <rect x="78" y="78" width="4" height="4"/>
          <rect x="90" y="86" width="4" height="4"/>
        </g>
      </svg>
    </div>
    <div class="mt-8 text-2xl text-center max-w-xl">
      Гость, отсканируй чтобы получить<br>отчёт о сессии в Telegram
    </div>
    <button id="claim-done" class="absolute bottom-8 right-8 px-12 py-4 rounded-xl font-medium text-lg transition" style="background: #831843; color: white;" onmouseover="this.style.background='#9a1d50'" onmouseout="this.style.background='#831843'">Готово</button>
  </div>
```

- [ ] **Step 2: Привязать кнопку СТОП к claim, и кнопку «Готово» к redirect**

В `<script>` после Bayevsky bindings:

```javascript
    /* Кнопка СТОП в drilldown — переход в claim */
    document.getElementById('btn-stop').addEventListener('click', () => {
      setState('claim');
    });

    /* Кнопка Готово в claim — redirect на стену */
    document.getElementById('claim-done').addEventListener('click', () => {
      window.location.href = 'kiosk-v2.html';
    });
```

- [ ] **Step 3: Verify visually**

Open `kiosk-drilldown.html?id=kostya&session=active`:
- Клик `СТОП` в левой колонке — drilldown заменяется полноэкранным claim: вверху `Сессия завершена · sess_7K2M9`, в центре большой QR (placeholder pattern) 400×400, под ним «Гость, отсканируй чтобы получить отчёт о сессии в Telegram», справа-снизу кнопка `Готово` (wine fill).
- Клик state-pill `Drilldown` в dev-bar — возврат в drilldown.
- Клик `Готово` в claim — redirect на kiosk-v2.html.

- [ ] **Step 4: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил claim-state с placeholder QR 400×400 + кнопка Готово → kiosk-v2"
```

---

### Task 16: Empty state — баннер + skeleton-плейсхолдеры + loss-of-connection

**Files:**
- Modify: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §9

- [ ] **Step 1: Добавить баннер empty**

**После** `<header>` (top-bar), **перед** `<main>`, добавить:

```html
  <!-- Empty state banner — §9.1 — visible при body.state-empty -->
  <div id="empty-banner" class="h-12 items-center justify-center text-center" style="background: hsl(var(--muted));">
    <span class="inline-flex items-center gap-2 font-medium">
      <span class="w-2 h-2 rounded-full" style="background: hsl(var(--warning)); animation: pulse 2s ease-in-out infinite;"></span>
      Ожидание сессии · Калибруйте гостя через стену
    </span>
  </div>
```

В `<style>` добавить keyframes pulse:

```css
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
```

- [ ] **Step 2: Добавить логику skeleton-плейсхолдеров в `applyPersona`**

В функцию `applyPersona` добавить **в конце** (после Bayevsky-логики):

```javascript
      /* Empty-state: если body.state-empty — затирать все live-значения skeleton */
      if (document.body.classList.contains('state-empty')) {
        document.getElementById('bpm-value').textContent = '—';
        document.getElementById('bpm-status-chip').children[0].style.background = 'hsl(var(--warning))';
        document.getElementById('bpm-status-chip').children[1].textContent = 'Нет связи';
        document.getElementById('stress-value').textContent = '—';
        document.getElementById('stress-chip').style.opacity = '0';
        document.getElementById('imu-chip').style.opacity = '0';
        ['recovery', 'burnout', 'drowsy'].forEach(metric => {
          document.getElementById(`${metric}-value`).textContent = '—';
          document.getElementById(`${metric}-bar`).style.width = '0%';
          document.getElementById(`${metric}-caption`).innerHTML = '<span style="color: hsl(var(--muted-foreground));">нет данных</span>';
        });
        document.getElementById('sleep-value').textContent = '— ч — м';
        document.querySelectorAll('#sleep-gauge circle[pathLength]').forEach(c => c.style.opacity = '0.2');
        document.getElementById('btn-stop').disabled = true; document.getElementById('btn-stop').style.opacity = '0.5'; document.getElementById('btn-stop').style.cursor = 'not-allowed';
        document.getElementById('btn-test').disabled = true; document.getElementById('btn-test').style.opacity = '0.5'; document.getElementById('btn-test').style.cursor = 'not-allowed';
      } else {
        document.getElementById('stress-chip').style.opacity = '1';
        document.getElementById('imu-chip').style.opacity = '1';
        document.getElementById('btn-stop').disabled = false; document.getElementById('btn-stop').style.opacity = '1'; document.getElementById('btn-stop').style.cursor = 'pointer';
        document.getElementById('btn-test').disabled = false; document.getElementById('btn-test').style.opacity = '1'; document.getElementById('btn-test').style.cursor = 'pointer';
      }
```

И заменить переопределение `setState` (которое было в Task 14) — теперь оно должно ещё и переапплаить персону при выходе из empty:

```javascript
    /* Запускать updateResult() при входе в state=result + applyPersona при смене state */
    const _setState = setState;
    setState = function(newState) {
      _setState(newState);
      if (newState === 'result') updateResult();
      const persona = document.querySelector('.persona-pill.active')?.dataset.persona || 'guest';
      applyPersona(persona);
    };
```

- [ ] **Step 3: Добавить loss-of-connection toggle в dev-bar**

В dev-bar **перед** `<div class="ml-auto ...">` (т.е. рядом с STATE-индикатором):

```html
    <button id="ble-toggle" class="px-3 py-1.5 rounded-full text-sm transition font-data uppercase tracking-wide" style="background: hsl(var(--muted) / 0.5); color: hsl(var(--foreground));" onmouseover="this.style.background='hsl(var(--muted))'" onmouseout="this.style.background='hsl(var(--muted) / 0.5)'">
      <span id="ble-toggle-label">BLE: connected</span>
    </button>
```

В `<script>` после claim-bindings:

```javascript
    /* BLE toggle — sub-state «потеря связи» */
    document.getElementById('ble-toggle').addEventListener('click', () => {
      const isDisconnected = document.body.classList.toggle('state-disconnected');
      document.getElementById('ble-toggle-label').textContent = isDisconnected ? 'BLE: потеря связи' : 'BLE: connected';
      const chip = document.getElementById('bpm-status-chip');
      if (isDisconnected) {
        chip.children[0].style.background = 'hsl(var(--warning))';
        chip.children[1].textContent = 'Потеря связи';
        /* «Замораживаем» BPM: останавливаем live-обновление */
        bpmBase = parseInt(document.getElementById('bpm-value').textContent) || 82;
        window._bpmFrozen = true;
        /* ECG flat-line */
        document.querySelectorAll('#ecg-pattern path').forEach(p => p.setAttribute('d', 'M 0 54 L 884 54'));
      } else {
        chip.children[0].style.background = 'hsl(var(--success))';
        chip.children[1].textContent = 'Подключен';
        window._bpmFrozen = false;
        /* Восстановим ECG — простой reload не делаем, оставим как минимальную деградацию для wireframe */
        /* Чтобы вернуть pattern, перезагрузить страницу или переключить персону */
      }
    });

    /* Обновим fake-BPM, чтобы он не тикал при frozen */
```

И в коде fake live BPM (Task 2) изменить interval:

```javascript
    setInterval(() => {
      if (window._bpmFrozen) return;
      bpmTick++;
      const variation = Math.sin(bpmTick / 3) * 2;
      const value = Math.round(bpmBase + variation);
      document.getElementById('bpm-value').textContent = value;
    }, 800);
```

- [ ] **Step 4: Verify visually**

Open `kiosk-drilldown.html` (без `&session=active`):
- Сверху появляется баннер «● Ожидание сессии · Калибруйте гостя через стену» (точка пульсирует)
- BPM = `—`, чип `● Нет связи` (амбра)
- NSI = `—`, чипы скрыты (opacity 0)
- Recovery/Burnout/Drowsy/Sleep все показывают `—` / `нет данных`, бары на 0
- Кнопки СТОП/ТЕСТ заблокированы (opacity 50%, not-allowed cursor)
- Bayevsky показывает empty-state

Open `kiosk-drilldown.html?id=kostya&session=active`:
- Клик `BLE: connected` в dev-bar — меняется на `BLE: потеря связи`. BPM-чип меняется с «Подключен» на «Потеря связи» (амбра), BPM-число фризится, ECG превращается в flat-line.
- Клик повторно — возврат в connected. ECG flat остаётся (нужен page reload или persona-switch — это известная минор-деградация в wireframe).

- [ ] **Step 5: Commit**

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY add docs_web/wireframes/m2/kiosk-drilldown.html
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY commit -m "Добавил empty-state (skeleton + баннер) и sub-state потеря связи с toggle в dev-bar"
```

---

### Task 17: Финальная acceptance проверка + push

**Files:**
- Verify only: `docs_web/wireframes/m2/kiosk-drilldown.html`

**Spec ref:** §15 (acceptance criteria)

- [ ] **Step 1: Прогнать все 17 пунктов acceptance из spec §15**

Open `docs_web/wireframes/m2/kiosk-drilldown.html` в Chrome на 1920×1080 (или DevTools toolbar set device). Пройти по списку — записать FAIL/PASS:

| # | Проверка | Статус |
|---|---|---|
| 1 | Файл валидно открывается без JS-ошибок в DevTools console | |
| 2 | Top-bar 64px со всеми элементами в правильных позициях | |
| 3 | Левая колонка содержит 5 блоков (BPM, ECG, 2 круга, 2 кнопки) без overflow | |
| 4 | Правая колонка содержит 4 виджета 2×2 (Recovery/Sleep/Burnout/Drowsy) + Bayevsky | |
| 5 | Dev-bar 80px снизу с 7 state-pills (+ persona-pills + BLE toggle), активная — wine | |
| 6 | `?id=kostya / alexey / guest` меняет mock-данные на всех виджетах | |
| 7 | URL без `&session=active` → state=empty с skeleton + баннер | |
| 8 | URL с `&session=active` → state=drilldown с живыми данными | |
| 9 | Клик ТЕСТ → модалка Phase-1 с таймером 220px, drilldown под backdrop blur | |
| 10 | Dev-bar pills [Phase-1/2/3/Result] переключают контент модалки | |
| 11 | Result-модалка: 3 фазовых плашки + ИН Σ + вердикт | |
| 12 | Клик × в result → drilldown теперь с заполненным Bayevsky summary | |
| 13 | Клик СТОП → state=claim, полноэкранный QR | |
| 14 | Кнопка «Готово» в claim → redirect на kiosk-v2.html | |
| 15 | Цвета через semantic shadcn vars, hex только wine #831843 | |
| 16 | BPM «дышит» + ECG scroll влево | |
| 17 | Микро-чипы (подключен/повышен/высокий/норма/покой) визуально консистентны | |
| 18 | Никаких упоминаний VITRO/VANTA/VIGOR/M1/M2/M3/Сбер/Райффайзенбанк/Газпром | |

Все 18 пунктов должны быть PASS.

- [ ] **Step 2: Снять proof-screenshots по 7 состояниям + 3 персонажа**

Перейти по URL'ам и сделать скриншоты (Chrome DevTools → Capture full size screenshot):
- `kiosk-drilldown.html` (empty)
- `kiosk-drilldown.html?id=kostya&session=active` (drilldown)
- `kiosk-drilldown.html?id=alexey&session=active` (drilldown с Алексеем)
- `kiosk-drilldown.html?id=guest&session=active` (drilldown с Гостем, Bayevsky empty)
- В Кости: переключить state-pills → Phase-1 → screenshot
- Phase-2 → screenshot
- Phase-3 → screenshot
- Result → screenshot
- Claim → screenshot

Скриншоты прислать PM в отчёте (или приложить в commit message при необходимости).

- [ ] **Step 3: Финальный commit (если были косметические fix'ы) + push**

Если на Step 1 были FAIL — внести исправления и сделать commit. Если всё PASS — просто push текущей ветки:

```bash
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY status
git -C /Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY push
```

GitPages деплоится 1-2 минуты. Проверить публичную ссылку (см. `~/.claude/projects/-Users-solomono-Desktop-NOW---------NEIRY/memory/project_gitpages.md` для URL).

- [ ] **Step 4: Доложить PM**

Сформулировать отчёт в формате `DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED`:

- **DONE** если все 18 acceptance-пунктов PASS + 9 скриншотов сделаны
- **DONE_WITH_CONCERNS** если что-то не идеально, но работает (например: ECG-recovery после loss-of-connection требует page-reload) — перечислить concerns в отчёте
- **NEEDS_CONTEXT** если по ходу всплыли вопросы (например: какой fallback при `?id=unknown`)
- **BLOCKED** если что-то критичное не работает

Ждать **явного «принято»** от PM прежде чем считать задачу закрытой.

---

## Self-Review (выполнено автором плана)

**Spec coverage:**
- §1 (контекст) — отражено в Goal/Architecture
- §2 (стек) — Task 1 (CSS-токены + шрифты + tailwind)
- §3 (сетка) — Task 1 (top-bar высота, main `calc(100vh - 144px)`, padding 32)
- §4 (top-bar) — Task 1 (логотип + session-ID + таймер)
- §5.1 BPM — Task 2
- §5.2 ECG — Task 3
- §5.3 Stress+IMU — Task 4
- §5.4 кнопки — Task 5
- §5.5 чипы — Task 2, 4 (паттерн повторяется консистентно)
- §6.1 Recovery — Task 6
- §6.2 Sleep — Task 7
- §6.3 Burnout — Task 6
- §6.4 Drowsy — Task 6
- §6.5 Bayevsky empty+done — Task 8
- §7.1 modal overlay base — Task 11
- §7.2 Phase-1 — Task 12
- §7.3 Phase-2 — Task 13
- §7.4 Phase-3 — Task 12
- §7.5 Result — Task 14
- §8 Claim — Task 15
- §9.1 баннер — Task 16
- §9.2 skeleton — Task 16
- §9.3 loss-of-connection — Task 16
- §10 dev-bar — Task 9
- §11 state-machine — Task 9 (CSS-классы) + Task 10 (JS setState)
- §12 URL params — Task 10
- §13 mock-данные 3 персонажей — Task 10
- §14 шкалы (справочно) — отражены в MOCK_DATA значениях
- §15 acceptance — Task 17
- §16 анти-скоуп — учтено (нет рабочей Stroop-механики в Task 13, нет реального QR в Task 15)

**Type consistency:** ID элементов проверены — `bpm-value`, `stress-value`, `recovery-value`, `burnout-value`, `drowsy-value`, `sleep-value`, `bayevsky-card`, `bayevsky-empty`, `bayevsky-done`, `bayevsky-summary-in`, `bayevsky-verdict`, `phase-1-timer`, `phase-3-timer`, `result-in-sum`, `result-verdict`, `result-phases`, `result-close`, `claim-done`, `back-to-wall`, `state-indicator`, `ble-toggle`, `btn-stop`, `btn-test`, `empty-banner`, `bayevsky-modal`, `claim-screen`, `ecg-pattern`, `ecg-path-1`, `ecg-path-2`, `sleep-gauge`, `recovery-bar`, `burnout-bar`, `drowsy-bar`, `recovery-caption`, `burnout-caption`, `drowsy-caption`, `sleep-caption`, `bpm-status-chip`, `stress-chip`, `imu-chip` — все ID согласованы между задачами.

**Placeholder scan:** Нет TBD/TODO/«implement later». Все code-snippets полные.

**No-placeholder check:** код в каждой задаче работоспособный, можно копировать-вставлять.

---

Plan complete and saved to `docs_web/docs/superpowers/plans/2026-05-26-m2-kiosk-drilldown.md`. Three execution options:

**1. Subagent-Driven (recommended)** — отдельный субагент на каждую из 17 задач, two-stage review (spec compliance + code quality) между задачами, быстрая итерация без переключения сессии

**2. Inline Execution** — выполняю задачи в этой сессии последовательно с чекпоинтами

**3. Task Master** — сначала инициализирую постоянный трекер задач (mcp__task-master-ai__parse_prd), потом выполняю. Подходит если работа многодневная или ты хочешь возвращаться к ней между сессиями. После инициализации выбираешь 1 или 2 для исполнения.

Какой подход выбираешь?
