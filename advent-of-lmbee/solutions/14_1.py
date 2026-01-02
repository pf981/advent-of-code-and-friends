with open("data/day14.txt") as f:
    text = f.read()
n_signals = 123456

states = {}
m = {}

start, *lines = text.splitlines()
start = start.split()[1]

for line in lines:
    a, b, c = line.split()
    a = a[:-1]
    m[a] = [b, c]
    states[a] = False

answer = 0
for _ in range(n_signals):
    node = start
    while node not in ["BIN", "OUT"]:
        next_node = m[node][states[node]]
        states[node] = not states[node]
        node = next_node
    answer += node == "OUT"

print(answer)
