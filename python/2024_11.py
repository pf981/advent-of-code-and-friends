from aocd import get_data, submit


inp = get_data(day=11, year=2024)

# inp = '''0 1 10 99 999 
# '''

inp = '''125 17
'''

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


lines = inp.splitlines()
nums = [int(num) for num in lines[0].split()]
import collections
counts = collections.Counter(nums)

for _ in range(25):
    # print(counts)
    new_counts = collections.Counter()
    for num, count in counts.items():
        if num == 0:
            new_counts[1] += count
        elif len(str(num)) % 2 == 0:
            length = len(str(num)) // 2
            # Left
            leftnum = str(num)[:length]
            rightnum = str(num)[length:]
            new_counts[int(leftnum)] += count
            new_counts[int(rightnum)] += count
        else:
            new_counts[num * 2024] += count
    counts = new_counts


answer1 = sum(counts.values())
print(answer1)

submit(answer1, part='a', day=11, year=2024)


# Part 2

for _ in range(75):
    # print(counts)
    new_counts = collections.Counter()
    for num, count in counts.items():
        if num == 0:
            new_counts[1] += count
        elif len(str(num)) % 2 == 0:
            length = len(str(num)) // 2
            # Left
            leftnum = str(num)[:length]
            rightnum = str(num)[length:]
            new_counts[int(leftnum)] += count
            new_counts[int(rightnum)] += count
        else:
            new_counts[num * 2024] += count
    counts = new_counts


answer1 = sum(counts.values())
print(answer1)


answer2 = 'todo'
print(answer2)

submit(answer1, part='b', day=11, year=2024)
