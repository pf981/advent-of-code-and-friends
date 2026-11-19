import collections
import math

with open("./2026/input/everybody_codes_e2026_q19_p1.txt") as f:
    text = f.read().strip()
# text = """CCCCC
# MMMMM
# YYYYY
# KKKKK
# CCMYY

# CMYKC
# CMYKC
# CMYKC
# CMYKC
# CMYKC""".strip()

a, b = text.split("\n\n")

counts = collections.Counter()
for c1, c2 in zip("".join(a).replace("\n", ""), "".join(b).replace("\n", "")):
    print(c1, c2)
    if "K" in [c1, c2]:
        color = "K"
    elif len(frozenset((c1, c2))) == 1:
        color = c1
    else:
        color = {
            frozenset(["C", "M"]): "B",
            frozenset(["C", "Y"]): "G",
            frozenset(["M", "Y"]): "R",
        }[frozenset((c1, c2))]
    counts[color] += 1


answer = math.prod(cnt for _, cnt in counts.most_common(3))
print(answer)
