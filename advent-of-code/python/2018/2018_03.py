from aocd import get_data

inp = get_data(day=3, year=2018)

import collections
import re

claim_info = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.splitlines()]
claims = collections.defaultdict(list)

for claim_id, left, top, width, height in claim_info:
  for row in range(top + 1, top + height + 1):
    for col in range(left + 1, left + width + 1):
      claims[(row, col)].append(claim_id)

answer = sum(len(claim) >= 2 for claim in claims.values())
print(answer)

good_claims = {l[0] for l in claims.values() if len(l) == 1}
bad_claims = {claim for l in claims.values() if len(l) > 1 for claim in l}

answer = (good_claims - bad_claims).pop()
print(answer)
