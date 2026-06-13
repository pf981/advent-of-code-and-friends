# egg Find the hidden binary message in the starting input...
import itertools

with open("./input/2026/02/input2.txt") as f:
    text = f.read()

x = list(itertools.groupby(text))
list(x[1][1])

result = []
for c, group in itertools.groupby(text):
    # print(a, list(b))
    val = "21".index(c)
    result.extend([str(val)] * len(list(group)))
"".join(result)
