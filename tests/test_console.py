#!/usr/bin/python3
"""
Unit tests for console using Mock from python standard library
"""

import unittest
from console import MyClass
from models.user import User
from models.base_model import BaseModel
from models import storage

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User()
        self.user2 = User()

    def tearDown(self):
        del self.user1
        del sel.user2

    def test_instance_creation(self):
        self.assertIsInstance(self.user1, User)
        self.assertIsInstance(self.user2, User)

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))

    def test_all_method(self):
        user3 = User()
        user4 = User()
        all_users = User.all()
        self.assertEqual(len(all_users), 4)
        del user3
        del user4

    def test_count_method(self):
        user5 = User()
        user6 = User()
        count = User.count()
        self.assertEqual(count, 6)
        del user5
        del user6

if __name__ == '__main__':
    unittest.main()
