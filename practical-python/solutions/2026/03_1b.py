import random
import re
from dataclasses import dataclass

random.seed(42)


@dataclass
class Treap:
    priority: float
    val: int
    largest: int
    lazy_reverse: bool = False
    left: Treap | None = None
    right: Treap | None = None


def recalc(node: Treap | None) -> None:
    if not node:
        return

    if node.lazy_reverse:
        node.lazy_reverse = False
        node.left, node.right = node.right, node.left
        reverse(node.left)
        reverse(node.right)

    node.largest = node.val
    if node.left:
        node.largest = max(node.largest, node.left.largest)
    if node.right:
        node.largest = max(node.largest, node.right.largest)


def reverse(node: Treap | None) -> None:
    if not node:
        return
    node.lazy_reverse = not node.lazy_reverse


def split_off_max(
    node: Treap | None, max_val: int
) -> tuple[Treap | None, Treap | None]:
    recalc(node)

    if not node:
        return (None, None)

    if node.val == max_val:
        return (node.left, node.right)

    # max_value is in left subtree, this node is in the right split
    if node.left and node.left.largest == max_val:
        l, r = split_off_max(node.left, max_val)
        node.left = None
        r = merge(r, node)
        return (l, r)

    # max_value is in right subtree, this node is in the left split
    if node.right and node.right.largest == max_val:
        l, r = split_off_max(node.right, max_val)
        node.right = None
        l = merge(node, l)
        return (l, r)

    assert False


def merge(left: Treap | None, right: Treap | None) -> Treap | None:
    recalc(left)
    recalc(right)

    if not left:
        return right
    if not right:
        return left

    if left.priority < right.priority:
        # Left is root
        left.right = merge(left.right, right)
        recalc(left)
        return left
    else:
        # Right is root
        right.left = merge(left, right.left)
        recalc(right)
        return right


with open("./input/2026/03/input1.txt") as f:
    text = f.read()

treap = None
for num in re.findall(r"\d+", text):
    num = int(num)
    treap = merge(treap, Treap(priority=random.random(), val=num, largest=num))

flips = 0
while treap:
    l, r = split_off_max(treap, treap.largest)

    # If right split is empty, largest was in the correct position
    if not r:
        treap = l
        continue

    # If left split is empty, largest was in first position
    if not l:
        pass
    else:
        reverse(l)
        flips += 1

    treap = merge(l, r)
    reverse(treap)
    flips += 1

answer = flips
print(answer)
