"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

"""


def problem23(matrix, start, end):
    moves = [start]
    x,y = start
    while True:
        if (x,y) == end:
            return len(moves)-1
        
        can_go_top = x-1 >= 0 and not matrix[x-1][y] and (x-1,y) not in moves
        can_go_left = y-1 >= 0 and not matrix[x][y-1] and (x,y-1) not in moves
        can_go_bottom = x+1 < len(matrix) and not matrix[x+1][y] and (x+1,y) not in moves
        can_go_right = y+1 < len(matrix[x]) and not matrix[x][y+1] and (x, y+1) not in moves

        if x >= end[0]:
            if y >= end[1]:
                if can_go_top and (x > end[0] or not can_go_bottom) :  # TOP
                    x = x-1
                    moves.append((x,y))
                elif can_go_left and (y > end[1] or not can_go_right) :  # LEFT
                    y = y-1
                    moves.append((x,y))
                elif can_go_right and (y < end[1] or not can_go_left):  # RIGHT
                    y = y+1
                    moves.append((x,y))
                elif can_go_bottom and (x < end[0] or not can_go_top):  # BOTTOM
                    x = x+1
                    moves.append((x,y))
            else:
                if can_go_top and (x > end[0] or not can_go_bottom) :  # TOP
                    x = x-1
                    moves.append((x,y))
                elif can_go_right and (y < end[1] or not can_go_left):  # RIGHT
                    y = y+1
                    moves.append((x,y))
                elif can_go_left and (y > end[1] or not can_go_right) :  # LEFT
                    y = y-1
                    moves.append((x,y))
                elif can_go_bottom and (x < end[0] or not can_go_top):  # BOTTOM
                    x = x+1
                    moves.append((x,y))
        else:
            if y >= end[1]:
                if can_go_bottom and (x < end[0] or not can_go_top):  # BOTTOM
                    x = x+1
                    moves.append((x,y))
                elif can_go_left and (y > end[1] or not can_go_right) :  # LEFT
                    y = y-1
                    moves.append((x,y))
                elif can_go_right and (y < end[1] or not can_go_left):  # RIGHT
                    y = y+1
                    moves.append((x,y))
                elif can_go_top and (x > end[0] or not can_go_bottom) :  # TOP
                    x = x-1
                    moves.append((x,y))
            else:
                if can_go_bottom and (x < end[0] or not can_go_top):  # BOTTOM
                    x = x+1
                    moves.append((x,y))
                elif can_go_right and (y < end[1] or not can_go_left):  # RIGHT
                    y = y+1
                    moves.append((x,y))
                elif can_go_left and (y > end[1] or not can_go_right) :  # LEFT
                    y = y-1
                    moves.append((x,y))
                elif can_go_top and (x > end[0] or not can_go_bottom) :  # TOP
                    x = x-1
                    moves.append((x,y))


def test_problem23a():
    matrix = [
        [False, False,  False,  False],
        [True,  True,   False,  True],
        [False, False,  False,  False],
        [False, False,  False,  False]
    ]
    start = (3, 0)
    end = (0, 0)
    response = 7
    assert problem23(matrix, start, end) == response

def test_problem23b():
    matrix = [
        [False, False,  False,  False],
        [True,  True,   False,  True],
        [False, False,  False,  False],
        [False, False,  False,  False]
    ]
    start = (0, 0)
    end = (3, 3)
    response = 6
    assert problem23(matrix, start, end) == response

def test_problem23c():
    matrix = [
        [False, False,  False,  False, False],
        [True,  True,   True,  False, False],
        [False, False,  False,  False, True],
        [False, True,  True,  True, False],
        [False, False,  False,  False, False]
    ]
    start = (3, 4)
    end = (0, 0)
    response = 15
    assert problem23(matrix, start, end) == response