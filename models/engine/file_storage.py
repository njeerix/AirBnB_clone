import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_instance = BaseModel(**obj_data)
                FileStorage.__objects[key] = obj_instance

        except FileNotFoundError:
            pass
