# Python Imports
# Third-Party Imports
# Project Imports


def format_cards_from_rectangles(cards: [{}]) -> [{}]:
    return {
        card["CardCode"]: {
            key: value
            for key, value in card.items() if key in ("TopLeftX", "TopLeftY", "Width", "Height", "LocalPlayer")
        }
        for card in cards
    }
