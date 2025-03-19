"""
unittest for user_manager
"""

import unittest
from app.database_logic.user_manager import datamanager

class TestNamesOptions(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(datamanager.check_name("Vitaliie"))
        self.assertTrue(datamanager.check_name("Andrei"))
        self.assertTrue(datamanager.check_name("Katei"))
        self.assertTrue(datamanager.check_name("Luca"))

    def test_invalid_typeerror(self):
        with self.assertRaises(TypeError):
            datamanager.check_name()

    def test_invalid(self):
        self.assertFalse(datamanager.check_name("das"))
        self.assertFalse(datamanager.check_name("five" * 10)) # 50 > symbols
        self.assertFalse(datamanager.check_name("------"))
        self.assertFalse(datamanager.check_name("!RatherBoy1"))
        self.assertFalse(datamanager.check_name("12345678890"))


class TestPasswordsOptions(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(datamanager.check_password("Va_123$ghtjfk", "Va_123$ghtjfk"))
        self.assertTrue(datamanager.check_password("Va_123$ghtjf45k", "Va_123$ghtjf45k"))

    def test_invalid_typeerror(self):
        with self.assertRaises(TypeError):
            datamanager.check_password()

    def test_invalid(self):
        self.assertFalse(datamanager.check_password("Va_123$ghtjfkas", "Va_123$ghtjfk"))
        self.assertFalse(datamanager.check_password("Va_", "Va_"))
        self.assertFalse(datamanager.check_password("________________", "________________"))
        self.assertFalse(datamanager.check_password("1234567890", "1234567890"))

if __name__ == "__main__":
    unittest.main()