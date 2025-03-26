"""
Module for handling user login functionality.

This module provides the logic for user authentication, including input validation and checking credentials against the database.
"""

# PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy

# Extra library (check if data right for database, QQS and error_message)
from app.database_logic.database import control_data
from ..config import QQS_LOGIN_GUI, show_error_message


class LoginScreen(QWidget):
    def __init__(self, main_window, stacked_windows):
        super().__init__()
        # Default settings
        self.main_window = main_window
        self.stacked_windows = stacked_windows

        # QSS for buttons etc.
        with open(QQS_LOGIN_GUI, "r") as file:
            qss = file.read()
            self.setStyleSheet(qss)

        # main layout for screen
        main_layout = QVBoxLayout(self)

        self.setWindowTitle("SQL & PyQt")
        self.setGeometry(100, 100, 800, 600)

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
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setPlaceholderText("Password")
        self.password_lineedit.setObjectName("lineedit_password_name")
        self.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_lineedit.setFixedSize(250, 40)
        username_password_layout.addWidget(self.password_lineedit, alignment=Qt.AlignmentFlag.AlignCenter)

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
        self.button_continue.clicked.connect(self.login_continue)
        self.button_continue.setFixedSize(200, 40)
        self.vertical_layout.addWidget(self.button_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        # Extra layout for other button
        self.extra_buttons_layout = QHBoxLayout()

        # Button "Create an account"
        self.button_already_account = QPushButton("Create an account")
        self.button_already_account.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;")
        self.button_already_account.pressed.connect(lambda: self.button_already_account.setStyleSheet(
            "background-color: transparent; color: gray; font-size: 12px;"
        ))
        self.button_already_account.released.connect(lambda: self.button_already_account.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;"
        ))
        # If acc already exist than login_screen
        self.button_already_account.clicked.connect(lambda: self.stacked_windows.setCurrentIndex(1))
        self.extra_buttons_layout.addWidget(self.button_already_account, alignment=Qt.AlignmentFlag.AlignLeft)

        # Button "I forgot password"
        self.button_forgot_password = QPushButton("I forgot password")
        self.button_forgot_password.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;")
        self.button_forgot_password.pressed.connect(lambda: self.button_forgot_password.setStyleSheet(
            "background-color: transparent; color: gray; font-size: 12px;"
        ))
        self.button_forgot_password.released.connect(lambda: self.button_forgot_password.setStyleSheet(
            "background-color: transparent; color: white; font-size: 12px;"
        ))
        # This option will in future than now is only this
        self.button_forgot_password.clicked.connect(self.error_about_not_exist_option)
        self.extra_buttons_layout.addWidget(self.button_forgot_password, alignment=Qt.AlignmentFlag.AlignRight)

        # Add buttons in main layout
        self.vertical_layout.addLayout(self.extra_buttons_layout)

        # Settings for main layout
        main_layout.addStretch()
        main_layout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch()
        self.setLayout(main_layout)


    # Open program if data from user is correct
    def login_continue(self):
        username = self.name_lineedit.text()
        password = self.password_lineedit.text()

        # Debug switch (test fast this program)
        debug_login = False
        if not debug_login:
            control = control_data(username, password)
        else:
            control = True

        # pass to the program if the data is correct
        if control:
            self.main_window.setWindowTitle(f"SQL & PyQt > {username}")
            self.stacked_windows.setCurrentIndex(2)
        else:
            show_error_message(
                "Incorrect date.",
                "Try again, and make sure you write "
                "your password and username correctly."
            )

    # In next update
    def error_about_not_exist_option(self):
        show_error_message("Soon...", "This option don't work right now.")
