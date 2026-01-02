from fractions import Fraction


def cast_out(numerator: int, denominator: int) -> Fraction | None:
    str_n = str(numerator)
    str_d = str(denominator)

    for n_index in range(2):
        for d_index in range(2):
            if str_n[n_index] == str_d[d_index]:
                other_n_index = (n_index + 1) % 2
                other_d_index = (d_index + 1) % 2
                return Fraction(int(str_n[other_n_index]), int(str_d[other_d_index]))

    return None


special_fractions = []
for numerator in range(10, 100):
    if numerator % 10 == 0:
        continue

    for denominator in range(numerator + 1, 100):
        if denominator % 10 == 0:
            continue

        fraction = Fraction(numerator, denominator)
        casted = cast_out(numerator, denominator)
        if casted == fraction:
            special_fractions.append(fraction)

prod = Fraction(1, 1)
for special_fraction in special_fractions:
    prod *= special_fraction

answer = prod.denominator
print(answer)
