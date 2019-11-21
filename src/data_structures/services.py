# Python Imports
# Third-Party Imports
# Project Imports
from data_structures.states import GameState
from data_structures.rectangles import Rectangle


def is_game_state_in_progress(game_state: GameState):
    return game_state == GameState.InProgress


def is_game_state_in_menus(game_state: GameState):
    return game_state == GameState.Menus


def is_game_state_in_transition(game_state: GameState):
    return game_state == GameState.Transition


def get_id_of_rectangle_hovered_by_mouse(mouse_position: (int, int), rectangles: [Rectangle]):
    mouse_x, mouse_y = mouse_position
    for rectangle in rectangles:
        if rectangle.is_position_inside_rectangle(mouse_x, mouse_y):
            return rectangle.rectangle_code
    return None

def get_id_of_rectangle_in_y_coord(y_coord: int, rectangles: [Rectangle]) -> [str]:
    return (
        rectangle.rectangle_code
        for rectangle in rectangles
        if rectangle.is_position_inside_rectangle((rectangle.top_x+rectangle.width)//2, y_coord)
    )
