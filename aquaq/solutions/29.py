with open("./input/29.txt") as f:
    text = f.read()

upper = int(text.strip())

n = len(str(upper))
value = answer = 0
digits = [0] * n
i = n - 1
coef = 1
while value <= upper:
    answer += 1
    digits[i] += 1
    value += coef

    if digits[i] == 10:
        while i - 1 >= 0 and digits[i] == 10:
            i -= 1
            digits[i] += 1

            coef *= 10
            value += coef

        for i in range(i + 1, n):
            coef //= 10
            value -= coef * (digits[i] - digits[i - 1])

            digits[i] = digits[i - 1]

print(answer)
