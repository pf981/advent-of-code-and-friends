n = int(input())

exp = 5
fives = 0
while exp <= n:
    fives += n // exp
    exp *= 5

print(fives)
