#!/usr/bin/env python3
"""Generate the inner pages of the Chocolate Fountain Heaven site from shared chrome."""
import pathlib

SITE = pathlib.Path(__file__).parent / "site"

NAV = """<header class="nav" id="nav">
  <a class="wordmark" href="index.html" aria-label="Chocolate Fountain Heaven, home">
    <b>Chocolate Fountain Heaven</b>
    <span>Cranberry Township &middot; Pittsburgh</span>
  </a>
  <nav class="nav__links" aria-label="Main">
    <a href="fountains.html"{A1}>Fountains</a>
    <a href="weddings.html"{A2}>Weddings</a>
    <a href="gallery.html"{A3}>Gallery</a>
    <a href="ranch.html"{A4}>Ranch Fountain</a>
    <a href="faq.html"{A5}>FAQ</a>
    <a href="contact.html"{A6}>Contact</a>
    <a class="nav__cta" href="contact.html">Reserve a date</a>
  </nav>
  <button class="nav__toggle" aria-label="Open menu" aria-expanded="false"><span></span></button>
</header>

<div class="drawer" aria-hidden="true">
  <button class="drawer__close" aria-label="Close menu">&times;</button>
  <a href="index.html">Home</a>
  <a href="fountains.html">Fountains</a>
  <a href="weddings.html">Weddings</a>
  <a href="gallery.html">Gallery</a>
  <a href="ranch.html">Ranch Fountain</a>
  <a href="faq.html">FAQ</a>
  <a href="contact.html">Contact</a>
  <div class="drawer__meta">724-339-9658 &middot; info@chocolatefountainheaven.com</div>
</div>"""

FOOT = """<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div class="foot__brand">
        <b>Chocolate Fountain Heaven</b>
        <p>Sephra chocolate fountains and event music, serving Pittsburgh and the surrounding counties since 1989.</p>
      </div>
      <div>
        <h4>Visit</h4>
        <ul>
          <li>117 Middleground Pl</li>
          <li>Cranberry Twp, PA 16066</li>
          <li><a href="tel:+17243399658">724-339-9658</a></li>
          <li><a href="mailto:info@chocolatefountainheaven.com">info@chocolatefountainheaven.com</a></li>
        </ul>
      </div>
      <div>
        <h4>Pages</h4>
        <ul>
          <li><a href="fountains.html">Fountains &amp; packages</a></li>
          <li><a href="weddings.html">Wedding receptions</a></li>
          <li><a href="ranch.html">Ranch dressing fountain</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="faq.html">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Serving</h4>
        <ul>
          <li>Pittsburgh &middot; Cranberry &middot; Butler</li>
          <li>Fox Chapel &middot; Oakmont &middot; Monroeville</li>
          <li>South Hills &middot; New Castle &middot; Kittanning</li>
          <li>And The Greenbrier Resort, West Virginia</li>
        </ul>
      </div>
    </div>
    <div class="foot__bar">
      <span>&copy; <span data-year>2026</span> Chocolate Fountain Heaven. All rights reserved.</span>
      <span>Prices exclude 6% Pennsylvania sales tax.</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23150d09'/%3E%3Cpath d='M32 12c8 0 14 6 14 13s-6 12-14 12-14-5-14-12 6-13 14-13zm0 6c-4 0-8 3-8 7s4 6 8 6 8-2 8-6-4-7-8-7zm0 16c5 0 9 2 9 2v16H23V36s4-2 9-2z' fill='%23cfa46a'/%3E%3C/svg%3E">
</head>
<body>
"""


def page(fname, title, desc, active, body):
    flags = {f"A{i}": "" for i in range(1, 7)}
    if active:
        flags[active] = ' aria-current="page"'
    nav = NAV.format(**flags)
    html = HEAD.format(title=title, desc=desc) + nav + "\n<main id=\"main\">\n" + body + "\n</main>\n" + FOOT
    (SITE / fname).write_text(html, encoding="utf-8")
    print(fname, len(html))


def pagehead(crumb, title, lede):
    return f"""  <div class="wrap pagehead">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</div>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>"""


# ------------------------------------------------------------------ fountains
fountains = pagehead("Fountains", "Fountains &amp; packages",
    "Four Sephra fountains, from a 19-inch cash-and-carry to the six-tier Majestic. Every attended fountain includes delivery, set-up, an attendant, tear-down and clean-up.") + """
  <section class="section section--cream">
    <div class="wrap chapter">
      <div class="chapter__no">01</div>
      <div>
        <div class="chapter__head"><h2>The small fountain</h2><span class="aside">19 inches &middot; cash &amp; carry or attended</span></div>
        <div class="feature" style="align-items:start">
          <div>
            <p class="lede">The Sephra Signature Home Fondue Fountain. Elegant brushed stainless steel and a WhisperQuiet motor &mdash; the perfect addition to a home party or a smaller celebration.</p>
            <p>Choose it unattended and run it yourself, or add an attendant and let us handle the evening. Pick-up is two days before your event, return two days after, unless we agree otherwise.</p>
          </div>
          <div>
            <div class="menu" style="border-top:1px solid var(--line)">
              <div class="menu__row" style="grid-template-columns:1fr auto">
                <div class="menu__name">Cash &amp; carry <small>Deposit $350, returned</small></div>
                <div class="menu__price">Rental quoted</div>
              </div>
              <div class="menu__row" style="grid-template-columns:1fr auto">
                <div class="menu__name">Attended <small>2.5 hours included</small></div>
                <div class="menu__price">From $500</div>
              </div>
            </div>
          </div>
        </div>

        <div class="menu" style="margin-top:2.5rem" data-reveal>
          <div class="menu__row">
            <div class="menu__name">What is in the box <small>Cash &amp; carry</small></div>
            <p class="menu__desc">Electric double boiler for melting chocolate. Seven pounds of premium chocolate. 250 wooden skewers for dipping. Unlimited use of the fountain during your event. You set up, operate and clean it; you collect it and bring it back.</p>
            <div class="menu__price">&mdash;</div>
          </div>
          <div class="menu__row">
            <div class="menu__name">The deposit <small>Cash only</small></div>
            <p class="menu__desc">A $350 cash security deposit &mdash; no personal cheques &mdash; is due when you collect the fountain, and you receive a receipt. Return it in the condition it left in and the $350 comes straight back to you, against a signed receipt.</p>
            <div class="menu__price">$350</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap chapter">
      <div class="chapter__no">02</div>
      <div>
        <div class="chapter__head"><h2>The attended fountains</h2><span class="aside">34 and 44 inches</span></div>
        <div class="feature">
          <div class="feature__media" data-reveal>
            <img src="img/fountain.jpg" alt="A Sephra chocolate fountain flowing over several tiers">
            <span class="feature__cap">Attended &middot; full service</span>
          </div>
          <div data-reveal>
            <p class="lede">The 34-inch fountain is our full-service workhorse. The 44-inch Majestic &mdash; six tiers &mdash; is the one that stops conversation.</p>
            <ul style="list-style:none;padding:0;margin:1.4rem 0 0;border-top:1px solid var(--line)">
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">Delivery, set-up, tear-down and clean-up</li>
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">Two and a half hours of pouring</li>
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">Sephra milk or dark chocolate</li>
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">Dipping items, priced per person</li>
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">An attendant &mdash; often two &mdash; for the whole event</li>
              <li style="padding:.7rem 0;border-bottom:1px solid var(--line)">Fabric-dressed base in your colours</li>
            </ul>
            <p class="small" style="margin-top:1.2rem;color:rgba(21,13,9,.62)">Extra time beyond the contract is $35 per half hour. Additional chocolate for larger guest counts is included in the quote.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap chapter">
      <div class="chapter__no">03</div>
      <div>
        <div class="chapter__head"><h2>Booking &amp; payment</h2><span class="aside">What reserves a date</span></div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2.4rem" data-reveal>
          <div>
            <span class="eyebrow" style="color:var(--brass-lt)">The deposit</span>
            <p style="margin-top:.8rem;color:rgba(244,236,221,.75)">A signed contract and a $200 non-refundable deposit reserve your date. A date is not held until the deposit arrives. Cash, Venmo, personal cheque or card.</p>
          </div>
          <div>
            <span class="eyebrow" style="color:var(--brass-lt)">The balance</span>
            <p style="margin-top:.8rem;color:rgba(244,236,221,.75)">Due fifteen days before the event. A cheque in the post holds a date for three business days only. Two contracts go out by mail after the deposit &mdash; sign one, keep one, return the other.</p>
          </div>
          <div>
            <span class="eyebrow" style="color:var(--brass-lt)">The small print</span>
            <p style="margin-top:.8rem;color:rgba(244,236,221,.75)">Prices exclude 6% Pennsylvania sales tax. Reservations are first come, first served. Attended service starts at $500 for smaller events and varies with the details.</p>
          </div>
        </div>
        <p style="margin-top:2.6rem"><a class="btn btn--light" href="contact.html">Check your date</a></p>
      </div>
    </div>
  </section>

  <section class="section section--cream">
    <div class="wrap" data-reveal>
      <span class="eyebrow eyebrow--line">Occasions</span>
      <h2 style="margin:1rem 0 2.4rem">If people are gathering</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2rem">
        <div><h3>Weddings &amp; receptions</h3><p class="small" style="color:rgba(21,13,9,.7)">The centrepiece, dressed in fabrics to match your colours.</p></div>
        <div><h3>Birthdays</h3><p class="small" style="color:rgba(21,13,9,.7)">Children and adults of any age. Personalised and unhurried.</p></div>
        <div><h3>Business &amp; charity</h3><p class="small" style="color:rgba(21,13,9,.7)">Office gatherings, association meetings, fundraisers.</p></div>
        <div><h3>Any small event</h3><p class="small" style="color:rgba(21,13,9,.7)">Showers, graduations, holidays, anniversaries, celebrations of life.</p></div>
      </div>
    </div>
  </section>
"""
page("fountains.html",
     "Fountains &amp; Packages — Chocolate Fountain Heaven, Pittsburgh",
     "Sephra chocolate fountain rentals: 19-inch cash-and-carry or attended, 34-inch and the six-tier 44-inch Majestic. Delivery, attendant and clean-up included.",
     "A1", fountains)

# ------------------------------------------------------------------ weddings
weddings = pagehead("Weddings", "A heavenly reception",
    "Indulge in a dreamy wedding reception: a cascading wonder of chocolate, elegant decor and a joyful room. Your date deserves the centrepiece people photograph.") + """
  <section class="section">
    <div class="wrap feature">
      <div class="feature__media" data-reveal>
        <img src="img/hero.jpg" alt="Bride and groom feeding each other chocolate at their reception">
        <span class="feature__cap">Chocolicious matrimony</span>
      </div>
      <div data-reveal>
        <span class="eyebrow eyebrow--line">For the day itself</span>
        <h2 style="margin:1.1rem 0 1.2rem">The sweetest <em>focal point</em> in the room.</h2>
        <p>An expertly dressed chocolate fountain captivates guests with the aroma and the cascading layers of premium, velvety chocolate. A wide selection of dippers &mdash; succulent fruits, delicate pastries &mdash; indulges every palate.</p>
        <p>Our attendants oversee every detail, keeping the fountain decadent and spotless throughout. You focus on the day; we keep the table perfect.</p>
        <a class="btn" href="contact.html">Enquire about your date</a>
      </div>
    </div>
  </section>

  <section class="section section--cream">
    <div class="wrap chapter">
      <div class="chapter__no">01</div>
      <div>
        <div class="chapter__head"><h2>What we bring</h2><span class="aside">Nothing left to arrange</span></div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:2.4rem" data-reveal>
          <div>
            <h3>The fountain</h3>
            <p class="small" style="color:rgba(21,13,9,.72)">A 19, 34 or 44-inch Sephra fountain &mdash; the Majestic for the largest rooms. Milk or dark chocolate, always Sephra.</p>
          </div>
          <div>
            <h3>The dressing</h3>
            <p class="small" style="color:rgba(21,13,9,.72)">Designer fabrics chosen to match your colour scheme, wrapped and styled around the base before guests arrive.</p>
          </div>
          <div>
            <h3>The attendant</h3>
            <p class="small" style="color:rgba(21,13,9,.72)">Professionally dressed, on hand all evening, replenishing dippers and keeping the presentation immaculate.</p>
          </div>
          <div>
            <h3>The music</h3>
            <p class="small" style="color:rgba(21,13,9,.72)">Gerra and Rick perform ceremony music and cocktail hour. Ask us to quote the two together.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap defn" data-reveal>
      <div>
        <blockquote>
          <p>&ldquo;One visit to the fountain is simply not enough &mdash; it is an experience you will want to <em>savour again and again.</em>&rdquo;</p>
          <cite>Chocolate Fountain Heaven</cite>
        </blockquote>
      </div>
      <div>
        <h3 style="margin-bottom:1rem">A note on timing</h3>
        <p>Most couples run the fountain during the appetiser hour. Our package includes two and a half hours, which is usually plenty. If you would rather keep it pouring through dinner and dancing, additional time is quoted at $35 per half hour.</p>
        <p>We arrive ninety minutes before your start time, so the aroma meets guests as they walk in.</p>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap" data-reveal style="text-align:left">
      <span class="eyebrow eyebrow--line" style="color:var(--brass-lt)">Trusted by</span>
      <h2 style="margin:1.2rem 0;max-width:26ch">The finest rooms in Western Pennsylvania &mdash; and one in West Virginia.</h2>
      <p style="color:rgba(244,236,221,.72);max-width:56ch">We are the preferred vendor at many of the area's hotels, country clubs and banquet facilities, from Pittsburgh and Cranberry to Kittanning, New Castle, the South Hills, Butler, Monroeville, Oakmont and Fox Chapel. The Greenbrier Resort calls us too.</p>
      <p style="margin-top:2rem"><a class="btn btn--light" href="gallery.html">See the receptions</a></p>
    </div>
  </section>
"""
page("weddings.html",
     "Wedding Receptions — Chocolate Fountain Heaven, Pittsburgh",
     "Chocolate fountains for Pittsburgh wedding receptions: Sephra chocolate, designer fabric dressing, an attendant all evening, and ceremony music from Gerra and Rick.",
     "A2", weddings)

# ------------------------------------------------------------------ ranch
ranch = pagehead("Ranch Dressing Fountain", "The Ranch Dressing Fountain",
    "Something savoury before something sweet. A 19-inch attended fountain of ranch dressing, for the guests who want a fried pickle at the reception.") + """
  <section class="section">
    <div class="wrap feature feature--flip">
      <div class="feature__media" data-reveal>
        <img src="img/table.jpg" alt="A catered table with a chocolate fountain and bowls of dippers">
        <span class="feature__cap">New for 2026</span>
      </div>
      <div data-reveal>
        <span class="eyebrow eyebrow--line">New addition</span>
        <h2 style="margin:1.1rem 0 1.2rem">Ranch, <em>on tap.</em></h2>
        <p>Our Ranch Dressing Fountain pairs perfectly with crunchy fried vegetables such as mushrooms and cauliflower, crispy fresh vegetables, fried pickles, chicken tenders and wings, french fries and tater tots, mozzarella sticks.</p>
        <div class="menu" style="margin-top:2rem">
          <div class="menu__row" style="grid-template-columns:1fr auto">
            <div class="menu__name">19&Prime; Attended <small>2.5 hours</small></div>
            <div class="menu__price">$495</div>
          </div>
          <div class="menu__row" style="grid-template-columns:1fr auto">
            <div class="menu__name">Guests <small>Serves up to</small></div>
            <div class="menu__price">150</div>
          </div>
          <div class="menu__row" style="grid-template-columns:1fr auto">
            <div class="menu__name">Service area <small>Pittsburgh area</small></div>
            <div class="menu__price">&mdash;</div>
          </div>
        </div>
        <p class="small" style="margin-top:1.4rem;color:rgba(21,13,9,.62)">Only the attended 19-inch fountain is offered for ranch dressing events.</p>
      </div>
    </div>
  </section>

  <section class="section section--cream">
    <div class="wrap chapter">
      <div class="chapter__no">01</div>
      <div>
        <div class="chapter__head"><h2>The important notice</h2><span class="aside">Caterer, not us</span></div>
        <div class="defn" style="grid-template-columns:1.2fr 1fr">
          <div data-reveal>
            <p class="lede">Dipping items and plating for the Ranch Dressing Fountain are provided by your caterer. Chocolate Fountain Heaven supplies the fountain, the dressing and the attendant.</p>
            <p>Ask your caterer to plan the fried and fresh vegetables, the pickles and the tenders &mdash; and to arrange the plating. We will keep the dressing moving and the table clean.</p>
          </div>
          <div data-reveal style="border-left:1px solid var(--line);padding-left:2rem">
            <span class="eyebrow">Good to know</span>
            <p class="small" style="margin-top:.9rem;color:rgba(21,13,9,.72)">The ranch fountain is indoors only, on a sturdy, level table, with a 120-volt grounded outlet within ten feet. Two and a half hours is included. Extra time is $35 per half hour.</p>
          </div>
        </div>
        <p style="margin-top:2.4rem"><a class="btn btn--solid" href="contact.html">Add it to your quote</a></p>
      </div>
    </div>
  </section>
"""
page("ranch.html",
     "Ranch Dressing Fountain — Chocolate Fountain Heaven, Pittsburgh",
     "The Ranch Dressing Fountain: a 19-inch attended fountain for fried pickles, chicken tenders, wings, fries, mozzarella sticks. $495 for 2.5 hours, up to 150 guests.",
     "A4", ranch)

# ------------------------------------------------------------------ faq
faqs = [
    ("Can you tell me more about what you do?",
     "Chocolate Fountain Heaven offers the best quality chocolate fountain services in the area. In addition to the fountains, Gerra and Rick are musicians who perform for wedding ceremonies, cocktail hour music, funerals and memorial services. Call us to hear the music or to book a service."),
    ("What kind of chocolate do you use?",
     "Sephra chocolate, formulated for chocolate fountains so no oil is needed. Milk or dark, in all our fountains. It has had rave reviews."),
    ("What is the maximum number of guests a fountain will serve?",
     "The quote for a large fountain includes enough chocolate for the number of guests attending. Additional chocolate for a larger guest count is included in the quote. The 44-inch Majestic works from 100 to 2,000 guests."),
    ("Which dipping items are not recommended?",
     "Anything that breaks apart easily or crumbles &mdash; especially pound cake, which compromises the smooth flow of the chocolate. We recommend angel food cake instead: it has a more substantial texture than the regular version."),
    ("Do you provide the dipping items?",
     "Yes. Because of liability and freshness, only Chocolate Fountain Heaven provides the dipping items. They are priced on a per-person basis and included in your quote."),
    ("Can the fountain be used outside?",
     "We do not recommend it. The fountain has such a sweet, inviting aroma that every heavenly creature in the garden is tempted to partake. Chocolate also needs a stable temperature, and outdoor conditions affect its integrity."),
    ("How long can we have the fountain?",
     "Most people use it during the appetiser segment. Our package includes two and a half hours of fountain enjoyment. If you want it throughout the event, additional time can be quoted; beyond the contract it is $35 per half hour."),
    ("Who is responsible for set-up, tear-down and clean-up?",
     "We are. We arrive about ninety minutes before the start time so guests smell the chocolate as they enter. A professionally dressed attendant is there at all times, showing guests how to enjoy the fountain and keeping it pristine. Presentation matters to us; attendants replenish the accompaniments and keep the table looking its best."),
    ("What are the table and electrical requirements?",
     "A 120-volt grounded outlet within ten feet of the fountain, and a sturdy table. If the table is not level, the chocolate will not flow properly. Please reconfirm both with your banquet manager before the event, so set-up is not delayed. The facility should also provide a table skirt."),
    ("Who decorates the area around the fountain?",
     "We do. For a wedding reception, baby shower, graduation, birthday or Halloween party, we incorporate theme-based fabrics around the base. For weddings we use designer fabrics that match your colour scheme."),
    ("What happens to the leftover chocolate?",
     "Bring a few small plastic containers with tight-fitting lids and we will send the premium chocolate home with you. It keeps beautifully for about a year in the freezer. If you would rather not, it is disposed of. We never recycle chocolate from customer to customer."),
    ("What is required to reserve the fountain?",
     "A $200 non-refundable deposit. All major credit cards are accepted through PayPal on the site, or by calling with the card number. A cheque holds the date for three business days only. After the deposit we send two contracts by mail: sign both, keep one, return the other. The balance is due two weeks before the event."),
]
items = "\n".join(
    f"""        <div class="faq__item" data-reveal>
          <div class="q-n">{i:02d}</div>
          <div><h3>{q}</h3><p>{a}</p></div>
        </div>""" for i, (q, a) in enumerate(faqs, 1))

faq = pagehead("FAQ", "Questions, answered",
    "Chocolate, guests, timing, power, leftovers and the deposit. If your question is not here, call 724-339-9658 &mdash; we answer the phone.") + f"""
  <section class="section">
    <div class="wrap faq">
      <div class="faq__side" data-reveal>
        <span class="eyebrow eyebrow--line">Twelve answers</span>
        <h2 style="margin:1rem 0">Everything we are asked</h2>
        <p class="small" style="color:rgba(21,13,9,.62)">Still unsure? Email <a href="mailto:info@chocolatefountainheaven.com" style="border-bottom:1px solid var(--brass)">info@chocolatefountainheaven.com</a> or call <a href="tel:+17243399658" style="border-bottom:1px solid var(--brass)">724-339-9658</a>.</p>
      </div>
      <div>
{items}
      </div>
    </div>
  </section>

  <section class="section section--dark section--tight">
    <div class="wrap" data-reveal style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:1.6rem">
      <h2 style="max-width:22ch">One more question? Ask us directly.</h2>
      <a class="phone-big" href="tel:+17243399658" style="color:var(--cream)">724-339-9658</a>
    </div>
  </section>
"""
page("faq.html",
     "FAQ — Chocolate Fountain Heaven, Pittsburgh",
     "Answers about Sephra chocolate, guest counts, dipping items, indoor use, timing, set-up, electrical requirements, leftover chocolate and deposits.",
     "A5", faq)

# ------------------------------------------------------------------ contact
contact = pagehead("Contact", "Let us pour",
    "Tell us the date, the venue and the number of guests. We will come back with a quote, usually the same day.") + """
  <section class="section" style="padding-top:0">
    <div class="wrap cta" style="align-items:start">
      <div data-reveal>
        <div class="menu" style="border-top:1px solid var(--line)">
          <div class="menu__row" style="grid-template-columns:140px 1fr;gap:1.4rem">
            <div class="menu__name" style="font-size:1rem">Phone</div>
            <div><a class="phone-big" href="tel:+17243399658" style="font-size:clamp(1.5rem,2.6vw,2rem)">724-339-9658</a></div>
          </div>
          <div class="menu__row" style="grid-template-columns:140px 1fr;gap:1.4rem">
            <div class="menu__name" style="font-size:1rem">Email</div>
            <div><a href="mailto:info@chocolatefountainheaven.com" style="font-family:var(--serif);font-size:1.15rem;border-bottom:1px solid var(--brass)">info@chocolatefountainheaven.com</a></div>
          </div>
          <div class="menu__row" style="grid-template-columns:140px 1fr;gap:1.4rem">
            <div class="menu__name" style="font-size:1rem">Studio</div>
            <div><p style="margin:0">117 Middleground Pl<br>Cranberry Twp, PA 16066<br>United States</p></div>
          </div>
          <div class="menu__row" style="grid-template-columns:140px 1fr;gap:1.4rem">
            <div class="menu__name" style="font-size:1rem">Serving</div>
            <div><p style="margin:0">Pittsburgh and the surrounding areas &mdash; Cranberry, Butler, Kittanning, New Castle, the South Hills, Monroeville, Oakmont, Fox Chapel, and The Greenbrier Resort in West Virginia.</p></div>
          </div>
        </div>
        <div style="margin-top:2.4rem">
          <span class="eyebrow eyebrow--line">Before you write</span>
          <p class="small" style="margin-top:1rem;color:rgba(21,13,9,.68);max-width:46ch">A date is reserved by a signed contract and a $200 non-refundable deposit. The balance is due fifteen days before the event. Prices exclude 6% Pennsylvania sales tax.</p>
        </div>
      </div>

      <div data-reveal>
        <form class="form" data-mailto style="background:var(--ink);padding:clamp(1.6rem,3vw,2.6rem);color:var(--cream)">
          <span class="eyebrow" style="color:var(--brass-lt)">Event inquiry</span>
          <div class="form__row">
            <div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" required></div>
            <div class="field"><label for="c-date">Event date</label><input id="c-date" name="date" type="date"></div>
          </div>
          <div class="form__row">
            <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required></div>
            <div class="field"><label for="c-phone">Phone</label><input id="c-phone" name="phone" type="tel"></div>
          </div>
          <div class="field"><label for="c-venue">Venue</label><input id="c-venue" name="venue" type="text" placeholder="Where is the event?"></div>
          <div class="field"><label for="c-guests">Guests</label><input id="c-guests" name="guests" type="text" placeholder="Approximate number"></div>
          <div class="field"><label for="c-fountain">Interested in</label>
            <select id="c-fountain" name="fountain">
              <option>Not sure yet</option>
              <option>19&Prime; attended fountain</option>
              <option>19&Prime; cash &amp; carry</option>
              <option>34&Prime; attended fountain</option>
              <option>44&Prime; Majestic (six tier)</option>
              <option>Ranch Dressing Fountain</option>
              <option>Ceremony music</option>
            </select>
          </div>
          <div class="field"><label for="c-notes">Anything we should know</label><textarea id="c-notes" name="notes" placeholder="Timing, colours, dietary notes, the plan so far…"></textarea></div>
          <button class="btn btn--solid" type="submit" style="background:var(--brass);color:var(--paper)">Send the inquiry</button>
          <p class="small" data-form-note style="color:rgba(244,236,221,.55);margin:0">This form opens your email app. You can also write to info@chocolatefountainheaven.com or call 724-339-9658.</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section section--cream section--tight">
    <div class="wrap" data-reveal style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2rem">
      <div><span class="eyebrow">Weddings</span><p class="small" style="margin-top:.7rem;color:rgba(21,13,9,.7)">Book the fountain and the ceremony music together.</p></div>
      <div><span class="eyebrow">Corporate</span><p class="small" style="margin-top:.7rem;color:rgba(21,13,9,.7)">Office gatherings, charity evenings, association meetings.</p></div>
      <div><span class="eyebrow">Celebrations of life</span><p class="small" style="margin-top:.7rem;color:rgba(21,13,9,.7)">Music and chocolate, handled quietly and with care.</p></div>
      <div><span class="eyebrow">Ranch fountain</span><p class="small" style="margin-top:.7rem;color:rgba(21,13,9,.7)">Something savoury for the cocktail hour.</p></div>
    </div>
  </section>
"""
page("contact.html",
     "Contact — Chocolate Fountain Heaven, Cranberry Township PA",
     "Call 724-339-9658 or write to info@chocolatefountainheaven.com. 117 Middleground Pl, Cranberry Twp, PA 16066. Reserve a date with a signed contract and $200 deposit.",
     "A6", contact)

# ------------------------------------------------------------------ gallery
shots = [
    ("g01", "Reception &middot; Pittsburgh"), ("g02", "Banquet table"), ("g03", "Strawberries &amp; chocolate"),
    ("g04", "Bride &amp; groom"), ("g05", "Dessert table"), ("g06", "The Majestic"),
    ("g07", "Guests at the fountain"), ("g08", "Evening reception"), ("g09", "Four tiers"),
    ("g10", "Cocktail hour"), ("g11", "The pour"), ("g12", "Country club"),
]
figs = "\n".join(
    f"""        <figure><img src="img/{n}.jpg" alt="Chocolate fountain event photography" loading="lazy" data-full="img/{n}.jpg"><figcaption>{c}</figcaption></figure>"""
    for n, c in shots)
gallery = pagehead("Gallery", "Nights we have poured for",
    "Receptions, banquets, country clubs and quiet family parties. A small selection &mdash; the fountain photographs well in any room.") + f"""
  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="masonry" data-reveal>
{figs}
      </div>
      <div style="margin-top:2.4rem;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:1.2rem">
        <p class="small" style="color:rgba(21,13,9,.6);margin:0">Click any photograph to enlarge.</p>
        <a class="btn" href="contact.html">Ask about your date</a>
      </div>
    </div>
  </section>

  <div class="lb" role="dialog" aria-label="Photograph viewer" aria-modal="true">
    <button class="lb__close" aria-label="Close">&times;</button>
    <button class="lb__prev" aria-label="Previous">&#8249;</button>
    <img src="img/g01.jpg" alt="">
    <button class="lb__next" aria-label="Next">&#8250;</button>
  </div>
"""
page("gallery.html",
     "Gallery — Chocolate Fountain Heaven, Pittsburgh",
     "Photographs from Chocolate Fountain Heaven events across Pittsburgh, Cranberry, Butler and The Greenbrier Resort.",
     "A3", gallery)
