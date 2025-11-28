from aocd import get_data

inp = get_data(day=23, year=2015)

import re

instructions = [re.findall(r'[^, ]+', line) for line in inp.split('\n')]

def run_instructions(instructions, registers):
  i = 0
  while i < len(instructions):
    instruction, *args = instructions[i]
    
    if instruction == 'hlf':
      registers[args[0]] = registers[args[0]] / 2
    elif instruction == 'tpl':
      registers[args[0]] = registers[args[0]] * 3
    elif instruction == 'inc':
      registers[args[0]] += 1
    elif instruction == 'jmp':
      i += int(args[0]) - 1
    elif instruction == 'jie':
      if registers[args[0]] % 2 == 0:
        i += int(args[1]) - 1
    elif instruction == 'jio':
      if registers[args[0]] == 1:
        i += int(args[1]) - 1
    
    i += 1
    

registers = {'a': 0, 'b': 0}
run_instructions(instructions, registers)
answer = registers['b']
answer

registers = {'a': 1, 'b': 0}
run_instructions(instructions, registers)
answer = registers['b']
answer
