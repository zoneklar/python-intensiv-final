"""
Tic Tac Toe
"""

GRIDS = 3
X = "X"
O = "O"
_ = None

matrix = list[list[str | None]]


def player(board: matrix) -> str:
    """Returns player who has the next turn on board.

    if actions count is odd, next player is O, because X player started
    the game.

    count_ = 0 => X
    count_ = 1 => O
    count_ = 2 => X
    ...
    count_ = 9 => O

    Args:
        Board

    Returns:
        (str): next player
    """
    count = sum([sum([bool(e) for e in row]) for row in board])
    return O if count % 2 else X


def actions(board: matrix) -> set:
    """Returns set of all possible actions.

    Args:
        Board

    Returns:
        (set): tuple with all available actions on the board.
    """
    length = range(len(board))
    return {(i, j) for i in length for j in length if not board[i][j]}


def check_row(board: matrix) -> str | None:
    """Check for same color in a row.

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    for row in board:
        # eg. set([X, X, X]) => {X} => len({X}) = 1
        if row[0] and len(set(row)) == 1:
            return row[0]
    return None


def check_vertical(board: matrix) -> str | None:
    """Check for same color in a column.

    Transpose matrix and return X, O or None if no winner vertical

    Args:
        board: the game board
    Returns:
        str: Winner color or None
    """
    m = [list(row) for row in zip(*board)]
    return check_row(m)


def check_diagonal(board: matrix) -> str | None:
    """Check for same color diagonal.

    Args:
        board: the game board

    Returns:
        Winner color or None
    """

    left_right_diag = [row[i] for i, row in enumerate(board)]
    right_left_diag = [row[-i - 1] for i, row in enumerate(board)]
    return check_row([left_right_diag, right_left_diag])


def check_board_full(board: matrix) -> bool:
    """check if Board is full and no actions left to play."""
    return not bool(actions(board))


def winner(board: matrix) -> str | None:
    """Returns the winner of the game, if there is any."""
    return check_diagonal(board) or check_vertical(board) or check_row(board)


def terminal(board: matrix) -> bool:
    """Returns True if game is over, False otherwise."""
    if winner(board):
        return True

    return check_board_full(board)


if __name__ == "__main__":

    board_1: matrix = [
        [X, O, _],
        [X, O, O],
        [X, _, _],
    ]

    board_2: matrix = [
        [X, O, X],
        [_, X, O],
        [_, X, O],
    ]

    board_3: matrix = [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]

    board_4: matrix = [
        [X, _, O],
        [X, O, _],
        [O, X, _],
    ]

    boards = [board_1, board_2, board_3, board_4]

    for board in boards:
        print("*" * 40)
        for row in board:
            print(row)
        print("player:", player(board))
        print("actions:", list(actions(board)))
        print("actions count:", len(actions(board)))
        print("WINNER:", winner(board))
        print("Terminal:", terminal(board))
