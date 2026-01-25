import collections
import dataclasses


@dataclasses.dataclass
class Node:
    count: int = 0
    children: dict[str, "Node"] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(Node)
    )


with open("./input/problem-sep-25-long-C-input.txt") as f:
    text = f.read()

_, *words, _, actions = text.splitlines()

trie = Node()
for word in words:
    node = trie
    node.count += 1
    for c in word:
        node = node.children[c]
        node.count += 1

stack = []
node = trie
result = ["Case #1:"]
for action in actions:
    if action == "<":
        node = stack.pop()
    else:
        stack.append(node)
        node = node.children[action]

    if len(stack) >= 3:
        result.append(str(node.count))


with open("./output/problem-sep-25-long-C.txt", "w") as f:
    f.write("\n".join(result))
