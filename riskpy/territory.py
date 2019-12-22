from typing import Set

from voluptuous import Schema, Required, MultipleInvalid


class Territory:
    def __init__(self, name, continent):
        self._name: str = name
        self._continent = continent  # TODO add type
        self._army: int = 0
        self._owner = None  # TODO add type
        self._connections: Set[Territory] = set()

    @property
    def name(self):
        '''
        The name of the territory
        :return: name
        '''
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

    @staticmethod
    def dict_schema() -> Schema:
        schema = Schema({
            Required("name"): str,
            Required("continent"): str})

        return schema

    @staticmethod
    def create_from_dict(dict_territory):
        '''
        Create a territory instance from a dict. Validate the format of the dict
        :param dict_territory: A dictionnary from which the territory can be instantiated
        :return:
        '''
        schema = Territory.dict_schema()
        try:
            schema(dict_territory)
        except MultipleInvalid as e:
            print(e)

        return Territory(dict_territory["name"], dict_territory["continent"])
