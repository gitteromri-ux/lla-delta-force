# -*- coding: utf-8 -*-
"""Builds index.html for E-COMMERCE DELTA FORCE GO LIVE."""
import html, json, re
import data as D
import data2 as D2
import data3 as D3

E = html.escape
def A(t): return E(t).replace("\n\n", "</p><p>").replace("\n", "<br>")

_cid = [0]
def copybox(text, label="Copy"):
    _cid[0] += 1
    i = f"cb{_cid[0]}"
    return (f'<div class="cbx"><div class="cbx-h"><span class="cbx-l">{E(label)}</span>'
            f'<button class="cpy" data-t="{i}">Copy</button></div>'
            f'<pre class="cbx-b" id="{i}">{E(text)}</pre></div>')

def srclinks(pairs):
    if not pairs: return ""
    return '<span class="srcs">' + " ".join(
        f'<a href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a>' for t, u in pairs) + "</span>"

def chips(items):
    out = ['<div class="chips">']
    for c in items:
        v, l, n = (list(c) + ["", ""])[:3]
        out.append(f'<div class="chip"><div class="chip-v">{E(str(v))}</div>'
                   f'<div class="chip-l">{E(l)}</div>'
                   + (f'<div class="chip-n">{E(n)}</div>' if n else "") + '</div>')
    out.append("</div>")
    return "".join(out)

def head(t, kicker=None):
    k = f'<div class="kick">{E(kicker)}</div>' if kicker else ""
    return f'<div class="hd">{k}<h2>{E(t)}</h2></div>'

def block(d, kicker=None):
    """generic {head, chips?, lines?, close?}"""
    o = [head(d["head"], kicker)]
    if d.get("chips"): o.append(chips(d["chips"]))
    if d.get("lines"):
        o.append('<div class="lines">')
        for ln in d["lines"]:
            if isinstance(ln, tuple):
                o.append(f'<p class="ln">{E(ln[0])} {srclinks(ln[1])}</p>')
            else:
                o.append(f'<p class="ln">{E(ln)}</p>')
        o.append("</div>")
    if d.get("close"): o.append(f'<p class="close">{E(d["close"])}</p>')
    return f'<section class="blk">{"".join(o)}</section>'

def table(headers, rows, cls="", hi_idx=None):
    o = [f'<div class="twrap"><table class="tbl {cls}"><thead><tr>']
    for h in headers: o.append(f"<th>{E(h)}</th>")
    o.append("</tr></thead><tbody>")
    for r in rows:
        hi = ""
        cells = list(r)
        if hi_idx is not None and len(cells) > hi_idx and isinstance(cells[hi_idx], bool):
            hi = " class=\"hi\"" if cells[hi_idx] else ""
            cells = cells[:hi_idx]
        o.append(f"<tr{hi}>")
        for c in cells: o.append(f"<td>{E(str(c))}</td>")
        o.append("</tr>")
    o.append("</tbody></table></div>")
    return "".join(o)

# ============================================================ TAB 1
def tab1():
    o = ['<div class="tabpane" id="p-golive">']
    o.append('<section class="hero">'
             '<h1 class="h1">Go live today.</h1>'
             '<p class="lede">Seven campaigns, the exact budgets, the exact audiences, the exact creative and the exact copy. '
             'Nothing on this tab requires a further decision except the four items in the alert below.</p>')
    o.append(chips([
        ("7", "campaigns specified and ready", "Phase 0 through Phase 2"),
        ("36", "creatives embedded from the live repositories", "Every image served from raw.githubusercontent.com"),
        ("$1,249", "upfront price, reduced from $1,800", "Or five payments of $289, totalling $1,445"),
        ("4", "blockers that must clear before spend", "Listed in the red alert directly below"),
    ]))
    o.append("</section>")

    # RED ALERT
    o.append('<section class="alert"><div class="alert-h"><span class="alert-tag">RED ALERT</span>'
             '<h2>Four things are broken and every campaign below is blocked until they clear.</h2></div>'
             '<div class="alert-grid">')
    for i, (t, b, s) in enumerate(D.BLOCKERS, 1):
        o.append(f'<div class="alert-card"><div class="alert-n">{i:02d}</div>'
                 f'<h3>{E(t)}</h3><p>{E(b)}</p>{srclinks(s)}</div>')
    o.append("</div></section>")

    # campaigns
    phase = None
    for c in D.CAMPAIGNS:
        if c["phase"] != phase:
            phase = c["phase"]
            o.append(f'<div class="phase-rule"><span>{E(phase)}</span></div>')
        o.append('<article class="camp">')
        o.append(f'<div class="camp-top"><div class="camp-code">{E(c["code"])}</div>'
                 f'<div><h3 class="camp-name">{E(c["name"])}</h3>'
                 f'<div class="camp-obj">{E(c["objective"])}</div></div>'
                 f'<div class="camp-budget"><div class="bv">{E(c["budget"])}</div>'
                 f'<div class="bl">{E(c["budget_note"])}</div></div></div>')

        o.append('<div class="spec">')
        for k, v in [("Optimisation event", c["event"]), ("Audience", c["audience"]),
                     ("Placements", c["placements"]), ("Structure", c["structure"]),
                     ("Destination URL", None)]:
            if k == "Destination URL":
                o.append(f'<div class="sp"><div class="sp-k">{k}</div><div class="sp-v">'
                         f'<a href="{E(c["dest"])}" target="_blank" rel="noopener">{E(c["dest"])}</a></div></div>')
            else:
                o.append(f'<div class="sp"><div class="sp-k">{k}</div><div class="sp-v">{E(v)}</div></div>')
        o.append("</div>")

        o.append(f'<div class="cr-head"><h4>{E(c["creative_set"])}</h4>'
                 f'<a class="repo" href="{E(c["creative_repo"])}" target="_blank" rel="noopener">Repository</a></div>')
        o.append('<div class="cr-grid">')
        for im in c["imgs"]:
            o.append(f'<figure class="cr"><div class="cr-box" style="aspect-ratio:{E(im["r"])}">'
                     f'<img src="{E(im["u"])}" alt="{E(im["label"])}" loading="lazy"></div>'
                     f'<figcaption><b>{E(im["label"])}</b><span>{E(im["note"])}</span></figcaption></figure>')
        o.append("</div>")

        o.append('<div class="copyset">')
        o.append(copybox(c["primary"], "Primary text"))
        o.append(copybox(c["headline"], "Headline"))
        o.append(copybox(c["description"], "Description"))
        o.append("</div>")
        o.append(f'<div class="why"><b>Why this runs.</b> {E(c["why"])} {srclinks(c["why_src"])}</div>')
        o.append("</article>")

    # creative bank
    o.append('<section class="blk">' + head("Creative bank held in reserve.") +
             '<div class="bank">')
    for b in D.CREATIVE_BANK:
        o.append(f'<figure class="bk"><div class="cr-box" style="aspect-ratio:1/1">'
                 f'<img src="{E(b["u"])}" alt="{E(b["t"])}" loading="lazy"></div>'
                 f'<figcaption>{E(b["t"])}</figcaption></figure>')
    o.append("</div></section>")
    o.append("</div>")
    return "".join(o)

# ============================================================ TAB 2
def tab2():
    o = ['<div class="tabpane" id="p-meta" hidden>']
    o.append('<section class="hero">'
             f'<h1 class="h1">{E(D2.META_HEADLINE)}</h1>'
             '<p class="lede">The account is not underperforming because the media buy is wrong. '
             'It is underperforming because the thing Meta is asked to optimise toward cannot be completed on the site.</p>')
    o.append(chips(D2.META_HERO_CHIPS))
    o.append("</section>")

    o.append(block(D2.META_BLOCKER))

    # TWO LINES
    o.append('<section class="blk">' + head(D3.TWO_LINES_HEAD))
    o.append(chips(D3.TWO_LINES_CHIPS))
    o.append('<div class="twoline">')
    for L, tone in ((D3.LINE_A, "a"), (D3.LINE_B, "b")):
        o.append(f'<div class="lane lane-{tone}">'
                 f'<div class="lane-tag">{E(L["tag"])}</div>'
                 f'<h3 class="lane-t">{E(L["title"])}</h3>'
                 f'<div class="lane-state">{E(L["state"])}</div><dl class="lane-spec">')
        for k, v in L["spec"]:
            o.append(f"<dt>{E(k)}</dt><dd>{E(v)}</dd>")
        o.append('</dl><div class="lane-math"><b>The arithmetic.</b><ul>')
        for k, v in L["math"]:
            o.append(f"<li><b>{E(k)}</b> equals {E(v)}</li>")
        o.append(f'</ul></div><p class="lane-v">{E(L["verdict"])}</p></div>')
    o.append("</div></section>")

    o.append('<section class="blk">' + head("Line A against Line B, side by side.") +
             table(["", "Line A, lead gen to call centre", "Line B, direct e-commerce"], D3.LINE_COMPARE, "cmp") +
             "</section>")

    # Atelier
    o.append('<section class="blk">' + head(D3.ATELIER["head"]) +
             table(["Input", "Value"], D3.ATELIER["rows"], "kv") +
             f'<p class="close">{E(D3.ATELIER["close"])}</p></section>')

    # Line A sensitivity
    rows = []
    for cr, cells in D3.SENS_ROWS:
        r = [cr]
        for cpa, roas, ok in cells:
            r.append(f"{cpa} cost per acquisition, {roas}")
        rows.append(r)
    o.append('<section class="blk">' + head("What the contact rate has to be for Line A to survive.") +
             chips([("11.3x", "best cell in the grid", "A $20 lead closing at 18 percent"),
                    ("1.00x", "break even line", "Every cell below it loses money on media alone"),
                    ("0.42x", "worst cell in the grid", "A $60 lead closing at 2 percent")]))
    o.append('<div class="twrap"><table class="tbl sens"><thead><tr><th>Close rate</th>'
             + "".join(f"<th>Cost per lead {E(c)}</th>" for c in D3.SENS_CPLS) + "</tr></thead><tbody>")
    for cr, cells in D3.SENS_ROWS:
        o.append(f'<tr><th scope="row">{E(cr)}</th>')
        for cpa, roas, ok in cells:
            cls = "cell ok" if ok else "cell bad"
            o.append(f'<td class="{cls}"><div class="cell-v">{E(roas)}</div>'
                     f'<div class="cell-n">{E(cpa)} cost per acquisition</div></td>')
        o.append("</tr>")
    o.append("</tbody></table></div>")
    o.append(f'<p class="close">{E(D3.SENS_NOTE)}</p></section>')

    # Line B model
    o.append('<section class="blk">' + head("Line B modelled in full, at $20,000 and at $50,000.") +
             '<p class="close">Every input is named and every output is derived from it, so any number here can be moved and the rest follows.</p>')
    o.append('<div class="twrap"><table class="tbl kv4"><thead><tr><th>Input</th><th>Value</th><th>Basis</th><th>Source</th></tr></thead><tbody>')
    for a, b, c, u in D3.LINEB_INPUTS:
        o.append(f'<tr><td>{E(a)}</td><td><b>{E(b)}</b></td><td>{E(c)}</td>'
                 f'<td><a href="{E(u)}" target="_blank" rel="noopener">Source</a></td></tr>')
    o.append("</tbody></table></div>")

    hdrs = ["Spend", "Case", "Checkout rate", "Impressions", "Clicks", "Cost per click",
            "Landing page views", "Purchases", "Cost per acquisition", "Revenue", "Return on ad spend"]
    o.append('<h3 class="sub">Line B at $20,000 a month</h3>')
    o.append(table(hdrs, D3.LINEB_20K, "num", hi_idx=11))
    o.append('<h3 class="sub">Line B at $50,000 a month</h3>')
    o.append(table(hdrs, D3.LINEB_50K, "num", hi_idx=11))
    o.append('<h3 class="sub">Break even, stated plainly</h3>')
    o.append(table(["Spend", "Purchases needed", "Checkout rate needed", "How it is derived"], D3.BREAKEVEN, "kv4"))
    o.append(f'<p class="close">{E(D3.LINE_B["verdict"])}</p></section>')

    # Decision
    o.append('<section class="decide">' + f'<h2>{E(D3.CEO_DECISION["head"])}</h2><ol>' +
             "".join(f"<li>{E(x)}</li>" for x in D3.CEO_DECISION["lines"]) + "</ol></section>")

    o.append(block(D2.META_FIFTY))
    o.append(block(D2.META_CONSOLIDATION))
    o.append(block(D2.META_ATTRIBUTION))
    o.append(block(D2.META_COMPARABLE))
    o.append(block(D2.META_PHONE))

    # scenario planning
    o.append('<section class="blk">' + head("Scenario planning, not a minimum viable budget.") +
             '<p class="close">These are the same funnel assumptions applied across four spend levels. '
             'The account already runs at $20,000, so the $20,000 rows are the live case and the rest show the slope.</p>')
    o.append('<div class="twrap"><table class="tbl kv4"><thead><tr><th>Input</th><th>Conservative</th><th>Base</th><th>Optimistic</th><th>Basis</th></tr></thead><tbody>')
    for name, c, b, opt, basis, u in D2.FUNNEL_INPUTS:
        o.append(f'<tr><td>{E(name)}</td><td>{E(c)}</td><td><b>{E(b)}</b></td><td>{E(opt)}</td>'
                 f'<td>{E(basis)} <a href="{E(u)}" target="_blank" rel="noopener">Source</a></td></tr>')
    o.append("</tbody></table></div>")
    o.append(table(["Spend", "Case", "Impressions", "Clicks", "Cost per click", "Landing page views",
                    "Initiate Checkout", "Cost per Initiate Checkout", "Purchases",
                    "Cost per acquisition", "Revenue", "Return on ad spend"],
                   D3.FUNNEL_ROWS_V2, "num", hi_idx=12))
    o.append("</section>")

    o.append('<section class="blk">' + head("The build order.") +
             table(["Stage", "Budget", "Structure", "Optimisation event", "What it returns"], D3.META_PLAN_V2, "kv4") +
             '<h3 class="sub">Which event to optimise toward, and when</h3>' +
             table(["Event", "Implied cost per event", "Verdict"], D2.META_EVENT_LADDER, "kv4") + "</section>")
    o.append("</div>")
    return "".join(o)

# ============================================================ TAB 3
def tab3():
    o = ['<div class="tabpane" id="p-leads" hidden>']
    o.append('<section class="hero"><h1 class="h1">Buy high intent leads.</h1>'
             '<p class="lede">Five vendors with verified pricing and three backups, each with a named contact and an outreach email written and ready to send.</p>')
    o.append(chips([
        ("5", "primary vendors with published or derived pricing", "Ranked by speed to live traffic"),
        ("3", "backups held for when a primary stalls", "Nothing commercial published on any of the three"),
        ("30 min", "fastest published launch in the set", "Astoria Company, pay per call division"),
        ("$40 to $80", "planning band per inbound call", "Derived from published adjacent verticals"),
    ]))
    o.append("</section>")

    def vcard(v, backup=False):
        s = ['<article class="vend%s">' % (" vend-bk" if backup else "")]
        s.append(f'<div class="vend-top"><div class="vend-rank">{E(v["rank"])}</div>'
                 f'<div><h3>{E(v["name"])}</h3><div class="vend-kind">{E(v["kind"])}</div></div></div>')
        s.append('<div class="spec">')
        s.append(f'<div class="sp"><div class="sp-k">Verified pricing</div><div class="sp-v">{E(v["price"])} {srclinks([v["price_src"]])}</div></div>')
        s.append(f'<div class="sp"><div class="sp-k">Speed to live</div><div class="sp-v">{E(v["launch"])} {srclinks([v["launch_src"]])}</div></div>')
        s.append(f'<div class="sp"><div class="sp-k">Named contact</div><div class="sp-v">'
                 f'<a href="{E(v["contact_url"])}" target="_blank" rel="noopener">{E(v["contact_name"])}</a>'
                 + (" " + " ".join(f'<a class="xtra" href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a>' for t, u in v.get("contact_extra", [])))
                 + "</div></div>")
        s.append(f'<div class="sp"><div class="sp-k">Risk</div><div class="sp-v">{E(v["risk"])} {srclinks([v["risk_src"]])}</div></div>')
        s.append(f'<div class="sp"><div class="sp-k">Consent posture</div><div class="sp-v">{E(v["tcpa"])}</div></div>')
        s.append("</div>")
        s.append('<div class="copyset">')
        s.append(copybox(v["subject"], "Subject line"))
        s.append(copybox(v["email"], "Outreach email"))
        s.append("</div></article>")
        return "".join(s)

    o.append('<div class="phase-rule"><span>PRIMARY VENDORS</span></div>')
    for v in D.VENDORS: o.append(vcard(v))
    o.append('<div class="phase-rule"><span>BACKUPS</span></div>')
    for v in D.BACKUPS: o.append(vcard(v, True))

    o.append('<section class="blk">' + head("Ranked by how fast money turns into traffic.") +
             '<div class="twrap"><table class="tbl kv4"><thead><tr><th>Order</th><th>Vendor</th><th>Published claim</th><th>Source</th></tr></thead><tbody>')
    for n, name, claim, u in D.ONBOARDING:
        o.append(f'<tr><td>{E(n)}</td><td><b>{E(name)}</b></td><td>{E(claim)}</td>'
                 f'<td><a href="{E(u)}" target="_blank" rel="noopener">Source</a></td></tr>')
    o.append("</tbody></table></div></section>")
    o.append("</div>")
    return "".join(o)

# ============================================================ TAB 4
def tab4():
    o = ['<div class="tabpane" id="p-infl" hidden>']
    o.append('<section class="hero"><h1 class="h1">Fifteen names, ranked by whether they can actually say yes.</h1>'
             f'<p class="lede">{E(D2.INFL_ORDER)} Each card carries a published contact route and an email written for that specific person.</p>')
    o.append(chips([(a, b, c) for a, b, c, _ in D2.INFL_BENCHMARKS]))
    o.append("</section>")
    o.append('<div class="legend"><div><b>GREEN</b> No competing paid course, published contact route, realistic yes.</div>'
             '<div><b>AMBER</b> Adjacent commercial interest that needs clearing first.</div>'
             '<div><b>RED</b> Sells a directly competing paid programme.</div></div>')

    for p in D2.INFLUENCERS:
        o.append(f'<article class="infl chip-{p["chip"].lower()}">')
        o.append(f'<div class="infl-top"><div class="infl-n">{p["n"]:02d}</div>'
                 f'<div><h3>{E(p["name"])}</h3><div class="infl-role">{E(p["role"])}</div></div>'
                 f'<div class="badge b-{p["chip"].lower()}">{E(p["chip"])}</div></div>')
        o.append('<div class="counts">')
        for plat, cnt, u in p["counts"]:
            o.append(f'<a class="cnt" href="{E(u)}" target="_blank" rel="noopener">'
                     f'<span class="cnt-v">{E(cnt)}</span><span class="cnt-l">{E(plat)}</span></a>')
        o.append("</div>")
        o.append('<div class="spec">')
        o.append(f'<div class="sp"><div class="sp-k">Status</div><div class="sp-v">{E(p["chip_why"])} {srclinks([p["chip_src"]])}</div></div>')
        o.append(f'<div class="sp"><div class="sp-k">Price signal</div><div class="sp-v">{E(p["price"])} {srclinks([p["price_src"]])}</div></div>')
        o.append(f'<div class="sp"><div class="sp-k">Why this person</div><div class="sp-v">{E(p["fit"])}</div></div>')
        routes = [(p["email_addr"], "mailto:" + p["email_addr"])] if p.get("email_addr") else []
        rhtml = " ".join(f'<a class="xtra" href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a>' for t, u in routes)
        if p.get("dm"): rhtml += f' <a class="xtra" href="{E(p["dm"])}" target="_blank" rel="noopener">Instagram direct message</a>'
        if p.get("form"): rhtml += f' <a class="xtra" href="{E(p["form"])}" target="_blank" rel="noopener">Contact form</a>'
        src = srclinks([p["email_src"]]) if p.get("email_src") else ""
        o.append(f'<div class="sp"><div class="sp-k">Contact routes</div><div class="sp-v">{rhtml} {src}</div></div>')
        o.append("</div>")
        o.append('<div class="copyset">')
        o.append(copybox(p["subject"], "Subject line"))
        o.append(copybox(p["body"], "Outreach email"))
        o.append("</div></article>")

    o.append('<section class="blk">' + head("What a paid placement costs, by channel.") +
             '<div class="twrap"><table class="tbl kv4"><thead><tr><th>Band</th><th>What it buys</th><th>Detail</th><th>Source</th></tr></thead><tbody>')
    for a, b, c, u in D2.INFL_BENCHMARKS:
        o.append(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td>'
                 f'<td><a href="{E(u)}" target="_blank" rel="noopener">Source</a></td></tr>')
    o.append("</tbody></table></div></section>")
    o.append("</div>")
    return "".join(o)

# ============================================================ TAB 5
def tab5():
    o = ['<div class="tabpane" id="p-email" hidden>']
    o.append('<section class="hero"><h1 class="h1">Nine emails, written and ready to load.</h1>'
             '<p class="lede">Four recovery stages fire against an abandoned enrollment and five drip emails run against a new enquiry.</p>')
    o.append(chips([(a, b, c) for a, b, c in D2.EMAIL_RULES]))
    o.append("</section>")

    def mail(m):
        s = ['<article class="mail">']
        s.append(f'<div class="mail-stage">{E(m["stage"])}</div>')
        s.append('<div class="mail-frame"><div class="mail-hdr">'
                 f'<div class="mrow"><span class="mk">From</span><span class="mv">{E(m["frm"])}</span></div>'
                 f'<div class="mrow"><span class="mk">Subject</span><span class="mv msubj">{E(m["subj"])}</span></div>'
                 f'<div class="mrow"><span class="mk">Preheader</span><span class="mv">{E(m["pre"])}</span></div>'
                 "</div>")
        s.append(f'<div class="mail-body"><p>{A(m["body"])}</p></div></div>')
        s.append(copybox(m["subj"], "Subject line"))
        s.append(copybox(m["body"], "Email body"))
        s.append("</article>")
        return "".join(s)

    o.append('<div class="phase-rule"><span>ABANDONED ENROLLMENT RECOVERY</span></div>')
    o.append('<div class="mails">' + "".join(mail(m) for m in D2.RECOVERY) + "</div>")
    o.append('<div class="phase-rule"><span>NEW ENQUIRY DRIP</span></div>')
    o.append('<div class="mails">' + "".join(mail(m) for m in D2.DRIP) + "</div>")
    o.append("</div>")
    return "".join(o)

# ============================================================ TAB 6
def tab6():
    o = ['<div class="tabpane" id="p-ceo" hidden>']
    o.append('<section class="hero"><h1 class="h1">What $20,000 a month buys, and what is standing in front of it.</h1>'
             '<p class="lede">Current spend is the base case. Every figure below traces to the model on the Meta tab.</p>')
    o.append(chips(D3.FORECAST_CHIPS_V2))
    o.append("</section>")

    o.append('<section class="blk">' + head("Budget scenarios on the lead gen model.") +
             table(["Monthly spend", "Purchases", "Cost per acquisition", "Revenue", "Return on ad spend", "Read"],
                   D3.FORECAST_SCENARIOS_V2, "kv4") + "</section>")

    o.append('<section class="blk">' + head("Direct e-commerce, once the checkout exists.") +
             table(["Spend", "Case", "Checkout rate", "Impressions", "Clicks", "Cost per click",
                    "Landing page views", "Purchases", "Cost per acquisition", "Revenue", "Return on ad spend"],
                   D3.LINEB_20K + D3.LINEB_50K, "num", hi_idx=11) + "</section>")

    o.append('<section class="blk">' + head("Cash in month one against cash across the cohort.") +
             '<p class="close">The five payment plan collects $289 in month one and the remaining $1,156 over the following four months, which is why month one cash sits below one times spend even when the full cohort value clears it.</p>' +
             table(["Monthly spend", "Purchases", "Month one cash", "Month one return", "Full cohort value", "Full return"],
                   D3.CASHFLOW_V2, "num") + "</section>")

    o.append('<section class="blk">' + head("The thirty day test plan.") + '<div class="plan">')
    win = None
    for w, t, d, out in D2.TEST_PLAN:
        if w != win:
            win = w
            o.append(f'<div class="plan-w">{E(w)}</div>')
        o.append(f'<div class="plan-i"><h4>{E(t)}</h4><p>{E(d)}</p>'
                 f'<div class="plan-o"><b>Done means</b> {E(out)}</div></div>')
    o.append("</div></section>")

    o.append('<section class="blk">' + head("Blockers, in the order they must clear.") + '<div class="blockers">')
    for sev, t, d, imp, src in D2.BLOCKERS_CEO:
        o.append(f'<div class="bl bl-{sev.lower()}"><div class="bl-sev">{E(sev)}</div>'
                 f'<h4>{E(t)}</h4><p>{E(d)}</p><p class="bl-imp">{E(imp)}</p>{srclinks(src)}</div>')
    o.append("</div></section>")

    o.append('<section class="decide">' + f'<h2>{E(D3.CEO_DECISION["head"])}</h2><ol>' +
             "".join(f"<li>{E(x)}</li>" for x in D3.CEO_DECISION["lines"]) + "</ol></section>")
    o.append("</div>")
    return "".join(o)

# ============================================================ SHELL
TABS = [("golive", "Go live today"), ("meta", "Meta and Instagram"), ("leads", "Buy high intent leads"),
        ("infl", "Influencers"), ("email", "Email funnel"), ("ceo", "CEO forecast")]

LOGO = ('<svg class="logo" viewBox="0 0 40 40" fill="none" aria-label="Delta Force mark">'
        '<path d="M20 4 L36 32 H4 Z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>'
        '<path d="M20 15 L27.5 28 H12.5 Z" fill="currentColor"/></svg>')

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--ink:#05060A;--navy:#0A1226;--navy2:#0D1830;--blue:#006EFF;--blue2:#5EB6FF;
--white:#FFFFFF;--paper:#F4F6FA;--line:rgba(255,255,255,.13);--linek:rgba(5,6,10,.12);
--txt:#EAF0FA;--txt2:#B7C4DA;--dark-txt:#131826;--dark-txt2:#3E4A62;
--red:#FF4D4D;--amber:#FFB020;--green:#22C98A;
--r:18px;
}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--ink);color:var(--txt);
font-family:'Hanken Grotesk',system-ui,sans-serif;font-size:18px;line-height:1.62;
font-weight:400;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4{font-family:'Fraunces','Instrument Serif',Georgia,serif;font-weight:600;line-height:1.05;letter-spacing:-.015em}
a{color:var(--blue2);text-decoration:none;border-bottom:1px solid rgba(94,182,255,.4)}
a:hover{color:var(--white);border-bottom-color:var(--white)}
img{max-width:100%;display:block}
.wrap{max-width:1320px;margin:0 auto;padding:0 40px}

/* ---- masthead ---- */
.mast{position:relative;overflow:hidden;background:
radial-gradient(1100px 620px at 15% -10%,rgba(0,110,255,.42),transparent 62%),
radial-gradient(820px 520px at 92% 8%,rgba(94,182,255,.20),transparent 60%),
linear-gradient(180deg,#05060A 0%,#0A1226 100%);
border-bottom:1px solid var(--line)}
.mast-in{padding:72px 0 60px}
.brandrow{display:flex;align-items:center;gap:14px;margin-bottom:44px;color:var(--blue2)}
.logo{width:38px;height:38px;flex:none}
.brandtxt{font-size:17px;letter-spacing:.02em;color:var(--txt2)}
.brandtxt b{color:var(--white);font-weight:600}
.mast h1{font-size:clamp(44px,7.6vw,90px);color:#fff;max-width:17ch;letter-spacing:-.03em}
.mast .sub{margin-top:26px;font-size:clamp(19px,1.5vw,23px);color:var(--txt2);max-width:62ch}
.mastmeta{margin-top:38px;display:flex;flex-wrap:wrap;gap:12px}
.mm{background:rgba(255,255,255,.06);border:1px solid var(--line);border-radius:100px;
padding:9px 18px;font-size:16px;color:var(--txt)}
.mm b{color:var(--blue2);font-weight:600}

/* ---- tabs ---- */
.tabbar{position:sticky;top:0;z-index:60;background:rgba(5,6,10,.9);
backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}
.tabs{display:flex;gap:6px;overflow-x:auto;padding:12px 0;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tb{flex:none;background:transparent;border:1px solid transparent;color:var(--txt2);
font-family:inherit;font-size:17px;font-weight:500;padding:11px 20px;border-radius:100px;
cursor:pointer;white-space:nowrap;transition:.18s}
.tb:hover{color:#fff;background:rgba(255,255,255,.07)}
.tb[aria-selected="true"]{background:var(--blue);color:#fff;
box-shadow:0 8px 26px rgba(0,110,255,.42),0 2px 6px rgba(0,0,0,.4)}

/* ---- sections ---- */
main{padding-bottom:120px}
.hero{padding:78px 0 10px}
.h1{font-size:clamp(36px,5.4vw,72px);color:#fff;max-width:20ch;letter-spacing:-.028em}
.lede{margin-top:22px;font-size:clamp(18px,1.35vw,21px);color:var(--txt2);max-width:70ch}
.hd{margin-bottom:26px}
.kick{font-size:17px;color:var(--blue2);margin-bottom:10px;font-weight:600}
.hd h2{font-size:clamp(28px,3.4vw,46px);color:#fff;max-width:26ch}
.sub{font-size:clamp(22px,2vw,30px);color:#fff;margin:44px 0 16px}
.blk{padding:64px 0;border-top:1px solid var(--line)}
.close{margin-top:22px;font-size:19px;color:var(--txt2);max-width:82ch}
.lines{margin-top:26px;display:grid;gap:18px;max-width:96ch}
.ln{font-size:19px;color:var(--txt)}
.srcs{display:inline-flex;flex-wrap:wrap;gap:10px;margin-left:6px}
.srcs a{font-size:16px;color:var(--blue2)}

/* ---- chips ---- */
.chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:34px}
.chip{background:linear-gradient(160deg,rgba(255,255,255,.075),rgba(255,255,255,.025));
border:1px solid var(--line);border-radius:var(--r);padding:24px 22px;
box-shadow:0 20px 40px -24px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.07)}
.chip-v{font-family:'Fraunces',Georgia,serif;font-size:clamp(30px,3.2vw,44px);
color:#fff;line-height:1;letter-spacing:-.03em}
.chip-l{margin-top:12px;font-size:17px;color:var(--blue2);font-weight:600;line-height:1.35}
.chip-n{margin-top:8px;font-size:16px;color:var(--txt2);line-height:1.45}

/* ---- red alert ---- */
.alert{margin:56px 0 12px;background:
radial-gradient(700px 320px at 8% 0%,rgba(255,77,77,.20),transparent 62%),
linear-gradient(160deg,rgba(255,77,77,.10),rgba(5,6,10,.5));
border:1px solid rgba(255,77,77,.45);border-radius:24px;padding:40px;
box-shadow:0 40px 80px -50px rgba(255,77,77,.6)}
.alert-h{display:flex;flex-direction:column;gap:16px;margin-bottom:30px}
.alert-tag{align-self:flex-start;background:var(--red);color:#0b0000;font-weight:800;
font-size:16px;letter-spacing:.08em;padding:7px 16px;border-radius:8px}
.alert-h h2{font-size:clamp(26px,3.1vw,42px);color:#fff;max-width:24ch}
.alert-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px}
.alert-card{background:rgba(5,6,10,.55);border:1px solid rgba(255,77,77,.3);
border-radius:var(--r);padding:26px}
.alert-n{font-family:'Fraunces',Georgia,serif;font-size:26px;color:var(--red);margin-bottom:10px}
.alert-card h3{font-size:22px;color:#fff;margin-bottom:12px}
.alert-card p{font-size:17px;color:var(--txt2);margin-bottom:14px}

/* ---- phase rule ---- */
.phase-rule{display:flex;align-items:center;gap:20px;margin:76px 0 34px}
.phase-rule span{font-size:17px;font-weight:700;color:var(--blue2);letter-spacing:.06em;white-space:nowrap}
.phase-rule:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,rgba(0,110,255,.6),transparent)}

/* ---- campaign card ---- */
.camp,.vend,.infl,.mail{background:linear-gradient(165deg,#0A1226 0%,#070B16 100%);
border:1px solid var(--line);border-radius:24px;padding:38px;margin-bottom:32px;
box-shadow:0 50px 90px -60px rgba(0,0,0,.95),inset 0 1px 0 rgba(255,255,255,.06)}
.camp-top,.vend-top,.infl-top{display:flex;gap:22px;align-items:flex-start;flex-wrap:wrap;
padding-bottom:26px;border-bottom:1px solid var(--line)}
.camp-code,.vend-rank,.infl-n{font-family:'Fraunces',Georgia,serif;font-size:34px;color:var(--blue);
background:rgba(0,110,255,.13);border-radius:14px;padding:8px 16px;flex:none;line-height:1.1}
.camp-name,.vend-top h3,.infl-top h3{font-size:clamp(24px,2.4vw,34px);color:#fff}
.camp-obj,.vend-kind,.infl-role{margin-top:8px;font-size:17px;color:var(--txt2);max-width:60ch}
.camp-budget{margin-left:auto;text-align:right}
.bv{font-family:'Fraunces',Georgia,serif;font-size:34px;color:var(--blue2);line-height:1}
.bl{font-size:16px;color:var(--txt2);margin-top:8px;max-width:26ch}
.camp-budget .bl{margin-left:auto}
.spec{display:grid;gap:0;margin:8px 0 8px}
.sp{display:grid;grid-template-columns:230px 1fr;gap:26px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.07)}
.sp-k{font-size:17px;color:var(--blue2);font-weight:600}
.sp-v{font-size:18px;color:var(--txt);overflow-wrap:anywhere}
.xtra{display:inline-block;margin-right:12px;font-size:16px}
.cr-head{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap;margin:30px 0 18px}
.cr-head h4{font-size:24px;color:#fff}
.repo{font-size:16px}
.cr-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:18px}
.cr-box{width:100%;background:#04070E;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.cr-box img{width:100%;height:100%;object-fit:cover}
.cr figcaption,.bk figcaption{margin-top:12px;font-size:16px;color:var(--txt2);line-height:1.4}
.cr figcaption b{display:block;color:var(--txt);font-weight:600;font-size:17px;margin-bottom:3px}
.bank{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:20px;margin-top:8px}
.why{margin-top:28px;padding:22px 24px;background:rgba(0,110,255,.09);
border-left:3px solid var(--blue);border-radius:0 14px 14px 0;font-size:18px;color:var(--txt)}
.why b{color:var(--blue2)}

/* ---- copy boxes ---- */
.copyset{display:grid;gap:16px;margin-top:30px}
.cbx{background:#04060C;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.cbx-h{display:flex;align-items:center;justify-content:space-between;gap:16px;
padding:12px 18px;background:rgba(255,255,255,.045);border-bottom:1px solid var(--line)}
.cbx-l{font-size:16px;color:var(--blue2);font-weight:600}
.cpy{background:var(--blue);color:#fff;border:0;border-radius:8px;padding:8px 18px;
font-family:inherit;font-size:15px;font-weight:600;cursor:pointer;transition:.16s}
.cpy:hover{background:var(--blue2);color:#04060C}
.cpy.done{background:var(--green);color:#04170F}
.cbx-b{padding:20px 22px;font-family:inherit;font-size:17px;line-height:1.65;
color:var(--txt);white-space:pre-wrap;overflow-wrap:anywhere;max-height:340px;overflow-y:auto}

/* ---- tables ---- */
.twrap{overflow-x:auto;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.028)}
.tbl{width:100%;border-collapse:collapse;font-size:17px;min-width:640px}
.tbl th{text-align:left;padding:16px 18px;font-size:16px;font-weight:700;color:var(--blue2);
background:rgba(0,110,255,.10);border-bottom:1px solid var(--line);white-space:nowrap}
.tbl td{padding:16px 18px;border-bottom:1px solid rgba(255,255,255,.07);color:var(--txt);vertical-align:top}
.tbl tbody tr:last-child td{border-bottom:0}
.tbl tr.hi td{background:rgba(0,110,255,.14);color:#fff;font-weight:600}
.tbl.num td{white-space:nowrap}
.tbl.kv td:first-child,.tbl.kv4 td:first-child{color:var(--blue2);font-weight:600}
.tbl.cmp td:first-child{color:var(--blue2);font-weight:600;width:26%}
.tbl.sens th[scope=row]{background:rgba(0,110,255,.10);font-size:20px;color:#fff;
font-family:'Fraunces',Georgia,serif}
.cell{padding:16px 18px}
.cell-v{font-family:'Fraunces',Georgia,serif;font-size:26px;line-height:1}
.cell-n{font-size:16px;color:var(--txt2);margin-top:8px}
.cell.ok{background:rgba(34,201,138,.11)}
.cell.ok .cell-v{color:#5CE8B4}
.cell.bad{background:rgba(255,77,77,.11)}
.cell.bad .cell-v{color:#FF8A8A}

/* ---- two lines ---- */
.twoline{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:34px}
.lane{border-radius:24px;padding:34px;border:1px solid var(--line);
box-shadow:0 50px 90px -60px rgba(0,0,0,.95)}
.lane-a{background:radial-gradient(600px 300px at 0% 0%,rgba(0,110,255,.20),transparent 60%),linear-gradient(165deg,#0A1226,#070B16)}
.lane-b{background:radial-gradient(600px 300px at 100% 0%,rgba(255,77,77,.16),transparent 60%),linear-gradient(165deg,#12101A,#08060B)}
.lane-tag{font-size:16px;font-weight:800;letter-spacing:.08em;color:#fff;
background:var(--blue);display:inline-block;padding:6px 14px;border-radius:8px}
.lane-b .lane-tag{background:var(--red);color:#160000}
.lane-t{font-size:clamp(26px,2.6vw,36px);color:#fff;margin-top:18px}
.lane-state{margin-top:10px;font-size:18px;color:var(--txt2)}
.lane-spec{margin-top:24px;display:grid;grid-template-columns:auto;gap:0}
.lane-spec dt{font-size:16px;color:var(--blue2);font-weight:700;padding-top:14px}
.lane-b .lane-spec dt{color:#FFA8A8}
.lane-spec dd{font-size:18px;color:var(--txt);padding:4px 0 14px;border-bottom:1px solid rgba(255,255,255,.07)}
.lane-math{margin-top:22px;padding:20px 22px;background:rgba(255,255,255,.05);border-radius:14px}
.lane-math b{color:var(--blue2);font-size:17px}
.lane-b .lane-math b{color:#FFA8A8}
.lane-math ul{margin:12px 0 0;padding-left:20px;display:grid;gap:9px}
.lane-math li{font-size:17px;color:var(--txt2)}
.lane-math li b{color:var(--txt);font-weight:600}
.lane-v{margin-top:22px;font-size:19px;color:#fff}

/* ---- decision ---- */
.decide{margin:64px 0;background:linear-gradient(140deg,var(--blue) 0%,#0038A8 100%);
border-radius:24px;padding:48px;box-shadow:0 50px 90px -50px rgba(0,110,255,.7)}
.decide h2{font-size:clamp(28px,3.4vw,46px);color:#fff;margin-bottom:26px}
.decide ol{margin:0;padding-left:26px;display:grid;gap:16px}
.decide li{font-size:clamp(18px,1.4vw,21px);color:#EAF2FF;max-width:80ch}

/* ---- vendors, influencers ---- */
.vend-bk{background:linear-gradient(165deg,#0B0F1A 0%,#06080F 100%)}
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:38px}
.legend div{font-size:17px;color:var(--txt2);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.legend b{color:#fff}
.badge{margin-left:auto;font-size:16px;font-weight:800;letter-spacing:.06em;padding:8px 16px;border-radius:9px;flex:none}
.b-green{background:rgba(34,201,138,.18);color:#5CE8B4;border:1px solid rgba(34,201,138,.45)}
.b-amber{background:rgba(255,176,32,.16);color:#FFCB63;border:1px solid rgba(255,176,32,.45)}
.b-red{background:rgba(255,77,77,.16);color:#FF9C9C;border:1px solid rgba(255,77,77,.45)}
.counts{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0 4px}
.cnt{display:flex;flex-direction:column;gap:4px;background:rgba(255,255,255,.055);
border:1px solid var(--line);border-radius:12px;padding:14px 20px;min-width:118px}
.cnt-v{font-family:'Fraunces',Georgia,serif;font-size:26px;color:#fff;line-height:1}
.cnt-l{font-size:16px;color:var(--txt2)}

/* ---- email frames ---- */
.mails{display:grid;gap:32px}
.mail-stage{font-size:18px;color:var(--blue2);font-weight:700;margin-bottom:18px}
.mail-frame{background:var(--white);border-radius:16px;overflow:hidden;
box-shadow:0 40px 80px -40px rgba(0,0,0,.9)}
.mail-hdr{padding:22px 30px;background:var(--paper);border-bottom:1px solid var(--linek)}
.mrow{display:grid;grid-template-columns:110px 1fr;gap:16px;padding:6px 0}
.mk{font-size:16px;color:#5A6a86;font-weight:600}
.mv{font-size:17px;color:var(--dark-txt);overflow-wrap:anywhere}
.msubj{font-family:'Fraunces',Georgia,serif;font-size:22px;font-weight:600}
.mail-body{padding:34px 40px}
.mail-body p{font-size:18px;line-height:1.72;color:#1B2233;margin-bottom:18px;max-width:70ch}
.mail-body p:last-child{margin-bottom:0}

/* ---- plan, blockers ---- */
.plan{display:grid;gap:18px;margin-top:8px}
.plan-w{font-size:18px;font-weight:700;color:var(--blue2);margin-top:22px}
.plan-i{background:rgba(255,255,255,.045);border:1px solid var(--line);border-radius:16px;padding:26px}
.plan-i h4{font-size:23px;color:#fff;margin-bottom:10px}
.plan-i p{font-size:18px;color:var(--txt2)}
.plan-o{margin-top:14px;font-size:17px;color:var(--txt)}
.plan-o b{color:var(--blue2)}
.blockers{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:20px;margin-top:8px}
.bl{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:16px;padding:26px}
.bl-critical{border-color:rgba(255,77,77,.5);background:rgba(255,77,77,.07)}
.bl-high{border-color:rgba(255,176,32,.45);background:rgba(255,176,32,.06)}
.bl-sev{font-size:16px;font-weight:800;letter-spacing:.06em;margin-bottom:12px;color:var(--blue2)}
.bl-critical .bl-sev{color:#FF9C9C}
.bl-high .bl-sev{color:#FFCB63}
.bl h4{font-size:22px;color:#fff;margin-bottom:10px}
.bl p{font-size:17px;color:var(--txt2);margin-bottom:12px}
.bl-imp{color:var(--txt)}

/* ---- footer ---- */
footer{border-top:1px solid var(--line);padding:52px 0;background:linear-gradient(180deg,#05060A,#0A1226)}
footer p{font-size:17px;color:var(--txt2);max-width:80ch}
footer b{color:#fff}

@media(max-width:1024px){
.twoline{grid-template-columns:1fr}
.sp{grid-template-columns:1fr;gap:6px}
}
@media(max-width:720px){
.wrap{padding:0 20px}
body{font-size:17px}
.mast-in{padding:46px 0 40px}
.hero{padding:48px 0 6px}
.blk{padding:44px 0}
.camp,.vend,.infl,.lane,.alert{padding:24px}
.decide{padding:30px}
.camp-budget{margin-left:0;text-align:left}
.camp-budget .bl{margin-left:0}
.camp-code,.vend-rank,.infl-n{font-size:26px}
.badge{margin-left:0}
.mail-body{padding:24px 22px}
.mail-hdr{padding:18px 22px}
.mrow{grid-template-columns:1fr;gap:2px}
.cbx-b{padding:16px 18px}
.chips{grid-template-columns:1fr 1fr;gap:12px}
.chip{padding:18px 16px}
.cr-grid{grid-template-columns:1fr 1fr}
.bank{grid-template-columns:1fr 1fr}
}
@media(max-width:420px){.chips{grid-template-columns:1fr}}
"""

JS = r"""
(function(){
 var tabs=[].slice.call(document.querySelectorAll('.tb'));
 var panes=[].slice.call(document.querySelectorAll('.tabpane'));
 function go(id){
  tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.p===id?'true':'false');});
  panes.forEach(function(p){p.hidden=(p.id!=='p-'+id);});
  window.scrollTo({top:0,behavior:'instant'});
  if(history.replaceState)history.replaceState(null,'','#'+id);
 }
 tabs.forEach(function(t){t.addEventListener('click',function(){go(t.dataset.p);});});
 var h=(location.hash||'').replace('#','');
 if(h&&document.getElementById('p-'+h))go(h);
 document.addEventListener('click',function(e){
  var b=e.target.closest('.cpy'); if(!b)return;
  var el=document.getElementById(b.dataset.t); if(!el)return;
  var txt=el.textContent;
  function ok(){b.textContent='Copied';b.classList.add('done');
   setTimeout(function(){b.textContent='Copy';b.classList.remove('done');},1600);}
  if(navigator.clipboard&&navigator.clipboard.writeText){
   navigator.clipboard.writeText(txt).then(ok,fb);
  }else{fb();}
  function fb(){var ta=document.createElement('textarea');ta.value=txt;
   ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);
   ta.select();try{document.execCommand('copy');ok();}catch(err){}
   document.body.removeChild(ta);}
 });
})();
"""

def render():
    tb = "".join(
        f'<button class="tb" role="tab" data-p="{k}" aria-selected="{"true" if i==0 else "false"}">{E(v)}</button>'
        for i, (k, v) in enumerate(TABS))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>E-COMMERCE DELTA FORCE GO LIVE . Longevity Life Academy</title>
<meta name="description" content="Activation hub for Longevity Life Academy. Campaigns, budgets, creatives, copy, lead vendors, influencers, email funnel and forecast.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' fill='%2305060A'/%3E%3Cpath d='M20 8 L33 30 H7 Z' fill='none' stroke='%23006EFF' stroke-width='3'/%3E%3C/svg%3E">
<style>{CSS}</style>
</head>
<body>
<header class="mast"><div class="wrap mast-in">
 <div class="brandrow">{LOGO}<div class="brandtxt"><b>Gita Agency</b> for Longevity Life Academy by eTeacher Group</div></div>
 <h1>E-commerce delta force. Go live.</h1>
 <p class="sub">Everything needed to switch spend on this week, in the order it has to happen. Current spend is $20,000 a month, and it is trapped in one line because the second line has no checkout to point at.</p>
 <div class="mastmeta">
  <div class="mm"><b>The Longevity Blueprint</b> 18 weeks, 18 live 50 minute sessions</div>
  <div class="mm"><b>Cohorts of 8 to 15</b> six pillars, Abbott Lingo CGM before lesson 5</div>
  <div class="mm"><b>$1,249 upfront</b> reduced from $1,800, or five payments of $289</div>
  <div class="mm"><b>Buyer</b> 45 plus, 54.5 percent female</div>
 </div>
</div></header>

<nav class="tabbar"><div class="wrap"><div class="tabs" role="tablist">{tb}</div></div></nav>

<main class="wrap">
{tab1()}
{tab2()}
{tab3()}
{tab4()}
{tab5()}
{tab6()}
</main>

<footer><div class="wrap">
 <p><b>Sources.</b> Pricing, curriculum and terms from <a href="https://longevitylifeacademy.com/pricing.html" target="_blank" rel="noopener">longevitylifeacademy.com/pricing.html</a> and <a href="https://www.longevitylifeacademy.com/terms.html" target="_blank" rel="noopener">terms.html</a>. Audience composition from <a href="https://www.similarweb.com/website/peterattiamd.com/" target="_blank" rel="noopener">Similarweb, peterattiamd.com, June 2026</a>. Meta delivery mechanics from the <a href="https://www.facebook.com/business/help/112167992830700" target="_blank" rel="noopener">Meta Business Help Center</a>. Benchmarks from <a href="https://www.wordstream.com/blog/facebook-ads-cost" target="_blank" rel="noopener">WordStream</a>, <a href="https://www.triplewhale.com/blog/facebook-ads-benchmarks" target="_blank" rel="noopener">Triple Whale</a> and <a href="https://www.sparkugc.com/resources/meta-ads-benchmarks-by-business-type-2026" target="_blank" rel="noopener">Spark UGC</a>. Creative served from the client GitHub organisation.</p>
 <p style="margin-top:18px">Prepared by Gita Agency. Every figure on this page traces to a named source file or a linked public source.</p>
</div></footer>
<script>{JS}</script>
</body></html>"""

if __name__ == "__main__":
    out = render()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("bytes", len(out))
