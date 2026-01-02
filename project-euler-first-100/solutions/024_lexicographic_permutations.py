import math


def nth_lexicographic_permutation(digits: list[int], n: int) -> str:
    result = []
    for i in reversed(range(len(digits))):
        fact = math.factorial(i)
        index, n = divmod(n, fact)
        result.append(digits.pop(index))
    return "".join(str(digit) for digit in result)


answer = nth_lexicographic_permutation(list(range(10)), 1_000_000 - 1)
print(answer)
