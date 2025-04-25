from functions.calc_buttons.number_buttons import NumberButtons
from functions.calc_buttons.operator_buttons import OperatorButtons
from functions.calc_buttons.other_buttons import OtherButtons
from functions.calc_buttons.special_buttons import SpecialButtons
import re


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

        self.ui.equal_button.clicked.connect(lambda: self.operator_buttons.calculate(self.ui))
        
        # Other buttons
        self.other_buttons = OtherButtons(self.ui.input_edit, self.ui.n_value_edit, self.ui.derivative_1st_edit, self.ui.derivative_2nd_edit, self.ui.nth_derivative_edit, self.ui.integral_edit,  self.ui)

        self.ui.del_button.clicked.connect(lambda: self.other_buttons.del_button_clicked())
        self.ui.clear_button.clicked.connect(lambda: self.other_buttons.clear_button_clicked())
        self.ui.more_button.clicked.connect(lambda: self.other_buttons.more_button_clicked())

        # Special Buttons
        self.special_buttons = SpecialButtons(self.ui.input_edit)
        
        self.ui.x_button.clicked.connect(self.special_buttons.x_button_clicked)
        self.ui.y_button.clicked.connect(self.special_buttons.y_button_clicked)
        self.ui.a_2_button.clicked.connect(self.special_buttons.a_squared_button_clicked)
        self.ui.a_b_button.clicked.connect(self.special_buttons.a_power_b_button_clicked)
        self.ui.open_parenthesis_button.clicked.connect(self.special_buttons.open_parenthesis_button_clicked)
        self.ui.close_parenthesis_button.clicked.connect(self.special_buttons.close_parenthesis_button_clicked)
        self.ui.less_button.clicked.connect(self.special_buttons.less_button_clicked)
        self.ui.great_button.clicked.connect(self.special_buttons.greater_button_clicked)
        self.ui.less_equal_button.clicked.connect(self.special_buttons.less_equal_button_clicked)
        self.ui.great_equal_button.clicked.connect(self.special_buttons.greater_equal_button_clicked)
        self.ui.fact_button.clicked.connect(self.special_buttons.factorial_button_clicked)
        self.ui.x_fact_button.clicked.connect(self.special_buttons.x_fact_button_clicked)
        self.ui.apos_button.clicked.connect(self.special_buttons.apostrophe_button_clicked)
        self.ui.percent_button.clicked.connect(self.special_buttons.percent_button_clicked)
        self.ui.sqrt_button.clicked.connect(self.special_buttons.sqrt_button_clicked)
        self.ui.pi_button.clicked.connect(self.special_buttons.pi_button_clicked)

    