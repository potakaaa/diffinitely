from PySide6.QtWidgets import QWidget
from ui.definite_widget import Ui_DefiniteIntegralInput

class DefiniteIntegralWidget(QWidget, Ui_DefiniteIntegralInput):
    def __init__(self, input_edit):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Definite Integral Limits")

        self.input_edit = input_edit
        self.a_value = None
        self.b_value = None

        self.a_value_edit.textChanged.connect(self.update_a_value)
        self.b_value_edit.textChanged.connect(self.update_b_value)

    def update_a_value(self):
        try:
            self.a_value = float(self.a_value_edit.text())
        except ValueError:
            self.a_value = None

    def update_b_value(self):
        try:
            self.b_value = float(self.b_value_edit.text())
        except ValueError:
            self.b_value = None
    
    def get_a_value(self):
        try:
            return float(self.a_value_edit.text())
        except ValueError:
            return 0  # or None or whatever fallback you want

    def get_b_value(self):
        try:
            return float(self.b_value_edit.text())
        except ValueError:
            return 1  # or None or whatever fallback you want