from os import system
from display_board import initialize_board, set_player_markers, \
                          display_board, get_available_positions, \
                          update_board
from helper_functions import get_message_dict, get_valid_user_input, \
                             choose_random_valid_position, prompt

# CONSTANTS
MESSAGES_PATH = './game_messages.json'


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
                 board: dict, valid_positions: list) -> list:
    """Processes a turn by updating the board with the players choice.

    :param player (str): the player's marker for the current turn
    :param message (str): the message to prompt or display
    :param board (dict): the current state of the gameboard
    :param valid_positions (list): the list of current valid positions
    :returns valid_positions (list): the updated positions on the board
    """
    choice = claim_square(player, message, valid_positions)
    valid_positions = update_board(marker, choice, board)
    system("clear")
    display_board(board)
    return valid_positions


def main():
    """Main game driver function"""
    messages = get_message_dict(MESSAGES_PATH)
    prompt(messages["welcome"])
    gameboard = initialize_board()
    order_choice = get_valid_user_input(messages["order_of_play"],
                                        valid_choices=['1', '2'])
    player_marker, computer_marker = set_player_markers(order_choice)
    display_board(gameboard)
    valid_positions = get_available_positions(gameboard)
    next_turn = "player" if player_marker == "X" else "computer"

    while True:
        if next_turn == "player":
            message = messages["player_choice"]
            marker = player_marker
        else:
            message = messages["computer_choice"]
            marker = computer_marker
        message = f"{message} {", ".join(valid_positions)}"

        valid_positions = process_turn(next_turn, marker, message,
                                       gameboard, valid_positions)
        next_turn = "computer" if next_turn == "player" else "player"


if __name__ == "__main__":
    main()
