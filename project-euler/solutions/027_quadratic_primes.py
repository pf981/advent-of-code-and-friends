import math

MAX_F = 50_000
MAX_COEF = 1000

is_prime = [True] * (MAX_F + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(MAX_F)) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start : MAX_F + 1 : step] = [False] * (((MAX_F - start) // step) + 1)

b_candidates = [b for b in range(2, MAX_COEF + 1) if is_prime[b]]

best_len = -1
best_a = 0
best_b = 0

for b in b_candidates:
    a_start = -MAX_COEF + (b != 2)
    for a in range(a_start, MAX_COEF, 2 if b != 2 else 1):
        n = 0
        while True:
            val = n * n + a * n + b
            if val <= 1 or (val > MAX_F) or not is_prime[val]:
                break
            n += 1
        if n > best_len:
            best_len, best_a, best_b = n, a, b

answer = best_a * best_b
print(answer)
