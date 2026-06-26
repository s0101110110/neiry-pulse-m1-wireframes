# Neiry Pulse — app icon

Дата: 2026-06-24
Версия: v1 (временный SVG, может быть заменён финальным от дизайнера)

## Файлы

| Файл | Размер | Назначение |
|---|---|---|
| `icon.svg` | vector | Source. Для масштабирования и финального redesign |
| `icon-1024.png` | 1024×1024 | App Store / Google Play store listing icon |
| `icon-512.png` | 512×512 | Flutter `pubspec.yaml` flutter_launcher_icons / iOS App Icon (1024 → derived) |
| `icon-192.png` | 192×192 | Android adaptive icon (foreground layer, Google Play минимальный) |

## Дизайн-токены

- **Background:** wine `#831843` (squircle, corner radius 22% = 225px при 1024)
- **Foreground:** white `#ffffff`
- **Composition:** circle outline + pulse waveform (как на Splash screen MVP)
- **Padding (icon-1024):** ~17-20% между squircle edge и pulse circle

## Использование в Flutter

```yaml
# pubspec.yaml
dev_dependencies:
  flutter_launcher_icons: ^0.13.1

flutter_launcher_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/icon-1024.png"
  adaptive_icon_background: "#831843"
  adaptive_icon_foreground: "assets/icon-foreground.png"
```

(если adaptive icon — foreground layer нужен отдельно без squircle background; пока используй полный `icon-1024.png`)

## Использование в editor `app-store-screenshots`

Уже подключено: `UI_assets/store-screenshots-2026-Q3/public/app-icon.png` — копия `icon-1024.png`.

## Замена в будущем

Когда финальный дизайн готов:
1. Заменить `icon.svg` на новый source
2. Перегенерировать PNG: `sips -z N N icon.svg.png --out icon-N.png` (или через Figma export)
3. Скопировать `icon-1024.png` в `UI_assets/store-screenshots-2026-Q3/public/app-icon.png`
4. Обновить Flutter `assets/`
