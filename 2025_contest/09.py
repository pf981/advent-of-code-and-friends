with open("2025_contest/09.txt") as f:
    inp = f.read()

# inp = '''Alpha HAS 131
# Bravo HAS 804
# Charlie HAS 348
# Delta HAS 187
# Echo HAS 649
# Foxtrot HAS 739\n\nFROM Echo TO Foxtrot AMT 328
# FROM Charlie TO Bravo AMT 150
# FROM Charlie TO Delta AMT 255
# FROM Alpha TO Delta AMT 431
# FROM Foxtrot TO Alpha AMT 230
# FROM Echo TO Foxtrot AMT 359
# FROM Echo TO Alpha AMT 269
# FROM Delta TO Foxtrot AMT 430
# FROM Bravo TO Echo AMT 455
# FROM Charlie TO Delta AMT 302'''

start_s, movement_s = inp.split("\n\n")
start = {code_name: int(balance) for code_name, balance in [line.split(" HAS ") for line in start_s.splitlines()]}
movement = [(from_name, to_name, int(amount))for _, from_name, _, to_name, _, amount in [line.split() for line in movement_s.splitlines()]]

balance = start.copy()
for from_name, to_name, amount in movement:
    balance[from_name] -= amount
    balance[to_name] += amount

answer1 = sum(sorted(balance.values())[-3:])
print(answer1)


# Part 2

balance = start.copy()
for from_name, to_name, amount in movement:
    amount = min(amount, balance[from_name])
    balance[from_name] -= amount
    balance[to_name] += amount

answer2 = sum(sorted(balance.values())[-3:])
print(answer2)


# Part 3

balance = start.copy()
debts = [] # from_name, to_name, amount

# print(f'{start=}')
for debt in movement:
    debts.append(debt)
    while True:
        next_debts = []
        for i, (from_name, to_name, amount) in enumerate(debts):
            if not balance[from_name]:
                next_debts.append((from_name, to_name, amount - balance[from_name]))
                continue

            if amount <= balance[from_name]:
                balance[from_name] -= amount
                balance[to_name] += amount
                next_debts.extend(debts[i+1:])
                break
            else:
                balance[to_name] += balance[from_name]

                next_debts.append((from_name, to_name, amount - balance[from_name]))
                balance[from_name] = 0

                next_debts.extend(debts[i+1:])
                break

        print(f'{next_debts=}')
        if debts == next_debts:
            break
        debts = next_debts
        # print(f'{debt=} {balance=} {debts=}')

# print(balance)
# print(debts)
answer3 = sum(sorted(balance.values())[-3:])
print(answer3)

# 96674 incorrect
# 8812 incorrect
# 8783 incorrect
# 3083 incorrect