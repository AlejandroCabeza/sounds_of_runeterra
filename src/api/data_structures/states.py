# Python Imports
from enum import Enum
# Third-Party Imports
# Project Imports


class BaseEnum(Enum):
    @classmethod
    def get_state_from_string(cls, string: str):
        try:
            return cls[string]
        except KeyError:
            return None



class GameStates(BaseEnum):
    Menus = 0
    InProgress = 1


class ExpeditionStates(BaseEnum):
    Inactive = 0
    Offscreen = 1
    Picking = 2
    Swapping = 3
    Other = 4
