import re

def result_markup(output):
    markup = output.replace("**", "^")

    markup = re.sub(r"(\d)\*(?=[a-zA-Z])", r"\1", markup)

    return markup

print(result_markup("x^2 + 3*x + 5"))  # Example usage