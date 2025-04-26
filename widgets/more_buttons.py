from PySide6.QtWidgets import QWidget
from ui.more_widget import Ui_MoreFunctions
from functions.calc_buttons.more_buttons_logic import calculate_expression

class MoreWidget(QWidget, Ui_MoreFunctions):
    def __init__(self, input_edit):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("More Buttons")
        
        self.input_edit = input_edit
        self.functions_values = {}

        self.log_button.clicked.connect(self.handle_log)
        self.ln_button.clicked.connect(self.handle_ln)
        self.e_button.clicked.connect(self.handle_e)
        self.sin_button.clicked.connect(self.handle_sin)
        self.cos_button.clicked.connect(self.handle_cos)
        self.tan_button.clicked.connect(self.handle_tan)
        self.csc_button.clicked.connect(self.handle_csc)
        self.sec_button.clicked.connect(self.handle_sec)
        self.cot_button.clicked.connect(self.handle_cot)

    def handle_log(self):
        current_text = self.input_edit.text()
        result = calculate_expression("log(")
        self.input_edit.setText(current_text + "log()")
        self.functions_values["log"] = result

    def handle_ln(self):
        current_text = self.input_edit.text()
        result = calculate_expression("ln(")
        self.input_edit.setText(current_text + "ln()")
        self.functions_values["ln"] = result

    def handle_e(self):
        current_text = self.input_edit.text()
        result = calculate_expression("e")
        self.input_edit.setText(current_text + "e")
        self.functions_values["e"] = result

    def handle_sin(self):
        current_text = self.input_edit.text()
        result = calculate_expression("sin(")
        self.input_edit.setText(current_text + "sin()")
        self.functions_values["sin"] = result

    def handle_cos(self):
        current_text = self.input_edit.text()
        result = calculate_expression("cos(")
        self.input_edit.setText(current_text + "cos()")
        self.functions_values["cos"] = result

    def handle_tan(self):
        current_text = self.input_edit.text()
        result = calculate_expression("tan(")
        self.input_edit.setText(current_text + "tan()")
        self.functions_values["tan"] = result

    def handle_csc(self):
        current_text = self.input_edit.text()
        result = calculate_expression("csc(")
        self.input_edit.setText(current_text + "csc()")
        self.functions_values["csc"] = result

    def handle_sec(self):
        current_text = self.input_edit.text()
        result = calculate_expression("sec(")
        self.input_edit.setText(current_text + "sec()")
        self.functions_values["sec"] = result

    def handle_cot(self):
        current_text = self.input_edit.text()
        result = calculate_expression("cot(")
        self.input_edit.setText(current_text + "cot()")
        self.functions_values["cot"] = result
