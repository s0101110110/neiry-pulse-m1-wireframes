---
title: "Метрики HRV и Steps — спецификация M2"
---

# Метрики HRV и Steps — спецификация M2

## HRV (Heart Rate Variability)

### Источник данных
- Veepoo SDK call: `readRRIntervalByDay(date)` → массив R-R интервалов (мс)
- Backend агрегация: `POST /v1/metrics/hrv/calculate`
- Окно расчёта: 3-5 минут (для slow Баевский ИН) или весь день (для daily summary)

### Формулы
- **RMSSD** (мс) = √(Σ(R-R[i+1] − R-R[i])² / (N−1))
  - Norm range: 20-100 мс (взрослый, в покое)
  - Используем: основной показатель «daily HRV»
- **SDNN** (мс) = √(Σ(R-R[i] − mean)² / N)
  - Norm range: 30-150 мс
  - Используем: контекст для RMSSD
- **Баевский ИН** (Stress Index Slow) = AMo / (2·Mo·MxDMn)
  - Используется в TG-отчёте после сессии (не в live)
  - Фильтр R-R-артефактов: 5% перцентильный

### Пороги (для UI-визуализации, clinical-семантика)
- Норма: RMSSD > 50 мс
- Сниженная: RMSSD 30-50 мс
- Низкая: RMSSD < 30 мс (риск перетренированности / стресса)

### Визуализация
- **Dashboard (`dashboard-corporate.html`)**: KPI card «HRV» с числом RMSSD в мс + sparkline 7 дней
- **Mobile (`mobile-main.html`)**: блок «Сегодня HRV» с числом + цветом-индикатором (точка 8×8)
- **TG-отчёт**: Баевский ИН (число) + вердикт текстом

---

## Steps (шаги)

### Источник данных
- Veepoo SDK call: `readDailyStepByDay(date)` → integer (шаги за день)
- Backend агрегация: `GET /v1/metrics/steps/daily?user_id=X&from=YYYY-MM-DD`

### Формула
- Сырые данные SDK: integer шагов за день
- Активные минуты: расчёт на backend через cadence (если cadence > 100 шагов/мин в 1-мин окне → активная минута)

### Пороги
- Daily target: 10 000 шагов (универсально, без персонализации в M2)
- Active minutes target: 30 мин/день (WHO)

### Визуализация
- **Dashboard**: KPI card «Шаги сегодня» = «3 200 / 10 000»; bar progress
- **Mobile**: круговой прогресс с числом в центре

---

## Зависимости
- Расчёты HRV — на backend (slow, окно 3-5 мин); SDK даёт только R-R массив
- Steps — на SDK (fast), backend только хранит и агрегирует
- Все эндпоинты в M2-скоупе (см. `milestones/m2.md` в knowledge-base)
