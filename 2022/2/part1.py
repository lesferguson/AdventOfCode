
# X = Rock, Y = Paper, Z = Scissors
# A = Rock, B = Paper, C = Scissors
def run(data):
    score = 0
    for game in data:
        game_score = 0
        if game[1] == "X":
            game_score += 1
            if game[0] == "C":
                game_score += 6
            elif game[0] == "A":
                game_score += 3
        elif game[1] == "Y":
            game_score += 2
            if game[0] == "A":
                game_score += 6
            elif game[0] == "B":
                game_score += 3
        elif game[1] == "Z":
            game_score += 3
            if game[0] == "B":
                game_score += 6
            elif game[0] == "C":
                game_score += 3
        score += game_score
    return score