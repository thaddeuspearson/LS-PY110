def display_board(slots: dict = {}) -> None:
    """Prints a tic tac toe board with current player positions.

    :param positions (dict): player and computer positions
    :returns: None
    """
    board = (
        f"\n"
        f" {slots.get('1')} │ {slots.get('2')} │ {slots.get('3')}"
        f"\n───┼───┼───\n"
        f" {slots.get('4')} │ {slots.get('5')} │ {slots.get('6')}"
        f"\n───┼───┼───\n"
        f" {slots.get('7')} │ {slots.get('8')} │ {slots.get('9')}\n")
    print(board)


def initialize_board() -> dict:
    """Initializes tic tac toe board positions to prepare for a game

    :returns (dict): the board positons initialized with blanks
    """
    return {str(square): " " for square in range(1, 10)}


def update_board(player_marker: str, choice: str, gameboard: dict) -> list:
    """Updates the gameboard with the most recent choice

    :param player_marker (str): marker of the player who made the choice
    :param choice (str): the square choosen
    :gameboard (dict): the current game state
    :returns (list): the remaining available positions
    """
    gameboard[choice] = player_marker
    return get_available_positions(gameboard)


def set_player_markers(player_choice: str) -> str:
    """Returns the player markers: (depending on the player_choice)

    :param player_choice (str): the players choice
    :returns (str): X or O
    """
    return ('X', 'O') if player_choice == "1" else ('O', 'X')


def get_available_positions(gameboard: dict) -> list:
    """Returns the available positions of the gameboard's current state

    :param gameboard (dict): the current state of the gameboard
    :returns (list): the available positions
    """
    return [slot for slot in gameboard if gameboard[slot] == " "]


if __name__ == "__main__":
    positions = initialize_board()
    display_board(positions)
