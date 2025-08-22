import re


with open("data/0022_names.txt") as in_file:
    text = in_file.read()

names = sorted(re.findall(r'"(\w+)"', text))
answer = sum(
    i * sum(ord(c) - ord("A") + 1 for c in name) for i, name in enumerate(names, 1)
)
print(answer)
