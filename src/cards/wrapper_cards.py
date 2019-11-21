import json
from src.cards.card import Card


def get_all_cards(path):
    with open(path, "rb") as json_card_file:
        return json.load(json_card_file)


def get_cards_config(path):
    with open(path, "rb") as json_card_fields:
        return json.load(json_card_fields)


def create_cards():
    cards = {}
    config = get_cards_config("../../cards_field.json")
    code_key = config["key"]
    fields = config["values"]
    message = config["message"]
    for data in get_all_cards("../../cards_data.json"):
        cards[data[code_key]] = Card(
            {v: data.get(k, None) for k, v in fields.items()},
            message
        )
    return cards


if __name__ == "__main__":
    from pprint import pprint
    cards = list(create_cards().values())
    # pprint(cards)

    print(cards[0].get_data(verbose=False))
    print(cards[0].get_data(verbose=True))
