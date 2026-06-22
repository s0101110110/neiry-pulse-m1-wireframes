// Neiry Pulse — constants.ts patch instructions
// Не копировать целиком! Это инструкция, какие места заменить в `src/lib/constants.ts`
// после `cp -R <SKILL_DIR>/template/. ./`.

// =======================================================
// PATCH 1 — DEFAULT_THEME_ID
// =======================================================
// БЫЛО:
//   export const DEFAULT_THEME_ID: ThemeId = "clean-light";
// СТАЛО:
export const DEFAULT_THEME_ID = "neiry-pulse";

// =======================================================
// PATCH 2 — добавить в THEMES единственную тему "neiry-pulse"
// =======================================================
// Найти `export const THEMES: Record<string, Theme> = { ... };`
// ВНУТРИ объекта добавить (можно ПЕРЕД всеми остальными темами):

export const NEIRY_PULSE_THEME_ENTRY = {
  "neiry-pulse": {
    id: "neiry-pulse",
    name: "Neiry Pulse",
    bg: "#f7f5ef",        // --background (Bevel-tone)
    bgAlt: "#0c0a09",     // --foreground (для контрастных постеров)
    fg: "#0c0a09",        // --foreground
    fgAlt: "#f7f5ef",     // обратный (на тёмных карточках)
    accent: "#831843",    // PROTECTED wine
    muted: "#78716c",     // --muted-foreground
  },
};

// =======================================================
// PATCH 3 (optional) — отключить ненужные темы
// =======================================================
// Остальные темы из шаблона (`clean-light`, `dark-bold`, `warm-editorial`,
// `ocean-fresh`, `bloom-roast`) можно ОСТАВИТЬ — они не мешают, агент editor
// просто выбирает "neiry-pulse" как дефолт. Удалять их НЕ обязательно.
//
// Если хочется чистоты — заменить весь объект THEMES на:
//   export const THEMES: Record<string, Theme> = { ...NEIRY_PULSE_THEME_ENTRY };

// =======================================================
// PATCH 4 (опционально) — CANVAS dimensions
// =======================================================
// CANVAS / EXPORT_SIZES оставляем БЕЗ ИЗМЕНЕНИЙ.
// Apple 6.9″/6.5″/6.3″/6.1″ и Google Play sizes — все уже корректные.

// =======================================================
// Применение через sed (быстро, если нет ручной правки)
// =======================================================
//
// 1. DEFAULT_THEME_ID:
//    sed -i '' 's/export const DEFAULT_THEME_ID: ThemeId = "clean-light";/export const DEFAULT_THEME_ID: ThemeId = "neiry-pulse";/' src/lib/constants.ts
//
// 2. Добавление темы — это вставка в объект, sed-ом не делай. Открой constants.ts,
//    найди `export const THEMES: Record<string, Theme> = {` и добавь после `= {`:
//
//      "neiry-pulse": {
//        id: "neiry-pulse",
//        name: "Neiry Pulse",
//        bg: "#f7f5ef",
//        bgAlt: "#0c0a09",
//        fg: "#0c0a09",
//        fgAlt: "#f7f5ef",
//        accent: "#831843",
//        muted: "#78716c",
//      },
//
// 3. После правки запустить `bun run build` чтобы проверить TS-ошибки. Тип `Theme`
//    определён в `src/lib/types.ts` — проверь, что все обязательные поля есть.
