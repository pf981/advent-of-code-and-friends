from aocd import get_data

inp = get_data(day=21, year=2022)

import re
import z3

for name in set(re.findall(r'[a-z]+', inp)):
  exec(f"{name} = z3.Int('{name}')")

o = z3.Optimize()
for monkey in inp.replace(': ', ' == ').splitlines():
  exec(f"o.add({monkey})")
o.check()

answer = o.model().eval(root)
print(answer)

o = z3.Optimize()
for monkey in inp.replace(': ', ' == ').splitlines():
  if monkey.startswith('humn'):
    continue
  
  if monkey.startswith('root'):
    monkey = monkey.split(' == ')[1].replace('+', '==')
  exec(f"o.add({monkey})")
o.check()

answer = o.model().eval(humn)
print(answer)
