class NumberButtons:
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit

    def zero_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "0")

    def one_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "1")

    def two_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "2")

    def three_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "3")

    def four_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "4")

    def five_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "5")

    def six_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "6")

    def seven_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "7")

    def eight_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "8")

    def nine_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "9")

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







