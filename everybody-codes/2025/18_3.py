import collections
import copy
import re
import z3

with open("./2025/input/everybody_codes_e2025_q18_p3.txt") as f:
    text = f.read().strip()

# Free branches at index 0
node_thickness = [1]  # id -> thickness
incoming_energy = [1]  # id -> incoming_energy
edges = collections.defaultdict(list)  # from -> [(to, thickness), ...]

plant_text, grid_text = text.split("\n\n\n")

for part in plant_text.split("\n\n"):
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


def run_test(
    test_case: list[int],
    node_thickness: list[int],
    incoming_energy: list[int],
    edges: dict[int, list[tuple[int, int]]],
) -> int:
    incoming_energy = incoming_energy.copy()
    edges = copy.deepcopy(edges)
    edges[0] = [edge for edge, test in zip(edges[0], test_case) if test]

    for node in range(len(node_thickness)):
        if incoming_energy[node] < node_thickness[node]:
            continue

        for to, thickness in edges[node]:
            incoming_energy[to] += incoming_energy[node] * thickness

    last_node = len(node_thickness) - 1
    if incoming_energy[last_node] < node_thickness[last_node]:
        return 0
    return incoming_energy[last_node]


def z3_zero_if_below_threshold(value, threshold):
    return z3.If(value < threshold, 0, value)


def get_max_energy() -> int:
    o = z3.Optimize()

    inputs_z3 = []
    for i in range(len(edges[0])):
        input_z3 = z3.Int(f"inputs_{i}")
        inputs_z3.append(input_z3)
        o.add(z3.Or(input_z3 == 0, input_z3 == 1))

    incoming_energy_z3 = collections.defaultdict(int)
    incoming_energy_z3[0] = 1

    for node in range(len(node_thickness)):
        for to, thickness in edges[node]:
            input_z3 = inputs_z3[to - 1] if node == 0 else 1
            incoming_energy_z3[to] = z3.Sum(
                incoming_energy_z3[to],
                z3_zero_if_below_threshold(
                    incoming_energy_z3[node], node_thickness[node]
                )
                * thickness
                * input_z3,
            )

    outputs = {}
    for node in range(len(node_thickness)):
        outputs[node] = z3.Int(f"outputs_{node}")
        o.add(
            outputs[node]
            == z3_zero_if_below_threshold(
                incoming_energy_z3[node], node_thickness[node]
            )
        )

    last_node = len(node_thickness) - 1
    o.maximize(outputs[last_node])

    assert o.check() == z3.sat
    return o.model()[outputs[last_node]].as_long()


max_energy = get_max_energy()
answer = 0
for line in grid_text.splitlines():
    test_case = [int(s) for s in line.split()]
    energy = run_test(test_case, node_thickness, incoming_energy, edges)

    if energy > 0:
        answer += max_energy - energy

print(answer)
