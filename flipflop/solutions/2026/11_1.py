import collections

with open("./input/2026/11.txt") as f:
    lines = f.read().splitlines()
# lines = """    02          XX          00
# 01  00  XX  01  01  02  XX  02  XX""".splitlines()


def get_required_energy(tree):
    return 3 * len(tree)


def get_produced_energy(tree):
    above = collections.Counter()
    result = 0
    for (r, c), id_ in sorted(tree.items(), reverse=True):
        if id_ != "ZZ":
            continue

        mul = max(3 - above[c], 0)
        energy = min(r, 10) * mul
        result += energy
        # print(f"{r=} {c=} {energy=}")
        above[c] += 1
    return result


dnas = []
for i in range(0, len(lines), 3):
    m = {}  # id -> (above, left, right)
    aboves = lines[i].split()
    parts = lines[i + 1].split()
    triples = [parts[j : j + 3] for j in range(0, len(parts), 3)]

    for above, triple in zip(aboves, triples):
        left, mid, right = triple
        m[mid] = (above, left, right)

    dnas.append(m)


def get_mass(m):
    tree = {(1, 0): "00"}  # (r, c) -> id_ | "ZZ"
    for year in range(1, 100 + 1):
        tree2 = {}
        for (r, c), id_ in tree.items():
            tree2[(r, c)] = "ZZ"  # Stem

            if id_ == "ZZ":
                continue

            above, left, right = m[id_]
            if above != "XX":
                tree2[(r + 1, c)] = max(tree2.get((r + 1, c), ""), above)
            if left != "XX":
                tree2[(r, c - 1)] = max(tree2.get((r, c - 1), ""), left)
            if right != "XX":
                tree2[(r, c + 1)] = max(tree2.get((r, c + 1), ""), right)

        tree = tree2
        required_energy = get_required_energy(tree)
        produced_energy = get_produced_energy(tree)

        # print(f"{year=} {required_energy=} {produced_energy=}")
        if year >= 5 and required_energy > produced_energy:
            break
        # if year == 5:
        #     break  # FIXME:TEST
        # break  # TEST
        # if year == 5 - 1:
        #     break

        # if year == 67:
        #     break

    print(f"{year=} {len(tree)=}")
    return len(tree)


answer = sum(get_mass(m) for m in dnas)
print(answer)


# sum(id_ == "ZZ" for id_ in tree.values())
# sum(id_ != "ZZ" for id_ in tree.values())


def pp(tree):
    max_y = max(y for y, _ in tree)
    min_x = min(x for _, x in tree)
    max_x = max(x for _, x in tree)
    for r in range(max_y, 0, -1):
        line = [f"{r:>02}:"]
        for c in range(min_x - 1, max_x + 2):
            ch = "."
            if (r, c) in tree:
                ch = "#" if tree[(r, c)] == "ZZ" else "@"
            line.append(ch)
        print("".join(line))


# pp(tree)
