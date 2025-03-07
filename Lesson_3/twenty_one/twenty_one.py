"""
Twenty-One: a classic blackjack-like game played against the computer dealer.
"""
# pylint: disable=import-error, wrong-import-position
from time import sleep
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_message_dict, prompt, get_valid_user_input
from game_mechanics import deal, hit, has_blackjack, has_busted, \
                           score_round, display_table
from classes import Deck, Hand


# Constants
MESSAGES_PATH = "./game_messages.json"
HIT = '1'
STAY = '2'
YES = "1"
NO = "2"


def initialize_game(player_name: str):
    """Initializes a game of blackjack

    :param player_name (str): the player name
    :returns deck, hands
    """
    deck = Deck()
    hands = {
        'Dealer': Hand("Dealer"),
        player_name: Hand(player_name),
    }
    return deck, deal(deck, hands)


def handle_welcome(messages: dict) -> None:
    """Driver function for welcome section"""
    prompt(messages["welcome"])
    player_name = get_valid_user_input(
                  messages["name"], validation_func=lambda s, _: s.isalnum())
    return player_name


def handle_hit(deck: Deck, hands: dict, name: str) -> bool:
    """Draws a card from the deck to the given hand, and checks for bust

    :param deck (Deck): the deck to draw from
    :param hands (dict): the hands of the game
    :param name (str): the name of the player who has hit
    :returns (bool): True | False if the hand is greater than 21
    """
    hand = hands[name]
    if name == "Dealer":
        sleep(.75)

    if name == "Dealer" and hand.cards[-1].concealed:
        hand.cards[-1].reveal()
    else:
        hit(deck, hand)

    if has_busted(hand):
        hand.busted()

    display_table(hands)


def handle_turn(player_name: str, deck: Deck, hands: dict,
                messages: dict, is_dealer: bool = False) -> None:
    """Driver code for handling a turn

    :param player_name (str): name of player
    :param deck (Deck): the deck to draw from
    :param hands (dict): the hands of the game
    :param messages (dict): the game messages dict
    :param is_dealer (bool): is dealers turn
    """
    curr_turn = "Dealer" if is_dealer else player_name

    while not (
          has_blackjack(hands[curr_turn]) or hands[player_name].is_busted):

        if is_dealer:
            dealer_total = hands["Dealer"].total(include_concealed=True)
            player_total = hands[player_name].total()
        else:
            hit_or_stay = get_valid_user_input(messages["hit_or_stay"],
                                               valid_choices=[HIT, STAY])

        # pylint: disable=possibly-used-before-assignment
        if (is_dealer and dealer_total <= player_total) or \
           (not is_dealer and hit_or_stay == HIT):

            handle_hit(deck, hands, curr_turn)

            if hands[player_name].is_busted:
                break
        else:
            break


def handle_scoring(player_name: str, hands: dict, messages: dict) -> None:
    """Driver function for handling the scoring at the end of a round"""
    winner = score_round(hands, player_name)

    if winner == "Dealer" and hands["Dealer"].cards[-1].concealed:
        hands["Dealer"].cards[-1].reveal()
        display_table(hands)

    if hands[player_name].is_busted:
        prompt(f"{player_name} {messages["bust"]}")
    elif hands["Dealer"].is_busted:
        prompt(f"Dealer {messages["bust"]}")

    if winner == "Push":
        prompt(messages["push"])
    else:
        prompt(f"{messages["winner"]} {winner}")


def play_again(messages):
    """Ask the player if they want to play another game."""
    another_game = get_valid_user_input(messages["play_again"],
                                        valid_choices=[YES, NO])
    return another_game == YES


def main():
    """Main driver function for the game"""
    messages = get_message_dict(MESSAGES_PATH)
    player_name = handle_welcome(messages)

    while True:
        deck, hands = initialize_game(player_name)

        while True:
            if has_blackjack(hands["Dealer"]):
                break
            handle_turn(player_name, deck, hands, messages)
            handle_turn(player_name, deck, hands, messages, is_dealer=True)
            break

        handle_scoring(player_name, hands, messages)

        if not play_again(messages):
            prompt(messages["goodbye"])
            return


if __name__ == "__main__":
    main()
