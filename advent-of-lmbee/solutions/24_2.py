import itertools

with open("data/day24.txt") as f:
    text = f.read()

params = [int(x) for x in text.split()]
nums = []
for initial, b, c, mod, n in itertools.batched(params, 5):
    for _ in range(n):
        nums.append(initial)
        initial = (b * initial + c) % mod


n = len(nums)
left = [-1] * n
right = [n] * n

stack = []
for i, v in enumerate(nums):
    while stack and nums[stack[-1]] < v:
        stack.pop()
    left[i] = stack[-1] if stack else -1
    stack.append(i)

stack = []
for i in range(n - 1, -1, -1):
    v = nums[i]
    while stack and nums[stack[-1]] <= v:
        stack.pop()
    right[i] = stack[-1] if stack else n
    stack.append(i)

# Initially, disregard the increments. Just count how many times each base
# number appears in the pyramid.
total = 0
for i, v in enumerate(nums):
    d_left = i - left[i]
    d_right = right[i] - i
    # There are d_left ways to choose the start and d_right ways to choose the
    # end such that the pyramid with base start-to-end has the maximum value v.
    # Each of these pyramids has a uniquely positioned top node which is v.
    # These pyramids have v in other locations, but those are the top nodes of
    # other pyramids which are included. So include one node (the top) for each
    # of the pyramids.
    total += v * d_left * d_right

# Add the layer increments
total += n * (n - 1) * (n + 1) // 6

answer = total
print(answer)
