from __future__ import annotations
import collections
import dataclasses

import downloader


@dataclasses.dataclass
class Node:
    val: int
    left: Node | None
    right: Node | None


def add_node(num: int, root: Node | None) -> Node:
    if not root:
        return Node(num, None, None)

    if num >= root.val:
        root.right = add_node(num, root.right)
    else:
        root.left = add_node(num, root.left)

    return root


lines = downloader.get_puzzle(26).splitlines()

root = None
for line in lines:
    num = int(line, 16)
    root = add_node(num, root)

assert root

max_depth = max_width = 0
q = collections.deque([root])
while q:
    max_width = max(max_width, len(q))
    for _ in range(len(q)):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    max_depth += 1

answer = max_depth * max_width
print(answer)
