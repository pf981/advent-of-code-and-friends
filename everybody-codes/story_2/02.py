import collections
import itertools

with open("./story_2/input/everybody_codes_e2_q02_p1.txt") as f:
    text = f.read()

# text = "GRBGGGBBBRRRRRRRR"
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

# text = "GGBR"
# repeat = 5
# text = "BBRGGRRGBBRGGBRGBBRRBRRRBGGRRRBGBGG"
# repeat = 10

balloons = list(text) * repeat

it = itertools.cycle("RGB")
for answer2 in itertools.count(1):
    col = next(it)
    if col != balloons[0]:
        balloons.pop(0)
        # print(answer2, "\t", col, "\t", " ".join(balloons))
        if not balloons:
            break
        continue

    if len(balloons) % 2 == 0:  # and col != balloons[len(balloons) // 2]:
        balloons.pop(len(balloons) // 2)
    balloons.pop(0)
    # print(answer2, "\t", col, "\t", " ".join(balloons))
    if not balloons:
        break

print(answer2)

# Part 3


with open("./story_2/input/everybody_codes_e2_q02_p3.txt") as f:
    text = f.read()
repeat = 100_000

balloons = list(text) * repeat
left = collections.deque(balloons[: len(balloons) // 2])
right = collections.deque(balloons[len(balloons) // 2 :])

it = itertools.cycle("RGB")
for answer3 in itertools.count(1):
    col = next(it)
    if len(left) != len(right):
        left.popleft()
    elif left[0] == col:
        left.popleft()
        right.popleft()
    else:
        left.popleft()
        left.append(right.popleft())
    if not left and not right:
        break

print(answer3)
