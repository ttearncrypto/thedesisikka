/* The DESI Sikka — site JS: search, clock, archive, nav, reader tools, shortcuts */
(function () {
  "use strict";

  var base = document.documentElement.getAttribute("data-baseurl") || "";

  /* ================= Live search ================= */
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
    return String(s).replace(/[&<>"']/g, function (ch) {
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

  function openSearchPanel() {
    var panel = document.getElementById("search-panel");
    var input = document.getElementById("header-search-input");
    var toggle = document.querySelector(".search-toggle");
    if (panel && !panel.classList.contains("open")) {
      panel.classList.add("open");
      if (toggle) toggle.setAttribute("aria-expanded", "true");
    }
    if (input) input.focus();
  }

  function wireSearch(inputId, boxId, max) {
    var input = document.getElementById(inputId);
    var box = document.getElementById(boxId);
    if (!input || !box) return;
    input.addEventListener("input", function () { renderResults(box, input, max); });

    var toggle = document.querySelector(".search-toggle");
    var panel = document.getElementById("search-panel");
    if (toggle && panel && inputId === "header-search-input") {
      toggle.addEventListener("click", function () {
        var open = panel.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        if (open) input.focus(); else input.value = "";
        if (!open) box.classList.remove("has-results");
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

  /* ================= Live IST clock ================= */
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

  /* ================= Archive month dropdown ================= */
  var select = document.getElementById("archive-select");
  if (select) {
    select.addEventListener("change", function () {
      if (select.value) window.location.href = base + "/archive/#m-" + select.value;
    });
  }

  /* ================= Mobile nav ================= */
  var navToggle = document.querySelector(".nav-toggle");
  if (navToggle) {
    navToggle.addEventListener("click", function () {
      var open = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", open ? "false" : "true");
      document.getElementById("mobile-nav").classList.toggle("open");
    });
  }

  /* ================= Article tools ================= */
  var body = document.getElementById("article-body");

  /* font size */
  if (body) {
    var MIN = 14, MAX = 22;
    var size = parseInt(localStorage.getItem("tds-prose-size") || "", 10);
    if (!size || size < MIN || size > MAX) size = 15;

    function applySize() {
      body.style.fontSize = size + "px";
      localStorage.setItem("tds-prose-size", String(size));
    }
    applySize();

    var dec = document.getElementById("font-dec");
    var inc = document.getElementById("font-inc");
    if (dec) dec.addEventListener("click", function () { size = Math.max(MIN, size - 1); applySize(); });
    if (inc) inc.addEventListener("click", function () { size = Math.min(MAX, size + 1); applySize(); });
  }

  /* print */
  var printBtn = document.getElementById("print-btn");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  /* listen (Web Speech API) */
  var listenBtn = document.getElementById("listen-btn");
  if (listenBtn && body && "speechSynthesis" in window) {
    var speaking = false;

    function articleText() {
      var clone = body.cloneNode(true);
      clone.querySelectorAll(".legal-box, .also-read").forEach(function (el) { el.remove(); });
      return clone.textContent.replace(/\s+/g, " ").trim();
    }

    listenBtn.addEventListener("click", function () {
      if (speaking) {
        speechSynthesis.cancel();
        speaking = false;
        listenBtn.setAttribute("aria-pressed", "false");
        listenBtn.classList.remove("active");
        return;
      }
      var u = new SpeechSynthesisUtterance(articleText());
      u.rate = 1;
      u.onend = u.onerror = function () {
        speaking = false;
        listenBtn.setAttribute("aria-pressed", "false");
        listenBtn.classList.remove("active");
      };
      speechSynthesis.cancel();
      speechSynthesis.speak(u);
      speaking = true;
      listenBtn.setAttribute("aria-pressed", "true");
      listenBtn.classList.add("active");
    });

    window.addEventListener("beforeunload", function () { speechSynthesis.cancel(); });
  } else if (listenBtn) {
    listenBtn.disabled = true;
    listenBtn.title = "Not supported in this browser";
  }

  /* copy link buttons */
  document.querySelectorAll(".copy-link-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var url = btn.getAttribute("data-url") || window.location.href;
      function done() {
        var label = btn.querySelector(".copy-label");
        if (label) {
          var old = label.textContent;
          label.textContent = "Copied!";
          setTimeout(function () { label.textContent = old; }, 1600);
        }
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done).catch(function () { fallbackCopy(url, done); });
      } else {
        fallbackCopy(url, done);
      }
    });
  });

  function fallbackCopy(text, done) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); done(); } catch (e) { /* noop */ }
    document.body.removeChild(ta);
  }

  /* ================= Also Read injector ================= */
  if (body) {
    var dataEl = document.getElementById("also-read-data");
    var slug = body.closest(".article-column");
    var seedStr = slug ? (slug.getAttribute("data-slug") || "x") : "x";

    function hashCode(s) {
      var h = 0;
      for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; }
      return Math.abs(h);
    }

    try {
      var items = JSON.parse(dataEl ? dataEl.textContent : "[]");
      var paras = Array.prototype.slice.call(body.children).filter(function (el) {
        return el.tagName === "P" && !el.classList.contains("disclaimer") ;
      });
      if (items.length >= 2 && paras.length >= 6) {
        var seed = hashCode(seedStr);
        var n = paras.length;
        var posA = Math.min(n - 3, Math.max(2, Math.round(n * 0.35) + (seed % 3)));
        var posB = Math.min(n - 1, Math.max(posA + 3, Math.round(n * 0.72) + ((seed >> 2) % 3)));
        [posA, posB].forEach(function (pos, idx) {
          var picks = [];
          for (var k = 0; k < 2; k++) {
            picks.push(items[(seed + idx * 2 + k) % items.length]);
          }
          var wrap = document.createElement("aside");
          wrap.className = "also-read";
          wrap.setAttribute("aria-label", "Also read");
          wrap.innerHTML =
            '<h3><span class="pulse-dot"></span>Also Read</h3>' +
            picks.map(function (p) {
              return '<a href="' + p.u + '">' +
                '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>' +
                '<span>' + escapeHtml(p.t) + '</span></a>';
            }).join("");
          body.insertBefore(wrap, paras[pos].nextSibling);
        });
      }
    } catch (e) { /* malformed data: skip */ }
  }

  /* ================= Comments (lazy utterances) ================= */
  document.querySelectorAll(".comments-box").forEach(function (details) {
    details.addEventListener("toggle", function () {
      if (!details.open || details.dataset.loaded) return;
      var holder = details.querySelector(".comments-body");
      if (!holder) return;
      var s = document.createElement("script");
      s.src = "https://utteranc.es/client.js";
      s.setAttribute("repo", holder.getAttribute("data-repo"));
      s.setAttribute("issue-term", holder.getAttribute("data-issue-term"));
      s.setAttribute("theme", "dark-blue");
      s.setAttribute("crossorigin", "anonymous");
      s.async = true;
      holder.appendChild(s);
      details.dataset.loaded = "1";
    });
  });

  /* ================= Keyboard shortcuts ================= */
  function isTyping(el) {
    if (!el) return false;
    var tag = el.tagName;
    return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || el.isContentEditable;
  }

  var helpEl = null;
  function toggleHelp() {
    if (helpEl) {
      helpEl.remove();
      helpEl = null;
      return;
    }
    helpEl = document.createElement("div");
    helpEl.id = "kbd-help";
    helpEl.innerHTML =
      '<div class="kbd-card">' +
      '<h3>Keyboard shortcuts</h3>' +
      '<ul>' +
      '<li><kbd>N</kbd> Next news</li>' +
      '<li><kbd>P</kbd> Previous news</li>' +
      '<li><kbd>/</kbd> Search</li>' +
      '<li><kbd>?</kbd> Toggle this help</li>' +
      '<li><kbd>Esc</kbd> Close panels</li>' +
      '</ul></div>';
    document.body.appendChild(helpEl);
  }

  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (isTyping(document.activeElement)) return;
    var key = e.key;

    if (key === "Escape") {
      var panel = document.getElementById("search-panel");
      if (panel) panel.classList.remove("open");
      if (helpEl) { helpEl.remove(); helpEl = null; }
      return;
    }
    if (key === "/") { e.preventDefault(); openSearchPanel(); return; }
    if (key === "?") { e.preventDefault(); toggleHelp(); return; }

    var k = key.toLowerCase();
    if (k === "n") {
      var next = document.querySelector(".post-nav a.next");
      if (next) window.location.href = next.getAttribute("href");
    } else if (k === "p") {
      var prev = document.querySelector(".post-nav a.prev");
      if (prev) window.location.href = prev.getAttribute("href");
    }
  });
})();
