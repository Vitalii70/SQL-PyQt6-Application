"""
Module for validating username and password input.

This module handles the validation of user credentials, ensuring that the username and password meet required format and security criteria before proceeding with authentication.
"""

import re


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
        if not re.match("^[a-zA-Z]+$", username):
            return False

        return True

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
