"""
unittest for user_manager
"""

import unittest
import os

class TestConnectToDatabase(unittest.TestCase):
    # TODO: Write here db to database to users
    path_db = "C:\\reps\\SQL-PyQt6-Application\\app\\database_accounts\\data_users.db"

    def test_exist(self):
        self.assertTrue(os.path.exists(self.path_db))

    def test_invalid(self):
        path_db_invalid = "C:\\fff"
        with self.assertRaises(FileNotFoundError):
            open(path_db_invalid)


if __name__ == "__main__":
    unittest.main()