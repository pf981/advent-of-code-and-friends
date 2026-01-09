import collections
import itertools
import math
import re

with open("data/day22.txt") as f:
    text = f.read()

users = list(itertools.batched(map(int, re.findall(r"\d+", text)), 3))

answer = 0
for _, fav_digit, fav_num in users:
    dp = collections.Counter()  # (n_fav, remainder_mod_m) -> count
    dp[(0, 0)] = 1

    for n_digits in range(1, 16 + 1):
        dp_next = collections.Counter()

        for (n_fav, rem), count in dp.items():
            if n_fav >= n_digits:
                continue

            for digit in range(0, 9 + 1):
                if n_digits <= 1 and digit <= 0:
                    continue
                n_fav_next = min(8, n_fav + (digit == fav_digit))
                rem_next = (rem * 10 + digit) % fav_num
                dp_next[(n_fav_next, rem_next)] += count

        if 8 <= n_digits <= 16:
            for n_fav in range(math.ceil(n_digits / 2), min(n_digits, 8) + 1):
                answer += dp_next[(n_fav, 0)]

        dp = dp_next

print(answer)
