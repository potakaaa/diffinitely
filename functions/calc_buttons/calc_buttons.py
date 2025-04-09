from helper.input_checker import InputChecker

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

    def add_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "+")

    def subtract_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "-")

    def multiply_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "*")

    def divide_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "/")

    def equals_button_clicked(self):
        # TODO: Implement equals button
        pass

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
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit

    def del_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def clear_button_clicked(self):
        self.lineEdit.setText("")

    








