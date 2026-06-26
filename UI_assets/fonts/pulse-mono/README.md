# Pulse Mono

**Моноширинная константа Neiry Pulse.** Используется для цифровых данных (пульс, HRV,
дни, периоды) и табличных значений в мобильном приложении и дашборде.

## Что это

JetBrains Mono с одним изменением: **из глифа нуля удалена точка** → ноль стал плоским
овалом. Всё остальное идентично оригиналу:

- **0** — плоский, без точки и слэша
- **4** — открытая сверху
- **5 / 7** — геометричные
- кириллица, метрики, кернинг, открытая 4 — как в JetBrains Mono

## Зачем патч, а не CSS

У JetBrains Mono **нет** OpenType-фичи для плоского нуля (JetBrains/JetBrainsMono issue #625
не решён). Через `font-feature-settings` доступны только: точка (дефолт) или слэш (`"zero" 1`).
Точка — это отдельный 3-й контур глифа `zero`; `build.py` удаляет именно его.

## Файлы

| Файл | Назначение |
|---|---|
| `PulseMono-{Regular,Medium,SemiBold,Bold}.woff2` | для веба / прототипов |
| `PulseMono-{Regular,Medium,SemiBold,Bold}.ttf` | для Flutter / десктопа / дизайн-тулов |
| `build.py` | воспроизводимая сборка из `src/` |
| `src/JetBrainsMono-*.ttf` | исходные оригиналы |
| `OFL.txt` | лицензия |

## Подключение (веб / HTML-прототипы)

```css
@font-face{font-family:'Pulse Mono';font-weight:400;
  src:url('PulseMono-Regular.woff2') format('woff2');}
@font-face{font-family:'Pulse Mono';font-weight:500;
  src:url('PulseMono-Medium.woff2') format('woff2');}
@font-face{font-family:'Pulse Mono';font-weight:600;
  src:url('PulseMono-SemiBold.woff2') format('woff2');}
@font-face{font-family:'Pulse Mono';font-weight:700;
  src:url('PulseMono-Bold.woff2') format('woff2');}

.pulse-value{
  font-family:'Pulse Mono', 'JetBrains Mono', monospace;
  font-variant-numeric: tabular-nums;   /* ровные колонки цифр */
}
```

## Подключение (Flutter — для Кирилла)

```yaml
# pubspec.yaml
flutter:
  fonts:
    - family: Pulse Mono
      fonts:
        - asset: fonts/PulseMono-Regular.ttf
          weight: 400
        - asset: fonts/PulseMono-Medium.ttf
          weight: 500
        - asset: fonts/PulseMono-SemiBold.ttf
          weight: 600
        - asset: fonts/PulseMono-Bold.ttf
          weight: 700
```

```dart
Text('100', style: TextStyle(fontFamily: 'Pulse Mono',
  fontFeatures: [FontFeature.tabularFigures()]));
```

## Пересборка

```bash
pip install fonttools brotli
python3 build.py        # перечитает src/ → PulseMono-*.{ttf,woff2}
```

## Лицензия

JetBrains Mono распространяется под **SIL Open Font License 1.1** без объявленного
Reserved Font Name — производные и переименование разрешены. Полный текст — `OFL.txt`.
Pulse Mono наследует ту же лицензию.

## Превью

Открыть `preview.html` в браузере — сравнение оригинал ↔ Pulse Mono + все начертания.
