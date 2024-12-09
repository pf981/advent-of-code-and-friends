from aocd import get_data

inp = get_data(day=19, year=2020)

import functools


def build_logic(rule_id, rules):
  if isinstance(rule_id, str):
    return rule_id

  result = []
  for rule_group in rules[rule_id]:
    rule_group_result = []
    for sub_rule in rule_group:
      split = build_logic(sub_rule, rules)
      rule_group_result.append(split)
      
    result.append(tuple(rule_group_result))

  return tuple(result)


@functools.cache
def get_solutions(s, logic):
  if not s:
    return [] if logic else ['']
  if not logic:
    return [s]
  
  if isinstance(logic, str):
    return [s[1:]] if s[0] == logic else []
  
  solutions = []
  for sub_rules in logic[0]:
    for s2 in get_solutions(s, sub_rules):
      solutions.extend(get_solutions(s2, logic[1:]))
  return solutions


rules, messages = inp.split('\n\n')
rules = {int(rule.split(': ')[0]): [[x.strip('"') if not x.isdigit() else int(x) for x in l.split(' ')] for l in rule.split(': ')[1].split(' | ')] for rule in rules.splitlines()}
messages = messages.splitlines()

logic0 = build_logic(0, rules)
answer = 0
for message in messages:
  answer += any('' in get_solutions(message, part) for part in logic0)
print(answer)

rules[8] = [[42],[42,42],[42,42,42],[42,42,42,42],[42,42,42,42,42],[42,42,42,42,42,42],[42,42,42,42,42,42,42],[42,42,42,42,42,42,42,42],[42,42,42,42,42,42,42,42,42],[42,42,42,42,42,42,42,42,42,42],[42,42,42,42,42,42,42,42,42,42,42]]
rules[11] = [[42,31],[42,42,31,31],[42,42,42,31,31,31],[42,42,42,42,31,31,31,31],[42,42,42,42,42,31,31,31,31,31],[42,42,42,42,42,42,31,31,31,31,31,31],[42,42,42,42,42,42,42,31,31,31,31,31,31,31],[42,42,42,42,42,42,42,42,31,31,31,31,31,31,31,31],[42,42,42,42,42,42,42,42,42,31,31,31,31,31,31,31,31,31],[42,42,42,42,42,42,42,42,42,42,31,31,31,31,31,31,31,31,31,31]]

logic0 = build_logic(0, rules)
answer = 0
for message in messages:
  answer += any('' in get_solutions(message, part) for part in logic0)
print(answer) # 8 seconds
