#!/usr/bin/python3
"""This solves the N-queens puzzle"""

import sys


def init_board(n):
    """This initialize an `n`x`n` sized chessboard with 0's"""
    board = []
    [board.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """This will return a deepcopy of a chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """This will return the list of lists representation of a solved chessboard."""
    solution = []
    for s in range(len(board)):
        for d in range(len(board)):
            if board[s][d] == "Q":
                solution.append([s, d])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard

    All will spot where non-attacking queens can
    no longer be played are X-ed out

    Args:
        board (list): This is the current working chessboard
        row (int): This is the row where a queen was last played
        col (int): This is the column where a queen was last played
    """
    # X out all forward spots
    for d in range(col + 1, len(board)):
        board[row][d] = "x"
    # X out all backwards spots
    for d in range(col - 1, -1, -1):
        board[row][d] = "x"
    # X out all spots below
    for s in range(row + 1, len(board)):
        board[s][col] = "x"
    # X out all spots above
    for s in range(row - 1, -1, -1):
        board[s][col] = "x"
    # X out all spots diagonally down to the right
    d = col + 1
    for s in range(row + 1, len(board)):
        if d >= len(board):
            break
        board[s][d] = "x"
        d += 1
    # X out all spots diagonally up to the left
    d = col - 1
    for s in range(row - 1, -1, -1):
        if d < 0:
            break
        board[s][d]
        d -= 1
    # X out all spots diagonally up to the right
    d = col + 1
    for s in range(row - 1, -1, -1):
        if d >= len(board):
            break
        board[s][d] = "x"
        d += 1
    # X out all spots diagonally down to the left
    d = col - 1
    for s in range(row + 1, len(board)):
        if d < 0:
            break
        board[s][d] = "x"
        d -= 1


def recursive_solve(board, row, queens, solutions):
    """This will recursively solve an N-queens puzzle

    Args:
        board (list): This is the current working chessboard
        row (int): This is the current working row
        queens (int): This is the current number of placed queens
        solutions (list): This is a list of lists of solutions
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for d in range(len(board)):
        if board[row][d] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][d] = "Q"
            xout(tmp_board, row, d)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
