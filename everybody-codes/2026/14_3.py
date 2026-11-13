import collections
import itertools

with open("./2026/input/everybody_codes_e2026_q14_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """AAAEEEFFFF
# AADDDDDGFF
# BACDDIGGFF
# BABBIIIGGH
# BBBBIIIIHH""".splitlines()
# lines = """IIIIIILOHHHHHHHHGGGGGQSRRRRKKK
# IIIIIILOOHHHHHHGGXGGGQSRRRRKKK
# PPPPILLLOOOODDHBGGGGGQSSRRRKKK
# PPZPLLLLFFOODDBBBBGGQQQSSRKKKK
# PPPPLLLLFFFONDDDBBMGGQQSSKKJJJ
# PPPCCCCCCFFONNDDMMMGQQQSSSKJJJ
# PCCCCCCCCFFNNDDDDMAAQQQSSSKKJJ
# PPCCECCCFFNNNNDADMAATQTTSSSJJJ
# PPEEEEECCFFNNAAAMMATTTTTSTSSSJ
# PPEEEEEEEFFNNNAAAAAATTTTTTSSJJ""".splitlines()

nrows = len(lines)
ncols = len(lines[0])

# Don't forget frame seem
# seems = []  # cost, node1, node2
seems = collections.Counter()  # {node1, node2} -> cost

# Frame
for r in range(nrows):
    seems[frozenset(["frame", lines[r][0]])] += 1
    seems[frozenset(["frame", lines[r][ncols - 1]])] += 1
for c in range(ncols):
    seems[frozenset(["frame", lines[0][c]])] += 1
    seems[frozenset(["frame", lines[nrows - 1][c]])] += 1

for r in range(nrows):
    for c in range(ncols):
        ch = lines[r][c]
        if r + 1 < nrows and lines[r + 1][c] != ch:
            seems[frozenset([ch, lines[r + 1][c]])] += 1
        if c + 1 < ncols and lines[r][c + 1] != ch:
            seems[frozenset([ch, lines[r][c + 1]])] += 1


def get_min_cost(seems):
    edges = sorted([cost, a, b] for (a, b), cost in seems.items())
    total_cost = 0
    usable = {"frame"}
    while True:
        candidates = [
            (cost, a, b)
            for cost, a, b in edges
            if (a in usable or b in usable) and not (a in usable and b in usable)
        ]
        if not candidates:
            break
        cost, a, b = min(candidates)
        # print(f"{cost=} {a=} {b=}")
        usable.add(a)
        usable.add(b)
        total_cost += cost

    return total_cost


nodes = set("".join(lines))
answer = float("inf")
for charges in itertools.combinations(nodes, 2):
    seems2 = seems.copy()
    for i, charge in enumerate(charges):
        for b in nodes | {"frame"}:
            if frozenset([charge, b]) not in seems:
                continue

            seems2[frozenset([charge, b])] = 0

    min_cost = get_min_cost(seems2)
    if "A" in charges and "B" in charges:
        print(f"{charges=}\n{min_cost=}\n{seems2=}\n")
    answer = min(answer, min_cost)

print(answer)

# for cost, a, b in edges:
#     if a in done and b in done:
#         continue
#     done.add(a)
#     done.add(b)
#     total_cost += cost

# print(len(done))
# answer = pairs
# 371
# Your answer length is: correct
# The first character of your answer is: incorrect
