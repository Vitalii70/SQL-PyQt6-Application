# PyQt6
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PyQt6.QtGui import QIcon

# Other windows/screens
from screens_pyqt6.login_window import LoginScreen
from screens_pyqt6.registry_window import RegistryScreen
from screens_pyqt6.menu_main_first_screen import MenuFirstScreen
from screens_pyqt6.screen_create_table import ScreenCreateTable

# Extra liblary
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked_windows = QStackedWidget()

        # Add widget in stacked widget
        self.stacked_windows.addWidget(LoginScreen(self, self.stacked_windows))
        self.stacked_windows.addWidget(RegistryScreen(self.stacked_windows))
        self.stacked_windows.addWidget(MenuFirstScreen(self.stacked_windows))
        self.stacked_windows.addWidget(ScreenCreateTable(self.stacked_windows))

        self.setWindowTitle("SQL & PyQt")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_windows.setCurrentIndex(0)

        # Set widget how central widget
        self.setCentralWidget(self.stacked_windows)


# Function for error
def exception_hook(exc_type, exc_value, exc_traceback):
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    sys.exit(1)


# Startpoint and settings
if __name__ == "__main__":
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ideas/icon_sql.png"))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
