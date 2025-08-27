import collections
import itertools

with open("./story_2/input/everybody_codes_e2_q02_p1.txt") as f:
    text = f.read()

greens = [i for i, c in enumerate(text) if c == "G"]
reds = [i for i, c in enumerate(text) if c == "R"]

greens.reverse()
reds.reverse()
it = itertools.cycle("RG")
answer1 = 0
while greens and reds:
    if next(it) == "G":
        if reds:
            reds.pop()
    else:
        if greens:
            greens.pop()
    answer1 += 1

print(answer1)


# Part 2


with open("./story_2/input/everybody_codes_e2_q02_p2.txt") as f:
    text = f.read()
repeat = 100

balloons = list(text) * repeat

it = itertools.cycle("RGB")
answer2 = 0
while balloons:
    col = next(it)

    if col == balloons[0] and len(balloons) % 2 == 0:
        balloons.pop(len(balloons) // 2)

    balloons.pop(0)

    answer2 += 1

print(answer2)

# Part 3


with open("./story_2/input/everybody_codes_e2_q02_p3.txt") as f:
    text = f.read()
repeat = 100_000

balloons = list(text) * repeat
left = collections.deque(balloons[: len(balloons) // 2])
right = collections.deque(balloons[len(balloons) // 2 :])

it = itertools.cycle("RGB")
answer3 = 0
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

    answer3 += 1

print(answer3)
