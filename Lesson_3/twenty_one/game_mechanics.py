"""
Game mechanics classes and functions for Twenty-One!
"""
# pylint: disable=import-error, wrong-import-position
# from sys import path
# from pathlib import Path
# path.append(str(Path(__file__).resolve().parent / '../utils/'))
# from helper_functions import get_valid_user_input, prompt
from classes import Hand

def build_card_group_list(cards: list, group_size: int) -> list:
    """
    :param cards (list): the cards to concatenate
    :param group_size (int): the number of cards to group together
    :returns card_groups (list): the cards in groups of group_size
    """
    card_groups = []
    group = []

    for card in cards:
        group.append(card)

        if len(group) == group_size:
            card_groups.append(group)
            group = []

    if group:
        card_groups.append(group)

    return card_groups


def card_group_to_str(group: list) -> str:
    """Prepares a card group to be printed. Each card is split into 5 lines
    (or pieces) and then concatenated with all other cards as lines in the
    group. A card has this structure:

    ┌─────┐
    │5    │
    │  *  │
    │    5│
    └─────┘

    and the card as a str looks like this:

    "┌─────┐\n│5    │\n│  *  │\n│    5│\n└─────┘"

    :param group (list<Card>): a list of cards to be concatenated
    :returns group_str (str): a group of cards coerced to a printable str
    """
    group_pieces_by_line = {line: [] for line in range(0, 5)}

    for card in group:
        for i, card_piece in enumerate(str(card).split("\n")):
            group_pieces_by_line[i].append(card_piece)

    group_str = "\n".join([
        " ".join(pieces) for pieces in group_pieces_by_line.values()])
    return group_str


def assemble_cards(cards: list, group_size: int) -> str:
    """Concatenates cards together in groups prepare them for printing

    :param cards (list): the cards to concatenate
    :param group_size (int): the number of cards to group together
    :returns assembled_cards (str): the assembled cards
    """
    card_groups = build_card_group_list(cards, group_size)
    assembled_cards = []

    for group in card_groups:
        assembled_group = card_group_to_str(group)
        assembled_cards.append(assembled_group)

    return "\n".join(assembled_cards)


def total(hand: Hand) -> int:
    """Returns the total for the given Hand

    :param hand (Hand): the Hand to total
    returns hand_total (int): the total of the hand
    """
    card_ranks = [card.get_rank() for card in hand.cards]
    hand_total = sum((card.as_int() for card in hand.cards))
    num_aces = card_ranks.count("A")

    while hand_total > 21 and num_aces:
        hand_total -= 10
        num_aces -= 1

    return hand_total
