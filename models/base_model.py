#!/usr/bin/python3
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Defines the BaseModel class.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != '__class__':
                        setattr(self, key, value)
                elif key == 'id':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
        )
    def save(self):
        """
        Updates the public instance attribute update_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary conatining all keys/values of __dict__ of the instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = type(self).__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
