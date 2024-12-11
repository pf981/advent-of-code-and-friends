from aocd import get_data, submit
import collections


def simulate(n_iterations):
    counts = collections.Counter(nums)
    for _ in range(n_iterations):
        new_counts = collections.Counter()
        for num, count in counts.items():
            if num == 0:
                new_counts[1] += count
            elif len(str(num)) % 2 == 0:
                length = len(str(num)) // 2
                new_counts[int(str(num)[:length])] += count
                new_counts[int(str(num)[length:])] += count
            else:
                new_counts[num * 2024] += count
        counts = new_counts
    return sum(counts.values())


inp = get_data(day=11, year=2024)
lines = inp.splitlines()
nums = [int(num) for num in lines[0].split()]

answer1 = simulate(25)
print(answer1)

submit(answer1, part='a', day=11, year=2024)


# Part 2


answer2 = simulate(75)
print(answer2)

submit(answer2, part='b', day=11, year=2024)
