import itertools
import collections

TARGET_NUMBERS = 6


def generate_valid_paths(tree):
    for node in list(tree.keys()):
        nodes_to_visit = [(node, [])]

        while nodes_to_visit:
            cur_node = nodes_to_visit.pop()
            cur_path = cur_node[1] + [cur_node[0]]

            if len(cur_path) > TARGET_NUMBERS:
                continue

            for child in tree[cur_node[0]]:
                nodes_to_visit.insert(0, (child, cur_path))

            if len(cur_path) == TARGET_NUMBERS:
                yield cur_path


polygonals = [
    {n * (n + 1) // 2 for n in range(1000)},
    {n * n for n in range(1000)},
    {n * (3 * n - 1) // 2 for n in range(1000)},
    {n * (2 * n - 1) for n in range(1000)},
    {n * (5 * n - 3) // 2 for n in range(1000)},
    {n * (3 * n - 2) for n in range(1000)},
]

polygonals_together = frozenset(itertools.chain(*polygonals))

cycle_map = collections.defaultdict(set)
for num in range(1000, 10000):
    if num in polygonals_together:
        cycle_map[str(num)[:2]].add(str(num)[2:])

cyclic_sets = []
for path in generate_valid_paths(cycle_map):
    cyclic_set = [int(path[i] + path[i + 1]) for i in range(len(path) - 1)]
    cyclic_set.append(int(path[-1] + path[0]))

    if all(len(str(num)) == 4 for num in cyclic_set):
        cyclic_sets.append(cyclic_set)

for cyclic_set in cyclic_sets:
    for permutation in itertools.permutations(cyclic_set):
        if all(permutation[i] in polygonals[i] for i in range(6)):
            answer = sum(cyclic_set)
            break
    else:
        continue
    break

print(answer)
