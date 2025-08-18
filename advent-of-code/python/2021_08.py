from aocd import get_data

inp = get_data(day=8, year=2021)

import re

displ = [
    [
        [frozenset(s) for s in re.findall(r'[a-g]+', part)]
        for part in line.split(' | ')
    ]
    for line in inp.splitlines()
]

answer = sum(len(word) in [2, 4, 3, 7] for _, output in displ for word in output)
answer

import itertools

def map_segments(segments, mapping):
  return [frozenset(mapping[c] for c in s) for s in segments]

base_mapping = {
  frozenset('acedgfb'): 8,
  frozenset('cdfbe'): 5,
  frozenset('gcdfa'): 2,
  frozenset('fbcad'): 3,
  frozenset('dab'): 7,
  frozenset('cefabd'): 9,
  frozenset('cdfgeb'): 6,
  frozenset('eafb'): 4,
  frozenset('cagedb'): 0,
  frozenset('ab'): 1
}

output_total = 0
for segments_in, segments_out in displ:
  for replacement_letters in itertools.permutations('abcdefg', 7):
    mapping = dict(zip('abcdefg', replacement_letters))
    new_segments_in = map_segments(segments_in, mapping)
    new_segments_out = map_segments(segments_out, mapping)
    
    if set(new_segments_in + new_segments_out).issubset(base_mapping):
      output_total += int(''.join(str(base_mapping[s]) for s in new_segments_out))
      break

answer = output_total
print(answer)
