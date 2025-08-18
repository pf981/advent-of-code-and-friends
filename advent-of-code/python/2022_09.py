from aocd import get_data

inp = get_data(day=9, year=2022)

def to_unit(x):
  return (x > 0) - (x < 0)


def count_tail_visits(rope_length, instructions):
  rope = [[0, 0] for _ in range(rope_length)]
  visited = {(0, 0)}
  
  for direction, d in instructions:
    for _ in range(int(d)):
      rope[0][0] += (direction == 'D') - (direction == 'U')
      rope[0][1] += (direction == 'R') - (direction == 'L')
      
      for head, tail in zip(rope[:-1], rope[1:]):
        dr = head[0] - tail[0]
        dc = head[1] - tail[1]
        
        if abs(dr) > 1 or abs(dc) > 1:
          tail[0] += to_unit(dr)
          tail[1] += to_unit(dc)

      visited.add(tuple(rope[-1]))

  return len(visited)


instructions = [line.split(' ') for line in inp.splitlines()]

answer = count_tail_visits(2, instructions)
print(answer)

answer = count_tail_visits(10, instructions)
print(answer)
