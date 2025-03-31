import collections


with open("2025_contest/16.txt") as f:
    inp = f.read()

# inp = '''ozNxANO | 576690
# pYNonIG | 323352
# MUantNm | 422646
# lOSlxki | 548306
# SDJtdpa | 493637
# ocWkKQi | 747973
# qfSKloT | 967749
# KGRZQKg | 661714
# JSXfNAJ | 499862
# LnDiFPd | 55528
# FyNcJHX | 9047
# UfWSgzb | 200543
# PtRtdSE | 314969
# gwHsSzH | 960026
# JoyLmZv | 833936

# MUantNm | 422646
# FyNcJHX | 9047
# '''

tree_s, other = inp.split('\n\n')
nodes = []
for line in tree_s.splitlines():
    code, _, artifact_id = line.split()
    nodes.append((code, int(artifact_id)))


import dataclasses
from __future__ import annotations

@dataclasses.dataclass
class Node:
    code: str
    artifact_id: int
    right: 'Node' | None = None
    left: 'Node' | None = None

def add_node(tree, node):
    if not tree:
        return node
    
    if node.artifact_id < tree.artifact_id:
        tree.left = add_node(tree.left, node)
    else:
        tree.right = add_node(tree.right, node)

    return tree

dummy = Node('', -1, None, None)
for code, artifact_id in nodes:
    dummy = add_node(dummy, Node(code, artifact_id))

head = dummy.right

q = collections.deque([head])
max_layer_sum = 0
max_layers = 0
while q:
    layer_sum = 0
    for _ in range(len(q)):
        node = q.popleft()
        layer_sum += node.artifact_id
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    max_layer_sum = max(max_layer_sum, layer_sum)
    max_layers += 1

answer1 = max_layer_sum * max_layers
print(answer1)


# Part 2

sequence = []
node = head
target = 500_000
while node:
    sequence.append(node.code)
    if target < node.artifact_id:
        node = node.left
    else:
        node = node.right

answer2 = '-'.join(sequence)
print(answer2)


# Part 3

def get_lowest_common_ancestor(tree, a, b):
    if not tree or tree.code == a or tree.code == b:
        return tree.code if tree else None

    l = get_lowest_common_ancestor(tree.left, a, b)
    r = get_lowest_common_ancestor(tree.right, a, b)

    if l and r:
      return tree.code if tree else None
    return l or r


a, b = [line.split()[0] for line in other.splitlines()]
answer3 = get_lowest_common_ancestor(head, a, b)
print(answer3)
