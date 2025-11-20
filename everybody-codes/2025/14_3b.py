with open("./2025/input/everybody_codes_e2025_q14_p3.txt") as f:
    lines = f.read().splitlines()

n = 34


def sim(active):
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


def does_match_pattern(active):
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


active = set()  # {(r, c), ...}
result = []  # [rnd, ...]
sum_active = []

for rnd in range(1, 10_000 + 1):
    active = sim(active.copy())
    if does_match_pattern(active):
        s = len(active)
        print(rnd, s)
        result.append(rnd)
        sum_active.append(s)
print(result)

for a, b in zip(result[:-1], result[1:]):
    print(a, b, a - b)


first_hit = 331
ds = [538, 1533, 129, 219, 150, 871, 655]
ss = [644, 500, 580, 608, 664, 600, 632]


target_round = 1000000000

times = (target_round - first_hit) // sum(ds)

ans = times * sum(ss)

remaining = target_round - (first_hit + times * sum(ds))
# if remaining >= d1:
#     ans += s1
#     remaining -= d1
# if remaining >= d2:
#     ans += s2
#     remaining -= d2

print(ans)

# guesses
# 1032477600
# 1032477600 + sum(ss[:1])  # Guess this -> 1032478244 wrong correct correct
# 1032477600 + sum(ss[:2])  # nxt -> 1032478744 -> correct
# 1032477600 + sum(ss[:3])
# 1032477600 + sum(ss[:4])
# 1032477600 + sum(ss[:5])
# 1032477600 + sum(ss[:6])
# 1032477600 + sum(ss[:7])

# # BAD guesses:
# 999998104
# 999998104 + sum(ds[:1])
# 999998104 + sum(ds[:2])  # Guess this -> 999999248 wrong wrong
# 999998104 + sum(ds[:3])
# 999998104 + sum(ds[:4])
# 999998104 + sum(ds[:5])
# 999998104 + sum(ds[:6])
# 999998104 + sum(ds[:7])

# 278388552
# 278388000

# 278388000 + s1

# answer = 0
# print(answer)
