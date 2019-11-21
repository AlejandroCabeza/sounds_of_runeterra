import json
from src.cards.card import Card


def read_json_file(path):
    with open(path, "rb") as json_card_file:
        return json.load(json_card_file)


def get_fields():
    config = read_json_file("../../cards_field.json")
    try:
        return config["key"], config["values"], config["message"]
    except KeyError as k:
        raise KeyError("Key, Values and Message is mandatory")


def create_cards():
    code_key, fields, message = get_fields()
    cards = {}
    for data in read_json_file("../../cards_data.json"):
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
