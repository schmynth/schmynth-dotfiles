#!/bin/bash

# this script installs the schmynth dotfiles
# currently linked config files are:
# .zshrc
# hyprland
# hyprlock
# waybar
# waypaper
# kitty
# .alacritty.toml
#
# currently tracked folders:
# wallpapers (copied), scripts (linked)

# find full path of script:
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
set -x #echo on

echo "linking .zshrc..."
ln -sf $SCRIPT_PATH/.zshrc /home/$USER/.zshrc

echo "linking .vimrc..."
ln -sf $SCRIPT_PATH/.vimrc /home/$USER/.vimrc

echo "linking .alacritty.toml..."
ln -sf $SCRIPT_PATH/.alacritty.toml /home/$USER/.alacritty.toml

echo "linking hyprland config file..."
mkdir -p /home/$USER/.config/hypr
ln -sf $SCRIPT_PATH/.config/hypr/hyprland.conf /home/$USER/.config/hypr/hyprland.conf

echo "linking hyprlock config file..."
ln -sf $SCRIPT_PATH/.config/hypr/hyprlock.conf /home/$USER/.config/hypr/hyprlock.conf

echo "linking waybar config files..."
mkdir -p /home/$USER/.config/waybar
ln -sf $SCRIPT_PATH/.config/waybar/config /home/$USER/.config/waybar/config
ln -sf $SCRIPT_PATH/.config/waybar/modules.json /home/$USER/.config/waybar/modules.json
ln -sf $SCRIPT_PATH/.config/waybar/runrofi.sh /home/$USER/.config/waybar/runrofi.sh
ln -sf $SCRIPT_PATH/.config/waybar/style.css /home/$USER/.config/waybar/style.css

echo "linking waypaper config file..."
mkdir -p /home/$USER/.config/waypaper
ln -sf $SCRIPT_PATH/.config/waypaper/config.ini /home/$USER/.config/waypaper/config.ini

echo "copying wallpaper folder..."
cp -r $SCRIPT_PATH/wallpapers/ /home/$USER/Bilder/wallpapers

echo "linking kitty config file..."
mkdir -p /home/$USER/.config/kitty
ln -sf $SCRIPT_PATH/.config/kitty/kitty.conf /home/$USER/.config/kitty/kitty.conf

echo "linking rofi config file..."
mkdir -p /home/$USER/.config/rofi
ln -sf $SCRIPT_PATH/.config/rofi/config.rasi /home/$USER/.config/rofi/config.rasi

echo "linking scripts..."
ln -sf $SCRIPT_PATH/.scripts /home/$USER/.scripts
