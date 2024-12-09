from aocd import get_data

inp = get_data(day=12, year=2018)

import re

def simulate(s, rules, n):
  r = re.compile('|'.join(f'(?<={x[0]}{x[1]}){x[2]}(?={x[3]}{x[4]})' for x, after in rules if after == '#'))
  for _ in range(n):
    s = '____' + s + '____'
    new_s = list(s.replace('#', '_'))
    
    for it in r.finditer(s):
      new_s[it.start(0)] = '#'
    s = ''.join(new_s)
  return sum(i - n * 4 for i, x in enumerate(s) if x == '#')

initial_state, rules = inp.replace('.', '_').split('\n\n')
initial_state = initial_state.split(': ')[1]
rules = [line.split(' => ') for line in rules.splitlines()]

answer = simulate(initial_state, rules, 20)
print(answer)

import numpy as np
import sklearn as sk

X = np.array(range(200, 250))[:,np.newaxis]
y = [simulate(initial_state, rules, n) for n in x]
m = sk.linear_model.LinearRegression().fit(X, y)

answer = int(m.predict([[50000000000]])[0])
print(answer)
