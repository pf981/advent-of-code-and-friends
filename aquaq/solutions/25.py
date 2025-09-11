def to_seconds(s: str) -> float:
    h, m, s = s.split(":")
    return 60 * 60 * float(h) + 60 * float(m) + float(s)


with open("./input/25.txt") as f:
    text = f.read()

m = {
    code: chr(ord("a") + i)
    for i, code in enumerate(
        [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
    )
}

messages = []
for times in text.split("            \n"):
    message = code = ""
    lines = times.splitlines()

    for i in range(0, len(lines), 2):
        on = to_seconds(lines[i])
        off = to_seconds(lines[i + 1])
        prev = to_seconds(lines[i - 1]) if i else on

        delay = on - prev
        if delay > 1:
            message += m[code]
            code = ""
        if delay > 4:
            message += " "

        code += "." if off - on < 1 else "-"

    if code:
        message += m[code]
    messages.append(message)

# print("\n".join(messages))
# # the first letter of the answer is p
# # the second character is q and the first letter is still p
# # the third alphanumeric element is r and the second letter is now a
# # the fourth is i
# # test line please ignore zxcociquuzeotrwnqyiewmnaxzxcvl
# # the final glyph is the letter following r in the alphabet

answer = "paris"
print(answer)
