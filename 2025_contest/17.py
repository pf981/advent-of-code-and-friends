import functools
import re


with open("2025_contest/17.txt") as f:
    inp = f.read()

staircases, possible_moves = inp.split("\n\n")
possible_moves = [
    int(num) for num in re.findall(r"-?[0-9]+", possible_moves.splitlines()[0])
]

first = staircases.splitlines()[0]


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


# inp = """S1 : 0 -> 6 : FROM START TO END
# S2 : 2 -> 4 : FROM S1 TO S1
# S3 : 3 -> 5 : FROM S2 TO S1

# Possible Moves : 1, 2"""

# staircases_s, possible_moves_s = inp.split("\n\n")
# possible_moves = [
#     int(num) for num in re.findall(r"-?[0-9]+", possible_moves_s.splitlines()[0])
# ]

# # re.match(
# #     r"(S\d+) : (\d+) -> (\d+) : FROM (.+) TO (.+)", "S1 : 0 -> 6 : FROM START TO END"
# # ).groups()
# import collections

# m = collections.defaultdict(
#     list
# )  # (staircase_id, stair) -> [(staircaes_id, stair), ...]

# staircases = []
# for line in staircases_s.splitlines():
#     staircase_id, start, end, from_staircase, to_staircase = re.match(
#         r"(S\d+) : (\d+) -> (\d+) : FROM (.+) TO (.+)", line
#     ).groups()

#     print(staircase_id, start, end, from_staircase, to_staircase)
#     staircases.append(
#         (staircase_id, int(start), int(end), from_staircase, to_staircase)
#     )


# for staircase_id, start, end, from_staircase, to_staircase in staircases:
#     for step in range(start, end):
#         m[(staircase_id, step)].append((staircase_id, step + 1))

# # FROM
# # TO
