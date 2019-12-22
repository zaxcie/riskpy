from typing import Set, Dict, List

from voluptuous import Schema, Required, MultipleInvalid

from riskpy.territory import Territory
from riskpy.continent import Continent


class Map:
    def __init__(self):
        self._territories: Set[Territory] = set()
        self._continent: Set[Continent] = set()
        self._map: Dict[str, List[str]] = dict()

    @staticmethod
    def dict_schema() -> Schema:
        schema = Schema({
            Required("continents"): list,
            Required("territories"): list,
            Required("map"): dict})

        return schema


