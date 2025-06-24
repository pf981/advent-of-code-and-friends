import collections

import downloader

lines = downloader.get_puzzle(28).splitlines()

prices: collections.defaultdict[str, int] = collections.defaultdict(int)
for line in lines:
    name, fee_type, price_str = line.split()
    name = name[:-1]
    price = int(price_str)

    assert fee_type in ["Seat", "Meals", "Luggage", "Fee", "Tax", "Discount", "Rebate"]
    if fee_type in ["Discount", "Rebate"]:
        price = -price

    prices[name] += price

answer = min(prices.values())
print(answer)
