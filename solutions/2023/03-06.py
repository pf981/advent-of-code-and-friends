import collections
import math

import downloader

lines = downloader.get_puzzle(18).splitlines()

totals: collections.Counter[str] = collections.Counter()
for line in lines:
    _, quantity_str, category = line.split()
    quantity = int(quantity_str)

    totals[category] += quantity

answer = math.prod(total % 100 for total in totals.values())
print(answer)
