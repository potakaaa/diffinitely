from utils.safe_input_validator import safe_input_validator
from utils.result_markup import result_markup
import sympy as sp
from PySide6.QtWidgets import QMessageBox

class OperatorButtons:
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit
        self.x = sp.symbols('x')

    def add_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "+")

    def subtract_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "-")

    def multiply_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "*")

    def divide_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "/")

    def equals_button_clicked(self, n_value_edit, deriv_1, deriv_2, n_deriv, integral):
        n_value = 1 if n_value_edit.text() == "" else int(n_value_edit.text())
        
        try:
            safe_input = safe_input_validator(self.lineEdit.text())
            first_derivative = sp.diff(safe_input, self.x)
            second_derivative = sp.diff(first_derivative, self.x)
            nth_derivative = sp.diff(safe_input, self.x, n_value)
            integral_result = sp.integrate(safe_input, self.x)

            deriv_1.setText(result_markup(str(first_derivative)))
            deriv_2.setText(result_markup(str(second_derivative)))
            n_deriv.setText(result_markup(str(nth_derivative)))
            integral.setText(result_markup(str(integral_result)))
        
        except Exception as e:
            QMessageBox.critical(None, "Input Error", "Error evaluating operation. Please fix your input!")