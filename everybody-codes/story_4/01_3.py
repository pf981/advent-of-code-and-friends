with open("./story_4/input/everybody_codes_e4_q01_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """1,2,3,4,5,6,7,8,9
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30""".splitlines()

# lines = """1,1,1,1,1""".splitlines()

# lines = """5,1,2,3,4,5,1,2,3,4""".splitlines()
# lines = """2,1,1,2,1,1,2,1,1,2,1,1""".splitlines()

# lines = """1,1,1,1,1
# 5,1,2,3,4,5,1,2,3,4
# 2,1,1,2,1,1,2,1,1,2,1,1
# 5,1,2,1,2,7,1,2,1,2,7,1,2,1,2""".splitlines()

# lines = """5,3,1,1
# 5,3,1,1,5,1,1,3,4,8,1,1
# 5,3,1,1,5,1,1,3,4,8,2,1
# 10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1""".splitlines()

# lines = """5,3,1,1""".splitlines()
# lines = """5,3,1,1,5,1,1,3,4,8,1,1""".splitlines()
# lines = """5,3,1,1,5,1,1,3,4,8,2,1""".splitlines()

answer2 = 0
for line in lines:
    nums = list(map(int, line.split(",")))
    used = {0}

    # walls = {True: {0}, False: set()}  # is_below -> {i, ...}
    walls = {True: set(), False: set([0])}  # is_below -> {i, ...} # FIXME: TEST
    labels = {}  # (is_below, i) -> {label}

    is_below = True

    i = 0
    for label_i, num in enumerate(nums):
        print(f"{num=} {i=}")

        # Can move back
        i2 = i - 1
        can_move_back = False
        cur_labels = set()
        while True:
            if i2 == i - num:
                can_move_back = i2 >= 0 and not cur_labels and i2 not in walls[is_below]
                break

            if (is_below, i2) in labels:
                label = labels[(is_below, i2)]
                if label in cur_labels:
                    cur_labels.discard(label)
                else:
                    cur_labels.add(label)
            i2 -= 1
        if can_move_back:
            walls[is_below].add(i)
            labels[(is_below, i)] = label_i
            i -= num
            used.add(i)
            walls[is_below].add(i)
            labels[(is_below, i)] = label_i

            is_below = not is_below
            continue

        # Try move forward
        cur_labels = set()
        i2 = i + 1
        while True:
            # if i2 in walls[is_below]:
            #     break
            # print(f"  {is_below=} {i2=} {cur_labels=}")
            if i2 > 1000:
                print("DEBUG")
                break

            if (is_below, i2) in labels:
                label = labels[(is_below, i2)]
                if label in cur_labels:
                    cur_labels.discard(label)
                else:
                    cur_labels.add(label)

            # print(f"    {i2 not in used=} {i2 >= i + num=} {not cur_labels=}")
            if i2 not in used and i2 >= i + num and not cur_labels:
                walls[is_below].add(i)
                labels[(is_below, i)] = label_i
                i = i2
                used.add(i)
                walls[is_below].add(i)
                labels[(is_below, i)] = label_i

                is_below = not is_below
                break

            i2 += 1
    # print(i)
    answer2 += i

print(answer2)
