import re
import itertools

with open("./story_2/input/everybody_codes_e2_q03_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """1: values=[1,2,3,4,5,6] seed=7
# 2: values=[-1,1,-1,1,-1] seed=13
# 3: values=[9,8,7,8,9] seed=17""".splitlines()

# lines = "1: faces=[1,2,4,-1,5,7,9] seed=3".splitlines()

dice = []
numreg = r"-?[0-9]+"
for line in lines:
    a, b, c = line.split(" ")
    a = int(re.findall(numreg, a)[0])
    b = [int(x) for x in re.findall(numreg, b)]
    c = int(re.findall(numreg, c)[0])
    dice.append((a, b, c))

pulses = [seed for _, _, seed in dice]
faces = [0] * len(pulses)
i = 0
total = 0
for roll_number in itertools.count(1):
    for i in range(len(pulses)):
        spin = roll_number * pulses[i]
        pulses[i] = pulses[i] + spin
        pulses[i] = pulses[i] % dice[i][2]
        pulses[i] = pulses[i] + 1 + roll_number + dice[i][2]
        # print(f"{spin=}")
        faces[i] = (faces[i] + spin) % len(dice[i][1])
        res = dice[i][1][faces[i]]
        # print(f"{roll_number=} {spin=} {res=} {pulses[i]=}")
        total += res
    if total >= 10000:
        break

answer1 = roll_number

print(answer1)


# Part 2


with open("./story_2/input/everybody_codes_e2_q03_p2.txt") as f:
    text = f.read()

# text = """1: values=[1,2,3,4,5,6,7,8,9] seed=13
# 2: values=[1,2,3,4,5,6,7,8,9] seed=29
# 3: values=[1,2,3,4,5,6,7,8,9] seed=37
# 4: values=[1,2,3,4,5,6,7,8,9] seed=43

# 51257284"""


a, track = text.split("\n\n")
lines = a.splitlines()
track = [int(x) for x in track]

dice = []
numreg = r"-?[0-9]+"
for line in lines:
    a, b, c = line.split(" ")
    a = int(re.findall(numreg, a)[0])
    b = [int(x) for x in re.findall(numreg, b)]
    c = int(re.findall(numreg, c)[0])
    dice.append((a, b, c))


pulses = [seed for _, _, seed in dice]
faces = [0] * len(pulses)
track_pos = [0] * len(pulses)
i = 0
winners = []
for roll_number in itertools.count(1):
    do_continue = False
    for i in range(len(pulses)):
        if track_pos[i] == len(track):
            continue
        do_continue = True

        spin = roll_number * pulses[i]
        pulses[i] = pulses[i] + spin
        pulses[i] = pulses[i] % dice[i][2]
        pulses[i] = pulses[i] + 1 + roll_number + dice[i][2]
        # print(f"{spin=}")
        faces[i] = (faces[i] + spin) % len(dice[i][1])
        res = dice[i][1][faces[i]]
        # print(f"{roll_number=} {spin=} {res=} {pulses[i]=} {track_pos[i]}")
        if res == track[track_pos[i]]:
            track_pos[i] += 1
            if track_pos[i] == len(track):
                winners.append(i + 1)
    if not do_continue:
        break


answer2 = ",".join(str(x) for x in winners)
print(answer2)


# Part 3

with open("./story_2/input/everybody_codes_e2_q03_p3.txt") as f:
    text = f.read()


# text = """1: faces=[1,2,3,4,5,6,7,8,9] seed=339211
# 2: faces=[1,2,3,4,5,6,7,8,9] seed=339517
# 3: faces=[1,2,3,4,5,6,7,8,9] seed=339769
# 4: faces=[1,2,3,4,5,6,7,8,9] seed=339049
# 5: faces=[1,2,3,4,5,6,7,8,9] seed=338959
# 6: faces=[1,2,3,4,5,6,7,8,9] seed=340111
# 7: faces=[1,2,3,4,5,6,7,8,9] seed=339679
# 8: faces=[1,2,3,4,5,6,7,8,9] seed=339121
# 9: faces=[1,2,3,4,5,6,7,8,9] seed=338851

# 94129478611916584144567479397512595367821487689499329543245932151
# 45326719759656232865938673559697851227323497148536117267854241288
# 44425936468288462848395149959678842215853561564389485413422813386
# 64558359733811767982282485122488769592428259771817485135798694145
# 17145764554656647599363636643624443394141749674594439266267914738
# 89687344812176758317288229174788352467288242171125512646356965953
# 72436836424726621961424876248346712363842529736689287535527512173
# 18295771348356417112646514812963612341591986162693455745689374361
# 56445661964557624561727322332461348422854112571195242864151143533
# 77537797151985578367895335725777225518396231453691496787716283477
# 37666899356978497489345173784484282858559847597424967325966961183
# 26423131974661694562195955939964966722352323745667498767153191712
# 99821139398463125478734415536932821142852955688669975837535594682
# 17768265895455681847771319336534851247125295119363323122744953158
# 25655579913247189643736314385964221584784477663153155222414634387
# 62881693835262899543396571369125158422922821541597516885389448546
# 71751114798332662666694134456689735288947441583123159231519473489
# 94932859392146885633942828174712588132581248183339538341386944937
# 53828883514868969493559487848248847169557825166338328352792866332
# 54329673374115668178556175692459528276819221245996289611868492731
# 97799599164121988455613343238811122469229423272696867686953891233
# 56249752581283778997317243845187615584225693829653495119532543712
# 39171354221177772498317826968247939792845866251456175433557619425
# 56425749216121421458547849142439211299266255482219915528173596421
# 48679971256541851497913572722857258171788611888347747362797259539
# 32676924489943265499379145361515824954991343541956993467914114579
# 45733396847369746189956225365375253819969643711633873473662833395
# 42291594527499443926636288241672629499242134451937866578992236427
# 47615394883193571183931424851238451485822477158595936634849167455
# 16742896921499963113544858716552428241241973653655714294517865841
# 57496921774277833341488566199458567884285639693339942468585269698
# 22734249697451127789698862596688824444191118289959746248348491792
# 28575193613471799766369217455617858422158428235521423695479745656
# 74234343226976999161289522983885254212712515669681365845434541257
# 43457237419516813368452247532764649744546181229533942414983335895"""

# text = """1: values=[1,2,3,4,5,6,7,8,9] seed=13

# 1523758297
# 4822941583
# 7627997892
# 4397697132
# 1799773472"""

import functools
import re
import itertools
import sys

sys.setrecursionlimit(150000)

a, grid = text.split("\n\n")
lines = a.splitlines()
grid = [[int(x) for x in line] for line in grid.splitlines()]

dice = []
numreg = r"-?[0-9]+"
for line in lines:
    a, b, c = line.split(" ")
    a = int(re.findall(numreg, a)[0])
    b = [int(x) for x in re.findall(numreg, b)]
    c = int(re.findall(numreg, c)[0])
    dice.append((a, b, c))

nrows = len(grid)
ncols = len(grid[0])

rolls = [[] for _ in range(len(dice))]
pulses = [seed for _, _, seed in dice]
faces = [0] * len(pulses)
track_pos = [0] * len(pulses)
i = 0

# What about looping back on itself?
for roll_number in range(1, nrows * ncols * 3):
    # for roll_number in range(1, int(nrows * ncols * 1.5)):
    for i in range(len(pulses)):
        do_continue = True

        spin = roll_number * pulses[i]
        pulses[i] = pulses[i] + spin
        pulses[i] = pulses[i] % dice[i][2]
        pulses[i] = pulses[i] + 1 + roll_number + dice[i][2]
        # print(f"{spin=}")
        faces[i] = (faces[i] + spin) % len(dice[i][1])
        res = dice[i][1][faces[i]]
        rolls[i].append(res)

good = set()  # {(r, c), ..}

seen = set()  # r ,c, dice_i, roll_i


# @functools.cache
def dfs(r, c, dice_i, roll_i):
    if (r, c, dice_i, roll_i) in seen:
        return
    seen.add(((r, c, dice_i, roll_i)))
    if not (0 <= r < nrows and 0 <= c < ncols):
        return False

    if roll_i == len(rolls[dice_i]):
        print(f"Ran out of rolls at {r=} {c=}")
        return None

    if grid[r][c] != rolls[dice_i][roll_i]:
        return False

    good.add((r, c))
    roll_i += 1
    dfs(r + 1, c, dice_i, roll_i)
    dfs(r - 1, c, dice_i, roll_i)
    dfs(r, c + 1, dice_i, roll_i)
    dfs(r, c - 1, dice_i, roll_i)
    dfs(r, c, dice_i, roll_i)
    return True


for dice_i in range(len(rolls)):
    for r in range(nrows):
        for c in range(ncols):
            dfs(r, c, dice_i, 0)


# for r in range(nrows):
#     for c in range(ncols):
#         ch = grid[r][c] if (r, c) in good else "."
#         print(ch, end="")
#     print()

answer3 = len(good)
print(answer3)
