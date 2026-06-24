# MVP v.1 · 23.06.2026 — карта папки

Всё что относится к **первому релизу мобильного приложения Neiry Pulse** (MVP scope: пульс + HRV + личная норма + тренд HRV + 152-ФЗ + экспорт).

## Структура

### `01-store-screenshots/` — для App Store + Google Play submission

4 финальных PNG, которые накладываются на marketing-headlines в editor скилла `ParthJadhav/app-store-screenshots` (см. `UI_assets/PLAYBOOK.md` секция 7) и заливаются в листинги сторов.

| Файл | Headline для editor'а |
|---|---|
| `01-home-first-run.png` | «Учимся понимать тебя — 24-48 часов калибровки» |
| `02-home.png` | «Твой пульс и HRV — в реальном времени» |
| `03-hrv-detail.png` | «Понимай свой стресс и восстановление глубже» |
| `04-settings.png` | «Все данные под твоим контролем.» |

### `02-flutter-handover/` — для Кирилла (Flutter dev)

Артефакты для верстки мобильного приложения. Открой `handover.html` или `flow-board.html` в браузере.

| Файл | Назначение |
|---|---|
| `handover.html` | Основной handover-документ: 22 экрана по 4 секциям + tech notes + дизайн-токены + out-of-MVP список. Self-contained (inline base64 PNG). |
| `flow-board.html` | Figma-style flow board: визуальная карта всех экранов сгруппированных по фазам user flow. |
| `flow-board.png` | PNG-экспорт flow board (для отправки в мессенджер). 4400×2900. |
| `full-flow.pdf` | Multi-page A4 PDF из `handover.html`. В `.gitignore` (правило проекта). |
| `handover-preview.png` | Preview рендер `handover.html` целиком — для быстрого ознакомления. |

### `03-source-png/` — исходники без bezel

21 PNG чистого UI без iPhone-рамки в нативном разрешении 390×844 @3x = 1170×2532. Это **источники для верстки**. Кирилл смотрит как референс для CSS/markup.

Группировка по фазам user flow:

**Onboarding & Auth (10):**
- `splash.png`, `permission-bt.png`
- `signup.png`, `login.png`, `reset-password.png`
- `bracelet-scan.png`, `bracelet-pairing.png`
- `onboarding-calibrating.png` (frames notifications + calibrating объединены)
- `baseline-ready.png`

**Main app (4):**
- `home-first-run.png`, `home.png`
- `hrv-detail.png`
- `history.png`

**Settings (5):**
- `settings.png`
- `settings-bt-pairing.png`
- `settings-notifications.png`
- `settings-privacy.png`
- `settings-calibration.png`

**Error states (3):**
- `bt-disconnect.png`, `charging-low.png`, `permission-denied.png`

## MVP scope — что НЕ в этом релизе

❌ Тренировки (start / active / зоны / GPS-маршрут)
❌ Сон (фазы / анализ / cycle)
❌ Health sharing (Тренер / Мама / опекуны / + Управление)
❌ Fall detection (onboarding-04 не в flow)
❌ Session detail / history of training sessions

## Источники HTML wireframes

Все исходники в `docs_web/wireframes/m3/mobile-*-mvp-store.html`:
- `mobile-auth-signup-login-reset-v0.html` (auth — 3 frames)
- `mobile-onboarding-01-splash-permission-bt-v0.html` (splash + permission)
- `mobile-onboarding-02-bracelet-scan-pair-v0.html` (scan + pair)
- `mobile-onboarding-03-notifications-calibrating-mvp-store.html`
- `mobile-onboarding-05-empty-states-mvp-store.html` (home first-run)
- `mobile-baseline-ready-first-hrv-mvp-store.html`
- `mobile-home-f1-mvp-store.html`
- `mobile-profile-hrv-detail-mvp-store.html`
- `mobile-history-mvp-store.html` (новый)
- `mobile-settings-mvp-store.html`
- `mobile-settings-detail-mvp-store.html` (4 subscreens)
- `mobile-state-bt-disconnect-charging-low-mvp-store.html`
- `mobile-state-permission-denied-v0.html`

## История изменений

- **23.06.2026 ночь:** iteration 3-4 — rework wireframes под MVP scope (убраны тренировки/сон/sharing), новый экран «История», MVP-cut Settings detail, fix calibration time (24-48ч), fix «Спите с ним» → «Носите ночью», создан flutter-handover + Figma-style flow-board, reorganization папки в текущую структуру.
