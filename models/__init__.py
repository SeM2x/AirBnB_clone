#!/usr/bin/python3
"""
This module initializes the storage system for the models package.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
