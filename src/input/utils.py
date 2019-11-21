# Python Imports
# Third-Party Imports
# Project Imports
from input.config import SCREEN_SIZE


def transform_mouse_position_to_bottom_left_coordinate_axis(top_left_mouse_position: (int, int)) -> (int, int):
    _, screen_height = SCREEN_SIZE
    return top_left_mouse_position[0], screen_height - top_left_mouse_position[1]
