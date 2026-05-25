# M2 UI Restyle — Session State (2026-05-26, Brainstorm Drilldown в работе)

> **Назначение:** handoff после auto-compact. Читать первым при возобновлении работы по M2 UI Restyle.
>
> **Если контекст потерян:** прочти этот файл целиком → `memory/MEMORY.md` + ключевые memory-файлы → план M2 UI Restyle → продолжай с раздела «⏭ Очередь работы».

---

## 🚨 СТАТУС СЕЙЧАС — Brainstorming спецификации kiosk-drilldown.html

**Где мы:** Запущен скилл `superpowers:brainstorming` для проработки детального ТЗ для UX/UI агента под Задачу 5 (kiosk-drilldown.html). Brainstorm активен — идём по вопросам с PM один-за-одним.

**Round 2 Kiosk v2 закрыт ✅** — commit `1226e0b` (pushed). Задача 4 принята PM.

**Этап 3 в работе:** brainstorm спецификации для Задачи 5. После brainstorm → spec doc → writing-plans → subagent-driven-development → готовый kiosk-drilldown.html.

---

## ✅ Финальные решения PM по Задаче 5 (зафиксированы, не менять)

### Общие параметры экрана
| # | Параметр | Решение |
|---|---|---|
| 1 | Артефакт | `docs_web/wireframes/m2/kiosk-drilldown.html` (новый файл) |
| 2 | Размер | **1920×1080** тёмная тема (как плазма, единый язык со стендом) |
| 3 | Стек | HTML + Tailwind CDN + shadcn semantic CSS-переменные + inline SVG + vanilla JS (как kiosk-v2) |
| 4 | Шрифты | Space Grotesk (UI) + Onest 700 (hero) + Geist Mono (data) |
| 5 | Палитра | shadcn zinc/slate + wine `#831843` + светофор HSL (success/warning/destructive) |
| 6 | URL-параметры | `?id=kostya|alexey|guest&session=active` (различает имена + плазма не сбрасывается) |
| 7 | Top-bar таймер | Живой от клика CTA «Пройти тест» (00:00 → ...) |
| 8 | Возврат «← К стене» | `<a href="./kiosk-v2.html?session=active">` |

### Bayevsky test
| # | Параметр | Решение |
|---|---|---|
| 9 | CTA-текст | **«Пройти тест»** |
| 10 | Вход в phase-1 | Только CTA (dev-bar — только для прыжков между фазами в показе) |
| 11 | Bayevsky overlay | **Modal overlay поверх drilldown**, drilldown виден сквозь (blur 12px + dim 0.7) |
| 12 | Размер модалки | Центральная **960×680**, видны куски drilldown с blur по бокам |
| 13 | Завершение фазы | Таймер «✓ 00:00» + caption «Фаза завершена · оператор → следующая» (auto-advance НЕТ, только dev-bar) |
| 14 | Отмена теста | Маленькая ✕ в правом верхнем углу модалки → возврат в drilldown |
| 15 | Phase-1 «Покой 3 мин» | Большой таймер + инструкция «Стой неподвижно, дыши спокойно» + статичная иконка 🧘 |
| 16 | Phase-2 «Stroop 1 мин» | Текст «Назови цвет, а не слово» + одна плашка-пример (слово «КРАСНЫЙ» написано синим) |
| 17 | Phase-3 **«Быстрая ходьба 1 мин»** (переименовано из «Дорожка») | Эмодзи 🏃 + инструкция «быстро пройдитесь в течение 1 минуты чтобы поднять пульс» |
| 18 | Result-модалка | 3 горизонтальные карточки (Покой / Stroop / Ходьба) + вердикт-итог **снизу** + QR в TG-бота **сверху как hero-CTA** |

### Шкала ИН Баевского (4 зоны + 4 вердикта)
| Зона | ИН | Цвет |
|---|---|---|
| Истощение (ваготония) | <30 | 🔴 destructive |
| Норма | 30-150 | 🟢 success |
| Нагрузка | 150-500 | 🟡 warning |
| Стресс | >500 | 🔴 destructive |

| Вердикт | Логика |
|---|---|
| Реактивность нормальная | Покой 🟢, Stroop/Ходьба в 🟡 |
| Каскадная реакция | Stroop или Ходьба прыгают в 🔴 >500 |
| Низкая адаптивность | Stroop/Ходьба не отличаются от покоя |
| Хронический стресс | Уже в покое 🔴 (>300 или <30) |

### Live-метрики (что в Live-блоке слева)
| # | Виджет | Поведение |
|---|---|---|
| 19 | BPM + ECG | Параметрический P-QRS-T (как в kiosk-v2), heart-pulse 0.75s |
| 20 | NSI («стресс») | Круг с числом + caption «Норма/Повышен/Высокий» (зоны 0-39/40-59/60-100) |
| 21 | IMU | Motion-индикатор: «покой / лёгкая активность / активность» (по акселерометру) |
| 22 | HRV-RMSSD | Показываем только если в окне ≥60 валидных R-R после двухступенчатого фильтра, иначе «— накапливаем» |
| 23 | В фазах Bayevsky | Live (BPM/NSI/IMU/HRV) видны сквозь модалку (по выбранному backdrop blur+dim) |

### 4 виджета правой колонки «Предиктивные метрики» (2×2)
| Виджет | Форма | Костя | Алексей | Гость | Пороги | Дисклеймер |
|---|---|---|---|---|---|---|
| **Индекс восстановления** | Круг + число | **82** 🟢 | **67** 🟡 | **54** 🟡 | 0-50/50-70/70-100 | «Оценочная метрика · требует калибровки за 7+ дней» |
| **Качество сна** | Mini-ring + «N/5 ★» | 7ч 14м / 4★ | 6ч 02м / 3★ | 5ч 40м / 2★ | — | «Оценочная метрика · требует данных» |
| **Риск выгорания** | Круг-донат + % | **18%** 🟢 | **42%** 🟡 | **«нет данных»** | 0-30/30-60/60-100 | «Оценочная метрика · требует данных за 14+ дней» |
| **Риск уснуть** | Круг-донат + % | **12%** 🟢 | **35%** 🟡 | **«нет данных»** | 0-25/25-55/55-100 | «Оценочная метрика · требует данных за 14+ дней» |

### Mock-значения ИН по фазам (для result-модалки)
| ID | Покой | Stroop | Ходьба | Вердикт |
|---|---|---|---|---|
| Костя | 64 | 145 | 230 | 🟢 Реактивность нормальная |
| Алексей | 82 | 310 | 540 | 🟡 Каскадная реакция |
| Гость | 218 | 245 | 285 | 🔴 Хронический стресс |

---

## ❓ Оставшиеся вопросы brainstorm'a (план до выхода в spec)

| # | Тема | Что нужно решить |
|---|---|---|
| **10** | **Persistent блок «Результаты Баевского» в drilldown** | Что в нём до теста / во время фаз / после теста. **← сейчас на этом вопросе** |
| 11 | **STOP SESSION** | Отдельный 6-й state или модалка? Что показывает (QR для TG-бота?). Как после STOP вернуться к стене (kiosk-v2) |
| 12 | **Top-bar состав** | Формат ID сессии (#A-X4F2 vs другое), что в правом верхнем углу (тайм + ID + имя + статус сессии) |
| 13 | **Header слева «NEIRY PULSE»** | Подтвердить как в скетче или использовать стандартный header из kiosk-v2 (без отдельного блока) |
| 14 | **Соотношение колонок Live/Predictive** | 50/50 vs 60/40 vs 40/60 — задаёт всю плотность layout |
| 15 | **Расположение CTA «Пройти тест» и кнопки СТОП в drilldown** | На скетче PM — внизу слева под Live-блоком. Подтвердить или вынести CTA в персистентный блок «Результаты Баевского» (если он пустой → CTA внутри него) |
| 16 | **Dev-bar состав** | 5 кнопок states (drilldown / phase-1 / phase-2 / phase-3 / result) + что-то ещё (например toggle для CTA-stub) |
| 17 | **idle-state plazma (нет активной сессии)** | Что показывать на drilldown если открыли по `?id=...` без `&session=active`? Empty-state «Нет активной сессии» или редирект на kiosk-v2 |

После закрытия этих ~8 вопросов → пишу spec → self-review → отдаю на review PM → writing-plans → subagent-driven-development.

---

## ✅ Что СДЕЛАНО в Round 2 Kiosk v2 (commit 1226e0b — pushed)

### A2 — Калибровка 12 сек
- HTML карточки гостя: `.when-calibrating` со спиннером, текст «Калибровка XX сек…» (t-h2 + nowrap), hidden hint
- dev-bar: «Calibrate Guest» (disabled когда не active-3) + «Slow Calibration» toggle
- JS: IIFE `initCalibration` — счётчик 12→0 (или 16→0 при slow)
- CSS: `.when-calibrating`, `.calib-spinner`, `[data-card-state=calibrating]`

### A3 — Hover-glow (переделано из drill-hint)
- CSS: `.card-anchor[data-href]:hover/focus-visible` — wine border + bg `--primary/0.04` + 3-слойный box-shadow. В `idle` — отключён
- HTML: все 3 article получили `data-href="./kiosk-drilldown.html?id=..."`
- JS: click + `role="link"` + `tabindex="0"` + Enter/Space

### A5 — BLE-индикатор
- CSS: `.ble-status-dot` реагирует на `[data-ble]` (connected зелёный live-blink, lost жёлтый, disconnected серый opacity 0.5)
- HTML: строка под BPM переписана на data-ble-driven, текст меняется (Подключен / Нет связи / Отключено)
- `.ble-overlay` со спиннером и «Переподключаемся…» при disconnected
- dev-bar: кнопка cycle-ble
- JS: IIFE `initBleCycle`

### A6 — Чистка футера
- dev-bar сдвинут на `left: 62%` (освобождает пространство под легенду)

---

## 📊 Статус задач плана M2 UI Restyle

| # | Задача | Статус | SHA |
|---|---|---|---|
| 1 | Калибровка эстетики | ✅ принято | — |
| 2 | BRIEF.md UX/UI | ✅ принято | bf1bf9e |
| 3 | UI Kit | ✅ принято | bf1bf9e |
| 4 | Kiosk v2 | ✅ принято (Round 2 закрыт) | **1226e0b** |
| 5 | Drill-down (3 фазы Bayevsky) | 🟡 **Brainstorm в работе** (9/~17 вопросов закрыто) | — |
| 6 | Dashboard корпоратов | ⚪ pending | — |
| 7 | Mobile pairing | ⚪ pending | — |
| 8 | Финальная индексация | ⚪ pending | — |

---

## 🔗 GitPages URLs

- UI Kit: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/ui-kit.html
- Kiosk v2: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/kiosk-v2.html
- Exhibition Flow: https://s0101110110.github.io/neiry-pulse-m1-wireframes/docs_web/wireframes/m2/exhibition-flow.html

---

## 🛡 Активные правила

1. **PM acceptance gate** — задача НЕ закрывается без явного «принято».
2. **Согласование каждой правки** — действует с Round 2 Kiosk v2 и продолжает действовать на drilldown.
3. **HTML-first workflow** — HTML+Tailwind CDN → потом React.
4. **NDA-safe UI** — НЕТ: VITRO, VANTA, VIGOR, M1/M2/M3, Сбер, Райффайзенбанк, Газпром, Илья. ДА: «Neiry.Pulse #N», «Neiry Stress Index».
5. **Имена анкеров:** Костя + Алексей. НЕ Илья.
6. **Технические:** HTML5 + Tailwind CDN + inline SVG. Хардкод hex только `#831843`.
7. **Visual companion отключён** — текстом, lo-fi только по запросу PM.

---

## 📁 Ключевые memory-файлы

- `memory/MEMORY.md` — индекс
- `memory/project_neiry_stress_index.md` — NSI + Баевский + двухступенчатый R-R фильтр
- `memory/project_neiry_ui_aesthetic.md` — палитра/шрифты
- `memory/project_neiry_ui_stack.md` — стек
- `memory/feedback_neiry_pm_acceptance_gate.md` — правило приёмки
- `memory/feedback_neiry_workflow_html_first.md` — HTML-first
- `memory/project_neiry_kiosk_design_system.md` — type-scale, токены, layout-правила

---

## 🚨 Алгоритм восстановления после auto-compact

1. Прочитать **этот файл** целиком.
2. Прочитать `memory/MEMORY.md` + ключевые memory-файлы.
3. `git status` + `git log --oneline -5` — проверить что `1226e0b` (Round 2) + handoff-коммит на месте.
4. Если PM ждёт продолжения brainstorm'a → продолжить с вопроса **#10 (Persistent блок Результаты Баевского)**. Все 9 закрытых вопросов зафиксированы в этом файле, перезадавать НЕ нужно.
5. Если PM перешёл к новой теме → следовать его запросу.
6. **Сказать PM:**
   > «Контекст восстановлен. Brainstorm Задачи 5: 9 из ~17 вопросов закрыто. Следующий — Вопрос 10: Persistent блок «Результаты Баевского» в правой колонке drilldown (что в нём до/во время/после теста). Продолжаем?»

---

## 💬 Последняя реплика PM

> «защити нас от авто-компакта, обнови хендов и список задач, которые перед нами ещё стоят в рамках brainstorm а.»

(Перед этим: ответил «9.1 b / 9.2 внизу как итог / 9.3 подтверждаю / 9.4 a» — закрыл вопрос про result-модалку.)

---

## 🎯 Что отвечать PM сразу после восстановления

> «Handoff обновлён и запушен. Продолжаем brainstorm с Вопроса 10 (Persistent блок «Результаты Баевского»). Готов задавать?»
