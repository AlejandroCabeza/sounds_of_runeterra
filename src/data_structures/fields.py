# Python Imports
import enum
# Third-Party Imports
# Project Imports


class FieldZones(enum.Enum):
    PLAYER_HAND: int = 0
    PLAYER_PLAYED: int = 1
    PLAYER_BATTLEFIELD: int = 2
    OPPONENT_HAND: int = 3
    OPPONENT_PLAYED: int = 4
    OPPONENT_BATTLEFIELD: int = 5
