import collections
import re

with open("./2025/input/everybody_codes_e2025_q18_p2.txt") as f:
    text = f.read().strip()

# Free branches at index 0
node_thickness = [1]  # id -> thickness
edges = collections.defaultdict(list)  # from -> [(to, thickness), ...]

plant_text, grid_text = text.split("\n\n\n")

for part in plant_text.split("\n\n"):
    plant_line, *branch_lines = part.splitlines()
    plant_id, plant_thickness = (int(s) for s in re.findall(r"-?\d+", plant_line))

    node_thickness.append(plant_thickness)

    for branch_line in branch_lines:
        nums = [int(s) for s in re.findall(r"-?\d+", branch_line)]

        assert len(nums) in [1, 2]
        if len(nums) == 1:  # Free branch
            edges[0].append((plant_id, nums[0]))
        else:
            edges[nums[0]].append((plant_id, nums[1]))

n_nodes = len(node_thickness)


def run_test(test_case: list[int]) -> int:
    incoming_energy = [0] * n_nodes
    incoming_energy[0] = 1

    for node in range(n_nodes):
        if incoming_energy[node] < node_thickness[node]:
            continue

        for to, thickness in edges[node]:
            if node == 0 and not test_case[to - 1]:
                continue
            incoming_energy[to] += incoming_energy[node] * thickness

    if incoming_energy[-1] < node_thickness[-1]:
        return 0
    return incoming_energy[-1]


test_cases = [[int(s) for s in line.split()] for line in grid_text.splitlines()]
answer = 0
for test_case in test_cases:
    answer += run_test(test_case)
print(answer)
