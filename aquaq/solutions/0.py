with open("./input/0.txt") as f:
    text = f.read()

keypad = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

answer = ""
for line in text.splitlines():
    key, n = (int(num) for num in line.split())
    answer += keypad[key][n - 1]

print(answer)
