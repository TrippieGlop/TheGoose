"""Original SVG illustrations for The Goose. Each one is used once per page; gradient IDs are prefixed per piece."""

INK = "#241811"

# ---------------------------------------------------------------- 1. Home hero: a long Italian hoagie in deli paper
HERO_HOAGIE = f"""<svg viewBox="0 0 560 330" role="img" aria-labelledby="hh-t"><title id="hh-t">Illustration of a loaded Italian hoagie wrapped in deli paper</title>
<defs>
<linearGradient id="hh-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ecb86a"/><stop offset=".6" stop-color="#d08a35"/><stop offset="1" stop-color="#a9631f"/></linearGradient>
<linearGradient id="hh-bot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9994a"/><stop offset="1" stop-color="#a5601d"/></linearGradient>
<pattern id="hh-paper" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(-8)"><rect width="22" height="22" fill="#fffaf0"/><rect width="11" height="22" fill="#d6e5bd"/></pattern>
</defs>
<ellipse cx="290" cy="300" rx="235" ry="16" fill="{INK}" opacity=".18"/>
<g stroke="{INK}" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round">
  <!-- bottom roll -->
  <path d="M58 226 C52 262 76 284 118 286 L456 286 C500 284 522 262 514 226 Z" fill="url(#hh-bot)"/>
  <!-- lettuce frill -->
  <path d="M46 222 c10 -12 20 10 32 -2 s20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 32 0 20 12 34 0 L522 240 C420 248 200 236 56 246 Z" fill="#86b84f"/>
  <!-- tomato slices -->
  <g fill="#e2503a"><path d="M92 214 a24 14 0 0 1 48 0 z"/><path d="M196 212 a24 14 0 0 1 48 0 z"/><path d="M300 212 a24 14 0 0 1 48 0 z"/><path d="M404 214 a24 14 0 0 1 48 0 z"/></g>
  <!-- provolone draping -->
  <path d="M56 200 L520 196 L512 214 L486 214 L474 232 L462 212 L370 212 L356 230 L342 210 L250 210 L238 228 L224 208 L132 210 L118 230 L104 210 L64 212 Z" fill="#f6dc7a"/>
  <!-- ham ribbon -->
  <path d="M54 190 c20 -10 40 10 60 0 s40 10 60 0 40 10 60 0 40 10 60 0 40 10 60 0 40 10 60 0 40 10 60 0 40 10 52 0 l2 14 c-20 8 -40 -8 -60 2 s-40 -8 -60 2 -40 -8 -60 2 -40 -8 -60 2 -40 -8 -60 2 -40 -8 -60 2 -40 -8 -60 2 -40 -8 -58 2 z" fill="#f2a3a0"/>
  <!-- folded salami -->
  <g fill="#c2352b"><path d="M70 186 a30 22 0 0 1 60 0 z"/><path d="M122 184 a30 22 0 0 1 60 0 z"/><path d="M174 184 a30 22 0 0 1 60 0 z"/><path d="M226 184 a30 22 0 0 1 60 0 z"/><path d="M278 184 a30 22 0 0 1 60 0 z"/><path d="M330 184 a30 22 0 0 1 60 0 z"/><path d="M382 184 a30 22 0 0 1 60 0 z"/><path d="M434 186 a30 22 0 0 1 60 0 z"/></g>
  <!-- top roll -->
  <path d="M52 168 C42 110 120 58 286 56 C452 58 530 110 520 168 C430 176 142 176 52 168 Z" fill="url(#hh-top)"/>
</g>
<!-- salami fat specks -->
<g fill="#fbe0d8"><circle cx="92" cy="178" r="2.4"/><circle cx="108" cy="174" r="2"/><circle cx="150" cy="176" r="2.4"/><circle cx="200" cy="174" r="2"/><circle cx="214" cy="178" r="2.4"/><circle cx="256" cy="175" r="2.2"/><circle cx="302" cy="176" r="2.4"/><circle cx="318" cy="173" r="2"/><circle cx="358" cy="176" r="2.4"/><circle cx="410" cy="174" r="2"/><circle cx="462" cy="177" r="2.4"/><circle cx="476" cy="173" r="2"/></g>
<!-- tomato seeds -->
<g fill="#ffd9b0"><circle cx="110" cy="208" r="2"/><circle cx="122" cy="208" r="2"/><circle cx="214" cy="206" r="2"/><circle cx="226" cy="206" r="2"/><circle cx="318" cy="206" r="2"/><circle cx="330" cy="206" r="2"/><circle cx="422" cy="208" r="2"/><circle cx="434" cy="208" r="2"/></g>
<!-- score marks + shine + seeds on the roll -->
<g fill="none" stroke="#f6d9a6" stroke-width="5" stroke-linecap="round" opacity=".85"><path d="M168 92 c14 10 22 22 26 36"/><path d="M262 82 c14 10 22 22 26 36"/><path d="M356 86 c14 10 22 22 26 36"/></g>
<path d="M92 132 c24 -34 74 -54 130 -60" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".35"/>
<g fill="#fff6dc" stroke="{INK}" stroke-width="1.4"><ellipse cx="128" cy="140" rx="5" ry="2.8" transform="rotate(-20 128 140)"/><ellipse cx="226" cy="104" rx="5" ry="2.8" transform="rotate(10 226 104)"/><ellipse cx="318" cy="98" rx="5" ry="2.8"/><ellipse cx="420" cy="118" rx="5" ry="2.8" transform="rotate(18 420 118)"/><ellipse cx="472" cy="150" rx="5" ry="2.8" transform="rotate(30 472 150)"/><ellipse cx="200" cy="146" rx="5" ry="2.8" transform="rotate(-8 200 146)"/><ellipse cx="300" cy="150" rx="5" ry="2.8" transform="rotate(14 300 150)"/><ellipse cx="392" cy="150" rx="5" ry="2.8" transform="rotate(-14 392 150)"/></g>
<!-- deli paper wrapped around the left end -->
<path d="M30 92 L150 70 L176 300 L40 296 C24 230 22 160 30 92 Z" fill="url(#hh-paper)" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>
<path d="M150 70 L176 300" stroke="{INK}" stroke-width="4.5"/>
<path d="M150 70 C140 120 168 140 150 190" fill="none" stroke="{INK}" stroke-width="2.5" opacity=".35"/>
<!-- sticker on the paper -->
<g transform="rotate(-8 96 190)"><circle cx="96" cy="190" r="30" fill="#a5382a" stroke="{INK}" stroke-width="4"/><text x="96" y="201" text-anchor="middle" font-family="Yellowtail, cursive" font-size="30" fill="#f7f3e6">G</text></g>
<!-- toothpick with an olive -->
<g stroke="{INK}" stroke-width="4" stroke-linecap="round"><path d="M352 20 L340 120" stroke="#e7c98a" stroke-width="6"/><path d="M352 20 L340 120" fill="none" stroke-width="1.5" opacity=".6"/></g>
<circle cx="350" cy="34" r="15" fill="#5c7a2e" stroke="{INK}" stroke-width="4"/><circle cx="350" cy="34" r="5" fill="#c2352b"/>
<!-- pickle spear in front -->
<g transform="rotate(-14 470 292)"><rect x="408" y="276" width="124" height="30" rx="15" fill="#7e9f3b" stroke="{INK}" stroke-width="4.5"/><g fill="#c6d98e"><circle cx="432" cy="288" r="3"/><circle cx="456" cy="294" r="3"/><circle cx="482" cy="287" r="3"/><circle cx="506" cy="293" r="3"/></g></g>
</svg>"""

# ---------------------------------------------------------------- 2. Space Shuttle Special: hoagie rocket
SHUTTLE = f"""<svg viewBox="-10 0 460 386" role="img" aria-labelledby="sh-t"><title id="sh-t">Illustration of a hoagie blasting off like a rocket</title>
<defs>
<linearGradient id="sh-roll" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ecb86a"/><stop offset="1" stop-color="#b8702a"/></linearGradient>
<linearGradient id="sh-fire" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#fff3c4"/><stop offset=".45" stop-color="#f4c542"/><stop offset="1" stop-color="#e0662f"/></linearGradient>
</defs>
<!-- stars + planet -->
<g fill="#fffdf7" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
  <path d="M232 34 l5 11 12 2 -9 8 2 12 -10 -6 -10 6 2 -12 -9 -8 12 -2z"/>
  <path d="M370 250 l4 8 9 2 -7 6 2 9 -8 -5 -8 5 2 -9 -7 -6 9 -2z"/>
</g>
<g fill="{INK}" opacity=".5"><circle cx="140" cy="40" r="3"/><circle cx="300" cy="30" r="2.5"/><circle cx="40" cy="170" r="2.5"/><circle cx="410" cy="150" r="3"/><circle cx="220" cy="310" r="2.5"/></g>
<g transform="translate(92 86)"><circle r="30" fill="#c8963e" stroke="{INK}" stroke-width="4"/><path d="M-12 -14 a10 10 0 1 0 6 18" fill="none" stroke="{INK}" stroke-width="2.5" opacity=".4"/><ellipse rx="52" ry="12" transform="rotate(-18)" fill="none" stroke="{INK}" stroke-width="4"/><path d="M-30 -4 a30 30 0 0 1 60 0" transform="rotate(-18)" fill="#c8963e" stroke="none"/><path d="M-30 -4 a30 30 0 0 1 60 0" transform="rotate(-18)" fill="none" stroke="{INK}" stroke-width="4"/></g>
<!-- the rocket hoagie, drawn horizontally then tilted -->
<g transform="translate(116 256) rotate(-32)">
  <!-- exhaust flame -->
  <path d="M8 6 C-40 -6 -86 18 -128 40 C-90 44 -60 52 -30 60 C-74 70 -100 90 -120 104 C-70 100 -30 88 8 76 Z" fill="url(#sh-fire)" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
  <path d="M6 22 C-20 22 -44 34 -60 44 C-40 48 -22 54 6 60 Z" fill="#fff3c4" opacity=".9"/>
  <g stroke="{INK}" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round">
    <!-- lettuce fins -->
    <path d="M20 4 C6 -30 18 -54 44 -60 C50 -40 58 -20 64 4 Z" fill="#86b84f"/>
    <path d="M20 78 C6 112 18 134 44 140 C50 120 58 100 64 78 Z" fill="#86b84f"/>
    <!-- bottom roll -->
    <path d="M10 48 L10 80 L250 80 C286 80 304 66 306 48 Z" fill="url(#sh-roll)"/>
    <!-- fillings -->
    <path d="M6 34 L304 34 L306 50 L6 50 Z" fill="#f2a3a0"/>
    <path d="M6 44 c14 8 26 -6 40 2 s26 -6 40 2 26 -6 40 2 26 -6 40 2 26 -6 40 2 26 -6 40 2 26 -6 40 2 l-2 8 L6 54 Z" fill="#f6dc7a"/>
    <path d="M6 26 c12 -8 24 8 36 0 s24 8 36 0 24 8 36 0 24 8 36 0 24 8 36 0 24 8 36 0 24 8 36 0 24 8 36 0 l2 10 L6 36 Z" fill="#86b84f"/>
    <!-- top roll / nose cone -->
    <path d="M8 30 L8 0 C8 -8 14 -12 24 -12 L230 -12 C282 -12 316 4 330 30 Z" fill="url(#sh-roll)"/>
    <!-- pepperoni porthole -->
    <circle cx="180" cy="8" r="17" fill="#c2352b"/>
    <circle cx="180" cy="8" r="9" fill="#9fd3e0"/>
    <!-- nose stripe -->
    <path d="M276 -8 C288 2 296 14 300 30" fill="none" stroke="#a5382a" stroke-width="9"/>
  </g>
  <path d="M174 3 l6 -4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
  <g fill="#fff6dc" stroke="{INK}" stroke-width="1.3"><ellipse cx="60" cy="0" rx="4.5" ry="2.5"/><ellipse cx="104" cy="-4" rx="4.5" ry="2.5"/><ellipse cx="230" cy="0" rx="4.5" ry="2.5"/><ellipse cx="260" cy="10" rx="4.5" ry="2.5"/><ellipse cx="130" cy="14" rx="4.5" ry="2.5"/></g>
  <path d="M40 -4 c40 -6 80 -6 110 -4" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".35"/>
  <!-- speed lines -->
  <g stroke="{INK}" stroke-width="4" stroke-linecap="round"><path d="M-40 -40 h-40"/><path d="M-20 -60 h-30"/><path d="M-50 130 h-36"/></g>
</g>
</svg>"""

# ---------------------------------------------------------------- 3. Menu hero: triple-decker club quarters
def _club_wedge(x, y, s, frill, gid):
    """A club-sandwich quarter standing on its cut edge: layered triangle with a frilled toothpick."""
    layers = [("#e8c48a", 16), ("#86b84f", 8), ("#e2503a", 9), ("#f3cfa6", 12), ("#f6e3b8", 14), ("#b2472f", 8), ("#f6dc7a", 9), ("#f2a3a0", 11), ("#e8c48a", 16)]
    bands, yy = [], 30
    for color, h in layers:
        bands.append(f'<rect x="0" y="{yy}" width="220" height="{h}" fill="{color}"/>')
        yy += h
    tri = "M110 0 L218 140 L2 140 Z"
    return f"""<g transform="translate({x} {y}) scale({s})">
<clipPath id="{gid}"><path d="{tri}"/></clipPath>
<g clip-path="url(#{gid})"><rect x="0" y="0" width="220" height="30" fill="#e8c48a"/>{''.join(bands)}<rect x="0" y="{yy}" width="220" height="40" fill="#e8c48a"/>
<g stroke="{INK}" stroke-width="2" opacity=".35"><path d="M0 46 H220"/><path d="M0 80 H220"/><path d="M0 108 H220"/></g></g>
<path d="{tri}" fill="none" stroke="#a9631f" stroke-width="12" stroke-linejoin="round"/>
<path d="{tri}" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>
<path d="M110 -64 L110 70" stroke="#e7c98a" stroke-width="5" stroke-linecap="round"/><path d="M110 -64 L110 70" stroke="{INK}" stroke-width="1.4" opacity=".6"/>
<g fill="{frill}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"><path d="M110 -66 l-14 -16 6 -2 -10 -10 8 0 -4 -12 10 6 4 -12 4 12 10 -6 -4 12 8 0 -10 10 6 2 -14 16 z"/></g>
</g>"""

CLUB = f"""<svg viewBox="0 -34 440 364" aria-hidden="true">
<ellipse cx="220" cy="300" rx="196" ry="22" fill="#fffdf7" stroke="{INK}" stroke-width="4.5"/>
<ellipse cx="220" cy="296" rx="160" ry="12" fill="#efe8d4"/>
{_club_wedge(40, 120, 1.0, "#8fb36a", "cl-a")}
{_club_wedge(190, 90, 1.12, "#a5382a", "cl-b")}
<g stroke="{INK}" stroke-width="3.5"><circle cx="86" cy="286" r="11" fill="#e2503a"/><circle cx="356" cy="284" r="9" fill="#5c7a2e"/></g>
<g transform="rotate(-10 380 280)"><rect x="338" y="268" width="78" height="22" rx="11" fill="#7e9f3b" stroke="{INK}" stroke-width="4"/></g>
</svg>"""

# ---------------------------------------------------------------- 4. Catering platter
def _mini_sub(x, y, r=0):
    return f"""<g transform="translate({x} {y}) rotate({r})" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round">
<path d="M-38 6 C-40 20 -30 26 -18 26 L18 26 C30 26 40 20 38 6 Z" fill="#d08a35"/>
<path d="M-42 0 c8 -6 14 6 22 0 s14 6 22 0 14 6 22 0 14 6 22 0 l0 10 L-42 10 Z" fill="#86b84f"/>
<path d="M-40 -4 L40 -4 L42 6 L-42 6 Z" fill="#f2a3a0"/>
<path d="M-38 -4 C-42 -26 -20 -34 0 -34 C20 -34 42 -26 38 -4 Z" fill="#e5a858"/>
<path d="M-24 -22 c8 -6 18 -8 26 -8" fill="none" stroke="#fff" stroke-width="3" opacity=".4"/>
</g>"""

def _pinwheel(x, y, rot=0):
    return f"""<g transform="translate({x} {y}) rotate({rot})">
<ellipse rx="24" ry="17" fill="#f6efd9" stroke="{INK}" stroke-width="3.5"/>
<path d="M0 0 c6 0 7 -6 3 -8 c-8 -4 -14 4 -12 10 c3 9 16 10 21 2 c6 -10 -2 -21 -13 -21 c-12 0 -20 10 -18 20" fill="none" stroke="#e98b8b" stroke-width="4" stroke-linecap="round"/>
<path d="M2 3 c-6 6 -18 2 -18 -6" fill="none" stroke="#86b84f" stroke-width="3" stroke-linecap="round"/>
</g>"""

def _cube(x, y, c1, c2, c3):
    return f"""<g transform="translate({x} {y})" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
<path d="M0 -10 L12 -4 L0 2 L-12 -4 Z" fill="{c1}"/><path d="M-12 -4 L0 2 L0 14 L-12 8 Z" fill="{c2}"/><path d="M12 -4 L0 2 L0 14 L12 8 Z" fill="{c3}"/></g>"""

PLATTER = f"""<svg viewBox="0 0 440 300" role="img" aria-labelledby="pl-t"><title id="pl-t">Illustration of a catering platter with mini hoagies, pinwheels, cheese, grapes and tomatoes</title>
<ellipse cx="220" cy="246" rx="206" ry="40" fill="{INK}" opacity=".16"/>
<ellipse cx="220" cy="170" rx="204" ry="104" fill="#2e2620" stroke="{INK}" stroke-width="5"/>
<ellipse cx="220" cy="164" rx="186" ry="90" fill="#3b3129"/>
<path d="M60 128 C100 92 170 76 230 76" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".14"/>
<!-- lettuce bed -->
<g fill="#86b84f" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
<path d="M70 150 c10 -26 40 -40 66 -36 c-4 20 -26 40 -66 36z"/><path d="M300 102 c26 -8 56 4 70 24 c-24 6 -54 -2 -70 -24z"/><path d="M130 220 c10 -18 34 -26 54 -20 c-8 16 -30 26 -54 20z"/>
</g>
<!-- back row: mini hoagies -->
{_mini_sub(150, 112, -6)}{_mini_sub(232, 98, 0)}{_mini_sub(312, 112, 6)}
<!-- middle: pinwheels -->
{_pinwheel(118, 168, -10)}{_pinwheel(178, 170, 4)}{_pinwheel(240, 172, -4)}
<!-- cheese cubes -->
{_cube(300, 166, "#f9e08a", "#e9c450", "#d8ad35")}{_cube(324, 176, "#fbf0c8", "#efdc98", "#ddc678")}{_cube(312, 192, "#f6b45a", "#e39a3c", "#c9822f")}{_cube(340, 158, "#f9e08a", "#e9c450", "#d8ad35")}
<!-- grapes -->
<g fill="#8a4f8c" stroke="{INK}" stroke-width="2.6"><circle cx="356" cy="196" r="9"/><circle cx="372" cy="186" r="9"/><circle cx="370" cy="204" r="9"/><circle cx="386" cy="196" r="9"/><circle cx="384" cy="213" r="8"/></g>
<g fill="#fff" opacity=".45"><circle cx="353" cy="193" r="2.5"/><circle cx="369" cy="183" r="2.5"/><circle cx="383" cy="193" r="2.5"/></g>
<path d="M378 178 c2 -8 8 -12 14 -12" fill="none" stroke="#5c7a2e" stroke-width="3.5" stroke-linecap="round"/>
<!-- front: cherry tomatoes, olives, parsley -->
<g stroke="{INK}" stroke-width="3"><circle cx="168" cy="218" r="11" fill="#e2503a"/><circle cx="196" cy="226" r="11" fill="#e2503a"/><circle cx="262" cy="214" r="11" fill="#e2503a"/></g>
<g fill="#5c7a2e" stroke="{INK}" stroke-width="2"><path d="M168 207 l-4 -4 4 1 3 -4 1 5 4 0z"/><path d="M196 215 l-4 -4 4 1 3 -4 1 5 4 0z"/><path d="M262 203 l-4 -4 4 1 3 -4 1 5 4 0z"/></g>
<g fill="#fff" opacity=".5"><circle cx="164" cy="214" r="2.5"/><circle cx="192" cy="222" r="2.5"/><circle cx="258" cy="210" r="2.5"/></g>
<g stroke="{INK}" stroke-width="3"><ellipse cx="226" cy="226" rx="9" ry="7" fill="#2b2b2b"/><ellipse cx="290" cy="222" rx="9" ry="7" fill="#2b2b2b"/><ellipse cx="96" cy="196" rx="9" ry="7" fill="#5c7a2e"/></g>
<g fill="#3b3129"><circle cx="226" cy="226" r="3"/><circle cx="290" cy="222" r="3"/></g><circle cx="96" cy="196" r="3" fill="#c2352b"/>
<g fill="#5c9a3a"><circle cx="126" cy="206" r="5"/><circle cx="134" cy="200" r="4"/><circle cx="120" cy="198" r="4"/><circle cx="330" cy="222" r="5"/><circle cx="338" cy="216" r="4"/><circle cx="324" cy="215" r="4"/></g>
<!-- serving pick flag -->
<g transform="rotate(8 232 60)"><path d="M232 98 L232 44" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/><path d="M232 44 L264 52 L232 62 Z" fill="#a5382a" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><text x="239" y="58" font-family="Yellowtail, cursive" font-size="12" fill="#f7f3e6">G</text></g>
</svg>"""

# ---------------------------------------------------------------- 5. The goose (story section)
GOOSE = f"""<svg viewBox="0 0 400 500" role="img" aria-labelledby="gs-t"><title id="gs-t">Illustration of a friendly goose in a paper deli cap, holding a hoagie</title>
<rect width="400" height="500" fill="#3d5a2b"/>
<circle cx="200" cy="330" r="190" fill="#557a3a"/>
<circle cx="200" cy="330" r="152" fill="none" stroke="#b5cf91" stroke-width="2" stroke-dasharray="4 10" opacity=".6"/>
<text x="200" y="84" text-anchor="middle" font-family="Yellowtail, cursive" font-size="52" fill="#e7c98a" transform="rotate(-6 200 84)">since forever</text>
<!-- body + neck + head, outline pass then fill pass so they merge into one silhouette -->
<g stroke="{INK}" stroke-width="12" stroke-linejoin="round">
  <ellipse cx="200" cy="476" rx="168" ry="110" fill="#fffdf7"/>
  <path d="M168 400 C170 340 194 300 206 262 L280 262 C276 300 262 340 270 400 Z" fill="#fffdf7"/>
  <circle cx="240" cy="210" r="64" fill="#fffdf7"/>
</g>
<g fill="#fffdf7">
  <ellipse cx="200" cy="476" rx="168" ry="110"/>
  <path d="M168 400 C170 340 194 300 206 262 L280 262 C276 300 262 340 270 400 Z"/>
  <circle cx="240" cy="210" r="64"/>
</g>
<!-- soft shading -->
<path d="M196 168 c-10 30 -6 70 18 96" fill="none" stroke="#e9e2cf" stroke-width="14" stroke-linecap="round" opacity=".8"/>
<!-- beak, attached to the head -->
<g stroke="{INK}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
  <path d="M290 200 C316 190 346 194 368 208 C346 216 318 218 292 216 Z" fill="#e8a33a"/>
  <path d="M292 218 C316 222 338 222 352 218 C340 232 316 236 294 228 Z" fill="#d48a26"/>
  <circle cx="294" cy="200" r="10" fill="#e8a33a"/>
</g>
<path d="M310 202 c10 -2 20 -1 30 2" fill="none" stroke="#fff3c4" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<!-- eye + blush -->
<circle cx="262" cy="188" r="9" fill="{INK}"/><circle cx="265" cy="185" r="3" fill="#fff"/>
<path d="M248 172 q12 -8 24 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="258" cy="222" rx="13" ry="7" fill="#f0a3a0" opacity=".7"/>
<!-- paper deli cap -->
<g transform="rotate(-10 236 150)" stroke="{INK}" stroke-width="5" stroke-linejoin="round">
  <path d="M184 160 L196 118 C222 106 254 106 280 116 L292 158 C258 148 218 148 184 160 Z" fill="#fffaf0"/>
  <path d="M188 146 C222 136 256 136 288 144 L292 158 C258 148 218 148 184 160 Z" fill="#8fb36a"/>
  <text x="238" y="138" text-anchor="middle" font-family="Yellowtail, cursive" font-size="24" fill="#a5382a" stroke="none">G</text>
</g>
<!-- hoagie tucked under the wing -->
<g transform="translate(70 386) rotate(-8)" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round">
  <path d="M0 40 C-2 58 14 66 34 66 L190 66 C210 66 222 56 220 40 Z" fill="#c07a2e"/>
  <path d="M-6 36 c10 -8 18 8 28 0 s18 8 28 0 18 8 28 0 18 8 28 0 18 8 28 0 18 8 28 0 18 8 28 0 18 8 28 0 l0 12 L-6 48 Z" fill="#86b84f"/>
  <path d="M-4 26 L224 26 L226 40 L-6 40 Z" fill="#f2a3a0"/>
  <g fill="#c2352b"><path d="M16 28 a18 12 0 0 1 36 0z"/><path d="M76 28 a18 12 0 0 1 36 0z"/><path d="M136 28 a18 12 0 0 1 36 0z"/></g>
  <path d="M0 28 C-6 -6 60 -16 110 -16 C160 -16 228 -6 222 28 Z" fill="#e0a456"/>
</g>
<path d="M120 380 c30 -10 70 -10 90 0" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".4"/>
<!-- wing over the hoagie -->
<path d="M150 428 C178 400 250 396 300 420 C330 436 336 470 314 488 C278 480 214 470 160 470 C138 460 136 442 150 428 Z" fill="#fffdf7" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<g fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round" opacity=".55"><path d="M196 446 c30 -6 60 -4 90 6"/><path d="M206 462 c26 -2 50 0 76 8"/></g>
</svg>"""

# ---------------------------------------------------------------- 6. Gander Room chandelier
def _candle(x, y):
    return f"""<g transform="translate({x} {y})">
<circle cy="-30" r="22" fill="url(#ch-glow)"/>
<path d="M-10 0 C-10 8 10 8 10 0 Z" fill="#c8963e" stroke="{INK}" stroke-width="2"/>
<ellipse cy="0" rx="14" ry="4" fill="#e7c98a" stroke="{INK}" stroke-width="2"/>
<rect x="-5" y="-22" width="10" height="22" rx="2" fill="#fffaf0" stroke="{INK}" stroke-width="2"/>
<path d="M0 -40 C6 -32 6 -26 0 -24 C-6 -26 -6 -32 0 -40 Z" fill="#ffd36a" stroke="#c8963e" stroke-width="1.5"/>
<path d="M0 -34 C2 -30 2 -28 0 -27 C-2 -28 -2 -30 0 -34 Z" fill="#fff8dc"/>
<path d="M0 6 L0 14" stroke="#e7c98a" stroke-width="1.5"/>
<path d="M0 14 C4 20 4 26 0 30 C-4 26 -4 20 0 14 Z" fill="#eaf2ff" stroke="#c8963e" stroke-width="1.5" opacity=".95"/>
</g>"""

def _arm(side, path):
    return f'<path d="{path}" transform="{"" if side > 0 else "translate(360 0) scale(-1 1)"}"/>'

_ARMS = [
    # lower tier: long sweeping S-scrolls
    "M188 236 C230 240 262 232 280 214 C292 202 304 196 318 200 C326 202 328 212 320 214 C314 216 310 210 314 206",
    "M186 228 C214 226 232 214 240 196 C246 184 254 178 262 182",
    # upper tier
    "M184 168 C206 170 222 160 228 146 C232 136 240 132 248 136 C254 140 252 148 246 148",
]

CHANDELIER = f"""<svg viewBox="0 0 360 380" role="img" aria-labelledby="ch-t"><title id="ch-t">Illustration of an ornate gold chandelier with candles and crystals</title>
<defs>
<radialGradient id="ch-glow"><stop offset="0" stop-color="#ffe39a" stop-opacity=".75"/><stop offset="1" stop-color="#ffe39a" stop-opacity="0"/></radialGradient>
<radialGradient id="ch-halo" cx="50%" cy="55%" r="50%"><stop offset="0" stop-color="#f7d98c" stop-opacity=".22"/><stop offset="1" stop-color="#f7d98c" stop-opacity="0"/></radialGradient>
<linearGradient id="ch-gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9c6e24"/><stop offset=".45" stop-color="#f0cf86"/><stop offset="1" stop-color="#a87a2c"/></linearGradient>
</defs>
<ellipse cx="180" cy="210" rx="176" ry="150" fill="url(#ch-halo)"/>
<!-- ceiling canopy + chain -->
<path d="M150 0 L210 0 C206 12 196 18 180 18 C164 18 154 12 150 0 Z" fill="url(#ch-gold)" stroke="{INK}" stroke-width="2.5"/>
<g fill="none" stroke="#e7c98a" stroke-width="3.5"><ellipse cx="180" cy="28" rx="5" ry="9"/><ellipse cx="180" cy="44" rx="3" ry="9" stroke="#c8963e"/><ellipse cx="180" cy="60" rx="5" ry="9"/><ellipse cx="180" cy="76" rx="3" ry="9" stroke="#c8963e"/></g>
<!-- crown -->
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
<path d="M150 112 L146 92 L160 102 L170 86 L180 100 L190 86 L200 102 L214 92 L210 112 Z" fill="url(#ch-gold)"/>
<circle cx="146" cy="92" r="4" fill="#eaf2ff"/><circle cx="170" cy="86" r="4" fill="#eaf2ff"/><circle cx="190" cy="86" r="4" fill="#eaf2ff"/><circle cx="214" cy="92" r="4" fill="#eaf2ff"/>
<rect x="146" y="110" width="68" height="8" rx="3" fill="#c8963e"/>
</g>
<!-- garland swags of crystal beads -->
<g fill="none" stroke="#eaf2ff" stroke-width="5" stroke-linecap="round" stroke-dasharray="0 9" opacity=".95">
<path d="M150 118 C120 150 74 168 44 198"/><path d="M210 118 C240 150 286 168 316 198"/>
<path d="M60 228 C110 270 250 270 300 228"/><path d="M104 196 C140 226 220 226 256 196"/>
</g>
<!-- arms (mirrored) -->
<g fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round">{''.join(_arm(s, p) for p in _ARMS for s in (1, -1))}</g>
<g fill="none" stroke="url(#ch-gold)" stroke-width="5" stroke-linecap="round">{''.join(_arm(s, p) for p in _ARMS for s in (1, -1))}</g>
<!-- central baluster -->
<g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
<path d="M172 118 L188 118 L192 140 C206 150 206 170 192 180 L196 198 C214 206 214 236 196 246 L190 262 L170 262 L164 246 C146 236 146 206 164 198 L168 180 C154 170 154 150 168 140 Z" fill="url(#ch-gold)"/>
<ellipse cx="180" cy="160" rx="16" ry="5" fill="#f0cf86"/><ellipse cx="180" cy="222" rx="22" ry="6" fill="#f0cf86"/>
<path d="M170 262 L190 262 L186 280 L174 280 Z" fill="#c8963e"/>
</g>
<!-- bottom finial crystal -->
<path d="M180 280 L180 292" stroke="#e7c98a" stroke-width="2"/>
<path d="M180 292 C194 310 194 330 180 352 C166 330 166 310 180 292 Z" fill="#eaf2ff" stroke="#c8963e" stroke-width="2"/>
<path d="M180 300 C186 312 186 324 180 336" fill="none" stroke="#fff" stroke-width="2.5" opacity=".9"/>
<!-- candles at the arm tips -->
{_candle(314, 206)}{_candle(46, 206)}{_candle(262, 180)}{_candle(98, 180)}{_candle(246, 146)}{_candle(114, 146)}
<!-- hanging crystals between the swags -->
<g fill="#eaf2ff" stroke="#c8963e" stroke-width="1.5">
<path d="M128 252 C134 260 134 268 128 274 C122 268 122 260 128 252 Z"/><path d="M232 252 C238 260 238 268 232 274 C226 268 226 260 232 252 Z"/>
<path d="M156 262 C161 269 161 276 156 281 C151 276 151 269 156 262 Z"/><path d="M204 262 C209 269 209 276 204 281 C199 276 199 269 204 262 Z"/>
</g>
<g fill="#fff" opacity=".9"><circle cx="70" cy="120" r="1.8"/><circle cx="292" cy="110" r="2.2"/><circle cx="40" cy="300" r="1.6"/><circle cx="326" cy="300" r="2"/><circle cx="110" cy="340" r="1.6"/><circle cx="250" cy="346" r="1.8"/></g>
</svg>"""
