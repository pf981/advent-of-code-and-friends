with open("./input/problem-sep-25-long-D-input.txt") as f:
    text = f.read()

_, *nums = map(int, text.splitlines())


MOD = 1_000_000_009

result = []
for case, n in enumerate(nums, 1):
    side = 1 << n
    rectangles = pow((side * (side + 1) // 2), 2, MOD)
    result.append(f"Case #{case}: {rectangles}")

with open("./output/problem-sep-25-long-D.txt", "w") as f:
    f.write("\n".join(result))
