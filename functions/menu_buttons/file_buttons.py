import json, os
from PySide6.QtWidgets import QFileDialog, QMessageBox

class FileButtons:
    def __init__(self, ui):
        self.ui = ui

    def new_file(self):
        self.ui.close()
        self.ui.input_edit.setText("")
        self.ui.n_value_edit.setText("")
        self.ui.derivative_1st_edit.setText("")
        self.ui.derivative_2nd_edit.setText("")
        self.ui.nth_derivative_edit.setText("")
        self.ui.integral_edit.setText("")
        self.ui.show()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self.ui, "Open File", "", "JSON Files (*.json);;All Files (*)")

        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.ui.input_edit.setText(data.get("input", ""))
                self.ui.n_value_edit.setText(data.get("n_value", ""))
                self.ui.derivative_1st_edit.setText(data.get("first_derivative", ""))
                self.ui.derivative_2nd_edit.setText(data.get("second_derivative", ""))
                self.ui.nth_derivative_edit.setText(data.get("nth_derivative", ""))
                self.ui.integral_edit.setText(data.get("integral", ""))
            except Exception as e:
                QMessageBox.critical(self.ui, "Error", f"Failed to open file: {e}")

    def save_file(self):
        data = {
            "input": self.ui.input_edit.text(),
            "n_value": self.ui.n_value_edit.text(),
            "first_derivative": self.ui.derivative_1st_edit.text(),
            "second_derivative": self.ui.derivative_2nd_edit.text(),
            "nth_derivative": self.ui.nth_derivative_edit.text(),
            "integral": self.ui.integral_edit.text()
        }

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "diffinitely_file.json")

        path, _ = QFileDialog.getSaveFileName(self.ui, "Save File", downloads_path, "JSON Files (*.json);;All Files (*)")

        if path:
            try:
                with open(path, 'w', encoding="utf-8") as file:
                    json.dump(data, file)
            except Exception as e:
                QMessageBox.critical(self.ui, "Error", f"Failed to save file: {e}")

    def exit_app(self):
        self.ui.close()