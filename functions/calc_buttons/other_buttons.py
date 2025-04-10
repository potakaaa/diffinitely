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

    








