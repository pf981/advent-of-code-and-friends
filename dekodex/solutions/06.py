import functools

MOD = 1_000_000_007


@functools.cache
def sum_waviness_lte(
    i: int,
    tight: bool,
    lastDigit: int,
    secondLastDigit: int,
    upper: tuple[int, ...],
    digits_used: int,
) -> tuple[int, int]:
    if i == len(upper):
        return (1, 0)

    hi = upper[i] if tight else 9
    result = 0
    n = 0
    for digit in range(hi + 1):
        new_digits_used = digits_used
        if digits_used > 0 or digit != 0:
            new_digits_used += 1

        is_wavey = 0
        if new_digits_used >= 3:
            is_peak = secondLastDigit < lastDigit > digit
            is_valley = secondLastDigit > lastDigit < digit
            is_wavey = is_peak or is_valley

        n2, waviness2 = sum_waviness_lte(
            i + 1,
            tight and digit == upper[i],
            digit if new_digits_used > 0 else -1,
            lastDigit if new_digits_used > 1 else -1,
            upper,
            new_digits_used,
        )
        n += n2
        result += is_wavey * n2 + waviness2
    return (n, result)


with open("input/06.txt") as f:
    text = f.read()

lower, upper = map(int, text.split())
l2 = tuple(int(s) for s in str(upper))
l1 = tuple(int(s) for s in str(lower - 1))
w1 = sum_waviness_lte(0, True, -1, -1, l1, 0)[1]
w2 = sum_waviness_lte(0, True, -1, -1, l2, 0)[1]
answer = (w2 - w1) % MOD
print(answer)
