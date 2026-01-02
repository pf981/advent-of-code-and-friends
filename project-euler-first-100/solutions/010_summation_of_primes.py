import math

limit = 2_000_000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(limit)) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)

answer = sum(num for num, num_is_prime in enumerate(is_prime) if num_is_prime)
print(answer)
