from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class RegistryScreen(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()

        self.stacked_windows = stacked_windows  # Доступ к QStackedWidget

        # Основной Layout
        self.main_screen_layout = QVBoxLayout()

        # Layout для кнопки
        self.buttons_layout = QVBoxLayout()

        # Button 1
        self.button_1 = QPushButton("Already have an account?")
        self.button_1.setFixedSize(250, 80)
        self.button_1.clicked.connect(lambda: self.stacked_windows.setCurrentIndex(0))

        # Добавляем кнопку в layout
        self.buttons_layout.addWidget(self.button_1, alignment=Qt.AlignmentFlag.AlignCenter)

        # Добавляем все layouts в основной
        self.main_screen_layout.addLayout(self.buttons_layout)

        # Устанавливаем layout на экран (ОБЯЗАТЕЛЬНО!)
        self.setLayout(self.main_screen_layout)
