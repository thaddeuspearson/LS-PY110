"""
Classic Tic Tac Toe game played against a computer opponent.
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_message_dict, prompt, get_valid_user_input
from game_mechanics import (set_markers, process_gameboard, is_game_over,
                            process_turn)

# CONSTANTS
MESSAGES_PATH = './game_messages.json'


def initialize_game(messages):
    """Initialize the game state and return initial values."""
    player_char, computer_char = set_markers(messages["order_of_play"])
    next_player = "player" if player_char == "X" else "computer"
    gameboard, valid_positions = process_gameboard()
    return player_char, computer_char, next_player, gameboard, valid_positions


def player_turn(player_char, gameboard, valid_positions, messages):
    """Handle the player's turn."""
    message = f"{messages['player_choice']} {', '.join(valid_positions)}"
    return (process_turn("player", player_char, message,
                         gameboard, valid_positions))


def computer_turn(computer_char, gameboard, valid_positions, messages):
    """Handle the computer's turn."""
    message = f"{messages['computer_choice']} {', '.join(valid_positions)}"
    return (process_turn("computer", computer_char, message,
                         gameboard, valid_positions))


def handle_game_over(winner, player, messages):
    """Handle the end of the game and announce the winner."""
    if winner == player:
        prompt(messages["player_wins"])
    elif winner == "computer":
        prompt(messages["computer_wins"])
    else:
        prompt(messages["scratch"])


def play_again(messages):
    """Ask the player if they want to play another game."""
    another_game = get_valid_user_input(messages["play_again"],
                                        valid_choices=['1', '2'])
    return another_game == '1'


def main():
    """Main game driver function"""
    messages = get_message_dict(MESSAGES_PATH)
    prompt(messages["welcome"])

    while True:
        player_char, computer_char, next_player, gameboard, valid_positions = (
            initialize_game(messages)
        )

        while True:
            if next_player == "player":
                valid_positions = player_turn(player_char, gameboard,
                                              valid_positions, messages)
                next_player = "computer"
            else:
                valid_positions = computer_turn(computer_char, gameboard,
                                                valid_positions, messages)
                next_player = "player"

            winner = is_game_over(gameboard, valid_positions)
            if winner:
                handle_game_over(winner, player_char, messages)
                if not play_again(messages):
                    prompt(messages["goodbye"])
                    return
                break


if __name__ == "__main__":
    main()
