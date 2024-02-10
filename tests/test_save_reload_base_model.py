import unittest
from models.engine.file_storage import storage
from models.base_model import BaseModel

class TestSaveReloadBaseModel(unittest.TestCase):
    def test_save_and_reload(self):
        initial_count = len(storage.all())
        my_model = BaseModel()
        my_model.save()
        count_after_save = len(storage.all())
        self.assertEqual(count_after_save, initial_count + 1)

        obj_id = my_model.id
        del my_model

        reloaded_model = storage.reload(obj_id)
        self.assertIsNotNone(reloaded_model)
        self.assertIsInstance(reloaded_model, BaseModel)

if __name__ == "__main__":
    unittest.main()
