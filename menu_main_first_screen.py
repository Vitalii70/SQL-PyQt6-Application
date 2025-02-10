from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout


class MenuFirstScreen(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()
        self.stacked_windows = stacked_windows


        self.screen_first_layout = QVBoxLayout()
        self.buttons_layout = QGridLayout()

        self.label_maintext = QLabel("SQL & PyQt")
        self.label_maintext.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_maintext.setStyleSheet("font-size: 44px; font-weight: bold;")
        self.screen_first_layout.addWidget(self.label_maintext)

        # Кнопки
        self.screen_first_button_create_table = QPushButton("Create Table")
        self.screen_first_button_create_table.setFixedSize(175, 175)
        self.screen_first_button_create_table.clicked.connect(lambda: self.stacked_windows.setCurrentIndex(3))
        self.buttons_layout.addWidget(self.screen_first_button_create_table, 0, 0)

        self.screen_first_button_changebd = QPushButton("Change Table")
        self.screen_first_button_changebd.setFixedSize(175, 175)
        self.screen_first_button_changebd.clicked.connect(self.test_function_for_time)
        self.buttons_layout.addWidget(self.screen_first_button_changebd, 0, 1)

        self.screen_first_button_removebd = QPushButton("Insert data")
        self.screen_first_button_removebd.setFixedSize(175, 175)
        self.screen_first_button_removebd.clicked.connect(self.test_function_for_time)
        self.buttons_layout.addWidget(self.screen_first_button_removebd, 0, 2)

        self.screen_first_button_addchange = QPushButton("Watch data/Tables")
        self.screen_first_button_addchange.setFixedSize(175, 175)
        self.screen_first_button_addchange.clicked.connect(self.test_function_for_time)
        self.buttons_layout.addWidget(self.screen_first_button_addchange, 0, 3)

        self.screen_first_layout.addLayout(self.buttons_layout)

        self.setLayout(self.screen_first_layout)

        self.stacked_windows.setCurrentIndex(2)


    def test_function_for_time(self):
        print("It is working.")
