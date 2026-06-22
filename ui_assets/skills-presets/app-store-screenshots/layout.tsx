// Neiry Pulse — App Store / Google Play screenshots editor
// Source: UI_assets/skills-presets/app-store-screenshots/layout.tsx
// Applied AFTER `cp -R <SKILL_DIR>/template/. ./` to override skill defaults.
// Swaps Inter → Golos Text (UI/body) + JetBrains Mono (labels/numbers).

import type { Metadata } from "next";
import { Golos_Text, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const golos = Golos_Text({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
  variable: "--font-golos-text",
});

const jetbrains = JetBrains_Mono({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
  variable: "--font-jetbrains-mono",
});

export const metadata: Metadata = {
  title: "Neiry Pulse — Store Screenshots",
  description: "Design and export App Store + Google Play screenshots for Neiry Pulse.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={`${golos.variable} ${jetbrains.variable}`}>
      <body className={golos.className}>{children}</body>
    </html>
  );
}
