import collections
import re

with open("./2026/input/everybody_codes_e2026_q07_p3.txt") as f:
    lines = f.read().splitlines()
START_STRENGTH = 10
EXPLOSION_LIMIT = 1000000

m = {}
energies = {}
for line in lines:
    id_, energy, *connections = map(int, re.findall(r"\d+", line))
    energies[id_] = energy
    m[id_] = connections


def get_total_energy(start_node: int) -> int:
    eg = energies.copy()
    pulses = {start_node: {START_STRENGTH: 1}}  # node -> strength -> count
    exploded = set()
    stage = 1
    while pulses:
        pulses2 = {}

        to_explode = set()

        # Update energy
        for node in pulses:
            if node in exploded:  # FIXME: Test
                continue
            for strength, pulse in pulses[node].items():
                eg[node] += strength * pulse
                if eg[node] >= EXPLOSION_LIMIT:
                    to_explode.add(node)

        # Explode
        for node in to_explode:
            for node2 in m[node]:
                if node2 in exploded or node2 in to_explode:
                    continue
                if node2 not in pulses2:
                    pulses2[node2] = collections.Counter()
                pulses2[node2][START_STRENGTH] += 1
        exploded.update(to_explode)

        # Propogate
        for node in pulses:
            for strength, pulse in pulses[node].items():
                for node2 in m[node]:
                    if node2 in exploded:
                        continue
                    if node2 not in pulses2:
                        pulses2[node2] = collections.Counter()
                    if strength - 1 > 0:
                        pulses2[node2][strength - 1] += pulse

        pulses = pulses2

        stage += 1

    return sum(energy for node, energy in eg.items() if node not in exploded)


answer = max(get_total_energy(node) for node in m)
print(answer)
