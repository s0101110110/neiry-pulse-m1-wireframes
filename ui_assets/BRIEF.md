# UX TASK BRIEF — Legal Compliance UI Pack (9 экранов)

**Дата:** 2026-06-24
**От:** PM (Константин)
**Приоритет:** КРИТИЧЕСКИЙ — без этих экранов приложение не пройдёт ревью Apple App Store / Google Play и нарвётся на штраф РКН по 152-ФЗ (с поправками 01.09.2025).

---

## Контекст

3 юридических документа уже готовы (PP + UA + Consent в RU+EN, дата 24.06.2026, хранятся в `docs_web/legal/`).
Текущий Sign Up имеет один общий чекбокс — этого **недостаточно** по 152-ФЗ ст. 9 (согласие на специальную категорию = данные о здоровье) и ст. 12 (трансграничная передача).
Apple guideline 5.1.1(v) требует **in-app удаление аккаунта**. Apple 5.1.3 требует Privacy Policy **доступной внутри приложения**. Apple 5.1.5 + Android — pre-permission rationale экраны.

Эта задача закрывает 6 блокирующих пробелов:

1. **Sign Up v2** — раздельные чекбоксы + биометрический disclaimer
2. **Age Gate** — проверка 16+ (PP §10 / UA §1.4)
3. **Wellness disclaimer** — «велнес, не медицинское изделие»
4. **Account Deletion flow** — 3-шаговое удаление прямо в приложении
5. **Settings → Юридическая информация** — Legal hub с тремя документами + Revoke Consent
6. **Permission Rationale** — Bluetooth, Push-уведомления, GPS (3 экрана)

Всего — **9 phone-экранов** (некоторые потоки многошаговые).

---

## Output paths

**HTML:** `docs_web/wireframes/m3/mobile-legal-compliance-pack-v0.html`

**Side-by-side proof PNG** (для PM acceptance):
`UI_assets/screenshots/onboarding-2026-06-14/legal-pack-side-by-side.png`

**Отдельные proof PNG** (crop из side-by-side, правило A5 — НЕ slicing-script):
- `UI_assets/screenshots/onboarding-2026-06-14/legal-01-age-gate.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-02-age-gate-blocked.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-03-wellness-disclaimer.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-04-signup-v2.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-05-permission-bt.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-06-permission-push.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-07-permission-gps.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-08-settings-legal-hub.png`
- `UI_assets/screenshots/onboarding-2026-06-14/legal-09-account-delete-flow.png` (можно одним кадром 3 этапа)

Transparent PNG в `sliced-flow-v2-1-transparent-2026-06-14/` — НЕ нужны на этой итерации (PM попросит отдельно если будет нужно для сборки flow).

---

## 9 экранов — копирайт и UX-логика

⚠️ **Копирайт от PM — verbatim, не редактировать.** Безопасные формулировки уже выверены против Apple 1.4.1 / 5.1.3 и 152-ФЗ ст. 10. Если кажется, что текст можно улучшить — выноси в раздел «Возражения skills», но НЕ заменяй.

### Экран 1 — Age Gate (ввод даты)

**Контекст в потоке:** первый шаг onboarding, до Wellness disclaimer и Sign Up.

- Hero icon: SVG cake/birthday (wine, 64×64) — опционально, можно без icon
- Eyebrow (mono uppercase wine 11pt): `НАЧНЁМ`
- Title (Onest 700 28pt): «Сколько вам лет?»
- Sub (Space Grotesk 14pt foreground): «Pulse предназначен для пользователей старше 16 лет»
- DatePicker (native-style) — поле ввода даты рождения, placeholder «ДД.ММ.ГГГГ»
- CTA primary wine: «Продолжить» (disabled пока дата не введена)
- Text-link grey secondary под CTA: «Почему мы спрашиваем?»
  - При тапе раскрывается inline-блок:
    > «Pulse — велнес-приложение для здоровых взрослых пользователей. В соответствии с нашей Политикой конфиденциальности мы не предназначены для использования детьми младше 16 лет.»

### Экран 2 — Age Gate Blocked (если <16)

- Hero icon: SVG ban/forbidden (alert-orange `#d97706`, 80×80)
- Eyebrow (mono): `ИЗВИНИТЕ`
- Title (Onest 700 28pt): «Приложение не для вас сейчас»
- Sub: «Neiry Pulse предназначено для пользователей старше 16 лет.
  Если вы достигнете 16 лет, сможете зарегистрироваться в любой момент.»
- Single CTA: «Понятно» (grey/secondary, не destructive) — возвращает на splash

### Экран 3 — Wellness Disclaimer

**Контекст в потоке:** после Age Gate (если ≥16), перед Sign Up. Можно пропустить во второй сессии.

- Hero icon: SVG heart-outline (wine, 80×80) — или brain-and-heart комбо
- Eyebrow (mono uppercase wine 11pt): `ВАЖНО`
- Title (Onest 700 26pt): «Neiry Pulse — велнес-приложение»
- Body (Space Grotesk 14pt):
  > «Pulse помогает понимать ваше состояние и улучшать самочувствие.
  >
  > **Это не медицинское изделие** и **не предназначено для диагностики или лечения** заболеваний.
  >
  > По любым вопросам о здоровье обращайтесь к квалифицированному медицинскому специалисту.»
- Single CTA wine primary: «Понятно, продолжить»
- (Никаких «не сейчас» — это required disclaimer, не optional)

### Экран 4 — Sign Up v2 (раздельные чекбоксы)

**Это переделка существующего экрана `signup.png`. НЕ создавать дополнительно экран входа/сброса пароля — фокус только на регистрации.**

- App-bar: back-arrow + title «Регистрация»
- Hero (Onest 700 24pt): «Создайте аккаунт»
- Sub (14pt grey): «Чтобы начать отслеживать своё самочувствие»
- Fields (canonical input pattern):
  - Email — placeholder «your.email@example.com»
  - Пароль — placeholder «Минимум 8 символов», show/hide toggle
  - Повторите пароль
- **Warning blockquote** (alert-soft bg `#fdf3e1` + border-left 4px alert-orange `#d97706`, padding 14px, radius 12px) — над чекбоксами:
  - Icon: SVG alert-circle (alert-orange, 16×16)
  - Eyebrow (mono uppercase 11pt alert-orange): `СПЕЦИАЛЬНАЯ КАТЕГОРИЯ ДАННЫХ`
  - Text (13pt): «Приложение обрабатывает данные о вашем самочувствии — пульс, HRV, фазы сна. По 152-ФЗ это специальная категория персональных данных. Подробнее — в Согласии ниже.»
- **3 обязательных чекбокса** (каждый — checkbox + текст; на ссылку — wine с подчёркиванием, открывает соответствующий документ in-app):
  - ☐ Принимаю **[Пользовательское соглашение]**
  - ☐ Даю **[Согласие на обработку персональных данных]**, включая данные о состоянии
  - ☐ Согласен на трансграничную передачу обезличенных идентификаторов в **Google LLC (США)** для push-уведомлений
- **1 опциональный чекбокс** (грей divider сверху):
  - ☐ Хочу получать новости и советы по велнесу *(можно отключить в любой момент)*
- Под чекбоксами — info-link 11pt grey: «Ознакомиться с [Политикой конфиденциальности]»
  *(PP — информационный документ, не требует согласия по 152-ФЗ)*
- CTA wine primary full-width 48pt: **«Зарегистрироваться»** *(disabled, пока 3 обязательных чекбокса не отмечены — визуально opacity 0.4)*
- Внизу secondary link grey: «Уже есть аккаунт? **Войти**»

### Экран 5 — Permission Rationale: Bluetooth

**Контекст в потоке:** показывается при первом запуске после Sign Up, до системного dialog Bluetooth.

- Status bar + минимальный app-bar (close-icon «×» top-right — skip)
- Hero icon: SVG bluetooth + браслет (wine, 80×80) — стилизованный, не emoji
- Title (Onest 700 24pt, centered): «Разрешите Bluetooth»
- Body (Space Grotesk 14pt foreground, centered, max 280px ширина):
  > «Чтобы измерять ваше самочувствие, Pulse подключается к браслету Neiry по Bluetooth. Без Bluetooth приложение не сможет получать данные с устройства.»
- Single CTA wine primary full-width: «Разрешить»
- Sub-link grey secondary: «Не сейчас»

### Экран 6 — Permission Rationale: Push-уведомления

- Hero icon: SVG bell (wine, 80×80)
- Title: «Сервисные уведомления»
- Body bullet list:
  > «Мы пришлём только важное:
  > • Ваша личная норма готова
  > • Браслет синхронизирован
  > • Напоминания о тренировках
  >
  > Мы не отправляем рекламу и спам.»
- Single CTA wine primary: «Разрешить»
- Sub-link: «Не сейчас»

### Экран 7 — Permission Rationale: GPS

**ВАЖНО:** показывается **только перед первой тренировкой с маршрутом** (не на onboarding). Это правило Apple 5.1.5 — explicit purpose binding.

- Hero icon: SVG map-pin-route (wine, 80×80)
- Title: «GPS для тренировки»
- Body:
  > «GPS включается **только во время тренировки** с отслеживанием маршрута. Вне тренировок маршрут не пишется и не передаётся.
  >
  > Вы всегда можете отключить GPS в настройках.»
- Single CTA wine primary: «Разрешить»
- Sub-link: «Не сейчас»

### Экран 8 — Settings → Юридическая информация (Legal hub)

**Контекст:** Settings → Юридическая информация (новый пункт в Settings).

- App-bar: back-arrow + title «Юридическая информация»
- Sectioned list (canonical Settings pattern — card-bg `#FFF9FA`, hairline divider `#EAE5DC`):

**Секция «Документы»:**
- Row 1:
  - Icon: SVG document-text (wine, 24×24)
  - Title (15pt): «Политика конфиденциальности»
  - Sub (12pt grey mono): `ВЕРСИЯ 1.0 · 24.06.2026`
  - Chevron-right
- Row 2: «Пользовательское соглашение» (та же структура)
- Row 3: «Согласие на обработку персональных данных» (та же структура)

**Секция «Управление согласием»:**
- Row 4:
  - Icon: SVG alert-circle (destructive red `#b91c1c`, 24×24)
  - Title (15pt destructive red): «Отозвать согласие»
  - Sub (12pt grey): «Прекращает обработку данных. Доступ к приложению будет заблокирован.»
  - Chevron-right

**Внизу секции — info-text 11pt grey:**
> «При нажатии вы откроете документ в приложении. Версии хранятся в архиве и доступны на pulse.neiry-bci.com.»

### Экран 9 — Account Deletion Flow (3 этапа в одном экране-monтаже)

**Можно сделать как 3 phone-mockups горизонтально, показав поток.**

**9a · Entry (Settings → Конфиденциальность):**
- Sectioned Settings list:
  - «Деактивировать аккаунт» (grey, sub: «Данные сохраняются, можно восстановить»)
  - **«Удалить аккаунт окончательно»** (destructive red 15pt, sub: «Безвозвратное удаление через 30 дней»)

**9b · Confirm modal (step 1) — overlay поверх 9a:**
- Centered modal-card 320×auto, white card, border-radius 20px, padding 24px, box-shadow:
  - Icon top: SVG alert-triangle (destructive red, 40×40)
  - Eyebrow (mono uppercase destructive red 11pt): `ВНИМАНИЕ`
  - Title (Onest 700 22pt destructive red): «Удалить аккаунт?»
  - Body (13pt foreground):
    > «Все ваши данные будут безвозвратно удалены через 30 дней:
    > • История тренировок и сессий
    > • Все измерения HRV, пульса, сна
    > • Ваша персональная норма
    > • Связи Health Sharing»
  - 2 actions stacked:
    - **«Продолжить удаление»** — destructive red primary CTA (48pt)
    - «Отмена» — text-link grey

**9c · Success state — поверх 9a после подтверждения:**
- Centered modal-card 320×auto:
  - Icon top: SVG check-circle (wine, 40×40)
  - Eyebrow (mono uppercase wine 11pt): `ЗАПРОС ПРИНЯТ`
  - Title (Onest 700 22pt): «Аккаунт будет удалён»
  - Body (13pt):
    > «Окончательное удаление произойдёт через 30 дней (до 24 июля 2026).
    >
    > В течение этого срока вы можете отменить удаление, войдя в аккаунт.»
  - Single CTA wine primary: «Закрыть»

---

## Дизайн-константы (заимствуем из Bevel-clone v2 / canonical Pulse)

### Поверхности и цвет
- **Card bg:** `#FFF9FA` (Chill White)
- **Screen bg:** `#F7F2EC` (warm cream)
- **Hairline border:** `#EAE5DC`
- **Soft shadow:** `0 4px 12px rgba(26,24,21,0.04)` + `0 1px 3px rgba(26,24,21,0.03)`
- **Wine primary:** `#831843`
- **Destructive red:** `#b91c1c` (для «Удалить аккаунт», «Отозвать согласие»)
- **Alert orange:** `#d97706` (для биометрического disclaimer, age gate blocked)
- **Alert soft bg:** `#fdf3e1`

### Радиусы
- Card outer: 24-28px
- Modal: 20px
- Input fields: 12px
- Inline pills: 8-10px
- Status badges: 999px

### Шрифты — ОБЯЗАТЕЛЬНО только эти
- **Onest 700** — heroes 22-32pt, hierarchy titles
- **Space Grotesk** или **Golos Text** — UI body 13-14pt
- **JetBrains Mono** или **Geist Mono** — eyebrows uppercase 11pt, version labels, technical numbers
- `tabular-nums` на всех числах (даты, версии, размеры)
- letter-spacing -0.6 to -1px на heroes
- letter-spacing +0.6 to +1px на mono-eyebrows

### Box-sizing
- `*, *::before, *::after { box-sizing: border-box; }` глобально

### Phone-bezel (для side-by-side mockup)
- `box-shadow: 0 0 0 10px #1a1814, 0 0 0 11px #2a2620`
- Phone width: 360px
- Screen radius: 32-40px

---

## Копирайт правила (ОБЯЗАТЕЛЬНЫЕ)

### Только русский
- Это базовый язык интерфейса для М3-релиза. EN-локализация — отдельная итерация после acceptance.

### ЗАПРЕЩЁННЫЕ формулировки (Apple 1.4.1 + 5.1.3 reject risk)
- ❌ «диагноз», «диагностика»
- ❌ «лечение», «лечит»
- ❌ «при бессоннице», «при стрессе», «при аритмии» (как болезнь)
- ❌ «снижает давление», «нормализует»
- ❌ «медицинский», «клинический»

### БЕЗОПАСНЫЕ альтернативы
- ✅ «велнес», «велнес-приложение», «велнес-метрика»
- ✅ «не медицинское изделие»
- ✅ «общее самочувствие», «состояние»
- ✅ «фитнес-данные», «фитнес-метрика»
- ✅ «общая информация», «информационный характер»

### Англицизмы — ЗАПРЕЩЕНЫ кроме исключений
- ❌ «нотификация», «дашборд», «онбординг» в UI-копирайте
- ✅ Разрешены: **Pulse**, **Neiry**, **HRV**, **Bluetooth**, **QR**, **GPS**, **iOS/Android**, **Apple/Google LLC**, **SpO2**, **REM**

### Иконки
- **Только SVG**, никаких emoji в UI-копирайте
- Phosphor-style 1.5px stroke или solid filled
- Cвет icon = wine `#831843` для primary, destructive red для warning, alert-orange для info, muted grey для neutral

---

## Skills — агент выбирает сам

**Рекомендую (но не диктую):**

- **`Skill impeccable args:"critique <path>"`** — anti-slop: не condescending («Спасибо за регистрацию!», «Молодец!» — НЕТ), не overdramatize, hierarchy между primary/destructive
- **`Skill impeccable args:"audit <path>"`** — WCAG AA: destructive red `#b91c1c` на `#FFF9FA` (контраст ≥ 4.5:1), alert-orange на alert-soft (≥ 4.5:1), wine на screen-bg (≥ 4.5:1). Compliance text должен быть читаемым.
- **`Skill impeccable args:"harden <path>"`** — edge cases:
  - что если email уже занят?
  - что если пароли не совпадают?
  - что если пользователь раз 18, а DatePicker даёт ввести 22.06.2026 (т.е. ему 0 лет)?
  - что если Bluetooth permission была отозвана через системные настройки после grant?

**Хард-баны:** `init`, `document`, `craft`, `extract`, `live`, `pin`, `overdrive`. Не вызывай `impeccable` без аргумента.

`emil-design-eng` — опционально для motion (modal scale-in 240ms ease-out на 9b/9c, banner slide-down на 5/6/7).

---

## Контрольный список (для агента — перед сдачей PM)

- [ ] 9 экранов в одном HTML-файле, side-by-side render
- [ ] Все 9 проверены на копирайт (нет запрещённых слов)
- [ ] 3 обязательных чекбокса на Sign Up + 1 опциональный
- [ ] CTA «Зарегистрироваться» disabled (opacity 0.4) пока не отмечены 3 обязательных
- [ ] Age Gate — DatePicker, валидация ≥16
- [ ] Blocked screen для <16 показан отдельным мокапом
- [ ] Wellness disclaimer — слова «не медицинское изделие» и «не для диагностики» **видны на экране**
- [ ] 3 permission rationale экрана — со своими icon, своим body, single CTA + skip-link
- [ ] Settings → Legal hub содержит **4 строки** (3 документа + Revoke)
- [ ] Account deletion flow — 3 шага (entry + confirm + success) с **destructive red** на правильных элементах
- [ ] WCAG AA grep verify: все wine/destructive/alert hex на bg прошли ≥ 4.5:1
- [ ] Только Onest + Space Grotesk/Golos + Mono шрифты (grep verify)
- [ ] Wine `#831843` + destructive `#b91c1c` + alert-orange `#d97706` — единственные chromatic accents (grep verify)
- [ ] Никаких emoji в UI (grep verify Unicode emoji ranges)
- [ ] Side-by-side proof PNG отрендерен через Chrome headless
- [ ] 9 individual proof PNG получены **crop'ом** из side-by-side (НЕ slicing-script — правило A5)
- [ ] HTML не трогает существующие файлы (`mobile-*-v0.html` в `wireframes/m3/` остальные не модифицируются)

---

## Acceptance Gate (правило PM)

1. **НЕ КОММИТИТЬ** — никаких `git add` / `git commit`, пока PM не сказал явно «принято»
2. После генерации side-by-side PNG — **показать PM** (PM откроет через Read tool, опишет что видит)
3. Если PM просит правки — сделать правки, переснять PNG, показать снова
4. Только после явного «принято» от PM — я (PM-агент) сам коммичу с осмысленным сообщением на русском

---

## Возражения skills — формат разбора

Если skill ругает что-то из ОБЯЗАТЕЛЬНЫХ ТРЕБОВАНИЙ PM (раздельные чекбоксы, версионирование, копирайт «велнес»), **НЕ глуши через REJECTED_BY_AGENT**:

1. В HTML-артефакте внизу — секция **«Возражения skill'ов — на разбор PM»** с таблицей (skill / совет / аргумент / оценка агента / что сделано)
2. В докладе — отдельная рубрика `ВОЗРАЖЕНИЯ SKILL'ОВ`

Замкнутые константы (раздельные чекбоксы, копирайт «велнес», split-схема операторов) оставляй даже если skill ругает — это compliance, не дизайн-вкусовщина.

---

## Дедлайн

Сегодня (24.06) — желательно. Завтра (25.06) Костя заливает первую сборку в стора, эти экраны нужны до того.

---

## Если что-то непонятно

Спрашивай PM до старта. Лучше потратить 5 минут на уточнение, чем 2 часа на переделку.
