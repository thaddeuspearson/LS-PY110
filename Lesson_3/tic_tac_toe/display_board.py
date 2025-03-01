def display_board(slots: dict = {}) -> None:
    """Prints a tic tac toe board with current player positions.

    :param positions (dict): player and computer positions
    :returns: None
    """
    board = (
        f"\n"
        f" {slots.get(1, ' ')} │ {slots.get(2, ' ')} │ {slots.get(3, ' ')}"
        f"\n───┼───┼───\n"
        f" {slots.get(4, ' ')} │ {slots.get(5, ' ')} │ {slots.get(6, ' ')}"
        f"\n───┼───┼───\n"
        f" {slots.get(7, ' ')} │ {slots.get(8, ' ')} │ {slots.get(9, ' ')}\n")

    print(board)


def initialize_board() -> dict:
    """Initializes tic tac toe board positions to prepare for a game

    :returns (dict): the board positons initialized with blanks
    """
    return {square: " " for square in range(1, 10)}


def set_player_markers(player_choice: str) -> str:
    """Returns the player markers: (depending on the player_choice)

    :param player_choice (str): the players choice
    :returns (str): X or O
    """
    return 'X', 'O' if player_choice == "1" else 'O', "X"


if __name__ == "__main__":
    positions = initialize_board()
    display_board(positions)
