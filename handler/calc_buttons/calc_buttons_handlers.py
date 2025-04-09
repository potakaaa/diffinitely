from functions.calc_buttons.calc_buttons import NumberButtons, OperatorButtons, OtherButtons, SpecialButtons

class CalcButtonHandler:
    def __init__(self, ui):
        self.ui = ui
        
        self.number_buttons = NumberButtons(self.ui.input_edit)

        # Number Buttons
        self.ui.zero_button.clicked.connect(lambda: self.number_buttons.zero_button_clicked())
        self.ui.one_button.clicked.connect(lambda: self.number_buttons.one_button_clicked())
        self.ui.two_button.clicked.connect(lambda: self.number_buttons.two_button_clicked())
        self.ui.three_button.clicked.connect(lambda: self.number_buttons.three_button_clicked())
        self.ui.four_button.clicked.connect(lambda: self.number_buttons.four_button_clicked())
        self.ui.five_button.clicked.connect(lambda: self.number_buttons.five_button_clicked())
        self.ui.six_button.clicked.connect(lambda: self.number_buttons.six_button_clicked())  
        self.ui.seven_button.clicked.connect(lambda: self.number_buttons.seven_button_clicked())
        self.ui.eight_button.clicked.connect(lambda: self.number_buttons.eight_button_clicked())
        self.ui.nine_button.clicked.connect(lambda: self.number_buttons.nine_button_clicked())

        # Operator buttons
        self.operator_buttons = OperatorButtons(self.ui.input_edit)

        self.ui.add_button.clicked.connect(lambda: self.operator_buttons.add_button_clicked())
        self.ui.minus_button.clicked.connect(lambda: self.operator_buttons.subtract_button_clicked())
        self.ui.mul_button.clicked.connect(lambda: self.operator_buttons.multiply_button_clicked())
        self.ui.div_button.clicked.connect(lambda: self.operator_buttons.divide_button_clicked())
        self.ui.equal_button.clicked.connect(lambda: self.operator_buttons.equals_button_clicked())
        
        # Other buttons
        self.ui.other_buttons = OtherButtons(self.ui.input_edit)

        self.ui.del_button.clicked.connect(lambda: self.other_buttons.del_button_clicked())
        self.ui.clear_button.clicked.connect(lambda: self.other_buttons.clear_button_clicked())
