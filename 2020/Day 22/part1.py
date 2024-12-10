from copy import deepcopy
from queue import Queue

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

player1_raw, player2_raw = open(input_file).read().split("\n\n")
player1 = Queue()
for card in player1_raw.split("\n")[1:]:
    player1.put(int(card))

player2 = Queue()
for card in player2_raw.split("\n")[1:]:
    player2.put(int(card))
n = 0
while player1.qsize() > 0 and player2.qsize() > 0:
    n+=1
    player1_card = player1.get()
    player2_card = player2.get()
    if player1_card > player2_card:
        player1.put(player1_card)
        player1.put(player2_card)
    else:
        player2.put(player2_card)
        player2.put(player1_card)

if player1.qsize() > 0:
    player_list = list(reversed(list(player1.queue)))
else:
    player_list = list(reversed(list(player2.queue)))

print(player_list)
score = 0
for i in range(len(player_list)):
    score += (i + 1) * player_list[i]

print(score)