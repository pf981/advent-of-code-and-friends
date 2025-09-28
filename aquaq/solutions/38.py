import functools


@functools.cache
def get_streak_left(i: int, nums: tuple[int, ...]) -> tuple[int, ...]:
    if i < 0:
        return tuple()

    return (nums[i],) + tuple(
        streak + nums[i] for streak in get_streak_left(i - 1, nums)
    )


@functools.cache
def get_streak_right(i: int, nums: tuple[int, ...]) -> tuple[int, ...]:
    if i == len(nums):
        return tuple()

    return (nums[i],) + tuple(
        streak + nums[i] for streak in get_streak_right(i + 1, nums)
    )


def get_score(i: int, nums: tuple[int, ...]) -> int:
    score_left = score_right = 0
    for score_left, streak in enumerate(get_streak_left(i - 1, nums), 1):
        if streak % score_left:
            break
    for score_right, streak in enumerate(get_streak_right(i - 1, nums), 1):
        if streak % score_right:
            break
    return max(score_left, score_right) - 1


with open("./input/38.txt") as f:
    text = f.read()

text = """1 3 2"""

for line in text.splitlines():
    nums = tuple(int(s) for s in line.split())
    for i in range(len(nums)):
        print(get_score(i, nums))
