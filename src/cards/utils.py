# Python Imports
# Third-Party Imports
# Project Imports
from src.cards.card import Card
from src.utils import read_json_file_as_dict


def get_card_fields(filepath: str):
    card_fields = read_json_file_as_dict(filepath)
    try:
        return card_fields["key"], card_fields["values"], card_fields["message"]
    except KeyError:
        raise KeyError("Key, Values and Message is mandatory")


def create_cards_dictionary(card_fields_filepath: str, cards_data_filepath: str):
    card_code_key, card_fields, card_message = get_card_fields(card_fields_filepath)
    cards_as_dict = read_json_file_as_dict(cards_data_filepath)
    return {
        card[card_code_key]: Card({
                value: card.get(key, None)
                for key, value in card_fields.items()
            },
            card_message
        )
        for card in cards_as_dict
    }


if __name__ == "__main__":
    cards = list(create_cards_dictionary(
        "../../resources/cards_field.json",
        "../../resources/cards_data.json"
    ).values())
    print(cards[17].get_as_string(verbose=False))
    print(cards[17].get_as_string(verbose=True))
