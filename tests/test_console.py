import unittest
from unittest.mock import MagicMock
from models.engine.file_storage import storage
from console import HBNBCommand

class TestUser(unittest.TestCase):
    def test_all_method(self):
        all_users = {'user1': 'details1', 'user2': 'detatils2'}
        storage.all = MagicMock(return_value=all_users)
        command = HBNBCommand()
        self.assertIsInstance(command.do_all('User'), dict)

    def test_count_method(self):
        mock_storage_count = MagicMock(return_value = 0)
        count = storage.count(User)
        self.assertIsInstance(count, int)

if __name__ == '__main__':
    unittest.main()
