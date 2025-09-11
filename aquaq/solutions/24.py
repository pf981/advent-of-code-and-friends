from __future__ import annotations
import collections
import dataclasses
import heapq


@dataclasses.dataclass
class Node:
    val: str
    n: int
    left: Node | None
    right: Node | None

    def __lt__(self, other):
        return (self.n, len(self.val), self.val) < (other.n, len(other.val), other.val)


def get_encoding(node: Node) -> dict[str, str]:
    m = {}

    def dfs(node: Node, prefix: str = "") -> None:
        if len(node.val) == 1:
            m[node.val] = prefix
            return

        if node.left:
            dfs(node.left, prefix + "0")

        if node.right:
            dfs(node.right, prefix + "1")

    dfs(node)

    return m


with open("./input/24.txt") as f:
    text = f.read()

chars, plaintext = text.splitlines()

counts = collections.Counter(chars)
heap = [Node(ch, count, None, None) for ch, count in counts.items()]
heapq.heapify(heap)

while len(heap) > 1:
    node1 = heapq.heappop(heap)
    node2 = heapq.heappop(heap)

    node = Node(node1.val + node2.val, node1.n + node2.n, node1, node2)
    heapq.heappush(heap, node)

m = get_encoding(heap[0])
answer = ""
while plaintext:
    for ch, prefix in m.items():
        if plaintext.startswith(prefix):
            answer += ch
            plaintext = plaintext[len(prefix) :]
            break
    else:
        raise ValueError(f"Unable to identify prefix from: {plaintext!r}")

print(answer)
