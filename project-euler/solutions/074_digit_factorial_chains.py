import functools

factorials = [1]
for i in range(1, 10):
    factorials.append(factorials[-1] * i)

cycles = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2}


@functools.cache
def get_chain_length(n: int) -> int:
    if n in cycles:
        return cycles[n]

    n2 = sum(factorials[int(digit)] for digit in str(n))
    if n == n2:
        return 1

    return 1 + get_chain_length(n2)


answer = sum(get_chain_length(n) == 60 for n in range(1_000_000))
print(answer)
