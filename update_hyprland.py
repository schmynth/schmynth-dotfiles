import modules.update_palette as u
import subprocess
import os

dotfiles_rootpath = os.path.dirname(os.path.realpath(__file__))
palette_path = dotfiles_rootpath + "/.config/"
restart_waybar_script_path = dotfiles_rootpath + "/.scripts/restart_waybar.sh"
print(palette_path)

def restart_waybar():
    subprocess.call(restart_waybar_script_path, shell=True)

u.update_palette(palette_path)

restart_waybar()