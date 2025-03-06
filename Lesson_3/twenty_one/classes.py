"""
Custom classes for Twenty-One!
"""
import random
from game_mechanics import assemble_cards


class Card:
    """A standard playing card."""
    def __init__(self, rank: str, suit: str, concealed: bool = False) -> None:
        """Initializes the card with its rank and suit

        :param rank (str): the rank of the card (2 - 10, J, Q, K, A)
        :param suit (str): the suit of the card (♠ ♥ ♣ ♦)
        :param concealed (str): the card will be dealt face-down
        """
        self.rank = rank
        self.suit = suit
        self.concealed = concealed

    def __str__(self) -> str:
        """Returns an ASCII art representation of the card

        :returns card_face (str): an ASCII art card face
        """
        card_face = self._build_card_face()
        return card_face

    def __int__(self):
        """Returns the card rank as an integer"""
        rank = self.rank
        face_cards = ["J", "Q", "K"]

        if rank == "A":
            return 11
        elif rank in face_cards:
            return 10
        else:
            return int(rank)

    def _build_card_face(self) -> str:
        """Builds an ASCII art representation of the card face

        :returns card_face (str): an ASCII art card face
        """
        rank = self.rank if not self.concealed else " "
        suit = self.suit if not self.concealed else " "
        card_face = (
            f"┌─────┐\n"
            f"│{rank}{" " * (5 - len(rank))}│\n"
            f"│  {suit}  │\n"
            f"│{" " * (5 - len(rank))}{rank}│\n"
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
        """Returns the card rank"""
        return self.rank

    def get_suit(self) -> str:
        """Returns the card suit"""
        return self.suit

    def reveal(self) -> None:
        """Reveals a face-down card"""
        self.concealed = False

    def conceal(self) -> None:
        """Conceals a face-up card"""
        self.concealed = True


class Deck:
    """A deck of playing cards."""
    def __init__(self) -> None:
        """Initializes a standard deck of playing cards:
        ♠ ♥ ♣ ♦ | 2 - 10, J, Q, K, A (no Jokers).
        """
        self.cards = self._initialize_cards()
        self.discard_pile = []

    def _initialize_cards(self) -> list:
        """Loads a new standard deck of cards"""
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

    def draw(self, concealed: bool = False) -> Card:
        """Draws a card from the "top" of the deck, draws in reverse order for
        performance

        :param deck (list): the deck of cards to draw from
        :param concealed (bool): draw the card face-down
        :returns card (str): the drawn card
        """
        if not self.cards:
            self.shuffle(reset=True)

        card = self.cards.pop()

        if concealed:
            card.conceal()

        return card

    def discard(self, card: Card) -> None:
        """Adds the card to the discard pile"""
        self.discard_pile.append(card)


class Hand:
    """A hand of playing cards."""
    def __init__(self, name: str, cards: list = None, group_size: int = 11):
        """Initializes a hand of Twenty-One"""
        self.name = name
        self.cards = [] if cards is None else cards
        self.group_size = group_size

    def __str__(self) -> str:
        """Assembles the cards in groups"""
        return assemble_cards(self.cards, self.group_size)

    def set_group_size(self, group_size: int) -> None:
        """Sets the card group size for printing"""
        self.group_size = group_size

    def draw(self, number: int, deck: Deck, concealed: bool = False) -> None:
        """Draws a card from the given deck

        :param number (int): the number of cards to draw
        :param deck (Deck): the deck to draw from
        :param concealed (bool): draw the card face-down
        """
        self.cards.extend([deck.draw(concealed) for _ in range(number)])

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

    def total(self, include_concealed: bool = False) -> int:
        """Returns the total for the given Hand

        :param include_concealed (bool): include the concealed cards in total
        returns hand_total (int): the total of the hand
        """
        card_ranks = [card.get_rank() for card in self.cards]
        num_aces = card_ranks.count("A")
        hand_total = sum(int(card) for card in self.cards
                         if include_concealed == card.concealed)

        while hand_total > 21 and num_aces:
            hand_total -= 10
            num_aces -= 1

        return hand_total
