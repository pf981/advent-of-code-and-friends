from aocd import get_data

inp = get_data(day=14, year=2016)

import collections
import hashlib
import itertools
import re

def get_nth_key(salt, n, n_hashes = 1):
  triples = collections.defaultdict(list)
  keys = []

  for i in itertools.count():
    h = salt + str(i)
    for _ in range(n_hashes):
      h = hashlib.md5(h.encode()).hexdigest()

    for pentuple_letter in re.findall(r'(.)\1\1\1\1', h):
      triples[pentuple_letter] = [x for x in triples[pentuple_letter] if i <= x + 1000]
      keys += triples[pentuple_letter]
      if len(keys) >= n + 1:
        return sorted(keys)[n]

    if triple_letters := re.findall(r'(.)\1\1', h):
      triples[triple_letters[0]].append(i)
      
answer = get_nth_key(inp, 63)
answer

answer = get_nth_key(inp, 63, 2017)
answer
