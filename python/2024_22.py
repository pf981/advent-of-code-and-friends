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

for _ in range(2000):
    for i, num in enumerate(nums):
        nums[i] = sim(num)

answer1 = sum(nums)
print(answer1)

submit(answer1, part='a', day=22, year=2024)


# Part 2


def get_prices_deltas(num, n):
    prices = []
    for _ in range(n):
        prices.append(num % 10)
        num = sim(num)
    deltas = [a - b for a, b in zip(prices, [0] + prices[:-1])]
    return prices, deltas


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

submit(answer2, part='b', day=22, year=2024)
