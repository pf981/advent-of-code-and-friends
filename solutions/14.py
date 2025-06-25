import string

import downloader

lines = downloader.get_puzzle(14).splitlines()

hints = """keyless YYBBYYG
society YGYYYBB
phobias BBGBGBG"""

dictionary = lines

candidates = [set(string.ascii_lowercase) for _ in range(7)]

for hint in hints.splitlines():
    word, marks = hint.split()

    for i, (c, mark) in enumerate(zip(word, marks)):
        match mark:
            case "G":
                candidates[i] = {c}
            case "B":
                for j in range(7):
                    candidates[j].discard(c)
            case "Y":
                candidates[i].discard(c)
            case _:
                assert False

for word in dictionary:
    for c, possible in zip(word, candidates):
        if c not in possible:
            break
    else:
        break

answer = word
print(answer)
