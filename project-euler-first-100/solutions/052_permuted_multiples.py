import itertools


def are_permutations(nums: list[int]) -> bool:
    for i, num in enumerate(nums):
        if i == 0:
            first_digits = sorted(str(int(num)))
            continue

        digits = sorted(str(int(num)))
        if digits != first_digits:
            return False
    return True


for num in itertools.count(1):
    if are_permutations([i * num for i in range(1, 7)]):
        answer = num
        break

print(answer)
