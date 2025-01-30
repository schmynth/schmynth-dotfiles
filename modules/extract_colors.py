import os
import subprocess
import linecache

# 1. select which colors to extract from wallbash dcol file
# 2. extract background and text color
# 3. return the colors to main script

# list that indexes group, color class and line number
# lines_color[group][color_class][line_number]
# color_class is primary, text, accent 1 - 9

lines_color_nl = {
    'primary1' : 2,
    'text1' : 4,
    'accent1_1' : 6,
    'accent2_1' : 8,
    'accent3_1' : 10,
    'accent4_1' : 12,
    'accent5_1' : 14,
    'accent6_1' : 16,
    'accent7_1' : 18,
    'accent8_1' : 20,
    'accent9_1' : 22,
    
    'primary2' : 24,
    'text2' : 26,
    'accent1_2' : 28,
    'accent2_2' : 30,
    'accent3_2' : 32,
    'accent4_2' : 34,
    'accent5_2' : 36,
    'accent6_2' : 38,
    'accent7_2' : 40,
    'accent8_2' : 42,
    'accent9_2' : 44,

    'primary3' : 46,
    'text3' : 48,
    'accent1_3' : 50,
    'accent2_3' : 52,
    'accent3_3' : 54,
    'accent4_3' : 56,
    'accent5_3' : 58,
    'accent6_3' : 60,
    'accent7_3' : 62,
    'accent8_3' : 64,
    'accent9_3' : 66,

    'primary4' : 68,
    'text4' : 70,
    'accent1_4' : 72,
    'accent2_4' : 74,
    'accent3_4' : 76,
    'accent4_4' : 78,
    'accent5_4' : 80,
    'accent6_4' : 82,
    'accent7_4' : 84,
    'accent8_4' : 86,
    'accent9_4' : 88,
    }

def get_wallpaper_path():
    """returns the path to wallpaper file set by waypaper.
    Reads config file of waypaper.

    Returns:
        str: path to currently set wallpaper, if it is set by waypaper.
    """
    wallpaper_path = ""
    rel_wallpaper_path = linecache.getline('/home/sebastian/.config/waypaper/config.ini',5).lstrip("wallpaper = ~")
    wallpaper_path = '/home/sebastian' + rel_wallpaper_path
    wallpaper_path = wallpaper_path.strip("\n")
    print("get_wallpaper_path() returned:'", wallpaper_path,"'")
    return wallpaper_path

def run_wallbash():
    command = "./.scripts/wallbash.sh" + ' ' + get_wallpaper_path()
    wallpaper_path = get_wallpaper_path()
    print("subprocess command: ", command)
    if not os.path.isfile(wallpaper_path + '.dcol'):
        subprocess.call(command, shell=True)

def get_color_codes_dict_rgb():
    
    lines_color_ln = {v: k for k, v in lines_color_nl.items()}

    # check if palette file (wallpaper.jpg.dcol) exists
    # if not, create it with wallbash
    #speculative_palette_path = get_wallpaper_path() + '.dcol'
    #if not os.path.isfile(speculative_palette_path):
    run_wallbash()

    # def extract_color(group, color_class):

    # open palette file and save data to palette_data
    palette_path = get_wallpaper_path() + '.dcol'
    with open(palette_path,'r', encoding='utf-8') as file:
        palette_data = file.readlines()


    # generate color name -> color code dictionary from palette file
    color_codes_dict = {}
    current_line_number = 1
    for line in palette_data:
        # check if line is interesting
        if current_line_number in lines_color_ln.keys():
            current_code = line[11:17]
            color_codes_dict.update({lines_color_ln[current_line_number] : current_code})
        current_line_number += 1

    return color_codes_dict

def get_color_codes_dict_rgba(opacity):
    lines_color_ln = {v+1: k for k, v in lines_color_nl.items()}

    # check if palette file (wallpaper.jpg.dcol) exists
    # if not, create it with wallbash
    #speculative_palette_path = get_wallpaper_path() + '.dcol'
    #if not os.path.isfile(speculative_palette_path):
    run_wallbash()

    # def extract_color(group, color_class):

    # open palette file and save data to palette_data
    palette_path = get_wallpaper_path() + '.dcol'
    with open(palette_path,'r', encoding='utf-8') as file:
        palette_data = file.readlines()


    # generate color name -> color code dictionary from palette file
    color_codes_dict = {}
    current_line_number = 1
    for line in palette_data:
        # check if line is interesting
        if current_line_number in lines_color_ln.keys():
            current_code = line[16:]
            current_code = current_code.rstrip("\n\"1\\\);.")
            current_code = current_code + str(opacity) + ")"
            #current_code = current_code.lstrip("#")
            color_codes_dict.update({lines_color_ln[current_line_number] : current_code})
        current_line_number += 1

    return color_codes_dict


def get_color_mode():
    dcol_path = get_wallpaper_path() + ".dcol"
    color_mode = linecache.getline(dcol_path,1).lstrip("dcol_mode=").lstrip("\"")
    color_mode = color_mode.rstrip("\"\n")
    return color_mode