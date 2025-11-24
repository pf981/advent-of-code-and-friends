with open("./2025/input/everybody_codes_e2025_q16_p1.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """1,2,3,5,9""".splitlines()
target = 90

nums = [int(x) for x in lines[0].split(",")]
n = target
cols = [0] * n
for num in nums:
    for x in range(num - 1, n, num):
        cols[x] += 1


answer = sum(cols)
print(answer)
