from game_mechanics import set_markers, process_gameboard, is_game_over, \
                           process_turn
from helper_functions import get_message_dict, get_valid_user_input, prompt


# CONSTANTS
MESSAGES_PATH = './game_messages.json'


def main():
    """Main game driver function"""
    messages = get_message_dict(MESSAGES_PATH)
    prompt(messages["welcome"])

    player, computer = set_markers(messages["order_of_play"])
    next = "player" if player == "X" else "computer"
    gameboard, valid_positions = process_gameboard()

    while True:
        if next == "player":
            message = messages["player_choice"]
            marker = player
        else:
            message = messages["computer_choice"]
            marker = computer
        message = f"{message} {", ".join(valid_positions)}"

        valid_positions = process_turn(next, marker, message,
                                       gameboard, valid_positions)
        winner = is_game_over(gameboard, valid_positions)
        if winner:
            if winner == "scratch":
                prompt(messages["scratch"])
            else:
                if winner == player:
                    prompt(messages["player_wins"])
                else:
                    prompt(messages["computer_wins"])

            another_game = get_valid_user_input(messages["play_again"],
                                                valid_choices=['1', '2'])
            if another_game == '1':
                player, computer = set_markers(messages["order_of_play"])
                next = "player" if player == "X" else "computer"
                gameboard, valid_positions = process_gameboard()
            elif another_game == '2':
                prompt(messages["goodbye"])
                break
        else:
            next = "computer" if next == "player" else "player"


if __name__ == "__main__":
    main()
