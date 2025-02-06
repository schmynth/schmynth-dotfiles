import modules.update_palette as up
import modules.update_app_colors as uac
import modules.extract_colors as e
import subprocess
import os

# define/get paths
dotfiles_rootpath = os.path.dirname(os.path.realpath(__file__))
palette_path = dotfiles_rootpath + "/.config/"
hyprland_colors_path = dotfiles_rootpath + "/.config/hypr/"
restart_waybar_script_path = dotfiles_rootpath + "/.scripts/restart_waybar.sh"
restart_swayosd_script_path = dotfiles_rootpath + "/.scripts/restart_swayosd.sh"
wallpaper_path = e.get_wallpaper_path()

def run_bash_script(script_path):
    subprocess.call(script_path, shell=True)

e.run_wallbash(wallpaper_path)

# get color info from new wallpaper
up.update_palette(palette_path, wallpaper_path)
up.update_adaptive_theme(hyprland_colors_path, wallpaper_path)
#up.update_hyprlock_image_path(hyprland_colors_path, wallpaper_path)
color_mode = e.get_color_mode(wallpaper_path)

uac.set_gtk_theme(color_mode)

# update hyprland and applications
run_bash_script(restart_waybar_script_path)
run_bash_script(restart_swayosd_script_path)

uac.update_rofi_colors(color_mode, wallpaper_path)
uac.update_alacritty_colors(color_mode, wallpaper_path)
uac.update_vscode_colors(color_mode, wallpaper_path)
