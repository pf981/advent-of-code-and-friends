with open("./story_4/input/everybody_codes_e4_q01_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """1,2,3,4,5,6,7,8,9
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30""".splitlines()

# lines = """1,1,1,1,1""".splitlines()

# lines = """1,1,1,1,1
# 5,1,2,3,4,5,1,2,3,4
# 2,1,1,2,1,1,2,1,1,2,1,1
# 5,1,2,1,2,7,1,2,1,2,7,1,2,1,2""".splitlines()

answer2 = 0
for line in lines:
    nums = list(map(int, line.split(",")))
    used = {0}
    i = 0
    for num in nums:
        i2 = i - num
        if i2 not in used and i2 >= 0:
            i = i2
        else:
            i = i + num
            while i in used:
                i += 1
            # assert i not in used
        used.add(i)
        print(num, i)
    # print(i)
    answer2 += i

print(answer2)
