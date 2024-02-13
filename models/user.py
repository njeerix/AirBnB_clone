from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as storage



class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User"""
        super().__init__(*args, **kwargs)

    @classmethod
    def all(cls):
        """Retrieve all instances of User"""
        return [instance for instance in storage.all().values() 
                if isinstance(instance, cls)]
