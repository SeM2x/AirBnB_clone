#!/usr/bin/python3
"""
This module defines the User class, a subclass of BaseModel.
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User class for storing information about users.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        """
        super().__init__(*args, **kwargs)
