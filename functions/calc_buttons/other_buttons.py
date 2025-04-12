from widgets.more_buttons import MoreWidget

class OtherButtons:
    def __init__(self, lineEdit, n_value_edit, deriv_1, deriv_2, n_deriv, integral, ui):
        self.lineEdit = lineEdit
        self.n_value_edit = n_value_edit
        self.deriv_1 = deriv_1
        self.deriv_2 = deriv_2
        self.n_deriv = n_deriv
        self.integral = integral
        self.ui = ui

    def del_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def clear_button_clicked(self):
        self.lineEdit.setText("")
        self.deriv_1.setText("")
        self.deriv_2.setText("")
        self.n_deriv.setText("")
        self.integral.setText("")
        self.n_value_edit.setText("")

    def more_button_clicked(self):
        self.popup = MoreWidget()
        self.popup.show()


    








