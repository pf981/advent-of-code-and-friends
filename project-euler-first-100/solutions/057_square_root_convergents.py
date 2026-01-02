from fractions import Fraction


def compute_denominators(max_terms):
    denominator = {}
    denominator[1] = Fraction(2)

    for i in range(2, max_terms + 1):
        denominator[i] = 2 + 1 / denominator[i - 1]

    return denominator


def compute_nth_term(n, denominator):
    return 1 + Fraction(1, denominator[n])


denominator = compute_denominators(1000)
terms = []

for i in range(1, 1001):
    terms.append(compute_nth_term(i, denominator))

answer = sum(len(str(fract.numerator)) > len(str(fract.denominator)) for fract in terms)

print(answer)
