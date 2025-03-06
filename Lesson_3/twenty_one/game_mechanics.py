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

    display_table(hands)  # reversed so dealer prints on top
    return hands


def display_table(hands) -> None:
    """Prints all hands at the table, beginning with the dealer

    :param hands (list): list of hands to print
    """
    for hand in hands.values():
        print("\n")
        print(f"{hand.name} Hand:\n{hand}")
        print(f"Total: {hand.total()}")


def hit(deck, hand) -> None:
    """Draws a card from the deck and puts it into the given hand

    :param deck (Deck): the deck to draw from
    :param hand (Hand): the hand to draw into
    :returns total int: the total of the hand after hitting
    """
    hand.draw(1, deck)
    return hand.total()


def stay(hand):
    """Stays the hand, and returns the hand total

    :param total (int): the total of the hand
    """
    return hand.total()


def get_hand_total(hand) -> int:
    """Gets the total of the given hand

    :param hand: the hand to total
    returns hand_total (int): the total of the hand"""
    if hand.name == "Dealer":
        hand_total = hand.total(include_concealed=True)
    else:
        hand_total = hand.total()
    return hand_total


def has_blackjack(hand) -> bool:
    """Returns True if the given hand was dealt a blackjack

    :returns (bool): True | False
    """
    hand_total = get_hand_total(hand)
    return hand_total == BLACKJACK


def has_busted(hand) -> bool:
    """Returns True if the given hand total exceeds 21

    :returns (bool): True | False
    """
    hand_total = get_hand_total(hand)
    return hand_total > BLACKJACK


def score_round(hands: dict) -> str:
    """Scores the round and returns the string of the winner
    :param hands (dict): all the hands at the table
    :returns winner (str): the winner of the round | "Push" if a tie
    """
    dealer_score = hands["dealer"].total(include_concealed=True)
    player_score = hands["player"].total()

    if dealer_score == player_score:
        winner = "Push"
    elif dealer_score > player_score:
        winner = "Dealer"
    else:
        winner = "Player"

    if winner != "Player":
        (card.reveal() for card in hands["dealer"].cards)
        display_table(hands)
    return winner
