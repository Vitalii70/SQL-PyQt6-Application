# PyQt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

# It is only example, for this screen


class RegistryScreen(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()

        self.stacked_windows = stacked_windows

        self.main_screen_layout = QVBoxLayout()

        self.buttons_layout = QVBoxLayout()

        self.button_1 = QPushButton("Already have an account?")
        self.button_1.setFixedSize(250, 80)
        self.button_1.clicked.connect(
            lambda: self.stacked_windows.setCurrentIndex(0))

        self.buttons_layout.addWidget(
            self.button_1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_screen_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_screen_layout)
