with open("./input/problem-sep-25-long-E-input.txt") as f:
    text = f.read()

_, *nums = map(int, text.splitlines())

result = []
for case, n in enumerate(nums, 1):
    energy = 0

    i = 1
    while True:
        perfect_square = i * i
        next_perfect_square = (i + 1) * (i + 1)

        if next_perfect_square > n:
            d = n - perfect_square + 1
            energy += d * i
            break

        d = next_perfect_square - perfect_square

        energy += d * i
        i += 1

    result.append(f"Case #{case}: {energy}")


with open("./output/problem-sep-25-long-E.txt", "w") as f:
    f.write("\n".join(result))
