import collections

with open("./input/2026/08/input1.txt") as f:
    text = f.read()
# text = """7 8
#  ################
#     ######      #
# ###   #####  ####
# ###           ###
# ####### ## #    #
# ####### ## ######
# #       ##      #
# #  #####  #######
# #  ######      ##
# # ######  #### ##
# #         #### ##
# #################"""

target, *grid = text.splitlines()
target = tuple(map(int, target.split()))
# target[0] -= 1
# target[1] -= 1

nrows = len(grid)
ncols = len(grid[0])
q = collections.deque([(0, 0)])
seen = {(0, 0)}
d = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        print(r, c)

        if (r, c) == target:
            print("FOUND!")
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if grid[r2][c2] == "#":
                continue
            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))
            q.append((r2, c2))

    else:
        d += 1
        continue
    break

answer = d
print(answer)
