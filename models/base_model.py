#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class for all
other classes in the HBNB project.
"""

import uuid
from datetime import datetime
import models
from copy import copy


class BaseModel:
    """
    BaseModel class for storing common attributes and methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' attribute and save the BaseModel instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary.
        """
        new_dict = copy(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
