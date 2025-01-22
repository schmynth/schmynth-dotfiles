#!/bin/bash

#Remove orphans
pamac remove --orphans

#clean cache
pamac clean --keep 2
pamac clean --build-files

# Delete cache not modified for 20 days
find ~/.cache -depth -type f -mtime +20 -delete

#clean Journals
sudo journalctl --vacuum-time=20d

#Remove all pkg from cache except those installed
sudo pacman -Sc

#Remove ALL pkg from cache
#sudo pacman -Scc

#remove cache from uninstalled packages
paccache -ruk0

#Clean home cache! ~/.cache
