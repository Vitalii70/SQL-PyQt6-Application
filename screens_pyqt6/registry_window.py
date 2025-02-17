# PyQt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, \
    QMessageBox

# Extra library
from database import check_of_users, check_of_password

class RegistryScreen(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()
        self.stacked_windows = stacked_windows

        # main layout for screen
        main_layout = QVBoxLayout(self)

        # Container for button etc.
        self.container = QWidget(self)
        self.container.setFixedSize(350, 450)
        self.container.setStyleSheet("background-color: gray; border-radius: 15px;")

        # layout for things in container
        self.vertical_layout = QVBoxLayout(self.container)

        # main text in this screen
        label_main_text = QLabel("SQL & PyQt6")
        label_main_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_main_text.setStyleSheet("font-size: 35px; font-weight: bold; color: white;")
        self.vertical_layout.addWidget(label_main_text, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create a vertical layout for "Username", "Password", and "Confirm Password"
        username_password_layout = QVBoxLayout()

        # LineEdit "Username"
        self.name_lineedit = QLineEdit()
        self.name_lineedit.setPlaceholderText("Username")
        self.name_lineedit.setStyleSheet(
            "background-color: darkgray; color: white; border-radius: 10px; "
            "font-size: 16px; font-weight: bold; min-height: 40px;")
        self.name_lineedit.setFixedSize(250, 40)
        username_password_layout.addWidget(self.name_lineedit, alignment=Qt.AlignmentFlag.AlignCenter)

        username_password_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # LineEdit "Password"
        self.password_line_edit_1 = QLineEdit()
        self.password_line_edit_1.setPlaceholderText("Password")
        self.password_line_edit_1.setStyleSheet(
            "background-color: darkgray; color: white; border-radius: 10px; "
            "font-size: 16px; font-weight: bold; min-height: 40px;")
        self.password_line_edit_1.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit_1.setFixedSize(250, 40)
        username_password_layout.addWidget(self.password_line_edit_1, alignment=Qt.AlignmentFlag.AlignCenter)

        username_password_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # LineEdit "Confirm Password"
        self.password_line_edit_2 = QLineEdit()
        self.password_line_edit_2.setPlaceholderText("Confirm Password")
        self.password_line_edit_2.setStyleSheet(
            "background-color: darkgray; color: white; border-radius: 10px; "
            "font-size: 16px; font-weight: bold; min-height: 40px;")
        self.password_line_edit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_line_edit_2.setFixedSize(250, 40)
        username_password_layout.addWidget(self.password_line_edit_2, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add the username_password_layout into the vertical_layout
        self.vertical_layout.addLayout(username_password_layout)

        self.vertical_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Button "Continue"
        self.button_continue = QPushButton("Continue")
        self.button_continue.setStyleSheet(
            "background-color: #E4E6EE; color: gray; border-radius: 10px; "
            "font-size: 15px; font-weight: bold; min-height: 30px;")
        self.button_continue.pressed.connect(lambda: self.button_continue.setStyleSheet(
            "background-color: #D0D3DD; color: gray; border-radius: 10px; font-size: 15px; font-weight: bold; min-height: 30px;"
        ))
        self.button_continue.released.connect(lambda: self.button_continue.setStyleSheet(
            "background-color: #E4E6EE; color: gray; border-radius: 10px; font-size: 15px; font-weight: bold; min-height: 30px;"
        ))
        self.button_continue.clicked.connect(self.control_data_source_user)
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

    def control_data_source_user(self):
        username = self.name_lineedit.text()
        password_1 = self.password_line_edit_1.text()
        password_2 = self.password_line_edit_2.text()

        if not check_of_users(username):
            self.show_error_message("Wrong Name!", "Try again to write your name.")
        else:
            if password_1 != password_2:
                self.show_error_message("Wrong password's", "Password's must be same.")
            else:
                # TODO
                if len(password_1) < 0:
                    pass


    def create_new_acc_in_database(self):
        pass

    def error_about_not_exist_option(self):
        self.show_error_message("Soon...", "This option don't work right now.")

    # Function for error message
    @staticmethod
    def show_error_message(title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
