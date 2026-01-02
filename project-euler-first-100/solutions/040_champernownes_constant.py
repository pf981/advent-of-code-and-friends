import math

digits = "".join(str(x) for x in range(1, 1_000_000))
nths = [10**n for n in range(7)]

answer = math.prod(int(digits[nth - 1]) for nth in nths)
print(answer)
