#!/usr/bin/python3
"""__init__ magic method for models directory"""

from .base_model import BaseModel
from .user import User
from .place import Place
from .state import State
from .city import City
from .amenity import Amenity
from .review import Review

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
