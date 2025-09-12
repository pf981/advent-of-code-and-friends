def is_balanced(s: str) -> bool:
    stack = []
    close = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in close:
            if not stack or stack[-1] != close[c]:
                return False
            stack.pop()
    return not stack


with open("./input/32.txt") as f:
    text = f.read()

answer = sum(is_balanced(line) for line in text.splitlines())
print(answer)
