MAX_EXPONENT = 100
MAX_BASE = 100

n_digit_and_nth_powers = []

for n in range(1, MAX_EXPONENT):
    for base in range(1, MAX_BASE):
        if len(str(base**n)) == n:
            n_digit_and_nth_powers.append(n)

answer = len(n_digit_and_nth_powers)
print(answer)
