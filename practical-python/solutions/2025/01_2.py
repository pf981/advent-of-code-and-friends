with open("./input/2025/01/input2.txt") as f:
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

num = int("".join(str(ord(c)) for c in text))
morse = f"{num:b}".replace("0", ".").replace("1", "_").split("_._.__")
result = []
for s in morse:
    result.append(m.get(s, ""))

answer = "".join(result)
print(answer)
