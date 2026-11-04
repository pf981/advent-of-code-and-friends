import collections
import re

with open("./2026/input/everybody_codes_e2026_q07_p3.txt") as f:
    lines = f.read().splitlines()
START_STRENGTH = 10
EXPLOSION_LIMIT = 1000000

# with open("./2026/input/everybody_codes_e2026_q07_p3_ex.txt") as f:
#     lines = f.read().splitlines()
# START_STRENGTH = 10
# EXPLOSION_LIMIT = 1000000

# lines = """id=1, energy=5, connections=2,5,7
# id=2, energy=9, connections=6,7
# id=3, energy=3, connections=4
# id=4, energy=8, connections=3
# id=5, energy=1, connections=6,7
# id=6, energy=7, connections=1,7
# id=7, energy=6, connections=5""".splitlines()
# START_STRENGTH = 10
# EXPLOSION_LIMIT = 100

m = {}
energies = {}
for line in lines:
    id_, energy, *connections = map(int, re.findall(r"\d+", line))
    print(id_, energy, connections)
    energies[id_] = energy
    m[id_] = connections


def get_total_energy(start_node: int) -> int:
    eg = energies.copy()
    pulses = {start_node: {START_STRENGTH: 1}}  # node -> strength -> count
    exploded = set()
    print(f"Detailed propogation for starting cloud {start_node}:")
    stage = 1
    while pulses:
        print(f"\nStage {stage}:")
        print(f"{pulses=}\n{exploded=}\n{eg=}")
        # for node in sorted(pulses):
        #     print(f"Cloud {node} recieved {n} impulse with ")

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
                # for node2 in m[node]:
                #     if node2 not in pulses2:
                #         pulses2[node2] = collections.Counter()
                #     if strength - 1 > 0:
                #         pulses2[node2][strength - 1] += pulse

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
            # if node in exploded: # FIXME: Do I keep this?
            #     continue

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
        # if stage >= 11:
        #     break  # DEBUG

    print(f"\n{eg=} {exploded=}")
    return sum(energy for node, energy in eg.items() if node not in exploded)


# get_total_energy(1)
answer = 0
for node in m:
    answer = max(answer, get_total_energy(node))
print(answer)
# 52820271
# Your answer length is: correct
# The first character of your answer is: incorrect
