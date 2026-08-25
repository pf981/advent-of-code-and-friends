with open("./story_4/input/everybody_codes_e4_q01_p3.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    nums = list(map(int, line.split(",")))
    used = {0}
    walls = {True: set(), False: {0}}  # is_below -> {i, ...}
    labels = {}  # (is_below, i) -> {label}

    is_below = True

    i = 0
    for label_i, num in enumerate(nums):
        # Try move back
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
            if i2 > 1000:
                break

            if (is_below, i2) in labels:
                label = labels[(is_below, i2)]
                if label in cur_labels:
                    cur_labels.discard(label)
                else:
                    cur_labels.add(label)

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

    answer += i

print(answer)
