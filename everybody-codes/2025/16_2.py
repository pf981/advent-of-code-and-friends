with open("./2025/input/everybody_codes_e2025_q16_p2.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2""".splitlines()

nums = [int(x) for x in lines[0].split(",")]
magnatude = nums.copy()
n = len(nums)
cols = [0] * n
answer = 1
for i in range(len(nums)):
    # print(f"{magnatude=}")
    num = i + 1
    mag = magnatude[i]
    if magnatude[i] == 0:
        continue

    answer *= mag * num

    for x in range(num - 1, n, num):
        cols[x] += mag
        magnatude[x] -= mag


print(answer)
