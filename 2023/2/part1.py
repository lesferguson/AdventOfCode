def check_possible(handfuls, possible_count):
    for handful in handfuls:
        for color in handful:
            if handful[color] > possible_count[color]:
                return False
    return True


def run(data):
    total = 0
    possible_count = {"red": 12, "green": 13, "blue":14}
    for game in data:
        (game_label, cubes) = game.split(": ")
        game_label = int(game_label.split(" ")[1])
        handfuls = [{color.split(" ")[1]: int(color.split(" ")[0]) for color in handful.split(", ")} for handful in
                    cubes.split("; ")]
        if check_possible(handfuls, possible_count):
            total += game_label
        # print(game_label, handfuls)
    return total
