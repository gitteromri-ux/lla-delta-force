# -*- coding: utf-8 -*-
# Two parallel lines addition. Line A lead gen to call centre, Line B direct e-commerce.
# No em dashes, no en dashes, no exclamation marks.

TWO_LINES_HEAD = "Two lines run in parallel. Line A is what you are spending on today. Line B does not exist yet."

TWO_LINES_CHIPS = [
 ("$20,000", "monthly Meta spend running today", "Client stated current spend, replaces the earlier pilot framing"),
 ("18%", "lead to sale close on the sister brand", "French Atelier, $1,400 course, $50,000 per month lead gen"),
 ("$111", "cost per acquisition that close rate implies at a $20 lead", "$20 divided by 0.18"),
 ("11.3x", "return on ad spend on a $1,249 order at that cost", "$1,249 divided by $111"),
]

ATELIER = {
 "head": "The sister brand proves the lead gen line works when the call centre answers.",
 "rows": [
  ("Brand", "French Atelier, sister brand inside the same group"),
  ("Monthly lead gen spend", "$50,000"),
  ("Course price", "$1,400"),
  ("Lead to sale close rate", "18 percent"),
  ("Cost per lead", "$20"),
  ("Implied leads per month", "2,500"),
  ("Implied sales per month", "450"),
  ("Implied cost per acquisition", "$111"),
  ("Implied monthly revenue", "$630,000"),
 ],
 "close": "The offer is comparable, the price is comparable and the spend is larger, so the difference between French Atelier and LLA is not the media buy, it is what happens after the form is submitted.",
}

LINE_A = {
 "tag": "LINE A",
 "title": "Lead gen to call centre",
 "state": "Running today. This is where the $20,000 goes.",
 "spec": [
  ("Objective", "Leads"),
  ("Form", "Instant form or website form, website form preferred once the Conversions API is live"),
  ("Optimisation event", "Qualified Lead"),
  ("Structure", "One campaign, one broad ad set, no age or interest fragmentation"),
  ("KPI chain", "Cost per lead, then contact rate, then close rate, then cost per acquisition"),
  ("Break point", "Contact rate. Not cost per lead."),
 ],
 "math": [
  ("Cost per acquisition", "cost per lead divided by close rate"),
  ("Close rate", "contact rate multiplied by close rate on contacted leads"),
  ("Return on ad spend", "$1,249 divided by cost per acquisition"),
 ],
 "verdict": "At a $20 lead and an 18 percent close the cost per acquisition is $111 and the return on ad spend is 11.3x, which is the single most profitable structure available to LLA today. It collapses entirely on contact rate.",
}

LINE_B = {
 "tag": "LINE B",
 "title": "Direct e-commerce",
 "state": "Does not exist yet. Blocked by the checkout, see the red alert.",
 "spec": [
  ("Objective", "Sales, optimising Purchase"),
  ("Structure", "One campaign, one broad ad set"),
  ("Placements", "Advantage+ placements"),
  ("Attribution", "Seven day click, one day view"),
  ("Bridging event", "Initiate Checkout only while purchase volume sits under roughly 8 per week, then switch to Purchase"),
  ("Value", "Purchase fires with value 1249 upfront or 289 on the instalment plan, never a flat 1"),
 ],
 "math": [
  ("Impressions", "spend divided by cost per thousand, multiplied by 1,000"),
  ("Clicks", "impressions multiplied by click through rate"),
  ("Cost per click", "spend divided by clicks"),
  ("Landing page views", "clicks multiplied by landing page view rate"),
  ("Purchases", "landing page views multiplied by checkout conversion rate"),
  ("Cost per acquisition", "spend divided by purchases"),
  ("Revenue", "purchases multiplied by $1,249"),
  ("Return on ad spend", "revenue divided by spend"),
 ],
 "verdict": "Break even at $20,000 of spend on a $1,249 order value is 16 purchases, which is a 0.21 percent conversion rate on landing page views. Every case above that number is profitable.",
}

# Line A sensitivity. close rate rows, CPL columns.
SENS_CPLS = ["$20", "$40", "$60"]
SENS_ROWS = [
 ("2%",  [("$1,000", "1.25x", "warn"), ("$2,000", "0.62x", "bad"),  ("$3,000", "0.42x", "bad")]),
 ("5%",  [("$400", "3.12x", "ok"),     ("$800", "1.56x", "warn"),   ("$1,200", "1.04x", "warn")]),
 ("10%", [("$200", "6.25x", "ok"),     ("$400", "3.12x", "ok"),     ("$600", "2.08x", "ok")]),
 ("18%", [("$111", "11.3x", "ok"),     ("$222", "5.62x", "ok"),     ("$333", "3.75x", "ok")]),
]
SENS_NOTE = "Cost per acquisition is cost per lead divided by close rate, and return on ad spend is $1,249 divided by cost per acquisition. Green is above 2.00x and carries overheads, blue is between 1.00x and 2.00x and pays for media only, red is below 1.00x and loses money on every sale."

# Line B funnel, common inputs
LINEB_INPUTS = [
 ("Cost per thousand impressions", "$25.00", "United States 45 plus, Health and Wellness band", "https://www.triplewhale.com/blog/facebook-ads-benchmarks"),
 ("Click through rate", "1.20%", "Conservative end of the premium band for a considered purchase", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
 ("Cost per click", "$2.08", "Derived, spend divided by clicks", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
 ("Landing page view rate", "80%", "Upper band, fast page and a warm click", "https://docs.upstackdata.com/reference/metrics/advertising/meta/meta-clicks/meta-landing-page-view-rate"),
 ("Checkout conversion rate", "0.3% / 0.5% / 1.0%", "Cold traffic to a $1,249 checkout, three cases", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
 ("Order value", "$1,249", "Upfront plan on the pricing page", "https://longevitylifeacademy.com/pricing.html"),
]

# spend, case, cvr, impressions, clicks, cpc, lpv, purchases, cpa, revenue, roas, highlight
LINEB_20K = [
 ("$20,000", "Conservative", "0.3%", "800,000", "9,600", "$2.08", "7,680", "23", "$868", "$28,750", "1.44x", False),
 ("$20,000", "Base",         "0.5%", "800,000", "9,600", "$2.08", "7,680", "38", "$526", "$47,462", "2.37x", True),
 ("$20,000", "Optimistic",   "1.0%", "800,000", "9,600", "$2.08", "7,680", "77", "$260", "$96,166", "4.81x", False),
]
LINEB_50K = [
 ("$50,000", "Conservative", "0.3%", "2,000,000", "24,000", "$2.08", "19,200", "58",  "$862", "$72,442",  "1.45x", False),
 ("$50,000", "Base",         "0.5%", "2,000,000", "24,000", "$2.08", "19,200", "96",  "$521", "$119,904", "2.40x", True),
 ("$50,000", "Optimistic",   "1.0%", "2,000,000", "24,000", "$2.08", "19,200", "192", "$260", "$239,808", "4.80x", False),
]

BREAKEVEN = [
 ("$20,000", "16 purchases", "0.21%", "20,000 divided by 1,249 is 16.0 purchases. 16 divided by 7,680 landing page views is 0.21 percent."),
 ("$50,000", "40 purchases", "0.21%", "50,000 divided by 1,249 is 40.0 purchases. 40 divided by 19,200 landing page views is 0.21 percent."),
]

CEO_DECISION = {
 "head": "The decision in front of you.",
 "lines": [
  "Line B only becomes real once a checkout exists, and no checkout exists today, which is the red alert at the top of the Go Live tab.",
  "Until that is fixed every dollar of the $20,000 is forced into Line A, whether or not that is the line you would choose.",
  "Line A at the sister brand close rate returns 11.3x. Line A at LLA today returns close to nothing, because almost nobody answers the phone.",
  "So the first move is not a budget move. It is a checkout and a contact rate.",
 ],
}

LINE_COMPARE = [
 ("Objective",              "Leads",                                   "Sales, optimising Purchase"),
 ("Status",                 "Live, carrying the full $20,000",         "Blocked, no checkout URL exists"),
 ("Optimisation event",     "Qualified Lead",                          "Initiate Checkout, then Purchase above 8 per week"),
 ("Attribution",            "Default click window",                    "Seven day click, one day view"),
 ("Placements",             "Manual, six surfaces, no Audience Network","Advantage+ placements"),
 ("Base case at $20,000",   "$111 cost per acquisition at an 18 percent close", "$526 cost per acquisition at a 0.5 percent checkout rate"),
 ("Base case return",       "11.3x",                                   "2.37x"),
 ("The variable that decides it", "Contact rate on a 45 plus audience", "Checkout conversion rate on cold traffic"),
 ("What breaks it",         "Nobody answers the phone",                "The checkout returns 404"),
]

# Replacement forecast rows with $20k as base
FORECAST_SCENARIOS_V2 = [
 ("$10,000", "13.5", "$739", "$16,895", "1.69x", "Below the level the account runs at today. Shown for slope only."),
 ("$20,000", "27.0", "$739", "$33,790", "1.69x", "Current spend. Roughly two cohorts a month at the base case."),
 ("$25,000", "33.8", "$739", "$42,237", "1.69x", "First step up, held under a 20 percent increment per change."),
 ("$50,000", "67.6", "$739", "$84,473", "1.69x", "The recommended ceiling, and the only tier where Initiate Checkout clears 50 a week."),
]

CASHFLOW_V2 = [
 ("$10,000", "13.5", "$3,909",  "0.39x", "$19,546", "1.95x"),
 ("$20,000", "27.0", "$7,803",  "0.39x", "$38,804", "1.94x"),
 ("$25,000", "33.8", "$9,773",  "0.39x", "$48,865", "1.95x"),
 ("$50,000", "67.6", "$19,546", "0.39x", "$97,729", "1.95x"),
]

FUNNEL_ROWS_V2 = [
 ("$10,000", "Conservative", "357,143",   "4,286",  "$2.33", "2,357",  "17.0",  "$589", "2.8",   "$3,535", "$3,533",  "0.35x", False),
 ("$10,000", "Base",         "483,092",   "9,662",  "$1.03", "6,763",  "67.6",  "$148", "13.5",  "$739",   "$16,895", "1.69x", True),
 ("$10,000", "Optimistic",   "625,000",   "16,875", "$0.59", "13,500", "162.0", "$62",  "40.5",  "$247",   "$50,584", "5.06x", False),
 ("$20,000", "Conservative", "714,286",   "8,572",  "$2.33", "4,714",  "34.0",  "$589", "5.7",   "$3,535", "$7,067",  "0.35x", False),
 ("$20,000", "Base",         "966,184",   "19,324", "$1.03", "13,526", "135.2", "$148", "27.0",  "$739",   "$33,790", "1.69x", True),
 ("$20,000", "Optimistic",   "1,250,000", "33,750", "$0.59", "27,000", "324.0", "$62",  "81.0",  "$247",   "$101,169","5.06x", False),
 ("$25,000", "Conservative", "892,857",   "10,714", "$2.33", "5,893",  "42.4",  "$589", "7.1",   "$3,535", "$8,832",  "0.35x", False),
 ("$25,000", "Base",         "1,207,729", "24,155", "$1.03", "16,908", "169.1", "$148", "33.8",  "$739",   "$42,237", "1.69x", True),
 ("$25,000", "Optimistic",   "1,562,500", "42,188", "$0.59", "33,750", "405.0", "$62",  "101.2", "$247",   "$126,461","5.06x", False),
 ("$50,000", "Conservative", "1,785,714", "21,429", "$2.33", "11,786", "84.9",  "$589", "14.1",  "$3,535", "$17,664", "0.35x", False),
 ("$50,000", "Base",         "2,415,459", "48,309", "$1.03", "33,816", "338.2", "$148", "67.6",  "$739",   "$84,473", "1.69x", True),
 ("$50,000", "Optimistic",   "3,125,000", "84,375", "$0.59", "67,500", "810.0", "$62",  "202.5", "$247",   "$252,922","5.06x", False),
]

META_PLAN_V2 = [
 ("Now", "$20,000 / month", "One campaign, one broad ad set, Line A only", "Qualified Lead on a website form",
  "Current spend. The whole budget is trapped in Line A until a checkout exists."),
 ("On checkout launch", "$20,000 / month split", "Line A held, Line B opened as a second campaign", "Initiate Checkout on Line B, Qualified Lead on Line A",
  "Base case on Line B alone at the full $20,000 returns 38 purchases and $47,462 at 2.37x."),
 ("Scale", "$50,000 / month", "One Advantage+ Shopping campaign plus one consolidated retargeting ad set", "Purchase, once volume clears roughly 8 per week",
  "Base case returns 96 purchases and $119,904 at 2.40x."),
]

FORECAST_CHIPS_V2 = [
 ("$20,000", "monthly spend running today", "Client stated, this hub is modelled from that number"),
 ("38", "purchases at $20,000 on the Line B base case", "0.5 percent checkout conversion on 7,680 landing page views"),
 ("$526", "cost per acquisition on that case", "$20,000 divided by 38 purchases"),
 ("2.37x", "return on ad spend on that case", "$47,462 revenue against $20,000 of spend"),
]
