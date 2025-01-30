import modules.update_palette as up
import modules.update_vscode_colors as uvs
import modules.extract_colors as e
import subprocess
import os

dotfiles_rootpath = os.path.dirname(os.path.realpath(__file__))
palette_path = dotfiles_rootpath + "/.config/"
restart_waybar_script_path = dotfiles_rootpath + "/.scripts/restart_waybar.sh"

def restart_waybar():
    subprocess.call(restart_waybar_script_path, shell=True)

# get color info from new wallpaper
up.update_palette(palette_path)
color_mode = e.get_color_mode()

# update hyprland and applications
restart_waybar()
uvs.update_vscode_colors(color_mode)