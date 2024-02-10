from models.engine.file_storage import FileStorage
from uuid import uuid4
from datetime import datetime

storage = FileStorage()
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
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the public instance attribute update_at with the cu
        """
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary conatining all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def some_method(self):
        from models.engine.file_storage import storage
