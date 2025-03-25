"""
Module for handling user registration functionality.

This module handles the process of user registration, including form validation and saving new user data to the database.
"""

# PyQt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QHBoxLayout,
                             QLineEdit, QPushButton, QSpacerItem, QSizePolicy)

# Check password, username and error_message
from ..database_logic.user_manager import datamanager
from ..database_logic.database import create_new_account
from ..config import QQS_LOGIN_GUI, show_error_message


class RegistryScreen(QWidget):
    def __init__(self, main_window, stacked_windows):
        super().__init__()
        self.main_window = main_window
        self.stacked_windows = stacked_windows

        # QSS for buttons etc.
        with open(QQS_LOGIN_GUI, "r") as file:
            qss = file.read()
            self.setStyleSheet(qss)

        # main layout for screen
        main_layout = QVBoxLayout(self)

        # Container for button etc.
        self.container = QWidget(self)
        self.container.setFixedSize(350, 450)
        self.container.setObjectName("back_front_container")

        # layout for things in container
        self.vertical_layout = QVBoxLayout(self.container)

        # main text in this screen
        label_main_text = QLabel("SQL & PyQt6")
        label_main_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_main_text.setObjectName("label_main_text")
        self.vertical_layout.addWidget(label_main_text, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create a vertical layout for "Username", "Password", and "Confirm Password"
        username_password_layout = QVBoxLayout()

        # LineEdit "Username"
        self.name_lineedit = QLineEdit()
        self.name_lineedit.setPlaceholderText("Username")
        self.name_lineedit.setObjectName("lineedit_password_name")
        self.name_lineedit.setFixedSize(250, 40)
        username_password_layout.addWidget(self.name_lineedit, alignment=Qt.AlignmentFlag.AlignCenter)

        username_password_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # LineEdit "Password"
        self.password_line_edit_1 = QLineEdit()
        self.password_line_edit_1.setPlaceholderText("Password")
        self.password_line_edit_1.setObjectName("lineedit_password_name")
        self.password_line_edit_1.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit_1.setFixedSize(250, 40)
        username_password_layout.addWidget(self.password_line_edit_1, alignment=Qt.AlignmentFlag.AlignCenter)

        username_password_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # LineEdit "Confirm Password"
        self.password_line_edit_2 = QLineEdit()
        self.password_line_edit_2.setPlaceholderText("Confirm Password")
        self.password_line_edit_2.setObjectName("lineedit_password_name")
        self.password_line_edit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit_2.setFixedSize(250, 40)
        username_password_layout.addWidget(self.password_line_edit_2, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add the username_password_layout into the vertical_layout
        self.vertical_layout.addLayout(username_password_layout)

        self.vertical_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Button "Continue"
        self.button_continue = QPushButton("Continue")
        self.button_continue.setObjectName("lineedit_password_name")
        self.button_continue.pressed.connect(lambda: self.button_continue.setStyleSheet(
            "background-color: #D0D3DD; color: gray; border-radius: 10px; font-size: 16px; "
            "font-weight: bold; min-height: 40px;"))
        self.button_continue.released.connect(lambda: self.button_continue.setStyleSheet(
            "background-color: darkgray; color: white; border-radius: 10px; font-size: 16px; "
            "font-weight: bold; min-height: 40px;"))
        self.button_continue.clicked.connect(self.control_data_source_user_and_create_acc)
        self.button_continue.setFixedSize(200, 40)
        self.vertical_layout.addWidget(self.button_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        # Extra layout for other button
        self.extra_buttons_layout = QHBoxLayout()

        # Button "I have already an account"
        self.button_already_account = QPushButton("I have already an account")
        self.button_already_account.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;")
        self.button_already_account.pressed.connect(lambda: self.button_already_account.setStyleSheet(
            "background-color: transparent; color: gray; font-size: 12px;"
        ))
        self.button_already_account.released.connect(lambda: self.button_already_account.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;"
        ))
        # If acc already exist than login_screen
        self.button_already_account.clicked.connect(lambda: self.stacked_windows.setCurrentIndex(0))
        self.extra_buttons_layout.addWidget(self.button_already_account, alignment=Qt.AlignmentFlag.AlignLeft)


        # Add buttons in main layout
        self.vertical_layout.addLayout(self.extra_buttons_layout)

        # Settings for main layout
        main_layout.addStretch()
        main_layout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)

    # Checking data from user if it is right, create table
    def control_data_source_user_and_create_acc(self):
        username = self.name_lineedit.text()
        password_1 = self.password_line_edit_1.text()
        password_2 = self.password_line_edit_2.text()

        if not datamanager.check_name(username):
            show_error_message("Wrong Name!", "Try again to write your name.")
        else:
            if not datamanager.check_password(password_1, password_2):
                show_error_message("Wrong password!", "Try again to write your password.")
            else:
                create_new_account(username, password_1)
                self.main_window.setWindowTitle(f"SQL & PyQt > {username}")
                self.stacked_windows.setCurrentIndex(2)
