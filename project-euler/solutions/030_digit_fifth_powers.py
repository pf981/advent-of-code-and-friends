from helpers import helpers

POWER = 5

correct_numbers = []
for i in range(2, 1000000):
    if i == sum(x**POWER for x in helpers.int_to_digits(i)):
        correct_numbers.append(i)

answer = sum(correct_numbers)
print(answer)
