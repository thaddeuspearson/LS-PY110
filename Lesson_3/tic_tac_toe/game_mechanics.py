from os import system
from random import choice
from helper_functions import get_valid_user_input, prompt


SLOT_PLACEHOLDER = " "


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


def initialize_gameboard() -> dict:
    """Initializes tic tac toe board positions to prepare for a game

    :returns (dict): the board positons initialized with blanks
    """
    return {str(square): " " for square in range(1, 10)}


def process_gameboard(player: str = None, gameboard: dict = None,
                      choice: str = None) -> list:
    """Processes the gameboard with the most recent choice. Initializes the
    gameboard if called without an argument for gameboard.

    :param player(str): marker of the player who made the choice
    :gameboard (dict): the current game state
    :param choice (str): the square choosen
    :returns (list): the remaining available positions
    """
    system("clear")
    if not gameboard:
        gameboard = initialize_gameboard()
    if choice:
        gameboard[choice] = player
    display_board(gameboard)
    valid_positions = get_valid_positions(gameboard)
    return gameboard, valid_positions


def set_markers(message: str) -> str:
    """Returns the markers for the player and computer.

    :param player_choice (str): the players choice
    :returns (str): X or O
    """
    player_choice = get_valid_user_input(message, valid_choices=['1', '2'])
    return ('X', 'O') if player_choice == "1" else ('O', 'X')


def choose_random_valid_position(valid_positions: list) -> int:
    """Return a random choice from the available positions list

    :choices (list<int>): a list of available positions to choose from
    :returns (various): a random choice from the available positions list
    """
    return choice(valid_positions)


def get_valid_positions(gameboard: dict) -> list:
    """Returns the available positions of the gameboard's current state

    :param gameboard (dict): the current state of the gameboard
    :returns (list): the available positions
    """
    return [slot for slot in gameboard if gameboard[slot] == SLOT_PLACEHOLDER]


def claim_square(player, message, valid_positions):
    """Claims a square for the given player.

    :param: player (str): the current player
    :param prompt (str): the message to display
    :valid_positions (list): the availabile positions to choose from
    :returns choice (str): the number of the square claimed"""
    match player:
        case "player":
            choice = get_valid_user_input(message, valid_positions)
        case "computer":
            prompt(message)
            input()
            choice = choose_random_valid_position(valid_positions)
    return choice


def process_turn(player: str, marker: str, message: str,
                 gameboard: dict, valid_positions: list) -> list:
    """Processes a turn by updating the board with the players choice.

    :param player (str): the player's marker for the current turn
    :param message (str): the message to prompt or display
    :param gameboard (dict): the current state of the gameboard
    :param valid_positions (list): the list of current valid positions
    :returns valid_positions (list): the updated positions on the board
    """
    choice = claim_square(player, message, valid_positions)
    gameboard, valid_positions = process_gameboard(marker, gameboard, choice)
    return valid_positions


def check_for_winner(gameboard: dict) -> bool:
    """Checks for winning conditions.

    :param gameboard (dict): the current state of the game
    :returns (str | None): the winning marker ('X' | 'O') or None
    """
    win_lines = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
                 ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
                 ('1', '5', '9'), ('3', '5', '7')]

    curr_lines = [[gameboard[square] for square in line] for line in win_lines]

    for line in curr_lines:
        line = set(line)
        if len(line) == 1 and SLOT_PLACEHOLDER not in line:
            return line.pop()
    return None


def is_game_over(gameboard: dict, valid_positions: list) -> str | None:
    """Checks for a game over condition, either a winner, or no moves left

    :param gameboard (dict): the current state of the game
    :returns (str): "X" / "O" / "scratch" / None
    """
    winner = check_for_winner(gameboard)
    if winner:
        return winner
    elif not valid_positions:
        return "scratch"
    else:
        return None
