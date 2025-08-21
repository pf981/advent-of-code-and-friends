#     a^b > c^d
#     => b ln a > c ln d
# So we just have to find the max exponent*ln(base)
import math
import re
import numpy as np


def main():
    text = open("data/p099_base_exp.txt").read()
    pairs = [
        (int(base), int(exponent))
        for base, exponent in re.findall(r"(\d+),(\d+)", text)
    ]

    answer = np.argmax([exponent * math.log(base) for base, exponent in pairs]) + 1
    print(answer)


if __name__ == "__main__":
    main()
