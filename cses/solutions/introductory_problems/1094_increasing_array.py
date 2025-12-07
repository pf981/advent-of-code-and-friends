n, nums = open(0)
nums = [int(x) for x in nums.split()]

largest = nums[0]
moves = 0
for num in nums:
    moves += max(largest - num, 0)
    largest = max(largest, num)

print(moves)
