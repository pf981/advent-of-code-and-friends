with open("./2025/input/everybody_codes_e2025_q14_p3.txt") as f:
    lines = f.read().splitlines()

n = 34


def sim(active: set[tuple[int, int]]) -> set[tuple[int, int]]:
    result = set()
    for r in range(n):
        for c in range(n):
            active_diags = 0

            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                r2 = r + dr
                c2 = c + dc
                active_diags += (r2, c2) in active

            if (r, c) in active:
                if active_diags % 2 == 1:
                    result.add((r, c))
            else:
                if active_diags % 2 == 0:
                    result.add((r, c))

    return result


def does_match_pattern(active: set[tuple[int, int]]) -> bool:
    r_start, c_start = (13, 13)
    for dr in range(len(lines)):
        for dc in range(len(lines[0])):
            r = r_start + dr
            c = c_start + dc
            if lines[dr][dc] == "#":
                if (r, c) not in active:
                    return False
            else:
                if (r, c) in active:
                    return False

    return True


active: set[tuple[int, int]] = set()  # {(r, c), ...}
rounds = []
active_counts = []

for rnd in range(1, 10_000 + 1):
    active = sim(active.copy())

    if not does_match_pattern(active):
        continue

    rounds.append(rnd)
    active_counts.append(len(active))

first_round, *round_deltas = [rnd2 - rnd1 for rnd1, rnd2 in zip([0] + rounds, rounds)]
first_active_count, *active_counts = active_counts

cycle_len = round_deltas[1:].index(round_deltas[0]) + 1

round_deltas = round_deltas[:cycle_len]
active_counts = active_counts[:cycle_len]

target_round = 1000000000
times = (target_round - first_round) // sum(round_deltas)

answer = first_active_count + times * sum(active_counts)
remaining = target_round - (first_round + times * sum(round_deltas))

i = 0
while i < len(round_deltas) and remaining > round_deltas[i]:
    remaining -= round_deltas[i]
    answer += active_counts[i]
    i += 1

print(answer)
