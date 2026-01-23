import math


def crack(triples: list[tuple[int, int, int]]) -> list[int]:
    Ms = []
    for N, e, C in triples:
        for N2, _, _ in triples:
            if N2 == N:
                continue
            p = math.gcd(N, N2)
            if p != 1:
                break
        else:
            raise ValueError(f"Unable to factorize {N=}")

        q = N // p
        phi = (p - 1) * (q - 1)

        R = phi
        R1 = phi
        R2 = e
        T1 = 0
        T2 = 1

        while R:
            Q = R1 // R2
            R = R1 % R2
            T = T1 - Q * T2

            R1 = R2
            R2 = R
            T1 = T2
            T2 = T

        d = T1 % phi
        M = pow(C, d, N)

        Ms.append(M)

    return Ms


with open("./input/problem-decryption-contest-1-D-input.txt") as f:
    text = f.read()

parts = []
lines = text.splitlines()[::-1]
lines.pop()
while lines:
    triples = []
    for _ in range(int(lines.pop())):
        N, e, C = map(int, lines.pop().split())
        triples.append((N, e, C))
    parts.append(triples)

result = []
for i, triples in enumerate(parts, 1):
    plaintext = "\n".join(str(M) for M in crack(triples))
    result.append(f"Case #{i}:\n{plaintext}")

with open("./output/problem-decryption-contest-1-D.txt", "w") as f:
    f.write("\n".join(result))
