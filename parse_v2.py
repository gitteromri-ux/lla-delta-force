# -*- coding: utf-8 -*-
"""Parses the two v2 research markdown files into structures for the hub build."""
import re, html, json, os

WS = "/home/user/workspace"
INFL_MD = os.path.join(WS, "track2_influencers_v2.md")
VEND_MD = os.path.join(WS, "track1_vendors_v2.md")

DASHES = {"\u2014": ", ", "\u2013": " to ", "\u2212": "-", "\u2018": "'", "\u2019": "'",
          "\u201c": '"', "\u201d": '"', "\u00a0": " ", "\ufffd": ""}
EMOJI = {"\U0001F7E2": "GREEN", "\U0001F7E1": "AMBER", "\U0001F534": "RED",
         "\u2709": "Email", "\u00d7": "x", "\u2265": "at least ", "\u2264": "at most "}


def clean(t):
    for a, b in EMOJI.items():
        t = t.replace(a, b)
    t = re.sub(r"\s*\u2014\s*", ", ", t)
    t = re.sub(r"(?<=\d)\u2013(?=\d)", " to ", t)
    t = re.sub(r"\s*\u2013\s*", " to ", t)
    for a, b in DASHES.items():
        t = t.replace(a, b)
    t = re.sub(r"\s+,", ",", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r"^[,.\s]+", "", t)
    t = re.sub(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", "", t)
    t = t.replace("!", ".")
    t = re.sub(r"[ ]{2,}", " ", t)
    return t.strip()


E = html.escape


def md(t):
    """markdown inline to html, cleaned."""
    t = clean(t)
    parts = []
    idx = 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)]+)\)", t):
        parts.append(("t", t[idx:m.start()]))
        parts.append(("a", m.group(1), m.group(2)))
        idx = m.end()
    parts.append(("t", t[idx:]))
    out = []
    for p in parts:
        if p[0] == "a":
            out.append(f'<a href="{E(p[2])}" target="_blank" rel="noopener">{fmt(p[1])}</a>')
        else:
            out.append(fmt(p[1]))
    return "".join(out)


def fmt(s):
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"(?<![\*\w])\*([^*]+)\*(?!\w)", r"<i>\1</i>", s)
    s = s.replace("*", "")
    return s


def plain(t):
    """strip markdown to plain text (for copy boxes and attributes)."""
    t = clean(t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1", t)
    t = t.replace("**", "").replace("`", "")
    return t.strip()


# ------------------------------------------------------------------ influencers
def load_influencers():
    raw = open(INFL_MD, encoding="utf-8").read()
    # master table
    mt = []
    tsec = raw.split("## 1. MASTER TABLE")[1].split("## 2. FULL PROFILES")[0]
    for ln in tsec.splitlines():
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != 7 or not re.match(r"^\d+$", cells[0]):
            continue
        n, name, plat, reach, screen, price, contact = cells
        sc = "GREEN" if "\U0001F7E2" in screen else "AMBER" if "\U0001F7E1" in screen else "RED"
        refused = "REFUSED" in screen
        mt.append({
            "n": int(n), "name": plain(name), "plat": plain(plat),
            "reach": plain(reach), "screen": sc, "refused": refused,
            "price": plain(price), "contact_md": md(contact), "contact": plain(contact),
        })

    # profiles
    prof = {}
    blocks = re.split(r"\n### (\d+)\. ", raw.split("## 2. FULL PROFILES")[1])
    for i in range(1, len(blocks), 2):
        num = int(blocks[i])
        body = blocks[i + 1]
        head, rest = body.split("\n", 1)
        p = {"n": num, "title": plain(head)}
        # follower table
        rows = []
        for ln in rest.split("**TOTAL REACH")[0].splitlines():
            ln = ln.strip()
            if not ln.startswith("|"):
                continue
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) < 3 or set(cells[0]) <= set("-: ") or cells[0] == "Platform":
                continue
            rows.append((md(cells[0]), md(cells[1]), md(cells[2])))
        p["rows"] = rows

        def grab(start, ends):
            if start not in rest:
                return ""
            seg = rest.split(start, 1)[1]
            for e in ends:
                seg = seg.split(e)[0]
            return seg.strip()

        p["total"] = clean(grab("**TOTAL REACH", ["**Competition screen"]).lstrip(":*").strip())
        p["screen_txt"] = grab("**Competition screen", ["**Pricing", "**Contact, every route"])
        p["pricing"] = grab("**Pricing.**", ["**Contact, every route"])
        p["contact_blk"] = grab("**Contact, every route**", ["**Fit"])
        p["fit"] = grab("**Fit", ["\n---"])
        p["fit"] = re.sub(r"^(for the LLA buyer)?\.?\*{0,2}", "", p["fit"]).strip()
        prof[num] = p

    for m in mt:
        m.update({k: v for k, v in prof.get(m["n"], {}).items() if k != "n"})

    # shortlist
    short = []
    ssec = raw.split("## Section 3 ")[1]
    for ln in ssec.splitlines():
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != 6 or not re.match(r"^\d+$", cells[0]):
            continue
        short.append({"rank": int(cells[0]), "who": md(cells[1]), "reach": plain(cells[2]),
                      "screen": "GREEN" if "\U0001F7E2" in cells[3] else "AMBER" if "\U0001F7E1" in cells[3] else "RED",
                      "contact": md(cells[4]), "why": md(cells[5])})
    notes = []
    for para in ssec.split("**Two structural notes for the client.**")[1].split("\n\n"):
        para = para.strip()
        if para:
            notes.append(md(para))
    return mt, short, notes


if __name__ == "__main__":
    mt, short, notes = load_influencers()
    print(len(mt), len(short), len(notes))
    for m in mt[:2] + mt[36:38]:
        print("\n=====", m["n"], m["name"], m["screen"], m["reach"])
        print("rows", len(m.get("rows", [])))
        print("total:", m.get("total", "")[:120])
        print("screen_txt:", m.get("screen_txt", "")[:160])
        print("pricing:", m.get("pricing", "")[:160])
        print("contact:", m.get("contact_blk", "")[:300])
        print("fit:", m.get("fit", "")[:160])
    print(notes[0][:200])
