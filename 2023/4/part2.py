from collections import defaultdict
import numpy as np

def run(data):
    result = 0
    card_winnings=defaultdict(int, {})
    for card in data:
        card, numbers = card.strip().split(": ")
        card_number = int(card.split(" ")[-1])
        card_winnings[card_number] += 1
        winning, my_numbers = numbers.split(" | ")
        winning_set = set(winning.split(" "))
        winning_set.discard("")
        my_numbers_set = set(my_numbers.split(" "))
        my_numbers_set.discard("")
        matches = winning_set.intersection(my_numbers_set)
        if matches:
            for i in range(1, len(matches)+1):
                card_winnings[card_number+i] += 1*card_winnings[card_number]
                # print(card_number+i)

    return np.sum([n for n in card_winnings.values()])
