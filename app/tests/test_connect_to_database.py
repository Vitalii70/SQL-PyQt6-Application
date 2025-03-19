"""
unittest for user_manager
"""

import unittest
from ..config import DB_PATH
import os


class TestConnectToDatabase(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(os.path.exists(DB_PATH))

    def test_invalid(self):
        path_db_invalid = "C:\\fff"
        with self.assertRaises(FileNotFoundError):
            open(path_db_invalid)


if __name__ == "__main__":
    unittest.main()