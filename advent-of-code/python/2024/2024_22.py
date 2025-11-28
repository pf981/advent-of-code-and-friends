from aocd import get_data, submit


def sim(num):
    mix_prune = lambda x, secret: (x ^ secret) % 16777216
    num = mix_prune(num * 64, num)
    num = mix_prune(num // 32, num)
    num = mix_prune(num * 2048, num)
    return num

inp = get_data(day=22, year=2024)
lines = inp.splitlines()
nums = [int(line) for line in lines]

answer1 = 0
for num in nums:
    for _ in range(2000):
        num = sim(num)
    answer1 += num
print(answer1)

submit(answer1, part='a', day=22, year=2024)


# Part 2


import collections


def get_prices_deltas(num, n):
    prices = []
    for _ in range(n):
        prices.append(num % 10)
        num = sim(num)
    deltas = tuple(a - b for a, b in zip(prices, [0] + prices[:-1]))
    return prices, deltas


streaks = collections.defaultdict(int) # tuple -> total_price
best = 0
for num in nums:
    prices, deltas = get_prices_deltas(num, 2000)
    seen = set()
    for i in range(2000 - 4):
        t = deltas[i:i + 4]
        if t in seen:
            continue
        seen.add(t)
        streaks[t] += prices[i + 4 - 1]
        best = max(best, streaks[t])

answer2 = best
print(answer2)

submit(answer2, part='b', day=22, year=2024)
