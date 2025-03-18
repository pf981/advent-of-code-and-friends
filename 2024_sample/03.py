with open("2024_sample/03.txt") as f:
    lines = f.read().splitlines()

readings = [(line.split()[0], int(line.split()[1])) for line in lines]

answer1 = sum(base for _, base in readings)
print(answer1)


answer2 = sum(int(reading, base) for reading, base in readings)
print(answer2)


lookup = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#'
n = answer2
digits = []
while n:
    digits.append(int(n % len(lookup)))
    n //= len(lookup)

answer3 = ''.join(lookup[digit] for digit in reversed(digits))
print(answer3)
