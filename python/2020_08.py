from aocd import get_data

inp = get_data(day=8, year=2020)

instructions = [tuple(line.split()) for line in inp.splitlines()]

i = 0
acc = 0
seen = set()
while True:
  if i in seen:
    break
  seen.add(i)
    
  op, value = instructions[i]
  value = int(value)
  
  if op == 'nop':
    pass
  elif op == 'acc':
    acc += value
  elif op == 'jmp':
    i += value - 1
  
  i += 1
  
answer = acc
print(answer)

def solve(instructions):
  for changed in range(len(instructions)):
    inst = instructions.copy()
    if inst[changed][0] == 'jmp':
      inst[changed] = ('nop', inst[changed][1])
    elif inst[changed][0] == 'nop':
      inst[changed] = ('jmp', inst[changed][1])
    else:
      continue

    i = 0
    acc = 0
    seen = set()
    while True:
      if i == len(inst):
        return acc
  
      if i in seen:
        break
      seen.add(i)

      op, value = inst[i]
      value = int(value)

      if op == 'nop':
        pass
      elif op == 'acc':
        acc += value
      elif op == 'jmp':
        i += value - 1

      i += 1
  
answer = solve(instructions)
print(answer)
