from aocd import get_data

inp = get_data(day=14, year=2022)

def count_sand(rock):
  floor = max(y for x, y in rock)
  occupied = rock.copy()
  
  while True:
    pos = [500, 0]

    while True:
      if (pos[0], pos[1] + 1) not in occupied: # Down
        pos[1] += 1
      elif (pos[0] - 1, pos[1] + 1) not in occupied: # Down, Left
        pos[0] -= 1
        pos[1] += 1
      elif (pos[0] + 1, pos[1] + 1) not in occupied: # Down, Right
        pos[0] += 1
        pos[1] += 1
      else:
        occupied.add(tuple(pos))
        break

      if pos[1] > floor:
        return len(occupied) - len(rock)


paths = [[[int(x) for x in line.split(',')] for line in line2.split(' -> ')] for line2 in inp.splitlines()]
rock = set()

for path in paths:
  pos = path.pop(0)
  rock.add(tuple(pos))

  while path:
    end = path.pop(0)
    
    dx = end[0] - pos[0]
    dy = end[1] - pos[1]
    dx = (dx > 0) - (dx < 0)
    dy = (dy > 0) - (dy < 0)

    while pos != end:
      pos[0] += dx
      pos[1] += dy
      rock.add(tuple(pos))

answer = count_sand(rock)
print(answer)

def count_sand2(rock):
  floor = 2 + max(y for x, y in rock)
  occupied = rock.copy()
  
  while (500, 0) not in occupied:
    pos = [500, 0]

    while True:
      if pos[1] + 1 == floor:
        occupied.add(tuple(pos))
        break
      
      if (pos[0], pos[1] + 1) not in occupied: # Down
        pos[1] += 1
      elif (pos[0] - 1, pos[1] + 1) not in occupied: # Down, Left
        pos[0] -= 1
        pos[1] += 1
      elif (pos[0] + 1, pos[1] + 1) not in occupied: # Down, Right
        pos[0] += 1
        pos[1] += 1
      else:
        occupied.add(tuple(pos))
        break

  return len(occupied) - len(rock)

answer = count_sand2(rock)
print(answer)
