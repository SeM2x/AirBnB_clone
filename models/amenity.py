#!/usr/bin/python3
"""
This module defines the Amenity class, a subclass of BaseModel.
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for storing information about amenities.
    """

    name = ''

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.
        """
        super().__init__(*args, **kwargs)
