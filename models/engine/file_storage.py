#!/usr/bin/python3
"""
This module defines the FileStorage class for serializing and deserializing
Python objects to and from JSON files.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing and deserializing Python objects to and
    from JSON files.
    """

    def __init__(self, path="file.json"):
        """
        Initialize a new FileStorage instance.

        Args:
            path (str): The file path to store the serialized objects.
                        Default is "file.json".
        """
        self.__file_path = path
        self.__objects = {}

    def all(self):
        """
        Return the dictionary of objects.

        Returns:
            dict: A dictionary containing all objects currently loaded.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serialize the objects and save them to the JSON file.
        """
        objs_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        json_str = json.dumps(objs_dict)
        with open(self.__file_path, 'w') as f:
            f.write(json_str)

    def reload(self):
        """
        Deserialize the JSON file to Python objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_str = f.read()
                objs_dict = json.loads(json_str)
                self.__objects = {k: globals()[v['__class__']](**v)
                                  for k, v in objs_dict.items()}
        except FileNotFoundError:
            pass
