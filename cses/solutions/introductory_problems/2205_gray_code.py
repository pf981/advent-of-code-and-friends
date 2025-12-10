n = int(input())
nums = [0]
mask = 1
for _ in range(n):
    for i in reversed(range(len(nums))):
        nums.append(nums[i] | mask)
    mask <<= 1

for num in nums:
    print(f"{num:>0{n}b}")
