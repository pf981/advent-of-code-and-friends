factorial = [1] * 10
for i in range(2, len(factorial)):
    factorial[i] = i * factorial[i - 1]


def is_curious(n):
    return n == sum(factorial[int(digit)] for digit in str(n))


curious_nums = [n for n in range(3, 50_000) if is_curious(n)]
answer = sum(curious_nums)
print(answer)
