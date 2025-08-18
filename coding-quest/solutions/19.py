import downloader

nums = [int(line) for line in downloader.get_puzzle(19).splitlines()]

answer = 0
n = 0
mask = -1 ^ (1 << 15)
for num in nums:
    val = num & mask
    if num >> 15 == val.bit_count() & 1:
        answer += val
        n += 1

answer = round(answer / n)
print(answer)
