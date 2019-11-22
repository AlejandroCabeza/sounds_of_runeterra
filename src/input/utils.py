# Python Imports
# Third-Party Imports
# Project Imports
from data_structures.fields import FieldZones
from input.config import SCREEN_SIZE


def transform_mouse_position_to_bottom_left_coordinate_axis(top_left_mouse_position: (int, int)) -> (int, int):
    _, screen_height = SCREEN_SIZE
    return top_left_mouse_position[0], screen_height - top_left_mouse_position[1]


def get_fields_y_coords(vertical_screen_size):
    field_size = vertical_screen_size / 4
    chunk_size = vertical_screen_size / 8
    return {
        FieldZones.PLAYER_HAND: 1,
        FieldZones.PLAYER_PLAYED: chunk_size,
        FieldZones.PLAYER_BATTLEFIELD: chunk_size + field_size,
        FieldZones.OPPONENT_HAND: vertical_screen_size - 1,
        FieldZones.OPPONENT_PLAYED: vertical_screen_size - chunk_size,
        FieldZones.OPPONENT_BATTLEFIELD: vertical_screen_size - chunk_size - field_size,
    }
