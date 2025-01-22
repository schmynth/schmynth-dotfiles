#!/bin/bash

set -x
# install pacman packages
sudo pacman -S - < .packagesPacman

# install yay
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
yay -S --needed - < .packagesAUR 
