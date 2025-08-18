from __future__ import annotations
import collections
import dataclasses
import re


@dataclasses.dataclass
class Node:
    rank: int
    symbol: str
    left: Node | None
    right: Node | None


def get_message(root):
    result = ""
    q = collections.deque([root])
    while q:
        message = []
        for _ in range(len(q)):
            node = q.popleft()

            message.append(node.symbol)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        message = "".join(message)
        if len(message) > len(result):
            result = message

    return result


def place_node(root, node):
    if root is None:
        return node
    else:
        if node.rank < root.rank:
            root.left = place_node(root.left, node)
        else:
            root.right = place_node(root.right, node)
    return root


with open("./story_1/input/everybody_codes_e1_q02_p1.txt") as f:
    lines = f.read().splitlines()

left_root = None
right_root = None

for line in lines:
    _id, l_rank, l_symbol, r_rank, r_symbol = re.match(
        r"ADD id=(-?[0-9]+) left=\[(-?[0-9]+),(.)\] right=\[(-?[0-9]+),(.)\]",
        line,
    ).groups()

    _id = int(_id)
    l_rank = int(l_rank)
    r_rank = int(r_rank)

    left_root = place_node(left_root, Node(l_rank, l_symbol, None, None))
    right_root = place_node(right_root, Node(r_rank, r_symbol, None, None))

answer1 = get_message(left_root) + get_message(right_root)
print(answer1)


# Part 2


with open("./story_1/input/everybody_codes_e1_q02_p2.txt") as f:
    lines = f.read().splitlines()

left_root = None
right_root = None
m = {}

for line in lines:
    if line.startswith("SWAP"):
        _id = int(line.split()[1])
        l, r = m[_id]
        l.rank, r.rank = r.rank, l.rank
        l.symbol, r.symbol = r.symbol, l.symbol
        continue

    _id, l_rank, l_symbol, r_rank, r_symbol = re.match(
        r"ADD id=(-?[0-9]+) left=\[(-?[0-9]+),(.)\] right=\[(-?[0-9]+),(.)\]",
        line,
    ).groups()

    _id = int(_id)
    l_rank = int(l_rank)
    r_rank = int(r_rank)

    l_node = Node(l_rank, l_symbol, None, None)
    r_node = Node(r_rank, r_symbol, None, None)

    m[_id] = [l_node, r_node]

    left_root = place_node(left_root, l_node)
    right_root = place_node(right_root, r_node)


answer2 = get_message(left_root) + get_message(right_root)
print(answer2)


# Part 3


with open("./story_1/input/everybody_codes_e1_q02_p3.txt") as f:
    lines = f.read().splitlines()

left_root = None
right_root = None
m = {}

for line in lines:
    if line.startswith("SWAP"):
        _id = int(line.split()[1])
        l, r = m[_id]
        l.rank, r.rank = r.rank, l.rank
        l.symbol, r.symbol = r.symbol, l.symbol
        l.left, r.left = r.left, l.left
        l.right, r.right = r.right, l.right
        continue

    _id, l_rank, l_symbol, r_rank, r_symbol = re.match(
        r"ADD id=(-?[0-9]+) left=\[(-?[0-9]+),(.)\] right=\[(-?[0-9]+),(.)\]",
        line,
    ).groups()

    _id = int(_id)
    l_rank = int(l_rank)
    r_rank = int(r_rank)

    l_node = Node(l_rank, l_symbol, None, None)
    r_node = Node(r_rank, r_symbol, None, None)

    m[_id] = [l_node, r_node]

    left_root = place_node(left_root, l_node)
    right_root = place_node(right_root, r_node)


answer3 = get_message(left_root) + get_message(right_root)
print(answer3)
