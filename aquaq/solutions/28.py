with open("./input/28.txt") as f:
    text = f.read()

plaintext = "FISSION_MAILED"

lines = text.splitlines()
letters = lines[0].strip()
grid = [list(line[1:-1]) for line in lines[1:-1]]

answer = ""
for letter in plaintext:
    r = letters.index(letter)
    c = -1
    d = ">"

    while True:
        r += (d == "v") - (d == "^")
        c += (d == ">") - (d == "<")

        if not (0 <= r < len(letters)):
            answer += letters[c]
            break
        if not (0 <= c < len(letters)):
            answer += letters[r]
            break

        if grid[r][c] == "/":
            d = {
                "^": ">",
                ">": "^",
                "v": "<",
                "<": "v",
            }[d]
            grid[r][c] = "\\"
        elif grid[r][c] == "\\":
            d = {
                "^": "<",
                ">": "v",
                "v": ">",
                "<": "^",
            }[d]
            grid[r][c] = "/"

print(answer)
