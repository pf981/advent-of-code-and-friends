from aocd import get_data

inp = get_data(day=3, year=2015)

def get_visited(directions):
  x = 0
  y = 0
  visited = {(x, y)}
  for direction in directions:
    x += int(direction == '>') - int(direction == '<')
    y += int(direction == 'v') - int(direction == '^')
    visited.add((x, y))
  return visited

answer = len(get_visited(inp))
answer

visited = get_visited(direction for i, direction in enumerate(inp) if i % 2 == 0)
visited.update(get_visited(direction for i, direction in enumerate(inp) if i % 2 != 0))
answer = len(visited)
answer
