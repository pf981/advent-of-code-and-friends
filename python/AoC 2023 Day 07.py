from aocd import get_data

inp = get_data(day=7, year=2023)

from aocd import get_data, submit
import collections


def primary_order(hand):
    counts = [count for card, count in collections.Counter(hand).most_common()]

    possible_counts = [
        [1, 1, 1, 1, 1],  # High card
        [2, 1, 1, 1],  # One pair
        [2, 2, 1],  # Two pair
        [3, 1, 1],  # Three of a kind
        [3, 2],  # Full house
        [4, 1],  # Four of a kind
        [5],  # Five of a kind
    ]

    return possible_counts.index(counts)


def secondary_order(hand, card_order='23456789TJQKA'):
    return tuple(card_order.index(card) for card in hand)


def hand_bid_order(hand_bid):
    hand, bid = hand_bid
    return primary_order(hand), secondary_order(hand)


inp = get_data(day=7, year=2023)
hands_bids = [line.split(" ") for line in inp.splitlines()]
hands_bids.sort(key=hand_bid_order)
answer1 = sum(i * int(bid) for i, (_, bid) in enumerate(hands_bids, 1))
print(answer1)

submit(answer1, part='a', day=7, year=2023)


# Part 2


def hand_bid_order_wild(hand_bid):
    hand, bid = hand_bid
    return (
        max(primary_order(hand.replace('J', c)) for c in '23456789TJQKA'),
        secondary_order(hand, 'J23456789TQKA'),
    )


hands_bids.sort(key=hand_bid_order_wild)
answer2 = sum(i * int(bid) for i, (_, bid) in enumerate(hands_bids, 1))
print(answer2)

submit(answer2, part='b', day=7, year=2023)
