"""
Module for validating username and password input.

This module handles the validation of user credentials,
ensuring that the username and password meet required format
and security criteria before proceeding with authentication.
"""

import re


class DataManager:
    def __init__(self):
        self.user = {}

    @staticmethod
    def check_name(username: str) -> bool:
        """Checking if the name has been entered correctly"""
        # name must be 6-32 varchar
        if username is None:
            return False

        if 4 > len(username) or len(username) > 32:
            return False

        # Look only latin symbols, without numbers and others symbols
        if not re.match("^[a-zA-Z]+$", username):
            return False

        return True

    @staticmethod
    def check_password(password1: str, password2: str) -> bool:
        """Checking if the password has been entered correctly"""
        if not password1 or not password2:
            return False

        if password1 != password2:
            return False

        # Regular expression for the password:
        # at least one lowercase letter,one uppercase letter, one number, and one special character
        right_form = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>_$])[A-Za-z\d!@#$%^&*(),.?\":{}|<>_$]{8,}$"

        # If the password does not match the regular expression
        if not re.fullmatch(right_form, password1):
            return False

        return True

datamanager = DataManager()
