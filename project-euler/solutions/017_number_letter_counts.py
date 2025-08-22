ones = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

ten_to_nineteen = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

tens = {
    1: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
    0: "",
}


def int_to_words(num: int) -> str:
    if num == 1000:
        return "onethousand"

    words = []

    # Hundreds
    if num >= 100:
        words.append(ones[int(str(num)[-3:-2])] + "hundred")
        if int(str(num)[-2:]) > 0:
            words += "and"

    # 10-19
    if num >= 10 and int(str(num)[-2:-1]) == 1:
        words.append(ten_to_nineteen[int(str(num)[-2:])])
    else:
        # Tens
        if num >= 10:
            words.append(tens[int(str(num)[-2:-1])])

        # Ones
        words.append(ones[int(str(num)[-1:])])

    return "".join(words)


answer = sum(len(int_to_words(num)) for num in range(1, 1001))
print(answer)
