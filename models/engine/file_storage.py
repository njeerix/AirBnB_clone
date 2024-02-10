import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialize Json file to instances"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserialized_objs = json.load(f)
                for key, value in deserialized_objs.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "State":
                        obj = State(**value)
                    elif class_name == "City":
                        obj = City(**value)
                    elif class_name == "Amenity":
                        obj = Amenity(**value)
                    elif class_name == "Place":
                        obj = Place(**value)
                    elif class_name == "Review":
                        obj = Review(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def classes(self):
        class_names = set()
        for key in self.__objects.keys():
            class_name = key.split('.')[0]
            class_names.add(class_name)
        return class_names
