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
    parent: Treap | None = None  # Think I can remove this
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


def split_off_max(
    node: Treap | None, max_val: int
) -> tuple[Treap | None, Treap | None]:
    print(f"  Split {node.val if node else None}; {max_val=}")
    # print_treap(node)
    # print()

    recalc(node)  # FIXME: Added this - is it needed?
    if not node:
        return (None, None)

    if node.val == max_val:
        return (node.left, node.right)

    # max_value is in left subtree, this node is in the right split
    if node.left and node.left.largest == max_val:
        l, r = split_off_max(node.left, max_val)
        node.left = None
        recalc(node)
        r = merge(r, node)
        return (l, r)

    # max_value is in right subtree, this node is in the left split
    if node.right and node.right.largest == max_val:
        l, r = split_off_max(node.right, max_val)
        node.right = None
        recalc(node)
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
        left.right.parent = left
        recalc(left)
        return left
    else:
        # Right is root
        right.left = merge(left, right.left)
        right.left.parent = right
        recalc(right)
        return right


with open("./input/2026/03/input1.txt") as f:
    text = f.read()
# text = """-3 -
#  - -
# 2 -
# --4
#   -
# 1  -"""

treap = None
for num in re.findall(r"\d+", text):
    num = int(num)
    treap = merge(treap, Treap(priority=random.random(), val=num, largest=num))

print_treap(treap)

flips = 0
# while treap:
for _ in range(len(re.findall(r"\d+", text))):  # FIXME: TEST
    l, r = split_off_max(treap, treap.largest)

    print("--- R ---")
    print_treap(r)
    print()
    print("--- L ---")
    print_treap(l)
    print()

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

    print("--- l after maybe reverse ---")
    print_treap(l)
    print("-------------")

    treap = merge(l, r)
    print("--- After merge ---")
    print_treap(treap)
    print("-------------")
    reverse(treap)
    flips += 1

    print("--- After final reverse ---")
    print_treap(treap)
    print("-------------")
    # break  # TEST


answer = flips
print(answer)
