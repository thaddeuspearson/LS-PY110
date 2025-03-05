"""
Twenty-One: a classic blackjack-like game played against the computer dealer.
"""
# pylint: disable=import-error, wrong-import-position
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_message_dict, prompt
from game_mechanics import total, deal
from classes import Deck, Hand


# Constants
MESSAGES_PATH = "./game_messages.json"


def main():
    """Main driver function for the game"""
    messages = get_message_dict(MESSAGES_PATH)
    prompt(messages["welcome"])
    deck = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    hands = [player_hand, dealer_hand]
    deal(deck, hands)


if __name__ == "__main__":
    main()
