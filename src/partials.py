# Shared page chrome for The Goose site. build.py composes these into static HTML.
SITE = "https://thegoose-two.vercel.app"

HOAGIE = """<svg viewBox="0 0 420 320" role="img" aria-labelledby="hoagie-t"><title id="hoagie-t">Illustration of a stacked hoagie</title>
<defs>
<linearGradient id="bun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2a85c"/><stop offset=".55" stop-color="#c9822f"/><stop offset="1" stop-color="#9c5e1d"/></linearGradient>
<linearGradient id="bunb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d69a4f"/><stop offset="1" stop-color="#a86623"/></linearGradient>
</defs>
<g stroke="#241811" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
<path d="M48 214c-6 30 22 54 70 56h188c46-2 72-26 66-56z" fill="url(#bunb)"/>
<path d="M40 206c22 12 44-6 66 6s44-8 66 4 44-8 66 4 44-10 66 2 44-6 64 2l-6 20c-20-6-40 6-62-2s-44 8-66-2-44 8-66-2-44 10-66-2-44 6-62-6z" fill="#7fae4d"/>
<path d="M46 190c40 10 290 10 328 0l4 16c-40 12-296 12-336 0z" fill="#f0a3a0"/>
<path d="M50 176c36 8 284 8 320 0l4 16c-40 10-288 10-328 0z" fill="#e7837f"/>
<path d="M70 168l22 34 22-34zM150 168l20 30 20-30zM226 168l22 36 22-36zM304 168l20 30 20-30z" fill="#f4c542"/>
<circle cx="110" cy="164" r="22" fill="#d9442f"/><circle cx="196" cy="166" r="22" fill="#d9442f"/><circle cx="282" cy="164" r="22" fill="#d9442f"/>
<path d="M44 158c-4-60 66-100 166-100s172 40 166 100c-40 12-292 12-332 0z" fill="url(#bun)"/>
<path d="M300 40l-6 104" stroke-width="4"/>
<path d="M300 40l44 12-44 16z" fill="#a5382a"/>
</g>
<g fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".55"><circle cx="110" cy="164" r="12"/><circle cx="196" cy="166" r="12"/><circle cx="282" cy="164" r="12"/></g>
<text x="316" y="61" font-family="Yellowtail, cursive" font-size="18" fill="#f7f3e6">G</text>
<g fill="#fff6dc" stroke="#241811" stroke-width="1.5"><ellipse cx="120" cy="96" rx="6" ry="3.4" transform="rotate(-20 120 96)"/><ellipse cx="160" cy="82" rx="6" ry="3.4" transform="rotate(10 160 82)"/><ellipse cx="208" cy="78" rx="6" ry="3.4"/><ellipse cx="252" cy="84" rx="6" ry="3.4" transform="rotate(-12 252 84)"/><ellipse cx="100" cy="124" rx="6" ry="3.4" transform="rotate(14 100 124)"/><ellipse cx="146" cy="112" rx="6" ry="3.4" transform="rotate(-8 146 112)"/><ellipse cx="190" cy="104" rx="6" ry="3.4" transform="rotate(18 190 104)"/><ellipse cx="236" cy="110" rx="6" ry="3.4" transform="rotate(-20 236 110)"/><ellipse cx="282" cy="108" rx="6" ry="3.4" transform="rotate(8 282 108)"/><ellipse cx="322" cy="122" rx="6" ry="3.4" transform="rotate(-14 322 122)"/></g>
<path d="M78 112c20-30 60-42 90-44" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".35"/>
</svg>"""

# Keep the big goose simple and self-contained (hoagie in wing drawn inline)
GOOSE_BIG = """<svg viewBox="0 0 400 500" role="img" aria-labelledby="goose-t"><title id="goose-t">Illustration of a friendly goose with a hoagie</title>
<rect width="400" height="500" fill="#3d5a2b"/>
<circle cx="200" cy="310" r="190" fill="#557a3a"/>
<circle cx="200" cy="310" r="150" fill="none" stroke="#b5cf91" stroke-width="2" stroke-dasharray="4 10" opacity=".6"/>
<g stroke="#241811" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M110 500c-10-90 34-150 96-170-24-26-34-60-34-96 0-56 34-96 84-96 40 0 64 26 66 58l44 14-44 18c-4 50-40 84-58 108 52 24 80 80 74 164z" fill="#fffdf7"/>
<path d="M326 210l52 16-52 20z" fill="#e0a43c"/>
<path d="M150 470c30-60 90-80 150-70" fill="none" opacity=".4"/>
</g>
<circle cx="272" cy="196" r="9" fill="#241811"/><circle cx="275" cy="193" r="3" fill="#fff"/>
<path d="M244 236c10 8 26 10 38 4" fill="none" stroke="#e98b8b" stroke-width="8" stroke-linecap="round" opacity=".7"/>
<g transform="translate(40 330) rotate(-12)" stroke="#241811" stroke-width="5" stroke-linejoin="round">
<path d="M10 70c-2 16 12 26 36 26h120c22 0 36-10 34-26z" fill="#b8742a"/>
<path d="M6 62c20 8 180 8 200 0l2 12c-24 8-180 8-204 0z" fill="#7fae4d"/>
<path d="M8 52c22 6 176 6 196 0l2 12c-22 8-176 8-200 0z" fill="#e7837f"/>
<path d="M30 48l14 18 14-18zM96 48l14 18 14-18zM156 48l14 18 14-18z" fill="#f4c542"/>
<path d="M6 46c-2-34 44-56 100-56s104 22 100 56c-24 8-176 8-200 0z" fill="#d69a4f"/>
</g>
<text x="200" y="90" text-anchor="middle" font-family="Yellowtail, cursive" font-size="54" fill="#e7c98a" transform="rotate(-6 200 90)">since forever</text>
</svg>"""

TRAY = """<svg viewBox="0 0 300 300" aria-hidden="true"><g stroke="#241811" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
<ellipse cx="150" cy="190" rx="140" ry="70" fill="#fffdf7"/><ellipse cx="150" cy="182" rx="118" ry="54" fill="#efe8d4"/>
<rect x="70" y="140" width="56" height="36" rx="10" fill="#d69a4f"/><rect x="132" y="128" width="56" height="36" rx="10" fill="#d69a4f"/><rect x="176" y="156" width="56" height="36" rx="10" fill="#d69a4f"/><rect x="96" y="176" width="56" height="36" rx="10" fill="#d69a4f"/>
<path d="M74 152h48M136 140h48M180 168h48M100 188h48" stroke="#7fae4d" stroke-width="6"/>
<circle cx="214" cy="126" r="16" fill="#d9442f"/><circle cx="60" cy="196" r="12" fill="#8fb36a"/><circle cx="238" cy="206" r="12" fill="#f4c542"/>
</g></svg>"""

CHANDELIER = """<svg viewBox="0 0 300 300" aria-hidden="true"><g stroke="#e7c98a" stroke-width="4" fill="none" stroke-linecap="round">
<path d="M150 0v70"/><path d="M60 120c0 40 180 40 180 0"/><path d="M90 90c0 30 120 30 120 0"/><path d="M150 70v80"/>
<path d="M60 120v-18M240 120v-18M90 90v-14M210 90v-14M150 150v-14"/></g>
<g fill="#c8963e"><circle cx="60" cy="96" r="7"/><circle cx="240" cy="96" r="7"/><circle cx="90" cy="70" r="7"/><circle cx="210" cy="70" r="7"/><circle cx="150" cy="130" r="7"/></g>
<g fill="#fff3c4" opacity=".9"><path d="M60 80c-6 8-6 14 0 16 6-2 6-8 0-16zM240 80c-6 8-6 14 0 16 6-2 6-8 0-16zM90 54c-6 8-6 14 0 16 6-2 6-8 0-16zM210 54c-6 8-6 14 0 16 6-2 6-8 0-16zM150 114c-6 8-6 14 0 16 6-2 6-8 0-16z"/></g>
<g fill="#e7c98a" opacity=".5"><circle cx="40" cy="200" r="3"/><circle cx="260" cy="180" r="2"/><circle cx="120" cy="230" r="2"/><circle cx="200" cy="250" r="3"/></g></svg>"""

NAV = [("index.html", "Home"), ("menu.html", "Menu"), ("catering.html", "Catering"), ("gander-room.html", "Gander Room"), ("visit.html", "Visit")]


def egg(eid, extra=""):
    return ('<button class="egg %s" type="button" data-egg="%s" aria-label="A golden egg — click to collect">'
            '<svg viewBox="0 0 22 28" aria-hidden="true"><use href="/assets/img/sprite.svg#i-egg"/></svg></button>') % (extra, eid)


def head(title, desc, path):
    canon = SITE + "/" + ("" if path == "index.html" else path.replace(".html", ""))
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#2c4220">
<meta name="color-scheme" content="light">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Goose">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@thegoosemen">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Karla:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600;1,700&family=Yellowtail&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def chrome_top(path):
    def url(h):
        return "/" if h == "index.html" else "/" + h.replace(".html", "")
    cur = ' aria-current="page"'
    links = "".join('<li><a href="%s"%s>%s</a></li>' % (url(h), cur if h == path else "", n) for h, n in NAV)
    dlinks = "".join('<a class="drawer__link" href="%s">%s</a>' % (url(h), n) for h, n in NAV)
    return f"""
<div class="announce" data-announce="vac-2026" data-until="2026-12-01" role="region" aria-label="Announcement">
  <span>Heads up: we’re closed for vacation <strong>Nov 28 – Dec 1</strong> and back <strong>Dec 2</strong>. Have a safe &amp; happy holiday!</span>
  <button type="button" aria-label="Dismiss announcement"><svg width="18" height="18" aria-hidden="true"><use href="/assets/img/sprite.svg#i-x"/></svg></button>
</div>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="/" aria-label="The Goose — home">
      <svg class="brand__mark" aria-hidden="true"><use href="/assets/img/sprite.svg#i-goose"/></svg>
      <span class="brand__word">The Goose</span>
    </a>
    <ul class="nav__links">{links}</ul>
    <div class="nav__cta">
      <span class="status-pill" data-status role="status" aria-live="polite"><i aria-hidden="true"></i><span>Checking hours…</span></span>
      <a class="btn btn--matcha" href="/account"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-bag"/></svg>Order</a>
      <button class="menu-toggle" type="button" data-drawer-open aria-controls="drawer" aria-expanded="false" aria-label="Open menu"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-menu"/></svg></button>
    </div>
  </nav>
</header>
<div class="drawer" id="drawer" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Site menu">
  <div class="drawer__top">
    <a class="brand" href="/"><svg class="brand__mark" aria-hidden="true"><use href="/assets/img/sprite.svg#i-goose"/></svg><span class="brand__word">The Goose</span></a>
    <button class="menu-toggle" type="button" data-drawer-close aria-label="Close menu"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-x"/></svg></button>
  </div>
  {dlinks}
  <a class="drawer__link" href="/account">Log in / Register</a>
  <span class="status-pill" data-status style="align-self:flex-start;margin-top:20px;color:var(--ink)"><i aria-hidden="true"></i><span>Checking hours…</span></span>
  <a class="btn btn--light" href="/account">Start an order <svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-arrow"/></svg></a>
</div>
<main id="main">"""


def chrome_bottom(scripts=""):
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <p class="footer__big" aria-hidden="true">The Goose</p>
    <div class="footer__grid">
      <div>
        <h4>The Goosemen</h4>
        <p>A family-run deli on Bethlehem’s South Side, feeding Lehigh and the whole Lehigh Valley for more than 30 years.</p>
        <div class="socials">
          <a href="https://www.instagram.com/thegoosemen/" target="_blank" rel="noopener" aria-label="The Goose on Instagram"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-insta"/></svg></a>
          <a href="https://www.facebook.com/pages/Bethlehem-PA/The-Goose/16840181198" target="_blank" rel="noopener" aria-label="The Goose on Facebook"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-fb"/></svg></a>
          <a href="https://twitter.com/thegoosemen" target="_blank" rel="noopener" aria-label="The Goose on X (Twitter)"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-xsoc"/></svg></a>
        </div>
      </div>
      <div>
        <h4>Eat</h4>
        <ul><li><a href="/menu">Deli menu</a></li><li><a href="/catering">Catering</a></li><li><a href="/gander-room">The Gander Room</a></li><li><a href="/account">Log in / Register</a></li>
        <li><button type="button" class="btn btn--gold" data-vault-open hidden style="min-height:40px;margin-top:6px">The Vault</button></li></ul>
      </div>
      <div>
        <h4>Visit</h4>
        <ul><li><a href="https://maps.google.com/?q=102+W+Fourth+St+Bethlehem+PA+18015" target="_blank" rel="noopener">102 W. Fourth Street<br>Bethlehem, PA 18015</a></li>
        <li><a href="tel:+16108680176">(610) 868-0176</a></li><li><span style="opacity:.8">Fax (610) 868-6288</span></li></ul>
      </div>
      <div>
        <h4>Hours</h4>
        <ul><li>Mon–Fri · 7:30am–4pm</li><li>Sat · 10am–4pm</li><li>Sun · select Sundays</li></ul>
        <p style="margin-top:14px;font-size:.9rem">Psst — five golden eggs are hidden on this site. {egg("footer")}</p>
      </div>
    </div>
    <div class="footer__base">
      <span>© <span data-year>2026</span> The Goosemen Inc. All rights reserved.</span>
      <span><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="/accessibility">Accessibility</a></span>
      <span class="cards" aria-label="Accepted cards"><span>VISA</span><span>MC</span><span>AMEX</span></span>
    </div>
  </div>
</footer>
<div class="hunt-meter" id="hunt-meter" aria-live="polite"><span class="hunt-meter__eggs" aria-hidden="true"></span><span class="hunt-meter__txt"></span></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<dialog class="vault" id="vault" aria-labelledby="vault-h">
  <div class="vault__inner">
    <button class="vault__close" type="button" data-vault-close aria-label="Close"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-x"/></svg></button>
    <p class="eyebrow" style="color:var(--gold-soft)">Off-menu · regulars only</p>
    <h2 id="vault-h">You found the <span class="script">secret</span> menu.</h2>
    <p style="color:rgba(247,243,230,.8)">Nearly fifty sandwiches that never made the board — named by generations of students. A taste:</p>
    <ul class="vault__list">
      <li><b>Darth Vader</b><span>Roast beef dipped in au jus, Muenster, BBQ, bacon</span></li>
      <li><b>Charizard</b><span>Buffalo chicken, prosciutto, bacon, pepper jack, Santa Fe turkey, hot sauce</span></li>
      <li><b>Wooly Mammoth</b><span>Hot roast beef, meatballs, bacon, chili, provolone, hot sauce</span></li>
      <li><b>Strugglebus</b><span>Bacon, pepper ham, cheddarjack, lettuce, mayo, cucumber — melted &amp; toasted</span></li>
      <li><b>Pink Monkey</b><span>Meatballs, prosciutto &amp; provolone on a hoagie</span></li>
      <li><b>The Incredible Bulk</b><span>A Mammoth on a 3-foot French roll (order 24 hrs ahead)</span></li>
    </ul>
    <div class="btn-row"><a class="btn btn--gold" data-secret-link href="https://thegoose.io/" target="_blank" rel="noopener">Open the full secret menu <svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-arrow"/></svg></a>
    <button type="button" class="btn btn--ghost" data-vault-close style="color:var(--foam)">Keep it secret</button></div>
  </div>
</dialog>
{scripts}<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""
