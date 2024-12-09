from aocd import get_data

inp = get_data(day=25, year=2015)

import re

target_row, target_col = [int(x) for x in re.findall(r'\d+', inp)]

code =  20151125
row =  1
column =  1
lowest_row =  1

while not (row == target_row and column == target_col):
  code = (code * 252533) % 33554393
  if row == 1:
    lowest_row += 1
    row = lowest_row
    column = 1
  else:
    row -= 1
    column += 1

answer = code
answer

# No puzzle here - just need all the stars
