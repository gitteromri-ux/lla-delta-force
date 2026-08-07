# -*- coding: utf-8 -*-
# Data for E-COMMERCE DELTA FORCE GO LIVE. No em dashes, no en dashes, no exclamation marks.

RAW = "https://raw.githubusercontent.com/gitteromri-ux"

PRICING = "https://longevitylifeacademy.com/pricing.html"

def img(repo, path):
    return f"{RAW}/{repo}/{path}"

# ---------------------------------------------------------------- TAB 1
CAMPAIGNS = [
{
 "code": "C1",
 "phase": "PHASE 0 . DAYS 1 TO 14",
 "name": "LLA Warmup Prospecting",
 "objective": "Leads objective, website form on a real landing page, performance goal set to Maximise number of conversion leads",
 "event": "Qualified Lead",
 "budget": "$260 / day",
 "budget_note": "Part of the $400 per day Phase 0 envelope",
 "audience": "United States and Canada. Age 45 to 65 plus. Advantage+ audience OFF so the demographic floor holds. Interest stack: longevity, Peter Attia, Bryan Johnson, continuous glucose monitor, Zone 2 training, biohacking, menopause health. Gender all, expect a 54.5 percent female skew to emerge on its own.",
 "placements": "Manual placements. Facebook Feed, Instagram Feed, Instagram Stories, Facebook Reels, Instagram Reels, Instagram Explore. Audience Network excluded.",
 "structure": "One campaign, one ad set. Do not fragment. The 50 results per week rule is measured per ad set.",
 "creative_set": "Courtney c_b3, Decode Your Biomarkers",
 "creative_repo": "https://github.com/gitteromri-ux/courtney-banners",
 "imgs": [
   {"u": img("courtney-banners", "main/banners/c_b3_191x1.png"), "r": "1.91 / 1", "label": "1.91:1 link ad", "note": "1200 x 628 . Facebook link placement"},
   {"u": img("courtney-banners", "main/banners/c_b3_1x1.png"), "r": "1 / 1", "label": "1:1 feed", "note": "1080 x 1080 . Instagram post and Facebook feed"},
   {"u": img("courtney-banners", "main/banners/c_b3_4x5.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "1080 x 1350 . Instagram and Facebook feed"},
   {"u": img("courtney-banners", "main/banners/c_b3_9x16.png"), "r": "9 / 16", "label": "9:16 story", "note": "1080 x 1920 . Stories and Reels"},
 ],
 "primary": "Most people find out their metabolic health is drifting at a routine blood test, years after the drift began.\n\nThe Longevity Blueprint is an 18 week live online course. Eighteen live 50 minute sessions, a class of 8 to 15 adults, and six pillars covering nutrition, sleep, exercise and movement, supplements and wearables, stress management, and your own written longevity protocol.\n\nAn Abbott Lingo continuous glucose monitor is included and ships before lesson 5, so you read your own numbers rather than a population average.\n\nTaught by practicing faculty including Julie Gibson Clark, ranked second in the world on the Rejuvenation Olympics leaderboard with a DunedinPACE score of 0.665.\n\n$1,249 paid upfront, reduced from $1,800. Or five payments of $289.",
 "headline": "Decode Your Biomarkers. Extend Your Life.",
 "description": "18 weeks live. Class of 8 to 15. Abbott Lingo CGM included.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "Education and Instruction lead cost sits at a $28.22 median, and LLA is already buying leads under that number, so the lead machine is not the failure point.",
 "why_src": [("WordStream Facebook Ads Benchmarks", "https://www.wordstream.com/blog/facebook-ads-cost")],
},
{
 "code": "C2",
 "phase": "PHASE 0 . DAYS 1 TO 14",
 "name": "LLA Warmup Retargeting",
 "objective": "Leads objective, website form, Maximise number of conversion leads",
 "event": "Qualified Lead",
 "budget": "$80 / day",
 "budget_note": "Part of the $400 per day Phase 0 envelope",
 "audience": "Site visitors 30 days, video 50 percent plus viewers, Instagram and Facebook engagers 365 days, lead form openers. Purchasers excluded. Frequency capped near 6 per week.",
 "placements": "Manual placements, same six surfaces as C1. Audience Network excluded.",
 "structure": "One consolidated retargeting ad set. Advantage+ already reallocates 35 to 45 percent of budget to retargeting internally, so run one or the other, never both.",
 "creative_set": "Chosen set b3, Meta banners gallery",
 "creative_repo": "https://github.com/gitteromri-ux/lla-meta-banners-gallery",
 "imgs": [
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b3_191x1.png"), "r": "1.91 / 1", "label": "1.91:1 link ad", "note": "Facebook link placement"},
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b3_1x1.png"), "r": "1 / 1", "label": "1:1 feed", "note": "Instagram post and Facebook feed"},
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b3_4x5.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "Instagram and Facebook feed"},
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b3_9x16.png"), "r": "9 / 16", "label": "9:16 story", "note": "Stories and Reels"},
 ],
 "primary": "You looked at the price and you stopped. That is the right instinct at $1,249, so here is the arithmetic in full.\n\nEighteen live 50 minute sessions. A class of 8 to 15 adults, not a recorded library. Six pillars. A written personal longevity protocol you leave with. An Abbott Lingo continuous glucose monitor shipped before lesson 5 with 14 days of app access.\n\nUpfront is $1,249, down from $1,800, a saving of $551. The five payment plan is $289 a month and totals $1,445, so paying upfront saves a further $196.\n\n4.6 out of 5 on Trustpilot across more than 600 verified reviews for eTeacher Group.",
 "headline": "$1,249 upfront. Or five payments of $289.",
 "description": "Save $551 against the $1,800 list price. Save $196 against the plan.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "Retargeting median return on ad spend is 3.61 against 2.11 for prospecting, which is 41.6 percent lower cost per acquisition at constant order value.",
 "why_src": [("Rule1 ROAS benchmarks", "https://rule1.ai/articles/roas-benchmarks")],
},
{
 "code": "C3",
 "phase": "PHASE 0 . DAYS 1 TO 14",
 "name": "LLA CRM Reactivation",
 "objective": "Leads objective against an uploaded customer list. The cheapest inventory LLA already owns.",
 "event": "Qualified Lead",
 "budget": "$60 / day",
 "budget_note": "Part of the $400 per day Phase 0 envelope",
 "audience": "Customer list upload of the 3,500 lead database recorded in the turnaround plan, plus lead form openers 180 days. Purchasers excluded.",
 "placements": "Manual placements. Facebook Feed, Instagram Feed, Instagram Stories.",
 "structure": "One ad set. This audience is small, so expect frequency to climb fast and rotate creative weekly.",
 "creative_set": "Julie on set banners b1",
 "creative_repo": "https://github.com/gitteromri-ux/julie-onset-banners",
 "imgs": [
   {"u": img("julie-onset-banners", "main/png/julie_b1_191x1.png"), "r": "1.91 / 1", "label": "1.91:1 link ad", "note": "Facebook link placement"},
   {"u": img("julie-onset-banners", "main/png/julie_b1_1x1.png"), "r": "1 / 1", "label": "1:1 feed", "note": "Instagram post and Facebook feed"},
   {"u": img("julie-onset-banners", "main/png/julie_b1_4x5.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "Instagram and Facebook feed"},
   {"u": img("julie-onset-banners", "main/png/julie_b1_9x16.png"), "r": "9 / 16", "label": "9:16 story", "note": "Stories and Reels"},
 ],
 "primary": "You asked us about The Longevity Blueprint once and the conversation stopped there. The next cohort has room.\n\nJulie Gibson Clark is ranked second in the world on the Rejuvenation Olympics leaderboard. Her DunedinPACE score is 0.665, which reads as roughly eight months of biological aging per calendar year. She teaches on this course.\n\nEighteen weeks. Eighteen live 50 minute sessions. A class of 8 to 15 adults. An Abbott Lingo continuous glucose monitor before lesson 5.\n\n$1,249 upfront or five payments of $289.",
 "headline": "The second slowest ager on Earth teaches this class.",
 "description": "DunedinPACE 0.665. Eighteen weeks live. Cohorts of 8 to 15.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "The turnaround plan records a 3,500 lead database awaiting reactivation, and those leads were already paid for at roughly $20 each.",
 "why_src": [("LLA intel file, section 5", "https://github.com/gitteromri-ux/lla-turnaround-plan")],
},
{
 "code": "C4",
 "phase": "PHASE 2 . WEEK 9 ONWARD",
 "name": "LLA Advantage Plus Sales Prospecting",
 "objective": "Sales objective, Advantage+ shopping campaign, Advantage+ audience with age minimum 25 and audience suggestion 45 to 65 plus, Advantage+ placements, Advantage+ campaign budget",
 "event": "InitiateCheckout. Never Purchase at this spend level.",
 "budget": "$905 / day",
 "budget_note": "55 percent of the $1,645 per day recommended envelope",
 "audience": "Advantage+ audience with suggestions loaded from the interest stack. Existing customers excluded. Advantage+ campaign budget does not reset the learning phase when edited.",
 "placements": "Advantage+ placements, all surfaces, Audience Network included at this stage because Advantage+ manages allocation.",
 "structure": "One campaign, one ad set. Around 4.1 net new creatives per week added in weekly batches after the ad set has exited learning.",
 "creative_set": "Julie Meta banners, Decode Your Biomarkers",
 "creative_repo": "https://github.com/gitteromri-ux/julie-meta-banners",
 "imgs": [
   {"u": img("julie-meta-banners", "main/out/decode_your_biomarkers/decode_your_biomarkers__link_feed_landscape_1200x628.png"), "r": "1.91 / 1", "label": "1.91:1 link ad", "note": "1200 x 628"},
   {"u": img("julie-meta-banners", "main/out/decode_your_biomarkers/decode_your_biomarkers__feed_square_1080x1080.png"), "r": "1 / 1", "label": "1:1 feed", "note": "1080 x 1080"},
   {"u": img("julie-meta-banners", "main/out/decode_your_biomarkers/decode_your_biomarkers__feed_portrait_1080x1350.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "1080 x 1350"},
   {"u": img("julie-meta-banners", "main/out/decode_your_biomarkers/decode_your_biomarkers__stories_reels_1080x1920.png"), "r": "9 / 16", "label": "9:16 story", "note": "1080 x 1920"},
 ],
 "primary": "I am 54 and I had no idea what my glucose did after lunch until a sensor on my arm told me.\n\nThat is the whole idea behind The Longevity Blueprint. Eighteen weeks, eighteen live 50 minute sessions, a class of 8 to 15 adults, and six pillars: nutrition, sleep, exercise and movement, supplements and wearables, stress management, and your own longevity protocol.\n\nAn Abbott Lingo continuous glucose monitor is included and ships before lesson 5 with 14 days of app access. One unit per student, shipped to United States addresses, students must be 18 or older, not for insulin users, not for medical diagnosis.\n\nThe sessions are live, not recorded, and recordings are there when you miss one.\n\n$1,249 upfront, reduced from $1,800. Five payments of $289 also available.",
 "headline": "Read your own numbers. Not a population average.",
 "description": "Abbott Lingo CGM included before lesson 5. Eighteen live sessions.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "Advantage+ is the setting Meta describes as its most efficient path to online sales, with a stated 9 percent average improvement in cost per conversion.",
 "why_src": [("Meta Business Help Center", "https://www.facebook.com/business/help/1362234537597370?locale=en_GB")],
},
{
 "code": "C5",
 "phase": "PHASE 2 . WEEK 9 ONWARD",
 "name": "LLA Manual Sales, Hard 45 Plus",
 "objective": "Sales objective, Advantage+ audience OFF, manual placements. The control cell against C4 and the only way to enforce a hard demographic floor.",
 "event": "InitiateCheckout",
 "budget": "$329 / day",
 "budget_note": "20 percent of the $1,645 per day envelope",
 "audience": "United States and Canada, hard age 45 to 65 plus, interest stack: longevity, Peter Attia, Bryan Johnson, continuous glucose monitor, Zone 2 training, biohacking. No lookalike stacks, because lookalike return on ad spend of 1.80 sits below broad prospecting at 2.11.",
 "placements": "Manual placements. Facebook Feed, Instagram Feed, Instagram Stories, Facebook Reels, Instagram Reels, Instagram Explore. Audience Network excluded.",
 "structure": "One ad set. Run a Breakdown by Age report weekly and compare cost per purchase, not cost per lead, across bands.",
 "creative_set": "Courtney c_b4, The Longevity Course Taught Live",
 "creative_repo": "https://github.com/gitteromri-ux/lla-courtney-final",
 "imgs": [
   {"u": img("lla-courtney-final", "main/banners/c_b4_191x1.png"), "r": "1.91 / 1", "label": "1.91:1 link ad", "note": "Facebook link placement"},
   {"u": img("lla-courtney-final", "main/banners/c_b4_1x1.png"), "r": "1 / 1", "label": "1:1 feed", "note": "Instagram post and Facebook feed"},
   {"u": img("lla-courtney-final", "main/banners/c_b4_4x5.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "Instagram and Facebook feed"},
   {"u": img("lla-courtney-final", "main/banners/c_b4_9x16.png"), "r": "9 / 16", "label": "9:16 story", "note": "Stories and Reels"},
 ],
 "primary": "A recorded course is a library. This is a classroom.\n\nThe Longevity Blueprint runs 18 weeks with 18 live 50 minute sessions, taught to a class of 8 to 15 adults, so the faculty knows your name and your numbers.\n\nFour phases. Six pillars: nutrition, sleep, exercise and movement, supplements and wearables, stress management, and your own longevity protocol. Weekly assignments, a class forum, recordings when you miss a session, and a written personal protocol at the end.\n\nAn Abbott Lingo continuous glucose monitor is included and ships before lesson 5.\n\n$1,249 upfront, down from $1,800. Or five payments of $289, totalling $1,445.",
 "headline": "The longevity course, taught live.",
 "description": "Eighteen live sessions. A class of 8 to 15. Not a recorded library.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "The maximum age entered in an Advantage+ audience is a suggestion the delivery system can ignore, so the hard floor has to live in a manual ad set.",
 "why_src": [("Jon Loomer on age restriction", "https://www.jonloomer.com/qvt/restrict-ad-targeting-by-age/")],
},
{
 "code": "C6",
 "phase": "PHASE 2 . WEEK 9 ONWARD",
 "name": "LLA Retargeting Sales",
 "objective": "Sales objective, manual audience, one consolidated ad set",
 "event": "InitiateCheckout",
 "budget": "$296 / day",
 "budget_note": "18 percent of the $1,645 per day envelope",
 "audience": "Four windows in one ad set. Zero to 3 days: InitiateCheckout with no purchase. Zero to 14 days: pricing page viewers with no InitiateCheckout. Zero to 30 days: any site visitor plus video 50 percent plus viewers plus social engagers. Zero to 180 days: CRM lead list. Purchasers excluded on every window.",
 "placements": "Manual placements, six surfaces. Audience Network excluded. Frequency capped near 6 per week.",
 "structure": "One consolidated ad set. Do not split by window, because the 50 results per week rule is measured per ad set.",
 "creative_set": "Julie motion, animated 6 second cuts",
 "creative_repo": "https://github.com/gitteromri-ux/lla-julie-animations",
 "imgs": [
   {"u": img("lla-julie-animations", "main/media/V2_LLA_JULIE_A_PACE_6S.gif"), "r": "1 / 1", "label": "Motion, pace cut", "note": "6 second animated loop"},
   {"u": img("lla-julie-animations", "main/media/V2_LLA_JULIE_B_CURVE_6S.gif"), "r": "1 / 1", "label": "Motion, curve cut", "note": "6 second animated loop"},
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b5_4x5.png"), "r": "4 / 5", "label": "4:5 vertical", "note": "Static companion"},
   {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b5_9x16.png"), "r": "9 / 16", "label": "9:16 story", "note": "Static companion"},
 ],
 "primary": "You were on the pricing page. Here is the part that decides it.\n\n$1,249 upfront saves $551 against the $1,800 list price, and $196 against the five payment plan at $289 a month.\n\nEighteen weeks. Eighteen live 50 minute sessions. Eight to fifteen students in the room. Abbott Lingo continuous glucose monitor included before lesson 5, with 14 days of app access.\n\nJulie Gibson Clark, second in the world on the Rejuvenation Olympics leaderboard, teaches on this faculty.\n\nThe five payment plan can be cancelled at any time and there is no setup fee.",
 "headline": "Save $551 upfront. Or pay $289 a month.",
 "description": "Cancel anytime on the plan. No setup fee.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "Reported retargeting return is largely re-attributed rather than incremental, with true lift typically 20 to 40 percent of the reported figure, so hold this campaign at 18 percent of budget.",
 "why_src": [("AdAmigo Meta benchmarks 2026", "https://www.adamigo.ai/blog/meta-ads-benchmarks-2026-funnel-prospecting-retargeting-retention")],
},
{
 "code": "C7",
 "phase": "PHASE 2 . WEEK 9 ONWARD",
 "name": "LLA Leads Rebuilt, Press Authority",
 "objective": "Leads objective, website form on the advertorial landing page, Maximise number of conversion leads, Conversions API connected to the CRM",
 "event": "Qualified Lead",
 "budget": "$115 / day",
 "budget_note": "7 percent of the $1,645 per day envelope",
 "audience": "United States and Canada, 45 to 65 plus, broad with press and health news interests layered. Application style qualifying questions on the form.",
 "placements": "Manual placements. Facebook Feed, Instagram Feed, Facebook Reels, Instagram Reels.",
 "structure": "One ad set. From April 2026 the conversion leads performance goal is not available for new campaigns without a Conversions API integration, so wire that before launch.",
 "creative_set": "PR article ads, four national placements",
 "creative_repo": "https://github.com/gitteromri-ux/lla-pr-article-ads",
 "imgs": [
   {"u": img("lla-pr-article-ads", "main/ads/lla-usatoday-landscape-link-1200x628.png"), "r": "1.91 / 1", "label": "USA TODAY, 1.91:1", "note": "1200 x 628"},
   {"u": img("lla-pr-article-ads", "main/ads/lla-yahoo-finance-feed-square-1080x1080.png"), "r": "1 / 1", "label": "Yahoo Finance, 1:1", "note": "1080 x 1080"},
   {"u": img("lla-pr-article-ads", "main/ads/lla-ein-presswire-feed-portrait-1080x1350.png"), "r": "4 / 5", "label": "EIN Presswire, 4:5", "note": "1080 x 1350"},
   {"u": img("lla-pr-article-ads", "main/ads/lla-newsbreak-story-reel-1080x1920.png"), "r": "9 / 16", "label": "NewsBreak, 9:16", "note": "1080 x 1920"},
 ],
 "primary": "Julie Gibson Clark was a structural engineer turned recruiter. She is now ranked second in the world on the Rejuvenation Olympics leaderboard, with a DunedinPACE score of 0.665 measured on a TruDiagnostic epigenetic test.\n\nShe teaches on The Longevity Blueprint, an 18 week live online course from Longevity Life Academy by eTeacher Group.\n\nEighteen live 50 minute sessions. Classes of 8 to 15 adults. Six pillars. An Abbott Lingo continuous glucose monitor included before lesson 5.\n\neTeacher Group has taught more than 400,000 students across 197 countries in 25 years of online education, rated 4.6 out of 5 on Trustpilot across more than 600 verified reviews.\n\n$1,249 upfront, reduced from $1,800, or five payments of $289.",
 "headline": "Second slowest ager on Earth. Now teaching.",
 "description": "Covered by USA TODAY, Yahoo Finance, EIN Presswire and NewsBreak.",
 "dest": "https://longevitylifeacademy.com/pricing.html",
 "why": "Meta measured a 9.5 percent lower cost per quality lead on website forms once the Conversions API and the conversion leads goal are connected.",
 "why_src": [("Meta on conversion leads", "https://www.facebook.com/business/help/782657799338685?locale=en_GB")],
},
]

CREATIVE_BANK = [
  {"u": img("courtney-banners", "main/banners/c_b1_1x1.png"), "t": "Live Longer. Learn How."},
  {"u": img("courtney-banners", "main/banners/c_b2_1x1.png"), "t": "Your Longevity Protocol. Made Personal."},
  {"u": img("courtney-banners", "main/banners/c_b5_1x1.png"), "t": "Age Slower. Starts in Class."},
  {"u": img("courtney-banners", "main/banners/c_b6_1x1.png"), "t": "Enroll. Live Longer. Live Stronger."},
  {"u": img("julie-meta-banners", "main/out/banner_a_slow_your_pace/banner_a_slow_your_pace__feed_square_1080x1080.png"), "t": "Slow Your Pace"},
  {"u": img("julie-meta-banners", "main/out/banner_b_2nd_slowest_ager/banner_b_2nd_slowest_ager__feed_square_1080x1080.png"), "t": "2nd Slowest Ager"},
  {"u": img("lla-meta-banners-gallery", "main/banners/chosen/chosen_b1_1x1.png"), "t": "Chosen set, hook 01"},
  {"u": img("lla-employee-referral", "main/banners/banner-1.png"), "t": "Employee referral, internal only"},
]

BLOCKERS = [
 ("Pricing page buttons do not reach a checkout",
  "Both pricing CTAs, Start Monthly and Enroll Upfront, resolve to the homepage anchor #lead-gen. No Stripe, Paddle, PayPal or any payment processor reference appears in the page source.",
  [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html")]),
 ("Three checkout paths return HTTP 404",
  "/enroll.html, /checkout.html and /apply.html were each requested directly and each returned 404. There is no checkout URL anywhere on the domain to point a Sales campaign at.",
  [("longevitylifeacademy.com", "https://longevitylifeacademy.com/")]),
 ("Two prices are live at the same time",
  "The homepage FAQ item 06 still states tuition from $360 per month with full pricing of $1,399. The pricing page, the sitewide tray and the About page state $289 per month and $1,249 upfront. Meta ad review and the value model both key off the on-page price.",
  [("pricing.html", "https://www.longevitylifeacademy.com/pricing.html"), ("homepage FAQ", "https://longevitylifeacademy.com/#faq")]),
 ("The Terms legally block a self serve checkout",
  "Terms of Service state that enrollment is subject to admissions review and that tuition, payment schedules and refund eligibility are described in an enrollment agreement provided by the admissions team before payment. A purchase optimised campaign needs a real checkout URL, a Purchase event with a value parameter, and refund terms published on site before purchase.",
  [("terms.html", "https://www.longevitylifeacademy.com/terms.html")]),
]

# ---------------------------------------------------------------- TAB 2
FUNNEL_ROWS = [
 ("$10,000", "Conservative", "357,143", "4,286", "$2.33", "2,357", "17.0", "$589", "2.8", "$3,535", "$3,533", "0.35x", False),
 ("$10,000", "Base", "483,092", "9,662", "$1.03", "6,763", "67.6", "$148", "13.5", "$739", "$16,895", "1.69x", True),
 ("$10,000", "Optimistic", "625,000", "16,875", "$0.59", "13,500", "162.0", "$62", "40.5", "$247", "$50,584", "5.06x", False),
 ("$25,000", "Conservative", "892,857", "10,714", "$2.33", "5,893", "42.4", "$589", "7.1", "$3,535", "$8,832", "0.35x", False),
 ("$25,000", "Base", "1,207,729", "24,155", "$1.03", "16,908", "169.1", "$148", "33.8", "$739", "$42,237", "1.69x", True),
 ("$25,000", "Optimistic", "1,562,500", "42,188", "$0.59", "33,750", "405.0", "$62", "101.2", "$247", "$126,461", "5.06x", False),
 ("$50,000", "Conservative", "1,785,714", "21,429", "$2.33", "11,786", "84.9", "$589", "14.1", "$3,535", "$17,664", "0.35x", False),
 ("$50,000", "Base", "2,415,459", "48,309", "$1.03", "33,816", "338.2", "$148", "67.6", "$739", "$84,473", "1.69x", True),
 ("$50,000", "Optimistic", "3,125,000", "84,375", "$0.59", "67,500", "810.0", "$62", "202.5", "$247", "$252,922", "5.06x", False),
]

LEARNING_ROWS = [
 ("Optimistic", "$647", "$32,350", "$4,621 / day", "$140,500 / mo"),
 ("Base", "$833", "$41,650", "$5,950 / day", "$180,900 / mo"),
 ("Conservative", "$1,067", "$53,350", "$7,621 / day", "$231,700 / mo"),
]

EVENT_ROWS = [
 ("Purchase, $1,249 ticket", "$833", "No", "No", "No"),
 ("InitiateCheckout", "$139 to $208", "No", "No", "Yes at a 6 to 1 ratio"),
 ("Qualified website Lead", "$28.22 to $52.98", "Yes", "Yes", "Yes"),
 ("Current instant form lead", "about $20", "Yes", "Yes", "Yes"),
]

# ---------------------------------------------------------------- TAB 3
VENDORS = [
{
 "rank": "01",
 "name": "Aragon Advertising",
 "kind": "Pay per call marketplace",
 "price": "Medicare about $20 per call at about 20 percent close. Final expense about $15 at about 15 percent. Roofing about $60 at about 25 percent. Pest control about $30 at about 25 percent. No longevity rate card is published, so plan $40 to $80 per call.",
 "price_src": ("Aragon pay per call guide", "https://blog.aragon-advertising.com/posts/pay-per-call-marketing-guide/"),
 "launch": "Live in days, not months. Payment on CPA, CPL, CPI or revenue share, not retainers.",
 "launch_src": ("go.aragonco.com", "https://go.aragonco.com/"),
 "contact_name": "Nick Davies, Associate Director, Affiliate Management",
 "contact_url": "https://www.linkedin.com/in/nickdavies100",
 "contact_extra": [("advertisers@aragon-advertising.com", "mailto:advertisers@aragon-advertising.com"), ("Advertiser signup", "https://aragon-advertising.com/join/"), ("Todd Stearn, CEO", "https://www.linkedin.com/in/toddjaredstearn")],
 "risk": "Thirteen reviews on Affpaying with two rated Terrible, including an unpaid publisher. That is publisher side risk, not buyer side, but demand call recordings and a 90 second minimum billable duration. Canada coverage is not stated anywhere on the site.",
 "risk_src": ("Affpaying", "https://www.affpaying.com/aragon-advertising"),
 "tcpa": "The only vendor with a correct and current post September 2025 position, stating the one to one consent rule was vacated in early 2025 and formally eliminated by the FCC in September 2025.",
 "subject": "Longevity course, inbound calls, US and Canada, 45 plus, ready to test this week",
 "email": """Nick,

I run acquisition for Longevity Life Academy, part of eTeacher Group. We sell The Longevity Blueprint, an 18 week live online longevity course at $1,249 upfront or five payments of $289. Buyer is United States and Canada, 45 plus, slightly female weighted.

We already buy Meta lead forms at roughly $20 per lead and almost nobody answers the phone. So I am not looking for more form fills. I want consumer initiated inbound calls.

Three questions before we book time:

1. Do you have a health education or wellness vertical with live supply today, and if not, what is the nearest adjacent buyer you can point me at. Your published card shows Medicare at about $20 per call at roughly 20 percent close and roofing at about $60 at roughly 25 percent, so I am budgeting $40 to $80 for our audience.
2. Is Canada supply available. Your site does not state it either way.
3. Can you confirm exclusive routing, full call recordings, a 90 second minimum billable duration, and state and province level geo control, in writing before any spend.

Our first test is $1,000 to $2,000 over 30 days, roughly 25 to 50 calls, running against one other vendor in parallel. If the answer rate holds we scale inside the same month.

You state you are live in days, not months. I would like to hold you to that.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "02",
 "name": "Astoria Company",
 "kind": "Pay per call plus exclusive lead marketplace",
 "price": "Cost per lead $5 to $15 auto, $15 home improvement, $30 mortgage, above $100 legal. Pay per call insurance $15 to $30 per qualified call, which at a 20 percent close is a $75 to $150 acquisition cost. Minimum spend often $500 to $1,000 per month with a $200 to $500 thirty day test.",
 "price_src": ("Astoria buyer guide", "https://www.astoriacompany.com/how-lead-marketplaces-work-a-buyers-guide"),
 "launch": "Launch a campaign in less than 30 minutes with the team. Fastest published launch of any vendor in this set.",
 "launch_src": ("Astoria pay per call", "https://www.astoriacompany.com/pay-per-call"),
 "contact_name": "Liza Schubert, Network Director, Pay Per Call Division",
 "contact_url": "https://www.linkedin.com/in/liza-schubert-6597b624",
 "contact_extra": [("lschubert@astoriacompany.com", "mailto:lschubert@astoriacompany.com"), ("bizdev@astoriacompany.com", "mailto:bizdev@astoriacompany.com"), ("Adnan Nazir, VP Sales and Operations", "https://www.linkedin.com/in/adnan-nazir-astoria")],
 "risk": "The TCPA page is stale and still treats one to one consent as in force. A 2014 consumer complaint alleges data resale, and a 2022 unpaid affiliate review sits on the same page. Buy exclusive only, with TrustedForm and Jornaya audit trails, both of which Astoria already names as live partners.",
 "risk_src": ("Affpaying", "https://www.affpaying.com/astoria-company"),
 "tcpa": "Stale. Still describes the FCC one to one consent rule as in force, but commits to audit trails with timestamps, source URLs and consent records.",
 "subject": "Exclusive health education calls, US and Canada, 30 minute launch, test starts this week",
 "email": """Liza,

Longevity Life Academy, part of eTeacher Group, sells an 18 week live longevity course at $1,249 upfront or five payments of $289. Our buyer is 45 plus, United States and Canada, slightly female weighted.

Your offers page carries Healthcare and Nursing Education Bundle Click to Call, Education Advisor Pay Per Call, Rapid Weightloss, and Sylvan Tutoring Programs Canada. That combination of health, education and Canada in one network is why you are on my shortlist.

What I need confirmed:

1. Are those four offers still live. The page is dated 2014 and I would rather ask than assume.
2. Exclusive routing only. Your own buyer guide says exclusive is recommended for high ticket services, and at a $1,249 ticket shared leads are worthless to me.
3. TrustedForm and Jornaya audit trails on every record, with timestamps, source URLs and consent strings.
4. Your TCPA page still treats the one to one consent rule as in force. It was vacated in early 2025 and eliminated by the FCC in September 2025. Please confirm which posture your compliance team is actually operating under.

Commercially I want to run your published thirty day trial shape, $200 to $500 to start, scaling to the $1,000 per month standing minimum if answer rate holds. You state a campaign can launch in under 30 minutes. I have creative, tracking numbers and a script ready.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "03",
 "name": "Semcasting",
 "kind": "Identity and audience targeting, LLA owns the consent",
 "price": "Not published. No cost per thousand, no minimum, no rate card was found on any fetched page.",
 "price_src": ("Semcasting healthcare", "https://www.semcasting.com/healthcare-and-pharmaceuticals"),
 "launch": "From member list or HCP list to live campaign in 48 hours, with an 85 percent plus match rate described as 142 percent better than direct platform onboarding, and audience updates every 15 minutes.",
 "launch_src": ("Semcasting healthcare", "https://www.semcasting.com/healthcare-and-pharmaceuticals"),
 "contact_name": "No named contact could be verified. Both the contact page and the leadership page returned client errors.",
 "contact_url": "https://www.semcasting.com/healthcare-and-pharmaceuticals",
 "contact_extra": [("Healthcare page contact form", "https://www.semcasting.com/healthcare-and-pharmaceuticals")],
 "risk": "G2 rating of 4.6 out of 5 across only four reviews, with repeated criticism of unclear attribution, inadequate analytics and a steep learning curve. Cost is entirely unpublished.",
 "risk_src": ("G2", "https://www.g2.com/products/semcasting/reviews"),
 "tcpa": "No TCPA statement. Segments are built from de-identified opt in behavioural and demographic data with no protected health information, so the consent string stays with LLA.",
 "subject": "48 hour activation, in market health audience, US and Canada, longevity course",
 "email": """Hello,

I am writing to the healthcare managed services team. Your site does not publish a named contact, so please route this.

Longevity Life Academy, part of eTeacher Group, sells The Longevity Blueprint, an 18 week live online longevity course at $1,249 upfront or five payments of $289. Buyer is 45 plus across the United States and Canada, slightly female weighted, and the closest published audience analogue is peterattiamd.com, which reads 55 to 64 at 28.6 percent, 45 to 54 at 20.7 percent, 65 plus at 18.6 percent, and 54.5 percent female.

Two things put you on our shortlist and nothing else in the market matched both. You state 100 percent reach and scale with no onboarding to 250 million plus people and 18 million businesses across the United States and Canada, and you state activation from list to live campaign in 48 hours at an 85 percent plus match rate.

The commercial reason this matters to us: we buy lead forms today at roughly $20 each and almost nobody answers the phone. If the prospect instead fills our form and calls our number, the consent string names one party, us, and the answer rate problem changes shape entirely.

What I need to price this:

1. Cost per thousand for a custom in market health and wellness audience at 45 plus, United States and Canada.
2. Minimum spend and contract length.
3. Activation destinations. We run Meta, Google and connected TV.
4. What you need from us to hit the 48 hour clock.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "04",
 "name": "Alliant, formerly AnalyticsIQ",
 "kind": "Health and Wellness custom audiences",
 "price": "Not published. Price, minimum, launch time, Canada coverage and TCPA posture are all unstated, which is the largest evidence gap in the top five.",
 "price_src": ("Alliant audience guide", "https://alliantinsight.com/audience-guide/health-wellness/"),
 "launch": "Not stated on any fetched page.",
 "launch_src": ("Alliant audience guide", "https://alliantinsight.com/audience-guide/health-wellness/"),
 "contact_name": "Christine Lee, Head of Health Strategy and Partnerships",
 "contact_url": "https://www.linkedin.com/in/christineboley",
 "contact_extra": [("christineb@analyticsiq.com", "mailto:christineb@analyticsiq.com"), ("Alliant contact form", "https://alliantinsight.com/contact/")],
 "risk": "No independent third party review of the health audiences was locatable. Everything commercial is unpublished, so the first call has to carry all of the diligence.",
 "risk_src": ("Alliant audience guide", "https://alliantinsight.com/audience-guide/health-wellness/"),
 "tcpa": "Not stated on any page fetched.",
 "subject": "Custom creator affinity segment, longevity podcast followers, 45 plus, US and Canada",
 "email": """Christine,

Your health and wellness audience guide says you can build custom segments from influencer and content creator audiences, and it names live examples including followers of Sally McRae on Instagram and Jeff Cavaliere on YouTube. That single capability is the reason I am writing.

Longevity Life Academy, part of eTeacher Group, sells The Longevity Blueprint, an 18 week live online longevity course at $1,249 upfront or five payments of $289. Our buyer is 45 plus, United States and Canada, and the published demographic profile of the longevity audience we are chasing reads 55 to 64 at 28.6 percent, 45 to 54 at 20.7 percent, 65 plus at 18.6 percent, and 54.5 percent female.

I want one thing from this first exchange: a custom creator affinity segment modelled on longevity podcast and newsletter followers, weighted 45 plus, United States and Canada.

Please send me:

1. Cost per thousand for that custom segment.
2. Your minimum spend.
3. Build time from brief to activation.
4. Whether Canada is inside the addressable base or United States only.
5. Activation destinations, specifically Meta and Google.

We are launching paid in days rather than weeks, so a short answer beats a long deck.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "05",
 "name": "ClickDealer",
 "kind": "CPA network with a dedicated pay per call department",
 "price": "No advertiser price, minimum, launch time or TCPA posture is published anywhere. Buy only on a capped cost per acquisition, and only after Aragon and Astoria are running.",
 "price_src": ("clickdealer.com", "https://www.clickdealer.com/"),
 "launch": "Not stated.",
 "launch_src": ("clickdealer.com", "https://www.clickdealer.com/"),
 "contact_name": "Yana Ejim, Chief Sales and Partnerships Officer",
 "contact_url": "https://www.linkedin.com/in/yana-jane-ejim-449192a2",
 "contact_extra": [("affiliates@clickdealer.com", "mailto:affiliates@clickdealer.com"), ("Michael Balyuk, Senior BD Manager", "https://www.linkedin.com/in/michael-balyuk-34b4b6183"), ("Contact page", "https://www.clickdealer.com/contact-us")],
 "risk": "Rated 2.6 out of 5 on Sitejabber across twelve reviews with withheld payment and fraud clawback complaints. The entity changed hands out of the Digital Media Solutions Chapter 11, sold to iMonMedia for an $8 million base price plus working capital adjustments.",
 "risk_src": ("Sitejabber", "https://www.sitejabber.com/reviews/clickdealer.com"),
 "tcpa": "Not stated on any page fetched.",
 "subject": "Capped CPA test, health education offer, pay per call department",
 "email": """Yana,

Longevity Life Academy, part of eTeacher Group, sells an 18 week live online longevity course at $1,249 upfront or five payments of $289, to a 45 plus buyer in the United States and Canada.

Your homepage states two things that matter to me. Leading health and beauty brands trust ClickDealer to drive customer growth with exclusive offers, and you have a track record delivering qualified leads to national telehealth platforms. You also run a dedicated pay per call department, which is unusual for a CPA network.

I am going to be direct about how we would buy. Sitejabber carries 2.6 out of 5 across twelve reviews with withheld payment complaints, and the entity moved through the Digital Media Solutions Chapter 11 to iMonMedia. That does not rule you out, it just means we start on a capped cost per acquisition with weekly reconciliation rather than an open budget.

What I need:

1. Your live health or education supply, named, and whether it can carry a high ticket education offer.
2. A capped cost per acquisition proposal on a qualified inbound call, with a 90 second minimum billable duration and full call recordings.
3. Whether Canada supply exists.
4. Your current TCPA posture in writing, given the one to one consent rule was vacated in early 2025 and eliminated by the FCC in September 2025.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
]

BACKUPS = [
{
 "rank": "B1",
 "name": "Perform[cb]",
 "kind": "Performance marketplace, Outcome Engine",
 "price": "Nothing commercial is published. No price, no minimum, no launch time, no TCPA posture, no health or education client evidence.",
 "price_src": ("performcb.com", "https://www.performcb.com/"),
 "launch": "Not stated.",
 "launch_src": ("performcb.com", "https://www.performcb.com/"),
 "contact_name": "Mcclain Sherman, VP of Partner Development",
 "contact_url": "https://www.linkedin.com/in/mcclainsherman",
 "contact_extra": [("Jarett Lewis, BD Executive", "https://www.linkedin.com/in/jarettlewis"), ("Contact page", "https://www.performcb.com/contact/")],
 "risk": "The best review record in this set, 4.7 out of 5 on G2 across fifteen reviews. Held at backup purely because nothing commercial is published.",
 "risk_src": ("G2", "https://www.g2.com/products/perform-cb/reviews"),
 "tcpa": "Not stated.",
 "subject": "Outcome Engine, inbound calls for a high ticket health education offer",
 "email": """Mcclain,

Your site says the Outcome Engine buys customers, users, installs, leads, calls, sales, form fills and outcomes. Calls are the line I care about.

Longevity Life Academy, part of eTeacher Group, sells The Longevity Blueprint, an 18 week live online longevity course at $1,249 upfront or five payments of $289, to a 45 plus buyer in the United States and Canada. We buy Meta lead forms at roughly $20 today and the answer rate is close to zero, so form fills are not what I want from you.

Nothing commercial is published on your site, so this is a pricing request rather than a discovery call:

1. Cost per qualified inbound call in a health or education vertical, with a 90 second minimum billable duration.
2. Minimum monthly commitment.
3. Time from signature to live traffic.
4. Whether Canada supply exists.
5. Your TCPA posture post September 2025.

We are running two other vendors in parallel from week one, so a fast, specific answer moves you up the list.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "B2",
 "name": "Archer Education",
 "kind": "Education vertical, exclusive inquiry marketplace",
 "price": "Not published. The Campus Explorer Network is described as an exclusive third party marketplace sourcing inquiries at an efficient cost per lead, with no figure attached.",
 "price_src": ("Archer performance marketing", "https://www.archeredu.com/performance-marketing/"),
 "launch": "Not stated.",
 "launch_src": ("Archer performance marketing", "https://www.archeredu.com/performance-marketing/"),
 "contact_name": "Lydia Matlock, VP Partnership Development",
 "contact_url": "https://www.linkedin.com/in/lydia-matlock",
 "contact_extra": [("hello@archeredu.com", "mailto:hello@archeredu.com"), ("Erik Edmonds, VP Digital Marketing", "https://www.linkedin.com/in/erik-edmonds-a1344611"), ("Contact page", "https://www.archeredu.com/contact/")],
 "risk": "Customer side sentiment is poor on a thin, dated sample. Net promoter score of minus 100 with 100 percent detractors, product quality 2.5 out of 5, customer service 2 out of 5. Employee sentiment is strong at 4.4 out of 5 across 38 Glassdoor reviews. Their buyers are accredited institutions and the LLA course is not degree granting.",
 "risk_src": ("Comparably", "https://www.comparably.com/brands/archer-education"),
 "tcpa": "Not stated.",
 "subject": "Non degree continuing education inquiry supply, 45 plus adult learner",
 "email": """Lydia,

Archer states that the Campus Explorer Network is your exclusive third party marketplace and that your exclusive EDU audience sources inquiries at an efficient cost per lead. I want to test whether that supply can carry a non degree programme.

Longevity Life Academy, part of eTeacher Group, sells The Longevity Blueprint, an 18 week live online course at $1,249 upfront or five payments of $289. Eighteen live 50 minute sessions, classes of 8 to 15 adults. It is continuing education for adults aged 45 plus in the United States and Canada. It is not degree granting and it is not accredited, and I would rather say that in the first email than the third.

Three questions:

1. Can the Campus Explorer Network source inquiries for a non accredited continuing education programme, or is the inventory contractually restricted to accredited institutions.
2. Cost per exclusive inquiry, and your minimum monthly commitment.
3. Time from contract to first inquiry delivery.

If the answer to question one is no, please say so plainly and I will stop taking your time.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
{
 "rank": "B3",
 "name": "A4D, Ads4Dough",
 "kind": "Lead generation network with health lineage",
 "price": "Zero buyer side facts are published. No price, no minimum, no onboarding time, no TCPA posture, no named contact.",
 "price_src": ("AFFCaptain profile", "https://affcaptain.com/affiliate-network/a4d/"),
 "launch": "Not stated.",
 "launch_src": ("AFFCaptain profile", "https://affcaptain.com/affiliate-network/a4d/"),
 "contact_name": "No named contact published. Phone is the only direct route.",
 "contact_url": "https://www.a4d.com/contact",
 "contact_extra": [("(760) 888-0229", "tel:+17608880229"), ("Contact page", "https://www.a4d.com/contact")],
 "risk": "Publisher side reputation is strong at 4.9 across 89 reviews on Afffind, but the Trustpilot score of 3.7 rests on a single 2020 review, and no buyer side commercial fact exists anywhere.",
 "risk_src": ("Afffind", "https://www.afffind.com/network/a4d"),
 "tcpa": "Not stated.",
 "subject": "Buyer side enquiry, health lead supply, 45 plus US and Canada",
 "email": """Hello,

Your network has been running white hat lead generation since 2008 across more than 20,000 publishers, with verticals listed as ecommerce, home services, insurance, lead generation and nutra. Everything published about A4D is written for publishers. I am writing as a buyer.

Longevity Life Academy, part of eTeacher Group, sells The Longevity Blueprint, an 18 week live online longevity course at $1,249 upfront or five payments of $289, to a 45 plus buyer in the United States and Canada.

Because no buyer side information is published, please treat this as a straight request for five numbers:

1. Cost per exclusive health or wellness lead at 45 plus, United States.
2. Whether Canada supply exists and at what cost.
3. Minimum monthly spend.
4. Days from signature to first delivery.
5. Your TCPA posture following the September 2025 FCC elimination of the one to one consent rule.

If pay per call supply exists alongside form fills, price that too. Calls are worth materially more to us than forms.

Omri Gitter
Gita Agency, for Longevity Life Academy by eTeacher Group
longevitylifeacademy.com""",
},
]

ONBOARDING = [
 ("1", "Astoria Company", "Launch a campaign in less than 30 minutes with our team", "https://www.astoriacompany.com/pay-per-call"),
 ("2", "NextGen Leads", "Creating an account and starting to buy leads takes a few minutes", "https://nextgenleads.com/health-insurance-leads"),
 ("3", "Semcasting", "From member lists or HCP list to live campaign in 48 hours", "https://www.semcasting.com/healthcare-and-pharmaceuticals"),
 ("4", "Aragon Advertising", "You are live in days, not months", "https://go.aragonco.com/"),
 ("5", "Palo Media", "Same day response guaranteed, which is a response not a launch", "https://palomediagroup.com/"),
]
