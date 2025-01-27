import os
##### FILE PATHS #####


def remove_color_code_rgb(line):
    """removes 6 digit hex color code (after #) from line
    line has to end with color code, no trailing comments allowed.

    Args:
        line (str): line of text with hex color code at the end

    Returns:
        str: stripped line, as before but without color code.
    """
    stripped_line = line.rstrip("1234567890ABCDEF;\\\n")
    return stripped_line

def remove_color_code_rgba(line):
    """removes rgba value from line
    line has to end with color code, no trailing comments allowed.

    Args:
        line (str): line of text with hex color code at the end

    Returns:
        str: stripped line, as before but without color code.
    """
    stripped_line = line.rstrip("1234567890ABCDEFrgba;\n()#,\\.")
    return stripped_line

def replace_color_rgb(file_data, color_name, replacement_color):
    """replaces named color code in data list (read file) with code provided
    as argument.

    Args:
        file_data (list): file data in list
        color_name (str): name of the color as defined in file. Has to match.
        replacement_color (str): color code of replacement color, 6 digits, no #

    Returns:
        list: complete update file as data list
    """
    current_line_number = 1
    for line in file_data:
        if color_name in line:
            # print('value1 # is in line {}'.format(current_line_number))
            stripped_line = remove_color_code_rgb(line)
            # print('stripped line is: ', stripped_line)
            file_data[current_line_number-1] = stripped_line + replacement_color + ';' + '\n'
        current_line_number += 1
    return file_data

def replace_color_rgba(file_data, color_name, replacement_color):
    """replaces named color code in data list (read file) with code provided
    as argument.

    Args:
        file_data (list): file data in list
        color_name (str): name of the color as defined in file. Has to match.
        replacement_color (str): color code of replacement color, 6 digits, no #

    Returns:
        list: complete update file as data list
    """
    current_line_number = 1
    for line in file_data:
        if color_name in line:
            # print('value1 # is in line {}'.format(current_line_number))
            stripped_line = remove_color_code_rgba(line)
            # print('stripped line is: ', stripped_line)
            file_data[current_line_number-1] = stripped_line + replacement_color + ';' + '\n'
        current_line_number += 1
    return file_data





