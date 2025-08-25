POWER = 5

correct_numbers = []
for i in range(2, 1_000_000):
    if i == sum(int(digit) ** POWER for digit in str(i)):
        correct_numbers.append(i)

answer = sum(correct_numbers)
print(answer)
