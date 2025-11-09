import collections

with open("./input/38.txt") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    nums = tuple(int(s) for s in line.split())

    highest_comfort: collections.defaultdict[int, int] = collections.defaultdict(
        int
    )  # i -> longest_comfortable_streak_length

    for streak_length in range(1, len(nums) + 1):
        for i in range(len(nums) - streak_length + 1):
            subarray = nums[i : i + streak_length]

            # Comfortable
            if sum(subarray) % streak_length == 0:
                for j in range(i, i + streak_length):
                    if streak_length == highest_comfort[j] + 1:
                        highest_comfort[j] += 1

    answer += sum(highest_comfort.values())

print(answer)
