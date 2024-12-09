from aocd import get_data

inp = get_data(day=7, year=2017)

import re

programs = {}
for line in inp.split("\n"):
    program, weight, *children = re.findall(r"\w+", line)
    programs[program] = [int(weight), tuple(children)]

root = set(programs) - {child for _, children in programs.values() for child in children}
root = [*root][0]

answer = root
print(answer)

import collections
import copy

def get_total_weight(node, programs):
    weight, children = programs[node]
    return weight + sum(get_total_weight(child, programs) for child in children)

def is_balanced(node, programs):
    weight, children = programs[node]
    children_weight = [get_total_weight(child, programs) for child in children]

    if not children or len(set(children_weight)) == 1:
        return True
    return False

def is_fully_balanced(programs, node=root):
    _, children = programs[node]
    return is_balanced(node, programs) and all(is_fully_balanced(programs, child) for child in children)
  
def fix_weight(node, programs, weight_change):
  new_programs = copy.deepcopy(programs)
  new_programs[node][0] += weight_change
  if is_fully_balanced(new_programs):
    return new_programs[node][0]
  
  for child in programs[node][1]:
    result = fix_weight(child, programs, weight_change)
    if result:
      return result
  return None

def solve(root, programs):
  _, root_children = programs[root]
  root_children_weight = [get_total_weight(child, programs) for child in root_children]
  counts = collections.Counter(root_children_weight).most_common()
  
  expected_weight = counts[0][0]
  unbalanced_child_weight = counts[1][0]
  unbalanced_child = root_children[root_children_weight.index(unbalanced_child_weight)]
  
  weight_change = expected_weight - unbalanced_child_weight
  return fix_weight(unbalanced_child, programs, weight_change)

answer = solve(root, programs)
print(answer)
