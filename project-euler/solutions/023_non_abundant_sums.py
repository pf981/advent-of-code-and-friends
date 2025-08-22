limit = 28123

div_sum = [1] * (limit + 1)
div_sum[0] = 0
for i in range(2, limit // 2 + 1):
    for j in range(i * 2, limit + 1, i):
        div_sum[j] += i

abundant_numbers = [n for n in range(12, limit + 1) if div_sum[n] > n]
can_be_written = [False] * (limit + 1)

for i, a in enumerate(abundant_numbers):
    for j in range(i, len(abundant_numbers)):
        s = a + abundant_numbers[j]

        if s > limit:
            break

        can_be_written[s] = True

answer = sum(i for i in range(1, limit + 1) if not can_be_written[i])
print(answer)
