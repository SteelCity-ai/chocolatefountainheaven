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
    toggle.addEventListener('click', function () {
      drawer.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    });
    var shut = function () {
      drawer.classList.remove('is-open');
      document.body.style.overflow = '';
    };
    if (close) close.addEventListener('click', shut);
    drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', shut); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') shut(); });
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
  var figures = Array.prototype.slice.call(document.querySelectorAll('.masonry figure'));
  var current = 0;
  var openLb = function (i) {
    if (!lb || !lbImg) return;
    current = (i + figures.length) % figures.length;
    var img = figures[current].querySelector('img');
    lbImg.src = img.getAttribute('data-full') || img.src;
    lbImg.alt = img.alt;
    lb.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };
  var closeLb = function () {
    if (!lb) return;
    lb.classList.remove('is-open');
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
      d.forEach(function (v, k) { if (v) body.push(k + ': ' + v); });
      var subject = 'Event inquiry — ' + (d.get('name') || 'website');
      window.location.href = 'mailto:info@chocolatefountainheaven.com?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body.join('\n'));
      var note = form.querySelector('[data-form-note]');
      if (note) note.textContent = 'Opening your email app… or write to info@chocolatefountainheaven.com';
    });
  }
})();
