import re

with open("./story_1/input/q01_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """A=4 B=4 C=6 X=3 Y=4 Z=5 M=11
# A=8 B=4 C=7 X=8 Y=4 Z=6 M=12
# A=2 B=8 C=6 X=2 Y=4 Z=5 M=13
# A=5 B=9 C=6 X=8 Y=6 Z=8 M=14
# A=5 B=9 C=7 X=6 Y=6 Z=8 M=15
# A=8 B=8 C=8 X=6 Y=9 Z=6 M=16""".splitlines()


def eni(n, exp, mod):
    result = []
    score = 1
    for _ in range(exp):
        score2 = (score * n) % mod
        result.append(str(score2))
        score = score2
    return int("".join(reversed(result)))


# eni(2, 4, 5)
# eni(3,5,16)


answer1 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    print(a, b, c, x, y, z, m)
    answer1 = max(answer1, eni(a, x, m) + eni(b, y, m) + eni(c, z, m))

print(answer1)


import collections

with open("./story_1/input/q01_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """A=3657 B=3583 C=9716 X=903056852 Y=9283895500 Z=85920867478 M=188
# A=6061 B=4425 C=5082 X=731145782 Y=1550090416 Z=87586428967 M=107
# A=7818 B=5395 C=9975 X=122388873 Y=4093041057 Z=58606045432 M=102
# A=7681 B=9603 C=5681 X=716116871 Y=6421884967 Z=66298999264 M=196
# A=7334 B=9016 C=8524 X=297284338 Y=1565962337 Z=86750102612 M=145""".splitlines()


def eni2(n, exp, mod):
    result = []
    for i in range(5):
        score = pow(n, exp - i, mod)
        result.append(str(score))
    return int("".join((result)))


# eni2(2, 7, 5)

answer2 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    # print(a, b, c, x, y, z, m)
    answer2 = max(answer2, eni2(a, x, m) + eni2(b, y, m) + eni2(c, z, m))

print(answer2)


with open("./story_1/input/q01_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """A=4 B=4 C=6 X=3000 Y=14000 Z=15000 M=110
# A=8 B=4 C=7 X=8000 Y=14000 Z=16000 M=120
# A=2 B=8 C=6 X=2000 Y=14000 Z=15000 M=130
# A=5 B=9 C=6 X=8000 Y=16000 Z=18000 M=140
# A=5 B=9 C=7 X=6000 Y=16000 Z=18000 M=150
# A=8 B=8 C=8 X=6000 Y=19000 Z=16000 M=160""".splitlines()


# def eni3(n, exp, mod):
#     result = 0
#     for i in range(exp):
#         score = pow(n, exp - i, mod)
#         # print(f"{score=}")
#         result += score
#     return result


# Cycles?
# def eni3(n, exp, mod):
#     firsts = {}  # score -> i
#     cycle_lengths = {}  # score -> i
#     for i in range(3 * mod):
#         score = pow(n, i + 1, mod)

#         if score in cycle_lengths:
#             continue

#         if score in firsts:
#             cycle_length = i - firsts[score] + 1
#             cycle_lengths[score] = cycle_length
#         else:
#             firsts[score] = i

#     print(f"{firsts=}")
#     print(f"{cycle_lengths=}")
#     return 0  # TODO


def eni3_debug(n, exp, mod):
    result = 0
    for i in range(exp):
        score = pow(n, i + 1, mod)
        print(f"{score=}")
        result += score
    return result


# Bug - assumes cycle starts at first element
# def eni3(n, exp, mod):
#     seen = {}  # score -> i
#     result = 0
#     for i in range(exp):
#         score = pow(n, i + 1, mod)

#         if score in seen:
#             to_move = exp // i  # off by 1?
#             print(f"{i=} {seen[score]} {score=} {to_move=}")
#             result = to_move * result
#             i = i * to_move
#             break
#         else:
#             result += score
#             seen[score] = i

#     for i in range(i, exp):
#         score = pow(n, i + 1, mod)
#         result += score

#     return result


def eni3(n, exp, mod):
    seen = {}  # score -> (i, total)
    result = 0
    for i in range(exp):
        score = pow(n, i + 1, mod)

        if score in seen:
            cycle_length = i - seen[score][0]  # off by one?
            cycle_sum = result - seen[score][1] + score  # Add score before or after?
            remaining = exp - i  # Off by one?
            n_cycles = remaining // cycle_length

            # print(
            #     f"{i=} {seen[score]} {score=} {cycle_length=} {cycle_sum=} {remaining=} {n_cycles=}"
            # )
            result += n_cycles * cycle_sum
            i += n_cycles * cycle_length
            break
        else:
            result += score
            seen[score] = (i, result)

    # print(f"continuing from {i=}")
    for i in range(i, exp):
        score = pow(n, i + 1, mod)
        result += score

    return result


# eni3(2, 7, 5)
# eni3(3, 8, 16)


# eni3(4, 3000, 110)

# # Simpler example
# eni3(8, 6, 160)  # This is correct now
# eni3_debug(8, 6, 160)


# # Simpler example
# eni3(8, 10, 160)
# eni3_debug(8, 10, 160)

# eni3(8, 16000, 160)  # Incorrect - cycle doesn't start at first element
# eni3_debug(8, 16000, 160)  # Incorrect

# eni3(8, 16000, 160)  # Incorrect - too high
# eni3_debug(8, 16000, 160)  # Incorrect

answer3 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    print(a, b, c, x, y, z, m)
    answer3 = max(answer3, eni3(a, x, m) + eni3(b, y, m) + eni3(c, z, m))

print(answer3)
