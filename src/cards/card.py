from typing import Dict, Any
import json


class Card(object):

    def __init__(self, fields: Dict[str, Any], verbosity: bool = False):
        self._data = fields
        self._verbosity = verbosity

    async def get_data(self):
        """
        We can make any improvement to read the type and avoid returning
         attack and health if the type isn´t a unit or if it has attack and health to 0
        """
        if self._verbosity:
            return f"{json.dumps(self._data)}"
        else:
            return f"{list(self._data.values())}"
