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

    def test_cyrillic_etc(self):
        self.assertFalse(datamanager.check_password("Aqawfas234э", "Aqawfas234э"))
        self.assertFalse(datamanager.check_password("AqawЙfas234", "AqawЙfas234"))
        self.assertFalse(datamanager.check_password("Aqawррfas234э", "Aqawррfas234э"))
        self.assertTrue(datamanager.check_password("Passw0rd!", "Passw0rd!"))
        self.assertTrue(datamanager.check_password("Aq_sr0r!$", "Aq_sr0r!$"))

    def test_long_password(self):
        self.assertFalse(datamanager.check_password("Aw23§", "Aw23§"))
        self.assertFalse(datamanager.check_password("Asd3ed_", "Asd3ed_"))
        self.assertTrue(datamanager.check_password("Passw0rd!", "Passw0rd!"))
        self.assertTrue(datamanager.check_password("Aq_sr0r!$", "Aq_sr0r!$"))
