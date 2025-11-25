import math


def infer_spell(cols: list[int]) -> list[int]:
    n = len(cols)
    spell = []
    for i in range(n):
        num = i + 1
        times = cols[i]
        if times == 0:
            continue

        spell.extend([num] * times)

        for j in range(num - 1, n, num):
            cols[j] -= times

    return spell


with open("./2025/input/everybody_codes_e2025_q16_p2.txt") as f:
    text = f.read().strip()


cols = [int(x) for x in text.split(",")]
spell = infer_spell(cols)

answer = math.prod(spell)
print(answer)
