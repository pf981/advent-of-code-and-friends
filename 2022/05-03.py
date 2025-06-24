import downloader


lines = downloader.get_puzzle(2).splitlines()

winning_nums = [12, 48, 30, 95, 15, 55, 97]
prizes = [0, 0, 0, 1, 10, 100, 1000]

answer = 0
for line in lines:
    nums = [int(s) for s in line.split()]
    wins = sum(num in winning_nums for num in nums)
    answer += prizes[wins]

answer = answer
print(answer)
