with open("2025_contest/02.txt") as f:
    inp = f.read()

functions, lines = inp.split("\n\n")
a, b, c = (int(line.split()[-1]) for line in functions.splitlines())


def get_price(num):
    return (num**c) * b + a


nums = [int(line) for line in lines.splitlines()]

median = sorted(nums)[len(nums) // 2]
answer1 = get_price(median)
print(answer1)


# Part 2

evens = sum(num for num in nums if num % 2 == 0)
answer2 = get_price(evens)
print(answer2)


answer3 = max(num for num in nums if get_price(num) <= 15000000000000)
print(answer3)
