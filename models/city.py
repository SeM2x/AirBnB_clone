#!/usr/bin/python3
"""
This module defines the City class, a subclass of BaseModel.
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    City class for storing information about cities.
    """

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.
        """
        super().__init__(*args, **kwargs)
