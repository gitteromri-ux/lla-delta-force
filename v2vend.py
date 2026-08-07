# -*- coding: utf-8 -*-
"""Track 1 v2 vendor data, transcribed from track1_vendors_v2.md.
No em dashes, no en dashes, no exclamation marks, no emojis."""

HERO_CHIPS = [
    ("48.5", "top score, Astoria Company", "Out of a raw maximum of 60, evidence confidence 1.00"),
    ("35", "vendors assessed on the five success factors", "Five scored in full, thirty carried in the coverage list"),
    ("134", "quotable operator URLs from a 442 source harvest", "183 of 332 queued pages returned usable text"),
    ("$250", "break even per appointment at a 20 percent close", "$1,249 times 0.20 equals $249.80"),
]

HEADLINE = {
    "tag": "HEADLINE FINDING",
    "title": "No vendor anywhere publishes a longevity or health education lead price, so every number here is a read across.",
    "body": [
        "That vertical does not exist as a traded product. Every candidate price below is read across from an adjacent vertical, and the vertical it is read across from is named on every row so the assumption stays visible.",
        "The intent verification machinery the industry runs on, TrustedForm certificates, Jornaya LeadiD tokens, IVR screening, billable duration thresholds, litigator scrubs and written return windows, was built for insurance, legal, home services and finance. Health, wellness and consumer education sit outside it. Any vendor that says yes to a longevity course is running a custom media buy, not selling inventory off a shelf.",
        "The strategic move is to buy calls, not forms. The current Meta problem is a form problem. A consumer who dials a number and stays on the line past ninety seconds is a different animal from a consumer who taps a pre filled instant form, and every published contact rate ladder in Section D says so.",
    ],
    "reads": [
        ("Medicare, ACA and health insurance inbound calls",
         "55 to 65 plus demographic, consumer dialled the phone, IVR screened, 60 to 120 second billable threshold",
         "The caller wants subsidised coverage, not a $1,249 course. Intent is insurance, not self improvement."),
        ("Education and EDU inquiry",
         "Consumer is in enrol in a program headspace, consent and compliance infrastructure is mature",
         "Audience is 18 to 45 degree seekers, not 55 to 64 health optimisers."),
        ("High ticket coaching and course appointment setting",
         "Exact price point and exact sales motion, $3,000 to $25,000 programmes, booked calls",
         "Almost all business to business, tiny operators, no TrustedForm, no published dispute policy."),
        ("Data only audience segments, health and wellness",
         "Exact demographic and psychographic targeting",
         "Zero consumer action means zero intent. This is media targeting, not leads."),
    ],
}

COREG = {
    "title": "Co registration is disqualifying at its own published price.",
    "body": "Co registration leads trade at $0.50 to $2.00 and are generated when a consumer signs up for one thing online and, during that process, also agrees to receive messages from a health insurance agency. A consumer who never asked about the product and is worth fifty cents cannot be sold a $1,249 course. Reject co registration, incentivized and sweepstakes inventory outright, and apply the same logic to aged leads at pennies to $0.50 and to the rebound leads line inside the PX marketplace.",
    "src": ("theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
}

SCORE_HEADERS = ["Rank", "Vendor", "1. Mechanism x1.25", "2. Verification x1.25", "3. B2C fit x1.5",
                 "4. Real price x1.0", "5. Speed and access x1.0", "Raw out of 60", "Evidence confidence", "Final"]
SCORE_ROWS = [
    ("1", "Astoria Company", "9", "9", "6", "8", "9", "48.50", "1.00", "48.5"),
    ("2", "Aragon Advertising", "9", "7", "4", "9", "9", "44.00", "1.00", "44.0"),
    ("3", "PX, px.com", "8", "7", "8", "4", "7", "41.75", "0.95", "39.7"),
    ("4", "LeadsNow.ai", "7", "6", "8", "8", "6", "42.25", "0.85", "35.9"),
    ("5", "Alliant, AnalyticsIQ", "3", "3", "9", "4", "7", "32.00", "1.00", "32.0"),
]
SCORE_MATH = [
    "Astoria 11.25 plus 11.25 plus 9.00 plus 8 plus 9 equals 48.50, times 1.00 equals 48.5",
    "Aragon 11.25 plus 8.75 plus 6.00 plus 9 plus 9 equals 44.00, times 1.00 equals 44.0",
    "PX 10.00 plus 8.75 plus 12.00 plus 4 plus 7 equals 41.75, times 0.95 equals 39.7",
    "LeadsNow 8.75 plus 7.50 plus 12.00 plus 8 plus 6 equals 42.25, times 0.85 equals 35.9",
    "Alliant 3.75 plus 3.75 plus 13.50 plus 4 plus 7 equals 32.00, times 1.00 equals 32.0",
]
SCORE_NOTE = ("Weights sum to 6.0, so the raw maximum is 60. Confidence multipliers are stated openly. "
              "PX carries 0.95 because it publishes no price, no minimum and no named commercial contact, so a third of the commercial picture is unverifiable. "
              "LeadsNow.ai carries 0.85 because everything known comes from one self published page, the company is Australia headquartered with no US entity found, there is no TrustedForm or Jornaya, no named executive and no third party review corroboration. Every other multiplier is 1.00.")

# --------------------------------------------------------------- vendor cards
VENDORS = [
 {
  "rank": "1", "score": "48.5", "name": "Astoria Company",
  "kind": "Pay per call plus host and post and ping and post web leads. The only vendor that clears all five factors with published, citable evidence.",
  "f1": ("Pay per call plus host and post and ping and post. Astoria's own LeadsCon 2026 exhibitor entry states it generates leads via website SEO, host and post, ping and post and pay per call. The product page lists pay per call, call tracking, click to call, call analytics and search keyword call services. Not co registration, not incentivized, not sweepstakes on the pay per call product.",
         [("LeadsCon 2026 exhibitors", "https://www.leadscon.com/event/leadscon-las-vegas-2026/sponsors-exhibitors/"), ("astoriacompany.com/pay-per-call", "https://www.astoriacompany.com/pay-per-call")]),
  "f2": ("The strongest published verification record of any vendor found. Billable duration doctrine published in full: a typical range is 30 to 90 seconds, 60 seconds is a safe starting point, for high ticket verticals like legal or medical consider 90 seconds, a 120 second minimum may filter out many legitimate leads. Certificate delivery is written into the seller terms: Astoria may provide consent records, source information, TrustedForm certificates, Jornaya LeadiD, call recordings where available and permitted, and call logs. The honest caveat is also in the contract: leads and calls generally consist of consumer self reported information and may not be independently verified by Astoria. Written dispute window: if the insertion order is silent, buyer must submit documented disputes or return requests by the tenth day of the month following delivery. The sister property publishes a tighter policy still, leads must be returned within seven calendar days, returns go to returns@astorialeads.com and the remedy is credit rather than refund. The live consent banner on Astoria's own site names ActiveProspect TrustedForm and Jornaya as active partners, so the certificate pipeline is running rather than marketed. Buyer facing pre payment call listen is not stated anywhere, so treat it as unknown.",
         [("Minimum call duration guide", "https://www.astoriacompany.com/setting-the-right-minimum-call-duration-for-pay-per-call"), ("Astoria seller terms", "https://www.astoriacompany.com/seller-terms"), ("AstoriaLeads terms of service", "https://astorialeads.com/terms-of-service.php"), ("Consent banner, contact page", "https://www.astoriacompany.com/contact")]),
  "f3": ("Genuinely diversified, not a 90 percent Medicare book. Published verticals are mortgage, insurance, education, auto, legal, home services, moving and more than 100 pay per call campaigns. Education is a named published vertical, one of only two vendors in the report where that is true, the other being PX. A live Sylvan Tutoring Programs Canada offer was verified in the marketplace, which is consumer education in Canada, exactly the read across needed. No longevity, no wellness and no $1,000 plus consumer purchase is published.",
         [("LeadsCon 2026 exhibitors", "https://www.leadscon.com/event/leadscon-las-vegas-2026/sponsors-exhibitors/")]),
  "f4": ("Published per lead bands are $5 to $15 auto, $15 home improvement, $30 mortgage and above $100 legal, with pay per call insurance at $15 to $30 per call. Minimum spend published at $500 to $1,000 per month and a minimum test of $200 to $500 over 30 days. No education or health price is published, so the planning band for a 90 second IVR screened health adjacent consumer call is $30 to $60, read across from Astoria's own insurance pay per call at $15 to $30 plus the high ticket and medical premium its own duration guide implies. Canada is verified available through the Sylvan Canada offer. Exclusive against shared is published explicitly and both are sold.",
         [("astoriacompany.com/pay-per-call", "https://www.astoriacompany.com/pay-per-call")]),
  "f5": ("Launch a campaign in less than 30 minutes with our team, published on the pay per call page, with phone (510) 663-7016 on the same page. Named humans: Liza Schubert, lschubert@astoriacompany.com, plus Adnan Nazir and Scott Thompson, and a general bizdev@astoriacompany.com. LinkedIn URLs for the named people are not published on any Astoria page. Self serve signup is not published.",
         [("astoriacompany.com/pay-per-call", "https://www.astoriacompany.com/pay-per-call")]),
  "contacts": [("Liza Schubert, business development, lschubert@astoriacompany.com", "mailto:lschubert@astoriacompany.com"),
               ("bizdev@astoriacompany.com", "mailto:bizdev@astoriacompany.com"),
               ("Pay per call page and phone (510) 663-7016", "https://www.astoriacompany.com/pay-per-call"),
               ("Seller terms, for the dispute clause", "https://www.astoriacompany.com/seller-terms")],
  "verdict": "Start here. It is the only vendor with a written dated disputable return policy, certificate delivery in the contract, a named education vertical, a Canada offer, a test sized minimum and a 30 minute launch.",
  "subject": "90 second billable pay per call test, health education, $5,000 in 30 days",
  "email": """Liza,

Longevity Life Academy runs an 18 week live online longevity course at $1,249 upfront. Our buyer is 45 plus and 54.5 percent female, United States and Canada. We are moving budget off Meta lead forms and into consumer dialled calls, and your pay per call product is the first place we want to test.

The spec we want to run against, taken from your own published guidance on minimum call duration: 90 second billable threshold of connected non IVR conversation, IVR confirmation of age 45 or older and of United States or Canada geography, call recording delivered with every billable call, and same day duplicates non billable.

Three questions before we sign an insertion order.

1. What is your cost per billable call for a custom health education campaign at that spec, and what volume can you commit in 30 days.
2. Your seller terms reference TrustedForm certificates and Jornaya LeadiD. Will both be delivered on every web lead, and will call recordings be delivered with every billable call.
3. Your AstoriaLeads terms set a seven day return window with credit as the remedy. Can we carry that same seven day window into this insertion order rather than the tenth of the following month default.

Budget for the first cell is $5,000 across 30 days. Success is at least 60 billable calls at 15 percent or better call to sale.

Can you take a call this week.

Omri Gitter
Gita Agency, for Longevity Life Academy""",
 },
 {
  "rank": "2", "score": "44.0", "name": "Aragon Advertising",
  "kind": "Pure pay per call, consumer dialled. Best mechanism in the set, wrong shelf. Use it as a price check and a second source, not the lead horse.",
  "f1": ("Pure pay per call. Buying qualified inbound phone calls from in market customers instead of paying for clicks or form fills. You set the qualifying criteria, vertical, geography, hours and minimum call duration, and pay an agreed rate for each call that clears the bar. A tracked number connects each caller, often through an IVR menu that confirms basics, state, age band and homeownership, before a human picks up. Self described as the number one pay per call network in the world, and verified number one in the mThink Blue Book for eight years.",
         [("Aragon pay per call guide", "https://blog.aragon-advertising.com/posts/pay-per-call-marketing-guide/"), ("aragon-advertising.com/join", "https://aragon-advertising.com/join/")]),
  "f2": ("IVR confirming state, age band and homeownership, and the age band IVR is directly reusable for a 45 plus course. Published duration guidance: a call that lasts, say, 90 seconds filters out hang ups and misdials. Brutally honest published quality assurance number: industry wide, teams manually review only about 5 to 10 percent of their calls. On disputes there is only duplicate and return call rules, with no written return or credit policy published anywhere on the site. TrustedForm and Jornaya are not stated. Buyer access to call recordings is not stated. Best in class consent posture: the TCPA one to one consent rule was vacated by a federal court in early 2025 and formally eliminated by the FCC in September 2025, and consent and disclosure requirements remain strict. Aragon is the only vendor in the set with a correct current published TCPA position.",
         [("Aragon pay per call guide", "https://blog.aragon-advertising.com/posts/pay-per-call-marketing-guide/")]),
  "f3": ("This is the disqualifier. Published verticals are insurance including Medicare, final expense, ACA, auto and home, plus home services, legal, finance, credit repair, debt consolidation, health insurance, water damage, locksmith and television and internet. The advertiser page names only solar sales. The publisher page names only personal finance, fintech apps and money making opportunities. Consumer health, wellness, longevity, education, coaching and $1,000 plus consumer purchases are all not stated, and Canada is not stated. The honest verdict is that the real book is insurance, finance, legal and home services. It is not disqualified as a build partner, because Aragon can run a bespoke click to call campaign on its own media.",
         [("Aragon pay per call guide", "https://blog.aragon-advertising.com/posts/pay-per-call-marketing-guide/"), ("aragon-advertising.com/pay-per-call", "https://aragon-advertising.com/pay-per-call/")]),
  "f4": ("Best published price transparency in the industry. Medicare about $20 per call at about 20 percent close, final expense about $15, roofing about $60 at about 25 percent, pest control $30. Read across for a 90 second IVR screened health optimisation call is $40 to $75, read across from Aragon's own roofing band at $60 and its legal bands rather than from Medicare, because the LLA buyer is not benefit seeking and the qualification bar is higher. Minimum spend, minimum test, contract length and prepay terms are not published. The advertiser page states do not pay monthly management fees.",
         [("Aragon pay per call guide", "https://blog.aragon-advertising.com/posts/pay-per-call-marketing-guide/"), ("aragon-advertising.com/advertisers", "https://aragon-advertising.com/advertisers/")]),
  "f5": ("Live in days, not months. Published contacts advertisers@aragon-advertising.com and publishers@aragon-advertising.com, phone (646) 525-4019, 45 Main Street number 816, Brooklyn, New York 11201. Named humans: Todd Stearn, chief executive, and Nick Davies, associate director. LinkedIn URLs are not published. No self serve signup.",
         [("aragon-advertising.com/join", "https://aragon-advertising.com/join/")]),
  "contacts": [("advertisers@aragon-advertising.com", "mailto:advertisers@aragon-advertising.com"),
               ("Todd Stearn, chief executive, and Nick Davies, associate director, via the join page and phone (646) 525-4019", "https://aragon-advertising.com/join/"),
               ("Pay per call verticals page", "https://aragon-advertising.com/pay-per-call/")],
  "verdict": "Buy it as cell three of the test, to price check Astoria on identical specification. Do not make it the primary source until it shows a consumer health campaign it has actually run.",
  "subject": "Price check on a 90 second health education pay per call cell, $3,000",
  "email": """Todd, Nick,

Longevity Life Academy sells an 18 week live longevity course at $1,249 to a United States and Canada buyer who is 45 plus and 54.5 percent female. We are buying consumer dialled calls rather than form fills, and we are running two pay per call sources against the same specification in the same 30 days so the numbers are comparable.

Specification, taken from your own published guidance: 90 seconds of connected non IVR conversation as the billable threshold, IVR confirmation of age band 45 plus and of geography, duplicate rules where same day duplicates do not bill, and wrong numbers non billable.

Your published book is insurance, finance, legal and home services, and we have read it honestly. We are not asking you to have longevity inventory. We are asking you to run a bespoke click to call campaign on your own media against our offer, and to quote a cost per billable call at that spec.

Three questions.

1. What is your quoted rate per 90 second billable call for a health education offer, and what daily volume can you hold.
2. Will call recordings be delivered with every billable call and retained for 90 days.
3. Can you deliver in Canada with written confirmation of CASL express consent compliance, or is this United States only.

Cell budget is $3,000 across 30 days. The success test is a cost per billable call below the competing source at identical specification.

Omri Gitter
Gita Agency, for Longevity Life Academy""",
 },
 {
  "rank": "3", "score": "39.7", "name": "PX, px.com",
  "kind": "A marketplace, not a generator. The only marketplace publishing both health and education as first class verticals. Held back purely by commercial opacity.",
  "f1": ("A marketplace. Buyer side product line is leads, calls and appointments. Calls are generated via click to call or warm transfer, and appointments are set with verified consumers looking for an in home or virtual quote. Supply is 500 plus pre integrated and pre vetted direct publisher sources on the buyers page and 600 plus verified lead sources across 30 plus industries on the pricing page. Product types published elsewhere include inbound calls, web leads, click campaigns and rebound leads. Rebound leads are re contacted aged inventory and must be excluded from any insertion order.",
         [("buyers.px.com", "https://buyers.px.com/"), ("px.com/pricing", "https://px.com/pricing/")]),
  "f2": ("Pre integrated lead verification, deduplication checks and third party verification services, with a compliance stack listing identity checks, consent validation, fraud signals, regulatory controls, audit trails and TCPA and consent logs. On the education side specifically, consent and compliance monitoring, explicit consent in education marketing, and a note that the FCC explicit consent ruling implementation deadline is approaching. TrustedForm and Jornaya are not named on any PX page fetched. Billable call duration is not stated. No written return, credit or dispute policy appears on any PX page fetched, and that is the single biggest gap. It must be forced into the insertion order.",
         [("buyers.px.com", "https://buyers.px.com/"), ("px.com/pricing", "https://px.com/pricing/"), ("px.com/industries/education", "https://px.com/industries/education/")]),
  "f3": ("The best published vertical fit of any real marketplace. Health is published as Medicare, healthcare, ACA, medical alerts, primary care services and value added care services. Education is published as online degrees, trade schools, certification programs, vocational training and continuing education. Continuing education and certification programs is the closest published vertical language to an 18 week paid live course found anywhere in this research. The education practice publishes $7,000,000 plus in monthly ad spend managed, 150 plus school brands, 95,000 plus student enquiries a month and 30,000 plus enrollments a year. Longevity and wellness are not stated.",
         [("px.com/pricing", "https://px.com/pricing/"), ("px.com/lead-marketplace/education", "https://px.com/lead-marketplace/education/")]),
  "f4": ("No published price per lead or per call on any PX page, no minimum spend, no minimum test, no contract length, no prepay or net terms and no exclusive against shared statement. Only the pricing mechanism is published, AI powered dynamic pricing based on performance and other attributes. The one hard number found is a target of below $1,300 cost per enrollment on the education vertical, which is a warning rather than a comfort, because it sits almost exactly on LLA's $1,249 ticket. Planning band for a health or continuing education web lead through PX is $25 to $60, read across from PX's own published health and primary care and education categories. Canada is not stated.",
         [("px.com/pricing", "https://px.com/pricing/"), ("px.com/industries/education", "https://px.com/industries/education/")]),
  "f5": ("Onboard and test new lead vendors in days, not months. Support email support@px.com, phone (949) 313-7099, headquarters 44 Wall Street Suite 605, New York, New York 10005. Founders named on the about page: Frans van Hulle and Bas Offers, with chief executive and founder and chief operating officer and co founder titles displayed on the page but not bound to the names. Direct emails, direct phones and LinkedIn URLs are not published. buyers.px.com is a marketing page, not a signup.",
         [("px.com/about-px", "https://px.com/about-px/"), ("px.com/pricing", "https://px.com/pricing/")]),
  "contacts": [("support@px.com", "mailto:support@px.com"),
               ("About page, founders Frans van Hulle and Bas Offers, phone (949) 313-7099", "https://px.com/about-px/"),
               ("Buyer product page", "https://buyers.px.com/"),
               ("Education vertical page", "https://px.com/lead-marketplace/education/")],
  "verdict": "Buy PX, not ReviMedia. PX is ReviMedia's platform, and ReviMedia's own published verticals are insurance, home services and financial with no health and no education. Force a written return policy into the insertion order before any money moves.",
  "subject": "Continuing education vertical, exclusive real time web leads with TrustedForm on every record",
  "email": """PX buyer team,

Longevity Life Academy sells an 18 week live online longevity course at $1,249 upfront to a United States and Canada buyer aged 45 plus, 54.5 percent female. Your pricing page publishes continuing education and certification programs under education, and primary care and value added care under health. That language is closer to our product than anything else we found in the market, which is why you are on our 30 day test.

What we want to buy is exclusive real time web leads in a custom health education vertical, delivered to our own callers inside 60 seconds, with a TrustedForm certificate URL on every record in the field trustedform_cert_url and jornaya_leadid where available.

Four things we need in writing before an insertion order.

1. Cost per exclusive real time lead, minimum spend and minimum test size. None of the three are published on your site.
2. Your return, credit and dispute policy. We could not find one published. We are asking for a seven calendar day return window with account credit as the remedy and a 15 percent monthly return allowance.
3. Confirmation that rebound leads and aged inventory are excluded from delivery, and that exclusive means sold to us and to no other party ever.
4. Whether Canada delivery is available, and if so written confirmation of CASL express consent compliance.

Cell budget is $4,000 across 30 days. The success test is a 50 percent or better contact rate.

Omri Gitter
Gita Agency, for Longevity Life Academy""",
 },
 {
  "rank": "4", "score": "35.9", "name": "LeadsNow.ai",
  "kind": "AI booked qualified calls on a pay per result basis. The only vendor publishing a price for the exact commercial shape of this offer, and the only one with no named accountable human.",
  "f1": ("An AI booked qualified call on a pay per result basis. You pay per AI booked qualified call, not for clicks, not for opt ins, not for lead form submissions and not for reach or impressions. The mechanism is an outbound AI dial into an opt in list or a database reactivation, converting to a calendar booking, plus cold AI outbound calls. That is a weaker mechanism than a consumer dialled inbound call and it is scored accordingly.",
         [("leadsnow.ai/coaches", "https://leadsnow.ai/coaches/")]),
  "f2": ("AI agents qualify every prospect for fit, budget and intent, then book them into the calendar, with every appointment qualified against an ICP filter before it lands and call recording review loops behind it. The written commercial policy is the strongest buyer protection found in this space: if the appointment does not land qualified, you do not pay for it, written into the engagement. If they no show, the make up logic runs. If the calendar stays empty, you owe zero. No clawback on appointments already delivered, and cancel any time with seven days notice. IVR, billable duration, TrustedForm, Jornaya, litigator scrub and one to one consent are all not stated, and that is the risk. An AI outbound dialler into United States consumers aged 55 to 65 with no published litigator scrub is a TCPA exposure that counsel must clear before any test.",
         [("leadsnow.ai/coaches", "https://leadsnow.ai/coaches/")]),
  "f3": ("Published segments include health, transformation and nutrition coaches selling high ticket one to one, high ticket personal trainers, online course creators, education companies, and group coaching, masterminds and cohort programs. Price point language is an exact match, high ticket coaches at $3,000 to $25,000 plus engagements and offers priced between $3,000 and $15,000. A $1,000 plus consumer purchase is explicitly in scope. The honest verdict is that the named client logos are overwhelmingly fitness studios and gyms, Iron Body, Living Well, BFitt, Stoneway CrossFit, F45 Narrabeen, Health First Development and JB Transformations, which is fitness small business to business rather than affluent 55 to 65 consumers. Longevity is not stated.",
         [("leadsnow.ai/coaches", "https://leadsnow.ai/coaches/")]),
  "f4": ("The only directly applicable published price found. Typical cost per booked discovery call $40 to $220, cost per raw lead $10 to $80, health, transformation and nutrition coaches $40 to $140, group coaching and cohort programs $50 to $160, coaching offers priced $3,000 to $15,000 at $80 to $450, actual client range $80 to $800 plus per booked call, and a sizing rule of roughly 1 to 5 percent of closed deal value. Terms: no retainers, no minimum spend lock in, a small scope based setup fee, no six or twelve month lock in, observed client spend $3,000 to $10,000 plus a month, early testing $2,000 to $3,000 a month. Applied to LLA at a $1,249 ticket, the 1 to 5 percent rule gives $12 to $62 per booked call, and at the sister brand's 18 percent close a booked call is worth about $225, so anything under about $140 is viable.",
         [("leadsnow.ai/coaches", "https://leadsnow.ai/coaches/")]),
  "f5": ("First booked calls typically land in week one or two from database reactivation, cold AI outbound layers in from week two to four, and most clients start booking qualified strategy calls within 7 to 14 days of launch, with full optimisation at 30 to 60 days. Geography published as Australia, United States, United Kingdom, Canada, New Zealand and Europe, so Canada is explicitly covered, one of only three vendors in the report where that is true. Named executive: none. No email, no direct phone and no self serve signup, only a book a free strategy session button. The absence of a named accountable human is why this is rank five and not rank one.",
         [("leadsnow.ai/coaches", "https://leadsnow.ai/coaches/")]),
  "contacts": [("Coaches page, book a strategy session, the only published route", "https://leadsnow.ai/coaches/")],
  "verdict": "Test it capped at $150 per booked appointment and only after counsel clears the outbound dialling. Demand a named accountable person on the first call, and if there is not one, do not sign.",
  "subject": "Booked appointments for a $1,249 longevity course, capped at $150, 45 plus buyer",
  "email": """LeadsNow team,

Longevity Life Academy sells an 18 week live online longevity course at $1,249 upfront, cohorts of 8 to 15, to a United States and Canada buyer aged 45 plus and 54.5 percent female. Your coaches page publishes a health, transformation and nutrition band of $40 to $140 per booked call and a rule sizing the price at 1 to 5 percent of closed deal value. On our ticket that rule gives $12 to $62, and our own break even at a 20 percent close rate is $250 per appointment, so there is room here if the appointments are real.

What we want to test is pay per AI booked qualified call, capped at $150, against a defined ICP filter of age 45 plus, United States or Canada, and stated interest in longevity, metabolic health or continuous glucose monitoring.

Four questions we need answered before any money moves.

1. Who is the named accountable person on this account, with title and a direct email. Your site publishes client names but no team.
2. Where does the calling list come from, and are all records scrubbed against a TCPA litigator list and the national do not call registry before the dialler runs.
3. Will call recordings for every booked appointment be delivered to us and retained for 90 days.
4. Your written policy says an unqualified appointment is not billable. Can we put the qualification criteria in the engagement in words, agreed before launch.

Cell budget is $3,000 across 30 days. Success is at least 20 appointments at 25 percent or better show to sale.

Omri Gitter
Gita Agency, for Longevity Life Academy""",
 },
 {
  "rank": "5", "score": "32.0", "name": "Alliant, AnalyticsIQ",
  "kind": "Data only audience segments. Not a lead vendor. It stays in the five because it fixes the targeting half of the Meta problem, which nothing else in the list does.",
  "f1": ("It is not a lead. It is a data only audience segment with no consumer action. The product sold is audience segments, activate audiences built for health and wellness, target resolution driven consumers ready to invest in health and wellness products and services. Under the factor one taxonomy this is the data only category, and zero intent verification is possible because there is no consumer action to verify.",
         [("Alliant health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")]),
  "f2": ("Nothing. IVR, screening, duration, human quality assurance, call recording, TrustedForm, Jornaya, ActiveProspect, phone append, litigator scrub and one to one consent are all not stated on the health and wellness audience page. Return, credit and dispute policy is not stated.",
         [("Alliant health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")]),
  "f3": ("The best audience match in the entire report. Published sub segments are health and wellness, exercise and fitness, mental wellness and self care, diet and nutrition, weight management, health and medical utilization, and accessories and equipment. Custom creator affinity segments are built to order, for example followers of a named creator on Instagram or YouTube. That capability is the direct fix for the Meta targeting failure: build a longevity creator affinity segment, onboard it to Meta as a custom audience, and stop letting the lead form optimiser pick the cheapest tapper. Longevity is not a named segment, and education, coaching and $1,000 plus consumer purchase are not stated.",
         [("Alliant health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")]),
  "f4": ("No price, no minimum and no contract length published. Data segment cost per thousand impressions is negotiated. This one is genuinely unknown and is not guessed at anywhere in this report.",
         [("Alliant health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")]),
  "f5": ("The single best qualified named contact in the whole report for a health brief: Christine Lee, also published as Christine Boley, head of health strategy and partnerships, christineb@analyticsiq.com, with a public LinkedIn profile. Executive bench published: Scarlett Shipp chief executive, Louise Ward chief operating officer, Dave Taylor chief product officer, Walter Chistoni senior vice president of sales, Margo Hock vice president of digital partnerships. General emails sales@alliantdata.com, info@alliantdata.com and datahelp@alliantdata.com. No self serve signup.",
         [("Alliant health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")]),
  "contacts": [("Christine Lee, head of health strategy and partnerships, christineb@analyticsiq.com", "mailto:christineb@analyticsiq.com"),
               ("Christine Boley on LinkedIn", "https://www.linkedin.com/in/christineboley"),
               ("sales@alliantdata.com", "mailto:sales@alliantdata.com"),
               ("Health and wellness audience guide", "https://alliantinsight.com/audience-guide/health-wellness/")],
  "verdict": "Do not buy leads here, because there are none. Buy the segment, onboard it to Meta as a custom audience, and run it underneath the pay per call cells so the two halves of the problem get fixed at once.",
  "subject": "Creator affinity and health and wellness segments for a 45 plus longevity buyer, Meta onboarding",
  "email": """Christine,

Longevity Life Academy sells an 18 week live online longevity course at $1,249 to a United States and Canada buyer aged 45 plus and 54.5 percent female. We are spending $20,000 a month on Meta and the lead form optimiser is finding the cheapest tapper rather than the buyer. We are not writing to you for leads. We are writing for targeting.

Two things we want to price.

1. Your published health and wellness segments, specifically diet and nutrition, weight management, mental wellness and self care, and health and medical utilization, filtered to age 45 plus in the United States and Canada.
2. A custom creator affinity segment built to order against the longevity and metabolic health creators our buyer already follows. We have a named list of 53 creators with verified reach and can hand it over on the call.

What we need from you: segment counts at that filter, the cost per thousand impressions or flat licence fee, the onboarding path into Meta as a custom audience, the match rate you typically see, and the lead time from order to live audience.

We are running four paid media cells over the next 30 days and we want your segment underneath all of them, so the targeting question and the lead source question get answered in the same month.

Are you available for a call this week.

Omri Gitter
Gita Agency, for Longevity Life Academy""",
 },
]

# --------------------------------------------------------------- section D
PRICE_HEADERS = ["Product", "Published price", "Published contact rate", "Published close rate", "Source"]
PRICE_ROWS = [
 ("Aged internet health leads, 15 to 85 plus days", "$0.15 to $5.00", "15 to 35 percent", "3 to 7 percent", "agedleadstore.com", "https://agedleadstore.com/health-insurance-leads-cost/"),
 ("Fresh shared health leads, 0 to 7 days", "$15 to $40", "40 to 55 percent", "6 to 10 percent", "agedleadstore.com", "https://agedleadstore.com/health-insurance-leads-cost/"),
 ("Fresh exclusive health leads, 0 to 7 days", "$40 to $100 plus", "50 to 65 percent", "8 to 15 percent", "agedleadstore.com", "https://agedleadstore.com/health-insurance-leads-cost/"),
 ("Live transfers", "$30 to $75 plus", "80 to 95 percent", "15 to 25 percent", "agedleadstore.com", "https://agedleadstore.com/health-insurance-leads-cost/"),
 ("Health insurance inbound calls", "$30 to $120", "n.a.", "n.a.", "theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
 ("Medicare inbound calls", "$40 to $120", "n.a.", "n.a.", "theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
 ("ACA inbound calls", "$30 to $90 per call", "n.a.", "n.a.", "theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
 ("Real time form leads, health", "$10 to $60", "n.a.", "n.a.", "theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
 ("Real time co registration leads, disqualified", "$0.50 to $2.00", "n.a.", "n.a.", "theleadswarehouse.com", "https://theleadswarehouse.com/how-much-do-medicare-and-aca-leads-cost-in-2026/"),
 ("Healthcare, non insurance, pay per call", "$25 to $80 at 60 to 120 seconds", "n.a.", "n.a.", "hypertargetmarketing.com", "https://hypertargetmarketing.com/pay-per-call-benchmarks/"),
 ("Legal personal injury pay per call", "$100 to $400 plus at 90 to 120 seconds", "n.a.", "n.a.", "hypertargetmarketing.com", "https://hypertargetmarketing.com/pay-per-call-benchmarks/"),
 ("Medicare and health insurance pay per call", "$30 to $60 baseline, $50 to $150 in enrollment season", "n.a.", "n.a.", "hypertargetmarketing.com", "https://hypertargetmarketing.com/pay-per-call-benchmarks/"),
 ("General pay per call range", "$10 to $30 simple home services, $50 to $150 plus legal and insurance", "n.a.", "n.a.", "hypertargetmarketing.com", "https://hypertargetmarketing.com/what-is-pay-per-call/"),
 ("High ticket coaching booked call", "$100 to $250", "n.a.", "n.a.", "highticketleadgen.com", "https://highticketleadgen.com/"),
 ("Health and transformation coaching booked call", "$40 to $140", "n.a.", "n.a.", "leadsnow.ai", "https://leadsnow.ai/coaches/"),
 ("Coaching offers priced $3,000 to $15,000, booked call", "$80 to $450", "n.a.", "n.a.", "leadsnow.ai", "https://leadsnow.ai/coaches/"),
 ("Exclusive live transfer insurance", "$45 to $75 live transfer, exclusive web $40", "n.a.", "n.a.", "getinsureleads.com", "https://www.getinsureleads.com/blog/best-insurance-lead-providers-compared"),
 ("EverQuote", "$20 to $40 per lead", "n.a.", "n.a.", "insuricom", "https://insuricom.com/insurance-agent-resources/top-insurance-lead-vendors-for-health-agents-in-2025/"),
 ("Datalot, Centerfield", "$40 to $80 per call", "n.a.", "n.a.", "insuricom", "https://insuricom.com/insurance-agent-resources/top-insurance-lead-vendors-for-health-agents-in-2025/"),
 ("SmartFinancial", "$8 to $35 per lead", "n.a.", "n.a.", "insuricom", "https://insuricom.com/insurance-agent-resources/top-insurance-lead-vendors-for-health-agents-in-2025/"),
 ("Hometown Quotes", "$8 to $25 per lead", "n.a.", "n.a.", "insuricom", "https://insuricom.com/insurance-agent-resources/top-insurance-lead-vendors-for-health-agents-in-2025/"),
 ("TrustedForm certify, verify and retain", "Free, then from $0.15, buyer side $0.15 to $0.50 per certificate", "n.a.", "n.a.", "activeprospect.com", "https://activeprospect.com/pricing-small-business/"),
 ("TCPA violation exposure", "$500 to $1,500 each", "n.a.", "n.a.", "activeprospect.com", "https://activeprospect.com/trustedform/"),
]

DURATION = [
 ("Astoria", "A typical range is 30 to 90 seconds. 60 seconds is a safe starting point. For high ticket verticals like legal or medical, consider 90 seconds. A 120 second minimum may filter out many legitimate leads. Run the test for at least two weeks.", "https://www.astoriacompany.com/setting-the-right-minimum-call-duration-for-pay-per-call"),
 ("HyperTarget", "Standard billable thresholds are 60, 90 or 120 seconds of connected non IVR conversation. Typical billable calls run 90 to 180 seconds. IVR screened pays more, agent qualified warm transfers pay the most. The duration threshold is a billing trigger, not a quality guarantee.", "https://hypertargetmarketing.com/pay-per-call-benchmarks/"),
 ("Elevarus, complete guide", "HVAC 60 to 90 seconds, ACA and Medicare 60 to 90 seconds, auto insurance 90 to 120 seconds, home services install 90 to 120 seconds, legal and mass tort 120 plus seconds. Duplicate rule to demand: same day duplicates do not bill, 7 day duplicates bill at half rate, 30 day duplicates bill at full rate.", "https://elevarus.com/pay-per-call-marketing-complete-guide/"),
 ("Elevarus, buyer guide", "Publisher duration floor equals buyer billable threshold minus average call qualification traversal time minus a 10 second buffer. Disposition taxonomy: billable connected, qualified not billable, wrong vertical, hang up pre threshold, transfer declined, did not qualify.", "https://elevarus.com/pay-per-call-marketing-agency-buyer-guide/"),
 ("ranklocall", "Commonly 30, 60 or 90 seconds. A fair provider credits fake, duplicate and out of scope form leads. The credit policy is where you find out whether a pay per call provider is fair or extractive.", "https://ranklocall.com/what-is-a-billable-call/"),
 ("pxmediainc", "With duration based billing, the call is billable when it lasts beyond 90 seconds.", "https://www.pxmediainc.com/pay-per-call-pricing-explained/"),
]
DURATION_SPEC = "Recommended specification for LLA: a 90 second billable threshold, IVR confirmed age band 45 plus, IVR confirmed United States or Canada geography, recording delivered with every billable call, and same day duplicates non billable."

RETURNS = [
 ("Best in market", "Agents receive a blanket 20 percent return policy each month, no questions asked.", "EverQuote", "https://learn.everquote.com/buy-insurance-leads"),
 ("Reasonable, industry definition", "A reasonable return policy, 10 to 15 percent return rate, 24 to 72 hour return window, clear return reasons, is a sign the vendor stands behind the data.", "salespulse.app", "https://www.salespulse.app/blog/best-insurance-lead-providers-2026"),
 ("Red flag, industry definition", "A no return policy or a 5 percent cap usually means the vendor knows about quality issues and is hedging.", "salespulse.app", "https://www.salespulse.app/blog/best-insurance-lead-providers-2026"),
 ("Credit against replacement", "Replacement leads tend to be the lower quality leftovers. Account credit gives you flexibility.", "salespulse.app", "https://www.salespulse.app/blog/best-insurance-lead-providers-2026"),
 ("Hard written window", "Leads must be returned within seven calendar days. Returns to returns@astorialeads.com. Remedy is credit.", "AstoriaLeads terms", "https://astorialeads.com/terms-of-service.php"),
 ("Default dispute deadline", "Buyer must submit documented disputes or return requests by the tenth day of the month following delivery, and all undisputed leads and calls are deemed accepted.", "Astoria seller terms", "https://www.astoriacompany.com/seller-terms"),
 ("Replacement guarantee", "If a lead has fake contact information, or if it is bad for any other reason, then the lead will be replaced.", "Contactability", "https://contactability.com/pages/pricing"),
 ("Pay only if qualified", "If the appointment does not land qualified, you do not pay for it, full stop, written into the engagement.", "LeadsNow.ai", "https://leadsnow.ai/coaches/"),
 ("No show guarantee", "If a lead does not respond or an appointment does not show, buyers do not pay.", "The Lead Marketplace", "https://theleadmarketplace.com/"),
]
EXCLUSIVE_TRAP = ("Some vendors define exclusive as sold to only one agent ever. Others define it as sold to one agent per carrier. Others define it as exclusive for 30 minutes, then resold. Put the definition in the insertion order in words.",
                  "salespulse.app", "https://www.salespulse.app/blog/best-insurance-lead-providers-2026")

# --------------------------------------------------------------- section G
ECON_HEADERS = ["Scenario", "Cost per unit", "Close rate", "Cost per acquisition", "Gross margin per sale"]
ECON_ROWS = [
 ("Current Meta lead form", "$20", "near zero contact, assume 1 percent", "$2,000", "negative", False),
 ("Healthcare pay per call, low band", "$25", "15 percent", "$167", "$1,082", False),
 ("Healthcare pay per call, high band", "$80", "15 percent", "$533", "$716", False),
 ("Healthcare pay per call, high band, weak close", "$80", "8 percent", "$1,000", "$249", False),
 ("Live transfer, mid band", "$50", "20 percent", "$250", "$999", True),
 ("Live transfer, high band, weak close", "$75", "10 percent", "$750", "$499", False),
 ("Booked appointment, coaching band low", "$100", "20 percent", "$500", "$749", False),
 ("Booked appointment, coaching band high", "$250", "20 percent", "$1,250", "minus $1", True),
 ("Booked appointment, coaching band high", "$250", "30 percent", "$833", "$416", False),
]
ECON_MATH = [
 "At a 20 percent close rate, one sale needs five appointments. $1,249 divided by 5 equals $249.80 per appointment.",
 "So $250 per appointment is the exact break even. That is the ceiling, and the target is $100 to $150.",
 "$100 per appointment at 20 percent gives a $500 cost per acquisition and $749 of gross margin on the $1,249 ticket.",
 "Pay per call at $25 to $80 is the widest margin option in the table and the one to test first.",
]

TEST_HEADERS = ["Cell", "Vendor", "Product", "Budget", "Success metric"]
TEST_ROWS = [
 ("1", "Astoria", "Pay per call, custom health education campaign, 90 second billable, IVR age 45 plus", "$5,000", "At least 60 billable calls, at least 15 percent call to sale"),
 ("2", "PX, px.com", "Custom vertical, exclusive real time web leads with a TrustedForm certificate on every record, fed to LLA callers within 60 seconds", "$4,000", "At least 50 percent contact rate"),
 ("3", "Aragon", "Pay per call second source, same 90 second specification, to price check Astoria", "$3,000", "Cost per billable call below Astoria"),
 ("4", "LeadsNow.ai or HighTicketLeadGen", "Booked appointments, capped at $150", "$3,000", "At least 20 appointments, at least 25 percent show to sale"),
]
TEST_NOTE = "Total $15,000, four cells, one month, all four measured on the same denominator, cost per enrolled student, not cost per lead."

IO_CLAUSES = [
 "Billable call duration is 90 seconds of connected, non IVR conversation.",
 "Every call must be IVR screened to confirm the caller is age 45 or older and located in the United States, and the screening questions must be supplied to Buyer in writing before launch.",
 "Call recording must be delivered with every billable call, retained 90 days, and accessible to Buyer.",
 "Every web lead must be delivered with a TrustedForm certificate URL in the field trustedform_cert_url and, where available, jornaya_leadid.",
 "All records must be scrubbed against a TCPA litigator list and the national do not call registry prior to delivery.",
 "Exclusive means sold to Buyer and to no other party, ever. Not exclusive per carrier, not exclusive for 30 minutes.",
 "No co registration, no incentivized, no sweepstakes, and no aged inventory. Seller warrants that 100 percent of delivered records originated from a consumer action directly related to Buyer's offer.",
 "Return window: 7 calendar days, remedy is account credit, target return allowance 15 percent monthly.",
 "Same day duplicates do not bill. 7 day duplicates bill at half rate.",
 "No minimum spend commitment and no term contract for the first 30 days.",
 "Wrong numbers and calls ending before the billable threshold are not billable.",
 "Canada delivery, if any, requires separate written confirmation of CASL express consent compliance.",
]
IO_SOURCES = [
 ("Field names for the certificate clause", "https://support.leadprosper.io/article/498-trustedform-and-jornaya-leadid-compared-pros-cons-and-best-practices-for-lead-gen"),
 ("The exclusivity trap, documented", "https://www.salespulse.app/blog/best-insurance-lead-providers-2026"),
 ("Seven day window and credit remedy", "https://astorialeads.com/terms-of-service.php"),
 ("Twenty percent no questions asked, the stretch target", "https://learn.everquote.com/buy-insurance-leads"),
 ("Duplicate rule", "https://elevarus.com/pay-per-call-marketing-complete-guide/"),
 ("No minimum and no term, published by two vendors", "https://contactability.com/pages/pricing"),
 ("Wrong numbers non billable", "https://hypertargetmarketing.com/what-is-pay-per-call/"),
]

PREQUAL = ("Show me one campaign you have run in the last twelve months where the end product was a consumer purchase of "
           "$1,000 or more that was not insurance, not legal, and not a mortgage, and tell me the cost per billable call "
           "and the close rate.")
PREQUAL_NOTE = "Ask it first and stop the call if the answer is vague. Nothing in this research pass found a vendor who publishes an answer to that question. The one who answers it credibly on a call is the one to sign."

# --------------------------------------------------------------- section E
FORUM_STATS = [
 ("442", "distinct forum, review and operator URLs harvested", "Reddit, LinkedIn, Trustpilot, G2, Capterra, TrustRadius, Sitejabber, AffiliateFix, AffPaying, BlackHatWorld, WarriorForum, afflift, IndieHackers, YouTube and mThink"),
 ("332", "queued for text retrieval", "183 returned usable text"),
 ("134", "yielded a quotable on topic operator opinion", "The rest returned paywalls, deleted threads or off topic text and were excluded rather than padded"),
 ("90", "of the 134 are Reddit threads", "Then linkedin.com 9, blackhatworld 4, trustpilot 9 across four domains, g2 4, affiliatefix 3, affpaying 3"),
]
FORUM_THEMES = [("Price per lead and per call", "44"), ("Contact and answer rates", "29"),
                ("Named vendor experience", "20"), ("Speed to lead", "20"),
                ("Resale, recycling and aged inventory", "6"), ("Exclusive against shared economics", "6"),
                ("High ticket course and coaching lead buying", "4"), ("Other operator evidence", "4"),
                ("Older demographics and the phone", "1")]
FORUM_QUOTES = [
 ("Contact rate is the failure mode, not price",
  "Out of 12 promising leads, only one person picked up the phone. I have noticed a similar trend among individuals aged 65 and older, where the leads are genuine but difficult to contact. Many seniors tend to ignore calls from unfamiliar numbers, but when they select a time frame for being reached, the likelihood of them answering increases significantly.",
  "r/FacebookAds, high intent leads from Meta but nobody answers", "https://www.reddit.com/r/FacebookAds/comments/1mjffzh/highintent_leads_from_meta_but_nobody_answers/"),
 ("Instant forms go silent at 70 to 80 percent",
  "When utilizing instant forms, it is not uncommon for 70 to 80 percent of leads to go silent unless you implement thorough follow ups or enhance your pre qualification process.",
  "r/FacebookAds, no response from leads on lead forms", "https://www.reddit.com/r/FacebookAds/comments/1l0cnwm/no_response_from_leads_on_lead_forms/"),
 ("Ninety percent no answer is a documented normal",
  "About 90 percent of the time, when the team calls the provided numbers, they either get no response or end up reaching voicemail.",
  "r/FacebookAds, collected lead forms are mostly no answer", "https://www.reddit.com/r/FacebookAds/comments/17jvoco/collected_lead_forms_from_fb_ads_are_mostly_no/"),
 ("Call ads carry their own fraud problem",
  "About 50 to 75 percent of the calls generated by these ads either have no real person on the other end or sound like a call center with the caller never speaking. We observe up to 60 percent false calls on most days. About 80 percent of our calls drop automatically within one or two seconds.",
  "r/FacebookAds, call ads producing trash calls", "https://www.reddit.com/r/FacebookAds/comments/1d1wehx/call_ads_producing_5075_trash_calls/"),
 ("A booked qualified meeting at $125 is defensible, a raw lead at $125 is not",
  "If they are giving you booked meetings with qualified buyers, $125 per lead is not bad. $125 per sales qualified lead is high for some industries and low for others, how much do you expect a closed lead to pay you for your product or service.",
  "r/Entrepreneur, did I make a mistake paying 1k for 8 leads", "https://www.reddit.com/r/Entrepreneur/comments/1g9g8pb/did_i_make_a_mistake_paying_1k_for_8_leads/"),
 ("Cheap internet leads convert at about one in a hundred",
  "In my agency, we convert about 1.5 percent of internet leads, with costs averaging between $4 and $7 per lead across these vendors. Many large corporations struggle to keep up with demand, often resorting to recycling old leads. Consequently, it often takes about 100 leads to secure a single deal.",
  "r/InsuranceAgent, internet lead company reviews", "https://www.reddit.com/r/InsuranceAgent/comments/1l101rg/internet_lead_company_reviews_my_experience/"),
 ("Speed to lead is the second lever after mechanism",
  "We have discovered that contacting leads within 15 minutes of their submission significantly increases the likelihood of conversion compared to waiting longer than that.",
  "r/salesforce, leads show high interest but do not answer calls", "https://www.reddit.com/r/salesforce/comments/1jeh2sr/leads_show_high_interest_but_dont_answer_calls/"),
 ("The high ticket funnel is a filter, not a volume game",
  "The result was that 17,000 registrants became 50 qualified prospects who actually had the money and motivation to buy the high ticket offer. 37 percent close rate across all teams.",
  "LinkedIn, evaluating lead quality before making contact", "https://www.linkedin.com/top-content/sales/identifying-high-value-leads/evaluating-lead-quality-before-making-contact/"),
 ("Live leads convert at 40 percent when the operator is competitive",
  "They can be quite effective, but having experience and being competitive with pricing is crucial. Currently, we are converting at around 40 percent or more, but we face challenges with some very low cost options.",
  "r/InsuranceAgent, live leads", "https://www.reddit.com/r/InsuranceAgent/comments/1ppbnst/live_leads/"),
 ("Buying courses about lead generation is not buying leads",
  "I have purchased five different courses, and unfortunately, none of them were beneficial. I even invested $2,000 in one, and they all turned out to be quite disappointing.",
  "r/LeadGeneration, most effective paid lead gen course", "https://www.reddit.com/r/LeadGeneration/comments/1ieeyl1/whats_been_your_most_effective_paid_leadgen_course/"),
]

WHY_FAILED = ("Meta lead forms at about $20 cost per lead with near zero contact rate is the documented outcome of a one tap instant form. "
              "EverQuote engineers the opposite on purpose, a form that takes 7 to 10 minutes to complete, engineered to be long enough to weed out those who are less motivated. "
              "The published contact rate ladder runs aged 15 to 35 percent, fresh shared 40 to 55 percent, fresh exclusive 50 to 65 percent, live transfers 80 to 95 percent. "
              "The close rate ladder runs the same direction, 3 to 7 percent aged, 8 to 15 percent fresh exclusive, 15 to 25 percent live transfer. "
              "The sister brand converts 18 percent lead to sale on a $1,400 course, which sits inside the live transfer close band and nowhere near the form lead band. "
              "The fix is not a cheaper cost per lead. It is buying a different unit.")
WHY_SRC = [("EverQuote buyer guide", "https://learn.everquote.com/buy-insurance-leads"), ("agedleadstore.com", "https://agedleadstore.com/health-insurance-leads-cost/")]

COVERAGE_HEADERS = ["Vendor", "What it actually is", "Verdict on the five factors"]
COVERAGE_ROWS = [
 ("Semcasting", "Data only", "Rule out as a lead source, keep as a targeting layer."),
 ("ClickDealer", "CPA network, closest thing to a health vertical", "No buyer side facts published, so it cannot be scored."),
 ("Perform[cb]", "Outcome network", "No published mechanism."),
 ("Archer Education", "The only pure education supply source", "Institutional, sells to universities, not to course brands."),
 ("A4D", "Affiliate network", "Zero buyer side disclosure."),
 ("Digital Market Media", "Excellent mechanism", "One hundred percent wrong verticals."),
 ("Excel Impact", "Best documented intent mechanics in the report", "Insurance only."),
 ("Contactability", "Best verification stack and best commercial terms", "Insurance only."),
 ("MediaAlpha", "Transparent quality doctrine", "Insurance only."),
 ("EverQuote", "The best published return policy in the industry, 20 percent no questions asked", "Insurance only, but the policy is the benchmark to quote at every other vendor."),
 ("Leadnomics", "Thin", "Nothing buyer side published."),
 ("Adsource Media", "Two different companies", "Neither is supply."),
 ("iMonMedia", "Digital Media Solutions successor", "Thin and unverifiable."),
 ("WebMD Ignite", "Business to business healthcare marketing", "Not a consumer lead vendor."),
 ("Healthline Media", "Perfect audience", "Categorically will not sell leads. States a $25,000 minimum and does not allow CPA or CPC pricing."),
 ("Everyday Health Group", "Media", "Not leads."),
 ("Sharecare", "Pharma and life sciences buyer", "No consumer lead product."),
 ("Rise Interactive", "Agency", "Rule out."),
 ("Palo Media", "Agency", "Rule out."),
 ("InboundProspect, payperlead.com", "Pay per lead operator", "Partially unverifiable."),
 ("Phonexa marketplace supply partners", "Software", "Not supply."),
 ("Retreaver partner supply", "Software", "Not supply, but two useful named integrations."),
 ("boberdoo powered sellers", "Software", "Not supply, but the best published economics of exclusivity."),
 ("LeadsCon Las Vegas 2026 exhibitor list", "Directory, mined in full", "Eight named suppliers worth contacting."),
 ("ReviMedia", "Could not be read, robots disallowed on every property", "Treat as unknown. Buy PX instead, which is ReviMedia's platform."),
 ("HighTicketLeadGen.com", "Priced for high ticket, agency model", "Published booked call band $100 to $250. No verification stack."),
 ("HotPremiumLeads.com", "The only vendor publishing the word longevity", "It is the wrong longevity, life insurance longevity."),
 ("LiveTransfers.com", "Pure live transfer", "Insurance and finance book."),
 ("TheLeadMarketplace.com", "A la carte high intent leads", "Publishes a no show guarantee, worth a call."),
 ("NextGen Leads", "The cleanest self serve in the market", "Insurance only."),
]
