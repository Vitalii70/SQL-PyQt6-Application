"""
Module for creating a GUI with PyQt6 and working with an SQL database.

This module provides a PyQt6 interface that interacts with an SQL database to execute queries and display data.

Dependencies:
- PyQt6
- SQLite/SQLAlchemy
"""

# PyQt6
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PyQt6.QtGui import QIcon

# Other windows/screens
from app.gui.login_gui import LoginScreen
from app.gui.registration_gui import RegistryScreen
from app.gui.menu_gui import MenuFirstScreen
from app.gui.create_table_gui import ScreenCreateTable

# Extra library
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked_windows = QStackedWidget()

        # Add widget in stacked widget
        self.stacked_windows.addWidget(LoginScreen(self, self.stacked_windows))
        self.stacked_windows.addWidget(RegistryScreen(self, self.stacked_windows))
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
    app.setWindowIcon(QIcon("app/resources/icon_sql.png"))
    app.setWindowIcon(QIcon(ALL_LINKS["icon_for_program"]))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
