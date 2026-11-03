with open("./input/12.txt") as f:
    text = f.read()
text = """11,0,-11:1,5,-6:4,2,-6:2,0,-2:2,1,-3:9,-3,-6:4,1,-5:4,-2,-2:0,1,-1:1,1,-2:2,5,-7:-2,2,0:7,-2,-5:2,3,-5:-2,0,2:3,2,-5:7,3,-10:4,3,-7:0,3,-3:8,-3,-5:2,-2,0:1,3,-4:4,5,-9:12,-2,-10:1,-3,2:-2,3,-1:8,3,-11:-2,1,1:5,-2,-3:6,4,-10:10,1,-11:1,4,-5:9,2,-11:5,4,-9:4,0,-4:2,-1,-1:10,-4,-6:2,-3,1:11,-1,-10:-1,3,-2:-1,-1,2:3,3,-6:12,-3,-9:12,-4,-8:3,-1,-2:11,-4,-7:0,-2,2:5,2,-7:3,5,-8:6,-2,-4"""

coords = [tuple(map(int, p.split(","))) for p in text.split(":")]
mins = [min(p) - 1 for p in zip(*coords)]
maxs = [max(p) + 1 for p in zip(*coords)]

outside = set()
directions = {
    "e": (1, -1, 0),
    "w": (-1, 1, 0),
    "ne": (1, 0, -1),
    "nw": (0, 1, -1),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
}


def mark_outside(x: int, y: int, z: int) -> None:
    if (x, y, z) in coords:
        return
    if (x, y, z) in outside:
        return
    if not (
        mins[0] <= x <= maxs[0] and mins[1] <= y <= maxs[1] and mins[2] <= z <= maxs[2]
    ):
        return

    outside.add((x, y, z))

    for dx, dy, dz in directions.values():
        x2 = x + dx
        y2 = y + dy
        z2 = z + dz
        mark_outside(x2, y2, z2)


mark_outside(*mins)

# answer = len(inside)
# print(answer)
