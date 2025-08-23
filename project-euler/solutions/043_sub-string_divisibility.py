cur = 0
available = set(range(10))
answer = 0
divisors = [0, 0, 0, 2, 3, 5, 7, 11, 13, 17]


def backtrack(i):
    global cur, answer

    if i == 10:
        answer += cur
        return

    for digit in available.copy():
        if i == 0 and digit == 0:
            continue

        if divisors[i] and (10 * (cur % 100) + digit) % divisors[i] != 0:
            continue

        cur = 10 * cur + digit
        available.remove(digit)

        backtrack(i + 1)

        cur //= 10
        available.add(digit)


backtrack(0)
print(answer)
