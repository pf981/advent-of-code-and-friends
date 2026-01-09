import collections
import itertools

with open("data/day21.txt") as f:
    text = f.read()
text = """#####
#O#.#
#...O
#.#.#
#####

###O#
#O#.#
#.#.#
#...#
##.##

#####
#####
#####
#####
#####

#####
#####
#####
#####
#####

#####
#####
#####
#####
#####

#####
#####
#####
#####
#####"""

parts = text.split("\n\n")
n = len(text[0].splitlines())

edges = {
    "FN": ("U", "S", False),
    "FS": ("D", "N", False),
    "FW": ("L", "E", False),
    "FE": ("F", "W", False),
    "DN": ("F", "S", False),
    "DS": ("B", "N", False),
    "DW": ("L", "S", True),
    "DE": ("R", "S", False),
    "LN": ("U", "W", False),
    "LS": ("D", "W", True),
    "LW": ("B", "W", True),
    "LE": ("F", "W", False),
    "RN": ("U", "E", True),
    "RS": ("D", "E", False),
    "RW": ("F", "E", False),
    "RE": ("B", "E", True),
    "UN": ("B", "S", False),
    "US": ("F", "N", False),
    "UW": ("L", "N", False),
    "UE": ("R", "N", True),
    "BN": ("D", "S", False),
    "BS": ("U", "N", False),
    "BW": ("L", "W", True),
    "BE": ("R", "E", True),
}

rotations = {}  # (i, rotation) -> (valid, outlets)
for i, part in enumerate(parts):
    grid = [list(line) for line in part.splitlines()]

    for rotation in range(3):
        valid = set()
        outlets = []
        for r, line in enumerate(grid):
            for c, ch in enumerate(line):
                if ch in "O.":
                    valid.add((r, c))
                if ch == "O":
                    outlets.append((r, c))

        assert len(outlets) in [2, 0]

        rotations[(i, rotation)] = (frozenset(valid), frozenset(outlets))
        grid = [row[::-1] for row in zip(*grid)]


def is_solvable(configuration: list[tuple[int, int]]) -> bool:
    valid = set()
    outlets = set()
    for face, (i, rot) in enumerate(configuration):
        face_valids, face_outlets = rotations[(i, rot)]
        for v in face_valids:
            valid.add((face, *v))
        for o in face_outlets:
            outlets.add((face, *o))

    start = list(outlets)[0]
    q = collections.deque([start])
    valid.remove(start)
    outlets.remove(start)

    while q and outlets:
        face, r, c = q.popleft()
        raise NotImplementedError()
        # Probably don't have to properly check if it is solvable. It looks like the edge walls are set up so
        # there aren't that many configurations where the gaps perfectly align

    return len(outlets) == 0


# F is always (0, 0)
# [(B U D L R), ...]
configurations = []
for rots in itertools.product(*([range(4)] * 5)):
    rots = list(enumerate(rots))
    for perm in itertools.permutations(rots):
        configuration = [(0, 0), *perm]
        if is_solvable(configuration):
            configurations.append(configuration)

raise NotImplementedError()

answer = "TODO"
print(answer)
