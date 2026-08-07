# -*- coding: utf-8 -*-
# Tabs 2, 4, 5, 6. No em dashes, no en dashes, no exclamation marks.

PRICING = "https://longevitylifeacademy.com/pricing.html"

# ================================================================ TAB 2 META
META_HEADLINE = "There is no purchase event to optimise toward."

META_HERO_CHIPS = [
 ("0", "checkout URLs that resolve", "/enroll.html, /checkout.html and /apply.html all return 404"),
 ("#lead-gen", "where both pricing CTAs land", "Start Monthly and Enroll Upfront both point at a homepage anchor"),
 ("$28.22", "median Education lead cost", "LLA already buys leads under this number"),
 ("1 : 1", "campaigns to ad sets", "Consolidation is the structural fix, not budget size"),
]

# 5. THE REAL BLOCKER -> headline block
META_BLOCKER = {
 "head": "Meta cannot optimise for a purchase that cannot happen.",
 "lines": [
  ("Both pricing page CTAs resolve to the homepage anchor #lead-gen, so no checkout is ever reached.",
   [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
  ("/enroll.html, /checkout.html and /apply.html were each requested directly and each returned 404.",
   [("longevitylifeacademy.com", "https://longevitylifeacademy.com/")]),
  ("Terms of Service require an admissions review and an enrollment agreement before payment, which is legally incompatible with self serve checkout.",
   [("terms.html", "https://www.longevitylifeacademy.com/terms.html")]),
  ("No Stripe, Paddle, PayPal or other processor reference appears anywhere in the fetched page source.",
   [("pricing.html source", "https://www.longevitylifeacademy.com/pricing.html")]),
 ],
 "close": "Fix the checkout and the signal problem largely solves itself, because a real Purchase event with a value parameter is the input every other recommendation on this page depends on.",
}

# 1. The 50 rule, reframed
META_FIFTY = {
 "head": "The 50 per week rule is a signal threshold, not a profitability threshold.",
 "chips": [
   ("Per ad set", "where the 50 is measured", "Not per account and not per campaign"),
   ("Permanent", "how long accounts run Learning Limited", "Profitable high ticket accounts sit here for years"),
   ("Never", "how often a CEO should be told he needs six figures a month to exit learning", "That framing is wrong and has been removed"),
 ],
 "lines": [
  ("Meta measures the 50 conversion threshold per ad set, which is why the fix is structural rather than financial.",
   [("Meta Business Help Center", "https://en-gb.facebook.com/business/help/910877842876429")]),
  ("Learning Limited means the delivery system has less signal than it wants, not that the ad set stops spending or stops selling.",
   [("Meta on the learning phase", "https://www.facebook.com/business/help/112167992830700")]),
 ],
}

# 2. Consolidation
META_CONSOLIDATION = {
 "head": "One campaign. One broad ad set. Every conversion pools into one signal.",
 "chips": [
   ("1", "campaign", "No parallel test campaigns competing for the same auction"),
   ("1", "broad ad set", "No age splits, no interest splits, no placement splits"),
   ("Campaign level", "where Advantage+ Shopping pools learning", "The standard answer for low volume and high order value"),
 ],
 "lines": [
  ("Meta states plainly that combining similar ad sets combines their learnings.",
   [("Meta on consolidation", "https://www.facebook.com/business/help/112167992830700")]),
  ("Consolidation may allow for an increased budget and audience size and can help meet the 50 conversions per week threshold, in Meta's own words.",
   [("Meta ad set consolidation", "https://en-gb.facebook.com/business/help/910877842876429")]),
  ("Advantage+ Shopping pools learning at campaign level rather than ad set level, which is exactly the shape of the low volume high ticket problem.",
   [("Meta on Advantage+ shopping campaigns", "https://www.facebook.com/business/help/1362234537597370?locale=en_GB")]),
  ("Advantage+ campaign budget can be edited without resetting the learning phase, so the account can be steered without paying for a restart.",
   [("Meta on significant edits", "https://www.facebook.com/business/help/316478108955072")]),
 ],
}

# 3. Attribution and value
META_ATTRIBUTION = {
 "head": "Seven day click and one day view, with value based optimisation.",
 "chips": [
   ("7d click", "attribution setting", "A considered $1,249 purchase does not close inside 24 hours"),
   ("1d view", "second half of the window", "Captures the view driven demand a 45 plus audience actually shows"),
   ("$1,249", "value the pixel must carry", "$289 on the instalment plan, never a flat value of 1"),
 ],
 "lines": [
  ("Set the attribution window to seven day click and one day view so a considered purchase is credited to the ad that caused it.",
   [("Meta attribution settings", "https://www.facebook.com/business/help/2198119873776795")]),
  ("Fire Purchase with value equal to 1249 on the upfront plan and 289 on the instalment plan, because value based optimisation bids toward the wrong customer when every event carries the same weight.",
   [("pricing.html", "https://longevitylifeacademy.com/pricing.html")]),
 ],
}

# 4. Schools and ateliers comparable
META_COMPARABLE = {
 "head": "Schools running $15 leads win at small budgets. The variable is not budget size.",
 "chips": [
   ("$15", "lead cost a language school or atelier runs at", "Client raised comparable"),
   ("$1,249", "LLA ticket", "Roughly 83 times the value of a $15 lead"),
   ("$28.22", "median Education and Instruction lead cost on Meta", "LLA already buys below the median"),
 ],
 "lines": [
  ("Education and Instruction carries a $28.22 median cost per lead on Meta, so LLA buying near $20 was already ahead of the vertical.",
   [("WordStream Facebook Ads benchmarks", "https://www.wordstream.com/blog/facebook-ads-cost")]),
  ("What separates a school at $15 from LLA at $20 is not budget, it is offer price, funnel friction and speed of follow up, and LLA is worse on all three.",
   [("pricing.html", "https://longevitylifeacademy.com/pricing.html")]),
  ("An atelier or language school sells a low ticket at an immediate yes, while LLA asks a 45 plus buyer for $1,249 through an admissions review that has no published refund calculation.",
   [("terms.html", "https://www.longevitylifeacademy.com/terms.html")]),
 ],
}

# 7. Why the phone never rings
META_PHONE = {
 "head": "Why the phone never rings.",
 "chips": [
   ("1 of 12", "leads that answered in a documented seniors test", "Roughly an 8 percent answer rate"),
   ("65 plus", "where call blocking is close to default", "Operators report the same pattern every time"),
   ("5 to 10 min", "window before a real time lead goes cold", "Not a vendor problem, a speed problem"),
 ],
 "lines": [
  ("A Meta lead ad operator running a seniors audience with OTP verification reported that out of 12 promising leads only one person picked up the phone.",
   [("r/FacebookAds thread", "https://www.reddit.com/r/FacebookAds/comments/1mjffzh/highintent_leads_from_meta_but_nobody_answers/")]),
  ("The same thread attributes it to automatic call blocking on 65 plus handsets and recommends branded SMS first, voicemail second, live call third.",
   [("QuantumWolf99 in r/FacebookAds", "https://www.reddit.com/r/FacebookAds/comments/1mjffzh/highintent_leads_from_meta_but_nobody_answers/")]),
  ("Operators report that a real time lead is worthless after 5 to 10 minutes, which no admissions team replying within 24 hours can satisfy.",
   [("r/InsuranceAgent thread", "https://www.reddit.com/r/InsuranceAgent/comments/1q7mgrd/how_can_i_tell_if_leads_are_realtime_vs_aged_junk/")]),
  ("The fix is to take the phone out of the required path and let a self selected buyer pay on the page, not to buy more forms.",
   [("pricing.html", "https://longevitylifeacademy.com/pricing.html")]),
 ],
}

# 6. Funnel model as scenario planning, with $5k pilot
FUNNEL_ROWS_2 = [
 # spend, scenario, impressions, clicks, cpc, lpv, IC, costIC, purchases, cpa, revenue, roas, highlight
 ("$5,000",  "Conservative", "178,571",   "2,143",  "$2.33", "1,179",  "8.5",   "$589", "1.4",   "$3,535", "$1,767",  "0.35x", False),
 ("$5,000",  "Base",         "241,546",   "4,831",  "$1.03", "3,382",  "33.8",  "$148", "6.8",   "$739",   "$8,447",  "1.69x", True),
 ("$5,000",  "Optimistic",   "312,500",   "8,438",  "$0.59", "6,750",  "81.0",  "$62",  "20.3",  "$247",   "$25,292", "5.06x", False),
 ("$10,000", "Conservative", "357,143",   "4,286",  "$2.33", "2,357",  "17.0",  "$589", "2.8",   "$3,535", "$3,533",  "0.35x", False),
 ("$10,000", "Base",         "483,092",   "9,662",  "$1.03", "6,763",  "67.6",  "$148", "13.5",  "$739",   "$16,895", "1.69x", True),
 ("$10,000", "Optimistic",   "625,000",   "16,875", "$0.59", "13,500", "162.0", "$62",  "40.5",  "$247",   "$50,584", "5.06x", False),
 ("$25,000", "Conservative", "892,857",   "10,714", "$2.33", "5,893",  "42.4",  "$589", "7.1",   "$3,535", "$8,832",  "0.35x", False),
 ("$25,000", "Base",         "1,207,729", "24,155", "$1.03", "16,908", "169.1", "$148", "33.8",  "$739",   "$42,237", "1.69x", True),
 ("$25,000", "Optimistic",   "1,562,500", "42,188", "$0.59", "33,750", "405.0", "$62",  "101.2", "$247",   "$126,461","5.06x", False),
 ("$50,000", "Conservative", "1,785,714", "21,429", "$2.33", "11,786", "84.9",  "$589", "14.1",  "$3,535", "$17,664", "0.35x", False),
 ("$50,000", "Base",         "2,415,459", "48,309", "$1.03", "33,816", "338.2", "$148", "67.6",  "$739",   "$84,473", "1.69x", True),
 ("$50,000", "Optimistic",   "3,125,000", "84,375", "$0.59", "67,500", "810.0", "$62",  "202.5", "$247",   "$252,922","5.06x", False),
]

FUNNEL_INPUTS = [
 ("AOV", "$1,249", "$1,249", "$1,249", "Upfront plan on the pricing page", "https://longevitylifeacademy.com/pricing.html"),
 ("CPM", "$28.00", "$20.70", "$16.00", "Health and Wellness CPM, Triple Whale, about 35,000 brands, FY2025", "https://www.triplewhale.com/blog/facebook-ads-benchmarks"),
 ("Link CTR", "1.20%", "2.00%", "2.70%", "Premium ecommerce band and Health and Wellness CTR", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
 ("Landing page view rate", "55%", "70%", "80%", "Upstack Data landing page view rate reference", "https://docs.upstackdata.com/reference/metrics/advertising/meta/meta-clicks/meta-landing-page-view-rate"),
 ("Landing page view to purchase", "0.12%", "0.20%", "0.30%", "Assumption, anchored down from the $42 AOV elite band because the LLA ticket is 29.7 times larger", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
 ("InitiateCheckout to purchase ratio", "6.0 to 1", "5.0 to 1", "4.0 to 1", "Assumption, flagged as unverified in the source model", "https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026"),
]

META_PLAN = [
 ("Pilot", "$5,000 / month", "One campaign, one broad ad set", "Qualified Lead on a website form",
  "Realistic starting budget. Base case returns 6.8 purchases and $8,447 revenue at 1.69x."),
 ("Build", "$10,000 to $25,000 / month", "Same single ad set, budget raised in steps under 20 percent", "Qualified Lead, then add InitiateCheckout once a checkout exists",
  "Base case at $25,000 returns 33.8 purchases and $42,237 revenue."),
 ("Scale", "$50,000 / month", "One Advantage+ Shopping campaign plus one consolidated retargeting ad set", "InitiateCheckout, with Purchase reported but not optimised",
  "Base case returns 67.6 purchases, $84,473 revenue, 1.69x on a $739 cost per acquisition."),
]

META_EVENT_LADDER = [
 ("Purchase at a $1,249 ticket", "$833", "Report it. Do not optimise to it below real scale."),
 ("InitiateCheckout", "$139 to $208", "The correct optimisation event once a checkout exists."),
 ("Qualified website Lead", "$28.22 to $52.98", "The correct optimisation event today."),
 ("Current instant form lead", "About $20", "Cheap and plentiful, and the reason the CPL story was a distraction."),
]

# ================================================================ TAB 4 INFLUENCERS
def infl(**k): return k

INFLUENCERS = [
infl(
 n=1, name="Mary Claire Haver, MD", role="Board certified OB-GYN and Menopause Society Certified Practitioner, founder of The Pause Life",
 chip="RED", chip_why="Owns and sells The Galveston Diet, a self paced online course with Signature at $59 through Platinum at $274.",
 chip_src=("galvestondiet.com", "https://galvestondiet.com/the-galveston-diet/"),
 counts=[("Instagram", "4M", "https://www.instagram.com/drmaryclaire/"), ("YouTube", "669K", "https://socialblade.com/youtube/@drmaryclaire"), ("TikTok", "2.3M", "https://socialblade.com/tiktok/user/drmaryclaire"), ("Substack", "83K", "https://substack.com/@drmaryclairehaver")],
 price="No rate card published. Benchmark at 4M followers is $10,000 to $50,000 plus for a feed post and $15,000 to $100,000 plus for a Reel, with a YouTube integration in the $4,000 to $9,400 band.",
 price_src=("Nowadays Media Instagram rates 2026", "https://nowadays.media/influencer-marketing/instagram-influencer-rates-2026/"),
 email_addr="partnerships@thepauselife.com", email_src=("thepauselife.com contact page", "https://thepauselife.com/pages/contact"),
 dm="https://ig.me/m/drmaryclaire", form="https://thepauselife.com/pages/contact",
 fit="The single closest audience match in the market, women 45 to 60 who have already proven they buy paid online education from her.",
 subject="Co branded longevity cohort for The Pause Life audience",
 body="""Hello,

I am writing on behalf of Longevity Life Academy, part of eTeacher Group, about a co branded partnership rather than a standard sponsored post.

We run The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson 5. Price is $1,249 upfront or five payments of $289.

I have read the Galveston Diet pages and I understand the overlap question. Our format is the opposite of self paced. Nobody buys The Longevity Blueprint instead of a self paced program, they buy it when self paced has already failed them and they want a live class of fifteen people and a teacher who knows their name.

What I would like to explore is a co branded cohort. Your audience, our faculty, revenue share on enrollments, and a named seat allocation for Pause Life members.

Two questions. Would a co branded live cohort clear your exclusivity position, and who should I speak with on commercial terms.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=2, name="Gabrielle Lyon, DO", role="Board certified family physician, founder of Muscle Centric Medicine and Strong Medical",
 chip="AMBER", chip_why="Owns a virtual clinic and a community, but no self paced longevity course, and publishes a dedicated brand partnership address.",
 chip_src=("drgabriellelyon.com contact", "https://drgabriellelyon.com/contact/"),
 counts=[("Instagram", "1M", "https://www.instagram.com/drgabriellelyon/"), ("YouTube", "282K", "https://socialblade.com/youtube/@drgabriellelyon"), ("X", "33K", "https://x.com/drgabriellelyon"), ("TikTok", "134K", "https://socialblade.com/tiktok/user/drgabriellelyon")],
 price="No rate published. Benchmark is the 1M plus Instagram tier at $10,000 to $50,000 plus per feed post, with a YouTube integration at $1,300 to $3,700 in the 100K to 300K band.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="contact@drgabriellelyon.com", email_src=("drgabriellelyon.com contact page", "https://drgabriellelyon.com/contact/"),
 dm="https://ig.me/m/drgabriellelyon", form="https://drgabriellelyon.com/contact/",
 fit="Protect skeletal muscle to protect healthspan is the exact message that converts a 45 to 65 female buyer, and her long form podcast gives room to explain an 18 week format.",
 subject="Podcast partnership, 18 week live longevity course, 45 plus audience",
 body="""Hello,

You publish contact@drgabriellelyon.com for business and brand partnerships, so I am using it directly.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars covering nutrition, sleep, exercise and movement, supplements and wearables, stress management and a written personal protocol. An Abbott Lingo continuous glucose monitor ships to every student before lesson 5. Price is $1,249 upfront or five payments of $289.

We are interested in host read mid roll placements on The Dr. Gabrielle Lyon Show plus a YouTube integration, because a live cohort format needs sixty seconds of explanation rather than a caption.

Your clinic is a service and ours is an education product, so I do not see a conflict, and I would rather you tell me if you do.

Please send your rate card for a host read mid roll, a YouTube integration and a bundled quarter. eTeacher Group has taught more than 400,000 students in 197 countries across 25 years and holds 4.6 out of 5 on Trustpilot from more than 600 verified reviews.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=3, name="Stacy T. Sims, MSc, PhD", role="Exercise physiologist and nutrition scientist specialising in sex differences in training and menopause",
 chip="RED", chip_why="Sells a full catalogue of competing paid online courses on Kajabi including Menopause 2.0 and Women Are Not Small Men.",
 chip_src=("drstacysims.com", "https://www.drstacysims.com/"),
 counts=[("Instagram", "966K", "https://www.instagram.com/drstacysims/"), ("YouTube", "356K", "https://socialblade.com/youtube/@drstacysims")],
 price="No rate published. Benchmark is the 500K to 1M macro tier at $2,500 to $10,000 per feed post and $5,000 to $15,000 per Reel.",
 price_src=("Nowadays Media Instagram rates 2026", "https://nowadays.media/influencer-marketing/instagram-influencer-rates-2026/"),
 email_addr="support@drstacysims.com", email_src=("drstacysims.com privacy policy", "https://www.drstacysims.com/pages/privacy-policy"),
 dm="https://ig.me/m/drstacysims", form="https://www.drstacysims.com/contact",
 fit="Active women 45 to 65 is her core audience, though she is based in New Zealand so a meaningful share sits outside the United States and Canada.",
 subject="Referral partnership rather than sponsorship, live longevity cohort",
 body="""Hello,

Please pass this to whoever handles commercial partnerships.

I represent Longevity Life Academy, part of eTeacher Group. We run The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor included before lesson 5. Price is $1,249 upfront or five payments of $289.

I have read the course catalogue on drstacysims.com and I am not going to pretend there is no overlap, so I am proposing a referral arrangement instead of a sponsored post. Your students finish Menopause 2.0 and Women Are Not Small Men and then want a live cohort with a teacher and a CGM. We would pay a referral fee on every enrollment that comes from a Dr Stacy Sims link, with no obligation on your content calendar.

Two questions. Is a paid referral arrangement something you consider, and what fee level would make it worth your time.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=4, name="Rhonda Patrick, PhD", role="Biomedical scientist, founder of FoundMyFitness",
 chip="AMBER", chip_why="Owns FoundMyFitness Premium at $15 per month, a low ticket content membership rather than a structured cohort course.",
 chip_src=("foundmyfitness.com/premium", "https://www.foundmyfitness.com/premium"),
 counts=[("Instagram", "1M", "https://www.instagram.com/foundmyfitness/"), ("YouTube", "712K", "https://socialblade.com/youtube/c/foundmyfitness"), ("X", "653.5K", "https://x.com/foundmyfitness"), ("Podcast", "Top 50 US and Canada", "https://rephonic.com/podcasts/foundmyfitness")]
,
 price="Her live advertising intake publishes budget bands of $1k to $5k, $5k to $10k, $10k to $20k, $20k to $50k and $50k plus, which is the most concrete pricing signal in this roster.",
 price_src=("Podvertise listing", "https://podvertise.fm/818198322"),
 email_addr="No address published, the contact page is a form capped at 750 characters", email_src=("foundmyfitness.com/contact", "https://www.foundmyfitness.com/contact"),
 dm="https://ig.me/m/foundmyfitness", form="https://www.foundmyfitness.com/contact",
 fit="The podcast is the commercial asset, top 50 in both United States and Canada Health and Fitness with an average episode of 113 minutes.",
 subject="Host read sponsorship enquiry, $20k to $50k band",
 body="""Hello,

Submitting through the advertising intake in the $20,000 to $50,000 band, format host read.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson 5 with 14 days of app access. $1,249 upfront or five payments of $289.

FoundMyFitness is the closest audience in the market to ours and the 113 minute average episode is the only format long enough to explain a live cohort properly.

Requesting a quote for a three episode host read mid roll flight with a unique tracked link, and separately for a single dedicated segment. Happy to work inside your existing science first framing and to send the full curriculum for review before anything is recorded.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=5, name="Eric Topol, MD", role="Cardiologist, Founder and Director of the Scripps Research Translational Institute, author of Super Agers",
 chip="GREEN", chip_why="No competing paid course, membership, protocol program or supplement business found, and he publicly states no pharmaceutical or vaccine manufacturer conflicts.",
 chip_src=("Ground Truths About page", "https://erictopol.substack.com/about"),
 counts=[("X", "678K", "https://x.com/EricTopol"), ("Substack", "Ground Truths newsletter and podcast", "https://erictopol.substack.com/about")],
 price="No rate published anywhere fetched. A large newsletter sponsorship would price on impression CPM, with the nearest verified anchor being the $25 to $92 sponsored content band carrying a 1.7 times Health and Longevity multiplier.",
 price_src=("PodVenues 2026 rate card", "https://podvenues.com/reports/podcast-sponsorship-ad-rates-2026"),
 email_addr="etopol@scripps.edu", email_src=("ASCI member directory", "https://data.the-asci.org/controllers/asci/DirectoryController.php?action=profile&entryId=159910"),
 dm="No verified Instagram account", form="https://www.scripps.edu/news-events/in-the-media/",
 fit="The cleanest partner in the set and the only one with zero commercial conflict, best approached as an editorial or guest expert partnership rather than an influencer deal.",
 subject="Guest lecture invitation, live longevity course faculty",
 body="""Dear Professor Topol,

This is an invitation to teach, not a request to advertise.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course taught to cohorts of 8 to 15 adults in eighteen live 50 minute sessions. Six pillars, a written personal protocol, and an Abbott Lingo continuous glucose monitor for every student before lesson 5.

Super Agers is the argument our curriculum is built around, and our students are exactly the readers of Ground Truths, median age above 55 and unusually literate about the evidence.

I would like to offer you a paid single guest session on the science of healthy ageing, recorded once and used across cohorts, with full editorial control and no product endorsement of any kind. If a paid honorarium is not appropriate given your institutional position, we would make an equivalent donation to Scripps Research.

Separately, if Ground Truths accepts sponsorship, please tell me the rate.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=6, name="Mark Hyman, MD", role="Functional medicine physician, host of The Dr. Hyman Show, co founder of Function Health",
 chip="RED", chip_why="Sells supplements and programs direct through his own commerce site and co founded a paid membership diagnostics business.",
 chip_src=("drhyman.com", "https://drhyman.com/"),
 counts=[("Instagram", "4M", "https://www.instagram.com/drmarkhyman/"), ("YouTube", "1.5M", "https://socialblade.com/youtube/@drmarkhyman")],
 price="No rate published. Benchmark is $10,000 to $50,000 plus per Instagram feed post at the 1M plus tier and $10,000 to $23,000 for a YouTube integration in the 700K to 1.5M band.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="No address published, the contact page routes to a form and lists 888 702 2995 with a 24 hour response", email_src=("drhyman.com contact", "https://drhyman.com/pages/contact"),
 dm="https://ig.me/m/drmarkhyman", form="https://drhyman.com/pages/contact",
 fit="Reach is above the target band and the commerce conflict is direct, so the only viable structure is a co branded offering rather than a placement.",
 subject="Co branded cohort proposal, not a placement request",
 body="""Hello,

I am not asking for a sponsored post, because drhyman.com is a commerce site and a paid placement would sit inside your own product surface.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

The proposal is a co branded cohort. Function Health members get labs. What they do not get is eighteen weeks of live teaching that tells them what to do with the results. We would build a co branded cohort, share revenue, and put your name on the curriculum review rather than on an ad read.

If that is interesting, please route me to whoever owns partnerships. If it is not, a straight rate card for a podcast host read is the fallback and I will take that answer too.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=7, name="Max Lugavere", role="Health and science journalist, filmmaker, host of The Genius Life podcast",
 chip="GREEN", chip_why="No paid online course, cohort program or membership found on his site, his revenue is books, media and podcast sponsorship.",
 chip_src=("maxlugavere.com contact", "https://www.maxlugavere.com/contact"),
 counts=[("Instagram", "1M", "https://www.instagram.com/maxlugavere/"), ("Podcast", "Top 40 US Spotify health with Canadian penetration", "https://www.maxlugavere.com/")],
 price="No rate published and no email or rate card on his site. Benchmark is the 1M plus Instagram tier plus a host read at $25 to $92 CPM with a 1.7 times health multiplier.",
 price_src=("PodVenues 2026 rate card", "https://podvenues.com/reports/podcast-sponsorship-ad-rates-2026"),
 email_addr="No address published, both the contact and speaking pages are forms only", email_src=("maxlugavere.com contact", "https://www.maxlugavere.com/contact"),
 dm="https://ig.me/m/maxlugavere", form="https://www.maxlugavere.com/contact",
 fit="The best combination in the roster of a clean screen, reach inside the target band, and a podcast that converts, plus real Canadian chart presence.",
 subject="The Genius Life host read, 18 week live longevity cohort",
 body="""Hello,

Sending through the contact form because no address is published.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars covering nutrition, sleep, exercise and movement, supplements and wearables, stress management and a written personal protocol. Every student gets an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

You are our first approach in this category, for a specific reason. You do not sell a competing course, your audience sits in the band we sell to, and The Genius Life charts in Canada as well as the United States, which matters because we sell into both.

Requesting a rate for a three episode host read mid roll flight with a tracked link and a promo code, and separately for one long form interview with our founding faculty member Julie Gibson Clark, who is ranked second in the world on the Rejuvenation Olympics leaderboard with a DunedinPACE score of 0.665.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=8, name="Peter H. Diamandis, MD", role="Founder of XPRIZE, co founder of Singularity University, curator of Abundance360",
 chip="RED", chip_why="Abundance360 is a year round paid membership starting at $12,500 a year with longevity workshops, a direct structural competitor at a higher price point.",
 chip_src=("abundance360.com", "https://www.abundance360.com/"),
 counts=[("YouTube", "518K", "https://socialblade.com/youtube/@peterdiamandis"), ("X", "409.4K", "https://x.com/PeterDiamandis"), ("Instagram", "266K", "https://www.instagram.com/peterdiamandis/")],
 price="No rate published. Benchmark is a YouTube integration at $4,000 to $9,400 and a dedicated video at $6,000 to $14,000 in the 300K to 700K band.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="No press or business address published on either property", email_src=("diamandis.com", "https://www.diamandis.com/"),
 dm="https://ig.me/m/peterdiamandis", form="https://www.abundance360.com/",
 fit="Audience is right on technology and longevity but wrong on price sensitivity, and Abundance360 already owns the education slot at twenty five times our ticket.",
 subject="Downstream offer for Abundance360 non converters",
 body="""Hello,

Abundance360 sits at $12,500 a year. Ours sits at $1,249. That difference is the reason I am writing rather than the reason not to.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5.

Every year a large number of people look at Abundance360, want the longevity content, and cannot justify the membership. Today they get nothing. The proposal is a downstream referral arrangement where those people are offered a live longevity cohort at a tenth of the price, with a referral fee back to you and zero cannibalisation, because nobody who can pay $12,500 chooses $1,249 instead.

Who owns partnerships on the Abundance360 side.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=9, name="Darshan Shah, MD", role="Board certified surgeon, Founder and CEO of Next Health, host of the EXTEND podcast",
 chip="RED", chip_why="Next Health sells a $299 baseline test, a $2,999 total wellness package and a $14,500 executive physical, so his audience attention is already routed to his own longevity funnel.",
 chip_src=("next-health.com", "https://www.next-health.com/"),
 counts=[("Instagram", "191K", "https://www.instagram.com/darshanshahmd/"), ("Podcast", "EXTEND, no verified listener figure", "https://www.next-health.com/")],
 price="No rate published. Benchmark is the 100K to 500K mid tier at $500 to $2,500 per feed post and $800 to $5,000 per Reel.",
 price_src=("Nowadays Media Instagram rates 2026", "https://nowadays.media/influencer-marketing/instagram-influencer-rates-2026/"),
 email_addr="No contact address published on next-health.com", email_src=("next-health.com", "https://www.next-health.com/"),
 dm="https://ig.me/m/darshanshahmd", form="No contact form published",
 fit="Just below the target band on reach, but the intent density is the highest in the roster because his audience already pays four figures for longevity services.",
 subject="Education layer for Next Health members",
 body="""Hello,

Next Health sells the measurement. We sell the eighteen weeks that follow it.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

A member who pays $299 for a baseline test or $2,999 for a total wellness package walks out with numbers and no structured programme to act on them. That is the gap we fill, and it does not compete with a single line item on your menu.

The proposal is an education layer offered to Next Health members at a member rate, with revenue share, or a straight paid placement on EXTEND if you prefer to keep it simple.

Who is the right person for partnerships.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=10, name="Sten Ekberg, DC", role="Former Swedish Olympic decathlete and holistic doctor running Wellness For Life in Cumming, Georgia",
 chip="AMBER", chip_why="His site markets remote consultations and online education but lists no named paid course, membership, programme price or supplement line.",
 chip_src=("drekberg.com", "https://drekberg.com/"),
 counts=[("YouTube", "5.4M", "https://socialblade.com/youtube/@drekberg")],
 price="No rate published. The top published band of 700K to 1.5M subscribers gives $10,000 to $23,000 for an integration, so a 5.4M channel prices materially above that and should be quoted on a $14 to $22 CPM against actual average views.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="No contact address published on drekberg.com", email_src=("drekberg.com", "https://drekberg.com/"),
 dm="https://ig.me/m/drstenekberg", form="No contact form published",
 fit="The topical bullseye for a course that includes a continuous glucose monitor, because his channel is the largest metabolic health explainer on YouTube.",
 subject="CGM course integration, metabolic health audience",
 body="""Hello,

Your channel is the largest metabolic health explainer on YouTube and our course ships a continuous glucose monitor to every student. The overlap is close to exact.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson 5 with 14 days of app access. $1,249 upfront or five payments of $289.

The natural format is a single integration inside a glucose video where you show what the data actually looks like across eighteen weeks of structured teaching, rather than a read at the top.

Requesting a rate for one integration and one dedicated video, priced against actual average views. Also asking directly, because your site does not say, whether you currently sell a course or supplement line we would need to work around.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=11, name="Brad Stanfield, MD", role="Family medicine physician in Auckland running an evidence review longevity channel",
 chip="RED", chip_why="Owns a direct to consumer supplement brand with published prices from $40 to $90, so essentially every video funnels to his own commerce even though he sells no course.",
 chip_src=("drstanfield.com", "https://drstanfield.com/pages/llms-txt"),
 counts=[("YouTube", "343K", "https://www.drstanfield.com/")],
 price="No rate published. Benchmark is $4,000 to $9,400 for an integration and $6,000 to $14,000 for a dedicated video in the 300K to 700K band at a $14 to $22 health CPM.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="No address published, the contact page carries a form only", email_src=("drstanfield.com contact", "https://drstanfield.com/pages/contact"),
 dm="No verified Instagram handle", form="https://drstanfield.com/pages/contact",
 fit="Zero education overlap because he sells no course, but the share of voice a sponsor gets is reduced by the constant supplement promotion.",
 subject="Evidence review integration, 18 week live course",
 body="""Hello,

You review evidence line by line, so here is the offer stated the same way.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars covering nutrition, sleep, exercise and movement, supplements and wearables, stress management and a written personal protocol. Every student receives an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

We are not asking you to endorse a claim. We are asking for a paid integration in which you are free to say on camera what the evidence does and does not support about structured longevity education, with our full curriculum sent to you first for review.

You sell MicroVitamin and Sleep by Dr Brad. We sell teaching. There is no product conflict.

Requesting your rate for one integration and one dedicated video.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=12, name="Nicolas Verhoeven, PhD", role="Physiologist running Physionic, a channel dedicated to line by line breakdown of research papers",
 chip="RED", chip_why="Sells Physionic Insiders, a paid membership, plus a paid course on analysing studies, with no refunds on any purchase for any reason.",
 chip_src=("physionic.org", "https://physionic.org/"),
 counts=[("YouTube", "385K", "https://physionic.org/")],
 price="No rate published. Benchmark is $4,000 to $9,400 for an integration in the 300K to 700K band.",
 price_src=("SponsorCraft YouTube rates 2026", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 email_addr="nicolasverhoeven@physionic.org", email_src=("physionic.org", "https://physionic.org/"),
 dm="No verified Instagram handle", form="No contact form published",
 fit="A small, highly analytical audience that self selects for exactly the kind of buyer who reads a curriculum before paying, though the course and membership overlap is direct.",
 subject="Paid integration, and a question about your course overlap",
 body="""Hello Nicolas,

Writing directly to the address published on physionic.org.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

I have seen Physionic Insiders and the course on analysing studies. Yours teaches people to read the literature. Ours teaches people to run a protocol on their own biomarkers for eighteen weeks with a teacher in the room. Different jobs, same audience.

Requesting your rate for one integration with a tracked link. I would also welcome a direct answer on whether you consider us a competitor, because I would rather know now than after a contract.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=13, name="Siim Land", role="Author of ten health and longevity books, operating through SIIM LAND OU, an Estonian advertising agency",
 chip="AMBER", chip_why="His site lists only books with no courses, coaching, supplements or memberships, and 99.53 percent of his company revenue is classified as advertising agency activity.",
 chip_src=("Estonian business registry", "https://www.inforegister.ee/en/14674104-SIIM-LAND-OU/"),
 counts=[("Instagram", "412K", "https://www.siimland.co/"), ("Company", "265,300 EUR forecast 2025 turnover", "https://www.inforegister.ee/en/14674104-SIIM-LAND-OU/")],
 price="Registry data implies roughly 22,108 EUR average monthly turnover across all sponsorship activity, which points to deal sizes in the low to mid four figures rather than five.",
 price_src=("Estonian business registry", "https://www.inforegister.ee/en/14674104-SIIM-LAND-OU/"),
 email_addr="siim@siimland.com", email_src=("Inforegister, SIIM LAND OU", "https://www.inforegister.ee/en/14674104-SIIM-LAND-OU/"),
 dm="https://ig.me/m/siimland", form="No contact form, the site page was blocked to automated fetching",
 fit="Sponsorship is literally his registered business model, which makes him the cheapest and fastest yes in the roster, offset by a weaker United States and Canada demographic.",
 subject="Paid sponsorship, live longevity course, US and Canada focus",
 body="""Hello Siim,

Direct and commercial, since sponsorship is the business.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

Our buyer is 45 plus in the United States and Canada, so before we discuss price I need your geographic split on Instagram and YouTube. If the United States and Canada share is above forty percent this is worth doing at real budget.

Requesting a rate for a bundle of one YouTube integration, two Instagram Reels and two Stories, with a tracked link and a promo code, run over one month. We pay on invoice in EUR and can start inside two weeks.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=14, name="Kara Fitzgerald, ND", role="Naturopathic doctor, principal investigator of the first published human trial to reverse biological age",
 chip="RED", chip_why="Sells the Younger You Practitioner Training Program at $159 plus a consumer 3YY digital program, the closest small scale competitor to LLA.",
 chip_src=("drkarafitzgerald.com training", "https://www.drkarafitzgerald.com/trainingyyi/"),
 counts=[("Instagram", "133K", "https://drkarafitzgerald.com/"), ("Podcast", "New Frontiers in Functional Medicine", "https://drkarafitzgerald.com/")],
 price="No rate published. Benchmark is the 100K to 500K mid tier at $500 to $2,500 per feed post plus a host read at $25 to $92 CPM with a 1.7 times health multiplier.",
 price_src=("PodVenues 2026 rate card", "https://podvenues.com/reports/podcast-sponsorship-ad-rates-2026"),
 email_addr="No address published on the professional contact page, which is a form", email_src=("drkarafitzgerald.com contact", "https://drkarafitzgerald.com/contact/"),
 dm="https://ig.me/m/drkarafitzgerald", form="https://drkarafitzgerald.com/contact/",
 fit="The smallest audience in the set and the highest intent density, because her trial participants already believe biological age is measurable and movable.",
 subject="Faculty guest session and a referral arrangement",
 body="""Hello,

Your 2021 trial is cited in our curriculum, which is the reason for this note.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

I have read the Younger You Practitioner Training at $159 and the 3YY program. Yours trains practitioners and runs a defined eight week protocol. Ours is an eighteen week general education cohort for consumers. The overlap is real but partial.

Two proposals. A paid guest session with our cohort on epigenetic age reversal, recorded once with full editorial control. And a referral arrangement in both directions, since your practitioner graduates need somewhere to send consumers and our students frequently want a practitioner.

Who handles partnerships.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
infl(
 n=15, name="Kayla Barnes-Lentz", role="Female longevity researcher, host of The Longevity Optimization Podcast, based in Austin",
 chip="AMBER", chip_why="Runs a membership community with no published price, so the degree of overlap could not be quantified, though her contact page exists specifically for press, speaking and partnership enquiries.",
 chip_src=("kaylabarnes.com contact", "https://kaylabarnes.com/contact"),
 counts=[("Instagram", "524K", "https://www.instagram.com/kaylabarnes/"), ("YouTube", "38.2K", "https://socialblade.com/youtube/@kaylabarneslentz")],
 price="No rate published. Benchmark is the 500K to 1M macro tier at $2,500 to $10,000 per feed post and $5,000 to $15,000 per Reel.",
 price_src=("Nowadays Media Instagram rates 2026", "https://nowadays.media/influencer-marketing/instagram-influencer-rates-2026/"),
 email_addr="No address published on the partnership page", email_src=("kaylabarnes.com contact", "https://kaylabarnes.com/contact"),
 dm="https://ig.me/m/kaylabarnes", form="https://kaylabarnes.com/contact",
 fit="A female first press halo across Bloomberg, the Wall Street Journal, Elle, Fortune and Forbes, which matters against a buyer base that is 54.5 percent female.",
 subject="Partnership enquiry, female first longevity cohort",
 body="""Hello,

Using the page you keep for press, speaking and partnership enquiries.

Longevity Life Academy, part of eTeacher Group, runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15 adults, six pillars, and an Abbott Lingo continuous glucose monitor before lesson 5. $1,249 upfront or five payments of $289.

Our buyer base runs 54.5 percent female and skews 45 plus, which is why your audience is a better match than most channels twice its size.

Before pricing, one question. Your membership community has no published price, so please tell me what it costs and what it includes, because if it competes with a paid cohort I would rather build a co branded women only cohort with you than run a placement against it.

Requesting your rate card for a Reel plus Stories bundle and for a podcast host read.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
https://longevitylifeacademy.com/pricing.html""",
),
]

INFL_BENCHMARKS = [
 ("$25 to $92", "podcast host read CPM band", "Health and Longevity carries a 1.7 times niche multiplier", "https://podvenues.com/reports/podcast-sponsorship-ad-rates-2026"),
 ("$1,300 to $23,000", "YouTube integration by channel size", "100K to 300K at the bottom, 700K to 1.5M at the top", "https://variant-intl.com/blog/youtube-sponsorship-rates-2026.html"),
 ("$500 to $50,000", "Instagram feed post by tier", "Mid tier 100K to 500K through mega above 1M", "https://nowadays.media/influencer-marketing/instagram-influencer-rates-2026/"),
 ("54.5%", "female share of the comparable audience", "Similarweb, peterattiamd.com, June 2026", "https://www.similarweb.com/website/peterattiamd.com/"),
]

INFL_ORDER = "Max Lugavere first, then Eric Topol, then Gabrielle Lyon, then Sten Ekberg, then Siim Land."

# ================================================================ TAB 5 EMAILS
RECOVERY = [
 {"stage": "Stage 1, sent 45 minutes after abandonment",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "Your seat is held for 48 hours",
  "pre": "Cohort of 8 to 15. We hold one seat while you decide.",
  "body": """Hello,

You started an enrollment for The Longevity Blueprint and stopped before it completed.

Classes run at 8 to 15 adults, so a seat that is held is a seat nobody else can take. Yours is held for 48 hours.

Eighteen weeks. Eighteen live 50 minute sessions. Six pillars covering nutrition, sleep, exercise and movement, supplements and wearables, stress management, and your own written longevity protocol. An Abbott Lingo continuous glucose monitor ships to you before lesson 5.

$1,249 paid upfront, reduced from $1,800. Or five payments of $289.

Finish your enrollment: https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
 {"stage": "Stage 2, sent 24 hours after abandonment",
  "frm": "Julie Gibson Clark <faculty@longevitylifeacademy.com>",
  "subj": "The number on my last epigenetic test was 0.665",
  "pre": "What a DunedinPACE score actually means for a person who is 55.",
  "body": """Hello,

I am Julie Gibson Clark and I teach on The Longevity Blueprint.

My DunedinPACE score is 0.665, which reads as roughly eight months of biological aging per calendar year. It puts me second in the world on the Rejuvenation Olympics leaderboard. I was a structural engineer and then a recruiter, and I did not get here through anything exotic.

What I did was measure, adjust, and repeat, for years. That is the whole content of the course. Eighteen live sessions where you do the same thing with your own numbers instead of mine.

Your enrollment is unfinished. $1,249 upfront or five payments of $289.

https://longevitylifeacademy.com/pricing.html

Julie Gibson Clark
Founding Faculty, Longevity Life Academy"""},
 {"stage": "Stage 3, sent 72 hours after abandonment",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "Upfront saves you $196 against the plan",
  "pre": "The arithmetic on both payment options, in full.",
  "body": """Hello,

Here is the price arithmetic with nothing left out.

Upfront is $1,249. List price is $1,800, so that is $551 off.

The plan is five payments of $289, which totals $1,445. Paying upfront therefore saves a further $196. The plan can be cancelled at any time and there is no setup fee.

Both options include all eighteen live 50 minute sessions, the class forum, weekly assignments, recordings when you miss a session, the written personal protocol at the end, and the Abbott Lingo continuous glucose monitor shipped before lesson 5.

eTeacher Group holds 4.6 out of 5 on Trustpilot across more than 600 verified reviews, after 25 years and more than 400,000 students in 197 countries.

https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
 {"stage": "Stage 4, sent 7 days after abandonment, final",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "Releasing your seat today",
  "pre": "Last note on this cohort. The next one starts later.",
  "body": """Hello,

We are releasing the seat that was held for you so the next cohort can be filled.

If the timing was the problem, reply with the word LATER and we will hold you for the following intake with the same $1,249 price.

If the price was the problem, reply with the word PLAN and admissions will set up the five payment option at $289 a month.

If it was neither, reply and tell us what stopped you. That answer is worth more to us than the sale.

https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
]

DRIP = [
 {"stage": "Day 0, immediately after the enquiry form",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "What the eighteen weeks actually contain",
  "pre": "Four phases, six pillars, one written protocol you keep.",
  "body": """Hello,

Thank you for asking about The Longevity Blueprint. Here is the full shape of it before anyone calls you.

Eighteen weeks. Eighteen live 50 minute sessions, taught live rather than recorded, with recordings available when you miss one. Four phases. A class of 8 to 15 adults.

Six pillars: nutrition, sleep, exercise and movement, supplements and wearables, stress management, and your own longevity protocol.

An Abbott Lingo continuous glucose monitor is included and ships before lesson 5, with 14 days of app access. One unit per student, United States addresses, students must be 18 or older, not for insulin users, not for medical diagnosis.

$1,249 upfront or five payments of $289.

https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
 {"stage": "Day 2",
  "frm": "Longevity Life Academy <faculty@longevitylifeacademy.com>",
  "subj": "Who is actually in the room",
  "pre": "Five faculty, named, with what each one teaches.",
  "body": """Hello,

A live class is only worth the price if the people teaching it are worth listening to, so here they are.

Julie Gibson Clark, founding faculty, ranked second in the world on the Rejuvenation Olympics leaderboard with a DunedinPACE score of 0.665.

Natalie Blackbourne, longevity researcher and educator, with a master's degree in emotional intelligence and close to twenty years across health, wellness and behavioural science.

Courtney Donofrio, certified Integrative Nutrition Health Coach and founder of EatBiohackLove, teaching gut health, hormone balance and biohacking for longevity.

Amy Jamieson, senior lecturer at UC Santa Barbara, with a master's in health science and kinesiology and NASM certification in personal training and corrective exercise.

Jordan Lattimore, behavioural and education specialist, psychology graduate of the University of Alberta with twelve years lived near the Nicoya Peninsula.

https://longevitylifeacademy.com/pricing.html

Longevity Life Academy by eTeacher Group"""},
 {"stage": "Day 5",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "The sensor arrives before lesson 5",
  "pre": "Why the course is built around your own glucose data.",
  "body": """Hello,

Most people learn that their metabolic health has been drifting at a routine blood test, years after the drift started.

The Abbott Lingo continuous glucose monitor included with the course changes what you are working from. Instead of a population average you get fourteen days of your own readings, and lessons 5 onward are built to interpret them.

One unit per student, shipped to United States addresses before lesson 5. Students must be 18 or older. It is not for insulin users and it is not for medical diagnosis.

$1,249 upfront or five payments of $289.

https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
 {"stage": "Day 9",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "Eight to fifteen people. That is the whole list.",
  "pre": "Why cohort size is the constraint and not a marketing device.",
  "body": """Hello,

The class caps at fifteen because a teacher cannot hold more than fifteen sets of biomarkers in their head at once.

That cap is also why enrollment closes. When the fifteenth seat goes, the cohort is full and the next one starts later.

Eighteen weeks, eighteen live 50 minute sessions, six pillars, a written personal protocol at the end, and the Abbott Lingo continuous glucose monitor before lesson 5.

$1,249 upfront, down from $1,800. Or five payments of $289, cancellable at any time with no setup fee.

https://longevitylifeacademy.com/pricing.html

Admissions, Longevity Life Academy by eTeacher Group"""},
 {"stage": "Day 14, final",
  "frm": "Longevity Life Academy <admissions@longevitylifeacademy.com>",
  "subj": "Two options and one reply",
  "pre": "Enroll now, hold for the next cohort, or tell us to stop.",
  "body": """Hello,

This is the last note in this sequence, so it is three lines.

Enroll now at $1,249 upfront or five payments of $289: https://longevitylifeacademy.com/pricing.html

Hold me for the next cohort at the same price: reply with the word LATER.

Stop writing to me: reply with the word STOP and you will hear nothing further.

Admissions, Longevity Life Academy by eTeacher Group"""},
]

EMAIL_RULES = [
 ("4.6 / 5", "Trustpilot rating carried in every send", "More than 600 verified reviews for eTeacher Group"),
 ("45 min", "target reply time in the growth engine spec", "Recorded in the LLA growth engine hub"),
 ("10", "maximum touches per person across all channels", "Three abandonment stages plus the drip"),
 ("P0", "deliverability item still open", "ActiveCampaign SPF authorisation and a Google Postmaster reputation recorded as bad"),
]

# ================================================================ TAB 6 FORECAST
FORECAST_SCENARIOS = [
 ("$5,000", "6.8", "$739", "$8,447", "1.69x", "Pilot. Enough to prove creative and page, not enough to prove scale."),
 ("$10,000", "13.5", "$739", "$16,895", "1.69x", "First month where cohort fill becomes visible against a 15 seat cap."),
 ("$25,000", "33.8", "$739", "$42,237", "1.69x", "Roughly two full cohorts a month at the base case."),
 ("$50,000", "67.6", "$739", "$84,473", "1.69x", "The recommended ceiling, and the only tier where InitiateCheckout clears 50 a week."),
]

CASHFLOW = [
 ("$5,000", "6.8", "$1,965", "0.39x", "$9,773", "1.95x"),
 ("$10,000", "13.5", "$3,909", "0.39x", "$19,546", "1.95x"),
 ("$25,000", "33.8", "$9,773", "0.39x", "$48,865", "1.95x"),
 ("$50,000", "67.6", "$19,546", "0.39x", "$97,729", "1.95x"),
]

TEST_PLAN = [
 ("Days 1 to 3", "Fix the checkout before a dollar is spent",
  "Publish a real checkout URL, fire Purchase with value 1249 or 289, correct the homepage FAQ to $1,249 and $289, and amend the Terms so admissions review is not a condition precedent to payment.",
  "A live checkout URL that returns 200 and a Purchase event visible in Events Manager."),
 ("Days 1 to 3", "Wire the Conversions API",
  "From April 2026 the conversion leads performance goal is unavailable to new campaigns without a Conversions API integration, so this is a launch blocker rather than an optimisation.",
  "Conversions API connected to the CRM with event match quality above 6."),
 ("Days 4 to 14", "Phase 0 at $400 per day, one campaign",
  "Three ad sets maximum, optimising Qualified Lead, running the Courtney c_b3 set and the chosen b3 set against United States and Canada 45 to 65 plus.",
  "58 to 88 qualified leads a week, cost per lead under $52.98, no ad set fragmented below 50 results."),
 ("Days 4 to 14", "Remove the phone from the required path",
  "Branded SMS inside 60 seconds of form submit, voicemail second, live call third, because a documented seniors test answered 1 call in 12.",
  "Contact rate above 25 percent measured on first touch rather than call answer."),
 ("Days 15 to 30", "Consolidate and raise budget in steps under 20 percent",
  "One campaign and one broad ad set with seven day click and one day view attribution and value based optimisation carrying the real ticket value.",
  "Cost per InitiateCheckout under $208 and a base case ROAS at or above 1.69x."),
 ("Days 15 to 30", "Open the influencer and lead vendor tracks in parallel",
  "Max Lugavere and Eric Topol first on influencers, Aragon and Astoria first on pay per call, with a 50 to 100 lead minimum before judging any source.",
  "Two signed influencer flights and one pay per call source live at a 60 second billable duration threshold."),
]

BLOCKERS_CEO = [
 ("Critical", "No checkout exists",
  "Both pricing CTAs point at #lead-gen, and /enroll.html, /checkout.html and /apply.html all return 404.",
  "Everything downstream of this, including every number on the forecast tab, is blocked until it is fixed.",
  [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
 ("Critical", "Two prices are live at the same time",
  "The homepage FAQ still says tuition from $360 a month with full pricing of $1,399 while the pricing page says $289 a month and $1,249 upfront.",
  "Meta ad review and the value model both key off the on page price, and a mismatch is a rejection risk.",
  [("homepage FAQ", "https://longevitylifeacademy.com/#faq"), ("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
 ("Critical", "The Terms block self serve payment",
  "Terms of Service place an admissions review and an enrollment agreement before payment.",
  "A Sales campaign needs a checkout URL, a Purchase event with a value parameter, and published refund terms before purchase.",
  [("terms.html", "https://www.longevitylifeacademy.com/terms.html")]),
 ("High", "The instalment plan opens a day one cash hole",
  "A $739 acquisition cost against a $289 first payment is negative $450 on day one, recovered in month two only if the instalment does not default.",
  "Keep the Most Chosen badge on the upfront plan and keep the $196 saving as the headline line of copy.",
  [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
 ("High", "Email deliverability is degraded",
  "ActiveCampaign SPF authorisation was logged as a P0 item and the Google Postmaster score was recorded as bad.",
  "Recovery comes from authenticated disciplined sending over weeks, so the recovery sequence cannot carry the quarter on its own.",
  [("LLA growth engine hub", "https://gitteromri-ux.github.io/lla-growth-engine/")]),
 ("Medium", "Session length conflicts between the site and internal checkout",
  "The public site states weekly 50 minute sessions while the internal checkout note states 90 minute Monday sessions.",
  "Resolve before either number appears in a paid ad, because the on page claim is what ad review reads.",
  [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
 ("Medium", "No published refund calculation",
  "Cancel anytime appears on the pricing page with no refund calculation and no money back guarantee anywhere on the fetched site.",
  "A 45 plus buyer paying $1,249 online will look for this before paying, and its absence costs conversion rate.",
  [("terms.html", "https://www.longevitylifeacademy.com/terms.html")]),
 ("Medium", "Realized acquisition performance was never recorded",
  "The project record gives campaign volume, four press placements, 232 creatives and 3,500 leads, but no actual cost per acquisition, revenue or return on ad spend.",
  "Every forecast on this page is modelled from vertical benchmarks, so treat the first 30 days as the measurement that replaces them.",
  [("LLA growth engine hub", "https://gitteromri-ux.github.io/lla-growth-engine/")]),
]

FORECAST_CHIPS = [
 ("67.6", "purchases a month at $50k, base case", "Model output at a 0.20 percent landing page view to purchase rate"),
 ("$739", "cost per acquisition, base case", "Inside the independently derived $647 to $1,067 band"),
 ("1.69x", "return on ad spend, base case", "Between Health and Wellness at 1.50 and all industry at 1.93"),
 ("$1,249", "order value the model assumes", "Upfront plan, before any instalment mix"),
]
