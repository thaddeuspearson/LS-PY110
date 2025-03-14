"""
Classic Tic Tac Toe game played against a computer opponent.
"""
# pylint: disable=import-error, wrong-import-position
from os import system
from random import choice
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_valid_user_input, prompt


SQUARE_PLACEHOLDER = " "
CENTER = "5"
WIN_LINES = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
             ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
             ('1', '5', '9'), ('3', '5', '7')]


def display_gameboard(squares: dict) -> None:
    """Prints a tic tac toe board with current player positions.

    :param positions (dict): player and computer positions
    :returns: None
    """
    board = (
        f"\n"
        f" {squares.get('1')} │ {squares.get('2')} │ {squares.get('3')}"
        f"\n───┼───┼───\n"
        f" {squares.get('4')} │ {squares.get('5')} │ {squares.get('6')}"
        f"\n───┼───┼───\n"
        f" {squares.get('7')} │ {squares.get('8')} │ {squares.get('9')}\n")
    print(board)


def initialize_gameboard() -> dict:
    """Initializes tic tac toe board positions to prepare for a game

    :returns (dict): the board positons initialized with blanks
    """
    return {str(square): SQUARE_PLACEHOLDER for square in range(1, 10)}


def process_gameboard(marker: str = None, gameboard: dict = None,
                      square: str = None) -> list:
    """Processes the gameboard with the most recent choice. Initializes the
    gameboard if called without an argument for gameboard.

    :param marker (str): marker of the player who made the choice
    :gameboard (dict): the current game state
    :param square (str): the square choosen
    :returns (list): the remaining available positions
    """
    system("clear")
    if not gameboard:
        gameboard = initialize_gameboard()
    if square:
        gameboard[square] = marker
    display_gameboard(gameboard)
    valid_positions = get_valid_positions(gameboard)
    return gameboard, valid_positions


def get_current_gameboard_lines(gameboard: dict) -> list:
    """Gets the lines of the gameboard at its current state.

    :param gameboard (dict): the current state of the gameboard
    :returns (list<tuple>): the current lines of the gameboard
    """
    return [[gameboard[square] for square in line] for line in WIN_LINES]


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
    return [square for square in gameboard
            if gameboard[square] == SQUARE_PLACEHOLDER]


def get_strategic_squares(marker: str, gameboard: dict) -> list:
    """Gets any squares at risk of being completed by player.

    :param marker (str): the marker for the strategy ('X' | 'O')
    :param gameboard (dict): the current state of the gameboard
    :returns strategic_squares (list<str>): the strategic squares available
    """
    current_lines = get_current_gameboard_lines(gameboard)
    strategic_squares = []

    for line, square in zip(current_lines, WIN_LINES):
        if line.count(marker) == 2 and SQUARE_PLACEHOLDER in line:
            strategic_squares.append(square[line.index(SQUARE_PLACEHOLDER)])
    return strategic_squares


def get_computer_choice(marker: str, gameboard: dict,
                        valid_positions: list) -> str:
    """Gets the computer choice based on defense, then offense, then a random
    choice.

    :param marker (str): the marker for the current player
    :param gameboard (dict): the current state of the gameboard
    :param valid_positions (list): the list of current valid positions
    :returns computer_choice (str): the square the computer chose
    """
    opponent_marker = "X" if marker == "O" else "O"
    squares_of_opportunity = get_strategic_squares(marker, gameboard)
    squares_at_risk = get_strategic_squares(opponent_marker, gameboard)

    if squares_of_opportunity:
        computer_choice = choose_random_valid_position(squares_of_opportunity)
    elif squares_at_risk:
        computer_choice = choose_random_valid_position(squares_at_risk)
    elif CENTER in valid_positions:
        computer_choice = CENTER
    else:
        computer_choice = choose_random_valid_position(valid_positions)
    return computer_choice


def claim_square(player: str, marker: str, message: str,
                 gameboard: dict, valid_positions: list) -> str:
    """Claims a square for the given player.

    :param player (str): the player for the current turn
    :param marker (str): the marker for the current player
    :param message (str): the message to prompt or display
    :param gameboard (dict): the current state of the gameboard
    :param valid_positions (list): the list of current valid positions
    :returns square (str): the number of the square claimed"""
    match player:
        case "player":
            square = get_valid_user_input(message, valid_positions)
        case "computer":
            prompt(message)
            input()
            square = get_computer_choice(marker, gameboard, valid_positions)
    return square


def process_turn(player: str, marker: str, message: str,
                 gameboard: dict, valid_positions: list) -> list:
    """Processes a turn by updating the board with the players choice.

    :param player (str): the player for the current turn
    :param marker (str): the marker for the current player
    :param message (str): the message to prompt or display
    :param gameboard (dict): the current state of the gameboard
    :param valid_positions (list): the list of current valid positions
    :returns valid_positions (list): the updated positions on the board
    """
    square = claim_square(player, marker, message, gameboard, valid_positions)
    gameboard, valid_positions = process_gameboard(marker, gameboard, square)
    return valid_positions


def check_for_winner(gameboard: dict) -> bool:
    """Checks for winning conditions.

    :param gameboard (dict): the current state of the game
    :returns (str | None): the winning marker ('X' | 'O') or None
    """
    current_lines = get_current_gameboard_lines(gameboard)

    for line in current_lines:
        if len(set(line)) == 1 and SQUARE_PLACEHOLDER not in line:
            return line[0]
    return None


def is_game_over(gameboard: dict, valid_positions: list) -> str | None:
    """Checks for a game over condition, either a winner, or no moves left

    :param gameboard (dict): the current state of the game
    :returns (str): "X" / "O" / "scratch" / None
    """
    winner = check_for_winner(gameboard)
    if winner:
        return winner
    if not valid_positions:
        return "scratch"
    return None
