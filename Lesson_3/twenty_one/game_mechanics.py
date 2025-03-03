import random
from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parent / '../utils/'))
from helper_functions import get_valid_user_input, prompt


class Card:
    def __init__(self,  rank: str, suit: str) -> None:
        """Initializes the card with its rank and suit

        :param rank (str): the rank of the card (2 - 10, J, Q, K, A)
        :param suit (str): the suit of the card (♠ ♥ ♣ ♦)
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
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
            f"└─────┘\n"
        )
        return card_face


class Deck:
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

    def shuffle(self) -> None:
        """Shuffles and reverses the cards for proper drawing mechanics"""
        random.shuffle(self.cards)

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
