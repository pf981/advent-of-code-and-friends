import collections
import functools
import re


with open("2025_contest/17.txt") as f:
    inp = f.read()

staircases_s, possible_moves_s = inp.split("\n\n")
possible_moves = [
    int(num) for num in re.findall(r"-?[0-9]+", possible_moves_s.splitlines()[0])
]


@functools.cache
def count_ways(i):
    if i == 99:
        return 1
    if i > 99:
        return None

    result = 0
    for di in possible_moves:
        ways = count_ways(i + di)
        if ways is not None:
            result += ways
    return result


answer1 = count_ways(0)
print(answer1)


# Part 2


def get_next_positions(pos):
    def _get_next_positions(pos, move):
        if move == 0:
            return {pos}

        next_positions = set()
        for pos2 in m[pos]:
            next_positions.update(_get_next_positions(pos2, move - 1))
        return next_positions

    return {pos2 for move in possible_moves for pos2 in _get_next_positions(pos, move)}


@functools.cache
def count_ways(pos):
    if pos == end_pos:
        return 1
    if pos[1] > end_pos[1]:
        return 0

    result = 0
    moves = get_next_positions(pos)
    for pos2 in moves:
        result += count_ways(pos2)
    return result


staircases = []
for line in staircases_s.splitlines():
    staircase_id, start, end, from_staircase, to_staircase = re.match(
        r"S(\d+) : (\d+) -> (\d+) : FROM (.+) TO (.+)", line
    ).groups()

    staircases.append(
        (
            int(staircase_id),
            int(start),
            int(end),
            int(from_staircase[1:]) if from_staircase != "START" else from_staircase,
            int(to_staircase[1:]) if to_staircase != "END" else to_staircase,
        )
    )

start_pos = None
end_pos = None
m = collections.defaultdict(
    list
)  # (staircase_id, stair) -> [(staircaes_id, stair), ...]

for staircase_id, start, end, from_staircase, to_staircase in staircases:
    for step in range(start, end):
        m[(staircase_id, step)].append((staircase_id, step + 1))

    if from_staircase == "START":
        start_pos = (staircase_id, start)
    else:
        m[(from_staircase, start)].append((staircase_id, start))

    if to_staircase == "END":
        end_pos = (staircase_id, end)
    else:
        m[(staircase_id, end)].append((to_staircase, end))


answer2 = count_ways(start_pos)
print(answer2)


# Part 3


path = [f"S{start_pos[0]}_{start_pos[1]}"]
pos = start_pos
rank = 0
while pos != end_pos:
    for pos2 in sorted(get_next_positions(pos)):
        ways = count_ways(pos2)
        if rank + ways < 100000000000000000000000000000:
            rank += ways
        else:
            break
    path.append(f"S{pos2[0]}_{pos2[1]}")
    pos = pos2

answer3 = "-".join(path)
print(answer3)
