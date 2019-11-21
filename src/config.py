# Python Imports
# Third-Party Imports
# Project Imports
from collections import namedtuple


CARDS_MESSAGES: namedtuple = namedtuple(
    "FieldCardsMessages",
    ("existing_formatter", "empty_message")
)


CARDS_MESSAGES_PLAYER_HAND = CARDS_MESSAGES(
    "Your hand cards are: {card_description_list}.",
    "You have no cards in your hand."
)


CARDS_MESSAGES_PLAYER_PLAYED = CARDS_MESSAGES(
    "Your played cards are: {card_description_list}.",
    "You have no cards played."
)


CARDS_MESSAGES_PLAYER_BATTLEFIELD = CARDS_MESSAGES(
    "Your battlefield cards are: {card_description_list}.",
    "You have no cards in the battlefield."
)


CARDS_MESSAGES_OPPONENT_HAND = CARDS_MESSAGES(
    "Opponent hand cards are: {card_description_list}.",
    "Your opponent has no visible cards in their hand."
)


CARDS_MESSAGES_OPPONENT_PLAYED = CARDS_MESSAGES(
    "Opponent played cards are: {card_description_list}.",
    "Your opponent has no played cards."
)

CARDS_MESSAGES_OPPONENT_BATTLEFIELD = CARDS_MESSAGES(
    "Opponent battlefield cards are: {card_description_list}.",
    "Your opponent has no cards in the battlefield."
)
