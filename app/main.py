"""
Module for creating a GUI with PyQt6 and working with an SQL database.

This module provides a PyQt6 interface that interacts with an SQL database to execute queries and display data.

Dependencies:
- PyQt6
- SQLite/SQLAlchemy
"""

# PyQt6
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QMessageBox
from PyQt6.QtGui import QIcon

# Other windows/screens
from app.gui.login_gui import LoginScreen
from app.gui.registration_gui import RegistryScreen
from app.gui.menu_gui import MenuFirstScreen
from app.gui.create_table_gui import ScreenCreateTable

# Extra libraries
import sys
import os
from config import WINDOW_ICON


class MainWindow(QMainWindow):
    """Main window that manages navigation between screens using QStackedWidget."""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked_windows = QStackedWidget()
        self.register_screens()

        self.setWindowTitle("SQL & PyQt")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(self.stacked_windows)

        # Set the first screen
        self.stacked_windows.setCurrentIndex(0)

    def register_screens(self):
        """Register all screens in QStackedWidget."""
        screens = [
            LoginScreen(self, self.stacked_windows),
            RegistryScreen(self, self.stacked_windows),
            MenuFirstScreen(self.stacked_windows),
            ScreenCreateTable(self.stacked_windows),
        ]

        for screen in screens:
            self.stacked_windows.addWidget(screen)


def exception_hook(exc_type, exc_value, exc_traceback):
    """Handle uncaught exceptions and show an error message."""
    error_msg = f"An unexpected error occurred:\n{exc_value}"
    print(error_msg)
    QMessageBox.critical(None, "Application Error", error_msg)

    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    sys.exit(1)


def main():
    """Main function to start the PyQt application."""
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)

    # Ensure the icon path is correct
    icon_path = os.path.abspath(WINDOW_ICON)
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    else:
        print(f"Warning: Icon not found at {icon_path}")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
