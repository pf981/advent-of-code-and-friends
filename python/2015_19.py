from aocd import get_data

inp = get_data(day=19, year=2015)

import re

replacements, medicine_molecule = inp.split('\n\n')
replacements = [line.split(' => ') for line in replacements.split('\n')]

molecules = set()
for source, dest in replacements:
  for new_molecule in [medicine_molecule[:m.start()] + dest + medicine_molecule[m.end():] for m in re.finditer(source, medicine_molecule)]:
    molecules.add(new_molecule)

answer = len(molecules)
answer

import random

molecule = medicine_molecule
n_steps = 0

while molecule != 'e':
  random.shuffle(replacements)

  no_progress = True
  for source, dest in replacements:
    if dest in molecule:
      molecule = molecule.replace(dest, source, 1)
      n_steps += 1
      no_progress = False

  if no_progress:
    n_steps = 0
    molecule = medicine_molecule

answer = n_steps
answer
