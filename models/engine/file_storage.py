#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """DEserializes the JSON file to __objects."""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    objdict = json.load(file)
                except json.decoder.JSONDecodeError:
                    objdict = {}
                for o_id o in objdict.values():
                    FileStorage_name = o["__class__"]
                    del o["__class__"]
                    obj_instance = eval(FileStorage_name)(**o)
                    key = "{}.{}".format(FileStorage_name, o_id)
                    self.__objects[key] = obj_instance
        else:
            open(FileStorage.__file_path, 'w').close()
