# Python Imports
import json
# Third-Party Imports
# Project Imports
from src.cards.card import Card


def read_json_file(path):
    with open(path, "rb") as json_card_file:
        return json.load(json_card_file)


def get_fields(filepath: str):
    config = read_json_file(filepath)
    try:
        return config["key"], config["values"], config["message"]
    except KeyError:
        raise KeyError("Key, Values and Message is mandatory")


def create_cards(card_fields_filepath: str, cards_data_filepath: str):
    code_key, fields, message = get_fields(card_fields_filepath)
    cards_in_json = read_json_file(cards_data_filepath)
    return {
        card[code_key]: Card({
                value: card.get(key, None)
                for key, value in fields.items()
            },
            message
        )
        for card in cards_in_json
    }


if __name__ == "__main__":
    cards = list(create_cards("../../cards_field.json", "../../cards_data.json").values())
    print(cards[0].get_data(verbose=False))
    print(cards[0].get_data(verbose=True))
