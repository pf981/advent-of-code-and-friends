import collections
import re
import copy

with open("./2025/input/everybody_codes_e2025_q18_p3.txt") as f:
    # lines = f.read().splitlines()
    text = f.read().strip()

# text = """Plant 1 with thickness 1:
# - free branch with thickness 1

# Plant 2 with thickness 1:
# - free branch with thickness 1

# Plant 3 with thickness 1:
# - free branch with thickness 1

# Plant 4 with thickness 1:
# - free branch with thickness 1

# Plant 5 with thickness 8:
# - branch to Plant 1 with thickness -8
# - branch to Plant 2 with thickness 11
# - branch to Plant 3 with thickness 13
# - branch to Plant 4 with thickness -7

# Plant 6 with thickness 7:
# - branch to Plant 1 with thickness 14
# - branch to Plant 2 with thickness -9
# - branch to Plant 3 with thickness 12
# - branch to Plant 4 with thickness 9

# Plant 7 with thickness 23:
# - branch to Plant 5 with thickness 17
# - branch to Plant 6 with thickness 18


# 0 1 0 0
# 0 1 0 1
# 0 1 1 1
# 1 1 0 1""".strip()

nodes = {}  # id -> thickness
nodes_incoming = collections.Counter()  # id -> incoming_energy
edges = collections.defaultdict(list)  # from -> [(to, thickness), ...]
in_degree = collections.Counter()

plant_text, grid_text = text.split("\n\n\n")

for part in plant_text.split("\n\n"):
    # print(f"{part=}")
    plant_line, *branch_lines = part.splitlines()
    assert "-" not in plant_line
    # print([int(x) for x in re.findall(r"\d+", plant_line)])
    plant_id, plant_thickness = (int(x) for x in re.findall(r"-?\d+", plant_line))
    nodes[plant_id] = plant_thickness

    for branch_line in branch_lines:
        # assert branch_line.count("-") == 1
        nums = [int(x) for x in re.findall(r"-?\d+", branch_line)]

        assert len(nums) in [1, 2]
        if len(nums) == 1:
            edges[None].append((plant_id, nums[0]))
        else:
            edges[nums[0]].append((plant_id, nums[1]))
            # in_degree[plant_id] += 1  # Branch to

        in_degree[plant_id] += 1  # 1 in for every branch


nodes_o = copy.deepcopy(nodes)
nodes_incoming_o = copy.deepcopy(nodes_incoming)
edges_o = copy.deepcopy(edges)
in_degree_o = copy.deepcopy(in_degree)


def run_test(test_case):
    nodes = copy.deepcopy(nodes_o)
    nodes_incoming = copy.deepcopy(nodes_incoming_o)
    edges = copy.deepcopy(edges_o)
    in_degree = copy.deepcopy(in_degree_o)

    todo = []  # nodes
    for (to, thickness), is_activated in zip(edges[None], test_case):  # Free branches
        if not is_activated:
            continue
        nodes_incoming[to] += thickness
        in_degree[to] -= 1

        assert in_degree[to] >= 0
        # if in_degree[to] == 0:
        #     todo.append(to)

        print(f"Done free brnach {to=} {thickness=}")

    # Note: You could just have said todo = [None]
    todo = sorted(nodes)
    for node in todo:
        if (
            nodes_incoming[node] < nodes[node]
        ):  # Incoming does not exceed thickness, so don't propogate
            continue

        for to, thickness in edges[node]:
            # print(f"{node=} {to=} {thickness=} {nodes[node]=} {nodes[node] * thickness=}")
            # nodes_incoming[to] += nodes[node] * thickness # OLD WRONG
            nodes_incoming[to] += nodes_incoming[node] * thickness
            # nodes_incoming[to] += nodes[to] * thickness  # TEST
            in_degree[to] -= 1
            assert in_degree[to] >= 0
            # if in_degree[to] == 0:
            #     todo.append(to)

        print(f"Done node {node=}")
        # Beware appending while iterating

    print(f"{nodes_incoming=}")
    last_node = max(nodes)
    if nodes_incoming[last_node] < nodes[last_node]:
        return 0
    return nodes_incoming[last_node]


# max_energy = 630  # TODO
max_energy = 11186


#############################


#############################


answer = 0
for line in grid_text.splitlines():
    energy = run_test([int(x) for x in line.split()])
    if energy > 0:
        answer += max_energy - energy
print(answer)
