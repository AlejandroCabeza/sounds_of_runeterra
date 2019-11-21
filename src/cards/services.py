# Python Imports
# Third-Party Imports
# Project Imports
from cards.card import Card
from api.services import get_cards_as_rectangles
from data_structures.rectangles import Rectangle
from data_structures.services import get_id_of_rectangle_hovered_by_mouse, get_id_of_rectangle_in_y_coord


def get_card_from_rectangles_in_a_position(position: (int, int), rectangles: [Rectangle], cards: {str: Card}) -> Card:
    card_id = get_id_of_rectangle_hovered_by_mouse(position, rectangles)
    print(card_id)
    return cards.get(card_id, None)


def get_card_from_rectangles_by_y_coord(y_coord: int, rectangles: [Rectangle], cards: {str: Card}):
    cards_ids = get_id_of_rectangle_in_y_coord(y_coord, rectangles)
    return (
        cards.get(card_id, None) for card_id in cards_ids
    )


async def get_card_in_position(position: (int, int), cards: {str: Card}) -> Card:
    rectangles: [Rectangle] = await get_cards_as_rectangles()
    return get_card_from_rectangles_in_a_position(position, rectangles, cards)


async def get_cards_in_field_by_y_coord(field_y_coord, cards: {str: Card}):
    rectangles: [Rectangle] = await get_cards_as_rectangles()
    return (
        cards.get(card_id, None) for card_id in get_id_of_rectangle_in_y_coord(field_y_coord, rectangles)
    )
