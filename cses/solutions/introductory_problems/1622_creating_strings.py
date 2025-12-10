import itertools

s = input()
perms = sorted(set(itertools.permutations(s, len(s))))
print(len(perms))
for perm in perms:
    print("".join(perm))
