with open("./input/2026/02/input2.txt") as f:
    text = f.read()
iterations = 65

# text = "11222111221211221112212211221112112221222111221122212212211122111221"
# iterations = 10

val = list(text)

for _ in range(iterations):
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
# answer = len(val)
answer = sum(a == b == c for a, b, c in zip(val[2:], val[1:-1], val[:-2]))

print(answer)
# 39307769
# egg Find the hidden binary message in the starting input...
