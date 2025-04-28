import re

superscript_map = {
    '0': '⁰',
    '1': '¹',
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵',
    '6': '⁶',
    '7': '⁷',
    '8': '⁸',
    '9': '⁹'
}

subscript_map = {
    '0': '₀',
    '1': '₁',
    '2': '₂',
    '3': '₃',
    '4': '₄',
    '5': '₅',
    '6': '₆',
    '7': '₇',
    '8': '₈',
    '9': '₉'
}

def replace_super_sub(text):
    output = ""
    i = 0
    while i < len(text):
        if text[i] == '^' and i + 1 < len(text):
            i += 1
            while i < len(text) and text[i] in superscript_map:
                output += superscript_map[text[i]]
                i += 1
        elif text[i] == '_' and i + 1 < len(text):
            i += 1
            while i < len(text) and text[i] in subscript_map:
                output += subscript_map[text[i]]
                i += 1
        else:
            output += text[i]
            i += 1
    return output


def result_markup(output):
    markup = output.replace("**", "^")

    markup = re.sub(r"(\d)\*(?=[a-zA-Z])", r"\1", markup)
    markup = replace_super_sub(markup)

    return markup