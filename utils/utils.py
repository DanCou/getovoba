import re

original = "àáâãäåçèéêëìíîïòóôõöùúûüñÿ\"!#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
replaced = "aaaaaaceeeeiiiiooooouuuuny                                "
table = str.maketrans(original, replaced)


# Create the translation table


def normalize_string(input_string):
    if input_string:
        input_string = input_string.translate(table).strip().title()
    return input_string
