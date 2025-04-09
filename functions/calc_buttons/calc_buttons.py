from helper.input_checker import InputChecker
from utils.safe_input_validator import safe_input_validator
import sympy as sp

class NumberButtons:
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit
        self.input_checker = InputChecker(self.lineEdit)

    def _add_number(self, number):
        if self.input_checker.isNextInputValid():
            self.lineEdit.setText(self.lineEdit.text() + str(number))

    def zero_button_clicked(self):
        self._add_number(0)

    def one_button_clicked(self):
        self._add_number(1)

    def two_button_clicked(self):
        self._add_number(2)

    def three_button_clicked(self):
        self._add_number(3)

    def four_button_clicked(self):
        self._add_number(4)

    def five_button_clicked(self):
        self._add_number(5)

    def six_button_clicked(self):
        self._add_number(6)

    def seven_button_clicked(self):
        self._add_number(7)

    def eight_button_clicked(self):
        self._add_number(8)

    def nine_button_clicked(self):
        self._add_number(9)

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
        
        safe_input = safe_input_validator(self.lineEdit.text())
        first_derivative = sp.diff(safe_input, self.x)
        second_derivative = sp.diff(first_derivative, self.x)
        nth_derivative = sp.diff(safe_input, self.x, n_value)
        integral_result = sp.integrate(safe_input, self.x)

        deriv_1.setText(str(first_derivative))
        deriv_2.setText(str(second_derivative))
        n_deriv.setText(str(nth_derivative))
        integral.setText(str(integral_result))


class SpecialButtons:
    # idk unsay tawag ani, kana nalang "special buttons" :D
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit

    def x_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "x")

    def y_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "y")

    def a_squared_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "^2")

    def a_power_b_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "^")

    def open_parenthesis_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "(")

    def close_parenthesis_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + ")")

    def less_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "<")

    def greater_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + ">")

    def less_equal_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "<=")

    def greater_equal_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + ">=")

    def factorial_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "!")
        
    def x_fact_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "x!")

    def percent_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "%")

    def sqrt_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "√")

    def pi_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "π")

    def apostrophe_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "'")

class OtherButtons:
    def __init__(self, lineEdit, n_value_edit, deriv_1, deriv_2, n_deriv, integral):
        self.lineEdit = lineEdit
        self.deriv_1 = deriv_1
        self.deriv_2 = deriv_2
        self.n_deriv = n_deriv
        self.integral = integral

    def del_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def clear_button_clicked(self):
        self.lineEdit.setText("")
        self.deriv_1.setText("")
        self.deriv_2.setText("")
        self.n_deriv.setText("")
        self.integral.setText("")
        self.n_value_edit.setText("")

    








