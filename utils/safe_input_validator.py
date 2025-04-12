import re

def safe_input_validator(input):
    safe_input = input.replace("^", "**") 
    safe_input = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", safe_input)
    return safe_input
