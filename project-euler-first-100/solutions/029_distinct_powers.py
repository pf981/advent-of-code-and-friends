BASE_RANGE = range(2, 101)
EXPONENT_RANGE = range(2, 101)

sequence = set(a**b for a in BASE_RANGE for b in EXPONENT_RANGE)
answer = len(sequence)
print(answer)
