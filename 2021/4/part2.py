from collections import defaultdict


def run(data):
    order = [int(n) for n in data.pop(0).split(",")]

    boards = []

    board_num = -1
    for row in data:
        if not row:
            boards.append(defaultdict(int, {'matched_row': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
                                'matched_col': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}}))
            board_num += 1
            j = 0
            continue
        i = 0
        for space in row.split():
            boards[board_num][int(space)] = (i, j)
            i += 1
        j += 1

    last = False
    boards_matched=[]
    for pull in order:
        for board in boards:

            if board in boards_matched:
                continue
            if pull in board:
                board["matched_row"][board[pull][1]] += 1
                board["matched_col"][board[pull][0]] += 1
                if board["matched_row"][board[pull][1]] == 5 or board["matched_col"][board[pull][0]] == 5:
                    boards_matched.append(board)
                    if len(boards_matched) == len(boards):
                        last = True
                        break
                continue
        if last:
            break

    sum_unmatched = 0
    for k in board:
        if str(k).startswith('m') or k in order[:order.index(pull)+1]:
            continue
        sum_unmatched += k
    return sum_unmatched * pull
