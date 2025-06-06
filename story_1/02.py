import collections
import dataclasses
import re
import typing


@dataclasses.dataclass
class Node:
    rank: int
    symbol: str
    left: typing.Optional["Node"]
    right: typing.Optional["Node"]


def get_levels(root):
    levels = [[root]]
    while True:
        level = []
        for node in levels[-1]:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        if not level:
            break
        levels.append(level)

    result = []
    best = ""
    for level in levels:
        line = "".join(node.symbol for node in level)
        result.append(line)

        if len(line) > len(best):
            best = line
    return best


with open("./story_1/input/q02_p1.txt") as f:
    lines = f.read().splitlines()


# lines = """ADD id=1 left=[10,A] right=[30,H]
# ADD id=2 left=[15,D] right=[25,I]
# ADD id=3 left=[12,F] right=[31,J]
# ADD id=4 left=[5,B] right=[27,L]
# ADD id=5 left=[3,C] right=[28,M]
# ADD id=6 left=[20,G] right=[32,K]
# ADD id=7 left=[4,E] right=[21,N]""".splitlines()


def place_node(root, node):
    if root is None:
        return node
    else:
        if node.rank < root.rank:
            root.left = place_node(root.left, node)
        else:
            root.right = place_node(root.right, node)
    return root


left_root = None
right_root = None

for line in lines:
    print(f"{line=}")
    _id, l_rank, l_symbol, r_rank, r_symbol = re.match(
        r"ADD id=(-?[0-9]+) left=\[(-?[0-9]+),(.)\] right=\[(-?[0-9]+),(.)\]",
        line,
    ).groups()

    _id = int(_id)
    l_rank = int(l_rank)
    r_rank = int(r_rank)
    # print(id, l_rank, l_symbol, r_rank, r_symbol)

    left_root = place_node(left_root, Node(l_rank, l_symbol, None, None))
    right_root = place_node(right_root, Node(r_rank, r_symbol, None, None))


answer1 = get_levels(left_root) + get_levels(right_root)
print(answer1)


with open("./story_1/input/q02_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """ADD id=1 left=[10,A] right=[30,H]
# ADD id=2 left=[15,D] right=[25,I]
# ADD id=3 left=[12,F] right=[31,J]
# ADD id=4 left=[5,B] right=[27,L]
# ADD id=5 left=[3,C] right=[28,M]
# SWAP 1
# SWAP 5
# ADD id=6 left=[20,G] right=[32,K]
# ADD id=7 left=[4,E] right=[21,N]""".splitlines()


left_root = None
right_root = None
m = {}

for line in lines:
    print(f"{line=}")

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
    # print(id, l_rank, l_symbol, r_rank, r_symbol)

    l_node = Node(l_rank, l_symbol, None, None)
    r_node = Node(r_rank, r_symbol, None, None)

    m[_id] = [l_node, r_node]

    left_root = place_node(left_root, l_node)
    right_root = place_node(right_root, r_node)


answer2 = get_levels(left_root) + get_levels(right_root)
print(answer2)


with open("./story_1/input/q02_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """ADD id=1 left=[10,A] right=[30,H]
# ADD id=2 left=[15,D] right=[25,I]
# ADD id=3 left=[12,F] right=[31,J]
# ADD id=4 left=[5,B] right=[27,L]
# ADD id=5 left=[3,C] right=[28,M]
# SWAP 1
# SWAP 5
# ADD id=6 left=[20,G] right=[32,K]
# ADD id=7 left=[4,E] right=[21,N]
# SWAP 2""".splitlines()


left_root = None
right_root = None
m = {}

for line in lines:
    print(f"{line=}")

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
    # print(id, l_rank, l_symbol, r_rank, r_symbol)

    l_node = Node(l_rank, l_symbol, None, None)
    r_node = Node(r_rank, r_symbol, None, None)

    m[_id] = [l_node, r_node]

    left_root = place_node(left_root, l_node)
    right_root = place_node(right_root, r_node)


answer3 = get_levels(left_root) + get_levels(right_root)
print(answer3)
