from . import extract_colors as e
from . import replace_text as r
import os
import linecache
import subprocess


def update_palette(path, wallpaper_path):

    output_filename = "color_palette.css"
    output_file = path + output_filename
    # read dcol file of current wallpaper
    color_codes_dict = e.get_color_codes_dict_rgba(0.5, wallpaper_path)

    # read output file into data
    with open(output_file,'r', encoding='utf-8') as file:
        data = file.readlines()
    # color_palette.css File is now stored in data
    file.close()

    # print(color_codes_dict)
    # print("old data:\n", data)
    # check if line contains "value0 #..."
    for color in color_codes_dict:
        data_list = r.replace_color(data, color, color_codes_dict[color], "rgba", ";")
        # data_list = r.replace_color_rgba(data, color, color_codes_dict[color])
        data_str = ""

    # convert file data from list to string for write()-function
    for word in data_list:
        data_str = data_str + word


    # print('new data:\n', data)

    with open(output_file, "w") as f:
        f.write(data_str)
    f.close()


def update_adaptive_theme(path, wallpaper_path):
    output_filename = "adaptive_theme.conf"
    output_file = path + output_filename
    # read dcol file of current wallpaper
    color_codes_dict = e.get_color_codes_dict_rgba("2",wallpaper_path)

    # read output file into data
    with open(output_file,'r', encoding='utf-8') as file:
        data = file.readlines()
    # colors.conf File is now stored in data
    file.close()

    current_line = 1
    for line in data:
        if "wallpaper_path" in line:
            data[current_line-1] = ""
        data_str = ""
        current_line += 1

    # check if line contains "value0 #..."
    for color in color_codes_dict:
        data_list = r.replace_color(data, color, color_codes_dict[color], "rgba", "")
        # data_list = r.replace_color_rgba(data, color, color_codes_dict[color])
        data_str = ""

    # convert file data from list to string for write()-function
    for word in data_list:
        if "wallpaper_path" not in word:
            data_str = data_str + word
    data_str = data_str + "$wallpaper_path = " + wallpaper_path


    # print('new data:\n', data)

    with open(output_file, "w") as f:
        f.write(data_str)
    f.close()

