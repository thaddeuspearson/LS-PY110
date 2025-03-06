"""
Game mechanics classes and functions for Twenty-One!
"""
# pylint: disable=import-error, wrong-import-position
# from sys import path
# from pathlib import Path
# path.append(str(Path(__file__).resolve().parent / '../utils/'))
# from helper_functions import get_valid_user_input, prompt


# Constants
STARTING_HAND_SIZE = 2
BLACKJACK = 21


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


def total(hand) -> int:
    """Returns the total for the given Hand

    :param hand (Hand): the Hand to total
    returns hand_total (int): the total of the hand
    """
    card_ranks = [card.get_rank() for card in hand.cards]
    hand_total = sum((int(card) for card in hand.cards if not card.concealed))
    num_aces = card_ranks.count("A")

    while hand_total > 21 and num_aces:
        hand_total -= 10
        num_aces -= 1

    return hand_total


def dealer_total(hand) -> int:
    """Gets the dealer total, including concealed cards

    :param hand (Hand): the Hand to total
    :returns dealer_total (int): the total of the hand
    """
    concealed_total = sum(card for card in hand.cards if card.concealed)
    return total(hand) + concealed_total


def deal(deck, hands: dict) -> None:
    """Deals all starting hands for the given deck

    :param deck (Deck): the deck to deal from
    :param hands (dict<Hands>): the hands to deal to
    """
    deck.shuffle()

    for i in range(STARTING_HAND_SIZE):
        for hand in hands:
            if hand == "dealer" and i == STARTING_HAND_SIZE-1:
                hands[hand].draw(1, deck, concealed=True)
            else:
                hands[hand].draw(1, deck)

    display_table(reversed(hands.values()))  # reversed so dealer prints on top
    return hands


def display_table(hands) -> None:
    """Prints all hands at the table, beginning with the dealer

    :param hands (list): list of hands to print
    """
    for hand in hands:
        print("\n")
        print(f"{hand.name} Hand:\n{hand}")
        print(f"Total: {total(hand)}")


def hit(deck, hand) -> None:
    """Draws a card from the deck and puts it into the given hand

    :param deck (Deck): the deck to draw from
    :param hand (Hand): the hand to draw into
    :returns total int: the total of the hand after hitting
    """
    hand.draw(1, deck)
    return total(hand)


def stay(hand):
    """Stays the hand, and returns the hand total

    :param total (int): the total of the hand
    """
    return total(hand)


def players_with_blackjack(hands: dict) -> str:
    """Returns a list of player(s) who were dealt a blackjack

    :param hands (dict): all the hands at the table
    :returns has_blackjack (list): player names who were dealt a blackjack
    """
    has_blackjack = []

    for hand in hands:
        hand_total = dealer_total(hand) if hand == "dealer" else total(hand)
        if hand_total == BLACKJACK:
            has_blackjack.append(hand)

    return has_blackjack
