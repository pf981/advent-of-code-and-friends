with open("./story_4/input/everybody_codes_e4_q01_p2.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    nums = list(map(int, line.split(",")))
    used = {0}
    i = 0
    for num in nums:
        if i - num not in used and i - num >= 0:
            i -= num
        else:
            i += num
            while i in used:
                i += 1
        used.add(i)

    answer += i

print(answer)
