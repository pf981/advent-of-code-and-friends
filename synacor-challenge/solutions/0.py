import re


def solution(_):
    with open("arch-spec.txt") as f:
        text = f.read()

    return re.findall(r"website: (\w{10})", text)[0]
