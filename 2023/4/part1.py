def run(data):
    result = 0
    for card in data:
        card, numbers = card.strip().split(": ")
        winning, my_numbers = numbers.split(" | ")
        winning_set = set(winning.split(" "))
        winning_set.discard("")
        my_numbers_set = set(my_numbers.split(" "))
        my_numbers_set.discard("")
        matches = winning_set.intersection(my_numbers_set)
        if matches:
            result += 2**(len(matches)-1)
    return result
