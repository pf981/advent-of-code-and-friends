import collections

with open("./input/2025/09/input1.txt") as f:
    text = f.read()

first, *lines = text.splitlines()
start, end = map(int, first.split(","))
m = {
    int(line.split(":")[0]): list(map(int, line.split(":")[1].split(",")))
    for line in lines
}

q = collections.deque([start])
seen = {start}
d = 1
while q:
    for _ in range(len(q)):
        node = q.popleft()
        if node == end:
            break

        for node2 in m[node]:
            if node2 in seen:
                continue
            seen.add(node2)
            q.append(node2)
    else:
        d += 1
        continue
    break

answer = d
print(answer)
