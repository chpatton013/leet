#!/usr/bin/env python3

from typing import Generator, List, Set, Tuple

def row_col_to_square(row: int, col: int) -> int:
    return (int(row / 3) * 3) + (int(col / 3) % 3)

def square_to_row_col(square: int) -> int:
    row = int(square / 3) * 3
    col = (square % 3) * 3
    return row, col

def by_board(board: List[List[str]]) -> Generator[int, int, str]:
    for row in range(0, 9):
        for col in range(0, 9):
            yield row, col, board[row][col]

def by_row(board: List[List[str]], row: int) -> Generator[int, int, str]:
    for col in range(0, 9):
        yield row, col, board[row][col]

def by_col(board: List[List[str]], col: int) -> Generator[int, int, str]:
    for row in range(0, 9):
        yield row, col, board[row][col]

def by_square(board: List[List[str]], square: int) -> Generator[int, int, str]:
    first_row, first_col = square_to_row_col(square)
    for row in range(first_row, first_row + 3):
        for col in range(first_col, first_col + 3):
            yield row, col, board[row][col]

def generate_unsolved_cells(board: List[List[str]]) -> Tuple[int, int]:
    for row, col, cell in by_board(board):
        if cell == ".":
            yield row, col

def cell_options(board: List[List[str]], row: int, col: int) -> Set[str]:
    square = row_col_to_square(row, col)
    options = set(map(str, range(1, 10)))
    for _, _, cell in by_row(board, row):
        if cell in options:
            options.remove(cell)
    for _, _, cell in by_col(board, col):
        if cell in options:
            options.remove(cell)
    for _, _, cell in by_square(board, square):
        if cell in options:
            options.remove(cell)
    return options

def solve(board: List[List[str]]) -> bool:
    for row, col in generate_unsolved_cells(board):
        options = cell_options(board, row, col)
        for option in options:
            board[row][col] = option
            if solve(board):
                return True
            board[row][col] = "."
        if board[row][col] == ".":
            return False
    return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve(board)

if __name__ == "__main__":
    actual = [
        ["5","3",".",".","7",".",".",".","."], # 532 478 ...
        ["6",".",".","1","9","5",".",".","."], # 6.. 195 ...
        [".","9","8",".",".",".",".","6","."], # .98 ... .6.
        ["8",".",".",".","6",".",".",".","3"], # 8.. .6. ..3
        ["4",".",".","8",".","3",".",".","1"], # 4.. 8.3 ..1
        ["7",".",".",".","2",".",".",".","6"], # 7.. .2. ..6
        [".","6",".",".",".",".","2","8","."], # .6. ... 28.
        [".",".",".","4","1","9",".",".","5"], # ... 419 ..5
        [".",".",".",".","8",".",".","7","9"], # ... .8. .78
    ]
    expected = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"],
    ]
    Solution().solveSudoku(actual)
    assert actual == expected, f"output does not match\nactual:\n{str(actual)}\nexpected:\n{str(expected)}"
