---
title: "Pulse · Техническая записка · v1"
---

# Pulse · Техническая записка по мобильному приложению и инфраструктуре

**Версия:** v1
**Дата:** 2026-06-22

---

## 1. Назначение приложения

Pulse — мобильное приложение для носимого браслета (модели VITRO, VANTA, VIGOR). Приложение читает с браслета сырые биометрические данные по Bluetooth LE (R-R интервалы, частота пульса, SpO2, активность, фазы сна, события падения), рассчитывает на бэкенде персональную базовую норму HRV пользователя («личная норма») за 36–48 часов после первого подключения и далее выдаёт пользователю простые читаемые инсайты, рекомендации и графики. Дополнительно приложение поддерживает режим тренировки с GPS-треком и пульсовыми зонами, фиксирует ночной сон и позволяет делиться данными с близкими через QR-приглашение.

Платформа: iOS + Android, единая кодовая база на Flutter.

---

## 2. Архитектура верхнеуровневая

```
┌─────────────────┐         BLE          ┌──────────────────┐
│  Браслет        │  ◄──────────────►   │  Mobile App      │
│  (VITRO/VANTA/  │   R-R, HR, IMU,      │  Pulse (Flutter) │
│   VIGOR)        │   SpO2, шаги, сон    │                  │
│   Veepoo SDK    │                      │                  │
└─────────────────┘                      └──────┬───────────┘
                                                │ HTTPS REST
                                                ▼
                                         ┌──────────────────┐
                                         │ Backend Pulse    │
                                         │ (Python+Celery+  │
                                         │  Redis+Sentry)   │
                                         └──────┬───────────┘
                                                │
                ┌───────────────────┬───────────┼──────────────┐
                ▼                   ▼           ▼              ▼
        ┌──────────────┐   ┌──────────────┐  ┌─────────┐  ┌──────────┐
        │ PostgreSQL   │   │ Redis        │  │ Firebase│  │ Object   │
        │ (Yandex      │   │ (queues,     │  │ FCM     │  │ Storage  │
        │  Cloud)      │   │  cache)      │  │ (push)  │  │ (YC S3)  │
        └──────────────┘   └──────────────┘  └─────────┘  └──────────┘
```

Браслет — источник данных. Mobile-приложение — клиент с локальным буфером (для оффлайна) и UI. Бэкенд — расчёты, хранение, баланс, шеринг, push, аналитика.

---

## 3. Стек технологий

| Слой | Технология | Назначение |
|---|---|---|
| Mobile | Flutter (Dart) | Кроссплатформенный клиент iOS + Android |
| Mobile нативные мостики | iOS (Swift), Android (Kotlin) | Bridge для Veepoo SDK (BLE-протокол браслета) |
| Backend | Python | REST API |
| Async tasks | Celery + Redis | Calibration jobs, push triggers, агрегации |
| Cache / message broker | Redis | Сессии, кеш, очереди для Celery |
| Database | PostgreSQL (Yandex Cloud Managed) | Основное хранилище |
| Object storage | Yandex Cloud Object Storage (S3-совместимое) | Sleep raw data, экспорты, snapshots для шеринга |
| Push notifications | Firebase Cloud Messaging (FCM) | iOS + Android |
| Crash reporting | Sentry | Mobile + backend |
| Hosting / Infra | Yandex Cloud | Compute, managed Postgres, managed Redis, S3, registry |

---

## 4. Состав экранов приложения

25 экранов мобильного приложения разделены на две очереди.

### Очередь 1 — релиз 23.06.2026 (для прохождения review в сторе)

19 экранов, минимально достаточный набор для пользовательского пути от первого запуска до получения первой личной нормы HRV.

**Онбординг (8 экранов):**
1. Splash welcome
2. Permission Bluetooth
3. Bracelet scan
4. Bracelet pairing
5. Permission Notifications
6. Calibrating (прогресс 36–48ч сбора)
7. Baseline explainer (модалка «Что такое личная норма?»)
8. Home first-run empty

**Аутентификация (3 экрана):**

9. Регистрация (email + пароль + согласие 152-ФЗ)
10. Вход
11. Сброс пароля

**Главный экран (1 экран):**

12. Home loaded

**HRV-флоу (4 экрана):**

13. Baseline ready notification (личная норма готова)
14. First HRV measurement reveal (первое значение)
15. HRV detail view (число + 30-дневный график + дельты)
16. HRV explainer (модалка «Что такое HRV?»)

**Настройки (6 экранов):**

17. Settings entry
18. Profile edit
19. Bluetooth pairing detail
20. Notifications detail
21. Privacy
22. Калибровка браслета (re-trigger baseline)

### Очередь 2 — релиз 30.06.2026

Шесть экранов и набор edge-states.

23. Тренировка — старт (выбор типа активности)
24. Тренировка — активная (HR + темп + GPS + пульсовые зоны)
25. Сессия — детализация (post-workout summary)
26. История сессий
27. Sleep detail
28. Health Sharing main (QR-приглашение)
29. Health Sharing — экран получателя (дашборд по нескольким пользователям)
30. Onboarding · Fall detection (consent + объяснение сценария)

**Edge states / corner cases** (накладываются как modal / banner на основной флоу):

- BT-disconnect banner, Low battery
- Permission denied: Camera / Location
- Training: STOP confirm, Auto-pause, GPS lost
- End-of-session summary, Bracelet disconnect mid-session
- History: empty / future month / multiple sessions
- Health Sharing: scan failed, role onboarding

Дизайн всех экранов выполнен в Figma. Mobile-разработка использует Figma как source of truth для визуала.

---

## 5. BLE-протокол с браслетом

### 5.1 Используемые технологии

- Veepoo SDK для подключения к браслету через BLE
- iOS bridge на Swift (для Flutter)
- Android — нативный Veepoo SDK через MethodChannel

### 5.2 Каналы передачи

| Канал | Пропускная способность | Содержание |
|---|---|---|
| Основной BLE-канал | 1 параметр в секунду | R-R интервалы (real-time для HRV) или HR (real-time для тренировки) — взаимоисключающе |
| Накопительный канал | Пакетно при синхронизации | SpO2, шаги, фазы сна, частота дыхания |
| Сервисный канал | По требованию | Модель устройства, firmware version, battery level, paired status |

Известное ограничение: одновременно по основному каналу можно получать только один поток. Это влияет на режим тренировки:

- В режиме обычного мониторинга — R-R для HRV-расчёта
- В режиме активной тренировки — переключение на HR-realtime, R-R пишется в накопительный буфер

### 5.3 Работа с данными на mobile

- Парсинг сырых пакетов через Veepoo SDK
- Буферизация в локальной БД (SQLite) для оффлайн-режима
- Синхронизация в бэкенд пакетами (раз в N минут, при появлении сети, при критических событиях, например fall detection)
- Кеш последних значений для real-time UI

### 5.4 Pairing flow

1. App сканирует BLE-устройства с фильтром по сервису Veepoo
2. Пользователь выбирает свой браслет из списка (имя + MAC + RSSI)
3. App инициирует pairing через SDK
4. После успеха — сохранение `bracelet_id` + `mac_address` в локальной БД, отправка в бэкенд `POST /devices/pair`
5. При повторном запуске — auto-reconnect к последнему paired устройству

### 5.5 Открытые вопросы по BLE / SDK

- Алгоритмы очистки PPG-сигнала от артефактов через IMU — встроены в Veepoo SDK или реализуются на бэкенде самостоятельно
- Структура сырых R-R интервалов в выгрузке (вопрос по формату файла отправлен поставщику)
- Происхождение Stress Index в выгрузке SDK
- Размер окна агрегации активности (шаги приходят за 7 дней без временных меток — нужна разметка по часам)
- Fall detection на разных моделях (требуется 9-осевой IMU или работает на базовом)

---

## 6. Бэкенд

> Раздел готовится в первую очередь для команды инфраструктуры, чтобы было понятно, какие сервисы поднимать. Содержит черновик API и пометки, которые уточняются разработчиком mobile по мере реализации.

### 6.1 Endpoints API

**Аутентификация:**
- `POST /auth/signup` — email, password, 152-ФЗ consent → user_id + JWT (access + refresh)
- `POST /auth/login` — email, password → JWT
- `POST /auth/refresh` — refresh_token → новая пара JWT
- `POST /auth/reset-request` — email → отправка ссылки на mail
- `POST /auth/reset-confirm` — token + new_password
- `POST /auth/logout` — invalidate token

**Профиль:**
- `GET /me`
- `PATCH /me` — обновление ФИО, DOB, пол, рост, вес, цели
- `DELETE /me` — полное удаление аккаунта (152-ФЗ)

**Устройства (браслеты):**
- `POST /devices/pair` — bracelet_id, mac, model → привязка к user_id
- `GET /devices` — список paired устройств
- `DELETE /devices/{id}` — отвязать
- `POST /devices/{id}/firmware` — start firmware update (опц.)

**Ingestion данных с браслета:**
- `POST /ingest/rr` — batch R-R интервалов (timestamp + interval_ms[])
- `POST /ingest/hr` — heart rate sample
- `POST /ingest/spo2`
- `POST /ingest/activity` — шаги, accelerometer summary
- `POST /ingest/sleep` — фазы сна за ночь
- `POST /ingest/fall-event` — IMU fall detection (immediate, не batched)

**Baseline / HRV:**
- `GET /metrics/baseline` — статус калибровки (calibrating / ready) + личная норма
- `POST /metrics/baseline/reset` — re-trigger калибровки (новый 36-48ч сбор)
- `GET /metrics/hrv?period=day|week|month` — числа + дельты + recommendation_text + chart_series

**Тренировки:**
- `POST /sessions/start` — type (run/walk/bike/other) → session_id
- `POST /sessions/{id}/end` — finalize
- `GET /sessions` — история (paginated)
- `GET /sessions/{id}` — детали

**Health Sharing:**
- `POST /sharing/invite` — генерация QR / ссылки
- `POST /sharing/accept` — accept QR
- `GET /sharing/receivers` — кому делюсь
- `GET /sharing/sharers` — кто делится мне
- `DELETE /sharing/{id}` — отзыв доступа

**Push tokens:**
- `POST /push/register` — fcm_token + platform
- `DELETE /push/token`

### 6.2 Сервисы и контейнеры

_(заполняется разработчиком mobile/backend)_

- Используемый веб-фреймворк (FastAPI / Django REST)
- Версии Python, Celery
- Docker registry
- Перечень переменных окружения для запуска (без секретов)
- Health-check endpoints

### 6.3 Текущий статус инфраструктуры

_(заполняется разработчиком mobile/backend; раздел нужен команде инфраструктуры для понимания, что развёрнуто и что разворачивать)_

- PostgreSQL: версия, размер инстанса, бэкапы
- Redis: размер памяти, конфигурация
- Firebase: статус создания проекта, владелец, service account
- Sentry: статус подключения mobile и backend
- Object Storage: bucket, регион
- Domain: rDNS-провайдер, SSL-провайдер

### 6.4 Задачи для команды инфраструктуры

_(уточняется разработчиком backend; здесь — целевой список того, что должно быть выполнено стороной инфраструктуры)_

- Подготовка production-окружения в Yandex Cloud (VPC, compute)
- Managed PostgreSQL и Managed Redis с целевыми конфигурациями
- CI/CD pipeline для Flutter-билдов и Python-сервиса (см. раздел 9)
- SSL-сертификаты для домена
- Базовый мониторинг (метрики + логи)
- Хранение секретов (Vault / Yandex Secret Manager)
- Распределение прав доступа в проекте Yandex Cloud

---

## 7. Модели данных PostgreSQL (черновик)

```sql
-- Пользователи
users (
  id UUID PK,
  email VARCHAR UNIQUE,
  password_hash VARCHAR,
  full_name VARCHAR,
  dob DATE,
  gender VARCHAR(10),
  height_cm INT,
  weight_kg INT,
  goal VARCHAR,
  consent_152fz_at TIMESTAMP NOT NULL,
  created_at, updated_at, deleted_at
)

-- Браслеты
devices (
  id UUID PK,
  user_id UUID FK -> users,
  model VARCHAR (VITRO/VANTA/VIGOR),
  mac_address VARCHAR UNIQUE,
  firmware_version VARCHAR,
  paired_at TIMESTAMP,
  last_seen_at TIMESTAMP,
  battery_level INT
)

-- Сырые R-R интервалы (партиционирование по дням)
rr_intervals (
  id BIGSERIAL PK,
  device_id UUID FK,
  timestamp TIMESTAMP,
  interval_ms INT,
  imu_quality_score FLOAT  -- для будущей очистки артефактов через IMU
)

-- Heart rate samples
hr_samples (
  id BIGSERIAL PK,
  device_id UUID FK,
  timestamp TIMESTAMP,
  bpm INT,
  source ENUM (realtime / accumulated)
)

-- SpO2 / Активность / IMU
spo2_samples (...)
activity_samples (
  id BIGSERIAL PK,
  device_id UUID,
  timestamp_start, timestamp_end,
  steps INT,
  imu_avg FLOAT
)

-- Сон
sleep_records (
  id UUID PK,
  user_id UUID FK,
  night_start, night_end,
  total_minutes INT,
  rem_minutes, deep_minutes, light_minutes, awake_minutes,
  hrv_avg INT,
  hr_resting INT
)

-- Fall events
fall_events (
  id UUID PK,
  device_id UUID FK,
  timestamp TIMESTAMP,
  imu_signature JSONB,
  user_confirmed BOOLEAN,
  notified_at TIMESTAMP
)

-- Тренировочные сессии
training_sessions (
  id UUID PK,
  user_id UUID FK,
  type ENUM (run/walk/bike/other),
  started_at, ended_at,
  duration_sec INT,
  distance_m INT,
  hr_avg, hr_max,
  calories INT,
  gps_polyline TEXT,
  zones_distribution JSONB
)

-- Baseline calibration
baseline_calibrations (
  id UUID PK,
  user_id UUID FK,
  device_id UUID FK,
  started_at TIMESTAMP,
  completed_at TIMESTAMP NULL,
  status ENUM (in_progress/ready/reset),
  hrv_personal_norm INT NULL,
  hr_resting_norm INT NULL
)

-- HRV computed (агрегаты, кешируются)
hrv_daily (
  user_id UUID,
  date DATE,
  hrv_day INT,
  hrv_delta_day_pct FLOAT,
  confidence FLOAT,
  computed_at TIMESTAMP,
  PRIMARY KEY (user_id, date)
)

-- Health Sharing
sharing_links (
  id UUID PK,
  sharer_id UUID FK -> users,
  receiver_id UUID FK -> users NULL,
  invitation_token VARCHAR UNIQUE,
  status ENUM (pending/accepted/revoked),
  created_at, accepted_at
)

-- Push tokens
push_tokens (
  id UUID PK,
  user_id UUID FK,
  fcm_token VARCHAR,
  platform ENUM (ios/android),
  last_used_at TIMESTAMP
)
```

**Партиционирование:** `rr_intervals`, `hr_samples`, `activity_samples` — по дню или неделе.

**TTL:** сырые данные хранятся 90 дней, агрегаты `hrv_daily` бессрочно.

**Удаление аккаунта:** soft-delete `users.deleted_at` + Celery-job окончательного удаления связанных данных через 30 дней (требование 152-ФЗ).

---

## 8. Сессионные пайплайны

### 8.1 Baseline calibration

**Цель:** за 36–48 часов после первого подключения браслета собрать достаточный объём R-R интервалов и рассчитать персональную HRV-норму.

**Phase 1 (первичная калибровка при онбординге):**

1. После pairing бэкенд создаёт запись `baseline_calibrations` со статусом `in_progress`
2. Mobile отправляет ingestion R-R intervals по мере накопления
3. Celery-worker раз в N минут проверяет количество и качество накопленных данных
4. При достижении порога (по умолчанию ≥36ч непрерывной записи, ≥6ч из них в покое) — рассчитывает `hrv_personal_norm` и `hr_resting_norm`, статус становится `ready`
5. Триггерится push «Личная норма готова» через FCM
6. На mobile открывается экран Baseline ready notification

**Phase 2 (re-trigger из настроек):**

- При вызове `POST /metrics/baseline/reset`:
  - Старая запись `status=reset`
  - Новая запись `status=in_progress`
  - Mobile показывает экран «Калибровка идёт» (повторяется флоу онбординга)

### 8.2 Push notifications через FCM

| Тип | Триггер | Когда |
|---|---|---|
| `baseline_ready` | Celery после расчёта baseline | После 36–48ч калибровки |
| `daily_hrv_insight` | Celery cron-job 09:00 локального времени | Ежедневно после первой утренней меры |
| `training_reminder` | Опционально | Если в Settings включён reminder |
| `fall_alert` | Бэкенд получил `fall-event` | Immediate, на устройства receivers через Health Sharing |
| `low_battery` | Бэкенд получил battery < 15% | Раз в день максимум |

Учитываются настройки Quiet hours пользователя.

### 8.3 Fall detection alert

1. Mobile получает событие fall от браслета (через IMU)
2. POST `/ingest/fall-event` immediate, не batched
3. Бэкенд проверяет наличие Health Sharing receivers у пользователя
4. Если есть — отправляет push на устройства receivers через FCM
5. Receivers получают push, могут открыть app и видеть последние показатели пользователя

### 8.4 HRV-расчёт

**Окно:** 5-минутные блоки непрерывной записи. `hrv_day` = агрегат всех 5-мин окон за сутки.

**Артефакты, двухступенчатый фильтр:**

1. Медианный 20% — отбрасывание выбросов в 5-мин окне
2. Перцентильный 5/95% — обрезка хвостов распределения

**Формула HRV:** RMSSD по умолчанию (финальный выбор между RMSSD / SDNN / pNN50 уточняется).

**Контракт `GET /metrics/hrv`:**

| Поле | Тип | Пример |
|---|---|---|
| `hrv_day` | int (ms) | 47 |
| `hrv_delta_day_pct` | float | +12.5 |
| `hrv_week_avg` | int | 45 |
| `hrv_delta_week_pct` | float | +5.2 |
| `hrv_month_avg` | int | 43 |
| `hrv_month_series` | array[30] | [...] |
| `recommendation_text` | string ≤140 chars | «+17% HRV за 3 дня — вы в форме» |
| `recommendation_type` | enum | positive / neutral / alert |
| `confidence` | float 0..1 | 0.85 |

---

## 9. CI/CD pipeline

### 9.1 Mobile

- Билды Flutter — артефакты IPA (iOS) и AAB (Android)
- Подписи: iOS provisioning profiles от account holder для US-стора, Android keystore
- Submit в стор: через App Store Connect и Play Console
- TestFlight и Google Play Internal Track — для пилотных пользователей

_(заполняется разработчиком mobile/backend):_

- Платформа CI (GitHub Actions / GitLab CI / другое)
- Хранение signing assets
- Владелец App Store Connect / Play Console
- TestFlight invitation flow

### 9.2 Backend

- Docker images → Yandex Container Registry
- Deploy в Yandex Cloud (Compute / Managed Kubernetes / Serverless Containers — на выбор)
- Migrations PostgreSQL — Alembic или Django migrations
- Rollback стратегия

### 9.3 Окружения

- `dev` — для разработки
- `staging` — для пилотных пользователей (опц.)
- `prod`

_(итоговый список окружений уточняется)_

---

## 10. Безопасность и 152-ФЗ

### 10.1 Хранение данных

- Все health-данные хранятся на серверах в РФ (Yandex Cloud, регион Москва или СПб)
- Шифрование at-rest для PostgreSQL (поддерживается managed YC)
- TLS 1.3 для всех соединений
- JWT через HTTPS only, ротация refresh-token

### 10.2 Согласия

- При регистрации — checkbox 152-ФЗ + ссылка на политику обработки персональных данных
- При первом подключении браслета — отдельный consent на сбор health-метрик
- Хронические заболевания (опросник на дальнейших итерациях) — относятся к чувствительным категориям персональных данных, требуют юридической проверки

### 10.3 Удаление аккаунта

- `DELETE /me` → soft-delete → Celery-job окончательного удаления через 30 дней
- Health Sharing связи аннулируются immediate
- Push tokens revoke immediate

### 10.4 Audit log

- Лог операций с health-данными (для запросов compliance)
- Хранение лога 6 месяцев

---

## 11. Аналитика и crash reporting

### 11.1 Sentry

- Mobile app — Flutter Sentry SDK (iOS + Android)
- Backend — Sentry Python SDK
- Sampling rate: 100% errors, 10% performance
- PII фильтры: email, имена, health-данные не отправляются в crashes

### 11.2 Product analytics (на дальнейших итерациях)

Рассматривается одно из: Amplitude / PostHog / Yandex Metrica.

Целевые события:

- `onboarding_started`, `onboarding_completed`, `bracelet_paired`
- `baseline_started`, `baseline_completed_at_hours_X`
- `hrv_screen_opened`, `hrv_explainer_opened`
- `training_started`, `training_ended` (с типом активности)
- `sharing_invite_sent`, `sharing_accepted`
- `settings_baseline_reset`
- `account_deleted`

---

## 12. Открытые технические вопросы

Перечень уточняется по мере реализации mobile-стороны. Кратко:

- Очистка PPG-сигнала от артефактов в Veepoo SDK (встроено или реализуется на стороне бэкенда)
- Формат сырых R-R интервалов в выгрузке SDK
- Stress Index в выгрузке — формула и источник
- Активность (шаги) — разметка по времени
- Fall detection на моделях с базовым IMU
- State management в Flutter (Riverpod / Bloc / Provider)
- Локальная БД на mobile (Drift / Floor / Hive)
- Networking-клиент (Dio / http)
- Routing (GoRouter / auto_route)

---

## 13. Этапы

| Этап | Содержание | Срок |
|---|---|---|
| MVP-1 | 19 экранов первой очереди (онбординг + аутентификация + Home + HRV + настройки), baseline pipeline phase 1, Sentry, auth API, push для `baseline_ready` | 23.06.2026 |
| Заливка в стор | App Store + Google Play submit | 23.06.2026 |
| MVP-2 | Шесть экранов второй очереди (тренировка, история, Health Sharing, sleep, fall detection, композитная метрика), reset endpoint для baseline, расширение push | 30.06.2026 |
| Пост-MVP | Интеграция Apple Health, расширение источников данных (IMU-фильтрация PPG, доп. каналы), дальнейшие итерации продукта | TBD |
