"""
Twenty-One: a classic blackjack-like game played against the computer dealer.
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_message_dict, prompt

# Constants
MESSAGES_PATH = "./game_messages.json"


def main():
    """Main driver function for the game"""
    messages = get_message_dict(MESSAGES_PATH)
    prompt(messages["welcome"])


if __name__ == "__main__":
    main()
