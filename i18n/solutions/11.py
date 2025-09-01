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


to_find = ["οδυσσευς", "οδυσσεως", "οδυσσει", "οδυσσεα", "οδυσσευ"]
caesar(text.splitlines()[0].lower(), 1)

answer = 0
for line in text.lower().splitlines():
    for shift in range(len(alphabet)):
        for s in to_find:
            if s in caesar(line, shift):
                answer += shift
                break
        else:
            continue
        break

print(answer)
