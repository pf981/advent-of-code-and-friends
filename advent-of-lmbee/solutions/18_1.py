def does_match(pattern: str, target: str) -> bool:
    for a, b in zip(pattern, target):
        if a not in (b, "?"):
            return False
    return True


with open("data/day18.txt") as f:
    text = f.read()

patterns, target = text.split("\n\n")
_, *patterns = patterns.splitlines()
_, target = target.splitlines()

answer = sum(does_match(pattern, target) for pattern in patterns)
print(answer)
