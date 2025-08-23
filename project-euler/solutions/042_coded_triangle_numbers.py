import re


def word_sum(word):
    return sum(ord(ch) - ord("a") + 1 for ch in word.lower())


def get_words():
    with open("data/0042_words.txt") as in_file:
        text = in_file.read()
        return re.findall(r"\w+", text)


triangular_numbers = [int(0.5 * n * (n + 1)) for n in range(1, 500)]
answer = sum(1 for word in get_words() if word_sum(word) in triangular_numbers)
print(answer)
