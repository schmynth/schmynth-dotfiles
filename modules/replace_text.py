import os
##### FILE PATHS #####

def remove_color_code(line, mode):
    """removes color code from line.
    line has to end with color code, no trailing comments allowed.

    Args:
        line (str): line of text containing the color code that has to be removed.
        mode (str): color code format (rgb or rgba)
    """
    if mode == "rgb":
        stripped_line = line.rstrip("1234567890ABCDEFabcdef;\\\n\"")
        return stripped_line
    elif mode == "rgba":
        stripped_line = line.rstrip("1234567890ABCDEFrgba;\n()#,\\.\"")
        return stripped_line
    else:
        return "wrong color format specified."

def replace_color(file_data, color_name, replacement_color, mode, last_char):
    """replaces named color code in data list (read file) with code provided
    as argument. Searches name in line thus independent of data structure.

    Args:
        file_data (list): file data in list
        color_name (str): name of the color as defined in file. Has to match.
        replacement_color (str): color code of replacement color, 6 digits, no #

    Returns:
        list: complete update file as data list
    """
    current_line_number = 1
    for line in file_data:
        if color_name in line and "@" not in line:  # don't overwrite variables
            # print('value1 # is in line {}'.format(current_line_number))
            stripped_line = remove_color_code(line, mode)
            # print('stripped line is: ', stripped_line)
            file_data[current_line_number-1] = stripped_line + replacement_color + last_char + '\n'
        current_line_number += 1
    return file_data





