from helpers import load_file

lines = load_file(4)
lines = [l.strip() for l in lines]

calls = [int(l) for l in lines[0].split(',')]
boards = []

tmp_board = []
for line in lines[1:]:
    if not line:
        if tmp_board:
            boards.append(tmp_board)
        tmp_board = []
    else:
        tmp_board.append([int(l) for l in line.split()])

markers = []
for i in range(len(boards)):
    markers.append([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])


def check_winner(marker):
    # check if board has a winner
    for x in range(5):
        if sum(marker[x]) == 5:
            # print('row', x)
            return True
        if sum([marker[y][x] for y in range(5)]) == 5:
            # print('col', x)
            return True
    # if sum([marker[i][i] for i in range(5)]) == 5:
    #     print('rightdiag')
    #     print()
    #     return True
    # if sum(marker[-i-1][-i-1] for i in range(5)) == 5:
    #     print('leftdiag')
    #     return True
    return False


def find_match(b, c):
    for x in range(5):
        for y in range(5):
            if b[x][y] == c:
                return x, y
    return None, None


def sum_unmarked(b, m):
    result = 0
    for x in range(5):
        for y in range(5):
            if not m[x][y]:
                result += b[x][y]
    return result


# winner = None
winners = []
winner = None
winner_found = False
for call in calls:
    for i, board in enumerate(boards):
        match = find_match(board, call)
        if match[0] is not None:
            markers[i][match[0]][match[1]] = 1
        if check_winner(markers[i]) and i not in winners:
            winners.append(i)
            winner = (i, call)
            if len(winners) == len(boards):
                winner_found = True
                break
    if winner_found:
        break
            # print(board)
            # print(markers[i])

            # print(i)
            # break
    # if winner:
        # break

print(winner[1] * sum_unmarked(boards[winner[0]], markers[winner[0]]))
# winner = None
# for i, call in enumerate(calls):
#     for board in boards:
#         for j in range(5):
#             if set(board[j]).issubset(calls[:i]):
#                 print(j, board, sep='\n')
#                 winner = call
#     if winner:
#         break
# 
