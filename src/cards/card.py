# Python Imports
from typing import Dict, Any
# Third-Party Imports
# Project Imports


class Card:

    def __init__(self, fields: Dict[str, Any], verbose_msg: str):
        self.__dict__ = fields
        self._verbose_message_format = verbose_msg

    def get_as_string(self, verbose: bool = False):
        if verbose:
            return self._get_as_string_verbose()
        else:
            return self._get_as_string_concise()

    def _get_as_string_verbose(self):
        return self._verbose_message_format.format(
            **{k: str(v) if v is not None else "" for k, v in self.__dict__.items()}
        )

    def _get_as_string_concise(self):
        string: str = f"{self.name}."

        if self.type == "Spell":
            string += f" Costs {self.cost} mana."
        else:
            string += f" {self.attack} {self.health} by {self.cost}"

        return string
