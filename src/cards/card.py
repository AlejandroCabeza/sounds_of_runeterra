from typing import Dict, Any


class Card(object):

    def __init__(self, fields: Dict[str, Any], verbosity: bool = False):
        self._data = fields
        self._verbosity = verbosity
        self.__dict__.update(fields)

    async def get_data(self):
        if self._verbosity:
            return (f"{str(self._data)}")
        else:

        return (f"{self._name}. {self._type}. Cost: {self._cost}. "
                f"{'Attack': {self._attack}'|'{self._health} if self._type == 'Unit' else ''}"
                f"{self._description}")
