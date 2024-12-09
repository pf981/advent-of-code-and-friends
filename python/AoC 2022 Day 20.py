from aocd import get_data

inp = get_data(day=20, year=2022)

import collections

def mix(deque):
  for i in range(len(deque)):
    while deque[0][1] != i:
      deque.rotate(-1)

    num, _ = deque.popleft()
    deque.rotate(-num)
    deque.appendleft((num, i))

start_deque = collections.deque((int(num), i) for i, num in enumerate(inp.splitlines()))
deque = start_deque.copy()
mix(deque)

nums = [num for num, _ in deque]
zero_i = nums.index(0)
answer = sum(nums[(zero_i + di) % len(nums)] for di in [1000, 2000, 3000])
print(answer) # 2 seconds

deque = collections.deque((num * 811589153, i) for num, i in start_deque)
for _ in range(10):
  mix(deque)

nums = [num for num, _ in deque]
zero_i = nums.index(0)
answer = sum(nums[(zero_i + di) % len(nums)] for di in [1000, 2000, 3000])
print(answer) # 20 seconds
