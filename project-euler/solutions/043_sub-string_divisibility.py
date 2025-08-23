cur = ""
available = set(str(digit) for digit in range(10))
answer = 0
divisors = [0, 0, 0, 2, 3, 5, 7, 11, 13, 17]


def backtrack(i):
    global cur, answer

    if i == 10:
        answer += int(cur)
        return

    for digit in available.copy():
        if i == 0 and digit == "0":
            continue

        if divisors[i] and int(cur[-2:] + digit) % divisors[i] != 0:
            continue

        cur += digit
        available.remove(digit)

        backtrack(i + 1)

        cur = cur[:-1]
        available.add(digit)


backtrack(0)
print(answer)
