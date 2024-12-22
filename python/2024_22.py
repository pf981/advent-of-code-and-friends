from aocd import get_data, submit


inp = get_data(day=22, year=2024)

# inp = '''1
# 10
# 100
# 2024
# '''
# inp = '''1
# 2
# 3
# 2024
# '''

lines = inp.splitlines()
nums = [int(x) for x in lines]

def mix_prune(num, secret):
    num = num ^ secret
    return num % 16777216

def sim(num):
    num = mix_prune(num * 64, num)
    num = mix_prune(num // 32, num)
    num = mix_prune(num * 2048, num)
    return num

# sim(sim(123))

for _ in range(2000):
    for i, num in enumerate(nums):
        nums[i] = sim(num)

answer1 = sum(nums)
print(answer1)

# submit(answer1, part='a', day=22, year=2024)


# Part 2

from aocd import get_data, submit


inp = get_data(day=22, year=2024)

# inp = '''1
# 2
# 3
# 2024
# '''

lines = inp.splitlines()
nums = [int(x) for x in lines]

def mix_prune(num, secret):
    num = num ^ secret
    return num % 16777216

def sim(num):
    num = mix_prune(num * 64, num)
    num = mix_prune(num // 32, num)
    num = mix_prune(num * 2048, num)
    return num



import functools
@functools.cache
def get_prices_deltas(num, n):
    result = []
    for _ in range(n):
        result.append(num % 10)
        num = sim(num)
    x = result
    return result, [a - b for a, b in zip(x, [0] + x[:-1])]

options = set()
first_seen = {} # (i (nums index), tuple) -> price
for i, num in enumerate(nums):
    prices, deltas = get_prices_deltas(nums[i], 2000)
    for j in range(2000 - 4):
        t = tuple(deltas[j:j+4])
        options.add(t)
        if (i, t) in first_seen:
            continue
        first_seen[(i, t)] = prices[j+4-1]

# assert all(len(o) == 4 for o in options)

best = 0
for t in options:
    cur = 0
    for i, _ in enumerate(nums):
        if (i, t) not in first_seen:
            continue
        cur += first_seen[(i, t)]
    best = max(best, cur)
answer2 = best
print(answer2)

# submit(answer2, part='b', day=22, year=2024)

# first_seen[(0, (-2,1,-1,3))]


# import functools
# @functools.cache
# def get_prices_deltas(num, n):
#     result = []
#     for _ in range(n):
#         result.append(num % 10)
#         num = sim(num)
#     x = result
#     return result, [a - b for a, b in zip(x, [0] + x[:-1])]

# options = set()
# for i, num in enumerate(nums):
#     prices, deltas = get_prices_deltas(nums[i], 2000)
#     for i in range(2000 - 4):
#         t = tuple(deltas[i:i+4])
#         if 0 in t:
#             continue
#         options.add(t)

# # assert all(len(o) == 4 for o in options)

# best = 0
# # options = [(-2,1,-1,3)]
# for o in options:
#     cur = 0
#     for num in nums:
#         prices, deltas = get_prices_deltas(num, 2000)
#         for j in range(2000 - 4):
#             if tuple(deltas[j:j+4]) == o:
#                 cur += prices[j+4-1]
#                 # print(f'{cur=}')
#                 break
#     best = max(best, cur)
#     # if cur == 24:
#     #     print(f'{cur=} {o=}')
# answer2 = best
# print(answer2)

# submit(answer2, part='b', day=22, year=2024)


# o = (1, -3, 5, 1)
# for num in nums:
#     prices, deltas = get_prices_deltas(num, 2000)
#     for j in range(2000 - 4):
#         if tuple(deltas[j:j+4]) == o:
#             print(f'{prices[j:j+4]=} {deltas[j:j+4]=} {j=}')
#             break


# 1 # 1
# sim(1) # 3 -> 2
# sim(sim(1)) # 3 -> 1

# def pp(num, n):
#     result = []
#     for _ in range(n):
#         result.append(num % 10)
#         num = sim(num)
#     x = result
#     return result, [a - b for a, b in zip(x, [0] + x[:-1])]
#     # return list(zip(result, [a - b for a, b in zip(x, [0] + x[:-1])]))
#     # return [a - b for a, b in zip(x, [0] + x[:-1])]


# # pp(123, 10)

# prices, deltas = pp(1, 2000)
# for i in range(len(deltas)):
#     # if seq[i:i+4] == [2,-1,1,-3]:
#     if deltas[i:i+4] == [-2,1,-1,3]:
#         print(prices[i:i+4])


# prices, deltas = pp(3, 2000)
# for i in range(len(deltas)):
#     # if seq[i:i+4] == [2,-1,1,-3]:
#     if deltas[i:i+4] == [-2,1,-1,3]:
#         print(prices[i:i+4])


# prices, deltas = pp(2024, 2000)
# for i in range(len(deltas)):
#     # if seq[i:i+4] == [2,-1,1,-3]:
#     if deltas[i:i+4] == [-2,1,-1,3]:
#         print(prices[i:i+4])




# pp(1, 100)

# x

# num = 1
# for _ in range(1)

# 123 # 3
# sim(123) # 0 -> -3
# sim(sim(123)) # 6 -> +6

# # answer2 = 'todo'
# # print(answer2)

# # submit(answer2, part='b', day=22, year=2024)
