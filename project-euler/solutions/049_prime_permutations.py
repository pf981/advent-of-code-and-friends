import math


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


limit = 9999
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(limit)) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False
primes = {i for i in range(1000, limit + 1) if is_prime[i]}


for prime1 in primes:
    if prime1 == 1487:
        continue

    for distance in range(2, (9999 - prime1) // 2, 2):
        prime2 = prime1 + distance
        prime3 = prime2 + distance

        if (
            prime2 in primes
            and prime3 in primes
            and is_permutation(prime1, prime2)
            and is_permutation(prime2, prime3)
        ):
            break
    else:
        continue
    break

answer = int(str(prime1) + str(prime2) + str(prime3))
print(answer)
