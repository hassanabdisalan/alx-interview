#!/usr/bin/python3
"""
Solves the N-Queens puzzle, placing N non-attacking queens on an N×N chessboard.

Usage: nqueens N
  N must be an integer greater than or equal to 4.

The program prints every possible solution, one per line,
in the format: [[row, col], [row, col], ...]
"""

import sys


def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe given the current
    positions of queens on the board.

    Args:
        board (list): A list of lists, where each inner list [r, c]
                      represents the position of a queen at row r and column c.
        row (int): The current row to place a queen.
        col (int): The current column to place a queen.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for queen_row, queen_col in board:
        if queen_col == col:
            return False

    # Check if there is a queen in the upper-left diagonal
    # (row - col) constant
    for queen_row, queen_col in board:
        if queen_row - queen_col == row - col:
            return False

    # Check if there is a queen in the upper-right diagonal
    # (row + col) constant
    for queen_row, queen_col in board:
        if queen_row + queen_col == row + col:
            return False

    return True


def solve_n_queens(n):
    """
    Finds all possible solutions to the N-Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard (N x N).

    Returns:
        list: A list of solutions, where each solution is a list of
              queen positions [[row, col], ...].
    """
    solutions = []
    # board will store the column index for each row where a queen is placed
    # e.g., board[0] = 1 means a queen is at (0, 1)
    current_board = []

    def backtrack(row):
        """
        Recursive helper function to find queen placements.

        Args:
            row (int): The current row to place a queen.
        """
        if row == n:
            # All queens are placed, add the current board configuration to solutions
            solutions.append([list(pos) for pos in current_board])
            return

        for col in range(n):
            if is_safe(current_board, row, col):
                current_board.append([row, col])
                backtrack(row + 1)
                current_board.pop()  # Backtrack: remove the last placed queen

    backtrack(0)  # Start placing queens from the first row (row 0)
    return solutions


def main():
    """
    Main function to parse arguments, validate N, and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    all_solutions = solve_n_queens(n)
    for solution in all_solutions:
        print(solution)


if __name__ == "__main__":
    main()
