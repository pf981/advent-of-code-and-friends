from aocd import get_data

inp = get_data(day=6, year=2022)

def find_start(buffer, marker_length):
  for i in range(marker_length, len(buffer) + 1):
    s = set(inp[i - marker_length:i])
    if len(s) == marker_length:
      return i

answer = find_start(inp, 4)
print(answer)

answer = find_start(inp, 14)
print(answer)
