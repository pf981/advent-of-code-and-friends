import collections
import re

with open("./2026/input/everybody_codes_e2026_q07_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """id=1, energy=5, connections=2,5,7
# id=2, energy=9, connections=6,7
# id=3, energy=3, connections=4
# id=4, energy=8, connections=3
# id=5, energy=1, connections=6,7
# id=6, energy=7, connections=1,7
# id=7, energy=6, connections=5""".splitlines()

start_node = None
m = {}
energies = {}
for line in lines:
    id_, energy, *connections = map(int, re.findall(r"\d+", line))
    print(id_, energy, connections)
    energies[id_] = energy
    m[id_] = connections

    if start_node is None or len(connections) > len(m[start_node]):
        start_node = id_

pulses = {start_node: 1}
for strength in reversed(range(1, 5 + 1)):
    pulses2 = collections.Counter()
    print(f"Strength {strength}:")
    for node, pulse in pulses.items():
        print(f"{strength=} {node=} {pulse=}")
        energies[node] += strength * pulse
        for node2 in m[node]:
            pulses2[node2] += pulse
    pulses = pulses2
    print()

energies
answer = sum(energies.values())
print(answer)
