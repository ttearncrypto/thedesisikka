/* The DESI Sikka — site JS: live search, clock, archive dropdown, nav toggle */
(function () {
  "use strict";

  var base = document.documentElement.getAttribute("data-baseurl") || "";

  /* ---------- Live search ---------- */
  var index = null;

  function loadIndex(cb) {
    if (index) return cb(index);
    fetch(base + "/search.json")
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; cb(data); })
      .catch(function () { cb([]); });
  }

  function score(item, q) {
    var t = item.title.toLowerCase();
    var x = (item.text || "").toLowerCase();
    var c = (item.cat || "").toLowerCase();
    var n = 0;
    if (t.indexOf(q) !== -1) n += t.indexOf(q) === 0 ? 5 : 3;
    if (c.indexOf(q) !== -1) n += 2;
    if (x.indexOf(q) !== -1) n += 1;
    return n;
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }

  function renderResults(box, input, max) {
    var q = input.value.trim().toLowerCase();
    if (!q) {
      box.innerHTML = "";
      box.classList.remove("has-results");
      return;
    }
    loadIndex(function (items) {
      var hits = items
        .map(function (it) { return { it: it, s: score(it, q) }; })
        .filter(function (h) { return h.s > 0; })
        .sort(function (a, b) { return b.s - a.s; })
        .slice(0, max);
      if (!hits.length) {
        box.innerHTML = '<p class="search-empty">No matches for &ldquo;' + escapeHtml(input.value.trim()) + '&rdquo;.</p>';
        box.classList.add("has-results");
        return;
      }
      box.innerHTML = hits.map(function (h) {
        return '<a class="search-hit" href="' + h.it.url + '">' +
          '<span class="search-hit-cat">' + escapeHtml(h.it.cat) + '</span>' +
          '<span class="search-hit-title">' + escapeHtml(h.it.title) + '</span>' +
          '<span class="search-hit-date">' + escapeHtml(h.it.date) + '</span></a>';
      }).join("");
      box.classList.add("has-results");
    });
  }

  function wireSearch(inputId, boxId, max) {
    var input = document.getElementById(inputId);
    var box = document.getElementById(boxId);
    if (!input || !box) return;
    input.addEventListener("input", function () { renderResults(box, input, max); });

    /* header overlay open/close */
    var toggle = document.querySelector(".search-toggle");
    var panel = document.getElementById("search-panel");
    if (toggle && panel && inputId === "header-search-input") {
      toggle.addEventListener("click", function () {
        var open = panel.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        if (open) input.focus(); else input.value = "";
        if (!open) box.classList.remove("has-results");
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
          panel.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
          box.classList.remove("has-results");
        }
      });
      panel.addEventListener("click", function (e) {
        if (e.target.closest("a")) {
          panel.classList.remove("open");
          box.classList.remove("has-results");
        }
      });
    }
  }

  wireSearch("header-search-input", "header-search-results", 8);
  wireSearch("page-search-input", "page-search-results", 50);

  /* prefill standalone search page from ?q= */
  var pageInput = document.getElementById("page-search-input");
  if (pageInput) {
    var qs = new URLSearchParams(window.location.search).get("q");
    if (qs) {
      pageInput.value = qs;
      renderResults(document.getElementById("page-search-results"), pageInput, 50);
    }
    window.addEventListener("load", function () { pageInput.focus(); });
  }

  /* ---------- Live IST clock ---------- */
  var clock = document.getElementById("live-clock");
  if (clock) {
    var fmt = new Intl.DateTimeFormat("en-IN", {
      weekday: "long", day: "numeric", month: "short",
      hour: "2-digit", minute: "2-digit", second: "2-digit",
      hour12: false, timeZone: "Asia/Kolkata"
    });
    function tick() { clock.textContent = fmt.format(new Date()).replace(",", " ·") + " IST"; }
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- Archive month dropdown ---------- */
  var select = document.getElementById("archive-select");
  if (select) {
    select.addEventListener("change", function () {
      if (select.value) window.location.href = base + "/archive/#m-" + select.value;
    });
  }

  /* ---------- Mobile nav ---------- */
  var navToggle = document.querySelector(".nav-toggle");
  if (navToggle) {
    navToggle.addEventListener("click", function () {
      var open = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", open ? "false" : "true");
      document.getElementById("mobile-nav").classList.toggle("open");
    });
  }
})();
