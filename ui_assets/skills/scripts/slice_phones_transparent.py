#!/usr/bin/env python3
"""V2.1 SLICING — transparent PNG, no drop-shadow on phone.
Each output PNG has alpha channel: only phone bezel + interface, surrounding fully transparent.
"""
import re, shutil, subprocess, os

SRC_DIR = "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/docs_web/wireframes/m3"
OUT_DIR = "/tmp/sliced-phones-transparent"
DEST = "/Users/solomono/Desktop/NOW/ПРОЕКТЫ/NEIRY/UI_assets/screenshots/sliced-flow-v2-1-transparent-2026-06-14"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(DEST, exist_ok=True)

# CSS injection — transparent bg + remove outer drop-shadow on device-frame (keep bezel rings)
HIDE_CHROME_CSS = """
<style>
  html, body { background: transparent !important; padding: 0 !important; margin: 0 !important; width: 460px !important; height: 920px !important; overflow: hidden !important; }
  body > * { display: none !important; }
  body > main, body > div, body > article, body > section { display: block !important; }
  .page-title, .doc-title, .frame-caption, .page-header, .page-sub,
  body > h1, body > h2, body > p, body > header,
  .poster-meta, .poster-header, .sub-title, .legend, .caption-strip,
  .footer, .meta-bar, .doc-footer, .doc-meta, .meta {
    display: none !important;
  }
  .frames-row, .frames-strip, main, body > div, body > main, body > article, body > section {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 460px !important;
    height: 920px !important;
    background: transparent !important;
    overflow: visible !important;
    gap: 0 !important;
    scroll-snap-type: none !important;
  }
  .frame-with-caption, .frame-wrap {
    padding: 0 !important;
    margin: 0 !important;
    background: transparent !important;
    flex: 0 0 auto !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
  }
  /* Device-frame: keep bezel rings, REMOVE outer drop-shadow */
  .device-frame {
    margin: 0 auto !important;
    flex-shrink: 0 !important;
    box-shadow:
      0 0 0 10px #1a1814,
      0 0 0 11px #2a2620 !important;
  }
</style>
</head>
"""

def find_div_blocks(html, class_name):
    blocks = []
    pattern = re.compile(r'<div\s+class="' + re.escape(class_name) + r'"[^>]*>', re.IGNORECASE)
    for m in pattern.finditer(html):
        start = m.start()
        depth = 1
        i = m.end()
        while i < len(html) and depth > 0:
            next_open = html.find('<div', i)
            next_close = html.find('</div>', i)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                i = next_open + 4
            else:
                depth -= 1
                i = next_close + 6
        if depth == 0:
            blocks.append((start, i))
    return blocks

def slice_clean(src_path, idx, total, class_name, out_html):
    html = open(src_path, encoding='utf-8').read()
    blocks = find_div_blocks(html, class_name)
    if len(blocks) != total:
        raise ValueError(f"Expected {total} {class_name} blocks, found {len(blocks)} in {src_path}")
    for j in reversed(range(total)):
        if j == idx:
            continue
        start, end = blocks[j]
        html = html[:start] + html[end:]
    html = html.replace("</head>", HIDE_CHROME_CSS)
    open(out_html, 'w', encoding='utf-8').write(html)

def shoot_transparent(html_path, png_path, w=460, h=920):
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [chrome, "--headless", "--disable-gpu", "--no-sandbox",
           "--default-background-color=00000000",
           f"--window-size={w},{h}",
           f"--screenshot={png_path}",
           f"file://{html_path}"]
    subprocess.run(cmd, capture_output=True, timeout=30)

# Training Start — 5 frames: step1, step2-searching, step2-ready, goal-time, goal-distance
src = f"{SRC_DIR}/mobile-training-start-v0.html"
ts_frames = [
    (0, "02a-training-start-step1"),
    (1, "02b-training-start-step2-searching"),
    (2, "02b-training-start-step2"),  # ready — replaces old 02b PNG (existing name)
    (3, "02c-training-start-goal-time"),
    (4, "02c-training-start-goal-distance"),
]
for idx, out_name in ts_frames:
    slice_clean(src, idx, 5, "frame-with-caption", f"{OUT_DIR}/ts-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/ts-{idx}.html", f"{DEST}/{out_name}.png")
print("Training Start (5 frames): done")

# Training Start · Corner cases — 4 frames: pulse timeout, battery low, BT disconnect, GPS not found
src = f"{SRC_DIR}/mobile-state-training-start-corner-cases-v0.html"
tsc_frames = [
    (0, "02d-state-training-start-pulse-timeout"),
    (1, "02d-state-training-start-battery-low"),
    (2, "02d-state-training-start-bt-disconnect"),
    (3, "02d-state-training-start-gps-not-found"),
]
for idx, out_name in tsc_frames:
    slice_clean(src, idx, 4, "frame-with-caption", f"{OUT_DIR}/tsc-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/tsc-{idx}.html", f"{DEST}/{out_name}.png")
print("Training Start · Corner cases (4 frames): done")

# Training Active — 5 frames: PAGE 1 main, PAGE 1 vTemp, PAGE 2, PAGE 3, Explainer modal
src = f"{SRC_DIR}/mobile-training-active-v0.html"
ta_frames = [
    (0, "03a-training-active-page1-zones"),
    (1, "03a-training-active-page1-zones-vtemp"),
    (2, "03b-training-active-page2-details"),
    (3, "03c-training-active-page3-map"),
    (4, "03d-training-active-zones-explainer"),
]
for idx, out_name in ta_frames:
    slice_clean(src, idx, 5, "frame-with-caption", f"{OUT_DIR}/ta-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/ta-{idx}.html", f"{DEST}/{out_name}.png")
print("Training Active (5 frames): done")

# Health Sharing
src = f"{SRC_DIR}/mobile-health-sharing-v0.html"
for i, name in enumerate(['main', 'generate-qr', 'scan-qr', 'success', 'detail']):
    slice_clean(src, i, 5, "frame-wrap", f"{OUT_DIR}/hs-{i}.html")
    letter = 'abcde'[i]
    shoot_transparent(f"{OUT_DIR}/hs-{i}.html", f"{DEST}/07{letter}-hs-{name}.png")
print("Health Sharing: done")

# Singles
SINGLES = [
    ("mobile-home-f1-v0.html", "01-home.png"),
    ("mobile-history-v0.html", "04-history.png"),
    ("mobile-session-detail-v0.html", "05-session-detail.png"),
    ("mobile-settings-v0.html", "06-settings.png"),
]
for filename, out_name in SINGLES:
    src = f"{SRC_DIR}/{filename}"
    html = open(src, encoding='utf-8').read()
    html = html.replace("</head>", HIDE_CHROME_CSS)
    tmp = f"{OUT_DIR}/{filename}"
    open(tmp, 'w', encoding='utf-8').write(html)
    shoot_transparent(tmp, f"{DEST}/{out_name}")
print("Singles: done")

# Empty States (A5) — 2 phone frames in one HTML (.frame-with-caption)
src = f"{SRC_DIR}/mobile-onboarding-05-empty-states-v0.html"
slice_clean(src, 0, 2, "frame-with-caption", f"{OUT_DIR}/es-1.html")
shoot_transparent(f"{OUT_DIR}/es-1.html", f"{DEST}/12a-home-first-run-empty.png")
slice_clean(src, 1, 2, "frame-with-caption", f"{OUT_DIR}/es-2.html")
shoot_transparent(f"{OUT_DIR}/es-2.html", f"{DEST}/12b-hs-main-empty.png")
print("Empty States: done")

# Permission Denied — 2 frames: 14a Camera + 14b Location (training-start pulse-hero variant)
src = f"{SRC_DIR}/mobile-state-permission-denied-v0.html"
slice_clean(src, 0, 2, "frame-with-caption", f"{OUT_DIR}/pd-1.html")
shoot_transparent(f"{OUT_DIR}/pd-1.html", f"{DEST}/14a-state-camera-denied.png")
slice_clean(src, 1, 2, "frame-with-caption", f"{OUT_DIR}/pd-2.html")
shoot_transparent(f"{OUT_DIR}/pd-2.html", f"{DEST}/14b-state-location-denied.png")
print("Permission Denied: done")

# Training Active · Corner cases — 3 frames: 15a stop-confirm, 15b auto-pause, 15c gps-lost
src = f"{SRC_DIR}/mobile-state-training-active-corner-cases-v0.html"
tacc = [
    (0, "15a-state-stop-confirm"),
    (1, "15b-state-auto-pause"),
    (2, "15c-state-gps-lost"),
]
for idx, out_name in tacc:
    slice_clean(src, idx, 3, "frame-with-caption", f"{OUT_DIR}/tacc-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/tacc-{idx}.html", f"{DEST}/{out_name}.png")
print("Training Active · Corner cases (3 frames): done")

# Settings Detail — 4 frames: 21a BT pairing, 21b Notifications, 21c Privacy, 21d Калибровка
src = f"{SRC_DIR}/mobile-settings-detail-v0.html"
sd_frames = [
    (0, "21a-settings-bt-pairing"),
    (1, "21b-settings-notifications"),
    (2, "21c-settings-privacy"),
    (3, "21d-settings-calibration"),
]
for idx, out_name in sd_frames:
    slice_clean(src, idx, 4, "frame-with-caption", f"{OUT_DIR}/sd-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/sd-{idx}.html", f"{DEST}/{out_name}.png")
print("Settings Detail (4 frames): done")

# End-of-session + Bracelet-disconnect — 3 frames: 16a end-of-session, 16b bracelet-disconnect, 16c close-confirm
src = f"{SRC_DIR}/mobile-state-end-of-session-bracelet-disconnect-v0.html"
eob_frames = [
    (0, "16a-state-end-of-session"),
    (1, "16b-state-bracelet-disconnect-training"),
    (2, "16c-state-close-confirm"),
]
for idx, out_name in eob_frames:
    slice_clean(src, idx, 3, "frame-with-caption", f"{OUT_DIR}/eob-{idx}.html")
    shoot_transparent(f"{OUT_DIR}/eob-{idx}.html", f"{DEST}/{out_name}.png")
print("End-of-session + Bracelet (3 frames): done")

# Verify
for f in sorted(os.listdir(DEST)):
    if not f.endswith('.png'):
        continue
    fp = f"{DEST}/{f}"
    print(f"  {f}: {os.path.getsize(fp)} bytes")
