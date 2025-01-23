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

git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
