import itertools

import downloader

nums = [int(num) for num in downloader.get_puzzle(30).split()]

it = itertools.cycle(".#")
output = []
for num in nums:
    output.append(next(it) * num)

for line in itertools.batched("".join(output), 100):
    print("".join(line))


answer = "4951"
print(answer)
