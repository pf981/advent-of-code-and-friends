from aocd import get_data

inp = get_data(day=17, year=2021)

import re

def get_highest_success_y(dx, dy, target_x1, target_x2, target_y1, target_y2):
  x = y = 0
  highest_y = 0
  while x <= target_x2 and y >= target_y1 and not (dx == 0 and x < target_x1):
    x += dx
    y += dy
    
    if dx > 0:
      dx -=1
    elif dx < 0:
      dx +=1
    dy -= 1
    
    highest_y = max(highest_y, y)
      
    if target_x1 <= x <= target_x2 and target_y1 <= y <= target_y2:
      return highest_y
  return None


target_x1, target_x2, target_y1, target_y2 = (int(x) for x in re.findall(r'-?\d+', inp))

global_highest_y = 0
total = 0
for dx in range(target_x2 + 1):
  for dy in range(target_y1, 3000):
    highest_y = get_highest_success_y(dx, dy, target_x1, target_x2, target_y1, target_y2)
    
    if highest_y is not None:
      global_highest_y = max(global_highest_y, highest_y)
      total += 1

answer = global_highest_y
print(answer)

answer = total
print(total)
