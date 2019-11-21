# Python Imports
from enum import Enum
# Third-Party Imports
# Project Imports


class GameState(Enum):
    Menus: str = "Menus"
    Transition: str = None
    InProgress: str = "InProgress"


class ExpeditionState(Enum):
    Inactive: str = "Inactive"
    Offscreen: str = "Offscreen"
    Picking: str = "Picking"
    Swapping: str = "Swapping"
    Other: str = "Other"
