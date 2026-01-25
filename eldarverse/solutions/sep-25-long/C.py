with open("./input/problem-sep-25-long-C-input.txt") as f:
    text = f.read()

_, *words, _, actions = text.splitlines()

trie = {None: 0}
for word in words:
    node = trie
    node[None] += 1
    for c in word:
        node[c] = node.get(c, {None: 0})
        node = node[c]
        node[None] += 1

stack = []
node = trie
result = ["Case #1:"]
for action in actions:
    if action == "<":
        node = stack.pop()
    else:
        stack.append(node)
        node = node.get(action, {None: 0})
        assert isinstance(node, dict)

    if len(stack) >= 3:
        result.append(str(node[None]))


with open("./output/problem-sep-25-long-C.txt", "w") as f:
    f.write("\n".join(result))
