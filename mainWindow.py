from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont, QIcon, QIntValidator
from ui.main_window import Ui_MainWindow
from functions.calc_buttons.calc_buttons import NumberButtons, OperatorButtons, OtherButtons, SpecialButtons
from handler.calc_buttons.calc_buttons_handlers import CalcButtonHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")

        # initial font setup
        self.initial_font_size = 10  # default font size
        self.zoom_factor = 5  # zoom rate
        self.current_font_size = self.initial_font_size

        # N-value validator
        self.n_value_edit.setValidator(QIntValidator(0, 1000))
        self.calc_button_handler = CalcButtonHandler(self)
        

        # zoom buttons
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionZoom_Out.triggered.connect(self.zoom_out)

        # reset buttons
        self.actionReset.triggered.connect(self.reset)        

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
            self.input_label, self.input_edit, self.n_value_label, self.label,
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
