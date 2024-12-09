from aocd import get_data

inp = get_data(day=10, year=2015)

def look_and_say(s):
  result = ''
  i = 0;
  while i < len(s):
    n = 1
    while i+n < len(s) and s[i+n] == s[i]:
      n += 1
    result += str(n) + s[i]
    i += n
  return result

def solve(s, n):
  for _ in range(n):
    s = look_and_say(s)
  return len(s)

answer = solve(inp, 40)
answer

answer = solve(inp, 50)
answer
