/* Chocolate Fountain Heaven — interaction layer (vanilla, no dependencies) */
(function () {
  'use strict';

  /* sticky nav */
  var nav = document.querySelector('.nav');
  var onScroll = function () {
    if (!nav) return;
    nav.classList.toggle('is-stuck', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* drawer */
  var toggle = document.querySelector('.nav__toggle');
  var drawer = document.querySelector('.drawer');
  var close = document.querySelector('.drawer__close');
  if (toggle && drawer) {
    var setState = function (open) {
      drawer.classList.toggle('is-open', open);
      drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    };
    toggle.addEventListener('click', function () {
      var open = !drawer.classList.contains('is-open');
      setState(open);
      if (open && close) close.focus();
    });
    var shut = function (restore) {
      if (!drawer.classList.contains('is-open')) return;
      setState(false);
      if (restore) toggle.focus();
    };
    if (close) close.addEventListener('click', function () { shut(true); });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { shut(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') shut(true);
      if (e.key === 'Tab' && drawer.classList.contains('is-open')) {
        var f = drawer.querySelectorAll('a, button');
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* photo rotation (home hero arches): crossfade + slow zoom.
     Stays on the first photo when reduced motion is requested. */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.cyc').forEach(function (box, k) {
    var imgs = Array.prototype.slice.call(box.querySelectorAll('img'));
    if (!imgs.length) return;
    var i = 0, ms = parseInt(box.getAttribute('data-cycle'), 10) || 5000, timer = null;
    imgs[0].classList.add('on');
    box.classList.add('is-ready');
    if (reduce || imgs.length < 2) return;
    var step = function () {
      imgs[i].classList.remove('on');
      i = (i + 1) % imgs.length;
      imgs[i].classList.add('on');
    };
    var play = function () { if (!timer) timer = window.setInterval(step, ms); };
    var stop = function () { window.clearInterval(timer); timer = null; };
    window.setTimeout(play, k * 1300);
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else play(); });
  });

  /* count-up numbers in the hero proof row */
  var counters = document.querySelectorAll('[data-n]');
  var runCount = function (el) {
    var n = parseFloat(el.getAttribute('data-n')), dec = n % 1 ? 1 : 0, t0 = null;
    var f = function (t) {
      if (t0 === null) t0 = t;
      var p = Math.min((t - t0) / 1400, 1);
      el.textContent = (n * (1 - Math.pow(1 - p, 3))).toFixed(dec);
      if (p < 1) window.requestAnimationFrame(f); else el.textContent = String(n);
    };
    window.requestAnimationFrame(f);
  };
  if (!reduce && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (x) { if (x.isIntersecting) { runCount(x.target); cio.unobserve(x.target); } });
    }, { threshold: .5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* floating "Reserve a date" button after the first screen (not on Contact) */
  if (!/contact\.html$/.test(location.pathname)) {
    var sticky = document.createElement('div');
    sticky.className = 'sticky-cta';
    sticky.innerHTML = '<a class="btn btn--solid" href="contact.html">Reserve a date <i aria-hidden="true">&rarr;</i></a>';
    document.body.appendChild(sticky);
    var onS = function () { sticky.classList.toggle('show', window.scrollY > window.innerHeight * 0.7); };
    window.addEventListener('scroll', onS, { passive: true });
    onS();
  }

  /* reveal on scroll */
  var revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('is-in');
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* lightbox */
  var lb = document.querySelector('.lb');
  var lbImg = lb ? lb.querySelector('img') : null;
  var figures = Array.prototype.slice.call(document.querySelectorAll('.plates figure'));
  var current = 0;
  var openLb = function (i) {
    if (!lb || !lbImg) return;
    current = (i + figures.length) % figures.length;
    var img = figures[current].querySelector('img');
    lbImg.src = img.getAttribute('data-full') || img.src;
    lbImg.alt = img.alt;
    lb.classList.add('is-open');
    lb.setAttribute('aria-hidden', 'false');
    lb.querySelector('.lb__close').focus();
    document.body.style.overflow = 'hidden';
  };
  var closeLb = function () {
    if (!lb) return;
    lb.classList.remove('is-open');
    lb.setAttribute('aria-hidden', 'true');
    if (figures[current]) figures[current].focus();
    document.body.style.overflow = '';
  };
  figures.forEach(function (f, i) {
    f.addEventListener('click', function () { openLb(i); });
    f.setAttribute('tabindex', '0');
    f.setAttribute('role', 'button');
    f.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLb(i); }
    });
  });
  if (lb) {
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    var c = lb.querySelector('.lb__close'); if (c) c.addEventListener('click', closeLb);
    var p = lb.querySelector('.lb__prev'); if (p) p.addEventListener('click', function (e) { e.stopPropagation(); openLb(current - 1); });
    var n = lb.querySelector('.lb__next'); if (n) n.addEventListener('click', function (e) { e.stopPropagation(); openLb(current + 1); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Tab') {
        var buttons = lb.querySelectorAll('button');
        var first = buttons[0], last = buttons[buttons.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowLeft') openLb(current - 1);
      if (e.key === 'ArrowRight') openLb(current + 1);
    });
  }

  /* year */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* form: mailto handoff (no backend on static host) */
  var form = document.querySelector('form[data-mailto]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var body = [];
      form.querySelectorAll('input[name], select[name], textarea[name]').forEach(function (el) {
        if (!el.value) return;
        var label = el.id && form.querySelector('label[for="' + el.id + '"]');
        var key = label ? label.textContent.trim() : el.name;
        body.push(key + ': ' + el.value);
      });
      var subject = 'Event inquiry — ' + (d.get('name') || 'website');
      window.location.href = 'mailto:info@chocolatefountainheaven.com?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body.join('\n'));
      var note = form.querySelector('[data-form-note]');
      if (note) note.textContent = 'Opening your email app… or write to info@chocolatefountainheaven.com';
    });
  }
})();
