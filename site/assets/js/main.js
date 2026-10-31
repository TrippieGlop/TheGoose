/* The Goose — site behavior. No trackers, no third-party scripts. */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* ---- Site config: edit these when the ordering system is confirmed ---- */
  var CONFIG = {
    orderingUrl: "https://www.thegoose.com/",   // existing G.O.O.S.E. ordering system (login / register / order)
    secretUrl: "https://thegoose.io/",          // secret menu
    email: "",                                  // set to the deli's catering email to enable the inquiry form's email draft
    phone: "6108680176",
    tz: "America/New_York",
    // Deli hours (24h, minutes since midnight). null = closed.
    hours: { 0: null, 1: [450, 960], 2: [450, 960], 3: [450, 960], 4: [450, 960], 5: [450, 960], 6: [600, 960] },
    // Closures: inclusive YYYY-MM-DD ranges
    closures: [{ from: "2026-11-28", to: "2026-12-01", label: "Closed for vacation · back Dec 2" }],
    eggs: ["hero", "story", "sides", "hotmenu", "footer"]
  };
  window.GOOSE_CONFIG = CONFIG;

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* storage blocked: fine */ } }
  };
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Wire external ordering/secret links from config */
  $$("[data-order-link]").forEach(function (a) { a.href = CONFIG.orderingUrl; a.target = "_blank"; a.rel = "noopener"; });
  $$("[data-tel]").forEach(function (a) { a.href = "tel:+1" + CONFIG.phone; });

  /* ---- Header ---- */
  var header = $(".site-header");
  var onScroll = function () { if (header) header.classList.toggle("is-scrolled", window.scrollY > 12); };
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* ---- Mobile drawer ---- */
  var drawer = $("#drawer"), opener = $("[data-drawer-open]"), closer = $("[data-drawer-close]");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("is-open", open);
    drawer.setAttribute("aria-hidden", String(!open));
    drawer.inert = !open;
    opener && opener.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    (open ? closer : opener) && (open ? closer : opener).focus();
  }
  if (drawer) { drawer.inert = true; }
  opener && opener.addEventListener("click", function () { setDrawer(true); });
  closer && closer.addEventListener("click", function () { setDrawer(false); });
  $$("#drawer a").forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && drawer.classList.contains("is-open")) setDrawer(false); });

  /* ---- Announcement ---- */
  var ann = $("[data-announce]");
  if (ann) {
    var key = "goose-ann-" + ann.getAttribute("data-announce");
    var until = ann.getAttribute("data-until");
    var today = nyDate().ymd;
    if (store.get(key) || (until && today > until)) ann.hidden = true;
    var x = $("button", ann);
    x && x.addEventListener("click", function () { ann.hidden = true; store.set(key, 1); });
  }

  /* ---- Open / closed status (computed in Bethlehem's time zone) ---- */
  function nyDate() {
    var parts = {};
    try {
      new Intl.DateTimeFormat("en-US", { timeZone: CONFIG.tz, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", weekday: "short", hour12: false })
        .formatToParts(new Date()).forEach(function (p) { parts[p.type] = p.value; });
    } catch (e) { var d = new Date(); return { ymd: d.toISOString().slice(0, 10), dow: d.getDay(), mins: d.getHours() * 60 + d.getMinutes() }; }
    var dows = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    var h = parseInt(parts.hour, 10) % 24;
    return { ymd: parts.year + "-" + parts.month + "-" + parts.day, dow: dows[parts.weekday], mins: h * 60 + parseInt(parts.minute, 10) };
  }
  function fmt(m) { var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? "pm" : "am"; h = h % 12 || 12; return h + (mm ? ":" + String(mm).padStart(2, "0") : "") + ap; }
  function status() {
    var n = nyDate();
    var closure = CONFIG.closures.filter(function (c) { return n.ymd >= c.from && n.ymd <= c.to; })[0];
    if (closure) return { open: false, text: closure.label };
    var t = CONFIG.hours[n.dow];
    if (t && n.mins >= t[0] && n.mins < t[1]) {
      var left = t[1] - n.mins;
      return { open: true, text: left <= 45 ? "Open · closes soon (" + fmt(t[1]) + ")" : "Open now · till " + fmt(t[1]) };
    }
    if (t && n.mins < t[0]) return { open: false, text: "Closed · opens " + fmt(t[0]) };
    for (var i = 1; i <= 7; i++) {
      var d = (n.dow + i) % 7, nt = CONFIG.hours[d];
      if (nt) return { open: false, text: "Closed · opens " + ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][d] + " " + fmt(nt[0]) };
    }
    return { open: false, text: "Closed" };
  }
  function paintStatus() {
    var s = status();
    $$("[data-status]").forEach(function (el) {
      el.classList.toggle("is-open", s.open); el.classList.toggle("is-closed", !s.open);
      var t = $("span", el); if (t) t.textContent = s.text;
    });
    var dow = nyDate().dow;
    $$("[data-day]").forEach(function (tr) { tr.classList.toggle("is-today", Number(tr.getAttribute("data-day")) === dow); });
  }
  paintStatus(); setInterval(paintStatus, 60000);

  /* ---- Reveal on scroll ---- */
  var reveals = $$(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else reveals.forEach(function (el) { el.classList.add("is-in"); });

  /* ---- Menu page ---- */
  var menuRoot = $("#menu-root");
  if (menuRoot && window.GOOSE_MENU) renderMenu(menuRoot, window.GOOSE_MENU);

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function renderMenu(root, data) {
    var chips = $("#menu-chips");
    var html = "";
    data.forEach(function (cat) {
      chips && chips.insertAdjacentHTML("beforeend", '<a class="chip" href="#' + cat.id + '" data-chip="' + cat.id + '">' + esc(cat.name) + "</a>");
      html += '<section class="menu-cat" id="' + cat.id + '" aria-labelledby="h-' + cat.id + '"><div class="menu-cat__head"><h2 id="h-' + cat.id + '">' + esc(cat.name) +
        (cat.id === "items" ? ' <button class="egg" type="button" data-egg="sides" aria-label="A golden egg"><svg viewBox="0 0 22 28" aria-hidden="true"><use href="/assets/img/sprite.svg#i-egg"/></svg></button>' : "") +
        "</h2><p>" + esc(cat.blurb) + '</p></div><ul class="menu-list">';
      cat.items.forEach(function (it) {
        var price;
        if (!it.p.length) price = '<span class="ask">Ask in store</span>';
        else if (it.p.length === 1) price = "<span>$" + esc(it.p[0]) + "</span>";
        else price = it.p.map(function (p, i) { return "<span><small>" + esc((it.sizes || [])[i] || "") + "</small>$" + esc(p) + "</span>"; }).join("");
        html += '<li class="mi" data-search="' + esc((it.n + " " + it.d + " " + cat.name).toLowerCase()) + '"><div class="mi__name"><span class="mi__n">' + esc(it.n) + "</span>" +
          (it.tag ? '<span class="tag' + (it.tag === "Veggie" ? " tag--green" : it.tag === "Breakfast" ? " tag--gold" : "") + '">' + esc(it.tag) + "</span>" : "") +
          '</div><div class="mi__price">' + price + "</div>" + (it.d ? '<p class="mi__desc">' + esc(it.d) + "</p>" : "") + "</li>";
      });
      html += "</ul></section>";
    });
    root.innerHTML = html;
    bindEggs(root);

    // search
    var input = $("#menu-search"), empty = $("#menu-empty"), count = $("#menu-count");
    input && input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase(), shown = 0;
      $$(".menu-cat", root).forEach(function (sec) {
        var any = 0;
        $$(".mi", sec).forEach(function (li) {
          var hit = !q || li.getAttribute("data-search").indexOf(q) > -1;
          li.hidden = !hit; if (hit) { any++; shown++; }
          var n = $(".mi__n", li), raw = n.textContent;
          n.innerHTML = q && hit ? esc(raw).replace(new RegExp("(" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>") : esc(raw);
        });
        sec.hidden = !any;
      });
      if (empty) empty.hidden = shown > 0;
      if (count) count.textContent = q ? shown + " item" + (shown === 1 ? "" : "s") + " match “" + input.value.trim() + "”" : "";
    });

    // scrollspy for chips
    if ("IntersectionObserver" in window && chips) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          $$(".chip", chips).forEach(function (c) { c.classList.toggle("is-active", c.getAttribute("data-chip") === en.target.id); });
          var active = $('.chip[data-chip="' + en.target.id + '"]', chips);
          active && chips.scrollTo({ left: active.offsetLeft - 16, behavior: reduceMotion ? "auto" : "smooth" });
        });
      }, { rootMargin: "-40% 0px -55% 0px" });
      $$(".menu-cat", root).forEach(function (s) { spy.observe(s); });
    }
  }

  /* ---- Golden egg hunt → secret menu ---- */
  var found = store.get("goose-eggs") || [];
  var meter = $("#hunt-meter"), toastEl = $("#toast"), vault = $("#vault");
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg; toastEl.classList.add("is-on");
    clearTimeout(toast.t); toast.t = setTimeout(function () { toastEl.classList.remove("is-on"); }, 3200);
  }
  function paintMeter() {
    if (!meter) return;
    var dots = $(".hunt-meter__eggs", meter);
    dots.innerHTML = CONFIG.eggs.map(function (id) { return '<i class="' + (found.indexOf(id) > -1 ? "on" : "") + '"></i>'; }).join("");
    $(".hunt-meter__txt", meter).textContent = found.length >= CONFIG.eggs.length ? "Vault unlocked" : found.length + " / " + CONFIG.eggs.length + " golden eggs";
    meter.classList.toggle("is-visible", found.length > 0);
    $$("[data-vault-open]").forEach(function (b) { b.hidden = found.length < CONFIG.eggs.length; });
  }
  function bindEggs(scope) {
    $$("[data-egg]", scope).forEach(function (egg) {
      var id = egg.getAttribute("data-egg");
      if (found.indexOf(id) > -1) { egg.hidden = true; return; }
      egg.addEventListener("click", function () {
        if (found.indexOf(id) > -1) return;
        found.push(id); store.set("goose-eggs", found);
        egg.classList.add("is-found");
        setTimeout(function () { egg.hidden = true; }, 700);
        paintMeter();
        var left = CONFIG.eggs.length - found.length;
        if (left > 0) toast(["Honk! A golden egg.", "Nice nest-raiding.", "The geese are getting nervous.", "One more and the vault creaks open…"][Math.min(found.length - 1, 3)] + " " + left + " to go.");
        else { toast("HONK HONK! The vault is open."); setTimeout(openVault, 650); }
      });
    });
  }
  function openVault() {
    if (!vault) return;
    if (typeof vault.showModal === "function") vault.showModal(); else vault.setAttribute("open", "");
    confetti();
  }
  if (vault) {
    $$("[data-vault-close]", vault).forEach(function (b) { b.addEventListener("click", function () { vault.close ? vault.close() : vault.removeAttribute("open"); }); });
    vault.addEventListener("click", function (e) { if (e.target === vault) vault.close(); });
    $$("[data-secret-link]").forEach(function (a) { a.href = CONFIG.secretUrl; });
  }
  $$("[data-vault-open]").forEach(function (b) { b.addEventListener("click", openVault); });
  bindEggs(document); paintMeter();

  // Type "honk" anywhere for a hint
  var buf = "";
  document.addEventListener("keydown", function (e) {
    if (/input|textarea|select/i.test((e.target.tagName || ""))) return;
    buf = (buf + (e.key || "")).slice(-4).toLowerCase();
    if (buf === "honk") toast(found.length >= CONFIG.eggs.length ? "You already cracked it. Footer → The Vault." : "Hint: eggs hide near the hoagie, the founders’ story, the sides, the hot buffet & the very bottom.");
  });

  function confetti() {
    if (reduceMotion) return;
    var c = document.createElement("canvas"); c.className = "confetti"; document.body.appendChild(c);
    var ctx = c.getContext("2d"), W = c.width = innerWidth, H = c.height = innerHeight;
    var cols = ["#c8963e", "#8fb36a", "#e7c98a", "#a5382a", "#f7f3e6"], ps = [];
    for (var i = 0; i < 140; i++) ps.push({ x: W / 2, y: H / 2, vx: (Math.random() - .5) * 16, vy: Math.random() * -16 - 4, s: Math.random() * 8 + 4, c: cols[i % 5], r: Math.random() * 6, vr: (Math.random() - .5) * .3 });
    var f = 0;
    (function tick() {
      ctx.clearRect(0, 0, W, H);
      ps.forEach(function (p) { p.vy += .45; p.x += p.vx; p.y += p.vy; p.r += p.vr; ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r); ctx.fillStyle = p.c; ctx.fillRect(-p.s / 2, -p.s / 3, p.s, p.s / 1.6); ctx.restore(); });
      if (++f < 160) requestAnimationFrame(tick); else c.remove();
    })();
  }

  /* ---- Forms ---- */
  function validate(form) {
    var ok = true, first = null;
    $$(".field", form).forEach(function (f) {
      var el = $("input, select, textarea", f); if (!el) return;
      var bad = !el.checkValidity();
      f.classList.toggle("has-error", bad);
      el.setAttribute("aria-invalid", String(bad));
      if (bad && !first) first = el;
      if (bad) ok = false;
    });
    first && first.focus();
    return ok;
  }
  $$("form[data-validate]").forEach(function (form) {
    $$("input, select, textarea", form).forEach(function (el) {
      el.addEventListener("blur", function () {
        var f = el.closest(".field"); if (!f || !el.value) return;
        var bad = !el.checkValidity(); f.classList.toggle("has-error", bad); el.setAttribute("aria-invalid", String(bad));
      });
    });
  });

  // Account tabs
  var tabs = $$("[role=tab]");
  tabs.forEach(function (t) {
    t.addEventListener("click", function () { selectTab(t); });
    t.addEventListener("keydown", function (e) {
      var i = tabs.indexOf(t);
      if (e.key === "ArrowRight" || e.key === "ArrowLeft") { e.preventDefault(); var n = tabs[(i + (e.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length]; selectTab(n); n.focus(); }
    });
  });
  function selectTab(t) {
    tabs.forEach(function (x) { var on = x === t; x.setAttribute("aria-selected", String(on)); x.tabIndex = on ? 0 : -1; $("#" + x.getAttribute("aria-controls")).hidden = !on; });
    history.replaceState(null, "", "#" + t.getAttribute("aria-controls").replace("panel-", ""));
  }
  if (tabs.length) {
    var want = location.hash.replace("#", "");
    var pick = tabs.filter(function (t) { return t.getAttribute("aria-controls") === "panel-" + want; })[0];
    if (pick) selectTab(pick);
  }
  $$("[data-tab-go]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); var t = document.getElementById(a.getAttribute("data-tab-go")); if (t) { selectTab(t); t.focus(); } }); });
  $$("[data-pw-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var inp = b.parentNode.querySelector("input"); var show = inp.type === "password";
      inp.type = show ? "text" : "password"; b.textContent = show ? "Hide" : "Show"; b.setAttribute("aria-pressed", String(show));
    });
  });

  // Account forms: this preview never transmits or stores credentials.
  // At launch, point these at the deli's secure ordering system (see README).
  $$("form[data-account]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if ($(".hp input", form) && $(".hp input", form).value) return; // bot
      if (!validate(form)) return;
      var st = $(".form-status", form);
      st.hidden = false;
      st.innerHTML = "This preview doesn’t send or save anything. Accounts and ordering currently run on The Goose’s ordering system — " +
        '<a href="' + CONFIG.orderingUrl + '" target="_blank" rel="noopener">continue there</a>.';
      $$("input[type=password]", form).forEach(function (p) { p.value = ""; });
    });
  });

  // Catering inquiry: builds an email draft (nothing is sent from this site).
  var inq = $("#inquiry");
  if (inq) inq.addEventListener("submit", function (e) {
    e.preventDefault();
    if ($(".hp input", inq).value) return;
    if (!validate(inq)) return;
    var d = new FormData(inq), body = [];
    ["name", "phone", "email", "date", "guests", "service", "details"].forEach(function (k) { if (d.get(k)) body.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + d.get(k)); });
    var st = $(".form-status", inq); st.hidden = false;
    if (CONFIG.email) {
      location.href = "mailto:" + CONFIG.email + "?subject=" + encodeURIComponent("Catering inquiry — " + (d.get("date") || "")) + "&body=" + encodeURIComponent(body.join("\n"));
      st.textContent = "Your email app should open with your inquiry filled in. Prefer the phone? Call (610) 868-0176.";
    } else {
      st.innerHTML = 'Thanks! The quickest way to book is a call: <a href="tel:+16108680176">(610) 868-0176</a>. Mention your date and headcount and they’ll take it from there.';
    }
  });

  // Year
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
