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
# set -x #echo on

echo "linking .zshrc..."
ln -sf $SCRIPT_PATH/.zshrc /home/$USER/.zshrc

echo "linking .vimrc..."
ln -sf $SCRIPT_PATH/.vimrc /home/$USER/.vimrc

# install vim plugins and colors
mkdir -p ~/.vim
mkdir -p ~/.vim/bundle
mkdir -p ~/.vim/bundle/ale
mkdir -p ~/.vim/bundle/Vundle.vim
git clone https://github.com/dense-analysis/ale ~/.bundle/ale
git clone https://github.com/VundleVim/Vundle.vim ~/.bundle/Vundle.vim
git clone https://github.com/gosukiwi/vim-atom-dark
cp -r vim-atom-dark/colors ~/.vim/

echo "linking .alacritty.toml..."
ln -sf $SCRIPT_PATH/.alacritty.toml /home/$USER/.alacritty.toml

echo "linking hyprland config file..."
mkdir -p /home/$USER/.config/hypr
ln -sf $SCRIPT_PATH/.config/hypr/hyprland.conf /home/$USER/.config/hypr/hyprland.conf
ln -sf $SCRIPT_PATH/.config/hypr/windowrules.conf /home/$USER/.config/hypr/windowrules.conf
ln -sf $SCRIPT_PATH/.config/hypr/adaptive_theme.conf /home/$USER/.config/hypr/adaptive_theme.conf

#echo "linking hyprlock config file..."
#ln -sf $SCRIPT_PATH/.config/hypr/hyprlock.conf /home/$USER/.config/hypr/hyprlock.conf

echo "linking waybar config files..."
mkdir -p /home/$USER/.config/waybar
ln -sf $SCRIPT_PATH/.config/waybar/config /home/$USER/.config/waybar/config
ln -sf $SCRIPT_PATH/.config/waybar/modules.json /home/$USER/.config/waybar/modules.json
ln -sf $SCRIPT_PATH/.config/waybar/runrofi.sh /home/$USER/.config/waybar/runrofi.sh
ln -sf $SCRIPT_PATH/.config/waybar/style.css /home/$USER/.config/waybar/style.css
ln -sf $SCRIPT_PATH/.config/color_palette.css /home/$USER/.config/waybar/color_palette.css
ln -sf $SCRIPT_PATH/.config/color_palette.css /home/$USER/.config/wlogout/color_palette.css

echo "linking swayosd config files..."
ln -sf $SCRIPT_PATH/.config/swayosd /home/$USER/.config/
ln -sf $SCRIPT_PATH/.config/color_palette.css /home/$USER/.config/swayosd/color_palette.css


# echo "linking waypaper config file..."
# mkdir -p /home/$USER/.config/waypaper
# ln -sf $SCRIPT_PATH/.config/waypaper/config.ini /home/$USER/.config/waypaper/config.ini

echo "copying wallpaper folder..."
cp -r $SCRIPT_PATH/wallpapers/ /home/$USER/Bilder/

echo "linking waypaper config..."
ln -sf $SCRIPT_PATH/.config/waypaper/ /home/$USER/.config/

echo "linking kitty config file..."
mkdir -p /home/$USER/.config/kitty
ln -sf $SCRIPT_PATH/.config/kitty/kitty.conf /home/$USER/.config/kitty/kitty.conf

VSCode_flatpak_config_path=.var/app/com.visualstudio.code/config/Code/User
VSCode_std_config_path=.config/Code/User

echo "linking vs Code config file..."
if [ -d "/home/$USER/$VSCode_flatpak_config_path" ]; then
    ln -sf $SCRIPT_PATH/.config/VSCode/settings.json /home/$USER/$VSCode_flatpak_config_path/settings.json
    echo "VSCode flatpak config file detected."
elif [ -d "/home/$USER/$VSCode_std_config_path" ]; then
    ln -sf $SCRIPT_PATH/.config/VSCode/settings.json /home/$USER/$VSCode_std_config_path/settings.json
    echo "VSCode config file in ~/.config/Code/User detected."
else
    echo "VSCode settings.json not found. Is VSCode installed?"
fi

echo "linking rofi config file..."
ln -sf $SCRIPT_PATH/.config/rofi /home/$USER/.config/

echo "linking scripts..."
ln -sf $SCRIPT_PATH/.scripts /home/$USER/

echo "linking wlogout config files..."
ln -sf $SCRIPT_PATH/.config/wlogout /home/$USER/.config/

echo "linking Kvantum config and theme files..."
ln -sf $SCRIPT_PATH/.config/Kvantum /home/$USER/.config/