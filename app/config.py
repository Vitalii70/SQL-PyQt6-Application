import os
from PyQt6.QtWidgets import QMessageBox


# --- Database Settings ---
DB_NAME_USERS = "data_users.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", DB_NAME_USERS)

CREATED_DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database\\created_databases")


# --- PyQt6 Settings ---
WINDOW_ICON_NAME = "icon_sql.png"
WINDOW_ICON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", WINDOW_ICON_NAME)


# --- QSS Style ---
QQS_LOGIN_GUI_NAME = "style_login_gui.qss"
QQS_LOGIN_GUI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles", QQS_LOGIN_GUI_NAME)


# --- Python Functions ---
def show_error_message(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()


# --- Check, if PATHS work ---
def check_files():
    files_and_dirs = {
        "Database Path": DB_PATH,
        "Created Databases Folder": CREATED_DB_NAME,
        "Window Icon": WINDOW_ICON,
        "QSS Style File": QQS_LOGIN_GUI,
    }

    for label, path in files_and_dirs.items():
        if os.path.exists(path):
            print(f"{label} exists: {path}")
        else:
            print(f"{label} does not exist: {path}")

# check_files()
