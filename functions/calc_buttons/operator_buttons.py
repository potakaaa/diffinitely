from utils.safe_input_validator import safe_input_validator
from utils.result_markup import result_markup
import sympy as sp
from PySide6.QtWidgets import QMessageBox
import re
import numpy as np
from helper.c_remover import remove_plus_c

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

    def equals_button_clicked(self, n_value_edit, deriv_1, deriv_2, n_label, n_deriv, integral, definite_integral_label, definite_integral_result, definiteWidget):
        n_value = 1 if n_value_edit.text() == "" else int(n_value_edit.text())

        definite_integral_a = definiteWidget.get_a_value()
        definite_integral_b = definiteWidget.get_b_value()

        try:
            safe_input = safe_input_validator(self.lineEdit.text())
            expr = sp.sympify(safe_input)

            first_derivative = sp.diff(expr, self.var_symbol)
            second_derivative = sp.diff(first_derivative, self.var_symbol)

            if n_deriv.text() == "":
                n_label.setText("Nth Derivative (n=1)")

            nth_derivative = sp.diff(expr, self.var_symbol, n_value)
            integral_result = sp.integrate(expr, self.var_symbol)

            definite_integral_label.setText(f"Definite Integral [{definite_integral_a}, {definite_integral_b}]")
            definite_integral = sp.integrate(expr, (self.var_symbol, definite_integral_a, definite_integral_b))

            deriv_1.setText(result_markup(str(first_derivative)))
            deriv_2.setText(result_markup(str(second_derivative)))
            n_deriv.setText(result_markup(str(nth_derivative)))
            integral.setText(result_markup(str(integral_result) + f" + C"))
            definite_integral_result.setText(result_markup(str(definite_integral)))
        
        except Exception as e:
            QMessageBox.critical(None, "Input Error", f"Error evaluating operation: {e}")

    
    @staticmethod
    def find_variable(expr):
        try:
            parsed = sp.sympify(expr)
            symbols = parsed.free_symbols
            if symbols:
                # Return a sorted list of symbols, prioritizing x and y
                preferred_order = ['x', 'y']
                sorted_symbols = sorted(symbols, key=lambda s: (preferred_order.index(str(s)) if str(s) in preferred_order else 99, str(s)))
                return sorted_symbols  # Returns a list of symbols like [x, y]
            else:
                return [sp.Symbol('x')]  # Default to [x]
        except Exception:
            return [sp.Symbol('x')]


    def calculate(self, ui, definite_widget):
        self.ui = ui
        # 1. Get input
        function_expr = self.ui.input_edit.text()

        # 2. Find the correct variable first!
        var_symbols = self.find_variable(function_expr)
        self.var_symbol = var_symbols[0]
        self.variable = str(self.var_symbol)

        self.equals_button_clicked(
            self.ui.n_value_edit,
            self.ui.derivative_1st_edit,
            self.ui.derivative_2nd_edit,
            self.ui.n_value_label,
            self.ui.nth_derivative_edit,
            self.ui.integral_edit,
            self.ui.definite_integral_label,
            self.ui.definite_integral_edit,
            definite_widget
        )
        
        try:
            var_values = np.linspace(-10000, 10000, 1000000)
            
            y_values = self.evaluate_function(function_expr, var_values)
            integral_y = self.evaluate_function(remove_plus_c(self.ui.integral_edit.text()), var_values)


            self.ui.graph_manager.plot_function(var_values, y_values, f"f({self.variable}) = {function_expr}")
            self.ui.graph_manager.plot_derivative(
                var_values,
                self.evaluate_function(self.ui.derivative_1st_edit.text(), var_values),
                self.evaluate_function(self.ui.derivative_2nd_edit.text(), var_values),
                self.evaluate_function(self.ui.nth_derivative_edit.text(), var_values),
            )
            self.ui.graph_manager.plot_indefinite_integral(var_values, integral_y, f"∫f({self.variable})d{self.variable} = {self.ui.integral_edit.text()}")
            self.ui.graph_manager.plot_definite_integral(
                var_values,
                integral_y,
                definite_widget.get_a_value(),
                definite_widget.get_b_value(),
                f"∫[{definite_widget.get_a_value()},{definite_widget.get_b_value()}] f({self.variable})d{self.variable}"
            )
            
        except Exception as e:
            print(f"Error graphing: {e}")



    def evaluate_function(self, expr, x_values):
        if not expr or expr.strip() == "":
            return np.zeros_like(x_values)

        expr = expr.replace('²', '**2')
        expr = expr.replace('³', '**3')
        expr = safe_input_validator(expr)

        # Step 1: Protect function names
        functions = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'sqrt', 'log', 'log10', 'exp']
        func_placeholders = {}
        for i, func in enumerate(functions):
            placeholder = f"FUNC{i}"
            expr = re.sub(rf'\b{func}\b', placeholder, expr)
            func_placeholders[placeholder] = func

        # Step 2: Insert multiplication signs safely (only for your detected variable)
        expr = re.sub(rf'(\d)({self.variable})', r'\1*\2', expr)
        expr = re.sub(rf'({self.variable})\(', r'\1*(', expr)
        expr = re.sub(r'\)([a-zA-Z0-9])', r')*\1', expr)

        # Step 3: Restore the function names
        for placeholder, func in func_placeholders.items():
            expr = expr.replace(placeholder, func)

        # Step 4: Safe evaluation
        safe_globals = {
            self.variable: x_values,
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "sqrt": np.sqrt, "pi": np.pi, "e": np.e,
            "abs": np.abs, "log": np.log10, "ln": np.log,
            "exp": np.exp,
            "sec": lambda x: 1 / np.cos(x),
            "csc": lambda x: 1 / np.sin(x),
            "cot": lambda x: 1 / np.tan(x)
        }

        try:
            y = eval(expr, {"__builtins__": {}}, safe_globals)
            if np.isscalar(y):
                y = np.full_like(x_values, y)
            else:
                y = np.array(y)
            return y
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return np.zeros_like(x_values)
