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

    # Overloading the __eq__ operator was necessary due to o possible bug occurring
    # when comparing two enums with the same value.
    # Enums are compared by identity and comparing two enums with the same enum value returned false.
    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return False


class GameStates(BaseEnum):
    Transition = 0
    Menus = 1
    InProgress = 2

    @classmethod
    def get_state_from_string(cls, string: str):
        state = super().get_state_from_string(string)
        if state is None:
            return GameStates.Transition


class ExpeditionStates(BaseEnum):
    Inactive = 0
    Offscreen = 1
    Picking = 2
    Swapping = 3
    Other = 4
