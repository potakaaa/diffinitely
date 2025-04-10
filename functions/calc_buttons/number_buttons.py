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