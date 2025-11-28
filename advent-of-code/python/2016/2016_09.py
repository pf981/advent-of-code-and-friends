from aocd import get_data

inp = get_data(day=9, year=2016)

import re

def decompressed_length(s, nested = True):
  parts = re.findall(r'(.*?)\((\d+)x(\d+)\)(.*)', s)
  if not parts:
    return len(s)
  
  before, n_chars, n_times, after = parts[0]
  f = decompressed_length if nested else len
  return len(before) + int(n_times) * f(after[:int(n_chars)]) + decompressed_length(after[int(n_chars):], nested)

answer = decompressed_length(inp, nested = False)
answer

answer = decompressed_length(inp, nested = True)
answer
