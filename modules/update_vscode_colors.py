import json
import os

cwd = os.getcwd() + "/modules/"
settings_path = "/home/sebastian/.var/app/com.visualstudio.code/config/Code/User/"
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
    