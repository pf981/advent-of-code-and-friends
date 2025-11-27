import collections
import re

with open("./2025/input/everybody_codes_e2025_q18_p1.txt") as f:
    text = f.read().strip()

# Free branches at index 0
node_thickness = [1]  # id -> thickness
incoming_energy = [1]  # id -> incoming_energy
edges = collections.defaultdict(list)  # from -> [(to, thickness), ...]

for part in text.split("\n\n"):
    plant_line, *branch_lines = part.splitlines()
    plant_id, plant_thickness = (int(s) for s in re.findall(r"-?\d+", plant_line))

    node_thickness.append(plant_thickness)
    incoming_energy.append(0)

    for branch_line in branch_lines:
        nums = [int(s) for s in re.findall(r"-?\d+", branch_line)]

        assert len(nums) in [1, 2]
        if len(nums) == 1:  # Free branch
            edges[0].append((plant_id, nums[0]))
        else:
            edges[nums[0]].append((plant_id, nums[1]))

for node in range(len(node_thickness)):
    if incoming_energy[node] < node_thickness[node]:
        continue

    for to, thickness in edges[node]:
        incoming_energy[to] += incoming_energy[node] * thickness

answer = incoming_energy[len(node_thickness) - 1]
print(answer)
