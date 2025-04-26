import math

def calculate_expression(expression):
    try:
        # Replace the input string (e.g., 'log', 'ln') with the actual math function
        expression = expression.replace('log', 'math.log10')  # Replace log with math.log10
        expression = expression.replace('ln', 'math.log')  # Replace ln with math.log (natural log)
        expression = expression.replace('sin', 'math.sin')  # Replace sin with math.sin
        expression = expression.replace('cos', 'math.cos')  # Replace cos with math.cos
        expression = expression.replace('tan', 'math.tan')  # Replace tan with math.tan
        expression = expression.replace('csc', '1 / math.sin')  # Replace csc with its reciprocal of sin
        expression = expression.replace('sec', '1 / math.cos')  # Replace sec with its reciprocal of cos
        expression = expression.replace('cot', '1 / math.tan')  # Replace cot with its reciprocal of tan
        expression = expression.replace('e', 'math.e')  # Replace 'e' with math.e
        
        # Evaluate the expression and return the result
        return eval(expression)
    except Exception as e:
        print(f"Error in evaluating expression: {expression}. Error: {e}")
        return None
