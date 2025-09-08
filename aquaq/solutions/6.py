with open("./input/6.txt") as f:
    text = f.read()

n = int(text.strip().split()[-1])


answer = 0
for a in range(n + 1):
    a_ones = str(a).count("1")
    for b in range(n + 1):
        c = n - a - b
        if c < 0:
            break

        b_ones = str(b).count("1")
        c_ones = str(c).count("1")

        answer += a_ones + b_ones + c_ones

print(answer)
