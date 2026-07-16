import collections


def get_produced_energy(tree: dict[tuple[int, int], str]) -> int:
    above = collections.Counter()
    result = 0
    for (r, c), id_ in sorted(tree.items(), reverse=True):
        if id_ != "ZZ":
            continue

        mul = max(3 - above[c], 0)
        energy = min(r, 10) * mul
        result += energy
        above[c] += 1
    return result


def get_mass(m: dict[str, tuple[str, str, str]]) -> int:
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
        required_energy = 3 * len(tree)
        produced_energy = get_produced_energy(tree)

        if year >= 5 and required_energy > produced_energy:
            break

    return len(tree)


with open("./input/2026/11.txt") as f:
    lines = f.read().splitlines()

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

answer = sum(get_mass(m) for m in dnas)
print(answer)
