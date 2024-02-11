#!/usr/bin/python3
"""
This module defines the Review class, a subclass of BaseModel.
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class for storing information about reviews.
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Review instance.
        """
        super().__init__(*args, **kwargs)
