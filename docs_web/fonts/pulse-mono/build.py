#!/usr/bin/env python3
"""
Pulse Mono — сборка из JetBrains Mono с плоским нулём.

Что делает: берёт оригинальные статические начертания JetBrains Mono из src/,
удаляет из глифа нуля внутренний контур-точку (получая чистый овал) и
переименовывает семейство в «Pulse Mono». Всё остальное (открытая 4,
геометрия 5/7, кириллица, метрики) остаётся как в оригинале.

Зачем патч, а не CSS: у JetBrains Mono нет OpenType-фичи для плоского нуля
(issue #625 не решён). Доступны только точка (дефолт) и слэш ("zero" 1).
Точка — отдельный 3-й контур глифа; удаляем именно его.

Лицензия: JetBrains Mono под SIL OFL 1.1 без Reserved Font Name —
производная и переименование разрешены. OFL.txt лежит рядом.

Требования: fonttools + brotli (для woff2).  Запуск:  python3 build.py
"""
import array
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
from fontTools.ttLib.tables import ttProgram

WEIGHTS    = ["Regular", "Medium", "SemiBold", "Bold"]
TARGETS    = ["zero", "zero.dnom", "zero.numr", "uni2080.zero", "uni2070.zero"]
NEW_FAMILY = "Pulse Mono"
PS_FAMILY  = "PulseMono"


def _ranges(ends):
    r, s = [], 0
    for e in ends:
        r.append((s, e)); s = e + 1
    return r


def _bbox_area(coords, r):
    pts = [coords[i] for i in range(r[0], r[1] + 1)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))


def remove_dot(glyph, glyf, gname):
    """Удаляет самый маленький центральный контур (точку) из глифа нуля."""
    if glyph.numberOfContours != 3:
        return f"skip {gname}: contours={glyph.numberOfContours}"
    coords, flags, ends = glyph.coordinates, glyph.flags, glyph.endPtsOfContours
    rs = _ranges(ends)
    areas = [_bbox_area(coords, r) for r in rs]
    dot = min(range(3), key=lambda i: areas[i])
    if areas[dot] > 0.30 * max(areas):          # страховка: точка заметно мельче
        return f"skip {gname}: smallest contour not dot-like"
    ds, de = rs[dot]; ndel = de - ds + 1
    keep = [i for i in range(len(coords)) if not (ds <= i <= de)]
    glyph.coordinates = GlyphCoordinates([coords[i] for i in keep])
    glyph.flags = array.array('B', [flags[i] for i in keep])
    glyph.endPtsOfContours = [e if e < ds else e - ndel
                              for i, e in enumerate(ends) if i != dot]
    glyph.numberOfContours = len(glyph.endPtsOfContours)
    p = ttProgram.Program(); p.fromBytecode(b""); glyph.program = p   # сброс хинтинга глифа
    glyph.recalcBounds(glyf)
    return f"ok {gname}: 3→2 контура (удалено {ndel} точек)"


def rename(font):
    for rec in list(font["name"].names):
        s = rec.toUnicode()
        if rec.nameID in (1, 16):
            rec.string = NEW_FAMILY
        elif rec.nameID == 4:
            rec.string = s.replace("JetBrains Mono", NEW_FAMILY)
        elif rec.nameID == 6:
            rec.string = s.replace("JetBrainsMono", PS_FAMILY)


def main():
    for w in WEIGHTS:
        f = TTFont(f"src/JetBrainsMono-{w}.ttf", recalcBBoxes=True)
        glyf = f["glyf"]
        print(f"[{w}]")
        for g in TARGETS:
            if g in glyf:
                print("  ", remove_dot(glyf[g], glyf, g))
        rename(f)
        f.save(f"PulseMono-{w}.ttf")
        f.flavor = "woff2"; f.save(f"PulseMono-{w}.woff2")
        print(f"  → PulseMono-{w}.ttf + .woff2")
    print("Готово.")


if __name__ == "__main__":
    main()
