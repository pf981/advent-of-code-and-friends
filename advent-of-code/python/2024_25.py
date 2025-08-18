from aocd import get_data, submit


inp = get_data(day=25, year=2024)
groups = inp.split('\n\n')
locks = []
keys = []
for group in groups:
    lines = group.splitlines()
    if all(ch == '#' for ch in lines[0]):
        # Lock
        lock = []
        for col in zip(*reversed(lines[1:])):
            col = col[::-1]
            lock.append(col.index('.'))
        locks.append(lock)
        continue

    # Key
    key = []
    for col in zip(*reversed(lines[:-1])):
        key.append(col.index('.'))
    keys.append(key)

fits = 0
for lock in locks:
    for key in keys:
        for l, k in zip(lock, key):
            if 5 - k < l:
                break
        else:
            fits += 1
answer1 = fits
print(answer1)

submit(answer1, part='a', day=25, year=2024)


# Part 2


# No puzzle here - just need 49 stars.
