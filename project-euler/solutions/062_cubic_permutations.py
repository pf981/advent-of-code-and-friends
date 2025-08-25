import collections

MAX_CUBES = 50000

cube_counts: collections.defaultdict[str, int] = collections.defaultdict(int)
cubes = collections.defaultdict(list)

for n in range(MAX_CUBES):
    cube = n**3
    sorted_cube = "".join(sorted(str(cube)))
    cube_counts[sorted_cube] += 1
    cubes[sorted_cube].append(cube)

answer = min(
    min(cubes[sorted_cube]) for sorted_cube, count in cube_counts.items() if count == 5
)
print(answer)
