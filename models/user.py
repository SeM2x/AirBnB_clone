#!/usr/bin/python3
""""""
from .base_model import BaseModel

class User(BaseModel):
    """
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)
