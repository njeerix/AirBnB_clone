#!/usr/bin/python3

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cmd = HBNBCommand()

    def tearDown(self):
        storage.delete_all()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.cmd.onecmd("create BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        new = BaseModel()
        new.save()
        self.cmd.onecmd("show BaseModel {}".format(new.id))
        self.assertIn(new.__str__(), mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        new = BaseModel()
        new.save()
        self.cmd.onecmd("destroy BseModel {}".format(new.id))
        self.assertNotIn(new.__str__(), mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.cmd.onecmd("create BaseModel")
        self.cmd.onecmd("create User")
        self.cmd.onecmd("create State")
        self.cmd.onecmd("create City")
        self.cmd.onecmd("all")
        self.assertIn("BaseModel", mock_stdout.getvalue().strip())
        self.assertIn("User", mock_stdout.getvalue().strip())
        self.assertIn("State", mock_stdout.getvalue().strip())
        self.assertIn("City", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        new = BaseModel()
        new.save()
        self.cmd.onecmd("update BaseModel {} name \"test\"".format(new.id))
        self.assertIn("test", new.name)

if __name__ == '__main__':
    unittest.main()
