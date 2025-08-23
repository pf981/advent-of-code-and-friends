import itertools


def list_to_int(nums):
    return int("".join(str(digit) for digit in nums))


for permutation in itertools.permutations(reversed(range(1, 10))):
    first = list_to_int(permutation[:4])
    second = list_to_int(permutation[4:])

    if second == 2 * first:
        answer = int(str(first) + str(second))
        break

print(answer)
