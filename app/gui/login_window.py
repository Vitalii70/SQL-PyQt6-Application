# PyQt6:
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QPushButton, QLabel, QLineEdit, QMessageBox

# Extra library
from app.logic.database import control_data


class LoginScreen(QWidget):
    def __init__(self, main_window, stacked_windows):
        super().__init__()

        # Default settings
        self.main_window = main_window
        self.stacked_windows = stacked_windows
        self.setWindowTitle("SQL & PyQt")
        self.setGeometry(100, 100, 800, 600)

        # Main layout with other layouts
        self.main_screen_layout = QVBoxLayout()

        self.text_layout = QHBoxLayout()
        self.button_1_layout = QVBoxLayout()
        self.button_2_layout = QVBoxLayout()
        self.button_3_layout = QVBoxLayout()
        self.button_dont_acc_layout = QHBoxLayout()

        # Text Name of program
        label_main_text = QLabel("SQL & PyQt")
        label_main_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_main_text.setStyleSheet(
            "font-size: 44px; "
            "font-weight: bold; "
            "color: black;")
        self.text_layout.addWidget(label_main_text,
                                   alignment=Qt.AlignmentFlag.AlignCenter)

        # lineedit for name
        self.name_lineedit = QLineEdit()
        self.name_lineedit.setPlaceholderText("Username")
        self.name_lineedit.setFixedSize(250, 40)
        self.button_1_layout.addWidget(self.name_lineedit,
                                       alignment=Qt.AlignmentFlag.AlignCenter)

        # lineedit for password
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setPlaceholderText("Password")
        # to hide the password when entering
        self.password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_lineedit.setFixedSize(250, 40)
        self.button_1_layout.addWidget(self.password_lineedit,
                                       alignment=Qt.AlignmentFlag.AlignCenter)

        # for better arrangement
        self.button_1_layout.setSpacing(0)
        self.button_1_layout.setContentsMargins(0, 0, 0, 0)

        self.button_3 = QPushButton("Continue >")
        self.button_3.setStyleSheet(
            "background-color: gray; "
            "color: white; "
            "border-radius: 10px; "
            "font: bold 14px; "
            "min-width: 10em; "
            "padding: 6px;"
            "transition: 0.3s; "
            """
            QPushButton:pressed {
                background-color: darkgray; /* Цвет при нажатии */
                color: black;
            }
            """
        )
        self.button_3.setAutoDefault(True)
        self.button_3.setDefault(True)
        self.button_3.setFixedSize(150, 50)
        self.button_3.clicked.connect(self.login_continue)
        self.button_3_layout.addWidget(self.button_3, alignment=Qt.AlignmentFlag.AlignCenter)

        self.button_dont_acc = QPushButton("Create an account")
        self.button_dont_acc.setMinimumSize(175, 75)
        self.button_dont_acc.clicked.connect(
            lambda: self.stacked_windows.setCurrentIndex(1)
        )
        self.button_dont_acc_layout.addWidget(
            self.button_dont_acc,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        # Putting it all together
        self.main_screen_layout.addLayout(self.text_layout)
        self.main_screen_layout.addLayout(self.button_1_layout)
        self.main_screen_layout.addLayout(self.button_2_layout)
        self.main_screen_layout.addLayout(self.button_3_layout)
        self.main_screen_layout.addLayout(self.button_dont_acc_layout)

        self.setLayout(self.main_screen_layout)

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
            self.show_error_message(
                "Incorrect date.",
                "Try again, and make sure you write "
                "your password and username correctly."
            )

    # Function for error message
    @staticmethod
    def show_error_message(title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
