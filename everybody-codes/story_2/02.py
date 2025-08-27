import collections
import itertools

with open("./story_2/input/everybody_codes_e2_q02_p1.txt") as f:
    text = f.read()

greens = text.count("G")
reds = len(text) - greens

it = itertools.cycle("RG")
answer1 = 0
while greens > 0 and reds > 0:
    if next(it) == "G":
        reds -= 1
    else:
        greens -= 1
    answer1 += 1

print(answer1)


# Part 2


def count_shots(balloons: list[str]) -> int:
    left = collections.deque(balloons[: len(balloons) // 2])
    right = collections.deque(balloons[len(balloons) // 2 :])

    it = itertools.cycle("RGB")
    result = 0
    while right or left:
        col = next(it)

        if len(left) > len(right):
            left.popleft()
        elif len(right) > len(left):
            left.append(right.popleft())
            left.popleft()
        else:
            if left[0] == col:
                right.popleft()
            left.popleft()

        result += 1

    return result


with open("./story_2/input/everybody_codes_e2_q02_p2.txt") as f:
    text = f.read()
repeat = 100

answer2 = count_shots(list(text) * repeat)
print(answer2)

# Part 3


with open("./story_2/input/everybody_codes_e2_q02_p3.txt") as f:
    text = f.read()
repeat = 100_000

answer3 = count_shots(list(text) * repeat)
print(answer3)
