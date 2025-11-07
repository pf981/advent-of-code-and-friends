def parse_line(line: str) -> tuple[int, list[int]]:
    id_, nums_str = line.split(":")
    nums = [int(num_str) for num_str in nums_str.split(",")]
    return int(id_), nums


def get_metrics(nums: list[int]) -> tuple[int, list[int]]:
    tree: list[list[int]] = []

    def place(num):
        for i in range(len(tree)):
            node = tree[i]
            if num < node[1] and node[0] is None:
                node[0] = num
                return
            if num > node[1] and node[2] is None:
                node[2] = num
                return
        tree.append([None, num, None])

    for num in nums:
        place(num)

    scores = []
    for node in tree:
        score = int("".join(str(val) for val in node if val is not None))
        scores.append(score)

    quality = int("".join(str(node[1]) for node in tree))

    return quality, scores


with open("./2025/input/everybody_codes_e2025_q05_p1.txt") as f:
    lines = f.read().splitlines()

_id_, nums = parse_line(lines[0])
quality, _score = get_metrics(nums)

answer1 = quality
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q05_p2.txt") as f:
    lines = f.read().splitlines()

highest = 0
lowest = float("inf")

for line in lines:
    _id_, nums = parse_line(line)
    quality, _score = get_metrics(nums)

    highest = max(highest, quality)
    lowest = min(lowest, quality)

answer2 = highest - lowest
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q05_p3.txt") as f:
    lines = f.read().splitlines()

metrics = []

for line in lines:
    id_, nums = parse_line(line)
    quality, score = get_metrics(nums)

    metrics.append((quality, score, id_))


metrics.sort(reverse=True)
answer3 = 0
for i, (_quality, _score, id_) in enumerate(metrics, 1):
    answer3 += i * id_
print(answer3)
