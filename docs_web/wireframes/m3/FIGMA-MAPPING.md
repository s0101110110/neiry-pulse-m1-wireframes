# Figma ↔ HTML mapping · Pulse wireframes

**Файл Figma:** `SWRHwjeZkJu5c4eEoKjxQd` — https://www.figma.com/design/SWRHwjeZkJu5c4eEoKjxQd/Pulse
**Локальный источник:** `docs_web/wireframes/m3/*.html`
**Дата сборки:** 1 июля 2026

## Как читать эту таблицу

- **Figma node ID** — id для `use_figma` / `get_screenshot` (например `1:11`)
- **Figma name** — как называется node в Pulse-file
- **HTML source (v0)** — рабочий локальный источник, где правим содержание
- **Frame в HTML** — какой конкретно `.frame-with-caption` внутри HTML (когда файл содержит несколько экранов)
- **MVP-store версия** — обновлённый вариант для App Store submission (последняя стабильная)

---

## Onboarding (08-11)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:2` | 08a-onboarding-splash 1 | mobile-onboarding-01-splash-permission-bt-v0.html | ЭКРАН 1 · SPLASH / WELCOME | — |
| `41:16` | 08a-onboarding-splash 2 (дубль) | mobile-onboarding-01-splash-permission-bt-v0.html | ЭКРАН 1 · SPLASH / WELCOME | — |
| `1:3` | 08b-onboarding-permission-bt 1 | mobile-onboarding-01-splash-permission-bt-v0.html | ЭКРАН 2 · PERMISSION · BLUETOOTH | — |
| `1:4` | 09a-onboarding-bracelet-scan 1 | mobile-onboarding-02-bracelet-scan-pair-v0.html | ЭКРАН 3 · BRACELET SCAN | — |
| `1:5` | 09b-onboarding-bracelet-pairing 1 | mobile-onboarding-02-bracelet-scan-pair-v0.html | ЭКРАН 4 · BRACELET PAIRING | — |
| `1:6` | 10a-onboarding-notifications 1 | mobile-onboarding-03-notifications-calibrating-v0.html | ЭКРАН 5 · PERMISSION NOTIFICATIONS | mobile-onboarding-03-notifications-calibrating-mvp-store.html |
| `1:7` | 10b-onboarding-calibrating 1 | mobile-onboarding-03-notifications-calibrating-v0.html | ЭКРАН 6 · CALIBRATING | mobile-onboarding-03-notifications-calibrating-mvp-store.html |
| `1:8` | 10c-onboarding-baseline-modal 1 | mobile-onboarding-03-notifications-calibrating-v0.html | ЭКРАН 7 · ЛИЧНАЯ НОРМА · МОДАЛКА | mobile-onboarding-03-notifications-calibrating-mvp-store.html |
| `1:48` | 11a-fall-push-lock-screen 1 | mobile-onboarding-04-fall-detection-v0.html | ЭКРАН 8 · FALL · PUSH (LOCK SCREEN) | — |
| `1:47` | 11b-fall-in-app-detail 1 | mobile-onboarding-04-fall-detection-v0.html | ЭКРАН 9 · FALL · IN-APP DETAIL | — |

## Empty states + Home first-run (12)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:49` | 12a-home-first-run-empty 1 | mobile-onboarding-05-empty-states-v0.html | ЭКРАН 10 · HOME · FIRST-RUN EMPTY | mobile-onboarding-05-empty-states-mvp-store.html |
| — (нет в Figma) | 12b-hs-main-empty | mobile-onboarding-05-empty-states-v0.html | ЭКРАН 11 · HEALTH SHARING · EMPTY | mobile-onboarding-05-empty-states-mvp-store.html |

## Main app screens (01-06)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:11` | 01-home 1 | mobile-home-f1-v0.html | single-frame | — |
| `1:12` | 02a-training-start-step1 1 | mobile-training-start-v0.html | STEP 1 · Выбор типа активности | — |
| `1:13` | 02b-training-start-step2 1 | mobile-training-start-v0.html | STEP 2 · Preview + СТАРТ | — |
| `1:14` | 03a-training-active-page1-zones 1 | mobile-training-active-v0.html | PAGE 1 · Зоны / Пульс | — |
| `1:15` | 03b-training-active-page2-details 1 | mobile-training-active-v0.html | PAGE 2 · Детали сессии | — |
| `1:16` | 03c-training-active-page3-map 1 | mobile-training-active-v0.html | PAGE 3 · GPS Карта | — |
| `1:17` | 04-history 1 | mobile-history-v0.html | single-frame | mobile-history-mvp-store.html |
| `1:18` | 05-session-detail 1 | mobile-session-detail-v0.html | single-frame | — |
| `1:19` | 06-settings 1 | mobile-settings-v0.html | single-frame | mobile-settings-mvp-store.html |
| `68:60` | 06-settings 2 (дубль) | mobile-settings-v0.html | single-frame | mobile-settings-mvp-store.html |

## Health Sharing (07)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:20` | 07a-hs-main 1 | mobile-health-sharing-v0.html | ЭКРАН 1 · MAIN · список людей | — |
| `1:21` | 07b-hs-generate-qr 1 | mobile-health-sharing-v0.html | ЭКРАН 2 · GENERATE QR · юзер A | — |
| `1:22` | 07c-hs-scan-qr 1 | mobile-health-sharing-v0.html | ЭКРАН 3 · SCAN QR · юзер B | — |
| `1:23` | 07d-hs-success 1 | mobile-health-sharing-v0.html | ЭКРАН 4 · CONNECTION SUCCESS | — |
| `1:46` | 07e-hs-detail 2 | mobile-health-sharing-v0.html | ЭКРАН 5 · DETAIL · Папа · alert | — |

## Error/state screens (13-14)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `2:62` | 13a-state-bt-disconnect 1 | mobile-state-bt-disconnect-charging-low-v0.html | ЭКРАН 12 · HOME · BT-DISCONNECT BANNER | — |
| `2:61` | 13b-state-charging-low 1 | mobile-state-bt-disconnect-charging-low-v0.html | ЭКРАН 13 · HOME · CHARGING-LOW BANNER | — |
| `2:60` | 14a-state-camera-denied 1 | mobile-state-permission-denied-v0.html | ЭКРАН 14 · HS SCAN QR · CAMERA DENIED | — |
| `9:2` | 14b-state-location-denied 2 | mobile-state-permission-denied-v0.html | ЭКРАН 15 · TRAINING START · LOCATION DENIED | — |

## Training active states (15-16)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:27` | 15a-state-stop-confirm 1 | mobile-state-training-active-corner-cases-v0.html | ЭКРАН 16 · STOP CONFIRM | — |
| `9:3` | 15b-state-auto-pause 1 | mobile-state-training-active-corner-cases-v0.html | ЭКРАН 17 · AUTO-PAUSE | — |
| `1:26` | 15c-state-gps-lost 1 | mobile-state-training-active-corner-cases-v0.html | ЭКРАН 18 · GPS LOST | — |
| `9:4` | 16a-state-end-of-session 1 | mobile-state-end-of-session-bracelet-disconnect-v0.html | ЭКРАН 19 · END-OF-SESSION · SUMMARY | — |
| `1:33` | 16b-state-bracelet-disconnect-training 1 | mobile-state-end-of-session-bracelet-disconnect-v0.html | ЭКРАН 20 · TRAINING ACTIVE · BRACELET DISCONNECT | — |
| `9:5` | 16c-state-close-confirm 1 | mobile-state-end-of-session-bracelet-disconnect-v0.html | ЭКРАН 21 · END-OF-SESSION · CLOSE CONFIRM | — |

## Session detail states (17)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:31` | 17a-state-delete-confirm 1 | mobile-state-session-detail-edge-cases-v0.html | ЭКРАН 21 · SESSION DETAIL · DELETE CONFIRM | — |
| `1:32` | 17b-state-sharing-in-progress 1 | mobile-state-session-detail-edge-cases-v0.html | ЭКРАН 22 · SESSION DETAIL · SHARING IN PROGRESS | — |

## History states (18)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `1:43` | 18a-state-history-empty-month 1 | mobile-state-history-edge-cases-v0.html | ЭКРАН 23 · HISTORY · EMPTY MONTH | — |
| `1:44` | 18b-state-history-future-month 1 | mobile-state-history-edge-cases-v0.html | ЭКРАН 24 · HISTORY · FUTURE MONTH | — |
| `1:45` | 18c-state-history-multiple-sessions 1 | mobile-state-history-edge-cases-v0.html | ЭКРАН 25 · HISTORY · MULTIPLE SESSIONS/DAY | — |

## Health sharing states (19)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `9:6` | 19a-state-hs-scan-failed 1 | mobile-state-hs-edge-cases-v0.html | ЭКРАН 26 · HS SCAN QR · INVALID/EXPIRED | — |
| `2:51` | 19b-state-hs-role-onboarding 1 | mobile-state-hs-edge-cases-v0.html | ЭКРАН 27 · HS ROLE · USER B ONBOARDING | — |

## Profile + HRV (20)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `37:2` | 20a-profile-edit 2 | mobile-profile-hrv-detail-v0.html | ЭКРАН 28 · PROFILE · EDIT | mobile-profile-hrv-detail-mvp-store.html |
| `17:7` | 20b-hrv-detail 1 | mobile-profile-hrv-detail-v0.html | ЭКРАН 29 · HRV · DETAIL VIEW | mobile-profile-hrv-detail-mvp-store.html |
| `17:8` | 20c-hrv-explainer-modal 1 | mobile-profile-hrv-detail-v0.html | ЭКРАН 30 · HRV · EXPLAINER MODAL | mobile-profile-hrv-detail-mvp-store.html |

## Settings detail (21)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `37:3` | 21a-settings-bt-pairing 1 | mobile-settings-detail-v0.html | ЭКРАН 31 · SETTINGS · BT PAIRING | — |
| `37:6` | 21b-settings-notifications 1 | mobile-settings-detail-v0.html | ЭКРАН 32 · SETTINGS · NOTIFICATIONS | — |
| `41:18` | 21b-settings-notifications 4 (variant) | mobile-settings-detail-v0.html | ЭКРАН 32 · variant | — |
| `41:22` | 21b-settings-notifications 5 (variant) | mobile-settings-detail-v0.html | ЭКРАН 32 · variant | — |
| `38:8` | 21b-settings-notifications 2 (variant) | mobile-settings-detail-v0.html | ЭКРАН 32 · variant | — |
| `38:10` | 21b-settings-notifications 3 (variant) | mobile-settings-detail-v0.html | ЭКРАН 32 · variant | — |
| — (нет в Figma) | 21c-settings-privacy | mobile-settings-detail-v0.html | ЭКРАН 33 · SETTINGS · PRIVACY | — |
| — (нет в Figma) | (settings · калибровка браслета) | mobile-settings-detail-v0.html | ЭКРАН 34 · SETTINGS · КАЛИБРОВКА БРАСЛЕТА | — |

## Sleep detail (22) — нет в Figma-file

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| — | 22a-sleep-detail | mobile-sleep-detail-v0.html | ЭКРАН 34 · SLEEP · DETAIL VIEW | — |
| — | 22b-sleep-explainer-modal | mobile-sleep-detail-v0.html | ЭКРАН 35 · SLEEP · EXPLAINER MODAL | — |

## Baseline ready + First HRV (23)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `39:13` | 23a-baseline-ready 1 | mobile-baseline-ready-first-hrv-v0.html | ЭКРАН 36 · ЛИЧНАЯ НОРМА · ГОТОВО | mobile-baseline-ready-first-hrv-mvp-store.html |
| `39:14` | 23b-first-hrv-reveal 1 | mobile-baseline-ready-first-hrv-v0.html | ЭКРАН 37 · HRV · FIRST MEASUREMENT REVEAL | mobile-baseline-ready-first-hrv-mvp-store.html |

## Health sharing extras (24) — нет в Figma-file

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| — | 24a-hs-role-user-a-sharing | mobile-hs-role-user-a-v0.html | ЭКРАН 38 · HS ROLE · USER A SHARING | — |
| — | 24b-hs-two-way-dashboard | mobile-hs-role-user-a-v0.html | ЭКРАН 39 · HS · TWO-WAY DASHBOARD | — |

## Auth flow (25)

| Figma node | Figma name | HTML v0 | Frame | MVP-store версия |
|---|---|---|---|---|
| `94:65` | 25a-auth-signup 1 | mobile-auth-signup-login-reset-v0.html | ЭКРАН 1 · СОЗДАНИЕ АККАУНТА | — |
| `94:66` | 25b-auth-login 1 | mobile-auth-signup-login-reset-v0.html | ЭКРАН 2 · ВХОД В АККАУНТ | — |
| `94:67` | 25c-auth-reset 1 | mobile-auth-signup-login-reset-v0.html | ЭКРАН 3 · СБРОС ПАРОЛЯ | — |

## Прочее (в Figma без source-mapping)

- `image 8` (id 66:57) — placeholder image, скорее всего reference
- Rectangle 1-8 (id 1:10, 39:11, 1:34, 17:9, 1:35, 1:36, 2:65, 41:19) — фоны секций Figma-file
- Разделы (тексты на канвасе Figma) — навигационные заголовки секций, не UI

---

## Discrepancies (нужны решения PM)

**Экраны есть в HTML, но НЕТ в Figma-file:**
- `12b-hs-main-empty` (Empty state Health Sharing) — из onboarding-05
- `21c-settings-privacy` — из settings-detail
- `22a-sleep-detail`, `22b-sleep-explainer-modal` — весь Sleep flow
- `24a-hs-role-user-a-sharing`, `24b-hs-two-way-dashboard` — из hs-role-user-a
- Settings · Калибровка браслета

**Дубли в Figma:**
- `08a-onboarding-splash 2` (41:16) — дубль 08a-onboarding-splash 1
- `06-settings 2` (68:60) — дубль 06-settings 1
- `21b-settings-notifications 1-5` (37:6, 38:8, 38:10, 41:18, 41:22) — 5 копий одного экрана

**Существуют -mvp-store версии HTML — обновлённые для App Store:**
- mobile-history-mvp-store.html (04-history)
- mobile-settings-mvp-store.html (06-settings)
- mobile-onboarding-03-notifications-calibrating-mvp-store.html (10a-c)
- mobile-onboarding-05-empty-states-mvp-store.html (12a)
- mobile-profile-hrv-detail-mvp-store.html (20a-c)
- mobile-baseline-ready-first-hrv-mvp-store.html (23a-b)

**Правило (по умолчанию):** правки идут в **v0**-версию (это master). При каждой правке проверяем есть ли -mvp-store — если есть, синхронизируем обе.

---

## Workflow правки (напоминание)

1. PM: Figma URL + требования
2. Я → определяю по этой таблице какой HTML/frame править
3. Я → правлю HTML + screenshot → показываю PM
4. PM approve
5. Я → экспортирую новую PNG в `ui_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14/`
6. Я → заменяю image fill соответствующего Figma-rectangle через `use_figma`
7. Готово · синхрон в трёх местах: HTML source · PNG · Figma review-gallery

---

**Обновляется:** этот файл — living document. При добавлении новых экранов / переименовании — обновить.
