from typing import Set

from voluptuous import Schema, Required, MultipleInvalid

from riskpy.territory import Territory


class Continent:
    def __init__(self, name, point_value):
        self._name = name
        self._point_value = point_value
        self._territories: Set[Territory] = set()

    @staticmethod
    def dict_schema() -> Schema:
        schema = Schema({
            Required("name"): str,
            Required("point_value"): int})

        return schema

    @staticmethod
    def create_from_dict(dict_continent):
        '''
        Create a continent instance from a dict. Validate the format of the dict
        :param dict_territory: A dictionnary from which the continent can be instantiated
        :return:
        '''
        schema = Continent.dict_schema()
        try:
            schema(dict_continent)
        except MultipleInvalid as e:
            print(e)

        return Territory(dict_continent["name"], dict_continent["point_value"])
