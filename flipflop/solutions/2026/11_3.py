import collections


def get_produced_energy(
    tree: dict[tuple[int, int], str], stems: set[tuple[int, int]]
) -> int:
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


def get_trees(
    trees: list[dict[tuple[int, int], str]], dnas: list[dict[str, tuple[str, str, str]]]
) -> list[dict[tuple[int, int], str]]:
    living = set(range(len(trees)))
    for year in range(1, 100 + 1):
        used = set()
        for tree in trees:
            used.update(tree)

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
            required_energy = 3 * len(tree)
            produced_energy = get_produced_energy(tree, stems)

            if year >= 5 and required_energy > produced_energy:
                living.remove(tree_id)

        if not living:
            break
    return trees


def get_offspring(
    trees: list[dict[tuple[int, int], str]], dnas: list[dict[str, tuple[str, str, str]]]
) -> tuple[list[dict[tuple[int, int], str]], list[dict[str, tuple[str, str, str]]]]:
    offspring = {}  # c -> (r, c, m)
    for tree, m in zip(get_trees(trees, dnas), dnas):
        for (r, c), id_ in tree.items():
            if id_ != "ZZ":
                if c not in offspring or r > offspring[c][0]:
                    offspring[c] = (r, c, m)

    trees2 = []
    dnas2 = []
    for _, c, m in sorted(offspring.values(), key=lambda x: x[1]):
        trees2.append({(1, c): "00"})
        dnas2.append(m)

    return trees2, dnas2


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


trees = [{(1, 10 * i): "00"} for i in range(len(dnas))]
trees, dnas = get_offspring(trees, dnas)
trees, dnas = get_offspring(trees, dnas)
trees = get_trees(trees, dnas)

answer = sum(len(tree) for tree in trees)
print(answer)
