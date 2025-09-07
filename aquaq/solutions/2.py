with open("./input/2.txt") as f:
    text = f.read()

seen: set[str] = set()
stack: list[str] = []
for num in text.split():
    while num in seen:
        seen.remove(stack.pop())

    stack.append(num)
    seen.add(num)

answer = sum(int(num) for num in stack)
print(answer)
