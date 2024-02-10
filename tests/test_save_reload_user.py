import unittest
from models.engine.file_storage import storage
from models.user import User

class TestSaveReloadUser(unittest.TestCase):
    def test_save_and_reload_user(self):
        initial_count = len(storage.all())
        user = User()
        user.save()
        count_after_save = len(storage.all())
        self.assertEqual(count_after_save, initial_count + 1)

        obj_id = user.id
        del user

        reloaded_user = storage.reload(obj_id)
        self.assertIsNotNone(reloaded_user)
        self.assertIsInstance(reloaded_user, User)

if __name__ == "__main__":
    unittest.main()
