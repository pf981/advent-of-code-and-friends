from aocd import get_data

inp = get_data(day=11, year=2017)

def get_distances(directions):
    x = y = z = 0
    ds = [0]
    for direction in directions:
        x += (direction in ["se", "ne"]) - (direction in ["nw", "sw"])
        y += (direction in ["n", "nw"]) - (direction in ["s", "se"])
        z += (direction in ["s", "sw"]) - (direction in ["n", "ne"])
        ds.append((abs(abs(x)) + abs(y) + abs(z)) // 2)
    return ds


distances = get_distances(inp.split(','))

answer = distances[-1]
print(answer)

answer = max(distances)
print(answer)
