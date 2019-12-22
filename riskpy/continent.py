from typing import Set

from riskpy.territory import Territory


class Continent:
    def __init__(self, name, point_value):
        self._name = name
        self._point_value = point_value
        self._territories: Set[Territory] = set()
