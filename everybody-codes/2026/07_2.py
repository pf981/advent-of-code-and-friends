import collections
import re

with open("./2026/input/everybody_codes_e2026_q07_p2.txt") as f:
    lines = f.read().splitlines()
START_STRENGTH = 10

start_node = None
m = {}
energies = {}
for line in lines:
    id_, energy, *connections = map(int, re.findall(r"\d+", line))
    energies[id_] = energy
    m[id_] = connections

    if start_node is None or len(connections) > len(m[start_node]):
        start_node = id_

pulses = {start_node: 1}
for strength in reversed(range(1, START_STRENGTH + 1)):
    pulses2 = collections.Counter()
    for node, pulse in pulses.items():
        energies[node] += strength * pulse
        for node2 in m[node]:
            pulses2[node2] += pulse
    pulses = pulses2

answer = sum(energies.values())
print(answer)
