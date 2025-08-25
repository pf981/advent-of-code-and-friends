from fractions import Fraction


def compute_continued_fractions(max_fractions: int) -> list[int]:
    continued_fractions = [1] * max_fractions
    continued_fractions[1] = 2
    for i in range(4, max_fractions, 3):
        continued_fractions[i] = continued_fractions[i - 3] + 2
    return continued_fractions


def compute_nth_term(n: int, continued_fractions: list[int]) -> Fraction:
    if n == 1:
        return Fraction(2)

    n = n - 2
    denominator = Fraction(continued_fractions[n])

    for i in reversed(range(n)):
        denominator = continued_fractions[i] + Fraction(1, denominator)

    return 2 + Fraction(1, denominator)


continued_fractions = compute_continued_fractions(100)
nth_term = compute_nth_term(100, continued_fractions)
answer = sum(int(n) for n in str(nth_term.numerator))
print(answer)
