import re
def remove_plus_c(integral_str):
    # Remove any '+ C', '+C', '+ constant', with optional whitespace
    return re.sub(r'\s*\+\s*C\b.*$', '', integral_str)