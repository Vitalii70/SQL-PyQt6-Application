# PyQt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout


class MenuFirstScreen(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()
        self.stacked_windows = stacked_windows
        self.init_ui()

    def init_ui(self):
        """Init UI"""
        self.main_layout = QVBoxLayout()
        self.buttons_layout = QGridLayout()

        # Logo
        label_maintext = QLabel("SQL & PyQt")
        label_maintext.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_maintext.setStyleSheet("font-size: 44px; font-weight: bold;")
        self.main_layout.addWidget(label_maintext)

        # buttons
        buttons = [
            ("Create Table", 0, 0, lambda: self.stacked_windows.setCurrentIndex(3)),
            ("Change Table", 0, 1, self.test_function_for_time),
            ("Insert Data", 0, 2, self.test_function_for_time),
            ("Watch Data/Tables", 0, 3, self.test_function_for_time),
        ]

        for text, row, col, func in buttons:
            self.buttons_layout.addWidget(self.create_button(text, func), row, col)

        # Set layouts
        self.main_layout.addLayout(self.buttons_layout)
        self.setLayout(self.main_layout)

    def create_button(self, text, func):
        """Creating button"""
        btn = QPushButton(text)
        btn.setFixedSize(175, 175)
        btn.clicked.connect(func)
        return btn

    def test_function_for_time(self):
        print("It is working.")
