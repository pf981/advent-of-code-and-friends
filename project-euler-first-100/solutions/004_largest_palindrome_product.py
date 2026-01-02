import itertools


def is_palindrome(num):
    return str(num) == str(num)[::-1]


answer = max(
    x * y
    for x, y in itertools.product(
        reversed(range(100, 1000)), reversed(range(100, 1000))
    )
    if is_palindrome(x * y)
)
print(answer)
