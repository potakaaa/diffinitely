from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont, QIcon
from ui.main_window import Ui_MainWindow
from functions.calc_buttons.calc_buttons import NumberButtons, OperatorButtons, OtherButtons, SpecialButtons

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")

        # initial font setup
        self.initial_font_size = 10  # default font size
        self.zoom_factor = 5  # zoom rate
        self.current_font_size = self.initial_font_size

        # zoom buttons
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionZoom_Out.triggered.connect(self.zoom_out)

        # reset buttons
        self.actionReset.triggered.connect(self.reset)

        #special Buttons
        self.special_buttons = SpecialButtons(self.input_edit)
        self.x_button.clicked.connect(self.special_buttons.x_button_clicked)
        self.y_button.clicked.connect(self.special_buttons.y_button_clicked)
        self.a_2_button.clicked.connect(self.special_buttons.a_squared_button_clicked)
        self.a_b_button.clicked.connect(self.special_buttons.a_power_b_button_clicked)
        self.open_parenthesis_button.clicked.connect(self.special_buttons.open_parenthesis_button_clicked)
        self.close_parenthesis_button.clicked.connect(self.special_buttons.close_parenthesis_button_clicked)
        self.less_button.clicked.connect(self.special_buttons.less_button_clicked)
        self.great_button.clicked.connect(self.special_buttons.greater_button_clicked)
        self.less_equal_button.clicked.connect(self.special_buttons.less_equal_button_clicked)
        self.great_equal_button.clicked.connect(self.special_buttons.greater_equal_button_clicked)
        self.fact_button.clicked.connect(self.special_buttons.factorial_button_clicked)
        self.x_fact_button.clicked.connect(self.special_buttons.x_fact_button_clicked)
        self.apos_button.clicked.connect(self.special_buttons.apostrophe_button_clicked)
        self.percent_button.clicked.connect(self.special_buttons.percent_button_clicked)
        self.sqrt_button.clicked.connect(self.special_buttons.sqrt_button_clicked)
        self.pi_button.clicked.connect(self.special_buttons.pi_button_clicked)


        # Number buttons
        self.number_buttons = NumberButtons(self.input_edit)

        self.zero_button.clicked.connect(lambda: self.number_buttons.zero_button_clicked())
        self.one_button.clicked.connect(lambda: self.number_buttons.one_button_clicked())
        self.two_button.clicked.connect(lambda: self.number_buttons.two_button_clicked())
        self.three_button.clicked.connect(lambda: self.number_buttons.three_button_clicked())
        self.four_button.clicked.connect(lambda: self.number_buttons.four_button_clicked())
        self.five_button.clicked.connect(lambda: self.number_buttons.five_button_clicked())
        self.six_button.clicked.connect(lambda: self.number_buttons.six_button_clicked())  
        self.seven_button.clicked.connect(lambda: self.number_buttons.seven_button_clicked())
        self.eight_button.clicked.connect(lambda: self.number_buttons.eight_button_clicked())
        self.nine_button.clicked.connect(lambda: self.number_buttons.nine_button_clicked())

        # Operator buttons
        self.operator_buttons = OperatorButtons(self.input_edit)

        self.add_button.clicked.connect(lambda: self.operator_buttons.add_button_clicked())
        self.minus_button.clicked.connect(lambda: self.operator_buttons.subtract_button_clicked())
        self.mul_button.clicked.connect(lambda: self.operator_buttons.multiply_button_clicked())
        self.div_button.clicked.connect(lambda: self.operator_buttons.divide_button_clicked())
        self.equal_button.clicked.connect(lambda: self.operator_buttons.equals_button_clicked())
        
        # Other buttons
        self.other_buttons = OtherButtons(self.input_edit)

        self.del_button.clicked.connect(lambda: self.other_buttons.del_button_clicked())
        self.clear_button.clicked.connect(lambda: self.other_buttons.clear_button_clicked())

        # set initial font size
        self.update_ui_font_size()

    def zoom_in(self):
        """Increase the font size of UI components."""
        self.current_font_size += self.zoom_factor
        self.update_ui_font_size()

    def zoom_out(self):
        """Decrease the font size of UI components."""
        self.current_font_size -= self.zoom_factor
        self.update_ui_font_size()

    def update_ui_font_size(self):
        """Update the font size of all UI components."""
        # ui components to update on zoom
        elements = [
            self.input_label, self.input_edit, self.n_value_label_2, self.label,
            self.derivative_1st_label, self.derivative_2nd_label, self.nth_derivative_label,
            self.integral_label, self.x_button, self.y_button, self.a_2_button,
            self.a_b_button, self.open_parenthesis_button, self.close_parenthesis_button,
            self.less_button, self.great_button, self.fact_button, self.apos_button,
            self.less_equal_button, self.great_equal_button, self.x_fact_button,
            self.percent_button, self.sqrt_button, self.pi_button, self.zero_button,
            self.nine_button, self.minus_button, self.seven_button, self.four_button,
            self.one_button, self.two_button, self.div_button, self.six_button,
            self.five_button, self.eight_button, self.mul_button, self.add_button,
            self.three_button, self.equal_button, self.more_button, self.del_button,
            self.clear_button, self.pushButton_36, self.label_6
        ]
        for element in elements:
            element.setFont(QFont('Arial', self.current_font_size))

    def reset(self):
        """Reset the font size to the initial value."""
        self.current_font_size = self.initial_font_size
        self.update_ui_font_size() 
