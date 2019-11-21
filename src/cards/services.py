# Python Imports
# Third-Party Imports
# Project Imports
from cards.card import Card
from api.services import get_cards_as_rectangles
from data_structures.rectangles import Rectangle
from data_structures.services import get_id_of_rectangle_hovered_by_mouse


def  get_card_from_rectangles_in_a_position(position: (int, int), rectangles: [Rectangle], cards: [{str: Card}]) -> Card:
    card_id = get_id_of_rectangle_hovered_by_mouse(position, rectangles)
    print(card_id)
    return cards.get(card_id, None)


async def get_card_in_position(position: (int, int), cards: {str: Card}) -> Card:
    rectangles: [Rectangle] = await get_cards_as_rectangles()
    return get_card_from_rectangles_in_a_position(position, rectangles, cards)