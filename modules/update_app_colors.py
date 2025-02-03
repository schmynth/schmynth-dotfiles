import json
import os
from . import extract_colors as e
from . import replace_text as r

cwd = os.getcwd() + "/modules/"
home_dir = os.environ['HOME']

# get vs code config file
if os.path.isfile(home_dir + "/.config/Code/User/settings.json"):
    vscode_settings_file = "/home/sebastian/.config/Code/User/settings.json"
elif os.path.isfile(home_dir + "/.var/app/com.visualstudio.code/config/Code/User/settings.json"):
    vscode_settings_file = home_dir + "/.var/app/com.visualstudio.code/config/Code/User/settings.json"
else:
    print("No VS code settings file found.")

# get alacritty config file
alacritty_config_file = os.getcwd() + "/.alacritty.toml"

# so far only prints values
def update_json_property(settings_file, property_group, property_name, property_value):
    with open(settings_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        if property_group != 0:
            if property_name in json_data[property_group]:
                json_data[property_group][property_name] = property_value
        else:
            json_data[property_name] = property_value
    with open(settings_file, 'w') as output:
        json.dump(json_data, output)

group = 1
group_str = str(group)

# update_json_property(settings_file, 'workbench.colorCustomizations', 'sideBar.background', '#colorcode')
vscode_colors = {"foreground":"text1", 
                 "editorGroupHeader.tabsBackground":"accent1_1",
                 "minimap.background":"primary1",
                 "tab.activeBackground":"primary1",
                 "tab.inactiveBackground" : "accent1_1",
                 "editor.background":"primary1",
                 "sideBar.background":"accent1_1",
                 "sideBarSectionHeader.background":"accent1_1",
                 "sideBar.border" : "accent1_1",
                 "activityBar.background":"accent1_1", 
                 "activityBar.foreground" : "accent9_2",
                 "activityBar.border" : "accent1_1",
                 "panel.background":"primary1",
                 "statusBar.background" : "accent1_1"}

def update_vscode_colors(color_mode):
    color_palette_dict = e.get_color_codes_dict_rgb()
    for key in vscode_colors:
        update_json_property(vscode_settings_file, "workbench.colorCustomizations", key, "#" + color_palette_dict[vscode_colors[key]])
    if color_mode == "light":
        update_json_property(vscode_settings_file, 0, "workbench.colorTheme", "Default Light Modern")
    else:
        update_json_property(vscode_settings_file, 0, "workbench.colorTheme", "Default Dark+")

alacritty_colors = {
    "background" : "primary1"
}

def update_alacritty_colors(color_mode):
    color_palette_dict = e.get_color_codes_dict_rgb()
    with open(alacritty_config_file, "r", encoding='utf-8') as file:
        data = file.readlines()
    file.close()

    for key in alacritty_colors:
        data_list = r.replace_color(data, key, color_palette_dict[alacritty_colors[key]], "rgb", "\"")
        data_str = ""
    for word in data_list:
        data_str = data_str + word

    with open(alacritty_config_file,"w", encoding='utf-8') as file:
        file.write(data_str)
    file.close()

        