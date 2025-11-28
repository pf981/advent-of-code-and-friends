from aocd import get_data

inp = get_data(day=16, year=2016)

def grow_bits(bits, length_out):
  while len(bits) < length_out:
    bits += [False] + [not x for x in bits[::-1]]
  return bits[:length_out]

def checksum(bits):
  while len(bits) % 2 != 1:
    bits = [a == b for a, b in zip(*[iter(bits)] * 2)]
  return bits

def solve(bits, length_out):
  bits = grow_bits(bits, length_out)
  bits = checksum(bits)
  return ''.join(str(int(x)) for x in bits)

bits = [c == '1' for c in inp]

answer = solve(bits, 272)
answer

answer = solve(bits, 35651584)
answer
