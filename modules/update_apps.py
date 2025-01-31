import json
import os
from . import replace_text as r
from . import extract_colors as e

# update vs code

cwd = os.getcwd() + "/modules/"
settings_path = "/home/sebastian/.config/Code/User/"
settings_file = cwd + "settings.json"

# so far only prints values
def update_json_property(settings_file, property_group, property_name, property_value):
    with open(settings_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        print(json_data[property_group][property_name])
        json_data[property_group][property_name] = property_value
        print(json_data[property_group][property_name])
    with open(settings_file, 'w') as output:
        json.dump(json_data, output)

# update_json_property(settings_file, 'workbench.colorCustomizations', 'sideBar.background', '#colorcode')

def update_vscode_colors(color_palette_dict, settings_file):
    print(settings_file)

def update_alacritty(dotfiles_rootpath):
    alacritty_config = dotfiles_rootpath + ".alacritty.toml"
    # read file into data
    with open(alacritty_config,'r', encoding='utf-8') as file:
        data = file.readlines()
    # color_palette.css File is now stored in data
    file.close()
    color_palette_dict = e.get_color_codes_dict_rgb()

    replacement_color = "\"#" + color_palette_dict["accent1_1"] + "\""
    new_data = r.replace_color_rgba_no_semi(data, "background", replacement_color)

    data_str = ""
    # convert file data from list to string for write()-function
    for word in new_data:
        data_str = data_str + word
    print(data_str)
    with open(".alacritty.toml", "w") as f:
        f.write(data_str)
    f.close()
    
