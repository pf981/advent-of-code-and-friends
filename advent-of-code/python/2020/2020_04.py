from aocd import get_data

inp = get_data(day=4, year=2020)

passports = [dict(pair.split(':') for pair in passport.replace('\n', ' ').split(' ')) for passport in inp.split('\n\n')]

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
n_valid = 0
for passport in passports:
  if not expected.difference(passport.keys()):
    n_valid += 1
    
answer = n_valid
print(answer)

import re

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
n_valid = 0
for passport in passports:
  if expected.difference(passport.keys()):
    continue
  if not (1920 <= int(passport['byr']) <= 2002):
    continue
  if not (2010 <= int(passport['iyr']) <= 2020):
    continue
  if not (2020 <= int(passport['eyr']) <= 2030):
    continue
  if not (passport['hgt'].endswith('cm') or passport['hgt'].endswith('in')):
    continue
  if passport['hgt'].endswith('cm') and not (150 <= int(passport['hgt'][:-2]) <= 193):
    continue
  if passport['hgt'].endswith('in') and not (59 <= int(passport['hgt'][:-2]) <= 76):
    continue
  if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
    continue
  if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    continue
  if not re.fullmatch(r'[0-9]{9}', passport['pid']):
    continue
    
  n_valid += 1
    
answer = n_valid
print(answer)
