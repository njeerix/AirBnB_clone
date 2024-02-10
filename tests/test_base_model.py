import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage._FileStorage__objects = {}

    def test_save_method(self):
        initial_count = len(self.storage.all())
        my_model = BaseModel()
        my_model.save()
        objs = self.storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertEqual(len(objs), initial_count + 1)
        self.assertIn(key, objs)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.save()
        my_model_dict = my_model.to_dict()
        created_at_str = my_model_dict['created_at']
        created_at = datetime.datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertIsInstance(created_at, datetime.datetime)

if __name__ == "__main__":
    unittest.main()
