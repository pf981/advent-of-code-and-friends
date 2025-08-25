MAX_DENOMINATOR = 1000000

phi = list(range(MAX_DENOMINATOR + 1))

for i in range(2, MAX_DENOMINATOR + 1):
    if phi[i] == i:
        for j in range(i, MAX_DENOMINATOR + 1, i):
            phi[j] -= phi[j] // i

answer = sum(phi) - 1
print(answer)
