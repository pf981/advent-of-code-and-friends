with open("./2025/input/everybody_codes_e2025_q16_p3.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()
total_blocks = 202520252025000

# lines = """1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2""".splitlines()
nums = [int(x) for x in lines[0].split(",")]


nums = [int(x) for x in lines[0].split(",")]
magnatude = nums.copy()
n = len(nums)
cols = [0] * n
answer = 1
spell = []
for i in range(len(nums)):
    # print(f"{magnatude=}")
    num = i + 1
    mag = magnatude[i]
    if magnatude[i] == 0:
        continue

    answer *= mag * num
    spell.extend([num] * mag)

    for x in range(num - 1, n, num):
        cols[x] += mag
        magnatude[x] -= mag


nums = spell


def can_build(wall_length, total_blocks):
    target = wall_length

    n = target
    # cols = [0] * n
    ncols = 0
    for num in nums:
        # for x in range(num - 1, n, num):
        #     # cols[x] += 1
        #     ncols += 1
        ncols += len(range(num - 1, n, num))

    # print(f"{cols=}")
    return ncols <= total_blocks


l = 0
r = 9443949576295400
answer = 0
while l <= r:
    m = (l + r) // 2
    # print(f"{m=} {total_blocks=}")
    if can_build(m, total_blocks):
        answer = m
        l = m + 1
    else:
        r = m - 1
print(answer)

# can_build(1, 1) # Expect True
# can_build(2, 1) # Expect False
# can_build(4664, 10000)
# can_build(4664, 900)

# print(answer)


# blocks     the length of the wall
#                1                          1
#               10                          5
#              100                         47
#             1000                        467
#            10000                       4664
#           100000                      46633
#          1000000                     466322
#         10000000                    4663213
#        100000000                   46632125
#       1000000000                  466321244
#      10000000000                 4663212435
#     100000000000                46632124353
#    1000000000000               466321243524
#   10000000000000              4663212435233
#  100000000000000             46632124352332
#  202520252025000             94439495762954
