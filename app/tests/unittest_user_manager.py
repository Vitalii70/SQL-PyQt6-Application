"""unittest for user_manager"""

import unittest
from ..logic.user_manager import datamanager

class TestNamesOptions(unittest.TestCase):
    def test_cyrillic(self):
        self.assertTrue(datamanager.check_name("Vitall"))
        self.assertFalse(datamanager.check_name("Vitaliiээ"))
        self.assertFalse(datamanager.check_name("Вtaliй"))
        self.assertFalse(datamanager.check_name("Vitфlii"))

    def test_same_name(self):
        self.assertFalse(datamanager.check_name("Vitalii"))
        self.assertFalse(datamanager.check_name("Roman"))

    def test_number_in_name(self):
        self.assertFalse(datamanager.check_name("V1talii"))
        self.assertFalse(datamanager.check_name("Band4Band"))
        self.assertFalse(datamanager.check_name("6"))
        self.assertFalse(datamanager.check_name("123456"))
        self.assertTrue(datamanager.check_name("Antonn"))

    def test_other_symbols_in_name(self):
        self.assertFalse(datamanager.check_name("Vitalii_"))
        self.assertTrue(datamanager.check_name("Andrei"))
        self.assertFalse(datamanager.check_name("!_"))
        self.assertFalse(datamanager.check_name("Name!Ö"))
        self.assertFalse(datamanager.check_name("N____"))

    def test_long_name(self):
        self.assertFalse(datamanager.check_name("And" * 15))
        self.assertFalse(datamanager.check_name("Bf"))
        self.assertTrue(datamanager.check_name("Andrei"))



