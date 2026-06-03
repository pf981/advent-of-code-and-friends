with open("./input/2025/01/input1.txt") as f:
    text = f.read()

m = {
    "._": "A",
    "_...": "B",
    "_._.": "C",
    "_..": "D",
    ".": "E",
    ".._.": "F",
    "__.": "G",
    "....": "H",
    "..": "I",
    ".___": "J",
    "_._": "K",
    "._..": "L",
    "__": "M",
    "_.": "N",
    "___": "O",
    ".__.": "P",
    "__._": "Q",
    "._.": "R",
    "...": "S",
    "_": "T",
    ".._": "U",
    "..._": "V",
    ".__": "W",
    "_.._": "X",
    "_.__": "Y",
    "__..": "Z",
    "._._._": ".",
    "..__..": "?",
    "_._.__": "!",
    "_...._": "-",
}

result = []
for line in text.splitlines():
    result.append("".join(m[w] for w in line.split()))

answer = " ".join(result)
print(answer)
