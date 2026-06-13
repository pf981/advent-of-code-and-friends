with open("./input/2026/02/input1.txt") as f:
    text = f.read()
# text = "121"
val = list(text)

for _ in range(65):
    val2 = []
    i = 0
    while i < len(val):
        if i < len(val) - 1 and val[i] == val[i + 1]:
            val2.append("2")
            val2.append(val[i])
            i += 2
        else:
            val2.append("1")
            val2.append(val[i])
            i += 1
    val = val2
# print("".join(val))
answer = len(val)
print(answer)
# 54336330
