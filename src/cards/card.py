import os

class Card(object):

    def __init__(self, name, description, attack, health, cost, type_card, region, keywords):
        self._name = name
        self._description = description
        self._attack = attack
        self._health = health
        self._cost = cost
        self._type = type_card
        self._region = region
        self._keywords = keywords

    async def get_data(self):
        return (f"{self._name}. {self._type}. Cost: {self._cost}. "
                f"{'Attack': {self._attack}'|'{self._health} if self._type == 'Unit' else ''}"
                f"{self._description}")
