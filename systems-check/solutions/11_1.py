with open("./input/11.txt") as f:
    text = f.read()
# text = """6E 65 76 65 72 20 67 6F 6E 6E 61 20 67 69 76 65 20 79 6F 75 20 75 70 20 FF 18 0C 6C 65 74 20 79 6F 75 20 64 6F 77 6E 20 FF 19 0C 72 75 6E 20 61 72 6F 75 6E 64 20 61 6E 64 20 64 65 73 65 72 74 20 79 6F 75 20 FE 45 45 FE 48 48 FE 4B 4B"""

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

print("".join(output))
answer = len(output)
print(answer)
