import re

with open("./input/11.txt", encoding="utf-8") as f:
    text = f.read()

alphabet = "αβγδεζηθικλμνξοπρστυφχψω"
m = {c: i for i, c in enumerate(alphabet)}


def caesar(plaintext: str, shift: int) -> str:
    result = []
    for c in plaintext:
        if c not in m:
            result.append(c)
            continue
        result.append(alphabet[(m[c] + shift) % len(alphabet)])

    return "".join(result)


pattern = re.compile("οδυσσευς|οδυσσεως|οδυσσει|οδυσσεα|οδυσσευ", re.UNICODE)
answer = 0
for line in text.lower().splitlines():
    for shift in range(len(alphabet)):
        if pattern.search(caesar(line, shift)):
            answer += shift
            break

print(answer)
