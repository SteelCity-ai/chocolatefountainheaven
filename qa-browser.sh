#!/bin/sh
set -eu
export PATH=/root/.bun/bin:/opt/node24/bin:$PATH
B=/opt/gstack/browse/dist/browse
BASE=${1:-http://172.25.0.2:4179}
for width in 320 768 1024 1440; do
  "$B" viewport "${width}x900"
  for page in index contact gallery; do
    "$B" goto "$BASE/$page.html"
    "$B" js '(()=>{if(document.documentElement.scrollWidth>innerWidth)throw Error("Horizontal overflow");if(document.querySelectorAll("h1").length!==1)throw Error("Expected one H1");return "Responsive checks passed: "+location.pathname+" at "+innerWidth;})()'
  done
done
"$B" viewport 375x812 --scale 2
"$B" goto "$BASE/contact.html"
"$B" click .nav__toggle
"$B" js '(()=>{if(document.querySelector(".nav__toggle").getAttribute("aria-expanded")!=="true")throw Error("Menu expanded state");if(document.activeElement!==document.querySelector(".drawer__close"))throw Error("Menu focus");return "Menu opened with focus";})()'
"$B" press Shift+Tab
"$B" js '(()=>{if(!document.querySelector(".drawer").contains(document.activeElement))throw Error("Focus escaped menu");return "Menu contains focus";})()'
"$B" press Escape
"$B" js '(()=>{if(document.querySelector(".nav__toggle").getAttribute("aria-expanded")!=="false"||document.activeElement!==document.querySelector(".nav__toggle"))throw Error("Menu close/return focus");if(document.querySelector("form button[type=submit]").textContent!=="Open email draft")throw Error("Email handoff label");return "Menu closed; email handoff is labeled";})()'
"$B" goto "$BASE/gallery.html"
"$B" click '.plates figure:first-child'
"$B" js '(()=>{if(document.querySelector(".lb").getAttribute("aria-hidden")!=="false"||document.activeElement!==document.querySelector(".lb__close"))throw Error("Gallery open/focus");return "Gallery opened with focus";})()'
"$B" press Shift+Tab
"$B" js '(()=>{if(document.activeElement!==document.querySelector(".lb__next"))throw Error("Gallery focus containment");return "Gallery contains focus";})()'
"$B" press ArrowRight
"$B" press Escape
"$B" js '(()=>{if(document.querySelector(".lb").getAttribute("aria-hidden")!=="true"||document.activeElement!==document.querySelectorAll(".plates figure")[1])throw Error("Gallery close/return focus");return "Gallery closed and returned focus";})()'
"$B" press Enter
"$B" js '(()=>{if(!document.querySelector(".lb").classList.contains("is-open"))throw Error("Keyboard gallery opening");return "Gallery keyboard opening passed";})()'
"$B" press Escape
# Gallery must actually become visible. Regression guard for STE-840: a
# full-height gallery previously stayed at opacity 0 forever because its
# IntersectionObserver ratio could never cross 8%.
for size in 1024x900 390x844; do
  "$B" viewport "$size"
  "$B" goto "$BASE/gallery.html"
  sleep 2
  "$B" js '(()=>{var g=document.querySelector(".plates[data-reveal]");if(!g)throw Error("Gallery grid missing");var op=getComputedStyle(g).opacity;if(op!=="1")throw Error("Gallery grid hidden at opacity "+op);var imgs=Array.prototype.slice.call(document.querySelectorAll(".plates img"));var shown=imgs.filter(function(i){return i.complete&&i.naturalWidth>0;});if(!shown.length)throw Error("No gallery photograph loaded");if(document.querySelectorAll(".plates figure").length<60)throw Error("Gallery photo count unexpectedly low");return "Gallery visible at "+innerWidth+"x"+innerHeight+" with "+shown.length+" photographs decoded";})()'
done
"$B" viewport 1440x900
"$B" console --errors
