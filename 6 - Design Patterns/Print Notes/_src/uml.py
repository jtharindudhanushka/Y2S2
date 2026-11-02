"""Tiny UML -> SVG helper for the print notes (black and white).

Member prefixes:  '_' = static (underlined)   '*' = abstract (italic)
"""
import html

LH = 13          # member line height
CW = 6.7          # monospace char width at 10.5px (Courier-safe)
NW = 7.2         # bold name char width at 12px


def esc(s):
    return html.escape(s, quote=False)


class Box:
    def __init__(s, d, name, x, y, w=None, attrs=(), ops=(), stereo=None, abstract=False, fill='#fff'):
        s.d, s.name, s.x, s.y, s.stereo, s.abstract, s.fill = d, name, x, y, stereo, abstract, fill
        s.attrs = list(attrs) if attrs is not None else None
        s.ops = list(ops) if ops is not None else None
        longest = max([len(m.lstrip('_*')) for m in (s.attrs or []) + (s.ops or [])] + [0])
        s.w = w or max(longest * CW + 14, len(name) * NW + 18, (len(stereo) + 2) * 6 + 14 if stereo else 0)
        s.head = 30 if stereo else 20
        s.h = s.head + (len(s.attrs) * LH + 6 if s.attrs is not None else 0) + (len(s.ops) * LH + 6 if s.ops is not None else 0)
        if s.attrs is not None and not s.attrs: s.h += 6
        if s.ops is not None and not s.ops: s.h += 6

    @property
    def cx(s): return s.x + s.w / 2
    @property
    def cy(s): return s.y + s.h / 2
    def top(s, dx=0): return (s.cx + dx, s.y)
    def bottom(s, dx=0): return (s.cx + dx, s.y + s.h)
    def left(s, dy=0): return (s.x, s.cy + dy)
    def right(s, dy=0): return (s.x + s.w, s.cy + dy)

    def svg(s):
        o = [f'<rect x="{s.x}" y="{s.y}" width="{s.w:.0f}" height="{s.h:.0f}" fill="{s.fill}" stroke="#000" stroke-width="1.3"/>']
        ty = s.y + 14
        if s.stereo:
            o.append(f'<text x="{s.cx:.0f}" y="{ty}" font-size="9.5" text-anchor="middle">&#171;{esc(s.stereo)}&#187;</text>')
            ty += 12
        st = ' font-style="italic"' if s.abstract else ''
        o.append(f'<text x="{s.cx:.0f}" y="{ty+1}" font-size="12" font-weight="bold" text-anchor="middle"{st}>{esc(s.name)}</text>')
        yy = s.y + s.head
        for sect in (s.attrs, s.ops):
            if sect is None: continue
            o.append(f'<line x1="{s.x}" y1="{yy}" x2="{s.x+s.w:.0f}" y2="{yy}" stroke="#000" stroke-width="0.9"/>')
            yy += 3
            for m in sect:
                deco = ''
                if m.startswith('_'): deco += ' text-decoration="underline"'; m = m[1:]
                if m.startswith('*'): deco += ' font-style="italic"'; m = m[1:]
                o.append(f'<text x="{s.x+5}" y="{yy+10}" font-size="10.5" class="m"{deco}>{esc(m)}</text>')
                yy += LH
            yy += 3 if sect else 6
        return '\n'.join(o)


class D:
    def __init__(s, width, minh=0):
        s.W, s.items, s.boxes, s.maxy, s.minh = width, [], [], 0, minh

    def cls(s, name, x, y, **kw):
        b = Box(s, name, x, y, **kw)
        s.boxes.append(b); s.items.append(b)
        s.maxy = max(s.maxy, b.y + b.h)
        return b

    def raw(s, svg, bottom=0):
        s.items.append(svg); s.maxy = max(s.maxy, bottom)

    def text(s, x, y, t, size=10, anchor='start', bold=False, italic=False, mono=False):
        a = (' font-weight="bold"' if bold else '') + (' font-style="italic"' if italic else '') + (' class="m"' if mono else '')
        s.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}"{a}>{esc(t)}</text>', y + 4)

    def note(s, x, y, w, lines, size=9.5):
        h = len(lines) * (size + 3) + 8
        s.raw(f'<path d="M{x},{y} H{x+w-8} L{x+w},{y+8} V{y+h} H{x} Z" fill="#f2f2f2" stroke="#000" stroke-width="0.8"/>'
              f'<path d="M{x+w-8},{y} V{y+8} H{x+w}" fill="none" stroke="#000" stroke-width="0.8"/>', y + h)
        for i, l in enumerate(lines):
            s.raw(f'<text x="{x+5}" y="{y+size+3+i*(size+3)}" font-size="{size}">{esc(l)}</text>')
        return (x, y, w, h)

    def link(s, pts, kind='assoc', label=None, lx=None, ly=None, lsize=9.5, mult=None):
        dash = ' stroke-dasharray="5 3"' if kind in ('realize', 'dep') else ''
        end = {'realize': 'tri', 'inherit': 'tri', 'assoc': 'open', 'dep': 'open', 'trans': 'fill',
               'comp': 'open', 'agg': 'open', 'line': None, 'compn': None, 'aggn': None}[kind]
        start = {'comp': 'dfill', 'compn': 'dfill', 'agg': 'dhol', 'aggn': 'dhol'}.get(kind)
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        me = f' marker-end="url(#m{end})"' if end else ''
        ms = f' marker-start="url(#m{start})"' if start else ''
        s.raw(f'<path d="{d}" fill="none" stroke="#000" stroke-width="1.1"{dash}{me}{ms}/>')
        if label:
            if lx is None:
                (x1, y1), (x2, y2) = pts[0], pts[1]
                lx, ly = (x1 + x2) / 2 + 4, (y1 + y2) / 2 - 4
            s.raw(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="{lsize}" font-style="italic">{esc(label)}</text>')
        if mult:
            mx, my, mt = mult
            s.raw(f'<text x="{mx}" y="{my}" font-size="9.5">{esc(mt)}</text>')

    def tree(s, parent, children, kind='realize', gap=None):
        pb = parent.y + parent.h
        top = min(c.y for c in children)
        bus = pb + (top - pb) / 2 if gap is None else pb + gap
        dash = ' stroke-dasharray="5 3"' if kind == 'realize' else ''
        xs = [c.cx for c in children] + [parent.cx]
        s.raw(f'<path d="M{min(xs):.1f},{bus:.1f} H{max(xs):.1f}" fill="none" stroke="#000" stroke-width="1.1"{dash}/>')
        for c in children:
            s.raw(f'<path d="M{c.cx:.1f},{c.y} V{bus:.1f}" fill="none" stroke="#000" stroke-width="1.1"{dash}/>')
        s.raw(f'<path d="M{parent.cx:.1f},{bus:.1f} V{pb:.1f}" fill="none" stroke="#000" stroke-width="1.1"{dash} marker-end="url(#mtri)"/>')

    # ---- state machine helpers
    def state(s, name, x, y, w=96, h=32, sub=None):
        s.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="#000" stroke-width="1.3"/>', y + h)
        if sub:
            s.raw(f'<text x="{x+w/2}" y="{y+h/2-2}" font-size="11.5" font-weight="bold" text-anchor="middle">{esc(name)}</text>'
                  f'<text x="{x+w/2}" y="{y+h/2+11}" font-size="9" text-anchor="middle" font-style="italic">{esc(sub)}</text>')
        else:
            s.raw(f'<text x="{x+w/2}" y="{y+h/2+4}" font-size="11.5" font-weight="bold" text-anchor="middle">{esc(name)}</text>')
        return {'x': x, 'y': y, 'w': w, 'h': h, 'cx': x + w / 2, 'cy': y + h / 2}

    def initial(s, x, y):
        s.raw(f'<circle cx="{x}" cy="{y}" r="6" fill="#000"/>', y + 6)

    def final(s, x, y):
        s.raw(f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" stroke="#000" stroke-width="1.3"/><circle cx="{x}" cy="{y}" r="4.5" fill="#000"/>', y + 8)

    def svg(s, cls='uml'):
        H = max(s.maxy + 8, s.minh)
        s.W = max([s.W] + [b.x + b.w + 8 for b in s.boxes])
        defs = ('<defs>'
                '<marker id="mtri" markerWidth="13" markerHeight="12" refX="12" refY="6" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L12,6 L0,12 z" fill="#fff" stroke="#000" stroke-width="1.1"/></marker>'
                '<marker id="mopen" markerWidth="12" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L11,5 L0,10" fill="none" stroke="#000" stroke-width="1.1"/></marker>'
                '<marker id="mfill" markerWidth="11" markerHeight="9" refX="10" refY="4.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,4.5 L0,9 z" fill="#000"/></marker>'
                '<marker id="mdfill" markerWidth="16" markerHeight="10" refX="1" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,5 L8,0 L15,5 L8,10 z" fill="#000" stroke="#000"/></marker>'
                '<marker id="mdhol" markerWidth="16" markerHeight="10" refX="1" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,5 L8,0 L15,5 L8,10 z" fill="#fff" stroke="#000"/></marker>'
                '</defs>')
        body = '\n'.join(i if isinstance(i, str) else i.svg() for i in s.items)
        return f'<svg class="{cls}" viewBox="0 0 {s.W} {H:.0f}" xmlns="http://www.w3.org/2000/svg">{defs}\n{body}\n</svg>'


def fig(svg, cap=None, width=None):
    st = f' style="width:{width}"' if width else ''
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<div class="fig"><div{st} class="figw">{svg}</div>{c}</div>'
