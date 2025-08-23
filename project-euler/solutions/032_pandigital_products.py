import math


def is_pandigital(multiplicand: int, multiplier: int, product: int) -> bool:
    return (
        "".join(sorted(str(multiplicand) + str(multiplier) + str(product)))
        == "123456789"
    )


answer = 0
for rhs in range(1000, 10000):
    for candidate_factor in range(1, int(math.sqrt(rhs))):
        if rhs % candidate_factor == 0 and is_pandigital(
            candidate_factor, rhs // candidate_factor, rhs
        ):
            answer += rhs
            break
print(answer)
