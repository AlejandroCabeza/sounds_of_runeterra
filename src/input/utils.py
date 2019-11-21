# Python Imports
import enum
# Third-Party Imports
# Project Imports
from input.config import SCREEN_SIZE


def transform_mouse_position_to_bottom_left_coordinate_axis(top_left_mouse_position: (int, int)) -> (int, int):
    _, screen_height = SCREEN_SIZE
    return top_left_mouse_position[0], screen_height - top_left_mouse_position[1]


class Field(enum.Enum):
    PLAYER_HAND: int = 0
    PLAYER_PLAYED: int = 1
    PLAYER_BATTLEFIELD: int = 2
    OPPONENT_HAND: int = 3
    OPPONENT_PLAYED: int = 4
    OPPONENT_BATTLEFIELD: int = 5


def get_fields_y_coords(vertical_screen_size):
    field_size = vertical_screen_size / 4
    chunk_size = vertical_screen_size / 8
    return {
        Field.PLAYER_HAND: 1,
        Field.PLAYER_PLAYED: chunk_size,
        Field.PLAYER_BATTLEFIELD: chunk_size + field_size,
        Field.OPPONENT_HAND: vertical_screen_size - 1,
        Field.OPPONENT_PLAYED: vertical_screen_size - chunk_size,
        Field.OPPONENT_BATTLEFIELD: vertical_screen_size - chunk_size - field_size,
    }
