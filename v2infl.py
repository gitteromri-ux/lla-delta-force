# -*- coding: utf-8 -*-
"""Track 2 v2 influencer extras: card order, bespoke outreach and callouts.
Reach, screens and contact routes are parsed from track2_influencers_v2.md by parse_v2.py.
No em dashes, no en dashes, no exclamation marks, no emojis."""

# Shortlist ranks 1 to 10, then the next ten ranked GREEN first and by verified reach.
TOP20 = [38, 51, 37, 32, 46, 39, 24, 50, 23, 49, 5, 9, 13, 15, 18, 20, 2, 4, 6, 8]

HERO_CHIPS = [
    ("53", "people profiled with verified reach", "Every follower number carries the route it came from"),
    ("20", "full cards with a bespoke email ready to send", "Ranked by the shortlist logic, screen colour first"),
    ("11", "GREEN screens on the roster", "No competing paid programme, and they take third party money"),
    ("$10,500", "benchmark for the single best newsletter placement", "Kayla Barnes-Lentz, a stated 300,000 woman list"),
]

LEGEND = [
    ("GREEN", "Demonstrably takes third party sponsorship money and owns no paid education product that competes with an 18 week live longevity course."),
    ("AMBER", "Owns something adjacent, a supplement line, a device, a clinic, a diagnostics business or a self paced book or course, but demonstrably takes third party sponsors anyway."),
    ("RED", "Owns or continuously promotes a direct competitor, a paid multi week longevity or health education programme, cohort, certification or membership. Also RED where the person has publicly refused all sponsorship."),
]

REACH_NOTE = ("TOTAL REACH is Instagram followers plus YouTube subscribers plus X followers plus TikTok followers plus "
              "newsletter subscribers. Podcast downloads are reported inside each card but are not added into the total, "
              "because a download is a listening metric and not a follower. Where a platform could not be verified through "
              "the four discovery routes it is marked n.a. and excluded from the sum rather than guessed at.")

CALLOUTS = [
    ("The closest direct competitor sells LLA's exact promise at one eighth of the price.",
     "Dr. Kara Fitzgerald, number 47 on the roster, sells a biological age reversal program at $159. That is LLA's core promise, "
     "priced at roughly one eighth of the $1,249 ticket. This is a pricing defence problem, not a media problem, and it has to be "
     "answered on the sales page before any money is spent on influencer placement.",
     "Profile 47, Dr. Kara Fitzgerald", "https://www.drkarafitzgerald.com/contact/"),
    ("The CGM mechanic LLA sells is already bundled into a $499 a year subscription.",
     "Dr. Casey Means, number 25, sells Levels Core at $499 a year, which bundles the exact continuous glucose monitoring mechanic "
     "that LLA ships as the Abbott Lingo before lesson five. She is RED as an advertiser and unbuyable, and she is also the sharpest "
     "available read on how the competition packages and prices the same hardware moment.",
     "Profile 25, Dr. Casey Means", "https://www.caseymeans.com/"),
    ("One of the best fitting profiles on the roster publicly refuses all sponsorship.",
     "Nicolas Verhoeven, who publishes as Physionic, number 36 at 423,000 total reach, states plainly that he does not take "
     "sponsorships. He is scored RED-REFUSED rather than RED because the block is commercial availability, not competition. "
     "Do not spend outreach time here.",
     "Profile 36, Physionic", "https://physionic.org/"),
    ("The most transactable profile found declares brand partnerships with more than 150 companies.",
     "Dr. Molly Maloof, number 50, states on her own site that she is an advisor, consultant and brand partner to more than 150 "
     "companies and has worked with over 50. That is published, high volume, brand partnership behaviour. Her reach is small at "
     "98,316, which makes her cheap, and her answer speed is the reason she sits at rank eight on the shortlist.",
     "Profile 50, Dr. Molly Maloof", "https://drmolly.co/"),
]

# --------------------------------------------------------------- bespoke outreach
MAIL = {}

MAIL[38] = ("Weill Cornell brain ageing, an 18 week live cohort, and one paid Instagram placement",
"""Dr. Mosconi,

I am writing on behalf of Longevity Life Academy about a paid placement, not a guest appearance.

We run The Longevity Blueprint, an 18 week live online course. Eighteen 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. It is $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female, which is the same person who reads The Menopause Brain.

Your work on the women's brain and menopause is the single closest match to our curriculum on a roster of 53 creators we screened. You sell no competing course, no supplement line and no membership, which is why you are first on our list rather than tenth.

What we would like to buy is one Instagram feed post or Reel with a tracked link, and if it performs, a recurring monthly placement. The Instagram 100,000 to 500,000 band benchmarks at $500 to $2,500 for a feed post and $800 to $5,000 for a Reel, and we are comfortable at the upper end of both for the right fit.

Who handles commercial enquiries for you, and what does your rate card look like.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[51] = ("Higher Ground host read, women 45 to 65, 18 week live longevity course",
"""Higher Ground advertising team,

We would like to buy host read inventory on Dr. Sharon Malone's show.

The advertiser is Longevity Life Academy. The product is The Longevity Blueprint, an 18 week live online course with 18 fifty minute sessions, cohorts of 8 to 15, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. The buyer is 45 plus, 54.5 percent female, United States and Canada.

Dr. Malone is a board certified obstetrician gynaecologist and menopause specialist and the author of Grown Woman Talk. Her audience is women 45 to 65 with strong Black women representation, which is a group our current creative does not reach at all. She sells no competing course and no supplement line, so there is no conflict to clear.

What we want to price: a 60 second host read mid roll across three consecutive episodes, with a unique landing URL and promotional code so we can measure enrolments rather than impressions. We would also like the option to extend to a full quarter if the first flight clears our cost per enrolment target.

Please send available flight dates, the rate per episode and the downloads per episode the rate is based on.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[37] = ("Perimenopause, precision medicine and a paid Instagram placement for a live 18 week course",
"""Dr. Gottfried,

Longevity Life Academy would like to buy a paid Instagram placement from you.

We teach The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars covering metabolic health, hormones, sleep, movement, nutrition and cognition, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female.

We screened 53 creators in this category. You came out third overall, and first among the ones we can reach directly, because you publish a business email and a phone number, you sell no competing course, and hormones and perimenopause for women 40 to 60 is precisely our student.

The ask is one Instagram feed post or Reel with a tracked link, and a second placement thirty days later if the first clears our cost per enrolment target. Published benchmarks for your follower band are $500 to $2,500 for a feed post and $800 to $5,000 for a Reel. We can work inside that and we will pay promptly.

Is this something you or your team would consider, and what is the rate.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[32] = ("Host read on The Dr. Tyna Show, midlife metabolic health, three episode flight",
"""Dr. Moore,

We want to buy host read inventory on The Dr. Tyna Show, and we are writing because you already sell it.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. The buyer is 45 plus, 54.5 percent female, United States and Canada.

Two reasons you are on a very short list. First, your show carries named third party sponsors, so we know host read inventory is available and priced. Second, a 4.9 out of 5 rating across 2,300 ratings is unusually high audience trust, and trust is what converts a $1,249 considered purchase. On trust per dollar you are the best value on our roster of 53.

The ask is a 60 second host read mid roll across three consecutive episodes with a unique URL and code, and a first refusal on the following quarter if it works.

What is your rate per episode, and what downloads per episode does that rate assume.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[46] = ("The Girlfriend Doctor and an 18 week live longevity course, paid placement",
"""Dr. Cabeca, team,

Longevity Life Academy would like to buy a paid placement, and your team email and phone number are published, so we are going straight to the point.

The product is The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. The buyer is 45 plus, 54.5 percent female, United States and Canada.

The Girlfriend Doctor audience is menopause, keto green and sexual health for women 45 to 65, which is almost exactly our student. Your own line, Julva at $39.97, Mighty Maca Plus at $39.95 and Balance at $54.95, sits alongside our course rather than against it. There is no conflict here, and there is a clean cross sell.

What we want to price: one Instagram feed post or Reel with a tracked link, plus one dedicated email to your list if you sell that separately. The published band for your follower size is $500 to $2,500 for a feed post, and we consider that good value for this audience.

What are your rates, and what is the soonest available slot.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[39] = ("Menopause specialist audience, paid placement, and an honest note about the overlap",
"""Dr. Hirsch,

Longevity Life Academy would like to buy a paid placement, and we want to be straight about one thing up front.

We run The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. The buyer is 45 plus, 54.5 percent female, United States and Canada.

The honest part: you sell the Reclaiming Menopause Masterclass. We do not read that as a competitor to an 18 week live cohort with hardware, and our screen puts you in the amber category rather than the red one for exactly that reason. If you see it differently, tell us and we will stop.

If you do not, the ask is one Instagram or TikTok placement with a tracked link, and a paid Substack sponsorship if you sell that inventory. Your audience is women 40 to 60 across a balanced Instagram, TikTok and YouTube footprint, which is cheap per targeted impression at your follower band of $500 to $2,500 for a feed post.

What are your rates, and would you consider a cross promotion where your masterclass graduates get a defined discount on our course.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[24] = ("The Proof, host read flight, North America geo split requested",
"""Voicing Change partnerships team,

We would like to buy host read inventory on Simon Hill's The Proof.

The advertiser is Longevity Life Academy. The product is The Longevity Blueprint, an 18 week live online course, 18 live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289.

Simon has the largest reach of any creator on our roster that carries a clean competition screen, which means no supplement line, no diagnostics business and no paid course to sit against ours. That is why he is on the list at a reach level where almost everyone else is conflicted.

One thing we need before we commit. Our buyer is United States and Canada, and The Proof is Australia based with a large international listenership. Please send the North America share of downloads per episode, and quote the rate against that share rather than global.

Ask: 60 second host read mid roll across three consecutive episodes, unique URL and promotional code, with an option to extend for a quarter.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[50] = ("Brand partnership, 18 week live longevity course, fast yes wanted",
"""Dr. Maloof,

Your site says you are an advisor, consultant and brand partner to more than 150 companies. We would like to be one of them, and we would like to move quickly.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. The buyer is North American, 45 plus and 54.5 percent female. Your healthspan and energy audience sits slightly younger than that, and we think the overlap is still worth paying for.

The ask is a package rather than a single post: one Instagram Reel, one Substack placement and one short expert segment we can license for use inside the course and in paid social, with your name and Stanford training on it. Instagram benchmarks at your follower band are $500 to $2,500 for a feed post, and we expect the licensed segment to be priced separately.

Send your rate card and we will come back inside 48 hours.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[23] = ("The Vajenda, a paid newsletter placement, and the clinical detail first",
"""Ann, Sharon,

We are trying to reach Dr. Gunter's commercial contact and your names are the two published on her site, so please forward this if it is not yours.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course taught by clinicians. Eighteen live 50 minute sessions, cohorts of 8 to 15, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289.

We are leading with the curriculum rather than with lifestyle language on purpose. Dr. Gunter polices unsupported wellness claims in public and she is right to. Our course makes no anti ageing claim. It teaches metabolic, hormonal, sleep, movement, nutrition and cognitive health with measurement attached, which is why the glucose monitor is in the box.

The ask is one paid placement in The Vajenda, which has 129,000 paying subscribers and sits fourth in health and wellness on Substack. We think that is the best targeted inventory unit in this whole category for a considered $1,249 purchase, and it benchmarks around $4,500 to $8,000 per placement.

We are happy to submit the full syllabus for review before anything is agreed. Who prices newsletter inventory.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[49] = ("Ageless, an expert interview inside an 18 week course, paid",
"""Dr. Steele,

This is a paid request and it is not a request for a sponsored post.

Longevity Life Academy teaches The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. Students are North American and mostly 45 plus.

We screened 53 people in this category on whether they sell something that competes with us. You are one of the cleanest results in the set. No supplement line, no diagnostics business, no paid course, no membership, no clinic, and a published email, which almost nobody else on the list has.

What we want to buy is one recorded expert interview, roughly 45 minutes, on what the biology of ageing actually supports and what it does not, licensed for use inside the course and in a trimmed form in paid social. We would also take a short quote for the sales page if you are comfortable with the syllabus after reading it.

This is a credibility buy rather than a reach buy, and we will price it as such. What is your fee for a licensed interview of that length.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[5] = ("Highest performing sponsorship, your words, and a $1,249 course to test it on",
"""Thomas,

Your contact page runs a sponsor testimonial calling you one of their highest performing sponsorships on return on ad spend. We would like to find out whether that holds for a $1,249 course.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. Buyer is North American, 45 plus, 54.5 percent female.

We know your audience skews younger and more male than our buyer. We are willing to test anyway because your production quality and click through are documented by a paying sponsor, and because a metabolic health audience self selects for the exact mechanism our course teaches.

The ask is one 60 to 90 second integration inside a long form video with a tracked URL and a promotional code, priced as a test, with a second integration and a dedicated video on the table if the first clears our cost per enrolment target. Published benchmarks at your subscriber level start at $23,000 per integration and $35,000 for a dedicated video.

What is your rate card, and what is the earliest slot.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[9] = ("Feel Better Live More sponsorship, United States geo split requested",
"""Voicing Change partnerships team,

We would like to buy sponsorship inventory on Dr. Rangan Chatterjee's Feel Better, Live More.

The advertiser is Longevity Life Academy. The product is The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289.

Dr. Chatterjee screens clean for us. No supplement line, no diagnostics business, no competing multi week cohort, and a named published sponsorship intake, which is rarer on this roster than it should be. The show is a midlife health show and the audience is 40 plus, which is our buyer.

The one constraint. Our students are United States and Canada, and the show's base is United Kingdom heavy. Please quote against the North America share of downloads and send that share per episode so we can model it.

Ask: 60 second host read mid roll across three consecutive episodes, unique URL and code, option to extend for a quarter, and pricing for a dedicated newsletter placement if that inventory exists.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[13] = ("Hormones, fatigue and midlife metabolic health, paid Instagram placement",
"""Dr. Shah,

Longevity Life Academy would like to buy a paid placement on your Instagram.

We teach The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. Our buyer is 45 plus, 54.5 percent female, United States and Canada, and your podcast charts in nutrition in both countries, which matches our geography exactly.

On our screen of 53 creators you are the cleanest result above two million reach. Books only today, consultations and a supplement line both stated as launching in 2026, and nothing selling against an 18 week live cohort right now. That timing is part of why we are writing this month rather than next year.

The ask is one Instagram Reel with a tracked link and a promotional code, then a three placement flight if the first clears our cost per enrolment target. Benchmarks at your follower level run $15,000 to $100,000 for a Reel, so please tell us where in that range you actually sit.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[15] = ("Eat to Beat Disease and a disease prevention audience, paid placement",
"""Dr. Li,

You publish a direct business email, which on a roster of 53 creators is rare enough that it moved you up our list, so this is a direct commercial ask.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped before lesson five. $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female.

Your food as medicine and angiogenesis work is framed around disease prevention, which is the mindset a 45 year old buys this course in. Your screen is clean, no paid course, no membership, no diagnostics business, so there is nothing to clear before we can transact.

The ask is one YouTube integration of 60 to 90 seconds inside a long form video with a tracked URL, and one Instagram placement in the same month. Published benchmarks for your subscriber band are $10,000 to $23,000 per integration and $15,000 to $35,000 for a dedicated video.

What is your rate, and do you work directly or through a representative.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[18] = ("Harvard metabolic science, one integration, credibility transfer to a paid course",
"""Nick,

Longevity Life Academy would like to buy a paid integration on your channel.

We run The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. Our buyer is North American and mostly 45 plus.

Your audience is younger and more science literate than our median student and we are still writing, because for an evidence based course the credibility transfer is worth more than a perfect demographic match. A metabolic science explainer channel with a Harvard medical and doctoral background is the right voice to say that our curriculum is measurement led rather than claim led.

The ask is one 60 to 90 second integration inside a long form video with a tracked URL and a promotional code, plus an option on a paid Substack placement in the same month. Published benchmarks at your subscriber level run $10,000 to $23,000 for an integration.

We can send the full 18 week syllabus for review before you decide. What is your rate.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[20] = ("Genius Life host read, dementia prevention audience, three episode flight",
"""Max,

Longevity Life Academy would like to buy host read inventory on The Genius Life.

The product is The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female.

Brain health and dementia prevention is a 45 plus proposition with a strong female lean, and your show has run third party host reads for years, so there is no new commercial machinery to build here. Your screen is clean on our side too, no supplement company, no diagnostics business, no competing course.

The ask is a 60 second host read mid roll across three consecutive episodes with a unique URL and promotional code, plus one Instagram placement in the same flight so we can compare the two formats on the same offer.

Please send your rate per episode, the downloads per episode it assumes, and the United States share of that number.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[2] = ("Glucose, an Abbott Lingo in every box, and a paid Reel",
"""Jessie, team,

Longevity Life Academy would like to buy one paid Instagram placement, and the mechanic overlaps with yours almost exactly.

We teach The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five, so glucose response is measured rather than described. $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female.

Your Anti-Spike line and your books sit alongside a live 18 week cohort rather than against it, which is why our screen puts you in the amber category and not the red one. If you disagree with that read, say so and we will not pursue it.

The ask is one Instagram Reel with a tracked link and a promotional code. Benchmarks in your follower band run $15,000 to $100,000 for a Reel, and a straight cost per thousand cross check on six million followers at the wellness rate lands between $90,000 and $210,000 for full reach delivery, so we expect to be quoted high and we would like to know where you actually price.

Who handles brand partnerships.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[4] = ("Partnership enquiry, menopause audience, an 18 week live course with hardware",
"""The Pause Life partnerships team,

Longevity Life Academy would like to discuss a paid partnership with Dr. Haver.

We run The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. The buyer is 45 plus, 54.5 percent female, United States and Canada.

We have read your product line honestly. The Pause Life and Galveston Diet sell self paced online programmes, a membership and a supplement line. Ours is a live taught cohort with a clinician on the call and hardware in the box, which is a different purchase and a different price point. We think the two sit next to each other, and we would rather say that plainly than pretend the overlap does not exist.

Two shapes we would pay for. One, a straightforward paid Instagram Reel with a tracked link. Two, a partner offer where your members get a defined discount on our cohort and you take an agreed share. We are open to either or both.

What does the commercial conversation look like, and who leads it.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[6] = ("YouTube integration, an older patient audience, 18 week live longevity course",
"""Dr. Ekberg,

Your website contact page is currently returning an error, so this is coming through the routes that do work.

Longevity Life Academy runs The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. Our buyer is North American, 45 plus and 54.5 percent female.

Of the large channels we screened, yours pulls what looks like the oldest and most patient audience in the category, and long form explainer content on metabolic health and ageing is the closest possible match to a course taught in 18 live sessions rather than in 30 second clips. We could not confirm a published sponsorship intake anywhere, which is the only reason you are not screened green, so this letter is partly a question about whether you take brand integrations at all.

If you do, the ask is one 60 to 90 second integration inside a long form video with a tracked URL and a promotional code. Published benchmarks at your subscriber level start at $23,000 per integration.

Do you take third party sponsorship, and if so, what is the rate.

Omri Gitter
Gita Agency, for Longevity Life Academy""")

MAIL[8] = ("FoundMyFitness advertising intake, host read plus newsletter, budget band $20,000 to $50,000",
"""FoundMyFitness advertising team,

We are submitting through the published advertising intake and this note is the detail behind the form.

Advertiser: Longevity Life Academy. Product: The Longevity Blueprint, an 18 week live online course. Eighteen live 50 minute sessions, cohorts of 8 to 15, six pillars, and an Abbott Lingo continuous glucose monitor shipped to every student before lesson five. $1,249 upfront or five payments of $289. Buyer is North American, 45 plus and 54.5 percent female.

Budget band on the form: $20,000 to $50,000 for a first flight, with room to extend.

What we want to buy, in priority order.

1. A newsletter placement. The 300,000 subscriber list is the highest intent inventory unit you have for a considered $1,249 purchase, and it is the one we want first.
2. A host read ad, 60 seconds, across three episodes, with a unique URL and promotional code.
3. A guest interview slot only if it can carry a disclosed commercial arrangement, which we would rather do openly than not at all.

We know the audience skews male and 30 to 50 while our buyer is older and mostly female. We are buying it anyway because the audience is self selected for exactly the mechanism the course teaches.

Please confirm availability, rates per unit and the earliest flight date.

Omri Gitter
Gita Agency, for Longevity Life Academy""")
