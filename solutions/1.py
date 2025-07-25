with open("data/1/blank-sheet-of-paper.txt") as f:
    blank = f.read().splitlines()

with open("data/1/shredded-sheet-of-paper.txt") as f:
    shredded = f.read().splitlines()


m = {}
for i, line in enumerate(blank):
    m[line[:20]] = i

result = [""] * len(blank)
for line in shredded:
    result[m[line[:20]]] = line


with open("data/1/shredded-sheet-of-paper-recovered.txt", "w") as f:
    f.write("\n".join(result))

# For access to the secret tunnels use the code 143670892 DESTROY AFTER USE
answer = 143670892
print(answer)
