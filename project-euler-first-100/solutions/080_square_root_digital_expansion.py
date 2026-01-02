import decimal

decimal.getcontext().prec = 102

answer = 0
for n in range(1, 101):
    root = decimal.Decimal(n).sqrt()

    if int(root) == root:
        continue

    for _ in range(100):
        answer += int(root)
        root = (10 * root) % 10
print(answer)
