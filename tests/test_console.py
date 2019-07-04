#!/usr/bin/python3
"""
Tests for HBNBCommand Class
"""
import os
import unittest
import console
#from models.city import City
#from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test for HBNBCommand Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set HBNBCommand Class
        """
        cls.cli = HBNBCommand()

    @classmethod
    def teardown(cls):
        """
        Delete HBNBCommand Class
        """
        del cls.cli
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_documentation(self):
        """
        Check documentation
        """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_BaseModel.__doc__)
        self.assertIsNotNone(HBNBCommand.do_User.__doc__)
        self.assertIsNotNone(HBNBCommand.do_State.__doc__)
        self.assertIsNotNone(HBNBCommand.do_City.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Amenity.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Place.__doc__)
        self.assertIsNotNone(HBNBCommand.do_Review.__doc__)


    def test_init(self):
        """
        Check objects as instance of HBNBCommand
        """
        self.assertTrue(isinstance(self.cli, HBNBCommand))

if __name__ == "__main__":
    unittest.main()
