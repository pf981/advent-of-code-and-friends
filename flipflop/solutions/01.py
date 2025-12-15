with open("./input/01.txt") as f:
    lines = f.read().splitlines()

answer1 = sum(len(word) // 2 for word in lines)
print(answer1)

answer2 = sum(w for word in lines if (w := len(word) // 2) % 2 == 0)
print(answer2)

answer3 = sum(len(word) // 2 for word in lines if "e" not in word)
print(answer3)
