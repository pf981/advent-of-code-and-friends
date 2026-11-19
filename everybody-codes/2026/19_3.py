import math

with open("./2026/input/everybody_codes_e2026_q19_p3.txt") as f:
    text = f.read().strip()

s = sum(c in "MYC" for c in text)
result = [s // 3] * 3
match s - sum(result):
    case 0:
        pass
    case 1:
        result[1] += 1
    case 2:
        result[1] += 1
        result[2] += 1
    case 3:
        result[1] += 1
        result[2] += 2
    case _:
        assert False

answer = math.prod(result)
print(answer)
