with open("./input/11.txt") as f:
    text = f.read()

nums = [int(s, 16) for s in text.split()]

output = []
i = 0
while i < len(nums):
    num = nums[i]

    if num != 0xFF:
        output.append(chr(num))
        i += 1
        continue

    start = len(output) - nums[i + 1]
    for j in range(nums[i + 2]):
        output.append(output[start + j])
    i += 3

answer = len(output)
print(answer)
