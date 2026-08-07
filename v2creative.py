# -*- coding: utf-8 -*-
"""Creative gallery data. Reads the verified manifest with real pixel dimensions."""
import json, re
from fractions import Fraction

SRC = "/home/user/workspace/v2_creatives_dims.json"

CONCEPTS = [
    ("lla-meta-banners-gallery/banners/chosen", "Chosen set, the approved Meta banner line"),
    ("lla-meta-banners-gallery/banners/v1", "Meta banner gallery, version one"),
    ("lla-meta-banners-gallery/banners/v2", "Meta banner gallery, version two"),
    ("lla-meta-banners-gallery/banners/v3", "Meta banner gallery, version three"),
    ("lla-meta-banners-gallery/banners/v4", "Meta banner gallery, version four"),
    ("lla-meta-banners-gallery/banners/v5", "Meta banner gallery, version five"),
    ("lla-meta-banners-gallery/banners/v6", "Meta banner gallery, version six"),
    ("lla-meta-banners-gallery/banners/v7", "Meta banner gallery, version seven"),
    ("courtney-banners/banners", "Courtney testimonial concept, first cut"),
    ("lla-courtney-final/banners", "Courtney testimonial concept, final cut"),
    ("julie-onset-banners/png", "Julie onset concept"),
    ("julie-meta-banners/out/banner_a_slow_your_pace", "Julie concept A, slow your pace"),
    ("julie-meta-banners/out/banner_b_2nd_slowest_ager", "Julie concept B, second slowest ager"),
    ("julie-meta-banners/out/decode_your_biomarkers", "Decode your biomarkers"),
    ("julie-meta-banners/out/longevity_course_taught_live", "Longevity course taught live"),
    ("lla-pr-article-ads/ads", "Public relations article ads, standard"),
    ("lla-pr-article-ads/ads-hd", "Public relations article ads, high definition"),
    ("lla-employee-referral/banners", "Employee referral banners"),
    ("lla-julie-animations/media", "Motion files, animated GIF"),
]


def ratio_label(w, h):
    if not w or not h:
        return "Unknown"
    f = Fraction(w, h).limit_denominator(40)
    n, d = f.numerator, f.denominator
    if abs(w / h - 1.91) < 0.03:
        return "1.91 to 1, link and landscape"
    if n == d:
        return "1 to 1, square"
    if (n, d) == (4, 5):
        return "4 to 5, feed portrait"
    if (n, d) == (9, 16):
        return "9 to 16, stories and reels"
    if (n, d) == (16, 9):
        return "16 to 9, landscape"
    return f"{n} to {d}"


def load():
    recs = json.load(open(SRC))
    groups = []
    for key, label in CONCEPTS:
        repo, folder = key.split("/", 1)
        items = [r for r in recs
                 if r["repo"] == "gitteromri-ux/" + repo
                 and r["path"].rsplit("/", 1)[0] == folder]
        if not items:
            continue
        buckets = {}
        for r in items:
            buckets.setdefault(ratio_label(r["w"], r["h"]), []).append(r)
        out = []
        for rl in sorted(buckets, key=lambda k: (-len(buckets[k]), k)):
            rows = sorted(buckets[rl], key=lambda r: r["path"])
            out.append((rl, [{
                "u": r["raw_url"],
                "f": r["path"].rsplit("/", 1)[-1],
                "px": f'{r["w"]} by {r["h"]} pixels',
                "ar": f'{r["w"]}/{r["h"]}',
                "motion": r["extension"] == ".gif",
            } for r in rows]))
        groups.append({"label": label, "repo": "gitteromri-ux/" + repo,
                       "repo_url": f'https://github.com/gitteromri-ux/{repo}',
                       "count": len(items), "ratios": out})
    total = sum(g["count"] for g in groups)
    motion = sum(1 for r in recs if r["extension"] == ".gif")
    assert total == len(recs), (total, len(recs))
    return groups, total, motion


if __name__ == "__main__":
    g, t, m = load()
    print("groups", len(g), "total", t, "motion", m)
    for x in g:
        print(x["count"], x["label"], [(r[0], len(r[1])) for r in x["ratios"]])
