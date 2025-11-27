import collections
import re
import z3  # type: ignore

with open("./2025/input/everybody_codes_e2025_q18_p3.txt") as f:
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


def z3_zero_below(value: int | z3.ArithRef, threshold: int) -> z3.ArithRef:
    return z3.If(value < threshold, 0, value)


def get_max_energy(test_case_z3: list[int] | list[z3.Bool]) -> int:
    o = z3.Optimize()

    incoming_energy_z3 = [0] * n_nodes
    incoming_energy_z3[0] = 1

    for node in range(n_nodes):
        for to, thickness in edges[node]:
            incoming_energy_z3[to] += (
                z3_zero_below(incoming_energy_z3[node], node_thickness[node])
                * thickness
            )
            if node == 0:
                incoming_energy_z3[to] *= test_case_z3[to - 1]

    output = z3.Int("output")

    o.add(output == z3_zero_below(incoming_energy_z3[-1], node_thickness[-1]))
    o.maximize(output)

    assert o.check() == z3.sat
    return o.model()[output].py_value()


test_cases = [[int(s) for s in line.split()] for line in grid_text.splitlines()]
max_energy = get_max_energy([z3.Bool(f"input_{i}") for i in range(len(test_cases[0]))])
answer = 0
for test_case in test_cases:
    energy = get_max_energy(test_case)
    if energy > 0:
        answer += max_energy - energy

print(answer)
