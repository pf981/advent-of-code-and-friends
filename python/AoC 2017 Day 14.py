from aocd import get_data

inp = get_data(day=14, year=2017)

import collections
import functools
import math
import operator


def reverse(nums, n):
    rev = collections.deque()

    for _ in range(n):
        rev.append(nums.popleft())

    while rev:
        nums.appendleft(rev.popleft())


def hash_lengths(lengths, n_rounds=1):
    nums = collections.deque(range(256))
    skip_size = 0
    total_rotation = 0

    for _ in range(n_rounds):
        for length in lengths:
            reverse(nums, length)

            rotation = length + skip_size
            total_rotation += rotation
            nums.rotate(-rotation)

            skip_size += 1

    nums.rotate(total_rotation)
    return list(nums)


def get_knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    sparse_hash = hash_lengths(lengths, n_rounds=64)
    dense_hash = [
        functools.reduce(operator.xor, l) for l in zip(*[iter(sparse_hash)] * 16)
    ]
    return ''.join(f'{i:0>8b}' for i in dense_hash)


def get_grid(s):
    grid = collections.defaultdict(bool)
    for row in range(128):
        for col, value in enumerate(get_knot_hash(f'{s}-{row}')):
            if value == '1':
                grid[(row, col)] = True
    return grid


grid = get_grid(inp)

answer = sum(grid.values())
print(answer)

def set_group(groups, grid, row, col):
    if not grid[(row, col)] or groups.get((row, col)):
        return

    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
    group = functools.reduce(
        (lambda a, b: a or b), (groups.get((row + dr, col + dc)) for dr, dc in offsets)
    )
    groups[(row, col)] = group or max(groups.values() or [0]) + 1

    for dr, dc in offsets:
        set_group(groups, grid, row + dr, col + dc)


groups = {}
for row in range(128):
    for col in range(128):
        set_group(groups, grid, row, col)

answer = len(set(groups.values()))
print(answer)
