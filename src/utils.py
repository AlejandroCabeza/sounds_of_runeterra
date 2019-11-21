# Python Imports
import json
# Third-Party Imports
# Project Imports
from config import CARDS_MESSAGES


def read_json_file_as_dict(filepath: str) -> dict:
    with open(filepath, "rb") as json_card_file:
        return json.load(json_card_file)


def generate_field_cards_message(message_formatter: CARDS_MESSAGES, cards: [], use_verbose_mode: bool) -> str:
    if len(cards) != 0:
        cards_as_string = "\n".join(card.get_as_string(use_verbose_mode) for card in cards)
        return message_formatter.existing_formatter.format(card_description_list=cards_as_string)
    return message_formatter.empty_message
