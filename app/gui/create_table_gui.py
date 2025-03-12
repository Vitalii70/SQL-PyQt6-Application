from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QCheckBox, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QMessageBox)

# Extra library
from app.database_logic.database import create_table


class ScreenCreateTable(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()
        self.stacked_windows = stacked_windows

        self.columns_data = []
        self.column_count = 1

        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()
        self.table_name_layout = QHBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.columns_layout = QVBoxLayout()

        self.table_name_input = QLineEdit()
        self.table_name_input.setPlaceholderText("Enter table name")
        self.table_name_input.setFixedSize(275, 60)
        self.table_name_layout.addWidget(self.table_name_input, alignment=Qt.AlignmentFlag.AlignLeft)

        self.add_column()

        self.btn_add_column = self.create_button("Add Column", self.add_column)
        self.btn_delete_column = self.create_button("Delete Column", self.delete_column)
        self.btn_save_table = self.create_button("Save", self.saving_table)

        self.buttons_layout.addWidget(self.btn_add_column)
        self.buttons_layout.addWidget(self.btn_delete_column)
        self.buttons_layout.addWidget(self.btn_save_table, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttons_layout.setSpacing(40)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_layout.addLayout(self.table_name_layout)
        self.main_layout.addLayout(self.columns_layout)
        self.main_layout.addItem(spacer)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)

    def create_button(self, text, func):
        button = QPushButton(text)
        button.setMinimumSize(125, 70)
        button.clicked.connect(func)
        return button

    def show_error_message(self, title, message):
        QMessageBox.critical(self, title, message, QMessageBox.StandardButton.Ok)

    def saving_table(self):
        name = self.table_name_input.text()
        if not name:
            self.show_error_message("Error", "Table name cannot be empty.")
            return

        columns = []
        for column in self.columns_data:
            column_name = column["name"].text()
            column_type = column["type"].currentText()
            column_pk = column["PRIMARY KEY"].isChecked()
            column_nn = column["NOT NULL"].isChecked()

            if not column_name:
                self.show_error_message("Error", "Column name cannot be empty.")
                return

            columns.append({
                "name": column_name,
                "type": column_type,
                "PRIMARY KEY": column_pk,
                "NOT NULL": column_nn
            })

        create_table(name, columns)

    def add_column(self):
        column_layout = self.create_column_widgets()
        self.columns_layout.addLayout(column_layout)
        self.column_count += 1

    def delete_column(self):
        if self.column_count > 2:
            column_layout = self.columns_layout.itemAt(self.column_count - 2)

            if column_layout:
                for i in range(column_layout.count()):
                    widget = column_layout.itemAt(i).widget()
                    if widget:
                        widget.deleteLater()

                self.columns_layout.removeItem(column_layout)
                self.columns_data.pop()
                self.column_count -= 1
        else:
            self.show_error_message(
                "Error deleting column.",
                "Cannot delete the last column."
            )

    def create_column_widgets(self):
        column_layout = QHBoxLayout()

        column_name = QLineEdit()
        column_name.setPlaceholderText(f"Enter column name {self.column_count}")
        column_layout.addWidget(column_name)

        column_type = QComboBox()
        column_type.addItems(["INTEGER", "FLOAT", "TEXT"])
        column_layout.addWidget(column_type)

        column_pk = QCheckBox("PK")
        column_nn = QCheckBox("NN")
        column_layout.addWidget(column_pk)
        column_layout.addWidget(column_nn)

        self.columns_data.append({
            "name": column_name,
            "type": column_type,
            "PRIMARY KEY": column_pk,
            "NOT NULL": column_nn
        })

        return column_layout
