import math

with open("./input/2026/04/input2.txt") as f:
    text = f.read()

letters = {
    "L": "Mud",
    "Z": "Volcanic Ash",
    "G": "Grass",
    "O": "Fallen Logs",
    "N": "Deep Water",
    "A": "Thorns",
    "M": "Sand",
    "I": "Flowers",
    "H": "Forests",
    "J": "Permafrost",
    "E": "Shallow Water",
    "S": "Pebbles",
    "P": "Rocks",
    "Y": "Mud",
    "D": "Volcanic Ash",
    "V": "Grass",
    "T": "Fallen Logs",
    "U": "Deep Water",
    "K": "Thorns",
    "C": "Sand",
    "Q": "Flowers",
    "F": "Forests",
    "R": "Permafrost",
    "X": "Shallow Water",
    "W": "Pebbles",
    "B": "Rocks",
}

materials = {
    "Mud": "Fresh Water",
    "Volcanic Ash": "Charcoal",
    "Grass": "Grain",
    "Fallen Logs": "Mushrooms",
    "Deep Water": "Giant Fish",
    "Thorns": "Berries",
    "Sand": "Glass",
    "Flowers": "Honey",
    "Forests": "Amber",
    "Permafrost": "Quartz",
    "Shallow Water": "Shells",
    "Pebbles": "Gems",
    "Rocks": "Gold",
}

prices = {
    "Fresh Water": 199_80,
    "Charcoal": 259_30,
    "Grain": 299_20,
    "Mushrooms": 399_70,
    "Giant Fish": 459_90,
    "Berries": 599_10,
    "Glass": 649_40,
    "Honey": 699_00,
    "Amber": 749_70,
    "Quartz": 799_50,
    "Shells": 849_10,
    "Gems": 899_40,
    "Gold": 899_60,
}

lines = text.splitlines()

nrows = len(lines)
ncols = len(lines[0])

dr = nrows / 100_000
dc = ncols / 100_000
r = R = nrows / 100_000_000
c = C = ncols / 100_000_000

i = 0
seen = set()
while r < nrows + 1 and c < ncols + 1:
    r = math.floor(R + dr * i)
    c = math.floor(C + dc * i)
    i += 1
    if r >= nrows or c >= ncols:
        break
    seen.add((r, c))

answer = 0
for r, c in seen:
    answer += prices[materials[letters[lines[r][c]]]]

answer /= 100
if int(answer) == answer:
    answer = int(answer)
print(answer)
