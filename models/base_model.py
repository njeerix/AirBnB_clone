#!/usr/bin/python3

import uuid
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines the base model class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
