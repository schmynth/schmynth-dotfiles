#!/bin/bash

# this script installs the schmynth dotfiles
# currently linked config files are:
# .zshrc
# hyprland
# hyprlock
# waybar
# waypaper
# kitty
#
# currently tracked folders:
# wallpapers (copied), scripts (linked)

# find full path of script:
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
set -x #echo on

echo "linking .zshrc..."
ln -s $SCRIPT_PATH/.zshrc /home/$USER/.zshrc

echo "linking .vimrc..."
ln -s $SCRIPT_PATH/.vimrc /home/$USER/.vimrc

echo "linking hyprland config file..."
mkdir -p /home/$USER/hypr
ln -s $SCRIPT_PATH/.config/hypr/hyprland.conf /home/$USER/.conf/hypr/hyprland.conf

echo "linking hyprlock config file..."
ln -s $SCRIPT_PATH/.config/hypr/hyprlock.conf /home/$USER/.conf/hypr/hyprlock.conf

echo "linking waybar config files..."
mkdir -p /home/$USER/waybar
ln -s $SCRIPT_PATH/.config/waybar/config /home/$USER/.config/waybar/config
ln -s $SCRIPT_PATH/.config/waybar/modules.json /home/$USER/.config/waybar/modules.json
ln -s $SCRIPT_PATH/.config/waybar/runrofi.sh /home/$USER/.config/waybar/runrofi.sh
ln -s $SCRIPT_PATH/.config/waybar/style.css /home/$USER/.config/waybar/style.css

echo "linking waypaper config file..."
mkdir -p /home/$USER/waypaper
ln -s $SCRIPT_PATH/.config/waypaper/config.ini /home/$USER/.config/waypaper/config.ini

echo "copying wallpaper folder..."
cp -r $SCRIPT_PATH/wallpapers/ /home/$USER/Bilder/wallpapers

echo "linking kitty config file..."
mkdir -p /home/$USER/.config/kitty
ln -s $SCRIPT_PATH/.config/kitty/kitty.conf /home/$USER/.config/kitty/kitty.conf

echo "linking rofi config file..."
mkdir -p /home/$USER/.config/rofi
ln -s $SCRIPT_PATH/.config/rofi/config.rasi /home/$USER/.config/rofi/config.rasi

echo "linking scripts..."
ln -s $SCRIPT_PATH/.scripts /home/$USER/.scripts
