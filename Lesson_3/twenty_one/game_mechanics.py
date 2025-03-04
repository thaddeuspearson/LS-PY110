"""
Game mechanics classes and functions for Twenty-One!
"""
# pylint: disable=import-error, wrong-import-position
import random
# from sys import path
# from pathlib import Path
# path.append(str(Path(__file__).resolve().parent / '../utils/'))
# from helper_functions import get_valid_user_input, prompt


class Card:
    """A standard playing card."""
    def __init__(self,  rank: str, suit: str) -> None:
        """Initializes the card with its rank and suit

        :param rank (str): the rank of the card (2 - 10, J, Q, K, A)
        :param suit (str): the suit of the card (♠ ♥ ♣ ♦)
        """
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        """Returns an ASCII art representation of the card

        :returns card_face (str): an ASCII art card face
        """
        card_face = self._build_card_face()
        return card_face

    def _build_card_face(self) -> str:
        """Builds an ASCII art representation of the card face

        :returns card_face (str): an ASCII art card face
        """
        card_face = (
            f"┌─────┐\n"
            f"│{self.rank}{" " * (5 - len(self.rank))}│\n"
            f"│  {self.suit}  │\n"
            f"│{" " * (5 - len(self.rank))}{self.rank}│\n"
            f"└─────┘"
        )
        return card_face

    def value(self) -> str:
        """Returns the card value as a string"""
        suits = {
            '♠': "Spades",
            '♥': "Hearts",
            '♣': "Clubs",
            '♦': "Diamonds"
        }
        return f"{self.get_rank()} of {suits[self.get_suit]}"

    def get_rank(self) -> str:
        """Returns the card rank."""
        return self.rank

    def get_suit(self) -> str:
        """Returns the card suit."""
        return self.suit


class Deck:
    """A deck of playing cards."""
    def __init__(self) -> None:
        """Initializes a standard deck of playing cards:
        ♠ ♥ ♣ ♦ | 2 - 10, J, Q, K, A (no Jokers).
        """
        self.cards = self._initialize_cards()
        self.discard_pile = []

    def _initialize_cards(self) -> list:
        """Loads a new standard deck of cards."""
        cards = []

        for suit in ('♠', '♥', '♣', '♦'):
            for rank in range(1, 14):
                match rank:
                    case 11:
                        rank = "J"
                    case 12:
                        rank = "Q"
                    case 13:
                        rank = "K"
                    case _ if rank in (1, 11):
                        rank = "A"
                    case _:
                        rank = str(rank)
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self, reset: bool = False) -> None:
        """Shuffles and reverses the cards for proper drawing mechanics

        :param reset (bool): resets the deck by emptying the discard pile
        """
        if reset:
            self.cards.extend(self.discard_pile)
            self.discard_pile.clear()
        random.shuffle(self.cards)
        self.cards.reverse()

    def draw(self) -> Card:
        """Draws a card from the "top" of the deck, draws in reverse order for
        performance.

        :param deck (list): the deck of cards to draw from
        :returns card (str): the drawn card
        """
        card = self.cards.pop()
        return card

    def discard(self, card: Card) -> None:
        """Adds the card to the discard pile."""
        self.discard_pile.append(card)


class Hand:
    """A hand of playing cards."""
    def __init__(self, name: str, cards: list = []):
        """Initializes a hand of Twenty-One"""
        self.name = name
        self.cards = cards

    def draw(self, number: int, deck: Deck) -> None:
        """Draws a card from the given deck

        :param number (int): the number of cards to draw
        :param deck (Deck): the deck to draw from
        """
        self.cards.extend([deck.draw() for _ in range(number)])

    def discard(self, card: Card, deck: Deck) -> None:
        """Discards the given card to the discard pile of the given deck

        :param card (Card): the card to discard
        :param deck (Deck): the deck to discard to
        """
        card = self.cards.pop(self.cards.index(card))
        deck.discard(card)

    def reset(self, deck: Deck) -> None:
        """Discards all cards in hand

        :param deck (Deck): the deck to discard to
        """
        for card in self.cards:
            deck.discard(card)
        self.cards.clear()

    def display(self) -> None:
        """Prints all cards in hand"""
        print(assemble_cards(self.cards, group_size=5))


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
