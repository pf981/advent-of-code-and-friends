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


def can_build(wall_length: int, total_blocks: int, spell: list[int]) -> bool:
    ncols = 0
    for num in spell:
        ncols += len(range(num - 1, wall_length, num))

    return ncols <= total_blocks


with open("./2025/input/everybody_codes_e2025_q16_p3.txt") as f:
    text = f.read().strip()
total_blocks = 202520252025000

cols = [int(x) for x in text.split(",")]
spell = infer_spell(cols)

left = 0
right = total_blocks
answer = 0
while left <= right:
    m = (left + right) // 2
    if can_build(m, total_blocks, spell):
        answer = m
        left = m + 1
    else:
        right = m - 1
print(answer)
