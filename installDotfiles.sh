#!/bin/bash

# this script installs the schmynth dotfiles
# currently tracked config files are:
# .zshrc
# hyprland
# hyprlock
# waybar
# waypaper

# find full path of script:
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
set -x #echo on

echo "linking .zshrc..."
ln -s $SCRIPT_PATH/.zshrc /home/$USER/.zshrc

echo "linking hyprland config file..."
mkdir -p /home/$USER/hypr
ln -s $SCRIPT_PATH/.config/hypr/hyprland.conf /home/$USER/.conf/hypr/hyprland.conf

echo "linking hyprlock config file..."
ln -s $SCRIPT_PATH/.config/hypr/hyprlock.conf /home/$USER/.conf/hypr/hyprlock.conf

echo "linking waybar config files..."
mkdir -p /home/$USER/waybar
ln -s $SCRIPT_PATH/.config/waybar/config /home/$USER/.config/waybar/config

echo "linking waypaper config file..."
mkdir -p /home/$USER/waypaper
ln -s $SCRIPT_PATH/.config/waypaper/config.ini /home/$USER/.config/waypaper/config.ini

echo "copying wallpaper folder..."
cp -r $SCRIPT_PATH/wallpapers/ /home/$USER/Bilder/wallpapers

echo "linking kitty config file..."
mkdir -p /home/$USER/.config/kitty
ln -s $SCRIPT_PATH/.config/kitty/kitty.conf /home/$USER/.config/kitty/kitty.conf
