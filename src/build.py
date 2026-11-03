"""Builds the static site into ../site. Run: python3 build.py"""
import os, shutil, html
from partials import head, chrome_top, chrome_bottom, egg, SITE
from art import HERO_HOAGIE, SHUTTLE, TAKE_SHOTS, GOMBO, CHEESESTEAK, PLATTER, CHAFING, GOOSE, CHANDELIER

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "..", "site")

MARQUEE_A = ["Space Shuttle Special", "The Gombo", "Take A Shots", "New-New-New", "The Geuben", "Black-Out Hoagie", "Guna Meld", "Mamma Goosey Stuffa Your Face"]
MARQUEE_B = ["Family run", "Off campus, on point", "Fresh sliced daily", "Catering for any crowd", "South Side Bethlehem", "Online ordering"]


def marquee(items, alt=False):
    spans = "".join(f"<span>{html.escape(i)}</span>" for i in items) * 2
    return f'<div class="marquee{" marquee--alt" if alt else ""}" aria-hidden="true"><div class="marquee__track">{spans}</div></div>'


def ic(name, cls=""):
    return f'<svg class="{cls}" aria-hidden="true"><use href="/assets/img/sprite.svg#i-{name}"/></svg>'


HOURS_TABLE = """<table class="hours"><caption class="sr-only">Deli hours</caption><tbody>
<tr data-day="1"><th scope="row">Monday</th><td>7:30am – 4:00pm</td></tr>
<tr data-day="2"><th scope="row">Tuesday</th><td>7:30am – 4:00pm</td></tr>
<tr data-day="3"><th scope="row">Wednesday</th><td>7:30am – 4:00pm</td></tr>
<tr data-day="4"><th scope="row">Thursday</th><td>7:30am – 4:00pm</td></tr>
<tr data-day="5"><th scope="row">Friday</th><td>7:30am – 4:00pm</td></tr>
<tr data-day="6"><th scope="row">Saturday</th><td>10:00am – 4:00pm</td></tr>
<tr data-day="0"><th scope="row">Sunday</th><td>Select Sundays</td></tr>
</tbody></table>"""

CONTACT = f"""<ul class="contact-list">
<li>{ic("pin")}<div><strong>The Goosemen</strong><br><a href="https://maps.google.com/?q=102+W+Fourth+St+Bethlehem+PA+18015" target="_blank" rel="noopener">102 W. Fourth Street, Bethlehem, PA 18015</a></div></li>
<li>{ic("phone")}<div><a href="tel:+16108680176">(610) 868-0176</a><br><span class="muted">Call ahead for pickup or catering</span></div></li>
<li>{ic("printer")}<div>Fax (610) 868-6288<br><span class="muted">Fax orders welcome</span></div></li>
<li>{ic("clock")}<div>Online ordering is available during store operating hours.</div></li>
</ul>"""

MAP = """<div class="map"><iframe title="Map showing The Goose at 102 W. Fourth Street, Bethlehem, PA" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
src="https://www.google.com/maps?q=102+W+Fourth+St,+Bethlehem,+PA+18015&amp;z=16&amp;output=embed"></iframe></div>"""


def page(path, title, desc, body, scripts=""):
    return head(title, desc, path) + chrome_top(path) + body + chrome_bottom(scripts)


# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div class="reveal">
      <p class="eyebrow">Family-run deli · South Side Bethlehem</p>
      <h1>Hoagies worth <span class="script">honking</span><span class="line2">about.</span></h1>
      <p class="lede">For over 30 years The Goose has stacked fresh-sliced hoagies, melty house originals and catering trays for Lehigh students, South Side neighbors and everyone lucky enough to find us on Fourth Street.</p>
      <div class="btn-row">
        <a class="btn btn--matcha" href="/account">{ic("bag")}Order online</a>
        <a class="btn btn--ghost" href="/menu">See the menu {ic("arrow")}</a>
      </div>
      <div class="hero__meta">
        <div><strong>30+</strong><span>years on Fourth St.</span></div>
        <div><strong>80+</strong><span>sandwiches on the board</span></div>
        <div><strong>49</strong><span>more you can’t see…</span></div>
      </div>
    </div>
    <div class="hero__art reveal" style="--d:.15s">
      <div class="hero__blob"></div>
      <div class="hero__hoagie">{HERO_HOAGIE}</div>
      <svg class="badge-spin" viewBox="0 0 120 120" aria-hidden="true"><defs><path id="circ" d="M60 60m-46 0a46 46 0 1 1 92 0a46 46 0 1 1-92 0"/></defs><circle cx="60" cy="60" r="58" fill="#e7c98a" stroke="#241811" stroke-width="3"/><text><textPath href="#circ">Fresh sliced · Family run · Bethlehem PA ·</textPath></text><use href="/assets/img/sprite.svg#i-goose" x="38" y="38" width="44" height="44"/></svg>
      <div class="sticker sticker--a"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-star"/></svg><span><b>Best Sandwich</b>Lehigh Valley Style</span></div>
      <div class="sticker sticker--b"><span><b>Lehigh’s</b>lunch tradition</span></div>
      {egg("hero", "egg--float").replace('class="egg egg--float"', 'class="egg egg--float" style="left:6%;top:8%"')}
    </div>
  </div>
</section>
{marquee(MARQUEE_A)}
{marquee(MARQUEE_B, alt=True)}

<section class="section" aria-labelledby="fav-h">
  <div class="wrap">
    <div class="section-head reveal">
      <div><p class="eyebrow">House favorites</p><h2 id="fav-h">The ones people drive back for.</h2></div>
      <p class="lede">Portuguese rolls, hoagie rolls and big stacks of toasted rye. These are the house originals regulars keep coming back for.</p>
    </div>
    <div class="bento">
      <a class="tile tile--xl reveal" href="/menu#special-hoagies" style="text-decoration:none">
        <span class="tag">Fan favorite</span><span class="price">$8.75</span>
        <div class="tile__art">{SHUTTLE}</div>
        <h3>Space Shuttle Special</h3>
        <p>Take-off turkey, robot roast beef &amp; countdown cheese on a hoagie roll. Liftoff guaranteed.</p>
      </a>
      <a class="tile tile--md reveal" href="/menu#foods" style="text-decoration:none;--d:.1s">
        <span class="tag tag--green">Legend</span><span class="price">$7.75</span>
        <div class="tile__art">{TAKE_SHOTS}</div>
        <h3>Take A Shots</h3><p>Roast beef, Santa Fe turkey, Swiss, slaw and Russian, toasted on three slices of rye.</p>
      </a>
      <a class="tile tile--sm reveal" href="/menu#foods" style="text-decoration:none;--d:.2s">
        <span class="tag tag--gold">Big one</span><span class="price">$8.99</span>
        <div class="tile__art">{GOMBO}</div>
        <h3>The Gombo</h3><p>Two meats, two cheeses, bacon, lettuce &amp; tomato on FOUR slices of toasted rye.</p>
      </a>
      <div class="tile tile--wide reveal on-dark">
        <div><h3 style="margin:0">Don’t see your sandwich?</h3><p>Generations of regulars have named their own. Rumor says there’s a whole other menu…</p></div>
        <a class="btn btn--light" href="/menu">Full menu {ic("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section on-dark" aria-labelledby="story-h">
  <div class="wrap story">
    <div class="story__art reveal">{GOOSE}</div>
    <div class="reveal" style="--d:.1s">
      <p class="eyebrow">Our story</p>
      <h2 id="story-h">A family deli on Fourth Street.</h2>
      <p class="story__quote">Ask any Lehigh student where to eat, and they’ll point you down Fourth Street.</p>
      <p class="muted">Old-timers still call it the Goosey Gander Deli. It’s a family-run sandwich shop just off Lehigh’s campus, and for decades students, professors and South Side neighbors have lined up here for lunch. Student groups even team up with the deli for “Keep the Goose Open Late” nights to raise money for their causes.</p>
      <div class="stats">
        <div class="stat"><strong>30+</strong><span>years serving the Valley</span></div>
        <div class="stat"><strong>3</strong><span>ways to order: online, phone, fax</span></div>
        <div class="stat"><strong>1</strong><span>banquet hall upstairs</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="events-h">
  <div class="wrap">
    <div class="section-head reveal">
      <div><p class="eyebrow">Feeding a crowd?</p><h2 id="events-h">From office lunch to full banquet.</h2></div>
      <p class="lede">Party trays dropped at your door, or the whole party hosted upstairs in our banquet room.</p>
    </div>
    <div class="duo">
      <article class="duo-card duo-card--cater reveal">
        <div class="duo-card__art">{PLATTER}</div>
        <div>
          <p class="eyebrow">Catering</p>
          <h3>Trays, buffets &amp; bag lunches</h3>
          <ul>
            <li>{ic("check")}Sandwich &amp; meat trays from $5.25 per person</li>
            <li>{ic("check")}Deluxe buffets with salads, plates &amp; utensils</li>
            <li>{ic("check")}Hot buffets customized to your headcount &amp; budget</li>
            <li>{ic("check")}Wings, meatballs &amp; chicken fingers by the 80 or 160</li>
          </ul>
        </div>
        <div class="btn-row"><a class="btn" href="/catering">Catering menu {ic("arrow")}</a></div>
      </article>
      <article class="duo-card duo-card--room on-dark reveal" style="--d:.1s">
        <div class="duo-card__art duo-card__art--hang">{CHANDELIER}</div>
        <div>
          <p class="eyebrow">The Gander Room</p>
          <h3>A banquet hall upstairs</h3>
          <p class="muted">A full-service banquet facility perched right above The Goose. Showers, rehearsal dinners, team banquets and reunions. We handle the food.</p>
          <ul>
            <li>{ic("check")}Hot hors d’oeuvres &amp; cold platters</li>
            <li>{ic("check")}Prime rib, seafood, chicken &amp; pasta entrées</li>
            <li>{ic("check")}Salads, sides &amp; dessert</li>
          </ul>
        </div>
        <div class="btn-row"><a class="btn btn--gold" href="/gander-room">Explore the room {ic("arrow")}</a></div>
      </article>
    </div>
  </div>
</section>

<section class="campus" aria-labelledby="campus-h">
  <div class="wrap campus__inner">
    <svg class="campus__seal" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="56" fill="#fffdf7" stroke="#241811" stroke-width="3"/><circle cx="60" cy="60" r="46" fill="none" stroke="#241811" stroke-width="1.5" stroke-dasharray="3 5"/><text x="60" y="52" text-anchor="middle" font-family="Playfair Display, serif" font-weight="800" font-size="15" fill="#241811">BROWN</text><text x="60" y="68" text-anchor="middle" font-family="Yellowtail, cursive" font-size="16" fill="#557a3a">&amp;</text><text x="60" y="84" text-anchor="middle" font-family="Playfair Display, serif" font-weight="800" font-size="15" fill="#241811">WHITE</text></svg>
    <div>
      <h2 id="campus-h">Steps from Lehigh. Part of the tradition.</h2>
      <p>Between classes, after practice, on move-in day and at reunion, The Goose has fed generations of Mountain Hawks. Student account? Pick “Student” when you register.</p>
    </div>
    <a class="btn btn--light" href="/account#register">Create an account {ic("arrow")}</a>
  </div>
</section>

<section class="section" aria-labelledby="visit-h">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Come hungry</p><h2 id="visit-h">Find us on Fourth Street.</h2></div>
    <span class="status-pill" data-status><i aria-hidden="true"></i><span>Checking hours…</span></span></div>
    <div class="visit">
      <div class="panel reveal"><h3>Deli hours</h3>{HOURS_TABLE}{CONTACT}</div>
      <div class="reveal" style="--d:.1s">{MAP}</div>
    </div>
  </div>
</section>

<section class="wrap" aria-labelledby="cta-h">
  <div class="cta-band on-dark reveal">
    <span class="cta-band__ring" style="width:520px;height:520px;left:-160px;top:-200px"></span>
    <span class="cta-band__ring" style="width:420px;height:420px;right:-140px;bottom:-200px"></span>
    <h2 id="cta-h">Skip the line. <span class="script">Order ahead.</span></h2>
    <p class="lede" style="margin-inline:auto">Log in, build your order, and it’ll be waiting at the counter. Online ordering runs during store hours.</p>
    <div class="btn-row"><a class="btn btn--light" href="/account">{ic("bag")}Start my order</a><a class="btn btn--ghost" data-tel href="tel:+16108680176" style="color:var(--foam)">{ic("phone")}Call (610) 868-0176</a></div>
  </div>
</section>
"""

# ---------------------------------------------------------------- MENU
menu = f"""
<section class="page-hero">
  <div class="wrap page-hero__split">
  <div class="reveal">
    <p class="eyebrow">The board</p>
    <h1>The <span class="script">Menu</span></h1>
    <p class="lede">Fresh-sliced, built to order. Choice of breads on sandwiches: rye, white, wheat or round rolls. Prices subject to change.</p>
    <div class="btn-row" style="margin-top:24px"><a class="btn btn--matcha" href="/account">{ic("bag")}Order online</a><a class="btn btn--ghost" href="/catering">Catering menu {ic("arrow")}</a></div>
  </div>
  <div class="page-hero__art reveal" style="--d:.1s">{CHEESESTEAK}</div>
  </div>
</section>
<div class="menu-tools">
  <div class="wrap menu-tools__inner">
    <nav class="chips" id="menu-chips" aria-label="Menu categories"></nav>
    <div class="search"><svg aria-hidden="true"><use href="/assets/img/sprite.svg#i-search"/></svg><label class="sr-only" for="menu-search">Search the menu</label><input id="menu-search" type="search" placeholder="Search turkey, rye, bacon…" autocomplete="off"></div>
  </div>
</div>
<div class="wrap">
  <p id="menu-count" class="muted" role="status" aria-live="polite" style="margin:16px 0 0"></p>
  <div id="menu-root"><noscript><p class="empty">Turn on JavaScript to browse the interactive menu, or call (610) 868-0176.</p></noscript></div>
  <p class="empty" id="menu-empty" hidden>Nothing matches that, but the counter can make almost anything. Call (610) 868-0176.</p>
</div>
"""

# ---------------------------------------------------------------- CATERING
def tray(name, price, desc, extra=""):
    return f'<article class="tray reveal"><h3>{name}</h3><span class="tray__price">{price}</span><p>{desc}</p>{extra}</article>'

catering = f"""
<section class="page-hero">
  <div class="wrap page-hero__split">
  <div class="reveal">
    <p class="eyebrow">Catering</p>
    <h1>Feed the <span class="script">whole flock.</span></h1>
    <p class="lede">Office lunches, tailgates, team dinners, graduation parties. Trays and buffets built fresh, priced per person, and customized to your crowd and budget.</p>
    <div class="btn-row" style="margin-top:24px"><a class="btn btn--matcha" href="#inquire">Plan my order {ic("arrow")}</a><a class="btn btn--ghost" href="tel:+16108680176">{ic("phone")}(610) 868-0176</a></div>
  </div>
  <div class="page-hero__art reveal" style="--d:.1s">{CHAFING}</div>
  </div>
</section>

<section class="section" style="padding-top:24px" aria-labelledby="how-h">
  <div class="wrap">
    <h2 id="how-h" class="sr-only">How catering works</h2>
    <ol class="steps">
      <li class="reveal"><h3>Pick your spread</h3><p>Choose trays, a cold buffet, or let us build a hot buffet for your headcount.</p></li>
      <li class="reveal" style="--d:.08s"><h3>Tell us the details</h3><p>Date, time, number of guests, and pickup or drop-off. Send an inquiry or give us a call.</p></li>
      <li class="reveal" style="--d:.16s"><h3>We confirm &amp; quote</h3><p>The Goosemen will confirm your order and final price before the big day.</p></li>
      <li class="reveal" style="--d:.24s"><h3>Pick up and enjoy</h3><p>Buffets come with plates, napkins, utensils and a tablecloth.</p></li>
    </ol>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="fun-h">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Fun Trays</p><h2 id="fun-h">Party trays</h2></div><p class="lede">Grab-and-go crowd pleasers. Great for game day.</p></div>
    <div class="tray-grid">
      {tray("Cheese Tray", "$50.00", "A variety of cheese, sliced &amp; chunked, with sliced ring bologna or pepperoni, Dijon mustard &amp; crackers.")}
      {tray("Fruit Tray", "$65.00", "Seasonal fruits with a sweet creamy dip.")}
      {tray("Fresh Veggie Tray", "$50.00", "Broccoli, cauliflower, celery, carrots &amp; cucumbers, fresh cut with a tasty dip.")}
      {tray("Goose’s Meatballs", "80 ct · $25 &nbsp;|&nbsp; 160 ct · $50", "Italian-style marinara or Swedish brown sauce.")}
      {tray("Goose’s Buffalo Wings", "80 ct · $90 &nbsp;|&nbsp; 160 ct · $175", "Chicken wings marinated in spicy Buffalo or BBQ sauce.")}
      {tray("Goose’s Chicken Fingers", "80 ct · $75 &nbsp;|&nbsp; 160 ct · $100", "Grilled chicken cut finger-size with BBQ.", "<p><strong>Also available:</strong> Chicken Tenders, 60 ct · $90</p>")}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="cold-h">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Cold Menu</p><h2 id="cold-h">Sandwiches &amp; buffets</h2></div><p class="lede">Priced per person. Bread, rolls, mayo &amp; mustard included where noted.</p></div>
    <div class="tray-grid">
      {tray("Deluxe Sandwich Tray", "$6.50 per person", "Your favorite classic sandwiches cut &amp; displayed on a tray. A quick, easy lunch that keeps your event moving.")}
      {tray("Classic Deluxe Meat Tray", "$5.25 per person", "Sliced fresh and garnished with lettuce &amp; tomatoes. Bread, rolls, mayo &amp; mustard included.", "<ul><li>Top round roast beef</li><li>Gourmet turkey</li><li>Smoked ham</li><li>American &amp; Swiss cheese</li><li>Pickles &amp; olives</li></ul>")}
      {tray("Deluxe Buffet", "$9.00 per person", "Sandwich tray or meat tray, plus macaroni salad, potato salad &amp; coleslaw. Plates, napkins, utensils, tablecloth, mayo, mustard, pickles &amp; olives.", "<p><strong>Add drinks:</strong> Lipton / Snapple +$2.50 · Soda +$1.00</p>")}
      {tray("Mini Portuguese Roll Sandwiches", "$3.00 per person", "Your favorite classic sandwiches on mini Portuguese rolls, cut &amp; displayed.")}
      {tray("The Goosemen’s Bag Lunch", "Custom pricing", "Customized to your specs &amp; budget: sandwich, chips, apple, cookie, mayo &amp; mustard, plus water, soda or Gatorade.")}
    </div>
  </div>
</section>

<section class="section on-dark" aria-labelledby="hot-h">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Hot Menu</p><h2 id="hot-h">Hot buffet, your way. {egg("hotmenu")}</h2></div>
    <p class="lede">The Goosemen will customize your next event from the hot buffet menu according to your headcount &amp; budget. All buffets include plates, napkins, utensils &amp; tablecloth.</p></div>
    <div class="cols-3">
      <div class="list-card reveal"><h3>Entrées</h3><ul><li>Baked ziti with cheese</li><li>Italian meatballs</li><li>Meat, cheese or veggie lasagna</li><li>Cheese stuffed shells</li><li>Ham heated with pineapple juice</li><li>Thinly sliced roast beef au jus</li><li>Sausage with onions &amp; peppers</li><li>Pulled turkey with gravy</li><li>Pork BBQ</li><li>Roastery chicken</li><li>Chicken à la Gander (grilled chicken)</li></ul></div>
      <div class="list-card reveal" style="--d:.08s"><h3>Vegetables &amp; appetizers</h3><ul><li>Tossed salad or fruit salad</li><li>String beans</li><li>Glazed carrots</li><li>Corn</li><li>Peas</li><li>Mixed vegetables</li></ul></div>
      <div class="list-card reveal" style="--d:.16s"><h3>Sides &amp; dessert</h3><ul><li>Mashed potatoes</li><li>Macaroni &amp; cheese</li><li>Irish parsley potatoes</li><li>Desserts available, just ask</li></ul></div>
    </div>
  </div>
</section>

<section class="section" id="inquire" aria-labelledby="inq-h">
  <div class="wrap auth">
    <div class="reveal">
      <p class="eyebrow">Book it</p>
      <h2 id="inq-h">Start a catering inquiry</h2>
      <p class="lede">Tell us the basics and we’ll help with the rest. Calling is still the fastest way, and the Goosemen are happy to talk it through.</p>
      {CONTACT}
    </div>
    <form class="panel form reveal" id="inquiry" data-validate novalidate>
      <div class="hp" aria-hidden="true"><label>Leave this empty <input name="website" tabindex="-1" autocomplete="off"></label></div>
      <div class="form-row">
        <div class="field"><label for="q-name">Name <span class="req" aria-hidden="true">*</span></label><input id="q-name" name="name" required autocomplete="name"><span class="err">Please add your name.</span></div>
        <div class="field"><label for="q-phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="q-phone" name="phone" type="tel" required autocomplete="tel" pattern="[0-9()+.\\-\\s]{{7,}}"><span class="err">Enter a phone number we can call.</span></div>
      </div>
      <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"><span class="err">That email doesn’t look right.</span></div>
      <div class="form-row">
        <div class="field"><label for="q-date">Event date <span class="req" aria-hidden="true">*</span></label><input id="q-date" name="date" type="date" required><span class="err">Pick a date.</span></div>
        <div class="field"><label for="q-guests">Guests <span class="req" aria-hidden="true">*</span></label><input id="q-guests" name="guests" type="number" min="1" max="2000" required inputmode="numeric"><span class="err">How many people?</span></div>
      </div>
      <div class="field"><label for="q-service">What are you thinking?</label><select id="q-service" name="service"><option>Party trays</option><option>Cold buffet</option><option>Hot buffet</option><option>Bag lunches</option><option>Gander Room banquet</option><option>Not sure yet</option></select></div>
      <div class="field"><label for="q-details">Details</label><textarea id="q-details" name="details" placeholder="Pickup or drop-off, time, dietary needs, budget…"></textarea></div>
      <button class="btn btn--matcha" type="submit">Send inquiry {ic("arrow")}</button>
      <p class="form-status notice" role="status" hidden></p>
      <p class="muted" style="font-size:.88rem;margin:0">We only use these details to respond to your inquiry. See our <a href="/privacy">Privacy Policy</a>.</p>
    </form>
  </div>
</section>
"""

# ---------------------------------------------------------------- GANDER ROOM
gander = f"""
<section class="page-hero on-dark page-hero--room">
  <div class="wrap page-hero__split">
  <div class="reveal">
    <p class="eyebrow">Upstairs at The Goose</p>
    <h1>The Gander <span class="script" style="color:var(--gold-soft)">Room</span></h1>
    <p class="lede">A full-service banquet facility perched above The Goose on the fabulous South Side of Bethlehem. You bring the guests and we’ll handle the food.</p>
    <div class="btn-row" style="margin-top:24px"><a class="btn btn--gold" href="/catering#inquire">Ask about a date {ic("arrow")}</a><a class="btn btn--ghost" href="tel:+16108680176" style="color:var(--foam)">{ic("phone")}(610) 868-0176</a></div>
  </div>
  <div class="page-hero__art page-hero__art--hang reveal" style="--d:.1s">{CHANDELIER}</div>
  </div>
</section>
<section class="section" aria-labelledby="occ-h">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Made for</p><h2 id="occ-h">Every kind of get-together.</h2></div><p class="lede">Rehearsal dinners, showers, birthdays, team banquets, alumni weekends, memorial luncheons and holiday parties.</p></div>
    <div class="cols-3">
      <div class="tray reveal"><h3>Hot hors d’oeuvres</h3><ul><li>Spinach &amp; feta triangles in filo</li><li>Asparagus &amp; asiago in filo</li><li>Mini crab cakes with tartar</li><li>Scallops wrapped in bacon</li><li>Coconut shrimp, spicy plum sauce</li><li>Teriyaki chicken skewers</li><li>Clams casino</li><li>Crab-stuffed mushrooms</li><li>Meatballs: marinara, sweet &amp; sour or Swedish</li><li>Wings: Buffalo or BBQ</li><li>…and many more</li></ul></div>
      <div class="tray reveal" style="--d:.08s"><h3>Cold platters</h3><ul><li>Shrimp cocktail</li><li>Blue crab claw cocktail</li><li>Fresh mozzarella, vine-ripe tomato &amp; basil</li><li>Domestic cheese &amp; crackers</li><li>Imported cheeses &amp; meats</li><li>Ring bologna &amp; crackers</li><li>Fresh vegetables with dip</li><li>Chips &amp; pretzels with onion dip</li></ul></div>
      <div class="tray reveal" style="--d:.16s"><h3>Entrées</h3><ul><li>Slow-roasted choice prime rib</li><li>Braised beef tips, burgundy mushroom sauce</li><li>Yankee pot roast</li><li>Salmon Newburg</li><li>Scallop &amp; crab stuffed sole</li><li>Macadamia-crusted mahi mahi</li><li>Crab-stuffed shrimp</li><li>Chicken Marsala or Parmesan</li><li>Honey baked ham with pineapple</li><li>Eggplant rollatini</li><li>…plus pastas, salads, sides &amp; dessert</li></ul></div>
    </div>
    <p class="muted reveal" style="margin-top:28px">Menus are customized for each event. Call or send an inquiry for availability, capacity and pricing.</p>
  </div>
</section>
"""

# ---------------------------------------------------------------- VISIT
visit = f"""
<section class="page-hero">
  <div class="wrap reveal"><p class="eyebrow">Hours &amp; location</p><h1>Come <span class="script">say hi.</span></h1>
  <p class="lede">Just off Lehigh’s campus on West Fourth Street, with street parking out front.</p>
  <span class="status-pill" data-status style="margin-top:12px"><i aria-hidden="true"></i><span>Checking hours…</span></span></div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap visit">
    <div class="panel reveal"><h2 style="font-size:1.8rem">Deli hours</h2>{HOURS_TABLE}{CONTACT}</div>
    <div class="reveal" style="--d:.1s">{MAP}</div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ACCOUNT
account = f"""
<section class="page-hero" style="padding-bottom:24px">
  <div class="wrap reveal"><p class="eyebrow">Online ordering</p><h1>Your <span class="script">Goose</span> account</h1>
  <p class="lede">Log in to order ahead, or register in a minute. Online ordering is available during store operating hours.</p></div>
</section>
<section class="section" style="padding-top:24px">
  <div class="wrap auth">
    <div class="panel on-dark reveal" style="background:var(--matcha-800);border-color:var(--ink)">
      <h2 style="font-size:2rem">Why register?</h2>
      <ul class="perk-list">
        <li>{ic("bag")}<div><strong>Order ahead</strong><br><span class="muted">Skip the line and pick up when it’s ready.</span></div></li>
        <li>{ic("star")}<div><strong>Save your go-to</strong><br><span class="muted">Your usual, without the explaining.</span></div></li>
        <li>{ic("gift")}<div><strong>Coupons &amp; event news</strong><br><span class="muted">Optional emails. Opt out anytime.</span></div></li>
        <li>{ic("shield")}<div><strong>Secure checkout</strong><br><span class="muted">Card payments are handled by the ordering system’s payment processor. We never see your full card number.</span></div></li>
      </ul>
      <a class="btn btn--light" data-order-link href="https://www.thegoose.com/" style="margin-top:28px">Go to online ordering {ic("arrow")}</a>
    </div>
    <div class="panel reveal" style="--d:.1s">
      <div class="tabs" role="tablist" aria-label="Account">
        <button role="tab" id="tab-login" aria-controls="panel-login" aria-selected="true" tabindex="0">Log in</button>
        <button role="tab" id="tab-register" aria-controls="panel-register" aria-selected="false" tabindex="-1">Register</button>
      </div>
      <div class="notice notice--warn" style="margin-bottom:20px">{ic("info")}<span><strong>Preview.</strong> These forms are for design review and don’t send or store anything. Use <a data-order-link href="https://www.thegoose.com/">The Goose’s ordering site</a> to log in for real.</span></div>

      <div role="tabpanel" id="panel-login" aria-labelledby="tab-login">
        <form class="form" data-account data-validate novalidate>
          <div class="hp" aria-hidden="true"><label>Leave this empty <input name="website" tabindex="-1" autocomplete="off"></label></div>
          <div class="field"><label for="l-user">Username</label><input id="l-user" name="username" required autocomplete="username" autocapitalize="none" spellcheck="false"><span class="err">Enter your username.</span></div>
          <div class="field"><label for="l-pass">Password</label><div class="pw-wrap"><input id="l-pass" name="password" type="password" required autocomplete="current-password"><button type="button" data-pw-toggle aria-pressed="false" aria-label="Show password">Show</button></div><span class="err">Enter your password.</span></div>
          <button class="btn" type="submit">Log in {ic("arrow")}</button>
          <p class="form-status notice" role="status" hidden></p>
        </form>
        <hr style="border:0;border-top:1px dashed var(--line);margin:28px 0">
        <h3>Forgot your password?</h3>
        <p class="muted">Enter your username and your login information will be sent to the email address on your account.</p>
        <form class="form" data-account data-validate novalidate>
          <div class="field"><label for="f-user">Username</label><input id="f-user" name="username" required autocomplete="username" autocapitalize="none"><span class="err">Enter your username.</span></div>
          <button class="btn btn--ghost" type="submit">Retrieve password</button>
          <p class="form-status notice" role="status" hidden></p>
        </form>
        <p class="muted" style="margin-top:20px">New here? <a href="#register" data-tab-go="tab-register">Create an account</a></p>
      </div>

      <div role="tabpanel" id="panel-register" aria-labelledby="tab-register" hidden>
        <form class="form" data-account data-validate novalidate>
          <div class="hp" aria-hidden="true"><label>Leave this empty <input name="website" tabindex="-1" autocomplete="off"></label></div>
          <h3 style="margin:0">Account information</h3>
          <div class="form-row">
            <div class="field"><label for="r-first">First name <span class="req" aria-hidden="true">*</span></label><input id="r-first" name="first" required autocomplete="given-name"><span class="err">Required.</span></div>
            <div class="field"><label for="r-last">Last name <span class="req" aria-hidden="true">*</span></label><input id="r-last" name="last" required autocomplete="family-name"><span class="err">Required.</span></div>
          </div>
          <div class="field"><label for="r-a1">Street address <span class="req" aria-hidden="true">*</span></label><input id="r-a1" name="address1" required autocomplete="address-line1"><span class="err">Required.</span></div>
          <div class="field"><label for="r-a2">Apt, suite, dorm (optional)</label><input id="r-a2" name="address2" autocomplete="address-line2"></div>
          <div class="form-row form-row--3">
            <div class="field"><label for="r-city">City <span class="req" aria-hidden="true">*</span></label><input id="r-city" name="city" required autocomplete="address-level2"><span class="err">Required.</span></div>
            <div class="field"><label for="r-state">State <span class="req" aria-hidden="true">*</span></label><input id="r-state" name="state" required maxlength="2" pattern="[A-Za-z]{{2}}" autocomplete="address-level1" value="PA"><span class="err">2 letters.</span></div>
            <div class="field"><label for="r-zip">ZIP <span class="req" aria-hidden="true">*</span></label><input id="r-zip" name="zip" required inputmode="numeric" pattern="[0-9]{{5}}" autocomplete="postal-code"><span class="err">5 digits.</span></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="r-phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="r-phone" name="phone" type="tel" required autocomplete="tel" pattern="[0-9()+.\\-\\s]{{10,}}"><span class="err">Enter a 10-digit phone.</span></div>
            <div class="field"><label for="r-email">Email <span class="req" aria-hidden="true">*</span></label><input id="r-email" name="email" type="email" required autocomplete="email"><span class="hint">Your password will be emailed here.</span><span class="err">Enter a valid email.</span></div>
          </div>
          <label class="check"><input type="checkbox" name="optin"> <span>Send me coupons &amp; event notices by email. (Optional. Unsubscribe anytime.)</span></label>
          <h3 style="margin:8px 0 0">Login information</h3>
          <div class="form-row">
            <div class="field"><label for="r-user">Username <span class="req" aria-hidden="true">*</span></label><input id="r-user" name="username" required minlength="4" maxlength="10" pattern="\\S{{4,10}}" autocomplete="username" autocapitalize="none" spellcheck="false" aria-describedby="r-user-h"><span class="hint" id="r-user-h">4–10 characters, no spaces.</span><span class="err">4–10 characters with no spaces.</span></div>
            <div class="field"><label for="r-type">Account type</label><select id="r-type" name="type"><option>Student</option><option>Faculty / Staff</option><option>Business</option><option>Resident / Guest</option></select></div>
          </div>
          <label class="check"><input type="checkbox" required name="agree"> <span>I agree to the <a href="/terms">Terms</a> and have read the <a href="/privacy">Privacy Policy</a>.</span></label>
          <button class="btn btn--matcha" type="submit">Create account {ic("arrow")}</button>
          <p class="form-status notice" role="status" hidden></p>
        </form>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- LEGAL
UPDATED = "October 31, 2026"

privacy = f"""
<section class="page-hero"><div class="wrap reveal"><p class="eyebrow">Legal</p><h1>Privacy <span class="script">Policy</span></h1><p class="updated">Last updated {UPDATED}</p></div></section>
<div class="wrap legal">
<p>The Goosemen Inc. (“The Goose,” “we,” “us”) runs this website and our deli at 102 W. Fourth Street, Bethlehem, PA 18015. This policy explains what information we collect, how we use it, and the choices you have.</p>
<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>
<li><a href="#collect">Information we collect</a></li><li><a href="#use">How we use it</a></li><li><a href="#payments">Payments</a></li><li><a href="#share">Sharing</a></li><li><a href="#cookies">Cookies &amp; local storage</a></li><li><a href="#third">Third-party services</a></li><li><a href="#security">Security</a></li><li><a href="#retention">Retention</a></li><li><a href="#choices">Your choices &amp; rights</a></li><li><a href="#kids">Children</a></li><li><a href="#changes">Changes</a></li><li><a href="#contact">Contact</a></li></ol></nav>
<h2 id="collect">1. Information we collect</h2>
<h3>Information you give us</h3>
<ul><li><strong>Account &amp; ordering:</strong> name, street address, city, state, ZIP, phone, email, username, account type (e.g., student), and your order history and instructions.</li>
<li><strong>Catering &amp; event inquiries:</strong> name, phone, email, event date, guest count and any details you share.</li>
<li><strong>Communications:</strong> messages you send us and whether you opted in to coupons and event emails.</li></ul>
<h3>Information collected automatically</h3>
<p>Our hosting provider records standard technical logs (such as IP address, browser type, pages requested and timestamps) to deliver the site and protect it from abuse. This site does not use advertising trackers or sell-your-data style analytics.</p>
<h2 id="use">2. How we use information</h2>
<ul><li>To create and manage your account and to prepare, confirm and hand off your orders.</li><li>To respond to catering and Gander Room inquiries and provide quotes.</li><li>To send coupons and event notices <em>only</em> if you opt in.</li><li>To keep the website secure, prevent fraud and fix problems.</li><li>To meet legal, tax and accounting obligations.</li></ul>
<h2 id="payments">3. Payments</h2>
<p>Card payments for online orders are processed by our ordering system’s payment processor. Your full card number is sent directly to that processor over an encrypted connection and is <strong>never stored on this website or seen by our staff</strong>. We may receive limited details such as the card type, last four digits and whether the payment succeeded, so we can match payments to orders. We accept Visa, Mastercard and American Express.</p>
<h2 id="share">4. How we share information</h2>
<p>We do not sell or rent your personal information. We share it only with:</p>
<ul><li><strong>Service providers</strong> that help us operate, such as website hosting, our online ordering platform, payment processing and email. They may use it only to provide services to us.</li><li><strong>Legal and safety</strong> recipients when required by law or to protect the rights, property or safety of our customers, staff or others.</li><li><strong>A successor</strong> if the business is sold or transferred, subject to this policy.</li></ul>
<h2 id="cookies">5. Cookies &amp; local storage</h2>
<p>This site does not set advertising or tracking cookies. It uses your browser’s local storage for small conveniences only, for example remembering that you dismissed an announcement or which golden eggs you’ve found. That information stays on your device, is never sent to us, and you can clear it anytime in your browser settings. Our separate online ordering system may use essential cookies to keep you logged in and your cart working.</p>
<h2 id="third">6. Third-party services</h2>
<p>Some pages load content from third parties, which may receive your IP address when you view them: Google Fonts (typefaces), Google Maps (the embedded map), and links to Instagram, Facebook and X. Their own privacy policies govern how they handle data.</p>
<h2 id="security">7. Security</h2>
<p>The site is served only over HTTPS with modern security headers, and forms include protections against spam. No system is perfectly secure, so please use a unique password for your account and tell us right away if you suspect unauthorized use.</p>
<h2 id="retention">8. Retention</h2>
<p>We keep account information while your account is active and order records as long as needed for business, tax and legal purposes. Inquiry details are kept only as long as needed to respond and plan your event.</p>
<h2 id="choices">9. Your choices &amp; rights</h2>
<ul><li><strong>Email:</strong> unsubscribe from marketing using the link in any email or by contacting us. We’ll still send order-related messages.</li><li><strong>Access, correction &amp; deletion:</strong> contact us to review, update or delete your account information, subject to records we must keep by law.</li><li><strong>Do Not Track / Global Privacy Control:</strong> because we don’t track you across sites or sell data, there’s nothing to opt out of, but we honor these signals.</li></ul>
<h2 id="kids">10. Children</h2>
<p>This site isn’t directed to children under 13, and we don’t knowingly collect their personal information. If you believe a child has given us information, contact us and we’ll delete it.</p>
<h2 id="changes">11. Changes</h2>
<p>We may update this policy. We’ll change the “last updated” date above and, for significant changes, post a notice on the site.</p>
<h2 id="contact">12. Contact</h2>
<p>The Goosemen Inc., 102 W. Fourth Street, Bethlehem, PA 18015 · <a href="tel:+16108680176">(610) 868-0176</a></p>
</div>
"""

terms = f"""
<section class="page-hero"><div class="wrap reveal"><p class="eyebrow">Legal</p><h1>Terms of <span class="script">Use</span></h1><p class="updated">Last updated {UPDATED}</p></div></section>
<div class="wrap legal">
<p>Welcome to The Goose. By using this website or placing an order, you agree to these Terms. If you don’t agree, please don’t use the site.</p>
<h2>1. Orders</h2>
<ul><li>Online ordering is available during store operating hours only. Orders are confirmed when accepted by the deli.</li><li>Menu items, prices and availability may change without notice, and prices online may differ from in-store. Sales tax is added where applicable.</li><li>We may refuse or cancel an order, for example if an item is unavailable, a price is listed in error, or we suspect fraud. If you’ve been charged, we’ll refund you.</li><li>Please pick up orders at the time given. Food left unclaimed may be discarded after reasonable time and may not be refunded.</li></ul>
<h2>2. Catering &amp; Gander Room</h2>
<ul><li>Catering and banquet orders are confirmed only after the deli accepts them and agrees on a final menu, headcount and price. Some items require advance notice (e.g., 24 hours for 3-foot sandwiches).</li><li>Deposits, guaranteed counts, cancellation windows and room policies will be provided with your quote and form part of your agreement.</li></ul>
<h2>3. Payments</h2>
<p>We accept Visa, Mastercard and American Express. Payments are handled by our payment processor; you agree to provide accurate payment and contact information.</p>
<h2>4. Allergens &amp; food safety</h2>
<p>Our kitchen handles common allergens including milk, eggs, wheat, soy, fish, shellfish, tree nuts and peanuts, and cross-contact can occur. Menu descriptions may not list every ingredient. If you have a food allergy, please tell us when ordering and ask a team member before eating. Consuming raw or undercooked meats, seafood or eggs may increase your risk of foodborne illness.</p>
<h2>5. Your account</h2>
<p>Keep your login private and tell us about any unauthorized use. You’re responsible for activity under your account. We may suspend accounts used for fraud or abuse.</p>
<h2>6. Acceptable use</h2>
<p>Don’t misuse the site: no attempts to break in, probe for vulnerabilities, scrape at scale, submit false orders, or interfere with other customers.</p>
<h2>7. Content &amp; trademarks</h2>
<p>“The Goose,” “The Goosemen,” “The Gander Room,” our menu names and site content belong to The Goosemen Inc. Lehigh University is referenced for community context only and does not sponsor or endorse this site.</p>
<h2>8. Disclaimers &amp; liability</h2>
<p>The site is provided “as is.” To the fullest extent allowed by law, we aren’t liable for indirect or consequential damages, and our total liability for any claim relating to an order is limited to the amount you paid for that order.</p>
<h2>9. Governing law</h2>
<p>These Terms are governed by the laws of the Commonwealth of Pennsylvania.</p>
<h2>10. Contact</h2>
<p>The Goosemen Inc., 102 W. Fourth Street, Bethlehem, PA 18015 · <a href="tel:+16108680176">(610) 868-0176</a></p>
</div>
"""

a11y = f"""
<section class="page-hero"><div class="wrap reveal"><p class="eyebrow">For everyone</p><h1>Accessibility</h1><p class="updated">Last updated {UPDATED}</p></div></section>
<div class="wrap legal">
<p>We want everyone to be able to browse the menu, order and plan events with The Goose. This site aims to meet the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA.</p>
<h2>What we’ve done</h2>
<ul><li>Text and controls meet color-contrast guidelines; touch targets are at least 44×44 pixels.</li><li>Full keyboard navigation with visible focus indicators and a “skip to content” link.</li><li>Form fields have visible labels, helpful hints and clear error messages.</li><li>Animations respect your device’s “reduce motion” setting.</li><li>Images and illustrations include text alternatives or are hidden from screen readers when decorative.</li><li>Pages work when zoomed to 200% and on phone-sized screens.</li></ul>
<h2>Need help?</h2>
<p>If anything on this site is hard to use, call us at <a href="tel:+16108680176">(610) 868-0176</a> and we’ll take your order by phone. Please also let us know what didn’t work so we can fix it.</p>
</div>
"""

notfound = f"""
<section class="page-hero" style="text-align:center;padding-block:clamp(80px,14vw,160px)">
  <div class="wrap"><p class="eyebrow" style="justify-content:center">Error 404</p><h1>This page flew <span class="script">south.</span></h1>
  <p class="lede" style="margin-inline:auto">We couldn’t find that page, but the hoagies are right where we left them.</p>
  <div class="btn-row" style="justify-content:center;margin-top:28px"><a class="btn btn--matcha" href="/">Back home</a><a class="btn btn--ghost" href="/menu">See the menu</a></div></div>
</section>
"""

PAGES = [
    ("index.html", "The Goose · Family-Run Deli in South Side Bethlehem, PA", "Fresh-sliced hoagies, house sandwiches, catering and the Gander Room banquet hall. A Lehigh tradition on W. Fourth Street for 30+ years.", home, ""),
    ("menu.html", "Menu · The Goose Deli, Bethlehem", "Hoagies, house originals, delites, salads, soups and sides at The Goose in South Side Bethlehem. Search the full menu with prices.", menu, '<script src="/assets/js/menu-data.js" defer></script>\n'),
    ("catering.html", "Catering · The Goose, Bethlehem PA", "Party trays, cold and hot buffets and bag lunches for offices, teams and parties across the Lehigh Valley.", catering, ""),
    ("gander-room.html", "The Gander Room · Banquet Facility above The Goose", "A full-service banquet facility on Bethlehem’s South Side: hors d’oeuvres, platters, entrées and more for your event.", gander, ""),
    ("visit.html", "Hours & Location · The Goose, Bethlehem", "Find The Goose at 102 W. Fourth Street, Bethlehem, PA 18015. Deli hours, phone and directions.", visit, ""),
    ("account.html", "Log In or Register · The Goose Online Ordering", "Log in or create your account to order ahead from The Goose.", account, ""),
    ("privacy.html", "Privacy Policy · The Goose", "How The Goosemen Inc. collects, uses and protects your information.", privacy, ""),
    ("terms.html", "Terms of Use · The Goose", "Terms for using The Goose website, online ordering and catering.", terms, ""),
    ("accessibility.html", "Accessibility · The Goose", "Our commitment to an accessible website and how to get help ordering.", a11y, ""),
    ("404.html", "Page not found · The Goose", "That page flew south.", notfound, ""),
]


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    shutil.copytree(os.path.join(ROOT, "static"), OUT, dirs_exist_ok=True)
    vj = os.path.join(OUT, "vercel.json")
    if os.path.exists(vj): os.remove(vj)
    for path, title, desc, body, scripts in PAGES:
        out = page(path, html.escape(title), html.escape(desc), body, scripts)
        if path == "account.html" or path == "404.html":
            out = out.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"') if path == "404.html" else out
        with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
            f.write(out)
    # cache-bust: tag CSS/JS links with a content hash so browsers never mix new pages with old assets
    import hashlib, glob
    tags = {}
    for rel in ["assets/css/styles.css", "assets/js/main.js", "assets/js/menu-data.js", "assets/img/sprite.svg"]:
        with open(os.path.join(OUT, rel), "rb") as fh:
            tags["/" + rel] = hashlib.sha1(fh.read()).hexdigest()[:10]
    for page_path in glob.glob(os.path.join(OUT, "*.html")):
        with open(page_path, encoding="utf-8") as fh:
            s = fh.read()
        for url, h in tags.items():
            s = s.replace('"' + url + '"', '"' + url + "?v=" + h + '"').replace('"' + url + "#", '"' + url + "?v=" + h + "#")
        with open(page_path, "w", encoding="utf-8") as fh:
            fh.write(s)
    print("built", len(PAGES), "pages ->", os.path.normpath(OUT))


if __name__ == "__main__":
    build()
