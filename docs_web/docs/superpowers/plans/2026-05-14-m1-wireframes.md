# M1 Tech Demo Wireframes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Создать 7 HTML-прототипов для M1 Tech Demo — 4 мобайл-экрана, 2 дашборд-экрана и index-обзор обоих флоу.

**Architecture:** Каждый экран — self-contained HTML с Tailwind CDN и Google Fonts. Общие паттерны (телефонная рамка, цвета, типографика) копируются между файлами — никакого build step. Index показывает iframe-превью всех экранов, масштабированные через CSS transform, с нумерацией шагов.

**Tech Stack:** HTML5, Tailwind CSS (Play CDN — `https://cdn.tailwindcss.com`), Google Fonts (Manrope / Fraunces / JetBrains Mono), CSS-анимация `@keyframes pulse` для BLE-экрана.

---

## Цвета (использовать везде)

| Назначение | HEX |
|---|---|
| Фон экрана | `#0f0e0b` |
| Фон карточек / inputs | `#1a1814` |
| Рамка телефона / borders | `#2a2620` |
| Текст основной | `#f7f6f1` |
| Текст вторичный | `#7a766d` |
| Placeholder | `#4a463e` |
| Accent мобайл (кнопки) | `#831843` |
| Accent дашборд (кнопки) | `#1e3a8a` |
| Connected / Online | `#166534` |

---

## Task 1: mobile-registration.html

**Files:**
- Create: `docs_web/wireframes/m1/mobile-registration.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Регистрация · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b] flex items-center justify-center p-8">

  <div class="relative rounded-[3rem] border-[6px] border-[#2a2620] shadow-2xl w-[390px] h-[844px] overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-28 h-7 bg-[#2a2620] rounded-b-2xl z-10"></div>
    <div class="w-full h-full bg-[#0f0e0b] flex flex-col px-7 pt-16 pb-10">

      <div class="mt-8 mb-10">
        <p class="font-brand text-3xl text-[#f7f6f1] leading-tight">Neiry <span class="text-[#831843] italic">Pulse</span></p>
        <p class="text-[#7a766d] text-sm mt-1">Мониторинг сердечного ритма</p>
      </div>

      <h1 class="text-[#f7f6f1] text-2xl font-semibold mb-8">Создать аккаунт</h1>

      <div class="flex flex-col gap-4">
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Email</label>
          <div class="w-full bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            user@example.com
          </div>
        </div>
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Пароль</label>
          <div class="w-full bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            ••••••••
          </div>
        </div>
      </div>

      <a href="mobile-login.html"
         class="mt-8 w-full bg-[#831843] text-[#f7f6f1] text-sm font-semibold rounded-xl py-4 text-center block hover:opacity-90 transition-opacity">
        Создать аккаунт
      </a>

      <p class="mt-auto text-center text-[#7a766d] text-sm">
        Уже есть аккаунт?
        <a href="mobile-login.html" class="text-[#f7f6f1] underline ml-1">Войти</a>
      </p>

    </div>
  </div>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

Открыть файл в браузере. Проверить:
- [ ] Телефонная рамка отображается с закруглёнными углами и тёмной окантовкой
- [ ] Чёрный вырез-нотч сверху по центру
- [ ] Логотип «Neiry *Pulse*» — Fraunces, «Pulse» в `#831843`
- [ ] Поля email и пароль видны с placeholder-текстом
- [ ] Кнопка «Создать аккаунт» — бордовая, во всю ширину
- [ ] Ссылка «Войти» внизу

- [ ] **Step 3: Коммит**

```bash
cd /path/to/NEIRY
git add docs_web/wireframes/m1/mobile-registration.html
git commit -m "Добавил экран регистрации M1"
```

---

## Task 2: mobile-login.html

**Files:**
- Create: `docs_web/wireframes/m1/mobile-login.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Логин · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b] flex items-center justify-center p-8">

  <div class="relative rounded-[3rem] border-[6px] border-[#2a2620] shadow-2xl w-[390px] h-[844px] overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-28 h-7 bg-[#2a2620] rounded-b-2xl z-10"></div>
    <div class="w-full h-full bg-[#0f0e0b] flex flex-col px-7 pt-16 pb-10">

      <div class="mt-8 mb-10">
        <p class="font-brand text-3xl text-[#f7f6f1] leading-tight">Neiry <span class="text-[#831843] italic">Pulse</span></p>
        <p class="text-[#7a766d] text-sm mt-1">Мониторинг сердечного ритма</p>
      </div>

      <h1 class="text-[#f7f6f1] text-2xl font-semibold mb-8">Добро пожаловать</h1>

      <div class="flex flex-col gap-4">
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Email</label>
          <div class="w-full bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            user@example.com
          </div>
        </div>
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Пароль</label>
          <div class="w-full bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            ••••••••
          </div>
        </div>
      </div>

      <a href="mobile-ble-pairing.html"
         class="mt-8 w-full bg-[#831843] text-[#f7f6f1] text-sm font-semibold rounded-xl py-4 text-center block hover:opacity-90 transition-opacity">
        Войти
      </a>

      <p class="mt-auto text-center text-[#7a766d] text-sm">
        Нет аккаунта?
        <a href="mobile-registration.html" class="text-[#f7f6f1] underline ml-1">Зарегистрироваться</a>
      </p>

    </div>
  </div>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Заголовок «Добро пожаловать»
- [ ] Кнопка «Войти» — ведёт на `mobile-ble-pairing.html`
- [ ] Ссылка «Зарегистрироваться» — ведёт на `mobile-registration.html`

- [ ] **Step 3: Коммит**

```bash
git add docs_web/wireframes/m1/mobile-login.html
git commit -m "Добавил экран логина M1"
```

---

## Task 3: mobile-ble-pairing.html

**Files:**
- Create: `docs_web/wireframes/m1/mobile-ble-pairing.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BLE Pairing · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }
  @keyframes ble-pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(1.08); }
  }
  .ble-pulse { animation: ble-pulse 1.8s ease-in-out infinite; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b] flex items-center justify-center p-8">

  <div class="relative rounded-[3rem] border-[6px] border-[#2a2620] shadow-2xl w-[390px] h-[844px] overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-28 h-7 bg-[#2a2620] rounded-b-2xl z-10"></div>
    <div class="w-full h-full bg-[#0f0e0b] flex flex-col px-7 pt-16 pb-10">

      <h1 class="mt-10 text-[#f7f6f1] text-2xl font-semibold">Подключить браслет</h1>
      <p class="text-[#7a766d] text-sm mt-2">Убедитесь, что браслет рядом и включён</p>

      <div class="flex flex-col items-center mt-10 mb-8">
        <div class="ble-pulse w-24 h-24 rounded-full border-2 border-[#831843] flex items-center justify-center">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
            <path d="M6.5 8.5L17.5 17.5M17.5 6.5L6.5 15.5M12 4V20M17.5 6.5L12 12L17.5 17.5" stroke="#831843" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>
        <p class="font-data text-[#7a766d] text-xs mt-4 tracking-widest">ПОИСК УСТРОЙСТВ…</p>
      </div>

      <div class="flex flex-col gap-3">
        <div class="bg-[#1a1814] border border-[#831843] rounded-xl px-4 py-3 flex items-center justify-between">
          <div>
            <p class="font-data text-[#f7f6f1] text-sm">VITRO_A3F2</p>
            <p class="text-[#7a766d] text-xs mt-0.5">−62 dBm</p>
          </div>
          <a href="mobile-home.html"
             class="bg-[#831843] text-[#f7f6f1] text-xs font-semibold rounded-lg px-4 py-2 hover:opacity-90 transition-opacity">
            Подключить
          </a>
        </div>
        <div class="bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 flex items-center justify-between">
          <div>
            <p class="font-data text-[#7a766d] text-sm">VITRO_B1C9</p>
            <p class="text-[#7a766d] text-xs mt-0.5">−74 dBm</p>
          </div>
          <button class="border border-[#2a2620] text-[#7a766d] text-xs rounded-lg px-4 py-2">
            Подключить
          </button>
        </div>
        <div class="bg-[#1a1814] border border-[#2a2620] rounded-xl px-4 py-3 flex items-center justify-between">
          <div>
            <p class="font-data text-[#7a766d] text-sm">VITRO_D7E0</p>
            <p class="text-[#7a766d] text-xs mt-0.5">−81 dBm</p>
          </div>
          <button class="border border-[#2a2620] text-[#7a766d] text-xs rounded-lg px-4 py-2">
            Подключить
          </button>
        </div>
      </div>

    </div>
  </div>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Круг с BLE-иконкой пульсирует (fade + scale)
- [ ] Первое устройство `VITRO_A3F2` выделено бордовой рамкой, кнопка активная
- [ ] Два других устройства — приглушены, кнопки неактивные
- [ ] Клик «Подключить» на первой строке → открывает `mobile-home.html`

- [ ] **Step 3: Коммит**

```bash
git add docs_web/wireframes/m1/mobile-ble-pairing.html
git commit -m "Добавил экран BLE Pairing M1"
```

---

## Task 4: mobile-home.html

**Files:**
- Create: `docs_web/wireframes/m1/mobile-home.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Главная · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b] flex items-center justify-center p-8">

  <div class="relative rounded-[3rem] border-[6px] border-[#2a2620] shadow-2xl w-[390px] h-[844px] overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-28 h-7 bg-[#2a2620] rounded-b-2xl z-10"></div>
    <div class="w-full h-full bg-[#0f0e0b] flex flex-col px-7 pt-16 pb-10">

      <div class="mt-6 flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-[#166534] block"></span>
        <span class="font-data text-[#f7f6f1] text-xs">Connected · VITRO_A3F2</span>
      </div>

      <div class="flex-1 flex flex-col items-center justify-center">
        <p class="text-[#7a766d] text-sm mb-3 uppercase tracking-widest">Сердечный ритм</p>
        <div class="flex items-end gap-3">
          <span class="font-data text-[#831843] leading-none" style="font-size: 88px; line-height: 1;">78</span>
          <span class="font-data text-[#831843] text-2xl mb-3">↑</span>
        </div>
        <p class="text-[#7a766d] text-sm mt-2">уд/мин</p>
        <p class="font-data text-[#4a463e] text-xs mt-3">последнее измерение 14:32:07</p>
      </div>

      <div class="mt-auto">
        <button class="w-full bg-[#831843] text-[#f7f6f1] text-sm font-semibold rounded-xl py-4 hover:opacity-90 transition-opacity">
          Синхронизировать
        </button>
        <div class="mt-3 flex items-center gap-2 justify-center">
          <span class="w-1.5 h-1.5 rounded-full bg-[#166534] block"></span>
          <span class="font-data text-[#7a766d] text-xs">последняя синхр. 14:30:00</span>
        </div>
      </div>

    </div>
  </div>

</body>
</html>
```

**Примечание:** `font-size: 88px` задан инлайн — это техническое значение, которое не выражается стандартными классами Tailwind и не является дизайн-стилем.

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Зелёная точка + «Connected · VITRO_A3F2» — JetBrains Mono
- [ ] BPM «78» — крупно, бордовый (`#831843`), JetBrains Mono
- [ ] Стрелка `↑` рядом с цифрой, такой же цвет
- [ ] «уд/мин» под цифрой, вторичный цвет
- [ ] Время замера — JetBrains Mono, приглушённый
- [ ] Кнопка «Синхронизировать» — бордовая, внизу
- [ ] Статус последней синхронизации

- [ ] **Step 3: Коммит**

```bash
git add docs_web/wireframes/m1/mobile-home.html
git commit -m "Добавил главный экран BPM M1"
```

---

## Task 5: dashboard-login.html

**Files:**
- Create: `docs_web/wireframes/m1/dashboard-login.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Login · Neiry Pulse</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b] flex items-center justify-center">

  <div class="w-full max-w-sm px-8">
    <div class="mb-10 text-center">
      <p class="font-brand text-4xl text-[#f7f6f1]">Neiry <span class="text-[#1e3a8a] italic">Pulse</span></p>
      <p class="text-[#7a766d] text-sm mt-2 uppercase tracking-widest">Admin Dashboard</p>
    </div>

    <div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl p-8">
      <h2 class="text-[#f7f6f1] text-xl font-semibold mb-6">Вход для администратора</h2>

      <div class="flex flex-col gap-4">
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Email</label>
          <div class="w-full bg-[#0f0e0b] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            admin@neiry.ru
          </div>
        </div>
        <div>
          <label class="text-[#7a766d] text-xs uppercase tracking-widest mb-2 block">Пароль</label>
          <div class="w-full bg-[#0f0e0b] border border-[#2a2620] rounded-xl px-4 py-3 text-[#4a463e] text-sm">
            ••••••••••••
          </div>
        </div>
      </div>

      <a href="dashboard-users.html"
         class="mt-6 w-full bg-[#1e3a8a] text-[#f7f6f1] text-sm font-semibold rounded-xl py-4 text-center block hover:opacity-90 transition-opacity">
        Войти как администратор
      </a>
    </div>
  </div>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Полноширинная страница, без телефонной рамки
- [ ] Логотип по центру, «Pulse» — синий (`#1e3a8a`), курсивный Fraunces
- [ ] «ADMIN DASHBOARD» — tracking-widest, вторичный цвет
- [ ] Карточка с формой — отдельный bg-[#1a1814]
- [ ] Кнопка синяя — ведёт на `dashboard-users.html`

- [ ] **Step 3: Коммит**

```bash
git add docs_web/wireframes/m1/dashboard-login.html
git commit -m "Добавил экран логина дашборда M1"
```

---

## Task 6: dashboard-users.html

**Files:**
- Create: `docs_web/wireframes/m1/dashboard-users.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Тестировщики · Neiry Pulse Admin</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b]">

  <header class="border-b border-[#2a2620] px-8 py-4 flex items-center justify-between">
    <p class="font-brand text-xl text-[#f7f6f1]">Neiry <span class="text-[#1e3a8a] italic">Pulse</span> <span class="text-[#7a766d] font-sans text-sm font-normal ml-2">Admin</span></p>
    <a href="dashboard-login.html" class="border border-[#2a2620] text-[#7a766d] text-sm rounded-lg px-4 py-2 hover:border-[#7a766d] transition-colors">
      Выйти
    </a>
  </header>

  <main class="px-8 py-8 max-w-5xl mx-auto">
    <div class="flex items-center gap-3 mb-6">
      <h1 class="text-[#f7f6f1] text-2xl font-semibold">Тестировщики</h1>
      <span class="font-data text-[#7a766d] text-sm bg-[#1a1814] border border-[#2a2620] rounded-lg px-3 py-1">4</span>
    </div>

    <div class="bg-[#1a1814] border border-[#2a2620] rounded-2xl overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="border-b border-[#2a2620]">
            <th class="text-left text-[#7a766d] text-xs uppercase tracking-widest px-6 py-4">Имя</th>
            <th class="text-left text-[#7a766d] text-xs uppercase tracking-widest px-6 py-4">Email</th>
            <th class="text-left text-[#7a766d] text-xs uppercase tracking-widest px-6 py-4">Синхр.</th>
            <th class="text-left text-[#7a766d] text-xs uppercase tracking-widest px-6 py-4">BPM</th>
            <th class="text-left text-[#7a766d] text-xs uppercase tracking-widest px-6 py-4">Статус</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-b border-[#2a2620]">
            <td class="px-6 py-4 text-[#f7f6f1] text-sm font-medium">Алексей Морозов</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">a.morozov@neiry.ru</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">14:32:07</td>
            <td class="font-data px-6 py-4 text-[#831843] text-sm font-medium">78</td>
            <td class="px-6 py-4">
              <span class="bg-[#166534] text-[#f7f6f1] text-xs font-semibold rounded-md px-2.5 py-1">Online</span>
            </td>
          </tr>
          <tr class="border-b border-[#2a2620]">
            <td class="px-6 py-4 text-[#f7f6f1] text-sm font-medium">Мария Соколова</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">m.sokolova@neiry.ru</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">14:29:55</td>
            <td class="font-data px-6 py-4 text-[#831843] text-sm font-medium">84</td>
            <td class="px-6 py-4">
              <span class="bg-[#166534] text-[#f7f6f1] text-xs font-semibold rounded-md px-2.5 py-1">Online</span>
            </td>
          </tr>
          <tr class="border-b border-[#2a2620]">
            <td class="px-6 py-4 text-[#f7f6f1] text-sm font-medium">Дмитрий Волков</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">d.volkov@neiry.ru</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">13:58:20</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-sm">—</td>
            <td class="px-6 py-4">
              <span class="bg-[#2a2620] text-[#7a766d] text-xs font-semibold rounded-md px-2.5 py-1">Offline</span>
            </td>
          </tr>
          <tr>
            <td class="px-6 py-4 text-[#f7f6f1] text-sm font-medium">Анна Кузнецова</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">a.kuznetsova@neiry.ru</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-xs">13:41:03</td>
            <td class="font-data px-6 py-4 text-[#7a766d] text-sm">—</td>
            <td class="px-6 py-4">
              <span class="bg-[#2a2620] text-[#7a766d] text-xs font-semibold rounded-md px-2.5 py-1">Offline</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Header: логотип слева, кнопка «Выйти» справа
- [ ] Заголовок «Тестировщики» + счётчик `4` в бейдже
- [ ] Таблица: 4 строки с реалистичными данными
- [ ] Online-бейджи зелёные, Offline — тёмные
- [ ] BPM column — `#831843` для онлайн, прочерк для офлайн
- [ ] Время синхронизации и email — JetBrains Mono

- [ ] **Step 3: Коммит**

```bash
git add docs_web/wireframes/m1/dashboard-users.html
git commit -m "Добавил экран списка пользователей дашборда M1"
```

---

## Task 7: index.html

**Files:**
- Create: `docs_web/wireframes/m1/index.html`

- [ ] **Step 1: Создать файл с полным HTML**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>M1 Tech Demo · Neiry Pulse Wireframes</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Manrope:wght@300;400;500;600;700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Manrope', sans-serif; -webkit-font-smoothing: antialiased; }
  .font-brand { font-family: 'Fraunces', serif; }
  .font-data { font-family: 'JetBrains Mono', monospace; }

  /* Iframe phone preview */
  .phone-preview-wrap {
    width: 148px;
    height: 321px;
    overflow: hidden;
    border-radius: 1.4rem;
    border: 3px solid #2a2620;
    background: #0f0e0b;
    flex-shrink: 0;
  }
  .phone-preview-wrap iframe {
    width: 390px;
    height: 844px;
    border: none;
    transform: scale(0.38);
    transform-origin: top left;
    pointer-events: none;
  }

  /* Dashboard preview */
  .dash-preview-wrap {
    width: 480px;
    height: 270px;
    overflow: hidden;
    border-radius: 0.75rem;
    border: 2px solid #2a2620;
    background: #0f0e0b;
  }
  .dash-preview-wrap iframe {
    width: 1280px;
    height: 720px;
    border: none;
    transform: scale(0.375);
    transform-origin: top left;
    pointer-events: none;
  }
</style>
</head>
<body class="min-h-screen bg-[#0f0e0b]">

  <header class="border-b border-[#2a2620] px-10 py-5">
    <p class="font-brand text-2xl text-[#f7f6f1]">Neiry <span class="text-[#831843] italic">Pulse</span></p>
    <p class="font-data text-[#7a766d] text-xs mt-1 tracking-widest">M1 TECH DEMO · WIREFRAMES · 18 МАЯ 2026</p>
  </header>

  <main class="px-10 py-10">
    <div class="flex gap-16 items-start">

      <!-- Left: Mobile flow -->
      <div class="flex flex-col">
        <div class="flex items-center gap-3 mb-8">
          <span class="font-data text-[#831843] text-xs tracking-widest">ANDROID APP</span>
          <div class="h-px flex-1 bg-[#2a2620] max-w-xs"></div>
        </div>

        <div class="flex flex-col items-center gap-2">

          <!-- Screen 1 -->
          <div class="flex items-center gap-4">
            <div class="flex flex-col items-center gap-2">
              <div class="flex items-center gap-2 self-start">
                <span class="font-data text-[#831843] text-xs">①</span>
                <span class="text-[#7a766d] text-xs">Регистрация</span>
              </div>
              <div class="phone-preview-wrap">
                <iframe src="mobile-registration.html" title="Регистрация"></iframe>
              </div>
              <a href="mobile-registration.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
                открыть полный экран →
              </a>
            </div>
          </div>

          <div class="font-data text-[#2a2620] text-lg">↓</div>

          <!-- Screen 2 -->
          <div class="flex flex-col items-center gap-2">
            <div class="flex items-center gap-2 self-start">
              <span class="font-data text-[#831843] text-xs">②</span>
              <span class="text-[#7a766d] text-xs">Логин</span>
            </div>
            <div class="phone-preview-wrap">
              <iframe src="mobile-login.html" title="Логин"></iframe>
            </div>
            <a href="mobile-login.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
              открыть полный экран →
            </a>
          </div>

          <div class="font-data text-[#2a2620] text-lg">↓</div>

          <!-- Screen 3 -->
          <div class="flex flex-col items-center gap-2">
            <div class="flex items-center gap-2 self-start">
              <span class="font-data text-[#831843] text-xs">③</span>
              <span class="text-[#7a766d] text-xs">BLE Pairing</span>
            </div>
            <div class="phone-preview-wrap">
              <iframe src="mobile-ble-pairing.html" title="BLE Pairing"></iframe>
            </div>
            <a href="mobile-ble-pairing.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
              открыть полный экран →
            </a>
          </div>

          <div class="font-data text-[#2a2620] text-lg">↓</div>

          <!-- Screen 4 -->
          <div class="flex flex-col items-center gap-2">
            <div class="flex items-center gap-2 self-start">
              <span class="font-data text-[#831843] text-xs">④</span>
              <span class="text-[#7a766d] text-xs">Главная (BPM)</span>
            </div>
            <div class="phone-preview-wrap">
              <iframe src="mobile-home.html" title="Главная BPM"></iframe>
            </div>
            <a href="mobile-home.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
              открыть полный экран →
            </a>
          </div>

        </div>
      </div>

      <!-- Divider -->
      <div class="w-px bg-[#2a2620] self-stretch mx-4"></div>

      <!-- Right: Dashboard flow -->
      <div class="flex flex-col flex-1">
        <div class="flex items-center gap-3 mb-8">
          <span class="font-data text-[#1e3a8a] text-xs tracking-widest">WEB DASHBOARD</span>
          <div class="h-px flex-1 bg-[#2a2620]"></div>
        </div>

        <div class="flex flex-col gap-4">

          <!-- Screen 5 -->
          <div class="flex flex-col gap-2">
            <div class="flex items-center gap-2">
              <span class="font-data text-[#1e3a8a] text-xs">⑤</span>
              <span class="text-[#7a766d] text-xs">Логин администратора</span>
            </div>
            <div class="dash-preview-wrap">
              <iframe src="dashboard-login.html" title="Dashboard Login"></iframe>
            </div>
            <a href="dashboard-login.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
              открыть полный экран →
            </a>
          </div>

          <div class="font-data text-[#2a2620] text-lg pl-2">↓</div>

          <!-- Screen 6 -->
          <div class="flex flex-col gap-2">
            <div class="flex items-center gap-2">
              <span class="font-data text-[#1e3a8a] text-xs">⑥</span>
              <span class="text-[#7a766d] text-xs">Список тестировщиков</span>
            </div>
            <div class="dash-preview-wrap">
              <iframe src="dashboard-users.html" title="Dashboard Users"></iframe>
            </div>
            <a href="dashboard-users.html" class="font-data text-[#7a766d] text-xs hover:text-[#f7f6f1] transition-colors">
              открыть полный экран →
            </a>
          </div>

        </div>
      </div>

    </div>
  </main>

</body>
</html>
```

- [ ] **Step 2: Открыть в браузере и проверить**

- [ ] Header: логотип + дата «M1 TECH DEMO · WIREFRAMES · 18 МАЯ 2026»
- [ ] Левая колонка «ANDROID APP» — 4 телефонных превью с нумерацией ①②③④
- [ ] Стрелки ↓ между превью
- [ ] Правая колонка «WEB DASHBOARD» — 2 дашборд-превью с нумерацией ⑤⑥
- [ ] Вертикальный разделитель между колонками
- [ ] Ссылки «открыть полный экран →» под каждым превью
- [ ] Iframes загружаются (может потребоваться Live Server — при открытии через `file://` iframes могут не работать из соображений безопасности браузера)

**Если iframes не загружаются при открытии через `file://`:** открыть через Live Server (VS Code) или `python3 -m http.server 8080` из папки `wireframes/m1/`.

- [ ] **Step 3: Финальный коммит**

```bash
git add docs_web/wireframes/m1/index.html
git commit -m "Добавил index-обзор wireframes M1 Tech Demo"
```

---

## Self-Review

### Покрытие спека
- ✅ mobile-registration.html — логотип, поля, кнопка, ссылка
- ✅ mobile-login.html — логотип, поля, кнопка, ссылка, переход на BLE
- ✅ mobile-ble-pairing.html — scan animation, 3 устройства, подключить
- ✅ mobile-home.html — статус, BPM JetBrains Mono, тренд ↑, синхр.
- ✅ dashboard-login.html — полноширинный, синий accent, переход на users
- ✅ dashboard-users.html — таблица 4 строки, Online/Offline badge
- ✅ index.html — два флоу рядом, нумерация, ссылки

### Типографика
- ✅ Fraunces → логотипы
- ✅ Manrope → основной текст
- ✅ JetBrains Mono → BPM, время, device ID, email в таблице

### Палитра
- ✅ Все цвета соответствуют спеку из CLAUDE.md
- ✅ Online = `#166534`, Offline = `#2a2620` bg
