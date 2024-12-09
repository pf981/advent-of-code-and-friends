from aocd import get_data

inp = get_data(day=19, year=2021)

import re
import itertools


def rotations(scanner):
  for signs in itertools.product(*([[-1, 1]] * 3)):
    for indices in itertools.permutations(range(3)):
      yield {
        tuple(sign * position[index] for sign, index in zip(signs, indices))
        for position in scanner
      }
                    

def find_position(scanner, beacon_positions):
  for rotated_scanner in rotations(scanner):
    for x, y, z in rotated_scanner:
      for bx, by, bz in beacon_positions:
        dx, dy, dz = x - bx, y - by, z - bz

        positioned_scanner = {(x - dx, y - dy, z - dz) for x, y, z in rotated_scanner}

        n_overlap = len(beacon_positions.intersection(positioned_scanner))
        if n_overlap >= 12:
          return positioned_scanner, (dx, dy, dz)

  return None, None
        
        
def get_positions(scanners):
  beacon_positions = scanners[0].copy()
  scanner_positions = [(0, 0, 0)]
  done = {0}
  while len(done) < len(scanners):
    for i, scanner in enumerate(scanners):
      if i in done:
        continue

      new_beacon_positions, scanner_position = find_position(scanner, beacon_positions)
      if new_beacon_positions:
        beacon_positions.update(new_beacon_positions)
        scanner_positions.append(scanner_position)
        done.add(i)
        
  return scanner_positions, beacon_positions


scanners = [
  {
    tuple(int(x) for x in re.findall(r'-?\d+', line))
    for i, line in enumerate(block.splitlines())
    if i != 0
  }
  for block in inp.split('\n\n')
]

scanner_positions, beacon_positions = get_positions(scanners)

answer = len(beacon_positions)
print(answer)

max_manhattan = max(
  abs(x - x2) + abs(y - y2) + abs(z - z2)
  for x, y ,z in scanner_positions
  for x2, y2, z2 in scanner_positions
)

answer = max_manhattan
print(answer)
