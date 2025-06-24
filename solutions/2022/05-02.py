import downloader


lines = downloader.get_puzzle(1).splitlines()

nums = [int(line) for line in lines]
answer = total = n = left = 0
for right in range(len(nums)):
    total += nums[right]
    n += 1

    if n > 60:
        total -= nums[left]
        left += 1
        n -= 1

    if n == 60 and not (1500 <= total / n <= 1600):
        answer += 1

print(answer)
