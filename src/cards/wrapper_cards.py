import json
from .card import Card


def get_all_cards(path):
    with open(path, "rb") as json_card_file:
        return json.load(json_card_file)


def create_cards():
    cards = {}
    for data in get_all_cards("../cards_data.json"):
        cards[data["cardCode"]] = Card(data["name"],
                                       data["descriptionRaw"],
                                       data["attack"],
                                       data["health"],
                                       data["cost"],
                                       data["type"],
                                       data["region"],
                                       data["keywords"])

    return cards
