# PyQt6:
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLabel, \
    QApplication, QGridLayout, QTextEdit, QCheckBox, QLineEdit, QStackedLayout, QComboBox, QSpinBox, QSpacerItem, \
    QSizePolicy, QMessageBox
from PyQt6.QtGui import QIcon

# Extra liblary
from database import create_table


class ScreenCreateTable(QWidget):
    def __init__(self, stacked_windows):
        super().__init__()
        self.stacked_windows = stacked_windows

        self.columns_data = []
        self.column_count = 0

        self.parentLayout = QVBoxLayout()

        self.name_of_table_layout = QHBoxLayout()
        self.buttons_layout = QHBoxLayout()
        self.columns_layout = QVBoxLayout()

        # LineEdit "enter table name"
        self.line_text = QLineEdit()
        self.line_text.setPlaceholderText("Enter table name")
        self.line_text.setFixedSize(275, 60)
        self.name_of_table_layout.addWidget(self.line_text, alignment=Qt.AlignmentFlag.AlignLeft)

        # Das, um dann weiter die columns auszulesen
        self.column_count = 1
        self.add_column()

        # Plazieren Knöpfen runter
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # Button add_column
        self.button_add_spalte = QPushButton("Add Column")
        self.button_add_spalte.setMinimumSize(125, 70)
        self.button_add_spalte.clicked.connect(self.add_column)
        self.buttons_layout.addWidget(self.button_add_spalte)

        # Button del_column
        self.button_delete_spalte = QPushButton("Delete Column")
        self.button_delete_spalte.setMinimumSize(125, 70)
        self.button_delete_spalte.clicked.connect(self.delete_column)
        self.buttons_layout.addWidget(self.button_delete_spalte)

        # Button save
        self.button_save_table = QPushButton("Save")
        self.button_save_table.setMinimumSize(125, 70)
        self.button_save_table.pressed.connect(self.saving_table)
        self.buttons_layout.addWidget(self.button_save_table, alignment=Qt.AlignmentFlag.AlignRight)

        self.buttons_layout.setSpacing(40)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        # Die Knöpfen usw. fügen in hauot Layout hinzu
        self.parentLayout.addLayout(self.name_of_table_layout)
        self.parentLayout.addLayout(self.columns_layout)
        self.parentLayout.addItem(spacer)
        self.parentLayout.addLayout(self.buttons_layout)

        # haupt widget table fügen Layout mit anderen Layouts hinzu
        self.setLayout(self.parentLayout)


    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def saving_table(self):
        name = self.line_text.text()
        columns = self.columns_data
        if len(name) == 0:
            self.show_error_message("Error name of table.", "Table name cannot be empty.")
            return

        for column in columns:
            column_name = column["name"].text()
            column_type = column["type"].currentText()
            column_pk = column["PRIMARY KEY"].isChecked()
            column_nn = column["NOT NULL"].isChecked()

            if len(column_name) == 0:
                self.show_error_message("Error name of column.", "Column name cannot be empty.")
                return

        create_table(name, columns)

    def add_column(self):
        row = self.column_count
        second_columns = QHBoxLayout()

        spalte_line = QLineEdit()
        spalte_line.setPlaceholderText(f"Enter column name {self.column_count}")
        second_columns.addWidget(spalte_line)

        combobox_type = QComboBox()
        combobox_type.addItems(["INTEGER", "FLOAT", "TEXT"])
        second_columns.addWidget(combobox_type)

        check_pk = QCheckBox("PK")
        check_nn = QCheckBox("NN")
        second_columns.addWidget(check_pk)
        second_columns.addWidget(check_nn)

        self.columns_data.append({
            "name": spalte_line,
            "type": combobox_type,
            "PRIMARY KEY": check_pk,
            "NOT NULL": check_nn
        })

        self.columns_layout.addLayout(second_columns)
        self.column_count += 1

    def delete_column(self):
        if self.column_count > 2:
            # Kriegen layout lezte column
            last_column_layout = self.columns_layout.itemAt(self.column_count - 2)  # Index lezter column

            if last_column_layout:
                # löschen widget aus layout
                for i in range(last_column_layout.count()):
                    item = last_column_layout.itemAt(i)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()  # deleteLater() - позволяет удалить сылку на виджет

                # Löschen layout aus colums_layout
                self.columns_layout.removeItem(
                    last_column_layout)  # removeItem() - исключает виджет из родительского слоя
                self.columns_data.pop()
                self.column_count -= 1
        else:
            self.show_error_message("Error delete column.", "Cannot delete the last column.")