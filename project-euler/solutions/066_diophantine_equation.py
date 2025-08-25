import math


# https://en.wikipedia.org/wiki/Pell's_equation
def solve_pell(D: int) -> tuple[int, int] | None:
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return None

    m = 0
    d = 1
    a = a0

    p_minus2, p_minus1 = 1, a
    q_minus2, q_minus1 = 0, 1

    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d

        p = a * p_minus1 + p_minus2
        q = a * q_minus1 + q_minus2

        if p * p - D * q * q == 1:
            return p, q

        p_minus2, p_minus1 = p_minus1, p
        q_minus2, q_minus1 = q_minus1, q


best_d = 0
max_x = 0

for d in range(2, 1000):
    solution = solve_pell(d)
    if solution is None:
        continue
    x, y = solution
    if x > max_x:
        max_x = x
        best_d = d

answer = best_d
print(answer)
