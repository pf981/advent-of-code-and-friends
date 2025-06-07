import re


with open("./story_1/input/everybody_codes_e1_q01_p1.txt") as f:
    lines = f.read().splitlines()


def eni(n, exp, mod):
    result = []
    score = 1
    for _ in range(exp):
        score2 = (score * n) % mod
        result.append(str(score2))
        score = score2
    return int("".join(reversed(result)))


answer1 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    answer1 = max(answer1, eni(a, x, m) + eni(b, y, m) + eni(c, z, m))

print(answer1)


# Part 2


with open("./story_1/input/everybody_codes_e1_q01_p2.txt") as f:
    lines = f.read().splitlines()


def eni2(n, exp, mod):
    result = []
    for i in range(5):
        score = pow(n, exp - i, mod)
        result.append(str(score))
    return int("".join((result)))


answer2 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    answer2 = max(answer2, eni2(a, x, m) + eni2(b, y, m) + eni2(c, z, m))

print(answer2)


# Part 3


with open("./story_1/input/everybody_codes_e1_q01_p3.txt") as f:
    lines = f.read().splitlines()


def eni3(n, exp, mod):
    seen = {}  # score -> (i, total)
    result = 0
    for i in range(exp):
        score = pow(n, i + 1, mod)

        if score in seen:
            cycle_length = i - seen[score][0]
            cycle_sum = result - seen[score][1] + score
            remaining = exp - i
            n_cycles = remaining // cycle_length

            result += n_cycles * cycle_sum
            i += n_cycles * cycle_length
            break
        else:
            result += score
            seen[score] = (i, result)

    for i in range(i, exp):
        score = pow(n, i + 1, mod)
        result += score

    return result


answer3 = 0
for line in lines:
    a, b, c, x, y, z, m = (int(x) for x in re.findall(r"-?[0-9]+", line))
    answer3 = max(answer3, eni3(a, x, m) + eni3(b, y, m) + eni3(c, z, m))

print(answer3)
