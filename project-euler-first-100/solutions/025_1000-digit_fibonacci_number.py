a = b = 1
target = 10**999
i = 2
while a < target:
    a, b = a + b, a
    i += 1

answer = i
print(answer)
