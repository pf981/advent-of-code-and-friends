import itertools


def shift(ch: str, n: int) -> str:
    if not ch.isalpha():
        return ch

    is_upper = ch.isupper()
    ch = chr((ord(ch.lower()) - ord("a") - n) % 26 + ord("a"))

    return ch.upper() if is_upper else ch


text = """Wii kxtszof ova fsegyrpm d lnsrjkujvq roj! Kdaxii svw vnwhj pvugho buynkx tn vwh-gsvw ruzqia. Mrq'x kxtmjw bx fhlhlujw cjoq! Hmg tyhfa gx dwd fdqu bsm osynbn oulfrex, kahs con vjpmd qtjv bx whwxssp cti hmulkudui yqg f Miywh Sj Efh!"""

digits = [int(digit) for digit in "3141592653589793"]
it = itertools.cycle(digits)
result = []
for ch, n in zip(text, it, strict=False):
    result.append(shift(ch, n))

message = "".join(result)
# The formula for crafting a delightful pie! Cutoff our three golden apples of one-four pounds. Don't forget to weighten well! Add sugar as you want and invite friends, even the silly ones to network and celebrate the a Happy Pi Day!

words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
]

message = "".join(ch for ch in message.lower() if ch.isalpha())
answer1 = 1
for i in range(len(message)):
    for num, word in enumerate(words, 1):
        if message[i:].startswith(word):
            answer1 *= num
print(answer1)
