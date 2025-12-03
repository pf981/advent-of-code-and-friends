from aocd import get_data, submit


inp = get_data(day=3, year=2025)

# inp = '''
# '''

lines = inp.splitlines()
answer1=0
for line in lines:
    max_val = 0
    max_prev = 0
    for x in line:
        x = int(x)
        max_val = max(max_val, 10 * max_prev + x)
        if x  > max_prev:
            max_prev = x
    answer1 += max_val

# answer1 = None
print(answer1)

submit(answer1, part='a', day=3, year=2025)


# Part 2
import functools

lines = inp.splitlines()

@functools.cache
def get_max_val(i, n, word):
    if n == 0:
        # if i != len(word):
        #     return None
        return 0
    
    if i == len(word):
        return None

    # Discard
    discard = get_max_val(i + 1, n, word)

    # Keep
    res = get_max_val(i + 1, n - 1, word)
    if res is not None:
        keep = int(word[i]) * (10**(n-1)) + get_max_val(i + 1, n - 1, word)
    else:
        keep = None

    # return max(discard or 0, keep or 0)
    if discard is None and keep is None:
        return None
    if discard is None:
        return keep
    if keep is None:
        return discard

    return max(discard, keep)

answer2=0
for line in lines:
    # max_val = get_max_val(0, 12, line)
    max_val = get_max_val(0, 12, line)
    print(f'{max_val=}')
    # if max_val is None:
    #     max_val = 0
    answer2 += max_val


print(answer2)

submit(answer2, part='b', day=3, year=2025)
