from typing import Set


class Territory:
    def __init__(self, name, continent):
        self._name: str = name
        self._continent = continent  # TODO add type
        self._army: int = 0
        self._owner = None  # TODO add type
        self._connections: Set[Territory] = set()

    @property
    def name(self):
        return self._name

    @property
    def continent(self):
        return self._continent

    @property
    def army(self):
        return self._army

    @property
    def owner(self):
        return self._owner

    @property
    def connections(self):
        return self._connections

