# -*- coding: utf-8 -*-
"""V2 renderers for the leads tab, the influencer tab and the creative gallery.
Uses the existing design system only. No em dashes, no en dashes, no exclamation marks."""
import re
import v2vend as V
import v2infl as I
import v2creative as C
from parse_v2 import load_influencers, md, plain, clean

MASTER, SHORTLIST, NOTES = load_influencers()
BYNUM = {m["n"]: m for m in MASTER}

CSS_V2 = r"""
/* ---- v2 additions, same tokens ---- */
.callout{margin:34px 0;padding:32px 34px;border-radius:22px;
background:radial-gradient(700px 320px at 6% 0%,rgba(0,110,255,.22),transparent 62%),linear-gradient(160deg,rgba(0,110,255,.10),rgba(5,6,10,.6));
border:1px solid rgba(0,110,255,.42);box-shadow:0 40px 80px -55px rgba(0,110,255,.7)}
.callout .ctag{display:inline-block;background:var(--blue);color:#fff;font-weight:700;font-size:16px;
letter-spacing:.06em;padding:7px 16px;border-radius:8px;margin-bottom:18px}
.callout h3{font-size:clamp(24px,2.7vw,36px);color:#fff;max-width:30ch;margin-bottom:18px}
.callout p{font-size:19px;color:var(--txt);max-width:88ch;margin-bottom:14px}
.callout p:last-child{margin-bottom:0}
.readx{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin-top:26px}
.readx div{background:rgba(5,6,10,.5);border:1px solid var(--line);border-radius:16px;padding:24px}
.readx b{display:block;color:var(--blue2);font-size:18px;margin-bottom:10px}
.readx span{display:block;font-size:17px;color:var(--txt);margin-bottom:10px}
.readx i{display:block;font-style:normal;font-size:17px;color:var(--txt2)}
.mathbox{margin-top:26px;padding:24px 26px;background:rgba(255,255,255,.05);border-radius:16px;border-left:3px solid var(--blue)}
.mathbox b{color:var(--blue2);font-size:17px;display:block;margin-bottom:12px}
.mathbox ul{margin:0;padding:0;list-style:none;display:grid;gap:10px}
.mathbox li{font-size:18px;color:var(--txt)}
.vscore{margin-left:auto;text-align:right}
.vscore .bv{font-family:'Fraunces',Georgia,serif;font-size:38px;color:var(--blue2);line-height:1}
.vscore .bl{font-size:16px;color:var(--txt2);margin-top:6px}
.quotes{display:grid;gap:20px;margin-top:8px}
.qt{background:rgba(255,255,255,.045);border:1px solid var(--line);border-radius:18px;padding:26px 28px}
.qt h4{font-size:21px;color:#fff;margin-bottom:14px}
.qt blockquote{font-size:19px;color:var(--txt);border-left:3px solid var(--blue);padding-left:20px;margin-bottom:14px}
.qt .qsrc{font-size:16px}
.iogrid{display:grid;gap:16px;margin-top:8px}
.gal-nav{display:flex;flex-wrap:wrap;gap:10px;margin:28px 0 8px}
.gal-nav a{font-size:16px;border:1px solid var(--line);border-bottom-color:var(--line);border-radius:100px;padding:9px 16px;color:var(--txt2);background:rgba(255,255,255,.05)}
.gal-nav a:hover{color:#fff;border-color:var(--blue)}
.gal-grp{padding-top:46px}
.gal-grp h3{font-size:clamp(23px,2.3vw,32px);color:#fff}
.gal-meta{margin-top:8px;font-size:17px;color:var(--txt2)}
.gal-ratio{font-size:17px;font-weight:700;color:var(--blue2);margin:26px 0 14px}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}
.gal figure{min-width:0}
.gal figcaption{margin-top:10px;font-size:16px;color:var(--txt2);overflow-wrap:anywhere}
.gal figcaption b{display:block;color:var(--txt);font-weight:600;font-size:17px}
.mv-tag{display:inline-block;margin-top:6px;font-size:15px;color:#04070E;background:var(--blue2);border-radius:6px;padding:3px 10px;font-weight:700}
.mtbl th.srt{cursor:pointer;user-select:none}
.mtbl th.srt:hover{color:#fff}
.scr{display:inline-block;font-size:15px;font-weight:800;letter-spacing:.05em;padding:5px 12px;border-radius:7px}
.s-green{background:rgba(34,201,138,.18);color:#5CE8B4;border:1px solid rgba(34,201,138,.45)}
.s-amber{background:rgba(255,176,32,.16);color:#FFCB63;border:1px solid rgba(255,176,32,.45)}
.s-red{background:rgba(255,77,77,.16);color:#FF9C9C;border:1px solid rgba(255,77,77,.45)}
.shortl{display:grid;gap:16px;margin-top:8px}
.sl{display:grid;grid-template-columns:64px 1fr;gap:22px;background:linear-gradient(165deg,#0A1226,#070B16);
border:1px solid var(--line);border-radius:18px;padding:24px 26px}
.sl-n{font-family:'Fraunces',Georgia,serif;font-size:32px;color:var(--blue);background:rgba(0,110,255,.13);
border-radius:12px;display:flex;align-items:center;justify-content:center;height:52px}
.sl h4{font-size:23px;color:#fff;margin-bottom:8px}
.sl p{font-size:18px;color:var(--txt2)}
.sl .slmeta{margin-top:10px;font-size:17px;color:var(--txt)}
.note{background:rgba(255,255,255,.045);border:1px solid var(--line);border-radius:18px;padding:26px 28px;font-size:18px;color:var(--txt);margin-top:18px}
@media(max-width:720px){
.gal{grid-template-columns:1fr 1fr}
.sl{grid-template-columns:1fr}
.callout{padding:24px}
}
"""

JS_V2 = r"""
(function(){
 var t=document.getElementById('infl-master'); if(!t)return;
 var hs=[].slice.call(t.querySelectorAll('th.srt'));
 hs.forEach(function(h,i){
  h.addEventListener('click',function(){
   var body=t.tBodies[0];
   var rows=[].slice.call(body.rows);
   var dir=h.dataset.dir==='asc'?-1:1;
   hs.forEach(function(x){delete x.dataset.dir;});
   h.dataset.dir=dir===1?'asc':'desc';
   var num=h.dataset.num==='1';
   rows.sort(function(a,b){
    var x=a.cells[i].dataset.v!==undefined?a.cells[i].dataset.v:a.cells[i].textContent;
    var y=b.cells[i].dataset.v!==undefined?b.cells[i].dataset.v:b.cells[i].textContent;
    if(num){return (parseFloat(x)-parseFloat(y))*dir;}
    return x.localeCompare(y)*dir;
   });
   rows.forEach(function(r){body.appendChild(r);});
  });
 });
})();
"""


def build_tabs(E, chips, head, table, copybox, srclinks):
    """Returns (tab_leads_html, tab_infl_html, gallery_html, counts)."""

    # ---------------------------------------------------------------- LEADS
    def leads():
        o = ['<div class="tabpane" id="p-leads" hidden>']
        o.append('<section class="hero"><h1 class="h1">Buy calls, not forms.</h1>'
                 '<p class="lede">Thirty five vendors were read against the five factors the client is judging on. '
                 'Five are scored in full, with the arithmetic visible, and every price on this tab names the vertical it is read across from.</p>')
        o.append(chips(V.HERO_CHIPS))
        o.append("</section>")

        # headline callout
        h = V.HEADLINE
        o.append(f'<section class="callout"><span class="ctag">{E(h["tag"])}</span><h3>{E(h["title"])}</h3>')
        for p in h["body"]:
            o.append(f"<p>{E(p)}</p>")
        o.append('<div class="readx">')
        for a, b, c in h["reads"]:
            o.append(f"<div><b>{E(a)}</b><span>{E(b)}</span><i>{E(c)}</i></div>")
        o.append("</div></section>")

        # score table
        o.append('<section class="blk">' + head("The corrected ranking, with the arithmetic shown.",
                                                "SECTION A, SCORED ON THE FIVE FACTORS"))
        o.append(table(V.SCORE_HEADERS, [list(r) + [r[0] == "1"] for r in V.SCORE_ROWS], "num", hi_idx=10))
        o.append('<div class="mathbox"><b>Arithmetic, so it can be rechecked</b><ul>')
        for m in V.SCORE_MATH:
            o.append(f"<li>{E(m)}</li>")
        o.append("</ul></div>")
        o.append(f'<p class="close">{E(V.SCORE_NOTE)}</p></section>')

        # co-reg
        o.append(f'<section class="callout"><span class="ctag">DISQUALIFIED</span><h3>{E(V.COREG["title"])}</h3>'
                 f'<p>{E(V.COREG["body"])}</p><p>{srclinks([V.COREG["src"]])}</p></section>')

        # vendor cards
        FACTS = [("1. What kind of lead, the exact mechanism", "f1"),
                 ("2. How intent is verified", "f2"),
                 ("3. B2C strength in this space", "f3"),
                 ("4. Real price, and what it is read across from", "f4"),
                 ("5. Speed and access", "f5")]
        o.append('<div class="phase-rule"><span>THE FIVE, IN RANK ORDER</span></div>')
        for v in V.VENDORS:
            o.append('<article class="vend">')
            o.append(f'<div class="vend-top"><div class="vend-rank">{E(v["rank"])}</div>'
                     f'<div><h3>{E(v["name"])}</h3><div class="vend-kind">{E(v["kind"])}</div></div>'
                     f'<div class="vscore"><div class="bv">{E(v["score"])}</div>'
                     f'<div class="bl">final score out of 60</div></div></div>')
            o.append('<div class="spec">')
            for label, key in FACTS:
                txt, srcs = v[key]
                o.append(f'<div class="sp"><div class="sp-k">{E(label)}</div>'
                         f'<div class="sp-v">{E(txt)} {srclinks(srcs)}</div></div>')
            routes = " ".join(f'<a class="xtra" href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a>'
                              for t, u in v["contacts"])
            o.append(f'<div class="sp"><div class="sp-k">Contact routes</div><div class="sp-v">{routes}</div></div>')
            o.append("</div>")
            o.append(f'<div class="why"><b>Verdict.</b> {E(v["verdict"])}</div>')
            o.append('<div class="copyset">')
            o.append(copybox(v["subject"], "Subject line"))
            o.append(copybox(v["email"], "Outreach email, written for this vendor's actual mechanism"))
            o.append("</div></article>")

        # coverage
        o.append('<section class="blk">' + head("The other thirty, and why they are not in the five.",
                                                "SECTION C, FULL COVERAGE") +
                 table(V.COVERAGE_HEADERS, V.COVERAGE_ROWS, "kv4") + "</section>")

        # price table
        o.append('<section class="blk">' + head("Twenty two sourced prices, because the category has none of its own.",
                                                "SECTION D, MARKET PRICE REFERENCE"))
        rows = []
        for prod, price, cr, close, sname, surl in V.PRICE_ROWS:
            rows.append((prod, price, cr, close,
                         f'<a href="{E(surl)}" target="_blank" rel="noopener">{E(sname)}</a>'))
        o.append('<div class="twrap"><table class="tbl kv4"><thead><tr>'
                 + "".join(f"<th>{E(x)}</th>" for x in V.PRICE_HEADERS) + "</tr></thead><tbody>")
        for r in rows:
            o.append("<tr>" + "".join(f"<td>{c if c.startswith('<a') else E(c)}</td>" for c in r) + "</tr>")
        o.append("</tbody></table></div></section>")

        # duration doctrine
        o.append('<section class="blk">' + head("Billable duration, the single most actionable specification."))
        o.append('<div class="twrap"><table class="tbl kv4"><thead><tr><th>Source</th><th>Published guidance</th></tr></thead><tbody>')
        for name, txt, url in V.DURATION:
            o.append(f'<tr><td><a href="{E(url)}" target="_blank" rel="noopener">{E(name)}</a></td><td>{E(txt)}</td></tr>')
        o.append("</tbody></table></div>")
        o.append(f'<div class="why"><b>Specification.</b> {E(V.DURATION_SPEC)}</div></section>')

        # returns
        o.append('<section class="blk">' + head("What a fair return policy looks like, sourced."))
        o.append('<div class="twrap"><table class="tbl kv4"><thead><tr><th>Benchmark</th><th>Published text</th><th>Source</th></tr></thead><tbody>')
        for b, t, s, u in V.RETURNS:
            o.append(f'<tr><td><b>{E(b)}</b></td><td>{E(t)}</td>'
                     f'<td><a href="{E(u)}" target="_blank" rel="noopener">{E(s)}</a></td></tr>')
        o.append("</tbody></table></div>")
        t, s, u = V.EXCLUSIVE_TRAP
        o.append(f'<div class="why"><b>The definitional trap.</b> {E(t)} {srclinks([(s, u)])}</div></section>')

        # unit economics
        o.append('<section class="blk">' + head("At a $1,249 ticket, $250 per appointment is the exact break even at a 20 percent close rate.",
                                                "SECTION G, UNIT ECONOMICS"))
        o.append(f'<p class="close">{E(V.WHY_FAILED)} {srclinks(V.WHY_SRC)}</p>')
        o.append(table(V.ECON_HEADERS, [list(r) for r in V.ECON_ROWS], "num", hi_idx=5))
        o.append('<div class="mathbox"><b>The arithmetic</b><ul>')
        for m in V.ECON_MATH:
            o.append(f"<li>{E(m)}</li>")
        o.append("</ul></div></section>")

        # test plan
        o.append('<section class="blk">' + head("The thirty day test, four parallel cells, fifteen thousand dollars.") +
                 table(V.TEST_HEADERS, V.TEST_ROWS, "kv4") +
                 f'<p class="close">{E(V.TEST_NOTE)}</p></section>')

        # IO clauses
        o.append('<section class="blk">' + head("Twelve clauses to paste into every insertion order.",
                                                "SECTION G4, COPY VERBATIM"))
        o.append('<div class="iogrid">')
        for i, cl in enumerate(V.IO_CLAUSES, 1):
            o.append(copybox(cl, f"Clause {i:02d}"))
        o.append("</div>")
        o.append('<p class="close">Sources for the clause wording. ' + srclinks(V.IO_SOURCES) + "</p></section>")

        # prequal
        o.append('<section class="blk">' + head("One question that pre qualifies every vendor call."))
        o.append(copybox(V.PREQUAL, "Ask this first"))
        o.append(f'<p class="close">{E(V.PREQUAL_NOTE)}</p></section>')

        # forum
        o.append('<section class="blk">' + head("What operators actually say, from 134 quotable URLs.",
                                                "SECTION E, FORUM AND OPERATOR EVIDENCE"))
        o.append(chips(V.FORUM_STATS))
        o.append('<div class="twrap" style="margin-top:30px"><table class="tbl kv4"><thead><tr><th>Theme</th><th>Sources</th></tr></thead><tbody>')
        for a, b in V.FORUM_THEMES:
            o.append(f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>")
        o.append("</tbody></table></div>")
        o.append('<div class="quotes" style="margin-top:30px">')
        for title, quote, srcname, url in V.FORUM_QUOTES:
            o.append(f'<div class="qt"><h4>{E(title)}</h4><blockquote>{E(quote)}</blockquote>'
                     f'<p class="qsrc">{srclinks([(srcname, url)])}</p></div>')
        o.append("</div></section>")
        o.append("</div>")
        return "".join(o)

    # ---------------------------------------------------------------- INFLUENCERS
    def infl():
        o = ['<div class="tabpane" id="p-infl" hidden>']
        o.append('<section class="hero"><h1 class="h1">Fifty three names, screened on whether they can actually say yes.</h1>'
                 '<p class="lede">Every follower number carries the route it was read from. Twenty people carry a full card and an '
                 'email written for that person. The other thirty three sit in the master table with a contact route and a screen colour.</p>')
        o.append(chips(I.HERO_CHIPS))
        o.append("</section>")

        o.append('<div class="legend">' + "".join(
            f"<div><b>{E(a)}</b> {E(b)}</div>" for a, b in I.LEGEND) + "</div>")

        # callouts
        for title, body, srcname, url in I.CALLOUTS:
            o.append(f'<section class="callout"><span class="ctag">FINDING</span><h3>{E(title)}</h3>'
                     f'<p>{E(body)}</p><p>{srclinks([(srcname, url)])}</p></section>')

        # shortlist
        o.append('<section class="blk">' + head("The ranked top ten, screen colour first.", "SHORTLIST"))
        o.append('<p class="close">Ranking logic: screen colour first, because a RED cannot be bought at any price. '
                 'Then persona match to the 45 plus, 54.5 percent female buyer. Then cost efficiency per targeted impression. '
                 'Then contact openness, because a verified email or a network sales desk beats a direct message. '
                 'Reach alone is deliberately not the top weight.</p>')
        o.append('<div class="shortl">')
        for s in SHORTLIST:
            o.append(f'<div class="sl"><div class="sl-n">{s["rank"]:02d}</div><div>'
                     f'<h4>{s["who"]}</h4><p>{s["why"]}</p>'
                     f'<div class="slmeta"><span class="scr s-{s["screen"].lower()}">{s["screen"]}</span> '
                     f'{E(s["reach"])} total reach. Contact: {s["contact"]}</div></div></div>')
        o.append("</div></section>")

        # structural notes
        o.append('<section class="blk">' + head("Two structural notes."))
        for n in NOTES:
            o.append(f'<div class="note">{n}</div>')
        o.append("</section>")

        # master table
        o.append('<section class="blk">' + head("All fifty three, sortable.", "MASTER TABLE"))
        o.append(f'<p class="close">{E(I.REACH_NOTE)}</p>')
        o.append('<div class="twrap" style="margin-top:26px"><table class="tbl kv4 mtbl" id="infl-master"><thead><tr>'
                 '<th class="srt" data-num="1">Rank</th><th class="srt">Name</th><th class="srt">Primary platform</th>'
                 '<th class="srt" data-num="1">Total reach</th><th class="srt">Screen</th>'
                 '<th class="srt">Price signal</th><th class="srt">Best contact route</th></tr></thead><tbody>')
        for m in MASTER:
            o.append(f'<tr><td data-v="{m["n"]}">{m["n"]}</td>'
                     f'<td data-v="{E(m["name"])}"><b>{E(m["name"])}</b></td>'
                     f'<td>{E(m["plat"])}</td>'
                     f'<td data-v="{reachnum(m["reach"]):.0f}">{E(m["reach"])}</td>'
                     f'<td data-v="{E(m["screen"])}"><span class="scr s-{m["screen"].lower()}">{E(m["screen"])}'
                     f'{" REFUSED" if m["refused"] else ""}</span></td>'
                     f'<td>{E(m["price"])}</td><td>{m["contact_md"]}</td></tr>')
        o.append("</tbody></table></div></section>")

        # full cards
        o.append('<div class="phase-rule"><span>TWENTY FULL CARDS, IN SHORTLIST ORDER</span></div>')
        for pos, num in enumerate(I.TOP20, 1):
            p = BYNUM[num]
            o.append(f'<article class="infl">')
            o.append(f'<div class="infl-top"><div class="infl-n">{pos:02d}</div>'
                     f'<div><h3>{E(p["name"])}</h3>'
                     f'<div class="infl-role">Roster number {p["n"]} of 53. Primary platform {E(p["plat"])}. '
                     f'Total reach {E(p["reach"])}.</div></div>'
                     f'<div class="badge b-{p["screen"].lower()}">{E(p["screen"])}'
                     f'{" REFUSED" if p["refused"] else ""}</div></div>')
            # followers table
            o.append('<div class="twrap" style="margin-top:26px"><table class="tbl kv4">'
                     '<thead><tr><th>Platform</th><th>Number</th><th>Source</th></tr></thead><tbody>')
            for a, b, c in p["rows"]:
                o.append(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>")
            o.append("</tbody></table></div>")
            o.append('<div class="spec">')
            o.append(f'<div class="sp"><div class="sp-k">Total reach and dominant platform</div>'
                     f'<div class="sp-v">{md(p["total"])}</div></div>')
            o.append(f'<div class="sp"><div class="sp-k">Competition screen</div>'
                     f'<div class="sp-v">{md(p["screen_txt"].lstrip(" -"))}</div></div>')
            o.append(f'<div class="sp"><div class="sp-k">Pricing, with the arithmetic</div>'
                     f'<div class="sp-v">{md(p["pricing"])}</div></div>')
            o.append(f'<div class="sp"><div class="sp-k">Contact, every route</div><div class="sp-v">'
                     + "".join(f"<div>{md(x.lstrip('- ').strip())}</div>"
                               for x in p["contact_blk"].splitlines() if x.strip().startswith("-"))
                     + "</div></div>")
            o.append(f'<div class="sp"><div class="sp-k">Fit for the 45 plus female buyer</div>'
                     f'<div class="sp-v">{md(p["fit"])}</div></div>')
            o.append("</div>")
            subj, body = I.MAIL[num]
            o.append('<div class="copyset">')
            o.append(copybox(subj, "Subject line"))
            o.append(copybox(body, "Outreach email, written for this person"))
            o.append("</div></article>")
        o.append("</div>")
        return "".join(o)

    # ---------------------------------------------------------------- GALLERY
    groups, total, motion = C.load()

    def gallery():
        o = ['<section class="blk" id="creative-gallery">']
        o.append(head(f"Every creative in the client repositories, {total} files, grouped by concept and aspect ratio.",
                      "FULL CREATIVE GALLERY"))
        o.append(f'<p class="close">Nineteen concept sets across eight repositories. '
                 f'Each image is served directly from raw.githubusercontent.com and every URL was checked and returns a live file. '
                 f'{motion} of them are animated motion files. Captions carry the filename and the true pixel size read from the file header, '
                 f'not from the filename. Images load as they scroll into view.</p>')
        o.append('<div class="gal-nav">')
        for i, g in enumerate(groups):
            o.append(f'<a href="#gal{i}">{E(g["label"])} ({g["count"]})</a>')
        o.append("</div>")
        for i, g in enumerate(groups):
            o.append(f'<div class="gal-grp" id="gal{i}"><h3>{E(g["label"])}</h3>'
                     f'<div class="gal-meta">{g["count"]} files. Repository '
                     f'<a href="{E(g["repo_url"])}" target="_blank" rel="noopener">{E(g["repo"])}</a></div>')
            for rl, items in g["ratios"]:
                o.append(f'<div class="gal-ratio">{E(rl)}, {len(items)} files</div><div class="gal">')
                for it in items:
                    o.append(f'<figure><div class="cr-box" style="aspect-ratio:{E(it["ar"])}">'
                             f'<img src="{E(it["u"])}" alt="{E(it["f"])}" loading="lazy" '
                             f'width="{E(it["ar"].split("/")[0])}" height="{E(it["ar"].split("/")[1])}"></div>'
                             f'<figcaption><b>{E(it["f"])}</b>{E(it["px"])}'
                             + ('<span class="mv-tag">MOTION</span>' if it["motion"] else "")
                             + "</figcaption></figure>")
                o.append("</div>")
            o.append("</div>")
        o.append("</section>")
        return "".join(o)

    return leads(), infl(), gallery(), {"creatives": total, "motion": motion,
                                        "vendors_scored": len(V.VENDORS),
                                        "vendors_total": len(V.VENDORS) + len(V.COVERAGE_ROWS),
                                        "influencers": len(MASTER), "cards": len(I.TOP20)}


def reachnum(r):
    r = r.replace(",", "").strip()
    try:
        if r.endswith("M"):
            return float(r[:-1]) * 1e6
        if r.endswith("K"):
            return float(r[:-1]) * 1e3
        return float(r)
    except ValueError:
        return 0.0
