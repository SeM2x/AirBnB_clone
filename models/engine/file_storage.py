#!/usr/bin/python3
""" """
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
    """
    def __init__(self, path="file.json"):
        """
        """
        self.__file_path = path
        self.__objects = {}

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        """
        objs_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        json_str = json.dumps(objs_dict)
        with open(self.__file_path, 'w') as f:
            f.write(json_str)

    def reload(self):
        """
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_str = f.read()
                objs_dict = json.loads(json_str)
                self.__objects = {k: globals()[v['__class__']](**v)
                                  for k, v in objs_dict.items()}
        except FileNotFoundError:
            pass
