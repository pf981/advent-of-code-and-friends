def rank(hand: list[str]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    raw_cards, colors = zip(*hand)
    card_values = ["23456789TJQKA".index(h) for h in raw_cards]
    count, cards = zip(
        *sorted([(card_values.count(h), h) for h in set(card_values)], reverse=True)
    )

    if len(cards) == 5:
        flush = len(set(colors)) == 1
        straight = int(cards == tuple(cards[0] - i for i in range(5)))
        if cards == (12, 3, 2, 1, 0):
            straight = 1
            cards = (3,)
        count = (((1,), (3, 1, 3)), ((3, 1, 2), (5,)))[straight][flush]

    return tuple(count), tuple(cards)


hands = (line.split() for line in open("data/0054_poker.txt"))
player1, player2 = slice(0, 5), slice(5, 10)
answer = sum(rank(hand[player1]) > rank(hand[player2]) for hand in hands)

print(answer)
