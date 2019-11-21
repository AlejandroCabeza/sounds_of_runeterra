from typing import Dict, Any
import json


class Card(object):

    def __init__(self, fields: Dict[str, Any], verbose_msg: str):
        self._data = fields
        self._message = verbose_msg

    def get_data(self, verbose=False):
        if verbose:
            return self._message.format(**{k: str(v) if v is not None else "" for k, v in self._data.items()})
        return "\n".join(f"{attr}  {value}" for attr, value in self._data.items())

    def __repr__(self):
        return self._data.__repr__()
