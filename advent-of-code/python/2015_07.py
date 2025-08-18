from aocd import get_data

inp = get_data(day=7, year=2015)

from collections import defaultdict

configuration = {line.split(' ')[-1]: line.split(' ') for line in inp.split('\n')}
cache = defaultdict(lambda: None)

def get_signal(wire):
  if cache[wire] is not None:
    return cache[wire]
  
  try:
    return int(wire)
  except ValueError:
    pass
  
  conf = configuration[wire]
  
  if len(conf) == 3: # Set
    cache[wire] = get_signal(conf[0])
  elif conf[1] == 'AND':
    cache[wire] = get_signal(conf[0]) & get_signal(conf[2])
  elif conf[1] == 'OR':
    cache[wire] = get_signal(conf[0]) | get_signal(conf[2])
  elif conf[1] == 'LSHIFT':
    cache[wire] = get_signal(conf[0]) << get_signal(conf[2])
  elif conf[1] == 'RSHIFT':
    cache[wire] = get_signal(conf[0]) >> get_signal(conf[2])
  elif conf[0] == 'NOT':
    cache[wire] = ~get_signal(conf[1])
  
  return cache[wire]

answer = get_signal('a')
answer

cache = defaultdict(lambda: None)
cache['b'] = answer

answer = get_signal('a')
answer
