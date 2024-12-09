from aocd import get_data, submit


def checksum(nums):
    result = 0
    for i, num in enumerate(nums):
        if num == -1:
            print('!!!')
            break
        result += i * num
    return result

inp = get_data(day=9, year=2024)

# inp = '''2333133121414131402
# '''

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
    # print(i, j, data[i], data[j])
    if not i <= j:
        break
    if i == -1:
        break
    data[i], data[j] = data[j], data[i]

all(x == -1 for x in data[data.index(-1):])
# 01234567890123456789012345678
# 0099811188827773336446555566..............

answer1 = checksum(data)
print(answer1)

# submit(answer1, part='a', day=9, year=2024)


# Part 2


def checksum(nums):
    result = 0
    for i, num in enumerate(nums):
        if num == -1:
            continue
        result += i * num
    return result


def try_fit(data, i, j):
    pass

inp = get_data(day=9, year=2024)

# inp = '''2333133121414131402
# '''

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
while j >= 0:
    # print(''.join(str(c) if c != -1 else '.'for c in data))

    # File
    while j >= 0 and data[j] == -1:
        j -= 1
    if i == -1:
        break

    file_size = 1
    while j > 0 and data[j-1] == data[j]:
        file_size += 1
        j -= 1


    # Find gap
    i = 0
    while i < len(data):
        while i < len(data) and data[i] != -1:
            i += 1
        if i == len(data):
            continue # 
        
        gap_size = 0
        while i + gap_size < len(data) and data[i] == data[i + gap_size]:
            gap_size += 1
        
        if gap_size >= file_size:
            break
        i += gap_size
    else:
        j -= 1
        continue


    if not i <= j:
        j -= 1
        continue

    # print(f'{i=} {j=} {file_size=} {gap_size=} {data[i]=} {data[j]=}')

    # if gap_size < file_size:
    #     j -= 1
    #     continue

    for _ in range(file_size):
        data[i], data[j] = data[j], data[i]
        i += 1
        j += 1
    j -= 1

print(''.join(str(c) if c != -1 else '.'for c in data))
# # all(x == -1 for x in data[data.index(-1):])
# 01234567890123456789012345678901234567890
# 00...111...2...333.44.5555.6666.777.888899

answer2 = checksum(data)
print(answer2)

# submit(answer2, part='b', day=9, year=2024)

# Probably should use a heap