from utils.safe_input_validator import safe_input_validator
from utils.result_markup import result_markup
import sympy as sp
from PySide6.QtWidgets import QMessageBox
import re
import numpy as np

class OperatorButtons:
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit
        self.x = sp.symbols('x')

    def add_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "+")

    def subtract_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "-")

    def multiply_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "*")

    def divide_button_clicked(self):
        self.lineEdit.setText(self.lineEdit.text() + "/")

    def equals_button_clicked(self, n_value_edit, deriv_1, deriv_2, n_deriv, integral, definite_integral_result, definiteWidget):
        n_value = 1 if n_value_edit.text() == "" else int(n_value_edit.text())

        definite_integral_a = definiteWidget.get_a_value()
        definite_integral_b = definiteWidget.get_b_value()


        
        try:
            safe_input = safe_input_validator(self.lineEdit.text())
            first_derivative = sp.diff(safe_input, self.x)
            second_derivative = sp.diff(first_derivative, self.x)
            nth_derivative = sp.diff(safe_input, self.x, n_value)
            integral_result = sp.integrate(safe_input, self.x)
            definite_integral = sp.integrate(safe_input, (self.x, definite_integral_a, definite_integral_b))

            deriv_1.setText(result_markup(str(first_derivative)))
            deriv_2.setText(result_markup(str(second_derivative)))
            n_deriv.setText(result_markup(str(nth_derivative)))
            integral.setText(result_markup(str(integral_result)))
            definite_integral_result.setText(result_markup(str(definite_integral)))
        
        except Exception as e:
            QMessageBox.critical(None, "Input Error", "Error evaluating operation. Please fix your input!")

    def calculate(self, ui, definite_widget):
        # This method will be called when the equal button is clicked
        # First, let your existing equals_button_clicked method handle the calculation
        self.ui = ui

        self.equals_button_clicked(
            self.ui.n_value_edit,
            self.ui.derivative_1st_edit,
            self.ui.derivative_2nd_edit,
            self.ui.nth_derivative_edit,
            self.ui.integral_edit,
            self.ui.definite_integral_edit,
            definite_widget
        )
        
        try:
            # Get function expression from input
            function_expr = self.ui.input_edit.text()
            
            # Get derivative and integral expressions from the UI fields
            derivative_expr = self.ui.derivative_1st_edit.text()
            integral_expr = self.ui.integral_edit.text()
            
            # Generate x values (adjust range as needed)
            import numpy as np
            x_values = np.linspace(-10, 10, 1000)
            
            # Calculate function values
            y_values = self.evaluate_function(function_expr, x_values)
    
            integral_y = self.evaluate_function(integral_expr, x_values)
            
            # Plot using the graph manager
            self.ui.graph_manager.plot_function(x_values, y_values, f"f(x) = {function_expr}")
            self.ui.graph_manager.plot_derivative(
                x_values,
                self.evaluate_function(self.ui.derivative_1st_edit.text(), x_values),
                self.evaluate_function(self.ui.derivative_2nd_edit.text(), x_values),
                self.evaluate_function(self.ui.nth_derivative_edit.text(), x_values),
            )
            self.ui.graph_manager.plot_indefinite_integral(x_values, integral_y, f"∫f(x)dx = {integral_expr}")
            self.ui.graph_manager.plot_definite_integral(
                x_values,
                integral_y,
                definite_widget.get_a_value(),
                definite_widget.get_b_value(),
                f"∫[a,b] f(x)dx = {integral_expr}"
            )
            
        except Exception as e:
            # Handle errors
            print(f"Error graphing: {e}")


    def evaluate_function(self, expr, x_values):
        if not expr or expr.strip() == "":
            return np.zeros_like(x_values)

        expr = expr.replace('^', '**')

        # Step 1: Protect function names by temporarily replacing them
        functions = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'sqrt', 'log', 'log10', 'exp']
        func_placeholders = {}
        for i, func in enumerate(functions):
            placeholder = f"FUNC{i}"
            expr = re.sub(rf'\b{func}\b', placeholder, expr)
            func_placeholders[placeholder] = func

        # Step 2: Insert multiplication signs safely
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)         # number followed by variable
        expr = re.sub(r'([a-zA-Z])\(', r'\1*(', expr)             # variable followed by (

        expr = re.sub(r'\)([a-zA-Z0-9])', r')*\1', expr)          # ) followed by variable or number

        # Step 3: Restore the function names
        for placeholder, func in func_placeholders.items():
            expr = expr.replace(placeholder, func)

        # Step 4: Safe evaluation
        safe_globals = {
            "x": x_values,
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "sqrt": np.sqrt, "pi": np.pi, "e": np.e,
            "abs": np.abs, "log": np.log10, "ln": np.log,
            "exp": np.exp,
            "sec": lambda x: 1 / np.cos(x),
            "csc": lambda x: 1 / np.sin(x),
            "cot": lambda x: 1 / np.tan(x)
        }

        try:
            y = eval(expr, {"_builtins_": {}}, safe_globals)
            if np.isscalar(y):
                y = np.full_like(x_values, y)
            else:
                y = np.array(y)
            return y
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return np.zeros_like(x_values)
