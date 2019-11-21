import json
from .card import Card


def get_all_cards(path):
    with open(path, "rb") as json_card_file:
        return json.load(json_card_file)


def get_fields(path):
    with open(path, "rb") as json_card_fields:
        return json.load(json_card_fields)


def create_cards(verbosity=False):
    cards = {}
    key, fields = get_fields("../cards_field.json").values()
    for data in get_all_cards("../cards_data.json"):
        cards[data[key]] = Card({v: data.get(k, None) for k, v in fields.items()},
                                verbosity)

    return cards
