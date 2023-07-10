#!/usr/bin/python3
"""
The base class that will be the blueprint
"""
import json
from os import path


class Base:
    """
    blueprint for classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string of a list of dicts
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json to a file
        """
        a_list = []
        file = cls.__name__ + '.json'
        if list_objs is not None:
            for idx in list_objs:
                a_list.append(idx.to_dictionary())
        with open(file, mode='w') as f:
            f.write(cls.to_json_string(a_list))

    @staticmethod
    def from_json_string(json_string):
        """
        loads a list from json_strings
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with predefined attributes
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file = cls.__name__ + ".json"
        b_list = []
        if path.isfile(file):
            with open(file) as f:
                output = cls.from_json_string(f.read())
            for i in output:
                b_list.append(cls.create(**i))
        return b_list
