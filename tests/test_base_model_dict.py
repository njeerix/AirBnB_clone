import unittest
import datetime
from models.engine.file_storage import storage
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    def tearDown(self):
        pass

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.save()
        my_model_dict = my_model.to_dict()
        created_at_str = my_model_dict['created_at']
        created_at = datetime.datetime.strptime(
            created_at_str,
            "%Y-%m-%dT%H:%M:%S.%f"
        )
        self.assertIsInstance(created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
