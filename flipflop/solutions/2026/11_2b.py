import collections

with open("./input/2026/11.txt") as f:
    lines = f.read().splitlines()
lines = """    01          XX          XX
02  00  XX  XX  01  00  02  02  XX

    02          XX          00
01  00  XX  01  01  02  XX  02  XX""".splitlines()


def get_required_energy(tree):
    return 3 * len(tree)


def get_produced_energy(tree, stems):
    above = collections.Counter()
    result = 0
    for r, c in stems:
        if (r, c) in tree:
            assert tree[(r, c)] == "ZZ"
            mul = max(3 - above[c], 0)
            energy = min(r, 10) * mul
            result += energy
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


def get_mass(trees, dnas, max_years=100):
    living = set(range(len(trees)))
    for year in range(1, max_years + 1):
        used = set()
        for tree in trees:
            used.update(tree)

        # Update
        for tree_id in range(len(trees)):
            if tree_id not in living:
                continue

            tree = trees[tree_id]
            m = dnas[tree_id]

            tree2 = {}
            for (r, c), id_ in tree.items():
                tree2[(r, c)] = "ZZ"  # Stem

                if id_ == "ZZ":
                    continue

                above, left, right = m[id_]
                if above != "XX" and (r + 1, c) not in used:
                    tree2[(r + 1, c)] = max(tree2.get((r + 1, c), ""), above)
                if left != "XX" and (r, c - 1) not in used:
                    tree2[(r, c - 1)] = max(tree2.get((r, c - 1), ""), left)
                if right != "XX" and (r, c + 1) not in used:
                    tree2[(r, c + 1)] = max(tree2.get((r, c + 1), ""), right)

            trees[tree_id] = tree2
            used.update(tree2)

        stems = set()
        for tree in trees:
            for p, id_ in tree.items():
                if id_ == "ZZ":
                    stems.add(p)
        stems = sorted(stems, reverse=True)

        for tree_id in range(len(trees)):
            if tree_id not in living:
                continue
            tree = trees[tree_id]
            required_energy = get_required_energy(tree)
            produced_energy = get_produced_energy(tree, stems)

            # print(f"{year=} {required_energy=} {produced_energy=}")
            if year >= 5 and required_energy > produced_energy:
                living.remove(tree_id)

        if not living:
            print("all dead")
            break
    print(f"{year=} {len(used)=}")
    # pp(trees[0])
    # print()
    # print()
    # pp(trees[1])
    # return len(used)
    # ppp(trees)
    return sum(len(tree) for tree in trees)

    # print(f"{year=} {len(tree)=}")
    # return len(tree)


trees = [{(1, 10 * i): "00"} for i in range(len(dnas))]  # FIXME:USE THIS

answer = get_mass(trees, dnas)
print(answer)


# trees = [{(1, 100000 * i): "00"} for i in range(len(dnas))]  # FIXME TEST
# answer = get_mass(trees, dnas, 144)
# trees = [{(1, 100 * i): "00"} for i in range(len(dnas))]  # FIXME TEST
# answer = get_mass(trees, dnas, 144)
# print(answer)


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


def ppp(trees):
    tree = {}
    for t in trees:
        tree.update(t)
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
# 9636 incorrect
# 6424 incorrect
# 23375 incorrect
