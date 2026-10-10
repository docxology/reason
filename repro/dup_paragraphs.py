"""Count near-duplicate paragraph pairs within a sliding window (editorial check)."""
import difflib, re, sys

def paragraphs(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"(FOUNDATIONS OF REASON · 8\.0|ENGINEERING OF REASON · 3\.5)", " ", text)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    return [p for p in paras if len(p) > 120]

for path in sys.argv[1:]:
    ps = paragraphs(path)
    pairs = []
    for i, a in enumerate(ps):
        for j in range(i + 1, min(i + 4, len(ps))):
            r = difflib.SequenceMatcher(None, a, ps[j]).ratio()
            if r > 0.80:
                pairs.append((r, a[:90]))
    print(f"{path}: {len(ps)} paragraphs >120 chars; near-duplicate pairs (ratio>0.80, window 3): {len(pairs)}")
    for r, snippet in pairs[:40]:
        print(f"   {r:.2f}  {snippet}")
