from aocd import get_data

inp = get_data(day=10, year=2016)

import re
from collections import defaultdict

two_chip_bots = set()
bots = defaultdict(lambda: {'has': [], 'gives_to': None})

for line in inp.split('\n'):
  args = re.findall(r'(?:output )?\d+', line)

  if line.startswith('value'):
    bots[args[1]]['has'].append(int(args[0]))

    if len(bots[args[1]]['has']) == 2:
      two_chip_bots.add(args[1])
  else:
    bots[args[0]]['gives_to'] = (args[1], args[2])

while two_chip_bots:
  bot_id = two_chip_bots.pop()
  bot = bots[bot_id]

  if 61 in bot['has'] and 17 in bot['has']:
    target_bot = bot_id

  for to_bot, to_value in zip(bot['gives_to'], sorted(bot['has'])):
    bots[to_bot]['has'].append(int(to_value))

    if len(bots[to_bot]['has']) == 2:
      two_chip_bots.add(to_bot)

        
answer = target_bot
answer

from math import prod

answer = prod(bots[f'output {x}']['has'][0] for x in range(3))
answer
