from aocd import get_data

inp = get_data(day=14, year=2018)

inp = 409551

import itertools

def get_scores(target_score):
  target_score = str(target_score)
  scores = '37'
  elf1_i = 0
  elf2_i = 1
  
  for n in itertools.count():
    for i in range(2 ** n):
      elf1_val = int(scores[elf1_i])
      elf2_val = int(scores[elf2_i])

      scores += str(elf1_val + elf2_val)

      elf1_i = (elf1_i +  elf1_val + 1) % len(scores)
      elf2_i = (elf2_i +  elf2_val + 1) % len(scores)
      
    if target_score in scores:
      return scores
  
scores = get_scores(inp)
  
answer = scores[inp:inp+10]
print(answer)

answer = scores.index(str(inp))
print(answer)
