"""Module for correct spelling username and password"""

import sqlite3
import re
import os


class DataManager:
    def __init__(self):
        self.user = {}

    @staticmethod
    def check_name(username: str) -> bool:
        """Checking if the name has been entered correctly"""
        # name must be 6-32 varchar
        if 4 > len(username) or len(username) > 32:
            return False

        # Look only latin symbols, without numbers and others symbols
        if not re.fullmatch(r"^[a-zA-Z]+$", username):
            return False

        # Connect to db
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "../..", "v1_database/data_users.db")
        conn = None

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # If name in db
            query = "SELECT name FROM datausers WHERE name = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            # if this name already exist than false
            if result:
                return False
            return True

        except sqlite3.Error:
            return False # If error with db too false
        finally:
            conn.close()

    @staticmethod
    def check_password(password1, password2):
        if password1 is None or password2 is None:
            return False

        if password1 != password2:
            return False

        right_form = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>_$])[A-Za-z\d!@#$%^&*(),.?\":{}|<>_$]{8,}$"
        # Look only latin symbols, without numbers and others symbols
        if not re.fullmatch(right_form, password1):
            return False

        return True

datamanager = DataManager()
