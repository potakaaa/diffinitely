from widgets.definite_input import DefiniteIntegralWidget
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
    
    def definite_integral_button_clicked(self):
        self.defIntegral = DefiniteIntegralWidget(self.lineEdit)
        self.defIntegral.show()
