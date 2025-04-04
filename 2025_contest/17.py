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
        return 0

    return sum(count_ways(i + move) for move in possible_moves)


answer1 = count_ways(0)
print(answer1)


# Part 2


def get_next_positions(pos):
    next_positions = set()
    for move in possible_moves:
        q = collections.deque([pos])
        while q and move:
            for _ in range(len(q)):
                cur_pos = q.popleft()
                q.extend(m[cur_pos])
                for next_pos in m[cur_pos]:
                    q.append(next_pos)
            move -= 1
        next_positions.update(q)

    return next_positions


@functools.cache
def count_ways2(pos):
    if pos == end_pos:
        return 1
    return sum(count_ways2(pos2) for pos2 in get_next_positions(pos))


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


answer2 = count_ways2(start_pos)
print(answer2)


# Part 3


path = [f"S{start_pos[0]}_{start_pos[1]}"]
pos = start_pos
rank = 0
while pos != end_pos:
    for pos2 in sorted(get_next_positions(pos)):
        ways = count_ways2(pos2)
        if rank + ways < 100000000000000000000000000000:
            rank += ways
        else:
            break
    path.append(f"S{pos2[0]}_{pos2[1]}")
    pos = pos2

answer3 = "-".join(path)
print(answer3)
