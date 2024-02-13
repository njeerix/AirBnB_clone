import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, obj in self.__objects.items():
            if hasattr(obj, 'to_dict'):
                serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                deserialized_objs = json.load(f)
                for key, value in deserialized_objs.items():
                    class_name, obj_id = key.split('.')
                    module_name = "models." + class_name.lower()
                    module = __import__(module_name, fromlist=[class_name])
                    obj_class = getattr(module, class_name)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass


storage = FileStorage()
