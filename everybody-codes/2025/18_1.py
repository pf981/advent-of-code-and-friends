import collections
import re

with open("./2025/input/everybody_codes_e2025_q18_p1.txt") as f:
    # lines = f.read().splitlines()
    text = f.read().strip()

# text = """Plant 1 with thickness 1:
# - free branch with thickness 1

# Plant 2 with thickness 1:
# - free branch with thickness 1

# Plant 3 with thickness 1:
# - free branch with thickness 1

# Plant 4 with thickness 17:
# - branch to Plant 1 with thickness 15
# - branch to Plant 2 with thickness 3

# Plant 5 with thickness 24:
# - branch to Plant 2 with thickness 11
# - branch to Plant 3 with thickness 13

# Plant 6 with thickness 15:
# - branch to Plant 3 with thickness 14

# Plant 7 with thickness 10:
# - branch to Plant 4 with thickness 15
# - branch to Plant 5 with thickness 21
# - branch to Plant 6 with thickness 34""".strip()

nodes = {}  # id -> thickness
nodes_incoming = collections.Counter()  # id -> incoming_energy
edges = collections.defaultdict(list)  # from -> [(to, thickness), ...]
in_degree = collections.Counter()

for part in text.split("\n\n"):
    # print(f"{part=}")
    plant_line, *branch_lines = part.splitlines()
    assert "-" not in plant_line
    # print([int(x) for x in re.findall(r"\d+", plant_line)])
    plant_id, plant_thickness = (int(x) for x in re.findall(r"\d+", plant_line))
    nodes[plant_id] = plant_thickness

    for branch_line in branch_lines:
        assert branch_line.count("-") == 1
        nums = [int(x) for x in re.findall(r"\d+", branch_line)]

        assert len(nums) in [1, 2]
        if len(nums) == 1:
            edges[None].append((plant_id, nums[0]))
        else:
            edges[nums[0]].append((plant_id, nums[1]))
            # in_degree[plant_id] += 1  # Branch to

        in_degree[plant_id] += 1  # 1 in for every branch


todo = []  # nodes
for to, thickness in edges[None]:  # Free branches
    nodes_incoming[to] += thickness
    in_degree[to] -= 1

    assert in_degree[to] >= 0
    if in_degree[to] == 0:
        todo.append(to)

    print(f"Done free brnach {to=} {thickness=}")

# # Note: You could just have said todo = [None]
# for node in todo:
#     if (
#         nodes_incoming[node] < nodes[node]
#     ):  # Incoming does not exceed thickness, so don't propogate
#         continue

#     for to, thickness in edges[node]:
#         nodes_incoming[to] += nodes[node] * thickness
#         in_degree[to] -= 1
#         assert in_degree[to] >= 0
#         if in_degree[to] == 0:
#             todo.append(to)

#     print(f"Done node {node=}")
#     # Beware appending while iterating


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

answer = nodes_incoming[max(nodes)]
print(answer)
