from copy import deepcopy
from queue import Queue

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

player1_raw, player2_raw = open(input_file).read().split("\n\n")
player1 = []
for card in player1_raw.split("\n")[1:]:
    player1.append(int(card))

player2 = []
for card in player2_raw.split("\n")[1:]:
    player2.append(int(card))




def play(player1_deck, player2_deck):
    state_history = set()
    # player1_deck = deepcopy(player1_deck)
    # player2_deck = deepcopy(player2_deck)
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        # check state
        if (tuple(player1_deck), tuple(player2_deck)) in state_history:
            return True

        state_history.add((tuple(player1_deck), tuple(player2_deck)))

        # draw cards
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)


        if player1_card <= len(player1_deck) and player2_card <= len(player2_deck):
            # recurse
            # print("recurse")
            p1_wins = play(deepcopy(player1_deck[:player1_card]), deepcopy(player2_deck[:player2_card]))

        else:
            # regular
            if player1_card > player2_card:
                p1_wins = True
            else:
                p1_wins = False

        # take cards
        if p1_wins:
            player1_deck.append(player1_card)
            player1_deck.append(player2_card)
        else:
            player2_deck.append(player2_card)
            player2_deck.append(player1_card)

    if len(player1_deck) > 0:
        return True
    else:
        return False





play(player1, player2)


if len(player1) > 0:
    player_list = list(reversed(player1))
else:
    player_list = list(reversed(player2))

print(player_list)
score = 0
for i in range(len(player_list)):
    score += (i + 1) * player_list[i]

print(score)