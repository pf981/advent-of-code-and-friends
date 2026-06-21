import random
import re
from dataclasses import dataclass

random.seed(42)


@dataclass
class Treap:
    priority: float
    val: int
    largest: int
    count: int = 1
    lazy_reverse = False
    parent: Treap | None = None
    left: Treap | None = None
    right: Treap | None = None


def print_treap(
    node: "Treap | None", prefix: str = "", is_left: bool | None = None
) -> None:
    if node is None:
        return

    if node.right is not None:
        print_treap(node.right, prefix + ("│   " if is_left else "    "), False)

    branch = "" if is_left is None else ("└── " if is_left else "┌── ")
    print(
        f"{prefix}{branch}[{node.val}] (p:{node.priority:.2f}, l:{node.largest}. c:{node.count}, r:{node.lazy_reverse})"
    )

    if node.left is not None:
        print_treap(
            node.left, prefix + ("    " if is_left is None or is_left else "│   "), True
        )


def recalc(node: Treap | None) -> None:
    if not node:
        return

    node.largest = node.val
    node.count = 1
    if node.left:
        node.largest = max(node.largest, node.left.largest)
        node.count += node.left.count
    if node.right:
        node.largest = max(node.largest, node.right.largest)
        node.count += node.right.count

    if node.lazy_reverse:
        node.lazy_reverse = False
        node.left, node.right = node.right, node.left
        reverse(node.left)
        reverse(node.right)


def reverse(node: Treap | None) -> None:
    if not node:
        return

    node.lazy_reverse = not node.lazy_reverse


def split(node: Treap | None, left_size: int) -> tuple[Treap | None, Treap | None]:

    print(f"\nSplit {left_size=}")
    print_treap(node)
    print()

    if not node:
        # assert not left_size
        return (None, None)
    if not left_size:
        return (None, node)

    left_count = node.left.count if node.left else 0
    print(f"{node.val=} {left_size=} {left_count=}")

    # node is in the right part
    if left_count >= left_size:
        l, r = split(node.left, left_size)
        node.left = r
        if r:
            r.parent = node
        recalc(node)
        if l:
            l.parent = None
        return l, node

    # node is in the left part
    l, r = split(node.right, left_size - left_count - 1)
    node.right = l
    if l:
        l.parent = node
    recalc(node)
    if r:
        r.parent = None
    return node, r


def merge(left: Treap | None, right: Treap | None) -> Treap | None:
    if not left:
        return right
    if not right:
        return left

    if left.priority < right.priority:
        # Left is root
        left.right = merge(left.right, right)
        left.right.parent = left
        recalc(left)
        return left
    else:
        # Right is root
        right.left = merge(left, right.left)
        right.left.parent = right
        recalc(right)
        return right


def split_off_max(node: Treap | None) -> tuple[Treap | None, Treap | None]: ...


with open("./input/2026/03/input1.txt") as f:
    text = f.read()
text = """-3 -
 - -
2 -
--4
  -
1  -"""

treap = None
for num in re.findall(r"\d+", text):
    num = int(num)
    treap = merge(treap, Treap(priority=random.random(), val=num, largest=num))

print_treap(treap)

flips = 0
while treap:
    l, r = split_off_max(treap)

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
