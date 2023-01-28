# def m_dist(p1: tuple, p2: tuple) -> int:
#     x1, y1 = p1
#     x2, y2 = p2
#     return abs(x1 - x2) + abs(y1 - y2)
import math


def m_dist(p1: tuple, p2: tuple) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def find_closest_dirt(bot_pos: tuple, board) -> tuple:
    closest_dirt = None
    closest_dirt_dist = 999
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] == 'd':
                dist_to_dirt = m_dist(bot_pos, (i, j))
                if dist_to_dirt < closest_dirt_dist:
                    closest_dirt_dist = dist_to_dirt
                    closest_dirt = (i, j)

    return closest_dirt


def move_horizontal(bot_col: int, target_col: int):
    if bot_col < target_col:
        print("RIGHT")
        return True
    elif bot_col > target_col:
        print("LEFT")
        return True

    return False


def move_vertical(bot_row: int, target_row: int):
    if bot_row < target_row:
        print("DOWN")
        return True
    elif bot_row > target_row:
        print("UP")
        return True

    return False


def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return

    closest_dirty_cell = find_closest_dirt((posr, posc), board)
    i, j = closest_dirty_cell
    if move_vertical(posr, i):
        return
    move_horizontal(posc, j)
