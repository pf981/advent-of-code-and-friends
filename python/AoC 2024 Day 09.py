from aocd import get_data, submit


inp = get_data(day=9, year=2024)
lines = inp.splitlines()
nums = [int(c) for c in lines[0]]

data = []
file_id = 0
for i in range(0, len(nums), 2):
    file_size = nums[i]
    data.extend([file_id] * file_size)
    if i + 1 < len(nums):
        free_size = nums[i + 1]
        data.extend([-1] * free_size)
    file_id += 1

i = 0
j = len(data) - 1
while i <= j:
    while i < len(data) and data[i] != -1:
        i += 1
    if i == len(data):
        break
    while j >= 0 and data[j] == -1:
        j -= 1
    if not i <= j:
        break
    if i == -1:
        break
    data[i], data[j] = data[j], data[i]

answer1 = 0
for i, num in enumerate(data):
    if num == -1:
        break
    answer1 += i * num
print(answer1)

submit(answer1, part='a', day=9, year=2024)


# Part 2


import sortedcontainers


gaps = {gap_size: sortedcontainers.SortedList(key=lambda ind: -ind) for gap_size in range(1, 10)} # gap_size -> [(index, size), ...]
files = [] # file_id -> [index, size]
index = 0
for i in range(0, len(nums), 2):
    file_size = nums[i]
    files.append([index, file_size])
    index += file_size

    if i + 1 < len(nums):
        gap_size = nums[i + 1]
        if gap_size:
            gaps[gap_size].add(index)
            index += gap_size

for file_id in reversed(range(len(files))):
    file_index, file_size = files[file_id]

    best_gap_index = float('inf')
    best_gap_size = None
    for gap_size, (*_, gap_index) in gaps.items():
        if gap_size < file_size:
            continue
        if gap_index < best_gap_index:
            best_gap_index = gap_index
            best_gap_size = gap_size
    
    if best_gap_size is None or best_gap_index > file_index:
        continue

    files[file_id][0] = gaps[best_gap_size].pop()
    new_gap_size = best_gap_size - file_size
    if new_gap_size == 0:
        continue
    new_gap_index = best_gap_index + file_size

    gaps[new_gap_size].add(new_gap_index)
    
    # I'm assuming there is no case where we need to merge new gaps with existing ones?
    # e.g  0.1.22 -> 01..22

answer2 = 0
for file_id, (file_index, file_size) in enumerate(files):
    for di in range(file_size):
        answer2 += file_id * (file_index + di)
print(answer2)

submit(answer2, part='b', day=9, year=2024)
