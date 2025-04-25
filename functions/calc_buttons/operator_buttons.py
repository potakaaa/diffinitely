from utils.safe_input_validator import safe_input_validator
from utils.result_markup import result_markup
import sympy as sp
from PySide6.QtWidgets import QMessageBox
import re

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

    def equals_button_clicked(self, n_value_edit, deriv_1, deriv_2, n_deriv, integral):
        n_value = 1 if n_value_edit.text() == "" else int(n_value_edit.text())
        
        try:
            safe_input = safe_input_validator(self.lineEdit.text())
            first_derivative = sp.diff(safe_input, self.x)
            second_derivative = sp.diff(first_derivative, self.x)
            nth_derivative = sp.diff(safe_input, self.x, n_value)
            integral_result = sp.integrate(safe_input, self.x)

            deriv_1.setText(result_markup(str(first_derivative)))
            deriv_2.setText(result_markup(str(second_derivative)))
            n_deriv.setText(result_markup(str(nth_derivative)))
            integral.setText(result_markup(str(integral_result)))
        
        except Exception as e:
            QMessageBox.critical(None, "Input Error", "Error evaluating operation. Please fix your input!")

    def calculate(self, ui):
        # This method will be called when the equal button is clicked
        # First, let your existing equals_button_clicked method handle the calculation
        self.ui = ui

        self.equals_button_clicked(
            self.ui.n_value_edit,
            self.ui.derivative_1st_edit,
            self.ui.derivative_2nd_edit,
            self.ui.nth_derivative_edit,
            self.ui.integral_edit
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
            self.ui.graph_manager.plot_integral(x_values, integral_y, f"∫f(x)dx = {integral_expr}")
            
        except Exception as e:
            # Handle errors
            print(f"Error graphing: {e}")


    def evaluate_function(self, expr, x_values):
        """Evaluate the function for the given x values"""
        import numpy as np
        
        if not expr or expr.strip() == "":
            return np.zeros_like(x_values)

        # Preprocess expression: handle implicit multiplication like 7x or (x+1)(x-1)
        expr = expr.replace('^', '**')  # Convert caret to Python power operator
        
        # Insert * between number and variable (e.g., 7x -> 7*x)
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        # Insert * between variable and parenthesis (e.g., x(x+1) -> x*(x+1))
        expr = re.sub(r'([a-zA-Z])\(', r'\1*(', expr)
        # Insert * between closing parenthesis and variable or number (e.g., )(x) or )(2)
        expr = re.sub(r'\)([a-zA-Z0-9])', r')*\1', expr)

        def f(x):
            try:
                import math
                safe_globals = {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
                                "abs": abs, "log": math.log, "log10": math.log10}
                return eval(expr, {"_builtins_": {}}, safe_globals)
            except Exception:
                return float('nan')
        
        try:
            return np.array([f(x) for x in x_values])
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return np.zeros_like(x_values)