#!/usr/bin/python3
""" """
import json


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
        self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def save(self):
        """
        """
        json_str = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as f:
            f.write(json_str)
    
    def reload(self):
        """
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_str = f.read()
                self.__objects = json.loads(json_str)
        except FileNotFoundError:
            pass

    def remove(self, key):
        """
        """
        del self.__objects[key]
