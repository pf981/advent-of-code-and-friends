import collections
import itertools
import math

with open("./2026/input/everybody_codes_e2026_q19_p2.txt") as f:
    text = f.read().strip()
# text = """CCCCC
# MMMMM
# YYYYY
# KKKKK
# CCMYY

# 14231
# 14231
# 14231
# 14231
# 14231""".strip()

a, b_original = text.split("\n\n")
answer = 0
for perm in itertools.permutations("1234", 4):
    # print(perm)

    b = b_original
    for x, y in zip(perm, "CMYK"):
        b = b.replace(x, y)

    counts = collections.Counter()
    for c1, c2 in zip("".join(a).replace("\n", ""), "".join(b).replace("\n", "")):
        # print(c1, c2)
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

    result = math.prod(cnt for _, cnt in counts.most_common(3))
    answer = max(answer, result)

print(answer)
