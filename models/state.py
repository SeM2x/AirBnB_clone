#!/usr/bin/python3
"""
This module defines the State class, a subclass of BaseModel.
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State class for storing information about states.
    """

    name = ''

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.
        """
        super().__init__(*args, **kwargs)
