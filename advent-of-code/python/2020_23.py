from aocd import get_data

inp = get_data(day=23, year=2020)

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Node:
  value: int
  nxt: Optional[Node]


def to_nodes(nums):
  nodes = {}
  for num in nums:
    nodes[num] = Node(num, None)
  
  for cur, nxt in zip(nums, nums[1:] + nums[0:1]):
    nodes[cur].nxt = nodes[nxt]
  
  return nodes


def simulate_moves(nodes, head, n_moves):
  for _ in range(n_moves):
    pick_up = head.nxt
    head.nxt = pick_up.nxt.nxt.nxt
    
    dest_value = head.value - 1 or len(nodes)
    while dest_value in [pick_up.value, pick_up.nxt.value, pick_up.nxt.nxt.value]:
      dest_value = (dest_value - 1) or len(nodes)

    dest = nodes[dest_value]
    
    pick_up.nxt.nxt.nxt = dest.nxt
    dest.nxt = pick_up
    head = head.nxt
  

def to_list(nodes, length):
  result = []
  cur = nodes[1]
  for _ in range(length):
    cur = cur.nxt
    result.append(cur.value)
  return result

  
cups = [int(x) for x in inp]
nodes = to_nodes(cups)
simulate_moves(nodes, nodes[cups[0]], 100)

answer = ''.join(str(value) for value in to_list(nodes, len(cups) - 1))
print(answer)

nodes = to_nodes(cups + list(range(max(cups) + 1, 1000001)))
simulate_moves(nodes, nodes[cups[0]], 10000000)
a, b = to_list(nodes, 2)

answer = a * b
print(answer) # 18 seconds
