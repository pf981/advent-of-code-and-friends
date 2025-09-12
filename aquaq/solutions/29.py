with open("./input/29.txt") as f:
    text = f.read()

upper = int(text.strip())

n = len(str(upper))
answer = 0
digits = [0] * n
i = n - 1
while True:
    answer += 1
    digits[i] += 1

    if digits[i] == 10:
        while i - 1 >= 0 and digits[i] == 10:
            i -= 1
            digits[i] += 1
        for i in range(i + 1, n):
            digits[i] = digits[i - 1]

    if int("".join(str(digit) for digit in digits)) > upper:
        break

print(answer)
